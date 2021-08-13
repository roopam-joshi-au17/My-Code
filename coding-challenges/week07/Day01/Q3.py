'''
Given an integer array , every element is repeated TWICE , except one
element , Find that element ?
Input : - [1 , 2 , 1, 2 ,4 , 3 ,4 ,3]
Output: - 3
Explanation : HINT : - Use XOR operator ;
'''
#Time Complexity=O(n)
#Space Complexity=O(1)

def findSingle( ar, n):
    res = ar[0]
    for i in range(1,n):
        res = res ^ ar[i]
    return res
ar = [1 , 2 , 1, 2 ,4 , 3 ,4]
print ("Element occurring once is", findSingle(ar, len(ar)))