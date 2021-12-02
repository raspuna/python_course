#1 countdown
def countdown(num):
    countdown_list = []
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list

print(countdown(5))
# print(countdown(7))
# print(countdown(11))

#2 Print and Return
def print_and_return(num1, num2):
    print(num1)
    return num2

print_and_return(1,2)
#print_and_return(4,7)


#3 Frist Plus Length
def first_plus_length(num_list):
    return num_list[0] + len(num_list)

#print(first_plus_length([3,4,1,8]))
print(first_plus_length([1,2,3,4,5]))

#4 Values Greater than Second
def values_greater_than_second(num_list):
    if (len(num_list) < 2):
        return False
    new_list = []
    for i in num_list:
        if i > num_list[1]:
            new_list.append(i)
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5 This Length, That Value
def length_and_value(num1, num2):
    val_list = [ num2 for i in range(num1) ]
    return val_list

print(length_and_value(4,7))
print(length_and_value(6,2))

