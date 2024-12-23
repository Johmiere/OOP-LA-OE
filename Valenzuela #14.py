class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

tobey = Tobey("tobey maguire", 47, "Spider-Man")
andrew = Andrew("andrew garfield", 40, "The Amazing Spider-Man")
tom = Tom("tom holland", 28, "Spider-Man: Homecoming")

print(f"{tobey.name.upper()} - {tobey.movieTitle}")
print(f"{andrew.name.upper()} - {andrew.movieTitle}")
print(f"{tom.name.upper()} - {tom.movieTitle}")
