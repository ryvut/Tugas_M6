ipk = float(input("Masukkan IPK saat ini: "))

riwayat_nilai = ["A", "B+", "A-", "B", "C"]

syarat_ipk = ipk >= 3.50
syarat_nilai = "E" not in riwayat_nilai

lolos_beasiswa = syarat_ipk and syarat_nilai

print(f"IPK: {ipk}")
print(f"Riwayat Nilai: {riwayat_nilai}")
print(f"Apakah mahasiswa memenuhi syarat beasiswa? {lolos_beasiswa}")