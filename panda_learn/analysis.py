import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

poke.columns

#print(poke[['Name', 'Type 1', 'HP']][0:5])

#print(poke.iloc[0:4])

#print(poke.iloc[2,1])

#for index, row in poke.iterrows():
#    print(index, row['Name'])
print(poke.loc[poke["Type 1"] == "Fire"])
