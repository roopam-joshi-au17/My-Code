'''
a. Define a function arithmetic_operation() which takes 2 numbers and operation name as input and performs an ope
ration on them:
* opname: "Add" - Then we add 2 numbers
* opname: "Sub" - Then we subtract 2 numbers
* opname: "Multiply" - Then we multiply 2 numbers
* opname: "Divide" - Then we divide the 2 numbers
Print the result of the operation and also return it
'''
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def arithmetic_operation():
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    opname = int(input("Enter your choice:"))
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if opname == 1:
        print(n1, "+", n2, "=", add(n1, n2))
    elif opname == 2:
        print(n1, "-", n2, "=", subtract(n1, n2))
    elif opname == 3:
        print(n1, "*", n2, "=", multiply(n1, n2))
    elif opname == 4:
        print(n1, "/", n2, "=", divide(n1, n2))
    else:
        print("Invalid Operation")
arithmetic_operation()
