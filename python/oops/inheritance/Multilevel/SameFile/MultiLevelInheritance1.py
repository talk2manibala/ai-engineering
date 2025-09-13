class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    def is_adult(self):
        return self.age >= 18
    
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}, is adult: {self.is_adult()}")            
    
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
    

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def team_size(self, team_size):
        self.team_size = team_size
        print(f"{self.name} {self.employee_id} manages a team of {self.team_size} people in the {self.department} department.")    
    
if __name__ == "__main__":
    mgr = Manager("David", 40, "M456", "Sales")
    mgr.team_size(10)

