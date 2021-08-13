'''
Take a name, age and whether user has diabetes as user input and tell
them from when can they start taking vaccines for COVID-19. [Hint: you
can refer to the news for the timelines for each age group]
'''
name = input("Enter Your Name : ")
age = int(input("Enter Your Age: "))
diabetic = input("Do You have Diabetes ? : yes or no :")

if (age>=60) or (age>=45 and age<=59 and diabetic=="yes"):
    print("You can get Vaccinated from March 1")
elif (age>=45):
    print("You can get Vaccinated from April 1")
elif (age>=18):
    print("You can get Vaccinated from May 1")
elif (age<18):
    print("You are not Eligible for Vaccination ")