# Class Induk[cite: 1]
class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def info(self):
        print(f"Nama      : {self.nama}")
        print(f"Merk      : {self.merk}")
        print(f"Tahun     : {self.tahun}")
        print(f"Kecepatan : {self.kecepatan} km/jam")

# Turunan 1: Mobil[cite: 1]
class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def info_mobil(self):
        self.info()
        print(f"Jumlah Kursi : {self.jumlah_kursi}")
        print("-" * 30)

# Turunan 2: Motor[cite: 1]
class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def info_motor(self):
        self.info()
        print(f"Tipe Motor   : {self.tipe_motor}")
        print("-" * 30)

# Pengujian
print("=== SISTEM RENTAL KENDARAAN ===")
mobil1 = Mobil("Avanza", "Toyota", 2022, 180, 7)
motor1 = Motor("Vario 160", "Honda", 2023, 120, "Matic")

mobil1.info_mobil()
motor1.info_motor()