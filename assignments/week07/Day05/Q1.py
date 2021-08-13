'''
Question 1 :
--------------
Given a number N , count number of SET bits (having 1) in binary format of number N.
INPUT - 26
OUTPUT : 3
Explanation :
N = 26 , binary value = 11010 , count of set bits (having value 1) = 3.
HINT : - Make use of bit manipulation concept .
https://leetcode.com/problems/number-of-1-bits/ 
'''
def countSetBits(n):
 
    count = 0
    while (n):
        n &= (n-1)
        count+= 1
     
    return count
i = 26
print(countSetBits(i))

#Time Complexity: O(logn)
#Space Complexity:O(1)