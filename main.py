class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"My name is {self.name} and I can bark")

class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"My name is {self.name} and I can meow")

Sparky = Dog("Sparky")
Meowth = Cat("Meowth")

pets = (Sparky, Meowth)

for pet in pets:
    pet.make_sound()
