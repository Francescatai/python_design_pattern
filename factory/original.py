class Pizza:
    def prepare(self):
        return "Preparing a delicious pizza"

class Salad:
    def prepare(self):
        return "Preparing a fresh salad"


if __name__ == "__main__":
    dish_type = input("Enter the dish type (pizza/salad): ").strip().lower()

    if dish_type == 'pizza':
        dish = Pizza()
    elif dish_type == 'salad':
        dish = Salad()
    else:
        raise ValueError("Unknown dish type")

    print(dish.prepare())