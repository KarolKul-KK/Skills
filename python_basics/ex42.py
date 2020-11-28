class Parent(object):

    def implicit(self):
        print("RODZIC implicit()")

class Child(Parent):
    def implicit(self):
        print("AAA")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
