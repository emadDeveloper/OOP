class player:
    def __init__(self,run):
        self.run = run

    def hit_four(self):
        self.run += 4

    def hit_six(self):
        self.run += 6



jahin = player(0)
jahin.hit_six()
arif = player(0)
arif.hit_four()
print('jahin:', jahin.run)
print('arif:', arif.run)                