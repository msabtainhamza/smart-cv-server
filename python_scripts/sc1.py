import pandas as pd

df = pd.read_csv('gen.csv')

# Save the dataframe as a .pkl file
df.to_pickle('gen.pkl')