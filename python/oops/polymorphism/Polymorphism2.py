class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
class Profession:
    def __init__(self,  profession):
        self.profession = profession

    def display(self):
        print(f"Profession: {self.profession}")


class Experience(Person, Profession):
    def __init__(self, name, age, profession, years_experience):
        Person.__init__(self, name, age)
        Profession.__init__(self, profession)
        self.years_experience = years_experience

    def display(self):
        Person.display(self)
        Profession.display(self)
        print(f"Years of Experience: {self.years_experience}") 

if __name__ == "__main__":
    mr = Experience("Alice", 30, "Engineer", 5)
    mr.display()