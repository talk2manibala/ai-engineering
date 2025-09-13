class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.id}")

class Tester(Employee):
    def __init__(self, name, id, project):
        super().__init__(name, id)
        self.project = project

    def display_tester(self):
        print(f"Tester Name: {self.name}, ID: {self.id}, Project: {self.project}")  

    def run_tests(self):
        print(f"{self.name} is running tests on project {self.project}.")   

if __name__ == "__main__":
    tester1 = Tester("Bob", "T456", "ProjectX")
    tester1.display_tester()
    tester1.run_tests()
    tester1.display()