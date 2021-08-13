'''
Q-1 ) Check if a number is Palindrome: (5 marks)
Given an integer, write a function that returns true if the given number is
palindrome, else false.
For example,
Sample input:
12321
Sample output:
palindrome
eg2:
Sample input:
1451
Sample output:
not palindrome.
'''
def reverse(n, rev=0):
    if n == 0:
        return rev 
    rev = rev * 10 + (n % 10)
    rev = reverse(n // 10, rev)
    return rev
def isPalindrome(num):
    return num == reverse(num)
 
n = 1451
if isPalindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")