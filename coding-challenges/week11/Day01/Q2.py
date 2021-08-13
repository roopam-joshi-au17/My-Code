'''
Q-2 )Trapping Rain Water (7.5 marks)
https://leetcode.com/problems/trapping-rain-water/
(Hard)
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.
'''
def TrappingWater(height):
        if len(height)<= 2:
            return 0
        ans = 0
        i = 1
        j = len(height) - 1
        lmax = height[0]
        rmax = height[-1]
        while i <=j:
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]            
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            else:
                ans += rmax - height[j]
                j -= 1               
        return ans

   
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = TrappingWater(height)
print(ans)

# 2nd mathod

# def TrappingWater(height):

#     if len(height) == 0:
#         return 0

#     else:
#         res = 0
#         for i in range(0, len(height)):
#             lMax = 0
#             rMax = 0

#             for j in range(0, i):
#                 lMax = max(lMax, height[j])
 
#             for j in range(i + 1, len(height)):
#                 rMax = max(rMax, height[j])
            
#             water = min(lMax, rMax) - height[i]
#             if (water > 0): 
#                 res += water
        
#         return res