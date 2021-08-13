'''
https://leetcode.com/problems/plus-one/
Discussed the one simple Approach and code it as well :-
Another approach discussed as sum and carry .
Please try to apply this approach as well . will discuss in the class.
'''
digit=[9,9,9,9]
for i in range(-1,-len(digit) -1,-1):
    if digit[i]==9:
        digit[i]=0
        if i== -len(digit):
            digit.insert(0,1)
    else:
        digit[i]+=1
        break
print(digit)