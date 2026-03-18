# Game Character Stats Tracker

# This program defines a GameCharacter class to track a character's name, health, mana, and level. It includes validation for health and mana values, as well as a method to level up the character, which resets health and mana to their maximum values.
class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        elif value > 50:
            self._mana = 50
        else:
            self._mana = value

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f'{self.name} leveled up to {self.level}!')

    def __str__(self):
        return f'Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}'


# Example usage
hero = GameCharacter('Kratos')
print(hero)

hero.health -= 30
hero.mana -= 10
print(hero)

hero.level_up()
print(hero)

# Output:

# Name: Kratos
# Level: 1
# Health: 100
# Mana: 50
# Name: Kratos
# Level: 1
# Health: 70
# Mana: 40
# Kratos leveled up to 2!
# Name: Kratos
# Level: 2
# Health: 100
# Mana: 50