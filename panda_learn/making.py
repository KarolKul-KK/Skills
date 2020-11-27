import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

#poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense'] + poke['Sp. Atk'] + poke['Sp. Def'] + poke['Speed']


#Delete the column
#poke.drop(columns=['Total'])


# Change the order of column
poke['Total'] = poke.iloc[:, 4:10].sum(axis=1)
cols = list(poke.columns)
poke = poke[cols[0:4] + [cols[-1]] + cols[4:12]]

print(poke.head(5))