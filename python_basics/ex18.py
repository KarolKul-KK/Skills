def cheese_and_crackers(cheese_count, crackers_boxes): #Wprowadzenie funkcji z dwoma zmiennymi o nazwach cheese_count i crackers_boxes
    print(f"Masz {cheese_count} kawałków sera!") #teskt zawierający nasza zmienną zwróć uwagę na inny nawias i 'f' przed tekstem
    print(f"Masz {crackers_boxes} pudełek krakersów!") #to samo co wyzej
    print("To wystarczy, zeby zrobić imprezę!") 
    print("Zorganizuj sobie koc. \n") #tekst plus symbol ucieczki znak nowej lini \n


print("Mozemy poprostu bezpośrednio podać funckji liczby:")
cheese_and_crackers(20, 30) #sposób podania całej funckji


print("Albo mozemy uzyc zmiennych ze skryptu:")
amount_of_cheese = 10 #sposób podania jednej zmiennej 
amount_of_crackers = 50 #sposób podania jednej zmiennej

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("Mozemy równiez wykonać wewnątrz operacje arytmetyczne:")
cheese_and_crackers(10 + 20, 5 + 6) #sposób podania zmiennych jako działania arytmetyczne


print("I mozemy połączyć te dwie rzeczy, czyli zmienne i operacje arytmetyczne:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #sposóļ podania zmiennych jako zmienna i działania arytmetyczne.