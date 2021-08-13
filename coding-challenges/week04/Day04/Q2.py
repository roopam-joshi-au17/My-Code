'''
Create a dictionary that stores the following key value pairs:
(Name, Area): Phone Number
Populate this dictionary using user inputs as shown below:
Input:
Priyesh Shubham Megha Manish Vaibhav
Vadodara Bangalore Bangalore Bangalore Bangalore
9768576543 9736857654 9768576354 9768537654 9736857654
Output:
{(Priyesh,Vadodara): 9768576543, (Shubham,Bangalore): 9736857654,
(Megha,Bangalore): 9768576354, (Manish,Bangalore): 9768537654
(Vaibhav,Bangalore): 9736857654}
'''

names = input("Enter name separated by space :").split()
address =input("Enter address separated by space :").split()
phonenumber = input("Enter phone number separated by space :").split()
UserInput = {}
for i in range(0,min(len(names),len(address),len(phonenumber))):
  UserInput[names[i],address[i]] = (phonenumber[i])
print(UserInput)