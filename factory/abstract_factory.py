from abc import ABC, abstractmethod

class MainCourse(ABC):
    @abstractmethod
    def serve(self):
        pass

class Dessert(ABC):
    @abstractmethod
    def serve(self):
        pass

# 義大利菜系
class Pasta(MainCourse):
    def serve(self):
        return "Serving Italian pasta"

class Tiramisu(Dessert):
    def serve(self):
        return "Serving Italian tiramisu"

# 法式菜系
class Ratatouille(MainCourse):
    def serve(self):
        return "Serving French ratatouille"

class CremeBrulee(Dessert):
    def serve(self):
        return "Serving French crème brûlée"

class AbstractRestaurantFactory(ABC):
    @abstractmethod
    def create_main_course(self):
        pass

    @abstractmethod
    def create_dessert(self):
        pass

# 義大利餐廳
class ItalianRestaurantFactory(AbstractRestaurantFactory):
    def create_main_course(self):
        return Pasta()

    def create_dessert(self):
        return Tiramisu()

# 法式餐廳
class FrenchRestaurantFactory(AbstractRestaurantFactory):
    def create_main_course(self):
        return Ratatouille()

    def create_dessert(self):
        return CremeBrulee()

# 生成菜單
def create_dinner(factory: AbstractRestaurantFactory):
    main_course = factory.create_main_course()
    dessert = factory.create_dessert()
    print(main_course.serve())
    print(dessert.serve())

if __name__ == "__main__":
    print("Italian Dinner:")
    create_dinner(ItalianRestaurantFactory())

    print("\nFrench Dinner:")
    create_dinner(FrenchRestaurantFactory())
