class Pet:

    def __init__(self,name,family,hunger:int,power:int):

        self.name = name
        self.family = family
        self.hunger = hunger
        self.power = power






pet_1 = Pet('billy1','cat',7,9)

pet_2 = Pet('billy2','cat',9,10)

print(f"first pet is {pet_1.name} belongs to {pet_1.family} family and has hunger levels {pet_1.hunger} and power {pet_1.power}")