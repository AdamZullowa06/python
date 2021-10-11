# # Contoh string input
# print("Hayoooo buruan masukin datanya !!! : ")

# # Input variable
# nama = input("Nama : ")
# nim = int(input("Nim : "))
# jurusan = input("Jurusan : ")
# alamat = input("Alamat : ")
# tugas = int(input("Nilai Tugas : "))
# uts = int(input("Nilai UTS: "))
# uas = int(input("Nilai UAS : "))

# # Nilai total
# count = tugas + uts + uas

# # Nilai rata rata
# sum = (tugas + uts + uas)/3

# if sum >= 80 :
#     hasil = "Anda lulus ngab :v"
# elif sum >= 70 and sum < 80:
#     hasil = "Lumayan, lumayan"
# elif sum < 70 and sum >= 50 :
#     hasil = "Segera lakukan Remedial !"
# elif sum < 50 and sum >= 20 :
#     hasil = "Anda kuliah ngapain aja sih???"
# else :
#     hasil = "Ga usah kuliah disini deh, cabut sono!"

# # data diri
# print("=+=+=+=+ Data Diri Mahasiswa =+=+=+=+")
# print(f"Nama : {nama}")
# print(f"Nim : {nim}")
# print(f"jurusan : {jurusan}")
# print(f"Alamat : {alamat}")
# # nilai akademik
# print("=+=+=+=+ Nilai Akademik Mahasiswa =+=+=+=+")
# print(f"Nilai Tugas : {tugas}")
# print(f"Nilai UTS : {uts}")
# print(f"Nilai UAS : {uas}")
# print(f"Total Nilai : {count}")
# print(f"Rata-Rata : {sum}")
# print(f"Status : {hasil}")
# print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

# print("Dah lah capek saya, bye")

# Tugas Pertemuan 2 | Adam Zullowa | 15210394 | 15.1A.31
print("Silakan masukan data diri : ")
 
# Input variable
nama = input("Nama : ") # input string ke variable nama
nim = int(input("Nim : ")) # input angka ke variable nim 
jurusan = input("Jurusan : ") # input string ke variable jurusan
alamat = input("Alamat : ") # input string ke variable alamat
tugas = int(input("Nilai Tugas : ")) # input angka ke variable tugas
uts = int(input("Nilai UTS: ")) # input angka ke variable uts
uas = int(input("Nilai UAS : ")) # input angka ke variable uas
 
# hitung jumlah nilai tugas,uts,uas. simpan ke variable sum
sum = tugas + uts + uas
 
# hitung rata-rata nilai tugas,uts,uas. simpan ke variable avg
avg = (tugas + uts + uas)/3
 
# Mencari kondisi nilai rata-rata
if avg >= 80 : # jika avg kurang dari sama dengan 80 (true)
    hasil = "Anda lulus" # simpan string ke var.hasil
elif avg < 80 and avg >= 50: # jika avg kurang dari 80 dan lebih dari sama dengan 50 (true)
    hasil = "Segera lakukan Remedial !" # simpan string ke var.hasil
else : # jika tidak ada di kondisi 1 dan 2 (false)
    hasil = "Anda tidak lulus" # simpan string ke var.hasil
 
# Output data diri
print("=+=+=+=+=+ Data Diri Mahasiswa =+=+=+=+=+")
print(f"Nama : {nama}") # output variable nama
print(f"Nim : {nim}") # output variable nim
print(f"jurusan : {jurusan}") # output variable jurusan
print(f"Alamat : {alamat}") # output variable alamat
# Output nilai akademik
print("=+=+=+=+ Nilai Akademik Mahasiswa =+=+=+=+")
print(f"Nilai Tugas : {tugas}") # output variable tugas
print(f"Nilai UTS : {uts}") # output variable uts
print(f"Nilai UAS : {uas}") # output variable uas
print(f"Total Nilai : {sum}") # output variable sum
print(f"Rata-Rata : {avg}") # output variable avg 
print(f"Status : {hasil}") # output variable hasil
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

