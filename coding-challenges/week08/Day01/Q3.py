'''
Q-3 ) Reverse a string using recursion:(5 marks)
If we have a string, write a function that prints reverse of that string, using
recursion.
Sample Input:
ABCD
Sample Output:
DCBA
'''
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))