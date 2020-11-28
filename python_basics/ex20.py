def add(a, b): #definiuje nową funkcje i ustala ilość argumentów
    print(f"DODAWANIE {a} + {b}") #wypisuje 
    return a + b #ustala w jaki sposób ma się skończyć funkcja w tym przypadku funkcja skończy się dodaniem do siebie arguemntów

def subtract(a, b):
    print(f"ODEJMOWANIE {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MNOZENIE {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DZIELENIE {a} / {b}")
    return a / b


print("Wykonajmy kilka operacji arytmetycznych jedynie za pomocą funkcji!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Wiek: {age}, Wzrost: {height}, Waga: {weight}, IQ: {iq}")


#To łamigłówka za dodatkowe punkty
print("Oto zadanie.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("To daje: ", "Oblicz ręcznie")
x = 35 + 74 - 180 * (50 / 2)