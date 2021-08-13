'''
Q4.
Write a program to compute the power of a number.
Input - x = 10 , y = 5 , calculate = (x^y)
Output : - 100000
Example -
pow(n, 5) will give you n to the power 5. Use recursion in it.
def pow(x,y):
#write code here
'''
def power(N, P):
    if P == 0:
        return 1
    elif P == 1:
        return N   
    else:
        return (N*power(N, P-1))

N = 10
P = 5
  
print(power(N, P))
#Time Complexity: O(n)
#Space Complexity: O(1)