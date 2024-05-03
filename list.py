namelist=["Wasif","Nazifa","Prithiraj","John"]
print(namelist)
print(type(namelist))

namelist[1]="Robiul"
print(namelist)

namelist.append("Praggo")
print(namelist)

namelist.insert(3,"Ubaiz")
print(namelist)

namelist.remove("Praggo")
print(namelist)

namelist.pop(4)
print(namelist)