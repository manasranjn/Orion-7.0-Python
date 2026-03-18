# try:
#     print(10/2)
# except:
#     print("Division by 0 is not possible")
# finally:
#     print("Finally Block")

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError:
#     print("Division by 0 is nohit possible")

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Division by 0 is not possible")
# except Exception:
#     print("Invalid Input")



# File handling
file = open("example.txt", 'r')
content = file.read()
content = file.readline(10)
content = file.readlines()
content = file.readlines(100)
print(content)
file.close()

with open("example.txt", 'r') as file:
    content = file.read()
    print(content)

with open('example.txt', 'w') as f:
    # print(f.readable())
    # print(f.writable())
    # f.write("Hello World")
    # f.write("Hello World\n Good Morning")
    f.writelines(["Hello World\n", "Good Morning"])

with open('example2.txt', 'w') as f:
    f.writelines(["Hello World\n", "Good Morning"])

with open('example.txt', 'a') as f:
    print(f.readable())
    print(f.writable())
    f.write("\nAppend text")
    f.write("\nHello World\n Good Morning")

with open('example.txt', 'a+') as f:
    print(f.readable())
    print(f.writable())
    f.write("\nAppend text")
    f.write("\nHello World\n Good Morning")
    f.seek(0)
    content = f.read()
    print(content)

with open('example.txt', 'r+') as f:
    print(f.readable())
    print(f.writable())
    f.write("\nAppend text")
    f.write("\nHello World\n Good Morning")
    f.seek(0)
    content = f.read()
    print(content)

with open('example.txt', 'w+') as f:
    print(f.readable())
    print(f.writable())
    f.write("\nAppend text")
    f.write("\nHello World\n Good Morning")
    f.seek(0)
    content = f.read()
    print(content)