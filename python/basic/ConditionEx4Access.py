print("Welcome to Testleaf")
print("******************")

age = int(input("Enter your age : "))
itExperience = int(input("Enter your IT Experience : "))
print("Your age is : " + str(age))
print("Your IT Experience is : " + str(age))
print("--------------------")
if (age >= 22 and itExperience >= 2):
    print("+++ Access Granted +++")
else:
    print("--= Access Denied ---")