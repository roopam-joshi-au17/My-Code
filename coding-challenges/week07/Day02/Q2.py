'''
Given an sorted integer array . Write a program to find Lower Bound of
target number, return the index of the element
Input: arr = [1,2 ,3,3,3,4,4,5,5,7,7,7] , target = 6
Output: 8
Explanation : -
def Lower_Bound(arr , target):
'''
def Lower_Bound(arr, n, target):
 
    # Corner cases
    if (target <= arr[0]):
        return arr[0]
    if (target >= arr[n - 1]):
        return arr[n - 1]
 
    # Doing binary search
    i = 0; j = n; mid = 0
    while (i < j):
        mid = (i + j) // 2
 
        if (arr[mid] == target):
            return arr[mid]
 
        # If target is less than array
        # element, then search in left
        if (target < arr[mid]) :
 
            # If target is greater than previous
            # to mid, return closest of two
            if (mid > 0 and target > arr[mid - 1]):
                return getClosest(arr[mid - 1], arr[mid], target)
 
            # Repeat for left half
            j = mid
         
        # If target is greater than mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return getClosest(arr[mid], arr[mid + 1], target)
                 
            # update i
            i = mid + 1
         
    # Only single element left after search
    return arr[mid]
 
def getClosest(val1, val2, target):
 
    if (target - val1 >= val2 - target):
        return val2
    else:
        return val1

arr = [1,2 ,3,3,3,4,4,5,5,7,7,7]
n = len(arr)
target = 6
print(Lower_Bound(arr, n, target))


# Time Complexity: O(log n). 
# Space Complexity: O(1).