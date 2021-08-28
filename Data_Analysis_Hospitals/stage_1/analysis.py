import pandas as pd


pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

dfs = [general, prenatal, sports]
for df in dfs:
    print(df.head(20))


