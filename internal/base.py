from __future__ import print_function

import objects

	
class BuilderInterface:
    def set_wheels(self, value):
        pass
    def set_seats(self, value):
        pass
    def set_color(self, value):
        pass
    def get_result(self):
        pass

# we need one of these per product
class ConcreteBuilder(BuilderInterface):
    def __init__(self):
        self.car = Product()

    def set_wheels(self, value):
        self.car.wheels = value

    def set_seats(self, value):
        self.car.seats = value

    def set_color(self, value):
        self.car.color = value

    def get_result(self):
        return self.car
