class Parent(object):

    def override(self):
        print("Rodzic override()")

    def implicit(self):
        print("Rodzic implicit")

    def altered(self):
        print("Rodzic altered()")

class Child(Parent):
    def override(self):
        print("Dziecko override()")

    def altered(self):
        print("Dziecko przed altered() Rodzica")
        super(Child, self).altered() #moment dziedziczenia
        print("Dziecko po altered() Rodzica")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()