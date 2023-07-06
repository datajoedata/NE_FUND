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


# 3- Removing states and years that are out of our planned scope:

excluded_states = ['MG', 'ES', 'RJ']   # ->>>> Are not part of NORTHEAST states
df = df[~df['STATE'].isin(excluded_states)]

exclude_years = [1996, 1999, 2020]     # ->>>> 1996 and 1999 we're not from the expected years, and 2020 will prob
# give us outlying values due to covid especial financings

df = df[~df['HIRE_DATE'].dt.year.isin(exclude_years)]

# Calculating the avg. value of 'CONTRACT_VALUE' for each year:

years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2021', '2022']

state_list = df['STATE'].unique()

# Create an empty DataFrame to store the average values for each year and state
avg_values = pd.DataFrame(index=years, columns=state_list)

for year in years:
    df_year = df[df['HIRE_DATE'].dt.year == int(year)]
    sum_year = df_year['CONTRACT_VALUE'].sum()
    count_year = df_year.shape[0]
    avg_year = sum_year / count_year
    print(f"Average 'CONTRACT_VALUE' for year {year}: {avg_year}")


