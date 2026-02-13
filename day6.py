s1 = "       This is a a a a string      "
s2 = "This is Another string"
# print(s2.find('is'))
# print(s2.rfind('is'))
# print(s1.find('a'))
# print(s1.rfind('a'))
# print(s1.count('a'))
# print(s1.find('and'))
# print(s1.index('and'))
# print(s2.isalpha())
# print("2".isdigit())
# print("s2".isalnum())
# print(s2.isdecimal())
# print(s2.startswith('T'))
# print(s2.endswith('ig'))

# Dictionay and It's Inbuilt methods
student = {
    'name': "Smith",
    'age': 20,
    'marks': 80,
    'section': 'B',
    'gender': 'M',
    'is_active': True,
}

student2 = dict(name="Smith", age=20, marks=80, section='B', gender='M', is_active=True)
# print(student2)
# print(student['name'])
student['subject'] = 'Python'  # Add a new key value pair
# print(student)
student['age'] = 22 # Update the value of a key
# print(student)
# del student['is_active'] # Delete a key value pair
# print(student)

# for key in student:
#     print(key)
#     print(student[key])

# for key, value in student.items():
#     print(key, value)

# print(student.items())

# student3 = student
# print(student3)
# student3['name'] = "John"
# print(student3)
# print(student)

s1 = student.copy()
# print(s1)
s1['name'] = 'Allen'
# print(s1)
# print(student)

# print(student.keys())
# print(student.values())
# print(student.popitem())
# print(student)
# print(student.pop('is_active'))
# print(student)
# student.update({'is_active': False})
# print(student)
# student.clear()
# print(student)
# print(student.get('name'))
print(student.get('name', 'Not found'))