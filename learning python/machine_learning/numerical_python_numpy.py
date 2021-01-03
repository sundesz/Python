import os
import sys

print("Welcome")


# with open("script.py", "a") as f:
#     f.write("From python file")

# f = open("script.py", "r")
# print(f.readline())
# print(f.read())
# for i in f:
#     print(i)
# f.close()


with open("test.txt", "w") as f:
    f.write("Hello world")

with open("test.txt", "r") as f:
    print(f.read())

os.remove("test.txt")

print(sys.path)