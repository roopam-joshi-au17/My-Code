'''
Q-3 ) Given a number n, find sum of first n natural numbers:(5 marks)
Examples :
Input : 5
Output : 15
Explanation : 1 + 2 + 3 + 4 + 5 = 15
Input : 7
Output : 28
Explanation : 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
'''
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

num = 5

if num < 0:
   print("Enter a positive number")
else:
   print(recur_sum(num))