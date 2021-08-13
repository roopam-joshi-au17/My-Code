'''
Write code for the following sequence by taking line number as user input.
n = 3
  1
 121
12321
n = 4
   1
  121
 12321
1234321 
'''
#for loop
# n = int(input("Enter number of lines :"))
# for ln in range(1,n+1):
#     print(" "*(n-ln),end="")
#     for digit in range(1,ln+1):
#         print(digit,end="")
#     for rev in range(ln-1,0,-1):
#         print(rev,end="")
#     print()
# print()

#while loop
n = int(input("Enter the number of lines : "))
ln=1
while (ln<=n):
    print(" " * (n - ln),end="")
    digit=1
    while digit<=ln:
        print(digit,end="")
        if ln==digit:
            rev_digit=ln-1
            while rev_digit>=1:
                print(rev_digit,end="")
                rev_digit=rev_digit-1
        digit=digit+1
    print()
    ln=ln+1
print()