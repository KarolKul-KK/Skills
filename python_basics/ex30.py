the_count = [1, 2, 3, 4, 5]
fruits = ['jabłka', 'pomarańcze', 'gruszki', 'morele']
change = [1, 'jednogroszówki', 2, 'dwugroszówki', 3, 'pięciogroszówki']

# to jest pierwszy rodzaj pętli for, która przechodzi przez listę
for number in the_count:
    print(f"To jest liczba {number}")

#to samo co wyzej
for fruit in fruits:
    print(f"Rodzaj owocu: {fruit}")

#mozemy równiez przechodzić przez listy mieszane
#zwróć uwagę, ze musimy uzyć {}, poniewaz nie wiemy co w niej jest
for l in change:
    print(f"Mam {l}")

#Mozemy równiez budować listy; Zaczniemy od pustej
elements = []

#następnie uzywamy funkcji range, aby odliczyć od 0 do 5
for l in range(0, 9):
    print(f"Dodajemy {l} do tej listy.")
    #append jest funkcją, którą listy rozumieją
    elements.append(l)

#teraz mozemy je równiez wydrukować
for l in elements:
    print(f"Tym elementem było: {l}") #i to tylko domyślna zmienna