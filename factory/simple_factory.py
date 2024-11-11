class Pizza:
    def prepare(self):
        return "Preparing a delicious pizza"

class Salad:
    def prepare(self):
        return "Preparing a fresh salad"

class SimpleFactory:
    @staticmethod
    def create_dish(dish_type):
        if dish_type == 'pizza':
            return Pizza()
        elif dish_type == 'salad':
            return Salad()
        else:
            raise ValueError("Unknown dish type")

if __name__ == "__main__":
    dish = SimpleFactory.create_dish('pizza')
    print(dish.prepare())  # Output: Preparing a delicious pizza