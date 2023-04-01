import time

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
        self.hunger = 50
        self.energy = 50
        self.mood = 50
      
    def eat(self):
        self.hunger -= 10
        self.energy += 10
        self.mood += 5
        print(self.name + " :Я затоптав борща з салом.")

    def sleep(self):
        self.energy += 20
        self.hunger += 5
        self.mood += 10
        print(self.name + " :Я добряче поспав.")

  