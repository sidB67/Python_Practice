a = 'hellooo'

if(len(a)>5):
    print(f'too long {len(a)} elements')

#the above code can be made better with walrus operator

if((n := len(a))>5): #here using walrus operator n will now have value of len(a) and can be used
   print(f'too long {n} elements')

while ((n:=len(a))>1):
    print(n)
    a=a[:-1]