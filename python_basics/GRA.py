def start():
    print ("""
Jesteś policjantem i zostałeś wezwany do domu
w którym sąsiąd słyszał niepokojące odgłosy.""")
    print("Stajesz przed drzwiami domu, słyszysz odgłosy walki.")
    choice1()

def choice1():
    print("""
Co robisz?
\t 1. Pukasz do drzwi mówiąc, policja!
\t 2. Podchodzisz do okna zajrzeć co się dzieje.""")


    road1 = input("> ")
    
    if road1 == "1":
        print("Odgłosy natychmiast ustają.")
        choice2()

    elif road1 == "2":
        print("""
        Widzisz dwójke dziwnie ubranych ludzi, kłócą się
        To chyba małzeństwo, niestety
        Zauwazyli Cię! i szybko gdzieś zniknęli""")
        choice2()

    else:
         print("Musisz wybrać jedną z podanych opcji.")
         choice1()
    
def choice2(): 
    print("""
    Postanowiłeś dostać się do środka
    \t 1. Podchodzisz do drzwi i próbujesz je wywazyć.
    \t 2. Podchodzisz do okna z zamiarem wybicia go.
    \t 3. Idziesz na tył domu sprawdzić czy jest tam jakieś inne wejście.""")
    
    road2 = input("> ")

    if road2 == "1":
        print("""
        Bierzesz rozbieg i z całej siły próbujesz sforsować drzwi.
        Bezskutecznie, drzwi ani drgną.""")
        choice2()
    elif road2 == "2":
        print("""
        Bierzesz zamach i juz masz rozbijać szybę kiedy zauwazasz,
        ze w drzwiach jest nie przesunięta zasuwka, 
        wracasz do drzwi i naciskasz klamkę, drzwi są otwarte.\n""")
        inside_hol()
    elif road2 == "3":
        print("""
        \rIdziesz na tył domu i widzisz wejście do piwnicy,
        \rdrzwi są zamknięte a obok nich zauwazasz domofon.""")
        print("Myślisz *Domofon przy wejśćiu do piwnicy, dziwne...*")
        print("Wracasz przed dom.")
        choice2()
    else:
        print("Musisz wybrać jedną z podanych opcji.")
        choice2()

def inside_hol():
    print("\rW środku panowała niepokojąca cisza, zacząłeś się rozglądać...")
    print("""\rPrzed Tobą stały dwie mozliwości
    \t1. Iść rozejrzeć się w salonie
    \t2. Wejść po schodach na górę""")

    road3 = input("> ")

    if road3 == "1":
        print("\rWchodzisz do salonu, na pierwszy rzut oka wszystko wygląda normalnie.")
        inside_salon()
    elif road3 == "2":
        print("""
        Wchodzisz po schodach i widzisz
        """)
        inside_upstairs()
    else:
        print("Musisz wybrać jedną z podanych opcji")
        inside_hol()

def inside_salon():
    print("\r Salon jest duzy połączony z kuchnią, ładnie umeblowany")
    print("""
    Jest kilka rzeczy które przyciągają Twoją uwagę.
    1. Duzy kominek.
    2. Wielka szafa.
    3. Lodówka przy której znajdują się niepokające ślady.
    4. Wracam na schody.""")
    
    road4 = input("> ")

    if road4 == "1":
         print("""
         Kominek jeszcze oddaję ciepło, ktoś przed chwilą musiał w nim palić.
         Przyglądasz się i widzisz, ze w kominku palono ubraniami. 
         Zauwazasz małą niedopaloną karteczkę, a na niej dwie cyfry '07'
         """)
         inside_salon()
    elif road4 == "2":
         print("""
         Podchodzisz do szafy, otwierasz ją.
         W szafie znajdują się tylko czarne płaszcze z głębokimi kapturami.\n""")
         inside_salon()
    elif road4 == "3":
        print("""
        Podchodzisz do lodówki, przy drzwiach na dole widzisz plamy..
        plamy krwi...
        Otwierasz lodówkę, a w niej przerazający widok!
        Widzisz odcięte głowy przeróznych zwierząt\n""")
        inside_salon()
    elif road4 == "4":
        inside_upstairs()
    else:
        print("Musisz wybrać jedną z podanych opcji")
        inside_salon()

