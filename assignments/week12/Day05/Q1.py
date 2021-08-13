'''
Q-1 ) Top K Frequent Elements (5 marks)
https://leetcode.com/problems/top-k-frequent-elements/
(5 marks)
(Medium)
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
	   # return if it has only one element
	   if len(nums) == 1:
            return nums
        
		# count frequencies
        counter = {}
        for n in nums:
            if counter.get(n):
                counter[n] += 1
            else:
                counter[n] = 1

		# fins k top frequent with heap
        h = []
        for i, c in counter.items():
            if len(h) < k:
                heappush(h, (c, i))
            else:
                heappushpop(h, (c, i))
        
		# form result list from touples in the heap
        res = []
        for c, i in h:
            res.append(i)

        return res