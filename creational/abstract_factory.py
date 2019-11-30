# Interface
class Door():
    def get_description(self):
        raise NotImplementedError

class WoodenDoor(Door):
    def get_description(self):
        print("I am a wooden door!")

class IronDoor(Door):
    def get_description(self):
        print("I am a iron door!")

# Interface
class DoorFittingExpert():
    def get_description(self):
        raise NotImplementedError

class Welder(DoorFittingExpert):
    def get_description(self):
        print("I can only fit iron doors!")

class Carpenter(DoorFittingExpert):
    def get_description(self):
        print("I can only fit wooden doors!")


# Interface
class DoorFactory():
    def make_door(self):
        raise NotImplementedError

    def make_fitting_expert(self):
        raise NotImplementedError

class WoodenDoorFactory(DoorFactory):
    def make_door(self):
        return WoodenDoor()

    def make_fitting_expert(self):
        return Carpenter()

class IronDoorFactory(DoorFactory):

    def make_door(self):
        return IronDoor()

    def make_fitting_expert(self):
        return Welder()

if __name__ == "__main__":
    wooden_factory = WoodenDoorFactory()
    door = wooden_factory.make_door()
    expert = wooden_factory.make_fitting_expert()

    door.get_description()
    expert.get_description()

