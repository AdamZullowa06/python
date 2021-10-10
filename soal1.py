# soal cerita 2

"""Seorang pedagang mangga menjual dagangannya
yang setiap kg mangga dihargai dengan harga
tertentu. Setiap pembeli membayar harga
mangga yang dibeli nya berdasarkan berat."""

# Algoritma :
# 1. Masukkan harga mangga per kg (harga)
# 2. Masukkan berat pembelian (berat)
# 3. Kalikan harga dengan berat, simpan sebagai harga yang harusdibayar (bayar)
# 4. Tampilkan nilai bayar
# 5. Selesai

print("=+=+=+=+ jawaban no.6 =+=+=+=+")

# Masukan input harga dan berat
berat = int(input("Masukan berat (kg): "))
harga = int(input("Masukkan Harga (per kg): "))

# jumlah yang dibayar adalah harga dikalikan berat
bayar = harga * berat

curr = "Rp. {:,.2f}".format(bayar)

# tampilkan jumlah yang harus dibayar
print(f"Jumlah yang harus dibayar : {curr}")
print("=+=+=+=+ selesai =+=+=+=+")