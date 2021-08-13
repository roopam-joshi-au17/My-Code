'''
Q-1 ) Write a program to convert a string of binary number into a decimal
number: (5 marks)
(Easy)
eg:
Sample Input
st = “101”
Sample output
5
Revise the lecture to see the algorithm to convert binary to decimal
'''


def binaryToDecimal(n):
    dec_value = 0
    base1 = 1
    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):
            dec_value += base1
        base1 = base1 * 2

    return dec_value
num = "101"
print(binaryToDecimal(num))