#unordered collection of unique objects

my_set = {1,2,3,4,5}
a_set = {1,2,3,4,4,5}
print(my_set)
print(a_set)

#to remove duplicates from lists
my_list = [1,1,2,3,4,5]
b_set = set(my_set)
print(b_set)

#we can copy a set
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)