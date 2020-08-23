class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num,"/",self.den)

    def get_num(self):
        print("The numerator is:",self.num)

    def get_den(self):
        print("The denominator is:",self.den)

my_f = Fraction(3, 5)
my_f.show()
my_f.get_num()
my_f.get_den()
