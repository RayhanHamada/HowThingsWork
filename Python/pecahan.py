

class Pecahan:

    def __init__(self, bulat = 0, pemb = 0, peny = 1):
        self.bulat = bulat
        self.pemb = pemb
        self.peny = peny

    def __add__(self, other):
        """

        :type other: Pecahan
        """
        bulat_baru = self.bulat + other.bulat
        if (self.peny == other.peny):
            pemb_baru = self.pemb + other.pemb
            if pemb_baru % self.peny == 0:
                bulat_baru += pemb_baru//self.peny
                return Pecahan(bulat_baru, 0, self.peny)
            return Pecahan(bulat_baru, pemb_baru, self.peny)
        else:
            pemb_baru = self.pemb * other.peny + self.peny * other.pemb
            peny_baru = self.peny * other.peny
            if (pemb_baru % peny_baru == 0):
                bulat_baru += pemb_baru//peny_baru
                return Pecahan(bulat_baru, 0, peny_baru)
            return Pecahan(bulat_baru, pemb_baru, peny_baru)

    def __sub__(self, other):
        """

        :type other: Pecahan
        """
        bulat_baru = self.bulat - other.bulat
        if self.peny == other.peny:
            pemb_baru = self.pemb - other.pemb
            if pemb_baru % self.peny == 0:
                bulat_baru -= pemb_baru // self.peny
                return Pecahan(bulat_baru, 0, self.peny)
            return Pecahan(bulat_baru, pemb_baru, self.peny)
        else:
            pemb_baru = self.pemb * other.peny - self.peny * other.pemb
            peny_baru = self.peny * other.peny
            if pemb_baru % peny_baru == 0:
                bulat_baru -= pemb_baru // peny_baru
                return Pecahan(bulat_baru, 0, peny_baru)
            return Pecahan(bulat_baru, pemb_baru, peny_baru)


    def __repr__(self):
        return "Pecahan({}, {}, {})".format(self.bulat, self.pemb, self.peny)



a = Pecahan(1, 1, 2)
b = Pecahan(2, 1, 2)

c = a - b

print(c)
