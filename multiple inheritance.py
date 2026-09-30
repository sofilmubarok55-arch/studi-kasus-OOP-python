# Class Induk 1[cite: 1]
class Pegawai:
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji

    def info_pegawai(self):
        print(f"ID Pegawai : {self.id_pegawai}")
        print(f"Nama       : {self.nama}")
        print(f"Gaji       : Rp {self.gaji:,}")

# Class Induk 2[cite: 1]
class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def info_proyek(self):
        print(f"Nama Proyek: {self.nama_proyek}")

# Class Turunan yang Mewarisi Multiple Class Induk (Project Manager)[cite: 1]
class ProjectManager(Pegawai, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek, tunjangan):
        # Inisialisasi dari kedua parent class
        Pegawai.__init__(self, id_pegawai, nama, gaji)
        PegawaiProyek.__init__(self, nama_proyek)
        self.tunjangan = tunjangan

    def cetak_profil_lengkap(self):
        print("=== PROFIL PROJECT MANAGER ===")
        self.info_pegawai()
        self.info_proyek()
        print(f"Tunjangan  : Rp {self.tunjangan:,}")
        print(f"Total Gaji : Rp {self.gaji + self.tunjangan:,}")
        print("-" * 30)

# Pengujian
pm1 = ProjectManager("PM-001", "Rina Wijaya", 15000000, "Pengembangan Aplikasi E-Commerce", 5000000)
pm1.cetak_profil_lengkap()