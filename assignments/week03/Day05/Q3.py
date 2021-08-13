'''
Write code for the following sequence by taking line number as user input
n = 3
 1
121
 1
n = 5
  1
 121
12321
 121
  1 
'''
#for loop
# n = int(input("Enter the number of lines (only odd numbers) ?:  "))
# halfway_point = ( n//2 + n%2 )
# for ln in range(1,halfway_point+1 ):     
#         print(" "*(halfway_point-ln),end="")
#         for digit in range(1, ln + 1):
#             print(digit,end="")
#         for rev_digit in range(ln-1,0,-1):
#             print(rev_digit,end="")
#         print()
# for ln in range(halfway_point-1, 0,-1): 
#     print(" " * (halfway_point-ln),end="")
#     for digit in range(1,ln+1):
#         print(digit,end="")
#     for rev_digit in range(digit-1,0,-1):
#         print(rev_digit,end="")
#     print()
# print()

#while loop

n = int(input("Enter the number of lines (only odd numbers): ? "))
halfway_point = ( n//2 + n%2 )
ln=1
while ln<=halfway_point:     
        print(" "*(halfway_point-ln),end="")
        digit=1
        while digit<=ln:
            print(digit,end="")
            digit=digit+1
        rev_digit=ln-1
        while rev_digit>=1:
            print(rev_digit,end="")
            rev_digit=rev_digit-1
        print()
        ln=ln+1
ln=halfway_point-1
while ln>=1:     
    print(" " * (halfway_point-ln),end="")
    digit = 1
    while digit <= ln:
        print(digit, end="")
        digit = digit + 1
    rev_digit = ln - 1
    while rev_digit >= 1:
        print(rev_digit, end="")
        rev_digit = rev_digit - 1
    print()
    ln=ln-1
print()