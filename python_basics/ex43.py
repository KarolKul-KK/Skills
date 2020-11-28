class Other(object):

    def override(self):
        print("override() klasy Other")

    def implicit(self):
        print("Implicit() klasy Other")

    def altered(self):
        print("altered() klasy Other")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Dziecko override()")

    def altered(self):
        print("Dziecko przed alterd() klasy Other")
        self.other.altered()
        print("Dziecko po altered klasy Other")

son = Child()

son.implicit()
son.override()
son.altered()
