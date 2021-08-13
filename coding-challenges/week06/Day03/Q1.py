'''
Write a Program to swap values , without using 3rd variable .
Also find Time and Space Complexity --- 
Example : -
Input : -
A = 20 , B = 10
Output : - A = 10 , B = 20
Explanation : - values has been swapped
Sample :
Def swap(A,B):
'''
def swap(a,b):
    a,b=b,a
    print("A = ",a,"B = ",b)

n1=int(input("Enter First Number"))
n2=int(input("Enter Second Number"))
swap(n1,n2)

#Time complexity:O(1)
#Space complexity:O(1)