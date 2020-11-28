types_of_people = 10 #stworzenie zmiennej z wartością 10
x = f"Istnieje {types_of_people} rodzajów ludzi." #tworzenie zmiennej w której zawarty jest tekst ale równiez inna zmienna

binary = "binarny" #stworzenie zmiennej, moim zdaniem niepotrzebnej
do_not = "nie znają" #to samo co na górze
y = f"Ci którzy znają system {binary} i ci którzy go {do_not}." #stworzenie zmiennej zawierającej tekst w którym zawarte są dwie inne zmienne dzięki funkcji f{} pełna nazwa "format"

print(x) #wydrukowanie zmiennej x
print(y) #wydrukowanie zmiennej y

print(f"powiedziałem: {x}") #wydrukowanie tekstu i zmiennej
print(f"powiedziałem równie '{y}'") #to samo co na górze

hilarious = False #stworzenie zmiennej 
joke_evaluation = "Czyz to nie jest przezabawny dowcip?!{}" #bez znaku {} false z jakiejś przyczyny sie nie wydrukuje

print(joke_evaluation.format (hilarious)) #wydrukowanie zmiennych z pomocą funkcji .format

w = "To jest lewa strona..." #stworzenie zmiennych
e = "łańcucha znaków z prawą stroną." #stworzenie zmiennych

print(w + e) #Wydrukowanie zmiennych