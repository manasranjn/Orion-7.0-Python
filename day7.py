# WAP to check if a number is even or odd

# num = int(input("Enter a number: "))
# if num %2 ==0:
#     # print(f"{num} is even ")
#     print(num ,"is even ")
# else:
#     print(f"{num} is odd")

# WAP to check if two strings are anagrams

# s1 = 'listen'
# s2 = 'silent'

# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")


# Take a list of strings  and short them  based on string length
# l1 = ['Hi', 'Hello', 'Good', 'Morning', 'bye']

# l1.sort(key=len)
# print(l1)


l1 = ['Hi', 'Hello', 'Good', 'bye', 'Morning', 'bye']

# l1.append(10)
# l1.insert(3, 10)
# l1.extend([10, 20, 30])
# l1.remove('bye')
# elem = l1.pop(2)
# print(elem)
# l1.clear()
# print(l1)
# print(l1.index('bye'))
# print(l1.count('Hii'))

l2 = [30,20,40,60,10,50]
l2.sort()
# l2.sort(reverse=True)
l2.reverse()

l3 = l2.copy()
print(l3)