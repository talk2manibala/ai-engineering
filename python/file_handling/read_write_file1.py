file_path="python/file_handling/example.txt"

file = open(file_path, 'w')
file.write('Hello, World!\n')
file.write('Welcome to file handling in Python.\n')
file.close()

file = open(file_path, 'r')
content = file.read()
print(content)
file.close()