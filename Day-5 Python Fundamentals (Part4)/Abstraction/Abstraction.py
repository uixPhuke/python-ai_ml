#Hiding Internal Details
#And Showing Only Essential Features

#Diff between Data Hiding(public,protected,private) and Abstraction

#It has Abstract classes (BluePrint for OTHER classes)

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar !")
class Cat(Animal):
    def make_sound(self):
        print("Meow !")


lion=Lion() #lion is created as Object
lion.make_sound()

cat=Cat()
cat.make_sound()

