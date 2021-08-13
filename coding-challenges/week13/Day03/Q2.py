'''
Q-2 ) Tiling a Rectangle with the Fewest Squares - Solve with DP
(5 marks)
(Easy-since we solved it in recursion topic)
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
Given a rectangle of size n x m, find the minimum number of integer-sided
squares that tile the rectangle
'''
import math
import sys
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        area = n*m
        arr = [i*i for i in range(1,min(n,m)+1)]
        dp = [[-1 for i in range(area+1)] for j in range(len(arr)+1)]
        print(area,arr)
        for i in range(len(arr)+1):
            for j in range(area+1):
                if j == 0:
                    dp[i][j] = 0
                if i == 0:
                    dp[i][j] = sys.maxsize - 1
        for i in range(1,len(arr)+1):
            for j in range(1,area+1):
                if arr[i-1] <= j:
                    dp[i][j] = min(dp[i-1][j] , dp[i][j - arr[i-1]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        if dp[-1][-1] == sys.maxsize - 1:
            return -1
        else:
            return dp[-1][-1]