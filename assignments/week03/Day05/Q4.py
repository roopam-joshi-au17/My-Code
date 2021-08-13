# 4.
'''
 Write code for the following sequence by taking line number as user input, [using a single loop only]
n = 5 
1
21
321
21
1 
'''
# Using for-loops

# n = int(input("Enter the number of lines (only odd numbers) ?:  "))
# halfway_point = ( n//2 + n%2 )
# for ln in range(1,halfway_point+1):
#     for digit in range(ln,0,-1):
#         print(digit, end="")
#     print()
# for ln in range(halfway_point - 1, 0, -1):
#     for digit in range(ln,0,-1):
#         print(digit, end="")
#     print()
# print()

# Using While-Loops

# n = int(input("Enter the number of lines (only odd numbers) ?:  "))
# halfway_point = ( n//2 + n%2 )
# ln=1
# while ln<=halfway_point:
#     digit=ln
#     while digit>=1:
#         print(digit, end="")
#         digit=digit-1
#     print()
#     ln=ln+1

# ln=halfway_point-1
# while ln>=1:
#     digit=ln
#     while digit>=1:
#         print(digit, end="")
#         digit=digit-1
#     print()
#     ln = ln - 1


#single loop

n = int(input("Enter the number of lines (only odd numbers) ?:  "))
halfway_point = ( n//2 + n%2 )
string=""
for i in range(1,n+1):
    if i<=halfway_point:
        string = str(i) + string
        print(string)
    else:
        print(string[i-halfway_point:])
