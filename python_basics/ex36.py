states = {
    'Oregon': 'OR',
    'Floryda': 'FL',
    'Kalifornia': 'KA',
    'Nowy Jork': 'NJ',
    'Michigan': 'MI'
}


cities = {
    'KA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
#teraz dodamy kilka miast
cities['NJ'] = 'Nowy Jork'
cities['OR'] = 'Portland'

#wydrukujemy kilka miast
print('-' * 10)
print("Stan NJ ma: ", cities['KA'])
print("Stan OR ma: ", cities['MI'])

#drukujemy kilka stanów
print('-' * 10)
print("Skrót dla Michigan to: ", states['Michigan'])
print("Skrót dla Floryda to:", states['Floryda'])

#Drukujemy skrót kazdego stanu
print('-' * 10)
for state, abb in list(states.items()): #abbrev to tylko zmienna definiowana w tej linijce w inny sposób niz zazwyczaj
    print(f"{state} ma skrót {abb}")

#drukujemy kazde miasto w stanie
print('-' * 10)
for abb, city in list(cities.items()):
    print(f"{abb} ma miasto {city}")

#teraz obie te rzeczy na raz
print('-' * 10)
for state, abb in list(states.items()):
    print(f"Stan {state} ma skrót {abb}")
    print(f"oraz miasto {cities[abb]}")

print('-' * 10)
#bezpiecznie pobieramy skrót według nazwy stanu, który moze nie istnieć
state = states.get('Texas')

if not state:
    print("Przepraszamy, nie ma stanu Texas")

#pobieramy miasto za pomocą domyślnej wartości
city = cities.get('TX', 'Nie istnieje')
print(f"Miasto dla stanu 'TX' to {city}")