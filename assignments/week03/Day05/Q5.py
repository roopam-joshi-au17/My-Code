'''
5. Write a function that takes line number as input (with default value of 5) and prints the following pattern.
n=3
.....
.. ..
.   .
.. ..
.....
n = 5
.......
... ...
..   ..
.     .
..   ..
... ...
.......

'''
#for loop

n = int(input("Enter the number of lines (only odd numbers) ?:  "))
halfway_point=n//2+n%2
print("." * (n + 2))
for ln in range(1, halfway_point+1):
    print("." * (((n+1)//2)+1-ln) + " " * (2 * ln - 1) + "." * (((n+1)//2)+1-ln),end="")
    print()
for ln in range(halfway_point-1,0,-1):
    print("." * (((n+1)//2)+1-ln) + " " * (2 * ln-1) + "." * (((n+1)//2)+1-ln),end="")
    print()
print("." * (n + 2))

#while loop

n = int(input("Enter the number of lines (only odd numbers) ?:  "))
halfway_point=n//2+n%2
ln=1
print("." * (n + 2))
while ln<=halfway_point:
    print("." * (((n+1)//2)+1-ln) + " " * (2 * ln - 1) + "." * (((n+1)//2)+1-ln),end="")
    print()
    ln=ln+1
ln=halfway_point-1
while ln>=1:
    print("." * (((n+1)//2)+1-ln) + " " * (2 * ln-1) + "." * (((n+1)//2)+1-ln),end="")
    print()
    ln=ln-1
print("." * (n + 2))