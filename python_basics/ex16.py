from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Kopiowanie z {from_file} do {to_file}")

#Moglibyśmy zrobić te rzeczy w jednej linii? jak?
in_file = open(from_file); indata = in_file.read() #tak?


print(f"Plik wejściowy ma {len(indata)} bajtów")

print(f"Czy plik wyjśćiowy istnieje? {exists(to_file)}")
print("Wciśnij REETURN, aby kontynuować lub CTRL + C, zeby anulować.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("W porządku, zrobione")

out_file.close()
in_file.close()