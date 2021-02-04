# Pandas Data Frames
import pandas as pd

my_dict = {"animals": ['cat', 'dog', 'horse', 'pig'],
            "name": ['ram', 'sam', 'hari', 'gopal'],
            "age": [8, 10, 11, 4]
        }

df = pd.DataFrame(my_dict, index=['id1', 'id2', 'id3', 'id4'])
#
print(df.shape)
print(df.values)

#print(df.loc['id1', ['animals', 'name', 'age']])

#  access column by name with .loc
#print(df.loc[:, 'animals'])

# access column by name without .loc
#print(df['animals'])

# access column by index with .iloc
#print(df.iloc[:, 0])

# access row by name with .loc
#print(df.iloc[0])

# access row by index with .iloc
#print(df.loc['id1'])

"""
def pow_of_two(x):
    out = []

    for i in range(1, int(x) + 1):
        out.append(2 ** i)

    return out


y = pow_of_two(3)
print(y)



def multiply(x, y):
    '''
    this function takes input x and y
    and returns the multiplication of x and y
    '''

    # perform computation
    result = x * y

    return result


# apply the function
y = multiply(2, 3)

print(y)

print(type(y))


# create a sequence of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# initialize variables
odd_count = 0
even_count = 0

### STUDENT TASK ###
for i in numbers:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("Number of even numbers :", even_count)
print("Number of odd numbers :", odd_count)


english_number = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
]
finnish_number = [
    "nolla",
    "yksi",
    "kaksi",
    "kolme",
    "nelja",
    "viisi",
    "seitsemän",
    "kahdeksan",
]

for index, (eng, fin) in enumerate(zip(english_number, finnish_number)):
    print(index, eng, fin)


some_sequence = ["one", "two", "three", "four"]
another_sequence = ["yksi", "kaksi", "kolme", "nelja"]

for eng, fin in zip(some_sequence, another_sequence):
    print(eng, fin)


some_sequence = ["hi", "how", "are", "you"]
for key, value in enumerate(some_sequence):
    print("index: {} value: {}".format(key, value))


my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in my_list:
    print("\nouter list index:{}".format(i))
    for j in i:
        print("inner list index:{}".format(j))

"""
