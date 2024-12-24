def is_anagr(str1,str2):
    return sorted(str1)==sorted(str2)

s1=input('enter string1:')
s2=input("enter string2:")
if is_anagr(s1,s2):
    print("thery are anagrhms")
else:
    print("not")