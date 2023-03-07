class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise
        self.health = 100
        self.energy = 50
        
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)
        return self


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        print(f"{self.pet.name} is ready for a walk")
        print(f"{self.pet.name} energy level: {self.pet.energy}")
        return self
        
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}")
            self.pet.eat()
        else:
            print("You need more pet food.")
        return self

    def bathe(self):
        self.pet.noise()
        return self

my_treats = ['Bacon', 'Sausage']
pet_food = ['Pizza', 'Tacos', 'burgers']

bruce = Pet("Bruce", "Dog", ['jumps', 'roll over'], "Woof")
ninja1 = Ninja("Chad","Popp",my_treats, pet_food, bruce)

ninja1.walk().feed().bathe()
ninja1.feed()
ninja1.feed()
ninja1.feed()
