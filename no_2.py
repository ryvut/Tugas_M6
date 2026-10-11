data_pelanggan = ("Budi Santoso", "Premium")

berat_kardus = [25.5, 30.0, 45.2, 10.0]

_, status_member = data_pelanggan

total_berat = sum(berat_kardus)

apakah_vip = (status_member == "Premium") or (total_berat > 100)

print(f"Status Member: {status_member}")
print(f"Total Berat Barang: {total_berat} kg")
print(f"Apakah pengiriman masuk jalur VIP? {apakah_vip}")