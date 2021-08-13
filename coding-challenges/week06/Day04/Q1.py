'''
Question 1 :
--------------
https://leetcode.com/problems/rotate-array/
Attempt this question , this is related to array
'''
num = [1,2,3,4]
k=2
for i in range (k):
    num.insert(0,num.pop(-1))
print(num)

