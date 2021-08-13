'''
Given an sorted integer array . Write a program to find Lower Bound of
target number, return the index of the element
Input: arr = [1,2 ,3,3,3,4,4,5,5,7,7,7] , target = 6
Output: 8
Explanation : -
def Lower_Bound(arr , target):
#write code here

'''
def Lower_Bound(arr, n, target):
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2
        if (arr[mid] == target):
            return arr[mid]
        if (target < arr[mid]) :
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)
            j = mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)
            i = mid + 1
    return arr[mid]
 
def getClosest(val1, val2, target):
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1
arr = [1,2,3,3,3,4,4,5,5,7,7,7]
n = len(arr)
target = 6
print(Lower_Bound(arr, n, target))


# Time Complexity: O(log n). 
# Space Complexity: O(1).