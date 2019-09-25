'''
Count the number instances of date for any month-year combination
'''
import pandas as pd

paydate = pd.DataFrame()
paydate['PayDate'] = pd.date_range('2017-10-26', '2017-12-26', freq='14D')
print(paydate)
#      PayDate
# 0 2017-10-26
# 1 2017-11-09
# 2 2017-11-23
# 3 2017-12-07
# 4 2017-12-21

'''
Use Grouper with GroupBy.size or DataFrame.resample with Resampler.size 
output is DatetimeIndex

Reference:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.size.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.resample.Resampler.size.html
'''
print(paydate.groupby(pd.Grouper(freq='M', key='PayDate')).size())
# PayDate
# 2017-10-31    1
# 2017-11-30    2
# 2017-12-31    2
# Freq: M, dtype: int64

print(paydate.resample('M', on='PayDate').size())
# PayDate
# 2017-10-31    1
# 2017-11-30    2
# 2017-12-31    2
# Freq: M, dtype: int64

'''
Create month periods by Series.dt.to_period - 
output is PeriodIndex

Reference:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.to_period.html
'''

print(paydate.groupby(paydate['PayDate'].dt.to_period('m')).size())
# PayDate
# 2017-10    1
# 2017-11    2
# 2017-12    2
# Freq: M, dtype: int64
