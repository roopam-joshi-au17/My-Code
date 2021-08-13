'''
Print the following pattern after taking in the line number as input from the user: 
for example: if input line number is 5, then print the following pattern.
*
***
*****
***
* 
'''
n=int(input("Enter number of Lines : "))
h=n//2+n%2
j=h-1
for i in range(1,n+1,2):
    print(" "*j,"*"*i)
    j=j-1

j=1
for i in range(n-2, 0, -2):
    print(" "*j,"*"*i)
    j = j + 1
