class student:

    uni_name = 'AIUB'


    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def details(self):
        print('name:', self.name, 'id:', self.__id, student.uni_name) 

    @classmethod
    def up_uni_name(cls,u_name):
        cls.uni_name = u_name

    @classmethod
    def from_string(cls,info):
        name,id = info.split('-')
        obj = cls(name,id)
        return obj    



s1 = student.from_string('johir-47')
s2 = student('sabir',45)
s1.details()
s2.details()
student.up_uni_name('American International University')
s1.details()
s2.details()