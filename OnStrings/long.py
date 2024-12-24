sent=input("entr a sentence")
words=sent.split()
maximaum=max(len(word) for word in words)
print(maximaum)