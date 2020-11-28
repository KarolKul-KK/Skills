import pandas as pd


poke = pd.read_csv('pokemon_data.csv')

print(poke.loc[(poke['Type 1'] == 'Grass') & (poke['Type 2'] == 'Poison')])