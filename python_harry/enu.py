marks=[23,12,13,4,56,78]
index=0
for mark in marks:
    print(mark)
    if(index == 3):
        print("harry,awesome!")
    index+=1

marks=[23,12,13,4,56,78]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("harry,awesome!")
    