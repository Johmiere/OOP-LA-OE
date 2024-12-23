class FavoriteFood:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} is made with: {', '.join(self.ingredients)}"

food1 = FavoriteFood("Pizza", ["dough", "cheese", "tomato sauce", "pepperoni"])
food2 = FavoriteFood("Pasta", ["noodles", "tomato sauce", "cheese", "basil"])
food3 = FavoriteFood("Burger", ["bun", "patty", "cheese", "lettuce", "tomato"])

print(food1)
print(food2)
print(food3)

