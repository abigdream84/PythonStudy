#!/usr/bin/env python
#coding:UTF-8

class Car(object):

    material = 'metal'
    
    def __init__(self, brand, colour):
        self.Brand = brand
        self.Colour = colour

    def move(self, direction):
        print(direction)
    
    @staticmethod
    def bar():
        print('staticmethod1')



car1 = Car('BMW', 'Red')
#print(car1.Brand)
#print(car1.Colour)
#print(Car.material)
#car1.move('backward')
Car.bar()







