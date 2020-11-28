op = "t"
while op == "t":

    print("Podaj trzy liczby.")
    a = input("Pierwsza liczba: ")
    b = input("Druga liczba: ")
    c = input("Trzecia liczba: ")

    if int(a) > int(b):
        if a > c:
            print(f"Pierwsza liczba jest największa {a}")

        elif a < c:
            print(f"Trzecia liczba jest największa {c}")

    elif a < b:
        if b > c:
            print(f"Druga liczba jest największa {b}")

        else:
            print(f"Trzcia liczba jest największa {c}")

    op = input("Czy chcesz spróbować jeszcze raz? (t/n)")

print("Koniec.")
    




        