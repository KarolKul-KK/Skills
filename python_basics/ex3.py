cars = 100 #ustala zmienne do czwartej linijki włącznie
space_in_car = 4
drivers = 30
passengers = 90 
car_not_driven = cars - drivers #liczy ilość wolnych samochodów
cars_driven = drivers #ustanawia zmienną ze zmiennej
carpool_capacity = cars_driven * space_in_car #ustanawia zmienną i liczy ile miejsca jest w samochodach
average_passengers_per_car = passengers / cars_driven #ustanawia zmienną i liczy ile osób musimy zmieścić do jednego samochodu


print("Dostępnych jest", cars, "samochodów.") #drukuje tekst który zawiera zmienną
print("Dostępnych jest tylko", drivers, "kierowców.")
print("Dziś będzie", car_not_driven, "pustych samochodów")
print("dziś moemy przetransportować", carpool_capacity, "osób.")
print("Mamy dziś do przewiezienia", passengers, "pasaerów.")
print("Musimy umieścić średnio", average_passengers_per_car, "osoby w kazdym samochodzie") #wszystkie linjki z print wyświetlają tekst oraz jedną z potrzebnych zmiennych.