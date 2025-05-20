class OpsiPengiriman:
    ekspedisi = ["sifast", "j&e", "j&teh"]

    def __init__(self, nama_ekspedisi):
        self.nama_ekspedisi = nama_ekspedisi
    
    def pilih(self):
        if self.nama_ekspedisi.lower() in self.ekspedisi:
            self.ekspedisi[0] = 10000
            self.ekspedisi[1] = 12000
            self.ekspedisi[2] = 13000
        else:
            print("Ekspedisi yang anda masukkan tidak ada di daftar pilihan")
