# Tugas pertemuan 5

""" 
No. 1
Buatlah program untuk menggambar pola segitiga dengan sebuah karakter.
Karakter dapat berupa huruf atau karakter khusus seperti : *,#,%,@,& dan lainnya.
"""

num = int(input("Masukkan bilangan : "))
char = input("Masukkan karakter : ")
row = 0

while row < num :
    space = num - row - 1

    while space > 0 :
        print(end = " ")
        space = space - 1

    star = row + 1
    while star > 0 :
        print(f"{char}", end = " ")
        star = star - 1
    
    row = row + 1
    print()


"""
No. 2
Buatlah program tentang lagu anak ayam sebagai berikut
"""

num = int(input("Masukkan bilangan : "))
row = 0

print("\nTek kotek kotek, anak ayam turun berkotek")
while row < num :
    sisa = num - row - 1
    hidup = num - row

    if sisa == 0 :
        sisa = "induknya"

    print(f"anak ayam turunlah {hidup} mati satu tinggallah {sisa}")

    row = row + 1