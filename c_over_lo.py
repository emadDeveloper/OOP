class student:

    def __init__(self,**info):
        if len(info)==3:
          self.name = info['name'] 
          self.id = info['id']
          self.cgpa = info['cg']

        elif len(info)==2:
          self.name = info['name'] 
          self.id = info['id']

        elif len(info)==1:
           self.name = info['name']

        print('a student created')        


s1 = student(name = 'jord', id=13, cg=3.75)
s2 = student(name = 'bobi', id=34)        
s3 = student(name = 'mike')
s4 = student()
print(s1)