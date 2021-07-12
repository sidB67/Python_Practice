#formatted strings

name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age)+' years old')
#there is a better way to do above using fs
print(f'hi {name}. You are {age} years old')
#by adding f in print python accesses these variable as str 

#can also be done using .format in old python look it up if needed