try:
    with open("python/file_handling/example.txt", 'w') as file:
        file.write('Hello, World!\n')
        file.write('Welcome to file handling in Python.\n')

    with open("python/file_handling/example.txt", 'a') as file:
        file.write('Hello, World 2!\n')
        file.write('Welcome to file handling in Python 2.\n')

    with open("python/file_handling/example.txt", 'r') as file:
        content = file.read()
        print(content)

    print("File name : ", file.name)
    print("File closed : ", file.closed)
    print("File mode : ", file.mode)
except IOError as e:
    print(f"An error occurred: {e}")
finally:
    print("File operations completed.")