'''
Q-2 )Sum of Unique Elements:
https://leetcode.com/problems/sum-of-unique-elements/
(5 marks)
You are given an integer array nums. The unique elements of an array are the elements that appear
exactly once in the array.
Return the sum of all the unique elements of nums.
Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

'''
def sumofUnique(nums):
    unique = []
    for num in nums:
        if nums.count(num) == 1:
            unique.append(num)
    return sum(unique)
arr = [1,2,3,2]
print(sumofUnique(arr))