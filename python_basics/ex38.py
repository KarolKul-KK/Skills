class Animal(object):
    pass


# jest (is-a)
class Dog(Animal):

    def __init__(self, name):
        #ma(has-a)
        self.name = name 
    def przedstaw_sie(name):
        print(f"siema, jestem {name}")
        

#jest(is-a)
class Cat(Animal):

    def __init__(self, name):
    #ma(has-a)
        self.name = name


class Person(object):

    def __init__(self, name):
        #ma(has-a)
        self.name = name

        #Person (osoba) ma pet(jakiegoś zwierzaka)
        self.pet = None

#jest(is-a)
class Employee(Person):
    
    def __init__(self, name, salary):
        #co to?
        super(Employee, self).__init__(name)
        #ma(has-a)
        self.salary = salary

#jest(is-a)
class Fish(object):
    pass

#jest(is-a)
class Salmon(Fish):
    pass

#jest(is-a)
class Halibut(Fish):
    pass


#rover jest Dog(psem)
rover = Dog('Rover')

#jest(is-a)
satan = Cat("Satan")

#jest(is-a)
mary = Person("Mary")

#has-a
mary.pet = satan

#is-a
frank = Employee("Frank", 120000)

#has-a
frank.pet = rover

#is-a
flipper = Fish()

#is-a
crouse = Salmon()

#is-a
harry = Halibut()