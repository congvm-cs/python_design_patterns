""" Interface Segregation Principle

A client should never be forced to implement an interface 
that it doesn't use or clients shouldn't be forced to depend 
on methods they do not use


Example:
-> Square has no depth so no need to implement volume method
"""

class ShapeInterface():
    def area(self):
        raise NotImplementedError

class SolidShapeInterface():
    def volume(self):
        raise NotImplementedError

class Square(ShapeInterface):
    def __init__(self, w, h):
        self._w = w
        self._h = h

    def area(self):
        return self._w * self._h

class Cubic(SolidShapeInterface, ShapeInterface):
    def __init__(self, w, h, c):
        self._h = h
        self._w = w
        self._c = c

    def area(self):
        return self._w * self._h

    def volume(self):
        return self._w * self._h * self._c


if __name__ == "__main__":
    cubic = Cubic(10, 20, 30)
    print(cubic.volume())
    print(cubic.area())

