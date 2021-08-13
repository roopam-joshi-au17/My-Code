'''
Q-3 )Pow(x, n) - Solve using DP (5 marks)
https://leetcode.com/problems/powx-n/
(Medium)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base = x, exponent = abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f

if __name__ == "__main__":
   
    print()