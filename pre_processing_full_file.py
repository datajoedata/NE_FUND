#1- Before everything: Due to computing power this files were pre-pre processed in SQL Server Management Studio (SSMS) but only for concatenating purposes.

#2- Pre-processing is a important step for every data related work, but if you aren't interested you should probably skip this step and go to the analysis file.

#3- Now let's use the df.columns method to have a look at the columns:


#Input:

import pandas as pd
filename = 'FNE_ALL_ENG.csv'
df = pd.read_csv(filename, encoding='utf-8')

# Print all columns
print(df.columns)


# Output: Index(['HIRE_DATE', 'CONTRACT_NUMBER', 'MUNICIPALITY_CODE', 'STATE',
#               'URBAN_RURAL', 'LEGALENTITY_PHYSICALENTITY', 'BUSINESS_SIZE', 'PROGRAM',
#               'SECTOR', 'CONTRACT_VALUE']dtype='object')


#4- Dropping columns that isn't necessaire: 'PROGRAM' column:

df = df.drop('PROGRAM', axis=1)

#5- In this step I used unique method to see each unique values, known errors, and missing values in each column.

#for column in df_cleaned.columns:
#    unique_values = df_cleaned[column].unique()
#    print(f"Unique values in column '{column}':")
#    print(unique_values)
#    print()


#6- Now let's count the occurrences of values to be removed:

count_hire_date_errors = df['HIRE_DATE'].apply(lambda x: pd.to_datetime(x, errors='coerce')).isnull().sum()
count_business_size_not_specified = df['BUSINESS_SIZE'].isin(['Not Specified']).sum()
count_business_size_nan = df['BUSINESS_SIZE'].isna().sum()
count_legalent_physicalentity_nan = df['LEGALENTITY_PHYSICALENTITY'].isna().sum()

#7- Remove rows with the specified values/errors:
df_cleaned = df[~df['HIRE_DATE'].apply(lambda x: pd.to_datetime(x, errors='coerce')).isnull() &
                ~df['BUSINESS_SIZE'].isin(['Not Specified']) &
                ~df['BUSINESS_SIZE'].isna() &
                ~df['LEGALENTITY_PHYSICALENTITY'].isna()]

#8- Separate rows with errors into a different DataFrame
errors = df.loc[~df.index.isin(df_cleaned.index)]

#9- Printing the remaining number of rows
remaining_rows = df_cleaned.shape[0]
print("Number of rows remaining:", remaining_rows)

#10- Printing the counts of removed values
print("Occurrences of invalid HIRE_DATE values:", count_hire_date_errors)
print("Occurrences of 'Not Specified' in BUSINESS_SIZE column:", count_business_size_not_specified)
print("Occurrences of NaN in BUSINESS_SIZE column:", count_business_size_nan)
print("Occurrences of NaN in LEGALENTITY_PHYSICALENTITY column:", count_legalent_physicalentity_nan)

# Number of rows remaining:   8832976
# Occurrences of invalid HIRE_DATE values:   157325
# Occurrences of 'Not Specified' in BUSINESS_SIZE column:   88
# Occurrences of NaN in BUSINESS_SIZE column:   17583
# Occurrences of NaN in LEGALENTITY_PHYSICALENTITY column:   4106



# Save the main DataFrame with removed rows and 'PROGRAM' column to a new file
df_cleaned.to_csv(r'FNE_ALL_CLEANED.csv', index=False)

# Save the errors DataFrame to a new file
errors.to_csv(r'FNE_ALL_ERRORS.csv', index=False)
