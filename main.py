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
      
     def play(self):
        self.energy -= 10
        self.hunger += 5
        self.mood += 15
        print(self.name + " :Я пограв.")

    def check_status(self):
        print("Hunger: " + str(self.hunger))
        print("Energy: " + str(self.energy))
        print("Mood: " + str(self.mood))

cat = Cat("Борис", 2, "Темний")

while True:
    cat.check_status()
    action = input(cat.name + " хоче (eat/sleep/play/quit) ")
    if action == "eat":
        cat.eat()
    elif action == "sleep":
        cat.sleep()
    elif action == "play":
        cat.play()
    elif action == "quit":
        break
    else:
        print("Не пиши дурниць.")
    time.sleep(1)

  