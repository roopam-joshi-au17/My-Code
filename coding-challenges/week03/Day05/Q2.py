'''
b. Redefine the same function with default values for numbers as 3 and 5 and opname as "Add". Use the same functi
on to calculate 5+3-12+23 
'''
def arithmetic_operation(a=3,b=5,opname="Add"):
    if opname == "Add":
        result=a+b
    elif opname == "Sub":
        result=a-b
    elif opname == "Multiply":
        result=a*b
    elif opname == "Divide":
        result=a/b
    else:
        print("Invalid Operation")
    return result
x= arithmetic_operation(5,3,"Add")
y= arithmetic_operation(-12,23,"Add")
print(x+y)
