def login():
    actualPassword = "openAI123"
    for i in range(3):
        password = input("Enter Password : ")
        if password == actualPassword:
            print("Login Successful")
            return
        else:
            print("Incorrect Password. Try again.")
    print("Login Failed")

login()