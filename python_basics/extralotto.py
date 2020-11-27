from totomodul import ustawienia, losujliczby, pobierztypy, wyniki
from totomodul import czytaj_json, zapisz_json
import time

def main(args):
    nick, ileliczb, maksliczba, ilerazy = ustawienia()

    liczby = losujliczby(ileliczb, maksliczba)

    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(set(liczby), typy)

    
    nazwapliku = nick + ".json" #this is name of document
    losowania = czytaj_json(nazwapliku)

    losowania.append({
        "czas": time.time(),
        "dane": (ileliczb, maksliczba),
        "wylosowane": liczby,
        "ile": iletraf
    })


    zapisz_json(nazwapliku, losowania)

   
    print("Wylosowane liczby:", liczby)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))