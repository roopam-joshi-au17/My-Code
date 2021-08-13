'''
Q - 1) Write a program to print sum of right diagonal of a matrix: 
'''
def printDiagonalSums(mat, n): 
    diagonal = 0
    for i in range(0, n):
        for j in range(0, n):
            if ((i + j) == (n - 1)):
                diagonal += mat[i][j]
    print("Sum of Right Diagonal:", diagonal)

a = [[ 1,2,3],
     [ 4,5,6],
     [ 7,8,9],
    ]

printDiagonalSums(a, 4)