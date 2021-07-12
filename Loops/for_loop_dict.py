user = {
    'name' : 'Golem',
    'age' : 5006,
    'can_swim' : False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key , val in user.items():#shorthand to unpack tuple and get key and val in one loop
    print(key , val)