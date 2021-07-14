from functools import reduce

def accumulator (acc,item):#here acc will be initial val given in reduce and item will be the ele of iterable given(here list)
    return acc+item

my_list = [1,2,3]

print(reduce(accumulator,my_list,0))#this will reduce to a single value