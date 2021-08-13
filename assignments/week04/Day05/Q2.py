'''
You are given an integer, n. Your task is to print an alphabet rangoli of size .
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has
the alphabet letter (in alphabetical order).
[Hint: Use the chr() and ord() function in python and then try to build this
pattern]
Constraints: Use a single while loop to solve this question
Sample Input
5
Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

nl=int(input("Enter the number of lines to be printed :"))
str1=""
i=1
while(i<=2*nl-1):
    if(i<=nl):
        str1=str1[0:len(str1)//2+1]+"-"+chr(97+nl-i)+"-"+str1[len(str1)//2:len(str1)]
        if(i!=nl):
            print("-"*(2*(nl-i)-1)+str1+"-"*(2*(nl-i)-1))
        else:
            str1=str1[1:len(str1)-1]
            print(str1)
    else:
        if(i!=2*nl-1):
            str1=str1[0:len(str1)//2-1]+str1[(len(str1)//2-3)::-1]
            print("-"*2*(i-nl)+str1+"-"*(2*(i-nl)))
        else:
            str1=str1[0]
            print("-"*2*(i-nl)+str1+"-"*(2*(i-nl)))
    i+=1