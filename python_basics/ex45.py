class Person:
    
    
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"Hi, i am {self.name}")
        
Karol = Person('Karol')
Karol.talk()

bob = Person("Bob")
bob.talk()
