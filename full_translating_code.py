#FOR THOSE WHO WANT TO CHECK ALL THE JOB 

#///////////////////////////////////////////////////////////////////////// STEP 1
#////////////////// TRANSLATING ALL COLUMNS NAMES

import pandas as pd

filename = r'input_filepath'
output_filename = r'output_filepath'
df = pd.read_csv(filename, encoding='utf-8')


# Define the new column names

# REMINDER: Make sure to run STEP 1 first or pandas won't be able to find the columns names in eng.

new_column_names = {
    'DATA_CONTRATAÇÃO': 'HIRE_DATE',
    'CONTRATO': 'CONTRACT_NUMBER',
    'COD_MUNICIPIO_EMPREEDIMENTO': 'MUNICIPALITY_CODE',
    'UF': 'STATE',
    'URBANO_RURAL': 'URBAN_RURAL',
    'TIPO_PESSOA': 'LEGALENTITY_PHYSICALENTITY',
    'PORTE': 'BUSINESS_SIZE',
    'PROGRAMA': 'PROGRAM',
    'SETOR': 'SECTOR',
    'VALOR_CONTRATADO': 'CONTRACT_VALUE'
}

# Rename the columns in the DataFrame
df.rename(columns=new_column_names, inplace=True)





#//////////////////////  SEARCHING FOR ALL UNIQUE VALUES IN THE COLUMN URBAN_RURAL


filename = r'filepath'
df = pd.read_csv(filename, encoding='utf-8')


# PRINTING IN THIS CASE IS USED TO CHECK RESULTS

# Print unique values in the 'URBAN_RURAL' column
unique_values1 = df['URBAN_RURAL'].unique()
print(unique_values1)


#///////////////////////////////////////////////////////////////////////// STEP 2
# Define the 1st translation dictionary

translation_dict1 = {
    'RURAL': 'Rural',
    'URBANO': 'Urban',
    'Rural': 'Rural',
    'Urbano': 'Urban'
}

# Translate the values in the 'URBAN_RURAL' column
df['URBAN_RURAL'] = df['URBAN_RURAL'].map(translation_dict1)

# Print unique values in the 'URBAN_RURAL' column after translation to confirm it worked
unique_values1 = df['URBAN_RURAL'].unique()
print(unique_values1)


#///////////////////////////////////////////////////////////////////////// STEP 3
# Translate the values in the 'LEGALENTITY_PHYSICALENTITY' column:


translation_dict2 = {
   'PF': 'PHY_E',
    'PJ': 'LEGAL_E',
}

#
df['LEGALENTITY_PHYSICALENTITY'] = df['LEGALENTITY_PHYSICALENTITY'].map(translation_dict2)

# Print unique values in the 'URBAN_RURAL' column after translation
unique_values2 = df['LEGALENTITY_PHYSICALENTITY'].unique()
print(unique_values2)


#///////////////////////////////////////////////////////////////////////// STEP 4
# Define the 3rd translation dictionary:

translation_dict3 = {
    'Pecuária': 'Livestock',
    'Agrícola': 'Agriculture',
    'Agroindústria': 'Agroindustry',
    'Industria': 'Industry',
    'Serviços': 'Services',
    'Comércio': 'Commerce',
    'Infraestrutura': 'Infrastructure',
    'Comércio e Serviços': 'Commerce and Services',
    'Agricultura': 'Agriculture',
    'Turismo': 'Tourism',
    'Pessoa Fisica': 'Individual',
    'Pessoa FÃ­sica': 'Individual'
}

# Translate the values in the 'SECTOR' column
df['SECTOR'] = df['SECTOR'].map(translation_dict3)

# Print unique values in the 'SECTOR' column after translation
unique_values3 = df['SECTOR'].unique()
print(unique_values3)


#///////////////////////////////////////////////////////////////////////// STEP 5
#////////DEFINING THE 4th dictionary:

translation_dict4 = {
    'MINI': 'Mini',
    'PEQUENO': 'Small',
    'MEDIO': 'Medium',
    'GRANDE': 'Large',
    'MICRO': 'Micro',
    'NAO ESPECIFICADA': 'Not Specified',
    'PEQUENO-MEDIO': 'Small-Medium',
    'MEDIO-GRANDE': 'Medium-Large',
    'Mini/Micro': 'Mini/Micro',
    'Pequeno': 'Small',
    'Grande': 'Large',
    'MÃ©dio': 'Medium',
    'Pequeno-MÃ©dio': 'Small-Medium',
    'PEQUENO MÃ‰DIO': 'Small-Medium',
    'MÃ‰DIO I': 'Medium I',
    'MÃ‰DIO': 'Medium',
    'MÃ‰DIO II': 'Medium II',
    'Mini': 'Mini',
    'Micro': 'Micro',
    'MÃ©dio I': 'Medium I',
    'Pequeno MÃ©dio': 'Small-Medium',
    'MÃ©dio II': 'Medium II'
}


# Translate the values in the 'BUSINESS_SIZE' column
df['BUSINESS_SIZE'] = df['BUSINESS_SIZE'].map(translation_dict4)

# Print unique values in the 'BUSINESS_SIZE' column after translation
unique_values4 = df['BUSINESS_SIZE'].unique()
print(unique_values4)







# Save the modified DataFrame to a CSV file
output_filename = r'outputpathfile'
df.to_csv(output_filename, index=False)
