# python return value

def jumlah(*list_angka) :
    total = 0
    for angka in list_angka :
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlah(1,2,3,4,5,8)

# mengambil data total
print(f"Total {list_angka} = {total}")