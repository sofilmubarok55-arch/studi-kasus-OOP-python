class Dosen:
    def __init__(self, nidn, nama, prodi, fakultas):
        # Struktur Atribut
        self.nidn = nidn
        self.nama = nama
        self.prodi = prodi
        self.fakultas = fakultas

    # Logika / Fungsi
    def cek_profil(self):
        print(f"NIDN     : {self.nidn}")
        print(f"Nama     : {self.nama}")
        print(f"Prodi    : {self.prodi}")
        print(f"Fakultas : {self.fakultas}")
        print("-" * 30)

    def cek_prodi(self):
        return f"Dosen {self.nama} mengajar di program studi {self.prodi}."

# Instansiasi Objek (minimal 3 objek dosen)[cite: 1]
dosen1 = Dosen("00112233", "Dr. Budi Santoso", "Teknik Informatika", "Fakultas Ilmu Komputer")
dosen2 = Dosen("00445566", "Siti Aminah, M.T.", "Sistem Informasi", "Fakultas Ilmu Komputer")
dosen3 = Dosen("00778899", "Prof. Ahmad Dahlan", "Teknik Elektro", "Fakultas Teknik")

# Cetak profil seluruh data[cite: 1]
print("=== PROFIL SELURUH DOSEN ===")
dosen1.cek_profil()
dosen2.cek_profil()
dosen3.cek_profil()