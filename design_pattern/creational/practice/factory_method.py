from abc import ABC, abstractmethod

class Creator():
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}\n"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "Result of the Concrete Product 1\n"

class ConcreteProduct2(Product):
    def operation(self):
        return "Result of the Concrete Product 2\n"

def client_code(creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    client_code(ConcreteCreator1())
    client_code(ConcreteCreator2())
