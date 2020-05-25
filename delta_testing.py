import pandas as pd
import deltae

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
lab1, lab2 = get_pair(33)

deltae.DeltaE2000(lab1, lab2, verbose=True)
