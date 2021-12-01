# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Kyeongeun"
print("Hello", name, "!")	# with a comma
print("Hello "+ name +"!")	# with a +
# 3. print "Hello 42!" with the number in a variable
number = 7
print("Hello ", number, "!")	# with a comma
print("Hello " + str(number) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "hawaiian pizza"
fave_food2 = "steak"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string


print(f"{name}'s favorite number is {number}!")

print(f"{name} loves to eat {fave_food1.title()} and {fave_food2.title().}")
print(f"{name.upper()} is upper.")
print(f"{name.lower()} is lower.")
print(f"{name} has {len(name)} letters.")
print(f"{name} has ng {name.count('ng')} time(s).")