boy=float(input("boyunuzu giriniz: "))
agırlık=int(input("ağırlığınızı giriniz: "))
vki=agırlık/(boy*boy)
if vki>=18 and vki<25:
    print("Normal")
elif vki>=25 and vki<30:
    print("kilolu")
elif vki>=30 and vki<35:
    print("obez")
else:
    print("Ciddi obez")