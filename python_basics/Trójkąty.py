import math


op = "t" #Deklarujemy i inicjujemy zmienną pomocniczą
while op != "n": #dopóki wartość zmiennej jest inna ni n wykonuj pętle
    dane = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")

    lista = [] #definiujemy pustą listę
    for x in dane.split(","):
        lista.append(int(x)) 
    a, b, c = lista 

    print("Podane boki: ", a, b, c)

    if a + b > c and a + c > b and b + c > a:  #warunek złozony
        print("Z podanych boków mozna zbudować trójkąt.")
        #Czy boki spełniają warunki trójkąta prostokątnego
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Do tego prostokątny")


        #Na wyjściu mozemy wyprowadzać wyrazenia
        print("Obów wynosi: ", (a + b + c))
        p = 0.5 * (a + b + c)  #Obliczamy współczynnik wzoru Herona
        #liczmy pole ze wzoru Herona
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole wynosi: ", P)
        op = "n" #ustawiamy zmienną na "n", aby wyjść z pętli while

    else:
        print("Z podanych odcinków nie mozna stworzyć trójkąta prostokątnego")
        op = input("Chcesz spróbować jeszcze raz?(t/n)")

print("Do zobaczenia...")