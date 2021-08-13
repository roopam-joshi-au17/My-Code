'''
Write a function which takes a list as an input from the user [using the input()
command] and returns the highest and the second highest elements of a list.
Ex:
Input 1:
1 2 3 4
Output 1:
3 4
Input 2:
1 2 3 8 7
Output 2:
7 8
'''
def highest(list1): 
    largest=max(list1)
    list1.remove(max(list1))
    largest2=max(list1)
    print("Largest element is:", largest) 
    print("Second Largest element is:", largest2)
list1 = input('Enter elements of a list separated by space ').split()
print('list: ', list1)
for i in range(len(list1)):
    list1[i] = int(list1[i])
print(list1)
highest(list1)