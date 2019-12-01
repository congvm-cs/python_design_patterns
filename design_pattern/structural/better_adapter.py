# https://refactoring.guru/design-patterns/adapter

class TargetAbstract():
    """ A class that contains the existing bussiness logic of the program
    """
    def request(self):
        raise NotImplementedError

class Target(TargetAbstract):
    """Describe a protocol that other classes must follow to be able
       collaborate with the client code.
    """
    def request(self):
        return f"{self.__class__.__name__}: The default Target's behavior"

class Adaptee():
    """ Some useful class (usually 3rd-party or legacy). The client can't use this
    class directly because it has an incompatible interface
    """
    def specific_request(self):
        return f"{self.__class__.__name__}: The default Adaptee's behavior"

class Adapter(TargetAbstract):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

def client_code(target):
    print(target.request())

if __name__ == "__main__":
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
