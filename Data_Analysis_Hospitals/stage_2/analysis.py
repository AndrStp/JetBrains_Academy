import pandas as pd


pd.set_option('display.max_columns', 8)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# extract columns names
columns = general.columns

# change column names for other two dataframes
prenatal.columns = columns
sports.columns = columns

# merge dataframes and drop unnamed column
df = pd.concat([general, prenatal, sports], join='inner', ignore_index=True)
df.drop(columns=df.columns[0], inplace=True)

# display random 20 rows from merged dataframe
print(df.sample(n=20, random_state=30))




