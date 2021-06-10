# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
    # Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def a(list):
    for i in range(0, len(list), 1):
        if list[i] > 0:
            list[i] = "big"
print(a([-1,3,5,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
    # Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
    # Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# def positive(list)
#     for i in range(0, len(list), 1):
#         positivecount = list.count([i > 0)

test_list = [-1,1,1,1]
res = sum(1 for i in test_list if i > 0)
test_list[len(test_list) - 1] = res
print(test_list)

test_list = [1,6,-4,-2,-7,-2]
res = sum(1 for i in test_list if i > 0)
test_list[len(test_list) - 1] = res
print(test_list)


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
    # Example: sum_total([1,2,3,4]) should return 10
    # Example: sum_total([6,3,-2]) should return 7
def sumTotal(list):
    numbers_sum = sum(list)
    print(numbers_sum)
sumTotal([1,2,3,4])

# Average - Create a function that takes a list and returns the average of all the values.
    # Example: average([1,2,3,4]) should return 2.5
def average(list):
    average_num = sum(list)/len(list)
    print(average_num)
average([1,2,3,4])

# Length - Create a function that takes a list and returns the length of the list.
    # Example: length([37,2,1,-9]) should return 4
    # Example: length([]) should return 0
def length_list(list):
    length = len(list)
    print(length)
length_list([37,2,1,-9])

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
    # Example: minimum([37,2,1,-9]) should return -9
    # Example: minimum([]) should return False
def min_list(list):
    if len(list) > 0:
        print(f"Minimum value in list is {min(list)}")
    else:
        return False
min_list([37,2,1,-9])

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
    # Example: maximum([37,2,1,-9]) should return 37
    # Example: maximum([]) should return False
def max_list(list):
    if len(list) > 0:
        print(f"Maximum value in list is {max(list)}")
    else:
        return False
max_list([37,2,1,-9])
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
    # Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
keys = ['sumTotal', 'average', 'minimum', 'maximum', 'length']
def new_dict(list):
    result = {keys[0]: sum(list), keys[1]: sum(list)/len(list), keys[2]: min(list), keys[3]: max(list), keys[4]: len(list)}
    return result
print(new_dict([37,2,1,-9]))
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
    # Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_reverse(list):
    list.reverse()
    return list
print(reverse_reverse([37,2,1,-9]))
