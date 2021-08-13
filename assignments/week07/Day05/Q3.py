'''
Q3.
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
def findFirstAndLast(arr, n, x) :
    first = -1
    last = -1
    for i in range(0, n) :
        if (x != arr[i]) :
            continue
        if (first == -1) :
            first = i
        last = i
     
    if (first != -1) :
        print( "First Occurrence = ", first," \nLast Occurrence = ", last)
    else :
        print("Not Found")

arr = [5,7,7,8,8,10]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)
#Time Complexity: O(n)
#Space Complexity: O(1)