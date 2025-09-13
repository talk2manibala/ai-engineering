class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}") 

class AutomationSkils:
    def __init__(self, tool):
        self.tool = tool

    def display(self):
        print(f"Automation Tool: {self.tool}")

class AutomationTester(Employee, AutomationSkils):
    def __init__(self, name, emp_id, tool, project):
        Employee.__init__(self, name, emp_id)
        AutomationSkils.__init__(self, tool)
        self.project = project

    def display(self):
        Employee.display(self)
        AutomationSkils.display(self)
        print(f"Project: {self.project}")


if __name__ == "__main__":
    tester = AutomationTester("Eve", "AT789", "Selenium", "Project Y")
    tester.display()