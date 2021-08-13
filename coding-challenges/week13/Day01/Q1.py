'''Q-1 ) Fibonacci Number - solve without DP
https://leetcode.com/problems/fibonacci-number/
(5 marks)
(Easy)
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
Fibonacci sequence, such that each number is the sum of the two preceding
ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1
'''
def fib(N):

    res = [0, 1]
    if N == 0:
        return res[0]

    elif N==1:
        return res[1]

    for i in range(2, N+1):
        res.append(res[-1] + res[-2])  

    return res[-1]


if __name__=="__main__":

    n = 2
    ans = fib(n)
    print(ans)