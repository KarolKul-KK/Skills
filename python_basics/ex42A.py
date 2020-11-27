class Parent(object):
#definiuje klasę z której będziemy dziedziczyć dalej
    def altered(self):
        print("Rodzic altered()")

class Child(Parent):
#tutaj mamy drugą klasę i to właśnie ta klasa będzie dziedziczyć
    def altered(self):
        print("Dziecko PRZED altered() rodzica") 
        super(Child, self).altered() #Ten moment naszego kodu wymusza dziedziczenie.
        print("DZIECKO PO altered() rodzica")

dad = Parent()
son = Child()

dad.altered()
son.altered()