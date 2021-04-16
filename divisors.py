num = input("Enter number: ")


for x in range(1, num):
    if (num % x) == 0:
        print(x)