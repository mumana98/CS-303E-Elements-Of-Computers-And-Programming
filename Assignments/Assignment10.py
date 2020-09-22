#Matthew Umana msu245

class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        return self.health

    def __str__(self):
        print(str(self.name) + "(" + "health=" + str(self.health) + ")")
    
class Hero(Character):

    def __init__(self, name, health):
        super().__init__(name, health)
        self.__inventory = []

    def restore_health(self, restore):
        self.health += restore

    def add_inventory(self, item):
        self.__inventory.append(item)

    def remove_inventory(self, item):
        self.__inventory.remove(item)

    def get_inventory(self):
        return self.__inventory
        
class Enemy(Character):
    
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage


def main():
    Han = Hero("Han", 40)
    Zombie = Enemy("Zombie", 20, 15)
    Werewolf = Enemy("Werewolf", 15, 10)

    print("Start: \n" + "Han " + "(health=" + str(Han.health) + ")\n" +
          "Zombie " + "(health=" + str(Zombie.health) + ")\n" +
          "Werewolf "+ "(health=" + str(Werewolf.health) + ")")
    print("Battle 1:")
    Han.take_damage(Werewolf.damage)
    Werewolf.take_damage(10)
    print("Han " + "(health=" + str(Han.health) + ")\n" +
          "Werewolf "+ "(health=" + str(Werewolf.health) + ")")
    print("Battle 2:")
    Han.take_damage(Zombie.damage)
    Zombie.take_damage(20)
    print("Han " + "(health=" + str(Han.health) + ")\n" +
          "Zombie "+ "(health=" + str(Zombie.health) + ")")
    print("Restore Health:")
    Han.restore_health(5)
    print("Han " + "(health=" + str(Han.health) + ")")
    print("Inventory:")
    Han.add_inventory("gold coin")
    Han.add_inventory("candle")
    print(Han.get_inventory())
    
if __name__ == '__main__':
    main()
    
    
