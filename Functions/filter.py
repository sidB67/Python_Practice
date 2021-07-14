def check_odd(item):
    if(item % 2 != 0 ):
        return item


my_list = [1,2,3]
new_list = list(filter(check_odd,my_list))#this filters each item of given data with help of given function and creates new list(in this case)


print(new_list)
print(my_list)#filter doesnt change the data given