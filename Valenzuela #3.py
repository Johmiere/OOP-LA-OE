class MobileLegendHero:
  def __init__(self, hero_name, role):
    self.hero_name = hero_name
    self.role = role
  
  def describe_hero(self):
    print(f"{self.hero_name} is a {self.role} hero.")

hero = MobileLegendHero("Layla", "Marksman")
hero.describe_hero()
