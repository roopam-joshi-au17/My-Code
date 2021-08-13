'''
1) Write a Program to find the largest element in an arrray
Example:
Input : arr[] = {10, 20, 4}
Output : 20
Input : arr[] = {20, 10, 20, 4, 100}
Output : 100
'''
def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [20, 10, 20, 4, 100]
n = len(arr)
Ans = largest(arr,n)
print (Ans)