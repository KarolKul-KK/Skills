class Mammal:
     def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
   

class Cat(Mammal):
    def be_annoy(self):
      print("Annoy")  

cat1 = Cat()
cat1.walk()
cat1.be_annoy()