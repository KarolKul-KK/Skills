print("Zgubiłeś się w lesie. Masz trzy drogi LEWO, PROSTO, PRAWO")
road = input("> ").upper()
if road == "LEWO":
    print("""
    Spotykasz czarodzieja który moze wskazać Ci dalsza drogę 
    albo spełnić Twoje jedno zyczenie DROGA/ZYCZENIE""")
    road2 = input("> ").upper()
    if road2 == "DROGA":
        print("Czarodziej pokazuję Ci drogę do wyjścia. Dobra robota!")
    elif road2 == "ZYCZENIE":
        print("Wpisz zyczenie: ", end=' ')
        input("> ")
        print("Czarodziej Cie oszukał, zostaniesz w tym lesie na zawsze.")
elif road == "PRAWO":
    print("""
    Błądzisz po lesie kilka godzin głodny i bez wody.
    Dostrzegasz zająca co robisz? POLUJESZ/OMIJASZ i idziesz dalej.
    """)
    road3 = input("> ").upper()
    if road3 == "POLUJESZ":
        print("""
        Udaje Ci się upolować zająca,
        rozpalasz ogień i giniesz w skutek pozaru
        ale przynajmniej z pełnym zołądkiem :)""")
    elif road3 == "OMIJASZ":
        print("Umierasz z głodu")
elif road == "PROSTO":
    print("""
    Znajdujesz wioskę tybulców którzy pozwalają Ci zostań z nimi
    Zostajesz? TAK/NIE""")
    road4 = input("> ").upper()
    if road4 == "TAK":
        print(""" 
        Zaczynasz nowe zycie, znajdujesz partnera
        i zyjesz długo i szczęśliwie""")
    elif road4 == "NIE":
        print("Tubylcy okazują się kanibalami i Cię zjadają.")