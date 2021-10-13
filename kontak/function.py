# function kontak
from tabulate import tabulate

# menu daftar kontak
def display_kontak(daftar_kontak) :
    print("+-------+ Daftar Kontak +-------+")
    print(tabulate(daftar_kontak, headers="keys", tablefmt="pretty"))

# menu tambah kontak
def new_kontak() :
    print("+-------+ Tambah Kontak +-------+")
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    print("Kontak berhasil ditambah!, cek menu daftar kontak")
    return kontak

# menu hapus kontak
def hapus_kontak(daftar_kontak) :
    nama = input("Nama yang ingin dihapus : ")
    index = -1
    
    for i in range(0, len(daftar_kontak)) :
        kontak = daftar_kontak[i]
        if nama == kontak["nama"] :
            index = i
            break
    
    if index == -1 :
        print("Data tidak ditemukan!")
    else :
        del daftar_kontak[index]
        print("berhasil menghapus data kontak!, cek menu daftar kontak")

# menu cari kontak
def cari_kontak(daftar_kontak) :
    nama_input = input("Nama yang dicari : ")

    for kontak in daftar_kontak :
        nama = kontak["nama"]
        if nama.lower().find(nama_input.lower()) != -1 :
            print("+--------+ Cari Kontak +--------+")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"Telepon : {kontak['telepon']}")