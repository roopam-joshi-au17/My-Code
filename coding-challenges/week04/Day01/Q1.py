'''
Define a function factorial() with one input n. [The default value of n needs to
be 5]. Use the factorial() function and other inbuilt functions to find the
maximum between the following:
1. 5!+3!-21 and 2!+4!+12
2. 26!+31! and 22!+35!
3. 21!+34!-15! and 31!+27!-19!
Hint: you can use the min() and max() inbuilt functions of python.
'''

def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact = fact * i
  return fact
print(" 5!+3!-21 and 2!+4!+12  max is :",end="")
print(max((factorial(5)+ factorial(3)-21) , (factorial(2)+ factorial(4)+12)))
print(max)
print("26!+31! and 22!+35! max is :",end="")
print(max((factorial(26)+ factorial(31)) , (factorial(22)+ factorial(35))))
print(max)
print("21!+34!-15! and 31!+27!-19! max is :",end="")
print(max((factorial(21)+ factorial(34) -factorial(15)) , (factorial(31)+ factorial(27)-factorial(19))))
print(max)