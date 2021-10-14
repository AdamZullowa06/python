# program hitung gaji karyawan

from tabulate import tabulate

print("+------------------+ PRORGAM HITUNG GAJI KARYAWAN +------------------+")
print("Masukkan data karywan : \n")

# variable
gaji_pokok = 300000
honor_lembur = 3500

# tunjangan jabatan
def tunjangan_jabatan(golongan) :
    jumlah = 0

    if golongan == "1" :
        jumlah = gaji_pokok * 5 / 100

    elif golongan == "2" :
        jumlah = gaji_pokok * 10 / 100

    elif golongan == "3" :
        jumlah = gaji_pokok * 15 / 100

    else :
        jumlah

    return jumlah

# function tunjangan pendidikan
def tunjangan_pendidikan(pendidikan) :
    jumlah = 0

    if pendidikan == "sma" :
        jumlah = gaji_pokok * 2.5 / 100
    
    elif pendidikan == "d1" :
        jumlah = gaji_pokok * 5 / 100

    elif pendidikan == "d3" :
        jumlah = gaji_pokok * 20 / 100

    elif pendidikan == "s1" :
        jumlah = gaji_pokok * 20 / 100

    else :
        jumlah

    return jumlah

# function jam lembur
def honor(jam) :
    lembur = 0

    if jam > 8 :
        selisih = jam - 8
        lembur = selisih * honor_lembur
    
    else :
        lembur

    return lembur

# input variabel
nama = input("Nama Karyawan : ").title()
golongan = tunjangan_jabatan(input("Golongan Jabatan [1/2/3] : "))
pendidikan = tunjangan_pendidikan(input("Pendidikan [SMA/D1/D3/S1] : "))
lembur = honor(int(input("Jumlah jam kerja : ")))

# total gaji
total = gaji_pokok + golongan + pendidikan + lembur

gaji_jabatan = "{:,.2f}".format(golongan)
gaji_pendidikan = "{:,.2f}".format(pendidikan)
gaji_lembur = "{:,.2f}".format(lembur)
gaji_total = "{:,.2f}".format(total)

# output literal
print("\n+------------------+ Hasil +------------------+")
print(f"Nama Karyawan : {nama}")
print(f"Honor yang diterima")
print(f"tunjangan jabatan : Rp {gaji_jabatan}")
print(f"tunjangan pendidikan : Rp {gaji_pendidikan}")
print(f"tunjangan lembur : Rp {gaji_lembur}")
print(f"total gaji : Rp {gaji_total}")

# output table
table = [[nama, gaji_jabatan, gaji_pendidikan, gaji_lembur, gaji_total]]
header = ["Nama", "Tunjangan Jabatan", "Tunjangan Pendidikan", "Honor Lembur", "Total Gaji"]
print(tabulate(table, headers=header, tablefmt="pretty"))