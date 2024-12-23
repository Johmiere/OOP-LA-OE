class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage!")
        print(f"{target.name}'s remaining health: {target.health}")
    
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed for {amount} health!")
        print(f"{self.name}'s current health: {self.health}")

player1 = Player("Warrior", 100, 20)
player2 = Player("Mage", 80, 25)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player2.name} has been defeated! {player1.name} wins!")
        break
    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player1.name} has been defeated! {player2.name} wins!")
        break

player1.heal(10)
player2.heal(15)

