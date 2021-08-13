'''
Q-1 ) Is Subsequence
https://leetcode.com/problems/is-subsequence/
(7.5 marks)
(Easy)
Given two strings s and t, return true if s is a subsequence of t, or false
otherwise.
A subsequence of a string is a new string that is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative
positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde"
while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
def isSubsequence(s, t):
    sub_index = 0    
    if s == "":
        return True
    for i in t:
        if sub_index == len(s):
            return True
		#only add to our counter if the subsequent character matches. 
		# e.g. in "abc" in "azbdecg", we find "a", we go to "b". We can only move forward if the following substring from z-g has the character "b".
		#When we find b, we try to find c. "C" can only exist in d-g substring if it is truely sequential
        if i == s[sub_index]:
            sub_index += 1    
    return sub_index == len(s)