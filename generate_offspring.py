import pandas as pd
import numpy as np

# paths to 23andMe raw data to be used for child generation
PATH_ONE = './v2.txt'
PATH_TWO = './v5.txt'


def load_and_clean_data():
    """Load and clean 23andMe raw data at PATH_ONE and PATH_TWO"""

    def file2pd(path):

        # load a data file, remove comments, convert to list
        f = open(path, 'r').read().replace('# rsid', 'rsid').split('\n')
        f = [x for x in f if len(x) and x[0] != '#']

        # get column names and values
        cols = f[0].split('\t')
        f = [x.split('\t') for x in f[1:]]

        # convert to DataFrame, convert position column to int
        df = pd.DataFrame(f, columns=cols)
        df['position'] = df['position'].astype(np.int64)

        return df

    return [file2pd(PATH_ONE), file2pd(PATH_TWO)]

# oh no our rsids barely overlap

# def combine_data_frames(data):
#
#     data[0] = data[0].rename(columns={'genotype':'genotype0'})
#     data[1] = data[1].rename(columns={'genotype':'genotype1'})
#
#     data = pd.merge(data[0], data[1], how='outer')