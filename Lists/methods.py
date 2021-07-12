basket = [1,2,3,4,5]

#adding to end of list
basket.append(100)#changes the list doesnt create new one 
print(basket)

#adding to any index
basket.insert(3,200)
print(basket)

#extend method 
basket.extend([300,400])#requires an iterable not obj. add it to the end
print(basket)

#to see if something is in list
print(basket.index(1))#this will return index
print(1 in basket)#this will return true if exists

#count how many time a val occurs
print(f"No of time = {basket.count(100)}"  )
print(f"No of time = {basket.count(10)}"  )

#reverse
basket.reverse()#this just reverses indices
print(basket)

#sorting list
basket.sort() #use sorted(basket) to make a new list which is basket sorted
print(basket)

#removing
basket.pop()#by defualt removes from end but can specify index
basket.pop(2)#this will return the data it pops
print(basket)

#removing a value
basket.remove(4)
print(basket)

#clearing
basket.clear()
print(basket)