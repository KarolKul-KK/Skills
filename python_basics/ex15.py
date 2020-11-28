from sys import argv

script, filename = argv

print("Wymazemy {filename}.")
print("Jeśli tego nie chcesz, wciśnij CTRL+C (^C).")
print("Jeśli tego chcesz, wciśnij RETURN.")

input("?")

print("Otwieranie pliku")
target = open(filename, 'w')

print("Wykasowanie pliku. Do widzenia!")
target.truncate()  #metoda .truncate wykasowuje zawartość pliku

print("Teraz poproszę Cię o wpisanie trzech linii tekstu.")

line1 = input("Linia 1: ")
line2 = input("Linia 2: ")
line3 = input("Linia 3: ")

print("Zapisze je w pliku.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("A na koniec zamykamy plik.")
target.close()