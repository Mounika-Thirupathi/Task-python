# Inheritance:Accquring  the properties from parent class to child class
# Types of Inheritance:
# 1.single inheritance
# 2.multiple inheritance
# 3.multi level inheritance
# 4.hierarical inheritance
# 5.hybrid inheritance

# 1.single inheritance:Inherit properties from one parent class to one child class
class Animal:
    legs=4
    tail=1
    def sound(self):
        return "it  makes sounds "
class Dog(Animal):
    def sound1(self):
        return "it makes sound bow bow"
d1=Dog()
print(d1.legs)
print(d1.tail)
print(d1.sound())
print(d1.sound1())

# 2.hierarichal Inheritance:Inherit properties from one parent class to one or more child classes
class Animal:
    legs=4
    tail=1
    color="black"
    def sound(self):
        return "it makes sound"

class dog(Animal):
    def sound1(self):
        return "it sounds bow bow"
d1=dog()
print(d1.legs)
print(d1.tail)
print(d1.sound1())

class cat(Animal):
    def sound2(self):
        return "its sounds  meow meow"
c1=cat()
print(c1.legs)
print(c1.tail)
print(c1.sound2())

# 3.Multiple Inheritance:Multiple parent classes and single child class
class father:
    money="10000"
class mother:
    food="biryani"
class child(father,mother):
    result="A grade"
obj1=child()
print(obj1.money)
print(obj1.food)
print(obj1.result)

# 4.Multi level inheritance:multiple level of parents 
class grandparent:
    prop="10000"
gp=grandparent()
print(gp.prop)
class parent(grandparent):
    name="Mounika"
p=parent()
print(p.name)
print(p.prop)
class child(parent):
    surname="Thirupathi"
c=child()
print(c.prop)
print(c.name)
print(c.surname)    

# 5.Hybrid inheritance:combination of different inheritance
class A:
    name="A"
class B(A):
    name="B"
class C(A):
    name="C"
class D(B,C):
    name="D"
d1=D()
print(d1.name)



# Abstraction:hiding the internal details and providing the implementation details
from abc import ABC,abstractmethod
class device(ABC):
    @abstractmethod
    def welcome():
        pass
class mobile():
    def welcome():
        pass
m1=mobile()
print(m1)
class laptop():
    def welcome():
        pass
l1=laptop()
print(l1)