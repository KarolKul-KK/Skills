print("Przećwiczmy wszystko.")
print("Musisz poćwiczyć sekwencje ucieczki ze znakiem \\, które wstawiają: ")
print('\n nowe linie oraz \t tabulatory.')

poem = '''
\t Ten piękny świat
z tak mocno osadzoną logiką
nie potrafi dostrzec \n potrzeby miłości
ani pojąć pasji płynącej z przeczucia
i wymaga wyjaśnienia
\n\tale zadnego nie ma.
'''

print("\t-------------")
print(poem)
print("\t-------------")


five = 10 - 2 + 3 - 6
print(f"To powinno wynosić pięć: {five}")

def secret_formula(ending): #Robiłem to zeby pokazać, ze to są tylko nazwy
    jelly_beans = ending * 500 
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


point = 10000 
beans, jars, crates = secret_formula(point)

#pamiętaj, ze jest to kolejny sposób formatowania łańcucha znaków
print(f"Zaczynamy od wartości początkowej: {point}")
#działa to podobnie do łańcucha znaków f""
print("To nam da {} zelek, {} słoików oraz {} skrzyń.".format(beans, jars, crates))

point = point / 10

print("Mozemy to równie zrobić w ten sposób:")
formula = secret_formula(point)
#jest to prosty sposób zostosowania listy do sformatowanego łańcucha znaków 
print("To nam da {} zelek, {} słoików oraz {} skrzyń.".format(*formula))