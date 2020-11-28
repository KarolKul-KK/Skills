from abc import ABC, abstractmethod

class Zwierze(ABC):
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga
    
    @abstractmethod #tutaj wymuszamy implementację tej metdoy w klsach pochodnych
    
    def nazwa_gatunku(self):
        pass
    
    def przedstaw_sie(self):
        print(f"Jestem {self.nazwa_gatunku()}, mam na imię {self.nazwa}, mam {self.wiek} lat oraz waze {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1

class Slon(Zwierze):
    def nazwa_gatunku(self):
        return "Slon"

class Lew(Zwierze):
    def nazwa_gatunku(self):
        return "Lew"
      

class Papuga(Zwierze):
    def nazwa_gatunku(self):
        return "Papuga"

    def __init__(self, nazwa, wiek, waga, kolor):
        super().__init__(nazwa, wiek, waga)
        self.kolor = kolor
        
        def przedstaw_sie(self):
            super().przedstaw_sie()
        print(f"Jako papuga mój kolor to {self.kolor}")



def main():
    Dumboo = Slon("Dumboo", 77, "6000")
    Simba = Lew("Simba", 24, "100")
    Jago = Papuga("Jago", 32, "6", "czerwony" )
    #jakis_zwierz = Zwierze("Katarzyna", "21", "234")
    print(f"isinstance(Dumboo, Slon): {isinstance(Dumboo, Slon)}")

    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()

    Jago.urodziny()
    Jago.przedstaw_sie()

   
if __name__ == "__main__":
    main()