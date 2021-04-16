
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")


num3 = input("To add enter 1, to subtract enter 2, To multiply enter 3, To divide enter 4, : ")

if (num3 == 1):
    sum = num1+num2
    print("sum: ", sum)
elif (num3 == 2):
    difference = num1-num2
    print("difference: ", difference)
elif (num3 == 3):
    product = num1*num2
    print("product: ", product)
elif (num3 == 4):
    quotient = num1 / num2
    print("quotient: ", quotient)