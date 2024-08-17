class student:
    Roll = ''
    Gpa = ''

    def set_value(self,Roll,Gpa):
        self.Roll = Roll
        self.Gpa = Gpa

    def see(self):
        print(f'Roll : {self.Roll}, Gpa : {self.Gpa}')

emad = student()
emad.set_value(15,3.55)
emad.see()

akram = student()
akram.set_value(19,4.55)
akram.see()

imran = student()
imran.set_value(23,3.34)
imran.see()


    