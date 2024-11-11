from abc import ABC, abstractmethod

class Dish(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza(Dish):
    def prepare(self):
        return "Preparing a delicious pizza"

class Salad(Dish):
    def prepare(self):
        return "Preparing a fresh salad"

class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def prepare_dish(self):
        dish = self.factory_method()
        return dish.prepare()

class PizzaCreator(Creator):
    def factory_method(self):
        return Pizza()

class SaladCreator(Creator):
    def factory_method(self):
        return Salad()


if __name__ == "__main__":
    creator = PizzaCreator()
    print(creator.prepare_dish())  # Output: Preparing a delicious pizza

    creator = SaladCreator()
    print(creator.prepare_dish())  # Output: Preparing a fresh salad