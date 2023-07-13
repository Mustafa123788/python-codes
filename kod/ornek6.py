tercih=str(input("Nereye gitmek istersin(Sinema/Tiyatro):"))
if tercih=="Sinema":
    ogrenci=str(input("Öğrencimisiniz(E/H):"))
    if ogrenci=="E":
        indirim = 15 * 0.50
        indirimli_bilet = 15 - indirim
        print("Tutar",indirimli_bilet)
    else:
        print("Tutar","15 TL")
elif tercih=="Tiyatro":
    ogrenci=str(input("Öğrencimisiniz(E/H):"))
    if ogrenci=="E":
        indirim = 10 * 0.50
        indirimli_bilet = 10 - indirim
        print(indirimli_bilet)
    else:
        print("Tutar","10 TL")
else:
    print("Yanlış işlem girdiniz")



