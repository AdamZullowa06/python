# Soal No.7
"""
Aldi mempunyai kelereng 15 lebih banyak dari budi,
Sedangkan Anto mempunyai kelereng 2x jumlah kelereng Aldi dan Budi.
Agung memiliki kelereng 5 buah lebih sedikit dari jumlah kelereng Aldi, Budi, dan Anto.
Berapa jumlah kelereng Budi, Anto dan Agung apabila jumlah kelereng Aldi diketahui?
"""

# masukkan/input jumlah kelereng aldi miliki
aldi = int(input("masukan jumlah kelereng aldi : "))

# kelereng yang dimiliki budi adalah kelereng aldi saat ini dikurang 15 kelereng
budi = aldi - 15

# jumlah kelereng anto adalah 2 kali jumlah kelereng budi dan aldi
anto = 2 * (aldi + budi)

# jumlah kelereng agung adalah jumlah kelereng aldi, budi, dan anto dikurang 5
agung = (aldi + budi + anto) - 5

# output/hasil
print(f"jumlah kelereng aldi : {aldi} buah") # tampilkan jumlah kelereng aldi
print(f"jumlah kelereng budi : {budi} buah") # tampilkan jumlah kelereng budi
print(f"jumlah kelereng anto : {anto} buah") # tampilkan jumlah kelereng anto
print(f"jumlah kelereng agung : {agung} buah") # tampilkan jumlah kelereng agung