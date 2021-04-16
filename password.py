import random

num = input("Enter length of password: ")

password = ""

for x in range(0, num):
    newnum = str(random.randrange(1, 10))
    password = password + newnum

print("your password is: ", password)