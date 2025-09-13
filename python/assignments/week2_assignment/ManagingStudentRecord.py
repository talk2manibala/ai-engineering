class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
    def update_grade(self, new_grade):
        self.grade = new_grade
        return f"{self.name}'s grade updated to {self.grade}"
    
if __name__ == "__main__":
    student1 = Student("John Doe", 20, "A")
    print(student1.display_info())
    print(student1.update_grade("A+"))
    print(student1.display_info())
    
    student2 = Student("Jane Smith", 22, "B")
    print(student2.display_info())
    print(student2.update_grade("A"))
    print(student2.display_info())

    student3 = Student("Emily Davis", 19, "C")
    print(student3.display_info())