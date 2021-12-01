# 1 Basic
for i in range(151):
    print(i)

# 2 Mulitples of Five
for m in range(5, 1001, 5):
    print(m)

# 3 Counting, the Dojo Way
for j in range(101):
    if j % 10 == 0:
        print("Coding Dojo")
    elif j % 5 == 0:
        print("Coding")
    else:
        print(j)

# 4 Whoa, That Sucker's Huge
oddsum = 0
for odd in range(1, 500001, 2):
    oddsum += odd
print(oddsum)

# 5 Countdown by Fours
for count in range(2018, 0, -4):
    print(count)

# 6 Flexible Counter
def my_counter(lowNum, highNum, mult):
    for val in range(lowNum, highNum + 1):
        if val % mult == 0:
            print(val)

my_counter(2, 9, 3)
my_counter(1, 40, 4)
my_counter(1, 100, 23)

the_number = 4
my_counter(1, the_number * 10, the_number)
