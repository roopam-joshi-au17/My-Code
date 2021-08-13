'''
Q-1 ) Climbing Stairs - solve without DP
https://leetcode.com/problems/climbing-stairs/
(5 marks)
(Easy)
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
def climbStairs(n):
    if n <= 2: 
        return n
    a, b, c = 0, 1, 2  
    while (n > 2):
        a, b = b, c
        c = a + b
        n = n - 1    
    return c
n=int(input())
print(climbStairs(n))