""" Simple Factory
Simple factory simply generates an instance for client without exposing any instantiation
logic to client

- When to Use?

When creating an object is not just a few assignments and involves some logic, it makes sense to
put it in a dedicated factory instead of repeating the same code everywhere

"""

class Door():
    def get_width(self):
        raise NotImplementedError

    def get_height(self):
        raise NotImplementedError


class WoodenDoor(Door):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height


class DoorFactory():

    @classmethod
    def make_door(self, width, height):
        return WoodenDoor(width, height)


if __name__ == "__main__":    
    door = DoorFactory.make_door(100, 200)
    print(door.get_height())
    print(door.get_width())

    door = DoorFactory.make_door(200, 50)
    print(door.get_height())
    print(door.get_width())
