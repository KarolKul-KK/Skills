from sys import argv #pobiera z systemu i importuje argumenty do pliku

script, input_file = argv #nazywa argumenty

def print_all(f): #definiuje nową funkcje która ma drukować cały plik
    print(f.read())

def rewind(f): #definiuje funkcje przewijania jak taśme z magnetofonu 
    f.seek(0) #seek to wyszukiwanie a 0 oznacza, ze od początku

def print_a_line(line_count, f): #definiuje funkcje która ma drukować pojedyncze linie z pliku
    print(line_count, f.readline())

current_file = open(input_file) #otwiera zaimportowany plik

print("Najpierw wydrukujemy cały plik:\n") #drukuje plik a \n to symbol ucieczki który oznacza nową linijke

print_all(current_file) #drukuje cały plik naszą zdefiniowaną funkcją

print("Teraz przewińmy do tyłu tak jak przewija się kasetę")

rewind(current_file) #Cofa plik do początku naszą zdefiniowaną funkcją

print("Wydrukujmy trzy linie:")

current_line = 1
print_a_line(current_line, current_file) #drukuje pierwszą linie

current_line += 1
print_a_line(current_line, current_file) #drukuje drugą linie

current_line += 1
print_a_line(current_line, current_file) #drukuje trzecią linie