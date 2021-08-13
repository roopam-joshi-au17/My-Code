'''
You are given an integer, n. Your task is to print an alphabet rangoli of size .
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
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
'''

def print_rangoli(size):
    width  = size*4-3
    string = ''

    for i in range(1,size+1):
        for j in range(0,i):
            string = string + chr(96+size-j)
            if len(string) < width :
                string =string + '-'
        for k in range(i-1,0,-1):    
            string =string + chr(97+size-k)
            if len(string) < width :
                string =string + '-'
        print(string.center(width,'-'))
        string = ''
n = int(input("Enter the number of lines :"))
print_rangoli(n)
        

