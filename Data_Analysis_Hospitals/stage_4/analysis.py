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

# First question
highest_number_of_patients = df['hospital'].value_counts().idxmax()
print('The answer to the 1st question is', highest_number_of_patients)

# Second question
general_mask = df['hospital'] == 'general'
general_diagnosis_df = df.loc[general_mask][['diagnosis']]
general_diseases_counts = general_diagnosis_df.value_counts(normalize=True)
stomach_related = np.round(general_diseases_counts['stomach'], 3)
print('The answer to the 2nd question is', stomach_related)

# Third question
sport_mask = df['hospital'] == 'sports'
sports_diagnosis_df = df.loc[sport_mask][['diagnosis']]
sports_diseases_counts = sports_diagnosis_df.value_counts(normalize=True)
dislocation_related = np.round(sports_diseases_counts['dislocation'], 3)
print('The answer to the 3rd question is', dislocation_related)

# Fourth question
general_age = df.loc[general_mask][['age']]
sport_age = df.loc[sport_mask][['age']]
general_age_median = general_age.median()['age']
sport_age_median = sport_age.median()['age']
print('The answer to the 4th question is', general_age_median - sport_age_median)

# Fifth question
tests_df = df[df['blood_test'] == 't']
values_tests = tests_df[['hospital', 'blood_test']].value_counts()
print(f'The answer to the 5th question is {values_tests.idxmax()[0]}, {values_tests.max()} blood tests')




