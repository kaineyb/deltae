import pandas as pd
import deltae

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

    de2000_results = deltae.DeltaE2000(rds_Lab1, rds_Lab2, test=True)

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
