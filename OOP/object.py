class PlayerCharacter():
    #Class Object Attribute
    membership = True #all objects that instantiate will have this and 
                      #it will be same for all by default.... 
                      # can be changed using constructor

    def __init__(self,name,age):#this is a constructor
        if(self.membership):
            self.name = name #attributes
            self._age = age #no true private members _ indicates it is to be treated as private

        

    def run(self):
        print('run')
    
    def shout(self):
        print(f'My name is {self.name}')

    @classmethod #this a method which can also be accessed without instantiating and obj
    def adding_things(cls,num1,num2):
        return num1+num2

    @staticmethod #this is same as classmethod but doesnt have access to cls
    def add(num1,num2):
        return num1+num2

player1 = PlayerCharacter('Sid',19)
player2 = PlayerCharacter('SidB',19)

player1.shout()
player2.shout()
print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(2,4))
print(PlayerCharacter.add(1,2))
        