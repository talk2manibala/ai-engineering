# Use of "_" is temporary variable or to ignore the value
# Placeholder when the variable itself is not going to be used in the code
# Commonly used in loops or unpacking values


for _ in range(4) :
    print ("Hello")

def return_numbers():
    return 10, 20

_, num2 = return_numbers() # Ignoring the first value
print("The value of num2 is: " + str(num2))

num1, _ = return_numbers() # Ignoring the second value
print("The value of num2 is: " + str(num1))

