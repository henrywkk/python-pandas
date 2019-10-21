# Transpose dataframe columns based on a column's value
# https://stackoverflow.com/questions/58480479
import pandas as pd

# param       per     per_date    per_num
# 0   XYZ         1.0     2018-10-01  11.0
# 1   XYZ         2.0     2017-08-01  15.25
# 2   XYZ         3.0     2019-10-01  11.25
# 3   MMG         1.0     2019-08-01  15.71
# 4   MMG         2.0     2020-10-01  11.50
# 5   MMG         3.0     2021-10-01  11.75
# 6   MMG         4.0     2014-01-01  14.00
df = pd.DataFrame(columns=["param", "per", "per_date", "per_num"],
                  data=[["XYZ", 1, "10/1/2018", 11],
                        ["XYZ", 2, "8/1/2017", 15.25],
                        ["XYZ", 3, "10/1/2019", 11.25],
                        ["MMG", 1, "8/1/2019", 15.71],
                        ["MMG", 2, "10/1/2020", 11.5],
                        ["MMG", 3, "10/1/2021", 11.75],
                        ["MMG", 4, "1/1/2014", 14]])

# Use GroupBy.cumcount for counter and reshape by DataFrame.unstack, last flatten columns names by f-strings
df = df.set_index(['param', df.groupby('param').cumcount().add(1)]).unstack()
df.columns = [f'{a}_{b}' for a, b in df.columns]
df = df.reset_index()
print(df)
#  param per_1  per_2   per_3   per_4 per_date_1 per_date_2 per_date_3 per_date_4 per_num_1 per_num_2 per_num_3 per_num_4
# 0 XYZ   1      2       3       NaN  2018-10-01 2017-08-01 2019-10-01 NaN        11.0      15.25     11.25     NaN
# 1 MMG   1      2       3       4    2019-08-01 2020-10-01 2021-10-01 2014-01-01 15.71     11.50     11.75     14.00
