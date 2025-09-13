role=input("Enter your role (admin/guest): ")
match role:
    case "admin":
        print("Welcome, admin! You have full access")
    case "guest":
        print("Welcome, guest! You have limited access")
    case default:
        print("Unknown user! Access denied")