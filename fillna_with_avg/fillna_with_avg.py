import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['Month', 'Dayname', 'Class', 'Val1', 'Val2'],
                  data=[['Sep', 'Mon', 'A', 1, 2],
                        ['Sep', 'Mon', 'B', 3, 4],
                        ['Sep', 'Tue', 'A', 7, 5],
                        ['Oct', 'Mon', 'F', 5, 2],
                        ['Oct', 'Fri', 'K', 2, 8],
                        ['Oct', 'Fri', 'F', 7, 3],
                        ['Sep', 'Mon', 'A', np.nan, np.nan],
                        ['Sep', 'Mon', 'B', np.nan, np.nan],
                        ['Oct', 'Fri', 'F', np.nan, np.nan]])
print(df)
#   Month Dayname Class  Val1  Val2
# 0   Sep     Mon     A   1.0   2.0
# 1   Sep     Mon     B   3.0   4.0
# 2   Sep     Tue     A   7.0   5.0
# 3   Oct     Mon     F   5.0   2.0
# 4   Oct     Fri     K   2.0   8.0
# 5   Oct     Fri     F   7.0   3.0
# 6   Sep     Mon     A   NaN   NaN
# 7   Sep     Mon     B   NaN   NaN
# 8   Oct     Fri     F   NaN   NaN

# Drawback: sorted
df2 = df.groupby(['Month', 'Dayname']).apply(lambda x: x.fillna(x.mean())).reset_index(drop=True)
print(df2)
#   Month Dayname Class  Val1  Val2
# 0   Oct     Fri     K   2.0   8.0
# 1   Oct     Fri     F   7.0   3.0
# 2   Oct     Fri     F   4.5   5.5
# 3   Oct     Mon     F   5.0   2.0
# 4   Sep     Mon     A   1.0   2.0
# 5   Sep     Mon     B   3.0   4.0
# 6   Sep     Mon     A   2.0   3.0
# 7   Sep     Mon     B   2.0   3.0
# 8   Sep     Tue     A   7.0   5.0

# Drawback: work only when columns are static
df[['Val1', 'Val2']] = df.groupby(['Month', 'Dayname']).transform(lambda x: x.fillna(x.mean()))
print(df)
#   Month Dayname Class  Val1  Val2
# 0   Sep     Mon     A   1.0   2.0
# 1   Sep     Mon     B   3.0   4.0
# 2   Sep     Tue     A   7.0   5.0
# 3   Oct     Mon     F   5.0   2.0
# 4   Oct     Fri     K   2.0   8.0
# 5   Oct     Fri     F   7.0   3.0
# 6   Sep     Mon     A   2.0   3.0
# 7   Sep     Mon     B   2.0   3.0
# 8   Oct     Fri     F   4.5   5.5
