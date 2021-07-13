class User():
    def __init__(self,email) :
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power,email) :
        super().__init__(email)#to call the base class init super refers to base class
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows,email) :
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin',50,'merlinthewiz@gmail.com')
archer1 = Archer('Robin',100,'robinthehood@gmail.com')

wizard1.sign_in() #inherited from User
archer1.sign_in() #inherited from User

wizard1.attack()#attack of wizard
archer1.attack()#attack of archer

print(wizard1.email)
print(archer1.email)