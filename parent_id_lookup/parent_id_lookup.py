'''
    Merge multiple rows from same dataframe based on parent id

    I have a dataframe where some rows have a parent-child relationship. For example, 1002 is the parent of 1003, 1003
    is the parent of 1004. I want to merge the rows to keep only those rows without child item. However, some
    information appear only in the parent row but missing from child rows, e.g. column 'B' from 1002. I want to
    inherit it to the latest child row.

    https://stackoverflow.com/questions/58073380/merge-multiple-rows-from-same-dataframe-based-on-parent-id
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['Id', 'Parent Id', 'Child Id', 'A', 'B'],
                  data=[[1001, np.nan, 1004, 'A1001', 'B1001'],
                        [1004, 1003, np.nan, 'A1004', np.nan],
                        [1003, 1002, 1004, 'A1003', np.nan],
                        [1002, np.nan, 1003, 'A1002', 'B1002'],
                        [1005, 1001, np.nan, 'A1005', np.nan]
                        ])
print(df)
#      Id  Parent Id  Child Id      A      B
# 0  1001        NaN    1004.0  A1001  B1001
# 1  1004     1003.0       NaN  A1004    NaN
# 2  1003     1002.0    1004.0  A1003    NaN
# 3  1002        NaN    1003.0  A1002  B1002
# 4  1005     1001.0       NaN  A1005    NaN

for i in range(len(df)):
    df = df.merge(df[['Id', 'B']].rename({'Id': 'Parent Id', 'B': 'Parent B'}, axis=1), how='left')
    df['B'] = df['B'].combine_first(df['Parent B'])
    df.drop('Parent B', axis=1, inplace=True)
print(df)
#      Id  Parent Id  Child Id      A      B
# 0  1001        NaN    1004.0  A1001  B1001
# 1  1004     1003.0       NaN  A1004  B1002
# 2  1003     1002.0    1004.0  A1003  B1002
# 3  1002        NaN    1003.0  A1002  B1002
# 4  1005     1001.0       NaN  A1005  B1001

df = df[df['Child Id'].isnull()]
print(df)
#      Id  Parent Id  Child Id      A      B
# 1  1004     1003.0       NaN  A1004  B1002
# 4  1005     1001.0       NaN  A1005  B1001
