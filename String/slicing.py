#this is done using []
#[start:stop:stepover]

slefish = '01234567'
print(slefish[0])
print(slefish[0:8])#here stop isnt included
print(slefish[0:8:2])#it will no stepover by 2
print(slefish[1:])#this will say start and 1 and now nothing so it goes tll end
print(slefish[:5])#start at defualt 0 goes to 5

#we can use -ve index and start from end

print(slefish[::-1])#reverse