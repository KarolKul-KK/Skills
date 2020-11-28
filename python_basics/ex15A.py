from sys import argv

script, test = argv 
print("Zapełnimy tekstem plik {test}")

target = open(test ,'w')
linia1 = input("Pierwsza linia: ")
linia2 = input("Druga linia: ")

print("Zapiszmy linie w pliku")
target.write(linia1 + '\n' + linia2) #metoda .write zadziała na kilku arguemntach tylko jeśli uzyjemy znaku '+' bez tego wystąpi błąd, terminal powie nam ze tej metody mozna uzyc tylko do jegnego argumentu.
target.close()