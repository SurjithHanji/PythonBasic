a=input("enter the number")
print(f"multiplication of table {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")

except ValueError:
    print("error regarding integer")
except IndexError:
    print("index error")