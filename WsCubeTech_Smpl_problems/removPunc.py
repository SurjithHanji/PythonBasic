str=input("ente the string which contains punctuaions:")
punc=''' !()-[]{}:'"\,.<>?/@#$%^&*'''

empty_str =" "
for i in str:
    if i not in punc:
        empty_str += i
print(empty_str)