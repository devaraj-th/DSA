class Pet:

    def __init__(self,name):

        self.name = name
        self.hunger = 5


    def feed (self):

        self.hunger -=1

        print(f"{self.name} has been fed")

        print(f"{self.name}'s current hunger level is {self.hunger}")




pet_1 = Pet('Boom')

pet_1.feed()
pet_1.feed()
pet_1.feed()
        