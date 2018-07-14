
class Mobil:

    def __init__(self, warna, cc, merek): #
        self.warna = warna  # menginisiasikan atribut warna
        self.cc = cc  # menginisiasikan atribut cc
        self.merek = merek  # menginisiasikan atribut plat nomor
        self.diam() # menginisiasikan keadaan awal mobil menjadi diam

    def diam(self):
        print("mobil dalam keadaan diam")

    def maju(self):
        print("mobil dalam keadaan bergerak maju")

    def mundur(self):
        print("mobil dalam keadaan mundur")

    # getter(pengambil) dan setter(penginisiasi) dari atribut Mobil

    def set_warna(self, warna):
        self.warna = warna

    def set_cc(self ,cc):
        self.cc = cc

    def set_merek(self, merek):
        self.merek = merek

    def get_warna(self):
        return self.warna

    def get_cc(self):
        return self.cc

    def get_merek(self):
        return self.merek


avanzo = Mobil("Biru", 1200, "Avanzo")  # membuat objek dengan identifier avanzo

print(avanzo.get_warna()) # mencetak atribut warna ke konsol
print(avanzo.get_cc()) # menceteak atribut cc ke konsol
print(avanzo.get_merek()) # mencetak atribut merek ke konsol

"""Konstruktor adalah metode penginisiasi properti dan keadaan awal instansi/ objek dari
   suatu class pada saat pertama kali diciptakan. contohnya jika kita membuat class 
   Mobil, untuk membedakan instansi satu Mobil dari Mobil lain, maka class Mobil 
   harus mempunyai atribut.
   
   Saat program dijalankan, terlihat bahwa metode self.diam() pertama kali tereksekusi,
   terlihat bahwa metode self.diam() tereksekusi pertama kali, dilanjutkan dengan di 
   eksekusinya metode mencetak atribut-atribut ke konsol. konstruktor secara otomatis ter-
   panggil.
   """
