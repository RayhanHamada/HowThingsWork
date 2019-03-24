

class Pecahan:

    """
    nilai default dari bulat adalah 0
    nilai default dari pemb adalah 0
    nilai default dari peny adalah 1, karena jika 0 maka hasil akan menjadi tidak terdefinisi

    e.g : 1/0 == tak terdefinisi
    """
    def __init__(self, bulat = 0, pemb = 0, peny = 1):
        self.bulat = bulat
        self.pemb = pemb
        self.peny = peny

    def __add__(self, other):
        """

        :type other: Pecahan
        """
        bulat_baru = self.bulat + other.bulat
        if (self.peny == other.peny):                           #jika penyebut sama, maka tinggal jumlahkan saja langsung penyebutnya
            pemb_baru = self.pemb + other.pemb
            if pemb_baru % self.peny == 0:                      #jika sisa pembagian antara pembilang baru dan penyebut adalah 0, maka tambahkan nilai bagi nya ke bulat_baru
                bulat_baru += pemb_baru//self.peny
                return Pecahan(bulat_baru, 0, self.peny)
            return Pecahan(bulat_baru, pemb_baru, self.peny)
        else:                                                   #jika penyebut tidak sama, maka harus disamakan dahulu
            pemb_baru = self.pemb * other.peny + self.peny * other.pemb
            peny_baru = self.peny * other.peny
            if (pemb_baru % peny_baru == 0):                    #jika sisa pembagian antara pembilang baru dan penyebut baru adalah 0, maka tambahkan hasil bagi nya ke bulat_baru
                bulat_baru += pemb_baru//peny_baru
                return Pecahan(bulat_baru, 0, peny_baru)
            return Pecahan(bulat_baru, pemb_baru, peny_baru)

    def __sub__(self, other):
        """
        overall step nya sama seperti di atas, hanya saja menggunakan operasi kurang
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

    """
       untuk mengembalikan nilai return berupa representasi string dari objek Pecahan
        
    """
    def __repr__(self):
        return "Pecahan({}, {}, {})".format(self.bulat, self.pemb, self.peny)



a = Pecahan(1, 1, 2)
b = Pecahan(2, 1, 2)

c = a - b

print(c)
