import pandas as pd


def top3():
    # Top 3 Cost Notional in a dataframe group by Underlying 
    df = pd.DataFrame(columns=["Portfolio", "Underlying", "Cost Notional"],
                      data=[[1002, "5 HK",     230000],
                            [1002, "1 HK",     120000],
                            [1002, "700 HK",    80000],
                            [1002, "388 HK",   830000],
                            [1002, "12 HK",    110000],
                            [1005, "1299 HK", 5600000],
                            [1005, "700 HK",  8100000],
                            [5112, "3 HK",    9000000],
                            [5112, "6 HK",     120000],
                            [5112, "2318 HK",  640000],
                            [5112, "833 HK",  3100000]])
    print(df)
    '''
            Portfolio Underlying  Cost Notional
    0        1002       5 HK         230000
    1        1002       1 HK         120000
    2        1002     700 HK          80000
    3        1002     388 HK         830000
    4        1002      12 HK         110000
    5        1005    1299 HK        5600000
    6        1005     700 HK        8100000
    7        5112       3 HK        9000000
    8        5112       6 HK         120000
    9        5112    2318 HK         640000
    10       5112     833 HK        3100000
    '''

    df_top3 = df.sort_values(by='Cost Notional', ascending=False).groupby('Portfolio').head(3)
    print(df_top3)
    '''
            Portfolio Underlying  Cost Notional
    7        5112       3 HK        9000000
    6        1005     700 HK        8100000
    5        1005    1299 HK        5600000
    10       5112     833 HK        3100000
    3        1002     388 HK         830000
    9        5112    2318 HK         640000
    0        1002       5 HK         230000
    1        1002       1 HK         120000
    '''

    df_top3 = df_top3.groupby('Portfolio')['Underlying'].apply(lambda x: ','.join(x)).reset_index()
    print(df_top3)
    '''
           Portfolio           Underlying
    0       1002     388 HK,5 HK,1 HK
    1       1005       700 HK,1299 HK
    2       5112  3 HK,833 HK,2318 HK
    '''


if __name__ == '__main__':
    top3()
