
user = {
    'basket' : [1,2,3],
    'greet' : 'hello'

}

print(user.get('age'))#if doesnt exist by default return none
print(user.get('age', 55))#will give 55 if doesnt exist

#to check for keys
print('basket' in user.keys())#user.keys() gives a set of keys in a dict
print(user.keys())
#to check for values
print('hello' in  user.values())#user.values tells about values of dict
print(user.values())

#to copy a dict
user2 = user.copy()
print(user)
print(user2)

#to update and add a key value pair
user.update({'age':55})
user.update({'greet':'hi'})
print(user)

#to remove key 
user.pop('greet')#works same as list pop and returns the value
print(user)

#to clear a dict
user.clear()
print(user)