class Adobo:
    def __init__(self, chicken, soysauce, vinegar, potato, rekados):
        self._chicken = chicken
        self._soysauce = soysauce
        self._vinegar = vinegar
        self._potato = potato
        self._rekados = rekados

    def __str__(self):
        return f"My Adobo has {self._chicken}, {self._soysauce}, {self._vinegar}, {self._potato}, and {self._rekados}"

    def get_chicken(self):
        return self._chicken

adobong_chicken = Adobo("chicken", "soysauce", "vinegar", "potato", "rekados")
print(adobong_chicken.get_chicken()) 

