# Examples to select rows from a dataframe based on the values in a column
# reference:
# https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
                   'B': 'one one two three two two one three'.split(),
                   'C': np.arange(8), 'D': np.arange(8) * 2})
print(df)
#      A      B  C   D
# 0  foo    one  0   0
# 1  bar    one  1   2
# 2  foo    two  2   4
# 3  bar  three  3   6
# 4  foo    two  4   8
# 5  bar    two  5  10
# 6  foo    one  6  12
# 7  foo  three  7  14

# To select rows whose column value equals a scalar, some_value, use ==:
# df.loc[df['column_name'] == some_value]
print("====Example 1====")
print(df.loc[df['A'] == 'foo'])
#      A      B  C   D
# 0  foo    one  0   0
# 2  foo    two  2   4
# 4  foo    two  4   8
# 6  foo    one  6  12
# 7  foo  three  7  14

# To select rows whose column value is in an iterable, some_values, use isin:
print("==== Example 2====")
print(df.loc[df['B'].isin(['one', 'three'])])
#      A      B  C   D
# 0  foo    one  0   0
# 1  bar    one  1   2
# 3  bar  three  3   6
# 6  foo    one  6  12
# 7  foo  three  7  14

# Note, however, that if you wish to do this many times,
# it is more efficient to make an index first, and then use df.loc:
df = df.set_index(['B'])
print("==== Example 3====")
print(df.loc['one'])
#        A  C   D
# B
# one  foo  0   0
# one  bar  1   2
# one  foo  6  12
# or, to include multiple values from the index use df.index.isin:
df.loc[df.index.isin(['one', 'two'])]
print("==== Example 4====")
print(df)
#     A  C   D
# B
# one  foo  0   0
# one  bar  1   2
# two  foo  2   4
# two  foo  4   8
# two  bar  5  10
# one  foo  6  12
