'''
Take 2 sequences of space separated integers as input from the user and convert
it into a list of integers. Extend the first list with all the items of the
second list and print the output.
Ex:
Input 1:
1 2 3 4
11 434 1
Output 1:
1 2 3 4 11 434 1
Input 2:
1 2 3
8 7
Output 2:
1 2 3 8 7
Hint: Consider using the inbuilt extend() function of lists in python
'''
list1 = ['1','2','3']  
list2 = ['4','5','6']  
list1.extend(list2)
print(list1)