import pandas as pd
import numpy as np


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

# delete all the empty rows
df.dropna(how='all', inplace=True)

# correct all the gender column values to f and m respectively
df['gender'].replace({'man': 'm',
                      'male': 'm',
                      'woman': 'f',
                      'female': 'f',
                      np.nan: 'f'}, inplace=True)

# Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros
df.update(df[['bmi',
              'diagnosis',
              'blood_test',
              'ecg',
              'ultrasound',
              'mri',
              'xray',
              'children',
              'months']].fillna(0))

# Print shape of the resulting data frame
print('Data shape:', df.shape)

# display random 20 rows from merged dataframe
print(df.sample(n=20, random_state=30))



