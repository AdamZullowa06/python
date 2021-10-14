# latihan studi kasus : pendaftaran

# import module table
from tabulate import tabulate

print("+----------------+ Pendaftaran Mahasiswa Baru +----------------+")
print("Masukkan data mahasiswa : \n")

# input data mahasiswa
nama = input("Nama : ")
nim = input("Nim : ")
jurusan = input("Jurusan [SI/SIA]: ")

if jurusan.lower() == "si" :
    kode = "si"
    prodi = "sistem informasi"
    harga = "2.400.000"

    table = [[nama.title(),nim,kode,prodi.title(),harga]]
    header = ["Nama","Nim","Kode Jurusan","Nama Prodi","Harga"]
    print(tabulate(table, headers=header, tablefmt="pretty"))

elif jurusan.lower() == "sia" :
    kode = "sia"
    prodi = "sistem informasi akuntansi"
    harga = "2.000.000"

    table = [[nama.title(),nim,kode,prodi.title(),harga]]
    header = ["Nama","Nim","Kode Jurusan","Nama Prodi","Harga"]
    print(tabulate(table, headers=header, tablefmt="pretty"))

else :
    print("Input kode jurusan dengan tepat!")