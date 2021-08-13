'''
Write a program to print sum of border elements of a square Matrix
'''
def printBoundary(a, m, n):
    sum = 0
    for i in range(m):
        for j in range(n):
            if (i == 0):
                sum += a[i][j]
            elif (i == m-1):
                sum += a[i][j]
            elif (j == 0):
                sum += a[i][j]
            elif (j == n-1):
                sum += a[i][j]
    return sum

a = [ [ 1, 2, 3, 4 ],
      [ 4, 5, 6, 5 ],
      [ 7, 8, 9, 6 ], 
      [ 4, 9, 8, 7 ] 
    ]
sum = printBoundary(a, 4, 4)
print ("Sum of boundary elements is", sum)