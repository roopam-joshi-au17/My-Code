'''
Question : 2 -
https://leetcode.com/problems/sqrtx/
'''
def floorSqrt(x):
    if (x == 0 or x == 1):
        return x
    i = 1
    result = 1
    while (result <= x):
        i += 1
        result = i * i  
    return i - 1
x = 8
print(floorSqrt(x))

#Time Complexity: O(√n)
#Space Complexity: O(1)