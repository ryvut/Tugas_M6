usia = int(input("Masukkan usia pendaftar: "))
nama_departemen = input("Masukkan nama departemen mahasiswa: ")

syarat_usia = usia >= 19
syarat_departemen = "Statistika" in nama_departemen

hasil_lolos = syarat_usia and syarat_departemen

print(f"Apakah pendaftaran diterima oleh sistem? {hasil_lolos}")