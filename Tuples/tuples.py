#they are like lists but immutable

my_tuple = (1,2,3,4,5)

print(my_tuple[1])#we can access but cant change ele

#we can create a new tuple using slicing of old
new_tuple = my_tuple[1:4]
print(new_tuple)

#we can unpack tuple in same way as tuple
a,b,c, *other = (1,2,3,4,5,6)
print(a)
print(b)
print(c)
print(other)

#only two methods
print(my_tuple.count(3))#counts occurence of given value
print(my_tuple.index(4))#tell index of given val

#we can find its length
print(len(my_tuple))