class Student:
    def __init__(self):
        self.Roll = int(input('Enter Emad roll: '))
        self.Gpa = float(input('Enter Emad GPA: '))

    def see(self):
        print('Roll', self.Roll)
        print('cgpa', self.Gpa)

emad = Student()
emad.see()