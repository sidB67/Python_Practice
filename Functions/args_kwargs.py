# *args **kwargs

def super_func(*args): #we can accept any number of positional arugemnts
    print(args)#gives a tuple of arguements
    return sum(args)

print(super_func(1,2,3,4,5))
print(super_func(1,2,3))

def super_fun2(*args , **kwargs):#**kwargs accepts any no of keywords arguements
    print(kwargs)#this gives a dict
    total = 0
    for items in kwargs.values():
        total+= items
    return sum(args) + total

print(super_fun2(1,2,3,4,5,num1=2,num2=1,num3=3))
