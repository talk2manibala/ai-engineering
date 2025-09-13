def add(*args):
    print("Arguments received:", args)
    print("Type of args:", type(args))
    return sum(args)

result = add(10, 20, 30)
print("The sum is: " + str(result))
result = add(10, 20, 30, 40, 50)
print("The sum is: " + str(result))