# class Anjing:
#     def __init__(self, nama, umur, ras):
#         self.nama = nama
#         self.umur = umur
#         self.ras = ras

#     def makan(self):
#         print(f"{self.nama} sedang makan")

#     def jaga(self):
#         print(f"{self.nama} berjaga di sekitar rumah")


# class AnjingPenjaga(Anjing):
#     def __init__(self, nama, umur, ras, level_keamanan):
#         super().__init__(nama, umur, ras)
#         self.level_keamanan = level_keamanan

#     def jaga(self):
#         super().jaga()
#         print(f"{self.nama} memiliki level keamanan: {self.level_keamanan}/5")

#     def gonggong_peringatan(self):
#         print(f"{self.nama} menggonggong keras! Ada yang mencurigakan!")

# anjing_biasa = Anjing("Max", 3, "Golden Retriever")
# anjing_biasa.makan()
# anjing_biasa.jaga()
# anjing_penjaga = AnjingPenjaga("Rex", 5, "Siberian Husky", 5)
# anjing_penjaga.makan()
# anjing_penjaga.jaga()
# anjing_penjaga.gonggong_peringatan()

class Anjing:
    def __init__(self, nama):
        self.nama = nama
    
    def jaga(self):
        print(f"{self.nama} berjaga di rumah")

class HewanTerlatih:
    def ikuti_perintah(self, perintah):
        print(f"Mengikuti perintah: {perintah}")

class AnjingPolisi(Anjing, HewanTerlatih):
    def __init__(self, nama, badge_number):
        super().__init__(nama)
        self.badge_number = badge_number
    
    def tugas(self):
        self.jaga()
        self.ikuti_perintah("cari narkoba")

polisi = AnjingPolisi("Rex", "B-2234")
polisi.tugas()