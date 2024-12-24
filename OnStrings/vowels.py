def count_vowel(word):
    count=0
    vowels="aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            count+=1
    return count
word=input("entr a word:")
count=count_vowel(word)
print(count)
