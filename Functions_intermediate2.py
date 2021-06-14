# 1) Update Values in Dictionaries and Lists
    # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 
a = x[0]
b = x[1]
b[0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
a = students[0]
b = students[1]
a['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# #2 Iterate Through a List of Dictionaries
    # should output: (it's okay if each key-value pair ends up on 2 separate lines;
    # bonus to get them to appear exactly as below!)
    # first_name - Michael, last_name - Jordan
    # first_name - John, last_name - Rosales
    # first_name - Mark, last_name - Guillen
    # first_name - KB, last_name - Tonel
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iteratedictionary(students):
    for iteration in students:
        for key, value in iteration.items():
            print(key, value)

iteratedictionary(students)

# 3) Get Values From a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iteratedictionary2(Key_name, some_list):
    for iteration in some_list:
        for key, value in iteration.items():
            print(value)
iteratedictionary2('first_name', students)
iteratedictionary2('last_name', students)

# 4) Iterate Through a Dictionary with List Values
#         Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
#         prints the name of each key along with the size of its list, and then prints the associated values within each 
#         key's list. For example:
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print(f'{len(some_dict[key])}{key}')
        for item in some_dict[key]:
            print(item)
printInfo(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
