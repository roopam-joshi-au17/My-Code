'''
Q-3 ) Longest Common Subsequence - Solve using DP
(5 marks)
https://leetcode.com/problems/longest-common-subsequence/
(Medium)
Given two strings text1 and text2, return the length of their longest common
subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with
some characters (can be none) deleted without changing the relative order of the
remaining characters.
● For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both
strings.
Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is
3.
'''
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We want to represent the previous longest sequence for any
        # character within the sequence of chars of text2
        # Each position in the dp array then represents the length of the longest 
        # previous longest subsequence length
        
    dp = [0] * len(text2)
        
    for i, c in enumerate(text1):
        if c in text2:
            prev_max=0
            dp_clone = dp.copy()    # To avoid adding into the same character in the same iteration
            for k, text2_c in enumerate(text2):                
                if text2_c == c:
                    dp_clone[k] = prev_max + 1            
                prev_max = max(prev_max,dp[k])    
            dp = dp_clone
    return max(dp)