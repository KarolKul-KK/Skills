from sys import exit
from random import randint
from textwrap import dedent
import time


class scene(object):
    pass


class FrontDoor(object):

    def f_door():
        print(dedent("""
        Zostałeś wezwany do domu w którym sąsiedzi słyszeli niepojące dźwięki,
        Stoisz przed drzwiami i słyszysz odgłosy walki.
        1.Pukasz do drzwi 2.Zaglądasz przez okno"""))
        
        fdch1 = input("Co robisz? 1/2: ")

        if fdch1 == '1':
            print("Głosy natychmiast znikają")
            Front_door.come_in()
        elif fdch1 == '2':
            print("Widzisz kłócącę się małzenstwo")
        else:
            print("Musisz wybrać jedną z podanych opcji")

    def come_in():

        print(dedent("""
        Postanawiasz dostać się do środka.
        Widzisz na to 3 mozliwości, mozesz:
        1.Sforsować drzwi. 2.Wybić okno. 3.Poszukać innego wejśćia z tyłu domu."""))

        cich1 = input("Wybierz jedną z podanych opcji 1/2/3: ")
        if cich1 == "1":
            print(dedent("""
            Rozbiegasz się i próbujesz wywazyc drzwi.
            Niestety drzwi ani drgną, musisz znaleźć inny sposób"""))
        elif cich1 == "2":
            print(dedent("""
            Zamierzasz wybić okno ale w ostatniej chwili dostrzegasz,
            ze zasuwka od drzwi nie jest zasunięta. Podchodzisz do drzwi...
            są otwarte."""))
        elif cich1 == "3":
            print("Idziesz na tył, zauwazasz piwnicę")
        else:
            print("Wyberz jedną z podanych opcji.")

        

    



class BackDoor(object):
    pass


class FirstFloor(object):
    pass


class SecondFloor(object):
    pass


class Stairs:
    pass
start_time = time.time()
FrontDoor.f_door()
end_time = time.time()


