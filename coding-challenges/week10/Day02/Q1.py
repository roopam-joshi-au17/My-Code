'''
Q-1 )Find the Duplicate Number:
https://leetcode.com/problems/find-the-duplicate-number/
(Solve the above using both the approaches discussed in class) and comment on
time
complexity.
:(5 marks)
Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only
constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
'''
def findDuplicate(arr):
    hashTable = dict()
    n = len(arr)
    dup = 0
    for i in arr:
        if i not in hashTable:
            hashTable[i] = 1
        else:
            hashTable[i] += 1

    for key, value in hashTable.items():
        if value >= 2:
            dup = key
            break
    return dup
arr1 = [1,3,4,2,2]
print(findDuplicate(arr1))

# def hashing1(nums):
#     hashing = {}    
#     for i in nums: 
#         if i in hashing:           
#             return i   
#         else:
#             hashing[i]=1
# arr = [1,3,4,2,2]
# print(hashing1(arr))