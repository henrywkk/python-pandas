# Add aggregated/summary lines in Pandas dataframe
import pandas as pd

df = pd.DataFrame(data=[[2018, 'R1', 'C1', 1],
                        [2018, 'R1', 'C2', 2],
                        [2018, 'R1', 'C3', 3],
                        [2018, 'R1', 'C4', 4],
                        [2018, 'R1', 'C5', 5],
                        [2018, 'R2', 'C6', 6],
                        [2018, 'R2', 'C7', 7],
                        [2018, 'R2', 'C8', 8],
                        [2018, 'R2', 'C9', 9],
                        [2018, 'R2', 'C10', 10]],
                  columns=['Year', 'Region', 'Country', 'Spend'])
print(df)
# df
#    Year Region Country  Spend
# 0  2018     R1      C1      1
# 1  2018     R1      C2      2
# 2  2018     R1      C3      3
# 3  2018     R1      C4      4
# 4  2018     R1      C5      5
# 5  2018     R2      C6      6
# 6  2018     R2      C7      7
# 7  2018     R2      C8      8
# 8  2018     R2      C9      9
# 9  2018     R2     C10     10
df2 = df.groupby(['Year'])['Spend'].sum().reset_index()
df3 = df.groupby(['Year', 'Region'])['Spend'].sum().reset_index()
df = pd.concat([df, df2, df3], sort=False).fillna('All').sort_values(by=['Region', 'Country'])
# df2
#    Year  Spend
# 0  2018     55
#
# df3
#    Year Region  Spend
# 0  2018     R1     15
# 1  2018     R2     40
#
# df
#    Year Region Country  Spend
# 0  2018    All     All     55
# 0  2018     R1     All     15
# 0  2018     R1      C1      1
# 1  2018     R1      C2      2
# 2  2018     R1      C3      3
# 3  2018     R1      C4      4
# 4  2018     R1      C5      5
# 1  2018     R2     All     40
# 9  2018     R2     C10     10
# 5  2018     R2      C6      6
# 6  2018     R2      C7      7
# 7  2018     R2      C8      8
# 8  2018     R2      C9      9
