class student:

    uni_name = 'nsu'


    def __init__(self,name,id):
        self.name = name
        self.id = id

    def view(self):
        print('name:', self.name, 'id:', self.id, student.uni_name )

    @classmethod
    def up_uni_name(cls,u_name):
        cls.uni_name = u_name     

    @staticmethod
    def check_department(id):
        if id [3:5] == '01': print('cse')
        elif id [3:5] == '04': print('cs')  


student.check_department('234')          



 