#useful for functions we only need to use once
#anonymous function

#lambda param: action(param)

my_list = [1,2,3]
new_list = list(map(lambda item: item*2 , my_list))
new_list2 = list(filter(lambda item:item%2!=0,my_list))
print(new_list)
print(new_list2)