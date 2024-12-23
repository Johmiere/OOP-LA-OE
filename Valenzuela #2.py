class MobileLegendHero:
  def __init__(self, hero_name, role):
    self.hero_name = hero_name
    self.role = role

hero = MobileLegendHero("Alucard", "Fighter")
print(hero.hero_name)
print(hero.role)