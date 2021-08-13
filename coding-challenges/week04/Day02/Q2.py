'''
Accomplish the same task as Lists are US - 1 but without using the built-in
extend() function of the list data type in python.
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
'''
input_string1 = input('Enter elements of a first list separated by space ')
user_list1 = input_string1.split()
print('list: ', user_list1)
for i in range(len(user_list1)):
    user_list1[i] = int(user_list1[i])
input_string2 = input('Enter elements of a second list separated by space ')
user_list2 = input_string2.split()
print('list2: ', user_list2)
for i in range(len(user_list2)):
    user_list2[i] = int(user_list2[i])
user_list2[:0]=user_list1
print("Extended list : ",user_list2)
