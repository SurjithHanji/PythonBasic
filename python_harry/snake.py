import random


def check(compu,user):
    if(compu==user):
        print("its draw")
    if(compu==0 and user==1):
        return -1
    if(compu==1 and user==2):
        return -1
    if(compu==2 and user==0):
        return -1
    return 1

compu=random.randint(0,2)
user=int(input("0 for snake, 1 for water and 2 for gun"))

print("user:",user) 
print("computer:",compu)

score=check(compu,user)
if(score==0):
    print("its draw")
elif(score==-1):
    print("you lose")
else:
    print("you won")