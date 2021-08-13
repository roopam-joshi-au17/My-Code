'''
Q-3 ) Write a program perform selection sort using an auxiliary (extra) list,
and tell the time complexity and space complexity of your code.
'''
def selection_sort(A):

    n = len(A)
    for i in range(n):
        min_ele = A[i]
        min_ele_idx = i
        for idx in range(i, len(A)):
            if A[idx] < min_ele:
                min_ele = A[idx]
                min_ele_idx = idx
        A[i], A[min_ele_idx] = A[min_ele_idx], A[i]
    return A


if __name__ == "__main__":

    A = [6, 7, 1, 2, 4, 5, 6]
    print(selection_sort(A))

# Time Complexity   =  O(N^2)           |
# Space Complexity  =  O(1) 