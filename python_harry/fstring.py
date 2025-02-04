# fstrings

letter="hey my name is {1} i am from {0}"
country="India"
name="Harry"
# print(letter.format(name,country))
print(letter.format(country,name))


print(f"hey my name is {name} i am from {country}")