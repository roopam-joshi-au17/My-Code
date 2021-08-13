'''
Write a function called MaxSeq() which can take any number of inputs from the
user and returns the highest number in that sequence as the output.
[You cannot use the inbuilt function max() of python]
Ex:
Input 1:
11 2 3 4
Output 1:
11
Input 2:
1 2 3 8 7
Output 2:
8
'''
def MaxSeq(list1): 
    largest = list1[0] 
    for item in list1[:]:     
        if item > largest: 
            largest = item                       
    print("Largest element is:", largest) 
list1 = input('Enter elements of a list separated by space ').split()
print('list: ', list1)
for i in range(len(list1)):
    list1[i] = int(list1[i])
print(list1)
MaxSeq(list1)