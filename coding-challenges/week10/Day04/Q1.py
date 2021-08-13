'''
Q-1 ) Valid Parentheses:
https://leetcode.com/problems/valid-parentheses/
(5 marks)
(Easy)
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Example 1:
Input: s = "()"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', '[':']', '{':'}'}
        stack = []
        for char in s:
            if char in pair.keys():
                stack.append(char)
            elif len(stack) > 0 and pair.get(stack[-1]) == char:
                stack.pop()
            else: 
                return False
        return len(stack) == 0