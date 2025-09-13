def namelist(**kwargs):
    print("Keyword arguments received:", kwargs)
    print("Type of kwargs:", type(kwargs))
    consolidated_name=""
    for key, value in kwargs.items():
        print(key + ": " + value)
namelist(first="John", last="Doe")
namelist(first="Jane", middle="A.", last="Smith", suffix="Jr.")


dict1 = {"first": "Alice", "last": "Johnson"}
namelist(**dict1)   