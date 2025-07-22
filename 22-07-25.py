# Create a parent class name Vehicle and create 3 child classes to inherit the properties of parent class.
class vehicle:
    wheels=4
    seats=3
    color="black"
class Bike(vehicle):
    wheels=3
b1=Bike()
print(b1.wheels)
print(b1.seats)

class car(vehicle):
    seats=4
c1=car()
print(c1.seats)
print(c1.wheels)

class helicopter(vehicle):
    wings=2
h1=helicopter()
print(h1.wings)
print(h1.color)
    

    