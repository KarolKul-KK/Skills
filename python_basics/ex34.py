ten_things = "Jabłka Pomarańcze Wrony Telefon Światło Cukier"

print("Chwileczkę na tej liście nie ma 10 rzeczy, poprawmy to.")

stuff = ten_things.split(' ')
more_stuff = ["Dzień", "Noc", "Piosenka", "Frisbee", "Kukurydza", "Banan", "Dziewczyna", "Chłopak"]


while len(stuff) != 10:
    next_one = more_stuff.pop() #definiuje zmienną next_one jako funkcję która dodaje do listy
    print("Dodawanie: ", next_one) #drukuje co zostaje dodane do listy 
    stuff.append(next_one) #metoda append dodaje przekazany obiekt do listy, obiekt przekazujemy dzięki zmiennej next_one
    print(f"Teraz jest {len(stuff)} elementów.") #Liczy i drukuje ilość

print("Teraz to mamy: ", stuff)

print("Zróbmy jeszcze parę rzeczy ze stuff")

print(stuff[1]) #Drukuje drugą w koleności wartość
print(stuff[-1]) #Drukuje ostatnią wartość z listy
print(stuff.pop()) #zdejmuje ostatnią wartość z listy
print(' '.join(stuff)) #Drukuję całą listę 
print('#'.join(stuff[3:6])) #Ciekawe znak '#' pojawi się pomiędzy wartściami