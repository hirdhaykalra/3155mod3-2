#Worked with Haley Siharath

class student:
    name = ''
    GPA = 0.0
    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA
    
    def report_gpa(self):
        return f"{self.name} has a gpa of {self.GPA}"
