'''Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
and all even multiples from 2 to 20 if the number is even. using for loop
'''
n=int(input("Enter a Number : "))
if n%2==1: 
    for i in range(1,22,2):
        print(i*n)
else:
    for i in range(2,21,2):
        print(i*n)
'''Given a number as input from the user, print all its odd multiples from 1 to 21 if the number is odd
and all even multiples from 2 to 20 if the number is even. using while loop
'''
n=int(input("Enter a Number : "))
if n%2==1:
    i=1
    while(i<=21):
        print(i*n)
        i=i+2
else:
    i=2
    while(i<=20):
        print(i*n)
        i=i+2

