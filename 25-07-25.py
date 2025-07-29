
# class=class is a blue print of an object
# object=object is an instance of a class
# syntax of class: class keyword followed by class name
# syntax of object:variable name =class name followed by paranthesis

class car:
    seats=4
    wheels=4
    color="black"
    def sound(self):
        return "car has different sounds"
c1=car()
print(c1.wheels)
print(c1.seats)
print(c1.color)
print(c1.sound())

# constructor:a constructor is a special type of method created automatically when object is created
class laptop:
    brand="hp"
    def __init__(self,ram,storage,cpu):
        self.ram=ram
        self.storage=storage
        self.cpu=cpu
    def fun(self,val):
        self.ram=val
        return self.ram
l1=laptop("16gb","512gb","i5")
print(l1.ram)
print(l1.storage)
print(l1.cpu)
print(l1.fun())

# Four Pillars Of oops
# 1.Inheritance
# 2.Abstraction
# 3.encapsulation
# 4.polymorphism

# 1.Inheritance:Inheriting the properties from one class to another class
# Types Of Inheritance:
# single
# Multiple
# Multi level
# hierarical
# hybrid

# single inheritance:Inheriting properties from one parent class to child class
# Example:
class animal:
    legs=4
    tail=1
    def sound(self):
        return "it makes sound"
class cat(animal):
    def sound1(self):
        return "it makes meow meow"
c1=cat()
print(c1.legs)
print(c1.tail)
print(c1.sound())

# Multiple inheritance:In multiple inheritance multiple parent classes and one child class
class father:
    money="100000"
class mother:
    food="dosa"
class child(father,mother):
    def fun(self):
        return "enjoy"
c1=child()
print(c1.money)
print(c1.food)
print(c1.fun())

# Multilevel Inheritance:
class grand:
    prop="10000"
g1=grand()
print(g1.prop)
class parent(grand):
    surname="Thirupathi"
p1=parent()
print(p1.prop)
print(p1.surname)
class child(parent):
    name="Mounika"
c1=child()
print(c1.prop)
print(c1.surname)
print(c1.name)

# Hierarical inheritance:one parent class and multiple child classes
class animal:
    legs=4
    tail=1
    def fun(self):
        return "it makes sound"
class cat(animal):
    def sound(self):
        return "it makes meow meow"
c1=cat()
print(c1.legs)
print(c1.tail)
print(c1.sound())

class dog(animal):
    def sound1(self):
        return "it makes bow bow"
d1=dog()
print(d1.legs)
print(d1.tail)
print(d1.sound1())

class monkey(animal):
    def sound3(self):
        return "it makes different sound"
m1=monkey()
print(m1.legs)
print(m1.tail)
print(m1.sound3())

# Hybrid inheritance:combination of different inheritance
class A:
    legs=4
class B(A):
    legs=3
class C(A):
    legs=2
class D(B,A):
    legs=1
d1=D()
print(d1.legs)
    
# 2.polymorphism:same methods having different functionalities
class laptop:
    def fun(self):
        return "it used for work"
class dell:
    def fun(self):
        return "it is used for dell work"
class hp:
    def fun(self):
        return "it is used for hp work"
class lenovo:
    def fun(self):
        return "it is used for lenovo work"
l1=laptop()
print(l1.fun())
d1=dell()
print(d1.fun())
h1=hp()
print(h1.fun())
l1=lenovo()
print(l1.fun())

# 3.encapsulation:binding data and methods
class car:
    wheels=4
    seats=3
    colour="black"
    def fun(self):
        return "it used to travel"
c1=car()
print(c1.wheels)
print(c1.seats)
print(c1.colour)
print(c1.fun())

# 4.Abstraction:hiding internal details and providing implementation details
from abc import ABC, abstractmethod
class device(ABC):
    def welcome(self):
        pass
class mobile(device):
    def welcome(self):
        pass
m1=mobile()
print(m1.welcome())

class laptop(device):
    def welcome(self):
        pass
l1=laptop()
print(l1.welcome())

# call back:when function is used as parameter in another function or used in another function
# example :Addition of two number and finding whether it is even or not 
def addition(a,b,fun):  
    return fun(a+b)
def is_even(n):
    return n%2==0
print(addition(2,2,is_even))

# is_even is a call back function

#higher order:when function holds another function as a parameter or returns another function or both 
# example:
def addition(a,b,fun):
    return fun(a+b)
def is_even(n):
    return n%2==0
print(addition(2,2,is_even))

# addition is a higher order function

# write a program to print multiplication of a number with 2
l1=[1,2,3,4,5,6]
out=[]
for i in l1:
    out.append(i*2)
print(out)

# based on call back-->Map,filter
# Map:Map is used to return boolean value on conditions and return value on operations
# Filter:Filter is used to return  value on conditions
# syntax of map:Map(function,iterable)
# syntax of filter:Filter(function,iterable)

# Examples on maps on user defined functions on list
l1=[1,2,3,4,5,6]
def multiply(n):
    return n*2
    return n%2==0
print(list(map(multiply,l1)))      
print(list(filter(multiply,l1)))  
print(list(map(multiply,l1)))  

# using lambda function on list
print(list(map(lambda x:x%2==0,l1)))
print(list(filter(lambda x:x%2==0,l1)))

l1=["ganesh","arvind","srivali","savitri"]
print(list(map(lambda x:len(x)>=6,l1)))
print(list(filter(lambda x:len(x)>=6,l1)))

s=map(lambda x:len(x)>=6,l1)
print(list(s))

s=filter(lambda x:len(x)>=6,l1)
print(list(s))

# using isinstance method to find the data type
ele=["h1",1,"hello",[2,3,4],(4,5,6),{"name":"mani"},"world"]
print(list(filter(lambda x:isinstance(x,str),ele)))
print(list(map(lambda x:isinstance(x,str),ele)))

 
print(list(filter(lambda x:isinstance(x,str) or isinstance(x,int),ele)))
print(list(map(lambda x:isinstance(x,str) or isinstance(x,int),ele)))
print(list(map(lambda x:not isinstance(x,str),ele)))
print(list(filter(lambda x:not isinstance(x,str),ele)))