# Variables in Python

age = 20
name = "John"
first_name = "John"

# print(age, name, first_name)

#Data Types
#Number Types
#int
a = 10
b = -10
# print(type(a), type(b))

#float
c = 10.5
d = -10.0
# print(type(c), type(d))

#complex
e = 2 + 3j
f = 10 + 5j
# print(type(e), type(f))

#boolean
g = True
h = False
# print(type(g), type(h))

#Sequence Types
#string
s1 = 'a'
s2 = 'Hello Everyone'
s3 = "123456789"
s4 = "!@#$%^&*"
# print(type(s1), type(s2), type(s3), type(s4))
s5 = '''
    This is a multiline string
    with multiple lines
    '''
s6 = """
    This is a multiline string
    with multiple lines"""
# print(s5)
# print(s2[6])

#list
l1 = [1, 2, 3, 4, 5]
l2 = [1,2, 1,2,1,1,1,1,'a', 'b', 'c', True, False, 1.5, 2.5, 3.5]
# print(type(l1), type(l2))
# print(l1[-3])
# print(l2)

#tuple
t1 = (1, 2, 3, 4, 5)
t2 = (1,2, 1,2,1,1,1,1,'a', 'b', 'c', True, False, 1.5, 2.5, 3.5)
print(type(t1), type(t2))
# print(t1[-3])
# print(t1)
# print(t2)

#set
s1 = {1, 2, 3, 4, 5}
s2 = {1,2, 1,2,1,1,1,1,'a', 'b', 'c', True, False, 1.5, 2.5, 3.5}
# print(type(s1), type(s2))
# print(s1)
# print(s2)

#Mapping Type
#dictionary
d1 = {
    'name': 'John',
    'age': 20,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY',
        'zip': 10001
    },
    'phone': {
        'home': '123-456-7890',
        'work': '987-654-3210'
    }
}
# print(d1['name'])
# print(d1['age'])
# print(d1['phone']['home'])

#None
n1 = None
n2 = None
print(type(n1))
print(n1)
print(n2)