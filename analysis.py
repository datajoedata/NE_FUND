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

exclude_years = [1996, 1999, 2020]     # ->>>> 1996 and 1999 were not from the expected years, and 2020 will prob
# give us outlying values due to covid's supportive iniciatives

df = df[~df['HIRE_DATE'].dt.year.isin(exclude_years)]


#///////////////////////////////

# 4- Checking the avg lend value per year

# Now let's try to find the avg value of 'CONTRACT_VALUE' for each year


years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
         '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2021', '2022']

state_list = df['STATE'].unique()

# Create an empty DataFrame to store the average values for each year
avg_values = pd.DataFrame(index=years, columns=state_list)

for year in years:
    df_year = df[df['HIRE_DATE'].dt.year == int(year)]
    sum_year = df_year['CONTRACT_VALUE'].sum()
    count_year = df_year.shape[0]
    avg_year = sum_year / count_year
    print(f"Average 'CONTRACT_VALUE' for year {year}: {avg_year}")


# 5- Now let's plot the avg per state and year

# Create a dictionary to store the average values for each year
avg_year_values = {}

for year in years:
    df_year = df[df['HIRE_DATE'].dt.year == int(year)]
    sum_year = df_year['CONTRACT_VALUE'].sum()
    count_year = df_year.shape[0]
    avg_year = sum_year / count_year
    avg_year_values[year] = avg_year
    for state in state_list:
        df_state_year = df_year[df_year['STATE'] == state]
        sum_value = df_state_year['CONTRACT_VALUE'].sum()
        count_value = df_state_year.shape[0]
        avg_value = sum_value / count_value
        avg_values.loc[year, state] = avg_value


# Plotting bar chart of average per state per year
fig, ax = plt.subplots()
avg_values.plot(kind='bar', ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Average CONTRACT_VALUE')
ax.set_title('Average CONTRACT_VALUE by Year and State')
plt.xticks(rotation=45)
plt.legend(title='State')

# Plotting lines for the year average points 
for year, avg_value in avg_year_values.items():
    ax.plot([year, year], [0, avg_value], color='lightcoral', linestyle='--', linewidth=0.8)
    ax.scatter(year, avg_value, color='lightcoral', marker='o', edgecolor='black', linewidth=0.8)

# Adding legend for the average line
ax.plot([], [], color='lightcoral', linestyle='--', linewidth=0.8, label='Average')

plt.legend(loc='upper right')

plt.show()

# 6- Now let's check if we have any weird values regarding municipality/State
#    (A municipality code can only belong to one state)

# Group the data by 'MUNICIPALITY_CODE' and check the unique values of 'STATE'
municipality_state = df.groupby('MUNICIPALITY_CODE')['STATE'].unique()

# Find municipality codes with multiple states
municipality_codes_multiple_states = municipality_state[municipality_state.apply(lambda x: len(x) > 1)]

# Check if all municipality codes have their equivalent state
if len(municipality_codes_multiple_states) == 0:
    print("All municipality codes have their equivalent state.")
else:
    print("Municipality codes with different states:")
    print(municipality_codes_multiple_states)
