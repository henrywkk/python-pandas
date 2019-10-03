import datetime
from datetime import timedelta

import numpy as np
import pandas as pd

df = pd.DataFrame(columns=['timestamp', 'Price'],
                  data=[[datetime.datetime(2019, 9, 29, 15, 33, 00), 14],
                        [datetime.datetime(2019, 9, 29, 15, 34, 00), 15],
                        [datetime.datetime(2019, 9, 29, 15, 35, 00), 14],
                        [datetime.datetime(2019, 9, 29, 15, 36, 00), 17],
                        [datetime.datetime(2019, 9, 29, 15, 37, 00), 20],
                        ])
print(df)
#             timestamp  Price
# 0 2019-09-29 15:33:00     14
# 1 2019-09-29 15:34:00     15
# 2 2019-09-29 15:35:00     14
# 3 2019-09-29 15:36:00     17
# 4 2019-09-29 15:37:00     20
# 
# source: https://stackoverflow.com/questions/58211168/pandas-populate-cell-with-next-conditional-value-based-off-multiple-columns
# I'm trying to backtest a strategy, and so I want to populate the Exit price column with a subsequent value of the
# price column, when the first row with any of the following conditions is met:
#
# 1. The time difference between current row timestamp and the comparison timestamp is greater or equal to X minutes.
# 2. The percentage difference between current row price and comparison row price is greater than Y percent
#
# So for example, if the number of minutes is 2 and the return is 10% , the table should populated as follows:
#
#     timestamp                    Price      Exit Price
# 1   2019-09-29 15:33:00          14         14<-- From Row 3 because 2 minutes passed
# 2   2019-09-29 15:34:00          15         17<-- From Row 4, both conditions satisfied
# 3   2019-09-29 15:35:00          14         17<-- From Row 4, difference greater than 10%
# 4   2019-09-29 15:36:00          17         20
# 5   2019-09-29 15:37:00          20         Nan
E_Price = []
time_diff = df['timestamp'].apply(lambda x: x >= (df['timestamp'] + timedelta(minutes=2)))
print(time_diff)
#        0      1      2      3      4
# 0  False  False  False  False  False
# 1  False  False  False  False  False
# 2   True  False  False  False  False
# 3   True   True  False  False  False
# 4   True   True   True  False  False
price_diff = df['Price'].apply(lambda x: x >= (df['Price'] * 1.1))
print(price_diff)
#        0      1      2      3      4
# 0  False  False  False  False  False
# 1  False  False  False  False  False
# 2  False  False  False  False  False
# 3   True   True   True  False  False
# 4   True   True   True   True  False
for i in range(len(df)):
    check = (time_diff | price_diff)[i]
    ind = check.idxmax()
    val = df.iloc[ind, 1] if ind != 0 else np.nan
    E_Price.append(val)

df['Exit_Price'] = E_Price
print(df)
# Output
#             timestamp  Price  Exit_Price
# 0 2019-09-29 15:33:00     14        14.0
# 1 2019-09-29 15:34:00     15        17.0
# 2 2019-09-29 15:35:00     14        17.0
# 3 2019-09-29 15:36:00     17        20.0
# 4 2019-09-29 15:37:00     20         NaN
