from sys import exit

def gold_room():
    print("Ten pokój jest pełen złota. Ile złota zabierasz?") 

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Stary naucz się wpisywać liczby")

    if how_much < 50:
        print("Miło nie jestes chciwy, wygrywasz!")
        exit(0)
    else:
        dead("Ty chciwy draniu!")


def bear_room():
    print("Jest tutaj niedźwiedź.")
    print("Niedźwiedź ma beczkę miodu.")
    print("Ten gruby niedźwiedź siedzi przed następnymi drzwiami.")
    print("Jak przesuniesz niedźwiedzia?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "zabieram miód":
            dead("Niedźwiedź spodgląda na Ciebie i wali w twarz.")
        elif choice == "śmieje się z niedźwiedzia" and not bear_moved:
            print("Niedźwiedź odsunął się od drzwi")
            print("Mozesz teraz przez nie przejść")
            bear_moved = True
            exit()
        elif choice == "Śmieję się z nieźdźwiedzia" and bear_moved:
            dead("Niedźwiedź się wkurzył i odgryzł Ci nogę")
        elif choice == "Otwieram drzwi" and bear_moved:
            gold.room()
        else:
            print("Nie mam pojęcia, co to znaczy")


def cthulu_room():
    print("Widzisz wielkiego złego Cthulu.")
    print("On, znaczy to, niewazne, wpatruje się w Ciebie, a Ty popadasz w obłęd.")
    print("Ratujesz się ucieczką, czy zjadasz swoją głowę?")

    choice = input("> ")
    
    if "ucieczką" in choice:
        start()
    elif "głowę" in choice:
        print("To było pyszne!")
    else:
        cthulu_room


def dead(why):
    print(why, "Dobra robota!")
    exit(0)

def start():
    print("Znajdujesz się w mrocznym pokoju.")
    print("Po lewej i po prawej znajdują się drzwi.")
    print("Które wybierasz?")

    choice = input("> ")

    if choice == "lewe":
        bear_room()
    elif choice == "prawe":
        cthulu_room()
    else:
        dead("Błąkasz się po pokoju, az w końcu umierasz z głodu.")


bear_room()