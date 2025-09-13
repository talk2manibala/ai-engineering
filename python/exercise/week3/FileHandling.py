from collections import Counter

try:
    with open("python/exercise/week3/report.txt", 'w') as file:
        file.write('Test case 1 Passed\n')
        file.write('Test case 2 Failed\n')
        file.write('Test case 3 Passed\n')

    with open("python/exercise/week3/report.txt", 'a') as file:
        file.write('Test case 4 Passed\n')
        file.write('Test case 5 Failed')    

    line_count = 0
    with open("python/exercise/week3/report.txt", 'r') as file:
        for _ in file:
            line_count += 1
        print("Total : ", line_count)

    with open("python/exercise/week3/report.txt", 'r') as file:
        content = file.read().lower()  
        words = content.split()
        word_count = Counter(words)
    
        for word, count in word_count.items():
            if (word == "passed" or word == "failed"):
                print(f"{word} : {count}")
            
    print("File name : ", file.name)
    print("File closed : ", file.closed)
    print("File mode : ", file.mode)
except IOError as e:
    print(f"An error occurred: {e}")
finally:
    print("File operations completed.")