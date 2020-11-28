people = 20
cats = 30
dogs = 15

if people < cats:
    print("Zbyt duzo kotów! Świat jest skazany na zagłade!")

if people > cats:
    print(" Nie za duzo kotów! Świat jest ocalony!")

if people < dogs:
    print("Świat się ślini!")

if people > dogs:
    print("Świat jest suchy!")


dogs += 5

if people >= dogs:
    print("liczba ludzi jest większa lub równa liczbie psów.")

if people <= dogs:
    print("Liczba ludzi jest mniejsza lub równa liczbie psów.")

if people == dogs:
    print("Ludzie są psami.")