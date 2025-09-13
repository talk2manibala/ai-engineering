"""This is an class exercise"""

def add(*args):
    print("Arguments received = :", args)
    sum = 0
    for i in args:
        sum += i   # sum = sum + i
    return sum



print("Module name:", __name__)
if __name__ == "__main__":
    d = add(20, 10, 20, 10)
    print("Sum is =", d)
    print("Running from lib.py. Direct call")
    print(__doc__)
else:
    print("imported module")