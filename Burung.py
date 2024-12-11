from Animal import *

class Burung(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,design,terbang):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.design = design
        self.terbang = terbang
    def cetak_burung(self):
        super().cetak()
        print("Design\t\t :",self.design,"\nterbang\t : ",self.terbang)

humingbird = Burung("humingbird", "nektar", "hutan", "bertelur", "pelangi", "dapat diam di udara")
humingbird.cetak_burung()
lovebird = Burung ("lovebird", "biji-bijian", "hutan", "bertelur", "kuninng,hijau", "tidak dapat terbang")
lovebird.cetak_burung()