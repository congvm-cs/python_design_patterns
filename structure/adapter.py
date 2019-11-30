# interface
class Lion():
    def roar(self):
        raise NotImplementedError

class AfricanLion(Lion):
    def roar(self):
        print(self.__class__.__name__, "roar")

class AsianLion(Lion):
    def roar(self):
        print(self.__class__.__name__, "roar")

class Hunter():
    def hunt(self, lion_ins: Lion):
        lion_ins.roar()

class WildDog():
    def bark(self):
        print(self.__class__.__name__, "bark")

class Wolf():
    def bark(self):
        print(self.__class__.__name__, "bark")


class WildDogAdapter(Lion):
    def __init__(self, wild_dog: WildDog):
        self.dog = wild_dog

    def roar(self):
        return self.dog.bark()
    
class DogAdapter(Lion):
    def __init__(self, dog: Lion):
        self.dog = dog

    def roar(self):
        return self.dog.bark()


if __name__ == "__main__":
    hunter = Hunter()

    # ===========================
    wild_dog = WildDog()
    wild_dog_adapter = WildDogAdapter(wild_dog)
    hunter.hunt(wild_dog_adapter)

    # ===========================
    wolf = Wolf()
    wolf_adapter = DogAdapter(wolf)
    hunter.hunt(wolf_adapter)