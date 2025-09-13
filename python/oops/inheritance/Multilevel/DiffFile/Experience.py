from Profession import Profession
class Experience(Profession):
    def __init__(self, name, age, profession, years_experience):
        super().__init__(name, age, profession)
        self.years_experience = years_experience

    def display_experience(self):
        print(f"{self.name} has {self.years_experience} years of experience as a {self.profession}.")  
        self.display()
        self.display_profession()
        self.birthday()
        print(self.is_adult())
        print(f"Is adult: {self.is_adult()}")
if __name__ == "__main__":
    e1 = Experience("Charlie", 28, "Designer", 5)
    e1.display_experience()
    