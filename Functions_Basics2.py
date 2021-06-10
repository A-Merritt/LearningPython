# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) 
# down to 0 (as the last element).
def downOne():
    list = []
    val = input("Enter a integer:")
    for i in range(int(val), 0, -1):
        list.append(i)
    return list
a = downOne()
print (a)

# Example: countdown(5) should return [5,4,3,2,1,0]
def fromFive():
    for i in range(5, -1, -1):
        print(i)
fromFive()

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def list2numbers(b,c):
    print(b)
    test = c
    return test
var = list2numbers(1,2)
print(var)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
list = (1,2,3,4,5)
def a(list):
    sum = 0
    sum = list[0] + len(list)
    return(sum)
a(list)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
def a(orig_list):
    new_list = []
    second_val = orig_list[1]
    for i in range(len(orig_list)):
        if orig_list > second_val:
            new_list.append(orig_list[i])
    print(len(new_list))
    return new_list
print(a([5,2,3,2,1,4]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# input("Please provide a size:")
# input("Please provide a value:")
def lengthAndValue(b,c):
    y = b + c
    print(y)
    list = [c] * b
    print(list)
lengthAndValue(4,7)
lengthAndValue(6,2)