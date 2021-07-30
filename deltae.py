import math


def delta_e_1976(Lab1, Lab2):
    """
    Takes Lab values as a dictionary and outputs a DeltaE1976 calculation

    Example Dictionarys:
    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}
    """

    delL = Lab1['L'] - Lab2['L']
    dela = Lab1['a'] - Lab2['a']
    delb = Lab1['b'] - Lab2['b']
    result = math.sqrt(delL * delL + dela * dela + delb * delb)
    return result


def delta_e_2000(Lab1, Lab2, verbose=False, test=False, formula='Rochester'):
    """
    Takes Lab values as a dictionary and outputs a DeltaE2000 calculation

    Example Dictionarys:
    Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
    Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}

    #verbose=True

    Prints out all of the calculations that comes up with the deltaE2000.

    #test=True

    Returns all of the calculations that comes up with the deltaE2000 in the below order:
    a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, DE2000

    formula kwarg can be 'Rochester' or 'Bruce'. 

    Rochester uses a different calculation for hPrime, h1Prime, h2Prime and hBarPrime than Bruce
    Read the white paper by Gaurav Sharma, Wencheng Wu and Endul N. Dala (http://www2.ece.rochester.edu/~gsharma/ciede2000/ciede2000noteCRNA.pdf)
    """

    kL = 1.0
    kC = 1.0
    kH = 1.0
    lBarPrime = 0.5 * (Lab1['L'] + Lab2['L'])
    c1 = math.sqrt(Lab1['a'] * Lab1['a'] + Lab1['b'] * Lab1['b'])
    c2 = math.sqrt(Lab2['a'] * Lab2['a'] + Lab2['b'] * Lab2['b'])
    cBar = 0.5 * (c1 + c2)
    cBar7 = cBar**7
    g = 0.5 * (1.0 - math.sqrt(cBar7 / (cBar7 + 25**7)))  # 25**7 or 6103515625

    a1Prime = Lab1['a'] * (1.0 + g)
    a2Prime = Lab2['a'] * (1.0 + g)

    c1Prime = math.sqrt(a1Prime * a1Prime + Lab1['b'] * Lab1['b'])
    c2Prime = math.sqrt(a2Prime * a2Prime + Lab2['b'] * Lab2['b'])

    cBarPrime = 0.5 * (c1Prime + c2Prime)

    if formula == 'Rochester':
        # Rochester hPrime
        def hPrime(B_i_star, aiPrime):
            if B_i_star == 0 and aiPrime == 0:
                return 0
            else:
                hPrime = math.atan2(B_i_star, aiPrime) * 180 / math.pi
                if hPrime < 0:
                    hPrime += 360
                return hPrime

        # Gets h1 and h2 Primes
        h1Prime = hPrime(Lab1['b'], a1Prime)
        h2Prime = hPrime(Lab2['b'], a2Prime)

        # START Rochester hBarprime
        if abs(h1Prime - h2Prime) <= 180 and c1Prime * c2Prime != 0:
            hBarPrime = (h1Prime + h2Prime) / 2

        elif abs(h1Prime - h2Prime) > 180 and (h1Prime + h2Prime) < 360 and c1Prime * c2Prime != 0:
            hBarPrime = (h1Prime + h2Prime + 360) / 2

        elif abs(h1Prime - h2Prime) > 180 and (h1Prime + h2Prime) >= 360 and c1Prime * c1Prime != 0:
            hBarPrime = (h1Prime + h2Prime - 360) / 2

        elif (c1Prime * c2Prime) == 0:
            hBarPrime = (h1Prime + h2Prime)
        # END Rochester hBarprime

    elif formula == 'Bruce':

        # Bruces hPrimes
        h1Prime = (math.atan2(Lab1['b'], a1Prime) * 180.0) / math.pi

        if (h1Prime < 0.0):
            h1Prime += 360.0

        h2Prime = (math.atan2(Lab2['b'], a2Prime) * 180.0) / math.pi

        if (h2Prime < 0.0):
            h2Prime += 360.0

        # Bruces hBarPrime
        hBarPrime = 0.5 * (h1Prime + h2Prime + 360.0) if abs(h1Prime -
                                                             h2Prime) > 180.0 else 0.5 * (h1Prime + h2Prime)

    t = 1.0 - 0.17 * math.cos((math.pi * (hBarPrime - 30.0)) / 180.0) + 0.24 * math.cos((math.pi * (2.0 * hBarPrime)) / 180.0) + \
        0.32 * math.cos((math.pi * (3.0 * hBarPrime + 6.0)) / 180.0) - \
        0.2 * math.cos((math.pi * (4.0 * hBarPrime - 63.0)) / 180.0)

    if (abs(h2Prime - h1Prime) <= 180.0):
        dhPrime = h2Prime - h1Prime

    else:
        dhPrime = h2Prime - h1Prime + \
            360.0 if h2Prime <= h1Prime else h2Prime - h1Prime - 360.0

    dLPrime = Lab2['L'] - Lab1['L']
    dCPrime = c2Prime - c1Prime
    dHPrime = 2.0 * math.sqrt(c1Prime * c2Prime) * \
        math.sin((math.pi * (0.5 * dhPrime)) / 180.0)

    sL = 1.0 + (0.015 * (lBarPrime - 50.0) * (lBarPrime - 50.0)) / \
        math.sqrt(20.0 + (lBarPrime - 50.0) * (lBarPrime - 50.0))

    sC = 1.0 + 0.045 * cBarPrime
    sH = 1.0 + 0.015 * cBarPrime * t

    dTheta = 30.0 * math.exp(-((hBarPrime - 275.0) / 25.0)
                             * ((hBarPrime - 275.0) / 25.0))

    cBarPrime7 = cBarPrime**7

    rC = math.sqrt(cBarPrime7 / (cBarPrime7 + 6103515625.0))
    rT = -2.0 * rC * math.sin((math.pi * (2.0 * dTheta)) / 180.0)

    DE2000 = math.sqrt((dLPrime / (kL * sL)) * (dLPrime / (kL * sL)) + (dCPrime / (kC * sC)) * (dCPrime / (kC * sC)) +
                       (dHPrime / (kH * sH)) * (dHPrime / (kH * sH)) + (dCPrime / (kC * sC)) * (dHPrime / (kH * sH)) * rT)

    # If arbitury Keyword arg verbose=True then print out the below
    if verbose == True:

        decoration = '-'*20

        print(decoration)
        print('LAB Value Input')
        print(decoration)
        print(f"LAB1: {Lab1['L']}, {Lab1['a']}, {Lab1['b']}")
        print(f"LAB2: {Lab2['L']}, {Lab2['a']}, {Lab2['b']}")
        print(decoration)
        print('Outputs')
        print(decoration)
        print(f'a1Prime: {round(a1Prime, 4)}')
        print(f'a2Prime: {round(a2Prime, 4)}')
        print(decoration)
        print(f'cBar: {round(cBar, 4)}')
        print(f'cBar7: {round(cBar7, 4)}')
        print(decoration)
        print(f'c1Prime: {round(c1Prime, 4)}')
        print(f'c2Prime: {round(c2Prime, 4)}')
        print(decoration)
        print(f'h1Prime: {round(h1Prime, 4)}')
        print(f'h2Prime: {round(h2Prime, 4)}')
        print(decoration)
        print(f'(abs)h1Prime - h2Prime: {round(abs(h1Prime - h2Prime), 4)}')
        print(decoration)
        print(f'hBarPrime: {round(hBarPrime, 4)}')
        print(f'g: {round(g, 4)}')
        print(f't: {round(t, 4)}')
        print(f'sL: {round(sL, 4)}')
        print(f'sC: {round(sC, 4)}')
        print(f'sH: {round(sH, 4)}')
        print(f'rT: {round(rT, 4)}')
        print(decoration)
        print(f'DE2000: {round(DE2000, 4)}')

    if test == True:
        return a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, DE2000

    else:
        return DE2000


