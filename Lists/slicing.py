#List slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes',
]

# print(amazon_cart[0])
# print(amazon_cart[2:])
# print(amazon_cart[0::2])

amazon_cart[0] = 'laptop' #lists are mutable
print(amazon_cart)

new_cart = amazon_cart[0:3] #list slicing creates a new list
new_cart[0] = 'gum'
print(new_cart)

a_cart = amazon_cart ##this doesnt create new list. any changes made to a_cart reflect in amazon_cart
a_cart[0] = 'box'
print(a_cart)
print(amazon_cart)
#copy a list
b_cart = amazon_cart[:]
b_cart[0]= 'knife'
print(b_cart)
print(amazon_cart)

                        
