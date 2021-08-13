'''Given a number as input from the user, print a triangle like the following.
using for loop
'''
n = int(input("Enter the number of rows")) 
for i in range(1,n+1): 
    print("*"*i)
for i in range(n-1,0,-1): 
    print("*"*i)

'''Given a number as input from the user, print a triangle like the following.
using while loop
'''
n = int(input("Enter the number of rows"))
i=1
while(i<=n):
    print("*"*i)
    i=i+1
i=n-1
while(i>=1):
    print("*"*i)
    i=i-1
