'''
Q-2 )Solve above question with DP
'''
def step(a,n,dp):
    if a==n:
        return 1
    if a>n:
        return 0
    if dp[a] != -1:
        return dp[a]
    one_step=step(a+1,n,dp)
    two_step=step(a+2,n,dp)
    dp[a]=one_step+two_step
    return dp[a]
    
def climbStairs(n):
    a=0
    dp=[-1]*1000
    return step(a,n,dp)

n=int(input())
print(climbStairs(n))