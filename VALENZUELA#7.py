
class Car:
    def __init__(self, brand, color):
        self.brand= brand
        self.color= color
kotse= Car("Ford", "Black")
print(f"Original Value: {kotse.brand}, {kotse.color}")
kotse.color= ("Red")
print(f"Updated Color: {kotse.color}")
sasakyan=Car("Ford Ranger", "White")
print(f"Another Car: {sasakyan.brand}, {sasakyan.color}")
