isim=str(input("Adınızı giriniz: "))
maas=int(input("Maaşınızı giriniz: "))
calisma_yili=int(input("çalışma yılınızı giriniz: "))
if calisma_yili>=0 and calisma_yili<=5:
    zam=maas*0.10
    zamli_maas=maas+zam
    print("Sayın",isim,"Yeni maaşınız",zamli_maas)
elif calisma_yili>=6 and calisma_yili<=10:
    zam=maas*0.15
    zamli_maas=maas+zam
    print("Sayın",isim,"Yeni maaşınız",zamli_maas)
else:
    zam=maas*0.25
    zamli_maas=maas+zam
    print("Sayın",isim,"Yeni maaşınız",zamli_maas)