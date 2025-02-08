try:
    l=[1,2,3,4]
    i=int(input("enter the index :"))
    print(l[i])
except:
    print("some error")

finally:
    print("i am always executed")