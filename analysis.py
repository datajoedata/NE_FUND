import pandas as pd

filename = r'filepath'

df = pd.read_csv(filename, encoding='utf-8')

# Standardizing dates before anything

df['HIRE_DATE'] = pd.to_datetime(df['HIRE_DATE'])

# 1- Having a 1st look in the df ->>>>

# print(df.shape)

print(df.columns)

# print(df.info())

#df["CONTRACT_VALUE"] = df["CONTRACT_VALUE"].astype("int64")
#with pd.option_context('display.max_columns', None):
#    print(df.describe(include="all"))


#////////////////

# 2- Looking for unique values in each column:

# for column in df.columns:
#    unique_values = df[column].unique()
#    print(f"Unique values in '{column}' column:")
#    print(unique_values)
#    print()


# After using unique method to look deeper, one thing I've noticed was the incorrect number
# of states, Brazilian northeast region only has 9 states. After some research in this matter, I've found that
# the National Northeast Bank is subordinate to Federal Bank Instances. Even tho it's kind of weird finding
# this values here, Dunno if this was the case, but the respective Federal Bodies can lend loans in the name of FNE.


# 3-