def delta_e_2000_test():
    """
    Tests the delta_e_2000() function against the Rochester dataset, using the Rochester formula.
    Which is different to Bruce Lindbloom
    """
    import pandas as pd

    CSV = 'rochester_data.csv'
    Rds_df = pd.read_csv(CSV)

    FAILURES = 0

    print('-'*20)
    print('Testing Dataset: ', CSV)
    print('-'*20)

    for index, row in Rds_df.iterrows():
        rds_pair = row['Pair']
        rds_Lab1 = {'L': row['L1'], 'a': row['A1'], 'b': row['B1']}
        rds_Lab2 = {'L': row['L2'], 'a': row['A2'], 'b': row['B2']}
        rds_a1Prime = row['a1Prime']
        rds_a2Prime = row['a2Prime']
        rds_c1Prime = row['c1Prime']
        rds_c2Prime = row['c2Prime']
        rds_h1Prime = row['h1Prime']
        rds_h2Prime = row['h2Prime']
        rds_hBarPrime = row['hBarPrime']
        rds_g = row['G']
        rds_t = row['T']
        rds_sL = row['sL']
        rds_sC = row['sC']
        rds_sH = row['sH']
        rds_rT = row['rT']
        rds_de2000 = row['DE2000']

        de2000_results = delta_e_2000(
            rds_Lab1, rds_Lab2, test=True, formula='Rochester')

        a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, \
            hBarPrime, g, t, sL, sC, sH, rT, de2000 = de2000_results

        conditions = {
            'a1Prime': (a1Prime, rds_a1Prime),
            'a2Prime': (a2Prime, rds_a2Prime),
            'c1Prime': (c1Prime, rds_c1Prime),
            'c2Prime': (c2Prime, rds_c2Prime),
            'h1Prime': (h1Prime, rds_h1Prime),
            'h2Prime': (h2Prime, rds_h2Prime),
            'hBarPrime': (hBarPrime, rds_hBarPrime),
            'g': (g, rds_g),
            't': (t, rds_t),
            'sL': (sL, rds_sL),
            'sC': (sC, rds_sC),
            'sH': (sH, rds_sH),
            'rT': (rT, rds_rT),
            'de2000': (de2000, rds_de2000),
        }

        for key, value in conditions.items():
            test = round(value[0], 4) == round(value[1], 4)
            if not test:
                FAILURES += 1
                print('Pair', int(rds_pair), '| Failed |', key, '(Result:',
                      round(value[0], 4), 'Dataset:', round(value[1], 4), ')')

    if FAILURES == 0:

        print('-'*20)
        print('Test successful with :', FAILURES, 'errors.')
        print('-'*20)

    else:
        print('-'*20)
        print('Test failed with :', FAILURES, 'errors.')
        print('-'*20)


def delta_e_2000_test_pair(pair):
    """
    Analyse a specific pair in the Rochester Dataset.
    Returns delta_e_2000(lab1, lab2, verbose=True)
    """

    import pandas as pd

    CSV = 'rochester_data.csv'
    Rds_df = pd.read_csv(CSV)

    Rds_df = Rds_df.set_index('Pair')

    def get_pair(pair_number):

        l_1 = Rds_df.loc[pair_number, 'L1']
        a_1 = Rds_df.loc[pair_number, 'A1']
        b_1 = Rds_df.loc[pair_number, 'B1']
        l_2 = Rds_df.loc[pair_number, 'L2']
        a_2 = Rds_df.loc[pair_number, 'A2']
        b_2 = Rds_df.loc[pair_number, 'B2']

        rds_lab1 = {'L': l_1, 'a': a_1, 'b': b_1}
        rds_lab2 = {'L': l_2, 'a': a_2, 'b': b_2}

        return rds_lab1, rds_lab2

    # change get_pair(x) to a pair you want to see the results of verbosley.
    lab1, lab2 = get_pair(pair)

    return delta_e_2000(lab1, lab2, verbose=True)


if __name__ == '__main__':
    delta_e_2000_test()
