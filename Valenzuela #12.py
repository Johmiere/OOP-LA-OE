class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        print(f"Toy Name: {self.name}")
        print(f"Price: ${self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

my_car = Car("Speedster", 25.99)
my_car.display_details()




