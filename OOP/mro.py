#Method Resolution Order
#It is the way in which python determines which method to run in Inheritance
class A():
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

print(D.num)
print(D.mro())#this will show the order