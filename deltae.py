import math

# Takes Lab values as a dictionary
# Like the example below:

# Lab1 = {'L': 50.00, 'a': 2.6772, 'b': -79.7751}
# Lab2 = {'L': 50.00, 'a': 0.00, 'b': -82.7485}


def DeltaE1976(Lab1, Lab2):
    delL = Lab1['L'] - Lab2['L']
    dela = Lab1['a'] - Lab2['a']
    delb = Lab1['b'] - Lab2['b']
    result = math.sqrt(delL * delL + dela * dela + delb * delb)
    result = round(result, 6)
    print('DeltaE1975: ' + str(result))
    return result


def DeltaE2000(Lab1, Lab2, verbose=False, test=False):
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

    # Bruces hPrimes
    # h1Prime = (math.atan2(Lab1['b'], a1Prime) * 180.0) / math.pi

    # if (h1Prime < 0.0):
    #     h1Prime += 360.0

    # h2Prime = (math.atan2(Lab2['b'], a2Prime) * 180.0) / math.pi

    # if (h2Prime < 0.0):
    #     h2Prime += 360.0

    # Bruces hBarPrime
    # hBarPrime = 0.5 * (h1Prime + h2Prime + 360.0) if abs(h1Prime -
    #                                                      h2Prime) > 180.0 else 0.5 * (h1Prime + h2Prime)

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
        print('-'*20)
        print('LAB Values')
        print('-'*20)
        print('LAB1: ' + str(Lab1['L']) + ', ' +
              str(Lab1['a']) + ', ' + str(Lab1['b']))
        print('LAB2: ' + str(Lab2['L']) + ', ' +
              str(Lab2['a']) + ', ' + str(Lab2['b']))

        print('-'*20)
        print('Tests')
        print('-'*20)
        print('a1Prime: ' + str(round(a1Prime, 4)))
        print('a2Prime: ' + str(round(a2Prime, 4)))
        print('-'*20)
        print('cBar: ' + str(round(cBar, 4)))
        print('cBar7: ' + str(round(cBar7, 4)))
        print('-'*20)
        print('c1Prime: ' + str(round(c1Prime, 4)))
        print('c2Prime: ' + str(round(c2Prime, 4)))
        print('-'*20)
        print('h1Prime: ' + str(round(h1Prime, 4)))
        print('h2Prime: ' + str(round(h2Prime, 16)))
        print('-'*20)
        print('(abs)h1Prime - h2Prime: ', round(abs(h1Prime - h2Prime), 4))
        print('-'*20)
        print('hBarPrime: ' + str(round(hBarPrime, 4)))
        print('g: ' + str(round(g, 4)))
        print('t: ' + str(round(t, 4)))
        print('sL: ' + str(round(sL, 4)))
        print('sC: ' + str(round(sC, 4)))
        print('sH: ' + str(round(sH, 4)))
        print('rT: ' + str(round(rT, 4)))
        print('-'*20)
        print('DE2000: ' + str(round(DE2000, 4)))

    if test == True:
        return a1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, DE2000

    else:
        return DE2000
