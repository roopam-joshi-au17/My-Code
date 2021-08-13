'''Take a number as input from the user, print its multiple of 2, 4, 6,
8, 10 if it is an odd number, if it is an even number then print its
multiple of 1, 3, 5, 7 and 9.
'''
n = int(input("Enter a number: "))
if n%2!=0:
    print(n*2)
    print(n*4)
    print(n*6)
    print(n*8)
    print(n*10)
else:
    print(n*1)
    print(n*3)
    print(n*5)
    print(n*7)
    print(n*9)
