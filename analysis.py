import pandas as pd

filename = r'(filepath)

df = pd.read_csv(filename, encoding='utf-8')

unique_values = df['STATE'].unique()
print("Unique values in 'STATE' column:")
print(unique_values)

# After printing unique values to have a first look, one thing I noticed was the incorrect number
# of states, Brazilian northeast region only has 9 states. After some research in this matter, I've found that
# the National Northeast Bank is
