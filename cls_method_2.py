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



s1 = student('finch',1)
s2 = student('maxwell',100)
s1.view()
s2.view()
student.up_uni_name('North South University')
#print(s1.__dict__) 
s1.view() 
s2.view()         