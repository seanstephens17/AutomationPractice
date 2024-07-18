
student = {'name': 'Sean', 'age': 25, 'courses': ['math', 'english']}

print(student['name'])
print(student['age'])
print(student['courses'])

student2 = {1: 'Sean', 2: 25, 3: ['math', 'english']}

print(student2[1])
print(student2[2])
print(student2[3])

print(student.get('name'))

# print(student['email']) returns an error
# print(student.get('email')) returns 'none'
# print(student.get('phone', 'Not Found')) returns 'Not Found'

student['email'] = 'seanstephens@email'
student['name'] = 'Jane'  # updates name

student2.update({'name': 'Jane', 'age': 26, 'email': 'seanstephens@email'})

del student['age']  # deletes the age key
age = student.pop('age')  # removes the age and value from the dictionary but stores it in variable

print(len(student))  # amount of keys
print(student.keys())  # names of the keys
print(student.values())  # the values
print(student.items())  # prints the pairs, key and value

for key, value in student.items():
    print(key, value)
