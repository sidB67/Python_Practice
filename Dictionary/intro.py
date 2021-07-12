#unordered key value pair
#key has to be immutable
#key has to be unique as it gets overwritten
dictionary = {
    'a' : [1,2,3],
    'b' : 2
}


my_list = [
    {
    'a' : [1,2,3],
    'b' : 2
},
{
    'a' : 1,
    'b' : 2
}
]
print(dictionary['a'][1])
print(my_list[0]['a'][2])

#another way to make dictionary(less used)
dictionary2 = dict(name='Sid')
print(dictionary2)