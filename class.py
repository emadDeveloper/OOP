class student:
    Roll = ''
    Gpa = ''

    def see(self):
        print(f'Roll : {self.Roll}, Gpa : {self.Gpa}')

emad = student()
emad.Roll = 20
emad.Gpa = 4.00
emad.see()

akram = student()
akram.Roll = 30
akram.Gpa = 4.07
akram.see()

imran = student()
imran.Roll = 35
imran.Gpa = 4.11
imran.see()


    