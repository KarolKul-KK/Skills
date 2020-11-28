from sys import argv #pobiera arguemnty z systemu

script, filename = argv #ilość argumentów

txt = open(filename) #ustanawia zmienną i otwiera plik który podaliśmy. Otworzony plik podpinamy pod zmienna txt

print(f"Oto Twój plik {filename}:") #Drukuje nazwę pliku, który jest plikiem .txt i znajduje się w argumentach pobranych na początku
print(txt.read())   #drukuje plik .txt dzięki funkcji o nazwie .read

print("Wpisz ponownie nazwę pliku:") #Program drukuje tekst prosząc Cię o wpisanie nazwy pliku
file_again = input("> ") #dzięki funkcji input mozemy pobrać nazwę pliku(zwróć uwagę ze ustawiamy nową zmienną o nazwie file_again)

txt_again = open(file_again) #Za pomocą funkcji open otwieramy plik który wprowadziliśmy w linijce 11 przy pomocy input

print(txt_again.read()) #drukujemy plik