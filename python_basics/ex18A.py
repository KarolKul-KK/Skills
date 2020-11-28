def najlepsze_kluby_pilkarskie(miejsce1, miejsce2, miejsce3, liga):

    print(f"Najlepsze kluby piłkarskie z {liga}")
    print(f"Na pierwszym miejscu znajduję się {miejsce1}, na drugim {miejsce2} i na trzecim {miejsce3}. \n")
najlepsze_kluby_pilkarskie("Liverpool", "ManCity", "Leicester", "BPL")

print("Przed chwilą podawaliśmy zmienne za pomocą całej funkcji, teraz podamy oddzielne argumenty")
miejsce1 = ("Barcelona")
miejsce2 = ("Real")
miejsce3 = ("Sevilla")
liga = ("LaLiga")
najlepsze_kluby_pilkarskie(miejsce1, miejsce2, miejsce3, liga)


print("Teraz chciałbym zebys ty podał swoje najlepsze kluby a w miejscu liga wpisał 'wszystkie'")
wg1 = input("Wpisz kulb nr 1: "); wg2 = input("Wpisz klub nr2: "); wg3 = input("wpisz klub nr 3: ")
print(f"Według mnie najleszym klubem jest {wg1}, drugim najlepszym jest {wg2}, trzecim {wg3}: ")
najlepsze_kluby_pilkarskie #czy da się uzyc funkcji input? zagraj i sprawdz
#znalazłem 3 sposoby podobno jest ich znacznie więcej.>>CASE na potem.