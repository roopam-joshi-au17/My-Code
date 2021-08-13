'''
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. pop: Pop the last element from the list.
6. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the types listed above. Iterate through each
command in order and perform the corresponding operation on your list.
'''

n=int(input("Enter the amount of operation you want to perform :"))
list1=[]
for k in range(1,n+1):
    op=input().split(" ")
    for i in range(1,len(op)):
        op[i]=int(op[i])
    if op[0]=='insert':
        list1.insert(op[1],op[2])
    elif op[0]=='print':
        print(list1)
    elif op[0]=='remove':
        list1.remove(op[1])
    elif op[0]=='append':
        list1.append(op[1])
    elif op[0]=='pop':
        list1.pop()
    elif op[0]=='reverse':
        list1.reverse()
    else:
        print("wrong operation done :you have",n-k, "operation left")
    