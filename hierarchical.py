class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print('name:', self.name, 'id:', self.id) 


class CSEstudent(student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.no_of_labs = labs

    def cry(self):
        print('CSE student is crying because of', self.no_of_labs, 'labs')


class BBAstudent(student):
    def party(self):
        print('they are happy for their party')


s1 = CSEstudent('jarki',21,4) 
s2 = BBAstudent('bobi',23)
s1.details()
s1.cry()   
s2.details() 
s2.party() 

                     
