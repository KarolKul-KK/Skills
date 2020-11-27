import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

#print(poke.describe())

print(poke.sort_values(['Type 1', 'HP'], ascending=[1,0]))