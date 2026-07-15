#Challenge - Konversi Suhu
# def konversi_suhu(tinggi_suhu, satuan_asal, *args):
#     print("=== KONVERSI SUHU ===")
#     print(f"Suhu Asal: {tinggi_suhu}°{satuan_asal}")
#     for target in args:
#         if satuan_asal == "C" and target == "F":
#             hasil = (tinggi_suhu * 9 / 5) + 32
#         elif satuan_asal == "C" and target == "K":
#             hasil = tinggi_suhu + 273.15
#         elif satuan_asal == "F" and target == "C":
#             hasil = (tinggi_suhu - 32) * 5/9
#         elif satuan_asal == "F" and target == "K":
#             hasil = (tinggi_suhu - 32) * 5/9 + 273.15
#         elif satuan_asal == "K" and target == "C":
#             hasil = tinggi_suhu - 273.15
#         elif satuan_asal == "K" and target == "F":
#             hasil = (tinggi_suhu - 273.15) * 9/5 + 32
#         else:
#             print(f"Ngapain dia {satuan_asal} → {target} bengak")
#             continue
#         print(f"{tinggi_suhu}°{satuan_asal} → {hasil}°{target}")

# konversi_suhu(100, "C", "F", "K")

from abc import ABC, abstractmethod

class suhu(ABC):
    def __init__(self, nilai):
        self.nilai = nilai

    @abstractmethod
    def ke_celsius(self) -> float:
        pass
    
    @abstractmethod
    def dari_celsius(self, nilai_c: float) -> float:
        pass

    @property
    def nilai(self):
        return self._nilai
    
    @nilai.setter
    def nilai(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)):
            raise ValueError("Harus berupa angka!")
        self._nilai = nilai_baru

    def konversi_ke(self, target_class):
        nilai_celsius = self.ke_celsius()
        objek_baru = target_class(0)
        return objek_baru.dari_celsius(nilai_celsius)
    
class Celsius(suhu):
    def ke_celsius(self):
        return self.nilai
    
    def dari_celsius(self, nilai_c):
        return nilai_c
    
class Fahrenheit(suhu):
    def ke_celsius(self):
        return (self.nilai - 32) * 5 / 9
    
    def dari_celsius(self, nilai_c):
        return (nilai_c * 9 / 5) + 32
    
class Kelvin(suhu):
    def ke_celsius(self):
        return self.nilai - 273.15
    
    def dari_celsius(self, nilai_c):
        return nilai_c + 273.15
    
class Reamur(suhu):
    def ke_celsius(self):
        return self.nilai * 5 / 4
    
    def dari_celsius(self, nilai_c):
        return nilai_c * 4 / 5
    

f = Fahrenheit(100)
print(f.konversi_ke(Kelvin))
print(f.konversi_ke(Celsius))

r = Reamur(80)
print(r.konversi_ke(Fahrenheit))