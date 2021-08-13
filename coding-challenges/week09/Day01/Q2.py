'''
Program for Sum of the digits of a given number:(5 marks)
Sample Input:
1234567
Sample output:
28
'''
def sumdigits(number):
  if number == 0:
    return 0
  else:
    return (number%10) + sumdigits(number//10)
n=1234567
print(sumdigits(n))