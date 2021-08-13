#Write a program that takes in 2 numbers and returns true if they are divisible by each other ,otherwise false

n1= int(input("Enter First Number : "))
n2= int(input("Enter Second Number : "))
print(not(bool(n1%n2)) or not(bool(n2%n1)))
