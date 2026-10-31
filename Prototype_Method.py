
import copy


# 1. Original class
class GameCharacter:

    def __init__(self, name, health, weapon, level):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.level = level

    def show_details(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Weapon:", self.weapon)
        print("Level:", self.level)


# 2. Create original object
warrior = GameCharacter(
    "Warrior",
    100,
    "Sword",
    5
)


# 3. Clone the existing object
new_warrior = copy.copy(warrior)

# 4. Modify cloned object
new_warrior.name = "Dark Warrior"
new_warrior.weapon = "Axe"


# 5. Display both objects
print("Original Character:")
warrior.show_details()

print("\nCloned Character:")
new_warrior.show_details()
