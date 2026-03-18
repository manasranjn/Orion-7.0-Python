# Error
#Syntax Error
# for i range(10):
#     print(i)

# Runtime Error
def division(a,b):
    print(a/b)

# division(10,2)
# division(10,0)

#Logical Error
# def addition(a,b):
#     print( a - b)

# addition(10,40)

# Indentation Error
    # if True:
    # print("True")

# Exception Handling
# try:
#     statement
# except:
#     statement
# finally:
#     statement

try: 
    division(10,0)
except:
    print("Division by 0 is not possible")
finally:
    print("Finally Block")