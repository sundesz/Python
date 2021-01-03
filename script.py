def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Sandesh"))


for i in range(11):
    print(i)

fruits = ["banana", "apple", "cherry", "strawberry"]
for key, fruit in enumerate(fruits):
    print(key, fruit)


# a = input("Enter your name: ")
# print(f"Welcome {a}")


for i in range(11):
    print(i)

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)

nums_list3 = list(range(1, 12, 2))
print(nums_list3)

names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]

# Rewrite the for loop to use enumerate
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)

# """ import pynum as py

# num = [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]

# # Print second row of nums
# print(nums[1,:])

# # Print all elements of nums that are greater than six
# print(nums[nums > 6])

# # Double every element of nums
# nums_dbl = nums * 2
# print(nums_dbl)

# # Replace the third column of nums
# nums[:,2] = nums[:,2] + 1
# print(nums) """

print(list(range(1, 11)))

# a = int(input().strip())
# b = int(input())
# print(a % b == 0)

# a = int(input())
# print((10 > a) or (a > 250))

number = 0
while number < 12:
    print(number)
    number += 2

i = 0
while i < 5:
    print("*")
    if i % 2 == 0:
        print("**")
    if i > 2:
        print("***")
    i = i + 1

i = 1
while i <= 20:
    print(i ** 2)
    i += 1


# pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# omelette = "egg, milk, bacon, tomato, salt, pepper"

# ingridient = input()

# if ingridient in pasta:
#     print("pasta time!")
# if ingridient in apple_pie:
#     print("apple_pie time!")
# if ingridient in ratatouille:
#     print("ratatouille time!")
# if ingridient in chocolate_cake:
#     print("chocolate_cake time!")
# if ingridient in omelette:
#     print("omelette time!")


# # the following line reads the input and converts it into a list; do not modify it, please
# hidden = list(input())

# # your code here
# print(len(hidden))


# # the following line reads the list from the input, do not modify it, please
# prices = input().split()

# # please work with the list 'prices' here
# print(prices[2])

print((43 + 5) - (43 % 5))
print(43 % 5)


# # Save the input in this variable
# ticket = input()

# # Add up the digits for each half
# half1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
# half2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")


# def test():
#     print("Let's test your programming knowledge.")
#     print("Why do we use methods?")
#     print("1. To repeat a statement multiple times.")
#     print("2. To decompose a program into several small subroutines.")
#     print("3. To determine the execution time of a program.")
#     print("4. To interrupt the execution of a program.")

#     guess = int(input().strip())

#     while guess != 2:
#         print("Please, try again.")
#         guess = int(input().strip())

#     print("Completed, have a nice day!")


# test()

var = 101

if var >= 300:
    print("out of limit")
elif (var >= 100) and (var < 200):
    print("the second interval")
else:
    if var < 100:
        print("the first interval")
    else:
        print("the third interval")


# x = float(input())
# y = float(input())

# if x > 0 and y > 0:
#     print("I")
# elif x < 0 and y > 0:
#     print("II")
# elif x < 0 and y < 0:
#     print("III")
# elif x > 0 and y < 0:
#     print("IV")
# elif x == 0 or y == 0:
#     if x == y == 0:
#         print("It's the origin!")
#     else:
#         print("One of the coordinates is equal to zero!")


# spin = input()
# electric_charge = input()

# if spin == '1/2' and electric_charge == '-1/3':
#     print('Strange	Quark')
# elif spin == '1/2' and electric_charge == '2/3':
#     print('Charm Quark')
# elif spin == '1/2' and electric_charge == '-1':
#     print('Electron	Lepton')
# elif spin == '1/2' and electric_charge == '0':
#     print('Neutrino	Lepton')
# elif spin == '1' and electric_charge == '0':
#     print('Photon Boson')


# t = int(input())
# reference_time = 10.30
# a = t + reference_time

# if a >= 24:
#     print("Wednesday")
# elif a < 0:
#     print("Monday")
# else:
#     print("Tuesday")


singleton = ([0, 1, 1, 2, 3, 5, 8, 13, 21],)
print((singleton))

numbers = tuple(int(n) for n in input().split())
print(numbers[-1])From python file