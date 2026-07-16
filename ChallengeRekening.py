class Rekening:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru < 0 :
            raise ValueError("Saldo tidak boleh negatif!")
        self._saldo = saldo_baru

    def setor(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah setor harus positif")
        else:
            self.saldo += jumlah

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak cukup!")
        else:
            self.saldo -= jumlah
    
    def info(self):
        print(f"{self.pemilik}: saldo Rp{self.saldo}")

class RekeningPremium(Rekening):
    def __init__(self, pemilik, saldo, limit_tarik_harian):
        super().__init__(pemilik, saldo)
        self.limit_tarik_harian = limit_tarik_harian
        
    def tarik(self, jumlah):
        if jumlah > self.limit_tarik_harian:
            raise ValueError("Melebihi limit tarik harian")
        else:
            super().tarik(jumlah)

    def info(self):
        super().info()
        print(f"Limit tarik harian: Rp{self.limit_tarik_harian}")

    def tambah_bunga(self):
        bunga = self.saldo * 0.05
        self.saldo += bunga
        print(f"Bunga ditambahkan: Rp{bunga}")

r1 = Rekening("Budi", 500000)
r1.info()
r1.setor(200000)
r1.info()
r1.tarik(100000)
r1.info()

r2 = RekeningPremium("Sami", 5000000, 10000000)
r2.info()
r2.tarik(2000000)
r2.info()

# Ini harus ERROR:
r2.tarik(15000000)  # melebihi limit harian
