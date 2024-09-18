# Definisikan class untuk DataDiri
class DataDiri:
    # Constructor dengan atribut untuk data diri
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus
    
    # Method untuk menampilkan data diri
    def tampilkan_data(self):
        print(f"Nama    : {self.nama}")
        print(f"Kelas   : {self.kelas}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Fakultas: {self.fakultas}")
        print(f"Kampus  : {self.kampus}")

# Membuat objek dari class DataDiri
mahasiswa = DataDiri("Nur Kholis Yusuf Rabbani", "2023C", "23091397074", "D4 Manajemen Informatika", "Vokasi", "Universitas Negeri Surabaya")

# Menampilkan data diri
mahasiswa.tampilkan_data()
