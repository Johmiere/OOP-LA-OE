class Adobo:
    def __init__(self, chicken, soysauce, vinegar, potato, rekados):
        self.__chicken = chicken
        self.__soysauce = soysauce
        self.__vinegar = vinegar
        self.__potato = potato
        self.__rekados = rekados

    def __str__(self):
        return f"My Adobo has {self.__chicken}, {self.__soysauce}, {self.__vinegar}, {self.__potato}, and {self.__rekados}"

    def get_chicken(self):
        return self.__chicken

    def set_chicken(self, new_chicken):
        self.__chicken = new_chicken

    def may_chicken_ba(self, age):
        if age <= 100:
            return self.get_chicken()
        else:
            return "Secret"

adobong_chicken = Adobo("sliced chicken", "soysauce", "vinegar", "potato", "rekados")
print(adobong_chicken.may_chicken_ba(60))  

adobong_chicken.set_chicken("whole chicken")  
print(adobong_chicken.may_chicken_ba(60))  