"""
Q-3 ) Sort an array in wave form :(5 marks)
Given an unsorted array of integers, sort the array into a wave like array. An
array ‘arr[0..n-1]’ is sorted in wave form if arr[0] >= arr[1] <= arr[2] >= arr[3] <=
arr[4] >= …..
Examples:
Input: arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
{20, 5, 10, 2, 80, 6, 100, 3} OR
any other array that is in wave form
"""
def wave(A):
    for i in range(len(A)-1):
        if i%2 == 1 and (A[i] > A[i+1]):
            A[i], A[i+1] = A[i+1], A[i]
        elif i%2 == 0 and A[i] < A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    return A
arr = [10, 5, 6, 3, 2, 20, 100, 80]
print(wave(arr))