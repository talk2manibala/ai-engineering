amount = int(input("Enter Amount (Only multiples of 100) : "))
if (amount) % 100 == 0:
    print("Dispensing Cash : " + str(amount))
else:
    print("Invalid Amount, Please enter the amount in multiples of 100")