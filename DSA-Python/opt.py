n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<0 or num>110:
        print(hash_list[num])
    else:
        print(0)
        