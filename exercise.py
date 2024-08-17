#sclass emad:
    #def __init__(self,name,tk):
        #self.name = name
        #self.tk = tk


#eb = emad('akram',1400) 
#print(eb.tk) 
#eb.tk = 1600
#print(eb.tk)  

#class student:
    #def __init__(self,name,id):
        #self.__name = name
        #self.__id = id

    #def details(self):
        #print('name:', self.__name, 'id:', self.__id)

    #def set_id(self,id):
        #if(id>0):
            #self.__id = id
        #else:
            #print('wrong number, enter number again') 

    #def get_id(self):
        #return self.__id

    #def set_name(self,name):
        #self.__name = name 

    #def get_name(self):
        #return self.__name  


#s1 = student('jorge',21)
#s1.set_id(22)
#print(s1.get_id())
#s2 = student('fara',23) 
#s2.set_name('pori')
#print(s2.get_name())
#s1.details() 
#s2.details()      
# 
# 

#class student:
    #def  __init__(self,name,id):
        #self.name = name
        #self.id = id

    #def details(self):
        #print('name:', self.name, 'id:', self.id)


#class BAstudent(student):
    #def __init__(self,name,id,workshop):
        #super().__init__(name,id)
        #self.no_of_workshop = workshop

    #def cry(self):
        #print('BA students is crying for', self.no_of_workshop,'workshop')



#class CAstudent(student):
    #def party(self):
        #print('party in everyday')


#s1 = BAstudent('najir',33,5)
#s2 = CAstudent('kajir',22)
#s1.details()
#s2.details() 
#s1.cry()
#s2.party()                                        

