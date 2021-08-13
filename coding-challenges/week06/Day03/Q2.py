'''
Given a number , find if the number is a perfect square root or not ?
Also , find Time and space Complexity
example :
Input : n = 4
output : - True
Input : n = 10
output : - False
Explanation : since square root (4) =2 (perfect square ) --true
Square root(10) = 3.35 (Not perfect square) -- false
Sample :
Def find_perfect_square(N):
'''
from math import sqrt
def find_perfect_square(n):
   sq_root = int(sqrt(n))
   return (sq_root*sq_root) == n

n1=int(input("Enter a number : "))
print (find_perfect_square(n1))

#Time complexity:O(1)
#Space complexity:O(1)