def recursion(x):
    if x <= 0:
        return
    print("Recursion:", x)
    recursion(x - 1)

recursion(5)