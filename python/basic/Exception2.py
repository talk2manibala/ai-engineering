try:
    #print(x)
    #print(10/0)
    print("Hello, World!")

except NameError:
    print("Error: Variable 'x' is not defined.")
except:
    print("An unexpected error occurred.")
else:
    print("No errors occurred.")
finally:
    print("Execution completed.")