def multiplyby_2(item):
    return item*2

my_list = [1,2,3]
list1 = list(map(multiplyby_2,my_list)) #map function performs the action(first arguement which is a function)
                                        #on each ele of data(iterable,second arg) provided to it

print(list1)
print(my_list)#map doesnt change the data it recieves return a new one