l=[1,2,3,4,5,4,3,6,7]
m=[8,7,6,1,4,3]
for num in m:
    count=0
    for x in l:
        if num==x:
            count+=1
    print(f'{count}')