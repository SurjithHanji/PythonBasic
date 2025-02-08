a=input("enter the number")
print(f"multiplication of table {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")

except Exception as e:
    print(e)
    print("sry some error")

except:
    print("inval")

print("some lines of code")
print("end of program")