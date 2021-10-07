# belajar tipe data dictionary

customer = {"Name":"eko", "Age":30, "Alamat":"subang"}

name = customer["Name"]
age = customer["Age"]
address = customer["Alamat"]

customer["Company"] = "x"
customer["Name"] = "adam"

del customer["Alamat"]

for key,value in customer.items() :
    print(f"{key}: {value}")