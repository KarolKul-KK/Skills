print("""Wchodzisz do ciemniego pokoju z dwoma drzwiami.
Przechodzisz przez drzwi nr 1 czy nr 2?""")

door = input("> ")

if door == "1":
    print("Widzisz tam wielkiego niedźwiedzia, który zajada sernik.")
    print("Co robisz?")
    print("1. Zabierasz sernik.")
    print("2. Krzyczysz na niedźwiedzia.")

    bear = input("> ")

    if bear == "1":
        print("Niedźwiedź odgryza Ci nos. Dobra robota!")
    elif bear == "2":
        print("Niedźwiedź odgryza Ci nogi. Dobra robota")
    else:
        print(f"Cóz, {bear} to prawdopodobnie najlepszy wybór.")
        print("Niedźwiedź ucieka.")

elif door == "2":
    print("Wpatrujesz się w nieskończoną otchłań oka Cthulhu.")
    print("1. Jagody.")
    print("2. Zółte spinacze do bielizny")
    print("3. Wyrozumiałe rewolwery nucą melodie.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Twoje ciało ocalało, ale masz mózg jak galaretka owocowa")
        print("Dobra robota!")
    else:
        print("Z szaleństwa gniją Ci oczy i zamieniają w kałuzę błota.")
        print("Dobra robota!")
    
else:
    print("Potykasz się nadziewasz na nóz i umierasz. Dobra robota!")