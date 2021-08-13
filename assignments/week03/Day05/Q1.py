'''
1. Write code for the following sequence by taking line number as user input:
n = 5
**
 **
  **
**
**
n=3
**
 **
** 
'''
#for loop
# n=int(input("Enter the line of star you want to print :"))
# b=(n//2) +1
# for i in range(1,b+1):
#     print(" "*i,"*"*2)
# for i in range(b-1,0,-1):
#     print(" "*i,"*"*2)


#while loop
n=int(input("Enter the line of star you want to print :"))
b=(n//2) +1
i=1
while(i<=b):
    print(" "*i,"*"*2)
    i=i+1
i=b-1
while(i>=1):
    print(" "*i,"*"*2)
    i=i-1