def inside_upstairs():
    print("""
    Na górze znajdują się dwa wejścia
    jedno wygląda jak sypialnia, a drugie jak pokój dziecka.
    \t1.Wchodzisz do sypialni.
    \t2.Wchodzisz do pokoju dziecięcego.""")
    
    road5 = input("> ")

    if road5 == "1":
        print("""
        Sypialnia jest pusta, nie ma w niej nawet łózka.
        Na ścianach widzisz pełno dziwnych napisów.
        Napisy są w jakimś nieznanym Ci języku,
        chociaz moze to łacina, jedno słowo juz gdzieś widziałes
        MORTEM, a obok niego czy to jest?...
        tak to pentagram!
        """)
        print("Wracasz do holu")
        inside_upstairs()
    elif road5 == "2":
        print("""
        Pokój dziecka wygląda normalnie.\n""")
        inside_room()
    else:
        print("Musisz wybrać jedną z podanych opcji.")
        inside_upstairs()

def inside_room():
    print("""
    Rozglądasz się po pokoju, dostrzegasz kilka interesujących rzeczy.
    \t1.Kalendarz.
    \t2.Pamiętnik.""")

    road6 = input("> ")

    if road6 == "1":
        print("W kalendarzy zaznaczona jest jakaś data hmm.. to dzisiaj!")
        inside_room()
    elif road6 == "2":
        print("Pamiętnik jest otwarty.")
        print("""
        Wtorek                                            23.08.2020
        Drogi pamiętniku dzisiaj mam urodziny, kończę 13 lat
        Moi rodzicie ostatnio dziwnie się zachowują
        ale obiecali mi przyjęcie tylko nie wiem dlaczego w piwnicy.
        Ostatnio spedzają tam mnóstwo czasu.
        Nawet załozyli jakiś skomplikowany system i nie mogę tam wejść
        Rodzice mówią, ze ja jestem kluczem do piwnicy
        Ciekawe co to oznacza...\n""")
        print("""
        Gdzie powinieneś się teraz udać?
        \t 1. Do salonu.
        \t 2. Do piwnicy.""")

        road7 = input("> ")

        if road7 == "1":
            inside_salon()
        elif road7 == "2":
            outside_piwnica()
        else:
            print("Musisz wybrać jedną z opcji.")
            inside_room()
    else:
        print("Musisz wybrać jedną z podanych opcji.")
        inside_room()

def outside_piwnica():
    print("""
    Stajesz przed drzwiami do piwnicy.
    Juz wiesz, ze to nie jest domofon,
    zza ściany słyszysz jakieś krzyki.
    Czas się kończy, musisz szybko wpisać kod!""")
    
    road8 = input("> ")

    if road8 == "2007":
        print("Świetnie udało Ci się otworzyć drzwi!")
        print("""
        Widzisz dwie zakapturzone postacie obie trzymają coś w rękach,
        a za nimi dziecko! Dziecko przywiązane do krzyza!
        Musisz szybko podjąć decyzję
        \t1. Strzelasz do postaci z lewej strony.
        \t2. Strzelasz do postaci z prawej strony.""")

        road9 = input("> ")

        if road9 == "1":
            print("""
            Zabijasz matkę dziecka ale to ojciec trzymał nóz,
            Dziecko ginie na Twoich oczach.""")
            dead()
        elif road9 == "2":
            print("""
            Zabijasz ojca dziecka, to on trzymał nóz,
            udało Ci się uratować dziecko\n""")
            win()
        else:
            dead()
    else:
        print("Niestety wpisałeś zły kod.")
        print("Za drzwiami słyszysz przeraźliwy krzyk.")
        print("A po niej ciszę.")
        dead()
def dead():
    print("""
    Dziecko umiera, a Ty nie rozwiązujesz tej sprawy.
    Zostajesz zwolniony i do końca zycia czujesz się winny.""")
def win():
    print("Ratujesz dziecko i rowiązujesz sprawę!")
    print("""
    Okazało się, ze rodzice dziecka dołączyli do sekty.
    Chcieli swoje własne dziecko złozyc w ofierze.
    Ale Ty przybyłeś na czas, zeby je uratować.
    Zostałeś bohaterem znanym w całym kraju.
    Gratuluję wygrałeś.""")
            

    



start()



