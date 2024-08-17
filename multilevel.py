class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def details(self):
        print('name:', self.name, 'id:', self.id)


class CSEstudent(student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.no_of_labs = labs

    def cry(self):
        print(self.name,'is crying because of', self.no_of_labs, 'labs')


class CSEFresher(CSEstudent):
    def enroll_CSE110(self):
        print(self.name,'enrolled in cse110')


s1 = CSEstudent('kofa',100,50)
s2 = CSEFresher('alikki',200,40)
s1.details()
s2.details()
s1.cry()
s2.cry()
s2.enroll_CSE110()                                