from sys import exit
from random import randint
from textwrap import dedent


class Scene(object): #tego w nawiasie nie muszę pisać

    def enter(self):
        print("Tu chyba powinien być opis sceny głównej ale zobaczymy później.")


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

            #pamiętaj o wydrukowaniu ostatniej sceny
            current_scene.enter()


class Death(Scene):

    quips = [
        "Umarłeś, Jesteś w tym do bani.",
        "Twoja matka byłaby dumna... gdybyś był mądrzejszy"
        "Ale z Ciebie ciołek"
    ]
        
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        Goci z planety Percal 25 wdarli się na twój statek...
        Nie chce mi się pisać tej opowieści więc będę opisywał
        co według mnie się dzieje teraz i w jakim momencie kodu jesteśmy
        To jest opis korytarza, chyba w ten sposób zaczynamy grę
        będziemy wybierać drogą którą pójdziemy 
        przyjmijmy, ze naszą drogą numer jeden jest droga xyz,
         drogą numer dwa zxc i ostatnią abc."""))
    
    action = input(">")

    if action == "xyz":
        print(dedent("""
        dedent uzywam zeby linijki z potrójnego cudzysłowiu zaczęły się od początku lewej strony a nie były wcięty o tyle ile wcięty jest blok.Droga xyz kończy się końcem gry czyli naszą śmiercią"""))
        return 'death'

    elif action == "zxc":
        print(dedent("""
        Drugie jeśli w naszym kodzie, to znaczy ze funkcja zostanie wykonana jeśli jakiś warunek został wcześniej spełniony.
        Spełniliśmy warunek zxc i autor postanowił ze ta droga równiez
        kończy naszą grę czyli śmierć.
        """))
        return 'death'
    elif action == "abc":
        print("Kolejne jeśli, tym razem gracz wybierając tę drogę moze przejść dalej i uruchomić inne klasy z obiektami")
        return 'laser_weapon_armory'

    else:
        print(dedent("""Jeśli zaden ze wcześniejszych warunków nie został spełniony
        wykonaj else czyli ostatnią nie zdefiniowaną drogę
        Ta droga zaraz zostanie rozwinięta o petlę while i dostanie dwie opcje 
        rozstrzygnięcia, a decydował będzie o tym nasz pozornie losowy 
        randint
        Zgadnij 3 cyfry masz na to 10 szans""")

    code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
    guess = input("[keypad]")
    guesses = 0

        while guess != code and guesses < 10:
            print("Bzzz")
            guesses += 1
            guess = input("[Keypad]> ")

        if guess == code:
            print("Zgadłeś liczby wylosowane przez komputer za pomocą randint")
            return 'the_bridge'
        
        else:
            print("Zły kod, koniec gry")

             return 'death'

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        Po raz kolejny uzywam dedent do lepszego sformatowania tekstu
        w kolejnej scenie mamy kolejne wybort, funkcje if i znów mozemy przegrać grę. Mamy dwa wybory TB_choice1, TB_choice2"""))

    action = input("> ")
        
        if action == "TB_choice1 to":
            print(dedent("""
            Ten wybór kończy grę naszą śmiercią"""))
            return 'death'
            
        elif action == "TB_choice2":
            print(dedent("""
            Druga drogą którą mozemy poprowadzić naszą rozgrywkę dzięki
            funkcji elif i spełnieniu drugiego warunku TB_choice2, 
            drugi wybór kończy się kontynuowaniem rozgrywki."""))

            return 'escape_pod'

        else:
            print("Nie wybrałeś nic wracasz na początek tej sceny")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print(dedent())


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_map):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


