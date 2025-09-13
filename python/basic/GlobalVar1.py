c=5

def change1():
    c=10
    print("'c' Inside change1 function", c)

def change2():
    #globals()['c']=50
    global c
    c=50
    print("'c' Inside change 2 function", c)
    return c

change1()
print("'c' After change1 function", c)
change2()
print("'c' Outside function", c)
