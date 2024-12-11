from Animal import *

class Ikan(Animal):
    def __init__(self,nama,makanan,hidup,berkembang_biak,design,ciri_tubuh):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.design = design
        self.ciri_tubuh = ciri_tubuh
    def cetak_ikan (self):
        super().cetak()
        print("Design\t\t :",self.design,"\nciri tubuh\t : ",self.ciri_tubuh)

marlin = Ikan("marlin", "ikan kecil", "samudra atlantik", "bertelur", "biru,putih", "memanjang,moncong seperti tombak dan sirip panjang dan kaku")
marlin.cetak_ikan()
hiu_paus = Ikan("hiu_paus", "plankton", "laut samudra", "menghasilkan telur", "biru,putih", "bertotol putih")
hiu_paus.cetak_ikan()