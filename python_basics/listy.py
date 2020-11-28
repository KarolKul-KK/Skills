from random import randint

ile = int(input("Ile liczb wylosować?"))
lista = [] #pusta lista
for i in range(0, ile):
    lista.append(randint(0, 100))

print(lista) #Losuje liczby i zapisuje listy z przedziału 0:100


print("Dodawanie elementów na końcu listy")
for i in range(0, 3):
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)
print(lista)

print("Zawartość listy ([indeks] wartość):")
for i, v in enumerate(lista):
    print("[", i, "]", v)


print("Elementy w odwróconym porządku: ")
for e in reversed(lista):
    print(e, end= " ")

print("\nElementy posortowane: ")
for e in sorted(lista):
    print(e, end=" ")

e = int(input("\nKtóra liczbę usunąć? "))
lista.remove(e)
print(lista)

print("Wstawianie elementów do listy")
a, i = eval(input("Podaj element(liczbę) i miejsce w które wstawić(indeks) oddzielone przecinkiem: "))
lista.insert(i, a)
print(lista)

print("Wyszukiwanie i zliczanie elementu w liście")
e = int(input("Podaj liczbę: "))
print("Liczba wystąpień: ")
print(lista.count(e))
print("Indeks pierwszego wystąpienia: ")
if lista .count(e):
    print(lista.index(e))
else:
    print("Brak elemntu w liście")

print("Pobieramy ostatni element z listy: ")
print(lista.pop())
print(lista)

print("Częśc  listy (notacja wycinkowa):")
i,j = eval(input("Podaj indeks początkowy i końcowy oddzielone przecinkiem: "))
print(lista[i:j])

print("Tupla to lista niemodyfikalna.")
print("Prób zmiany tupli generuje błąd:")
tupla = tuple(lista)
tupla[0] = 100