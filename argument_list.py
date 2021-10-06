# python argument list

def jumlah(*list_angka) :
    total = 0
    for angka in list_angka :
        total = total + angka
    print(f"total {angka} = {total}")

jumlah(1,2,3,4,5,6)