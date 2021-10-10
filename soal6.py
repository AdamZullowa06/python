# Soal No.6

"""Diketahui bilangan 60, 20, 100, dan 40.
    Tentukan nilai terbesar diantara keempat bilangan!"""

# Simpan nilai bilangan ke dalam variable
a = 60 # variable a simpan nilai 60
b = 20 # variable b simpan nilai 20
c = 100 # variable c simpan nilai 100
d = 40 # variable d simpan nilai 40

# Gunakan elif statement

# jika a > b dan a > c dan a > d, tampilkan bilangan terbesar adalah a
if a > b and a > c and a > d :
    print(f"Bilangan terbesar adalah {a}")

# jika b > a dan b > c dan b > d, tampilkan bilangan terbesar adalah b
elif b > a and b > c and b > d :
    print(f"Bilangan terbesar adalah {b}")

# jika c > a dan c > b dan c > d, tampilkan bilangan terbesar adalah c
elif c > a and c > b and c > d :
    print(f"Bilangan terbesar adalah {c}")

# jika tidak ada di kondisi diatas, tampilkan bilangan terbesar adalah d
else :
    print(f"Bilangan terbesar adalah {d}")