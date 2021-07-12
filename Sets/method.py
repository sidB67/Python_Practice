my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

#to find difference between set

print(my_set.difference(your_set))#it doesnt change

#to remove element from a set
new_set = my_set.copy()
new_set.discard(5)
print(new_set)

#to update a given set to the difference between two sets
new_set = my_set.copy()
new_set.difference_update(your_set)
print(new_set)

new_set = {4,5}

#to find if two sets are disjoint
print(my_set.isdisjoint(your_set))

#to see if a set is a subset or not
print(new_set.issubset(your_set))

#to see if a set is a superset or not
print(new_set.issuperset(your_set))
print(your_set.issuperset(new_set))

#to find intersection
print(my_set.intersection(your_set))
#print(my_set & your_set ) is shorthand of above code



#to make union
print(my_set.union(your_set))
# print(my_set | your_set) is shorthand of above code