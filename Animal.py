# This is the parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"This animal says {sound}")

    def describe(self):
        return f"{self.name} is a {self.species}."

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is now sleeping.")
        
    def play(self):
        print(f"{self.name} is playing.")

# This is the child class
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")
        self.favorite_toy = "Bone"

    def make_sound(self, sound = "Woof"):
        return sound
    
    def play(self):
        print(f"{self.name} is playing with {self.favorite_toy}.")

# This is another child class    
class Cat(Animal):
    def __init__(self, name, species = "Cat"):
        super().__init__(name, species)
        self.favorite_toy = "Feather"

    def make_sound(self):
        return "Meow!"

    def nap(self):
        print(f"{self.name} is now napping after playing with {self.favorite_toy}.") 

# This is the main function    
if __name__ == "__main__":
    d = Dog("Rex")
    print(d.make_sound())
    print(d.describe())
    print(d.eat("Dog food"))
    print(d.play())
    
    c = Cat("Whiskers", "Cat")
    print(c.make_sound())
    print(c.describe())
    print(c.eat("Cat food")) 
    print(c.nap())