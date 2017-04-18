#!/usr/bin/env python


class Car(object):
    """docstring for Car."""
    wheels = 4
    def __init__(self, model, make):
        self.make = make
        self.model = model
    @staticmethod
    def make_car_sound():
        print Vrooooom!

# mustang = Car('Ford', 'Mustang')
# print mustang.wheels
# print Car.wheels
