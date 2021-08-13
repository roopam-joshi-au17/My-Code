'''
Q-3 ) Longest Common Prefix:
https://leetcode.com/problems/longest-common-prefix/submissions/
(5 marks)
Write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl
'''
def longestCommonPrefix(strs):
    if strs == None:
        print("List is None")
        return("")       
    length = len(strs)
    if length == 0:
        print("List is empty")
        return("")    
    if length == 1:
        print("List has just 1 string")
        return(strs[0])    
    retStr = ""  
    firstStr = strs[0]
    for i in range(len(firstStr)):
        for j in range(1, length):
            if i < len(strs[j]):
                if firstStr[i] != strs[j][i]:
                    return(retStr)
            else:
                return(retStr)
        retStr = retStr + firstStr[i]       
    return(retStr)
str = ["flower","flow","flight"]
print(longestCommonPrefix(str))
'''
Time-Complexity : O(m * n), m = length of the first string, n = total no. of strings in the list
Space-Complexity : O(1), no extra space except two strings, retStr and firstStr.
'''