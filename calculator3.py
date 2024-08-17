from multipledispatch import dispatch

class my_calculator:

    @dispatch(int,int)
    def product(self,a,b):
        print(a*b)

    @dispatch(int,int,int)    
    def product(self,a,b,c):
        print(a*b*c)


c1 = my_calculator()
c1.product(2,6)
c1.product(3,6,9)            