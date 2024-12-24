def is_pallindrome(str):
    return str==str[::-1]

str=input("enter a string:")
if is_pallindrome(str):
    print("pallindrome")
else:
    print("not")