from Animal import *

class Ular(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,design,racun):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak()
        print("\nDesign\t\t :",self.design,"\nRacun\t : ",self.racun)

anaconda = Ular("Anaconda", "kambing", "amazon", "bertelur", "batik", "tidak berbisa")
anaconda.cetak_ular()
ularlaut = Ular("ular laut", "ikan", "lautan lepas", "bertelur", "hitam,putih", "sangat berbisa")
ularlaut.cetak_ular()

