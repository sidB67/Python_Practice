#enumarate gives the index and the corresponding item in the iterable

for i,char in enumerate('abc'):
    print(i,char)

for i , num in enumerate(list(range(100))):
    if(num == 50):
        print(i)