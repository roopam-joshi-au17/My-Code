'''
Write a program to PRINT numbers from 1 to N , with conditions :
a) If number is divisible by 7 , print("HI")
b) If number is divisible by 11 , print("BYE")
c) If number divisible by both 7 and 11 , print ("HiBYE")
Also, find the Time complexity for the algorithm.
Example : -
N = 12
Output :
Hi
BYE
'''

n=int(input("Enter a number :"))
for i in range(1,n):
    if (i%7==0):
        print("HI")
    elif(i%11==0):
        print("BYE")
    elif(i%7==0) and (i%11==0):
        print("HIBYE")

#Time complexity: 0(n)