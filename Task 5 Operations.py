num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Which operation would you like to perform? ")
operation = input("Choose from the following menu: A for addition, S for subtraction, D for division, M for multiplication : ")

if operation == 'A':
    A = num1 + num2
    print(num1, "+", num2, "=", A)
elif operation == 'S':
    S = num1 - num2
    print(num1, "-", num2, "=", S)
elif operation == 'D':
    D = num1 / num2
    print(num1, "/", num2, "=", D)
elif operation == 'M':
    M = num1 * num2
    print(num1, "*", num2, "=", M)
else:
    print("Input operation is not recognised!")