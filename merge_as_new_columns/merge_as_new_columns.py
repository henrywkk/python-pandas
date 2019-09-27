'''
Problem:
Merge dataframes on 1 column for which the output to be an extra column instead of a new row
'''
import pandas as pd

df1 = pd.DataFrame({'A': ['A0'],
                     'B': ['B0']})

df2 = pd.DataFrame({'A': ['A0', 'A0'],
                     'C': ['C4', 'C5']})
print(df1)
#     A   B
# 0  A0  B0
print(df2)
#     A   C
# 0  A0  C4
# 1  A0  C5

'''
Solution:
Create unique values of column A in df2 by MultiIndex by DataFrame.set_index with counter column by GroupBy.cumcount, 
reshape by Series.unstack and flatten Multiindex by map with join
'''
df2 = df2.set_index(['A', df2.groupby('A').cumcount().add(1).astype(str)]).unstack()
df2.columns = df2.columns.map('_'.join)
df2 = df2.reset_index()
print (df2)
#     A C_1 C_2
# 0  A0  C4  C5

df = df1.merge(df2, on = 'A', how = 'left')
print (df)
#     A   B C_1 C_2
# 0  A0  B0  C4  C5
