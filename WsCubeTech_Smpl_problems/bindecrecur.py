def convertBinary(n):
    if n>1:
        convertBinary(n//2)

    print(n%2,end=" ")

print("binary of given number is:")

convertBinary(32)
