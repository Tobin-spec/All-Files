def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def gc_d(self):
        common = gcd(self.num,self.den)
        return self.num == self.num // common
        return self.den == self.den // common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        

x = Fraction(1, 2)
y = Fraction(1, 4)
print(x + y)
