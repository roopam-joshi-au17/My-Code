'''
Write a function fibonacci(n) which returns the nth fibonacci number. This
should be calcuated using the while loop. The default value of n should be 10.
fibonacci(1)
>>>0
fibonacci(2)
>>>1
fibonacci(3)
>>>1
fibonacci(4)
>>>2
fibonacci(5)
>>>3
Also find the maximum of:
fibonacci(12)+fibonacci(10) and fibonacci(11)+fibonacci(11).
'''
def fibonacci(n=10):
    if n==1:
        next=0
    elif n==2:
        next=1
    else:
        First_Value = 0
        Second_Value = 1
        i=3
        while(i <= n):
            next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = next
            i = i + 1
    return next
a= fibonacci(12)+fibonacci(10)
b=fibonacci(11)+fibonacci(11)
print(max(a,b))
