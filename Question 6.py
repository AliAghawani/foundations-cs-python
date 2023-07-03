num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 < num1:
    print("Error: Second number cannot be smaller than the first number.")
else:
    print("Even numbers between", num1, "and", num2, "are:")
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            print(num)





