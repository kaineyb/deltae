def delta_e_2000_test_builder():
    """
    Outputs Conditions to use in unit testing
    """
    import pandas as pd

    CSV = 'rochester_data.csv'
    Rds_df = pd.read_csv(CSV)

    with open('test.py', 'w') as f:

        f.write(f'import deltae\n')
        f.write(f'import unittest\n')
        f.write(f'class TestDeltaE2000(unittest.TestCase):\n\n')

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

            conditions = {
                'a1Prime': rds_a1Prime,
                'a2Prime': rds_a2Prime,
                'c1Prime': rds_c1Prime,
                'c2Prime': rds_c2Prime,
                'h1Prime': rds_h1Prime,
                'h2Prime': rds_h2Prime,
                'hBarPrime': rds_hBarPrime,
                'g': rds_g,
                't': rds_t,
                'sL': rds_sL,
                'sC': rds_sC,
                'sH': rds_sH,
                'rT': rds_rT,
                'de2000': rds_de2000
            }

            f.write(f'\tdef test_pair_{int(rds_pair)}(self):\n')
            f.write(f'\t\t""" Tests Pair {int(rds_pair)} """\n')
            f.write(f'\t\t# Pair {int(rds_pair)}\n')
            f.write(
                f"\t\tLab1 = {{'L': {rds_Lab1['L']}, 'a': {rds_Lab1['a']}, 'b': {rds_Lab1['b']}}}\n")
            f.write(
                f"\t\tLab2 = {{'L': {rds_Lab2['L']}, 'a': {rds_Lab2['a']}, 'b': {rds_Lab2['b']}}}\n\n")

            f.write(f"\t\ta1Prime, a2Prime, c1Prime, c2Prime, h1Prime, h2Prime, hBarPrime, g, t, sL, sC, sH, rT, de2000=deltae.delta_e_2000(Lab1, Lab2, test=True, formula='Rochester')\n\n")

            for key, value in conditions.items():
                f.write(f'\t\tself.assertEqual({key}, {value})\n')  # {value}

            f.write(f'\n\n')
        f.write(f"if __name__ == '__main__':\n")
        f.write(f'\tunittest.main()\n')

        print("File Saved")


if __name__ == '__main__':
    delta_e_2000_test_builder()
