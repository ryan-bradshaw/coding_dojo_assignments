class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(self.name + " is sleeping soundly. Zzzzz...")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.name + " eats a snack! Mmmmm")
        return self
    
    def play(self):
        self.health += 10
        print(self.name + " is playing! Weee")
        return self

    def noise(self):
        if(self.type == "cat"):
            print("Meooowwwwwww")
            return self
        if(self.type == "dog"):
            print("Woof woof!")
            return self
        else:
            print("Mwraaraghghaghghg!")
            return self