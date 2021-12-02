# console.log("Hello World")
print("Hello world") # command + slash(/) + # makes it comment

"""
var y = "Whats up class?"
var z = "Whats cooking?"
console.log(y+z)
"""
y = "Whats up python class?"
print(f"this is message : {y}")
z = "Whats cooking?"
print(y+z)
print(f"{y} {z}")

print("comma version : My question is:", y, z) # be careful about automatic space
print("plus version  : My question is:" + y + z)
# This is f string formatting wher no , or + i required unless for the sentence
print(f"format version: My question is: {y}, {z}")

# Tuples, Lists, Dictionaries JS vs Python
# Tuples and Lists are similar to Arrays in JS
# however Tuples a immutable (can not change) where Lists are mutable

dog = ("Bear", "Abby", "Lucy", "Roxy", "Copper")
dogs = ["Bear", "Abby", "Lucy", "Roxy", "Copper"]
#print("tuple:", dog)
#print("list:", dogs)
# print("Just Lucy:", dog[2])
# print("Just Lucy:", dogs[2])

# dogs.pop()
# print(dogs)
# dog = ("Bear", "Abby", "Lucy", "Roxy")
# print(dog)

# Dictionary
copper = {'name': 'Copper', 'breed': 'Beagle', 'age': '6 months'}
print(copper['name'])
print(copper['age'])

copper['weight'] = '24lbs'
copper['color'] = ['brown', 'black', 'white']
print(copper)
copper.pop("weight")

print(copper)

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50: # never run...
        print("bigger than 50")
else:
    print("smaller than 10")

for x in range(0, 10, 2):