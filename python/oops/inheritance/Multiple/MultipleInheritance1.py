class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    def is_adult(self):
        return self.age >= 18
    
class Profession:
    def __init__(self, profession):
        self.profession = profession

    def display_profession(self):
        print(f"Profession: {self.profession}") 

class Employee(Person, Profession):
    def __init__(self, name, age, profession, employee_id):
        Person.__init__(self, name, age)
        Profession.__init__(self, profession)
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        self.display()
        self.display_profession()
        self.birthday()
        print(f"Is adult: {self.is_adult()}")


if __name__ == "__main__":
    emp1 = Employee("Charlie", 28, "Engineer", "E123")
    emp1.display_employee()