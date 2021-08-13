'''
Print prime numbers between 1 to N :
using for loop :
Also , find the Time and Space complexity
Example : -
Input : - N = 10
output : - [2 , 3 , 5 , 7 ]
Explanation : - 2 , 3 , 5 , 7 are primes number between 1 to 10
Sample :-
Def Prime_number(N):
'''

def Prime_number(n):
    for i in range(1, n+1):
        if i>1:
            for j in range(2,i):
                if(i % j==0):
                    break
            else:
                print(i,end=" ")
n1 = int(input(" Please Enter any Number: "))
Prime_number(n1)

#Time complexity:O(n^2)
#Space complexity:O(n)
