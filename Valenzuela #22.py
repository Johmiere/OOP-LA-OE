class BirthdayParty:
    def __init__(self, theme, foods, special_dish, secret_dish):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
        self.secret_dish = secret_dish  

    def print_food_list(self):
        print(f"Party Theme: {self.theme}")
        print("Food Menu:")
        for food in self.foods:
            print(f"- {food}")
        print(f"Special Dish: {self.special_dish}")
        print(f"Secret Dish: {self.secret_dish}")

party1 = BirthdayParty("Superhero", ["Pizza", "Popcorn", "Cake"], "Spiderman Cupcakes", "Chocolate Lava Cake")
party2 = BirthdayParty("Under the Sea", ["Fish and Chips", "Shrimp Cocktail", "Seaweed Salad"], "Octopus Cake", "Rainbow Ice Cream")
party3 = BirthdayParty("Space Adventure", ["Astronaut Cookies", "Galaxy Cupcakes", "Star-Shaped Pizza"], "Rocket Ship Cake", "Cosmic Brownies")


party1.print_food_list()
print("-" * 20)
party2.print_food_list()
print("-" * 20)
party3.print_food_list()