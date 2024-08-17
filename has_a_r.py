class engine:
    def __init__(self,cc):
        self.capacity = cc

    def start(self):
        print('engine is starting')

    def stop(self):
        print('engine is stoping')


class car:
    def __init__(self,name,cc):
        self.name = name
        self.engine = engine(cc)

    def run(self):
        print('car is running')


c1 = car('audi',3000)
c1.run() 
                           