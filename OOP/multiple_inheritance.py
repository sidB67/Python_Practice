class User():
   def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power) :
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows) :
        self.name = name
        self.num_arrows = num_arrows

    def check_arrow(self):
        print(f'Arrows left - {self.num_arrows}')
    
    def run(self):
        print('I am speed')

class ArWiz(Wizard,Archer): 
    def __init__(self, name, power,arrows):
        Archer.__init__(self,name, arrows)
        Wizard.__init__(self,name,power)
    pass

arwiz1 = ArWiz('ArWee',50,100)
arwiz1.run()
arwiz1.check_arrow()
arwiz1.attack()
arwiz1.sign_in()