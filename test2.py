import random
line=['leon','kipkoech']
names=[]
for name in line:
    names.append(name)
    
random_number= random.randrange(1,3)
random_name=names[random_number-1]

print (random_name)
