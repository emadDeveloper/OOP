#class student:
    #def __init__(self,name,id):
        #self.name = name
        #self.id = id
        #print('a student came ')
    #def  details(self):
        #print("name:", self.name, "id:", self.id)    


#s1 = student('bark',12)
#s1.details()


class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def details(self):
        print("name:", self.name, "id:", self.id)    



s1 = student('ramsy',23) 
s2 = student('james',34)
s1.details()