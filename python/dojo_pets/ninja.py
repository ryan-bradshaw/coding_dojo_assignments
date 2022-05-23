from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        if(self.treats > 0):
            self.treats -= 1
        else:
            print("Oh no! I'm out of treats! I'll grab some more")
            self.treats =+ 5
        return self

    def bathe(self):
        self.pet.noise()
        print(self.pet.name + " got a bath. So clean!")
        return self

ryan = Ninja("Ryan", "Bradshaw", 10, "kibbles", Pet("Puppers", "dog", ["Roll-over"], 50, 30))

ryan.feed()
ryan.walk()
ryan.bathe()