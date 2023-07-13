# 1.soru

# 2.soru
sayi1=int(input("Başlangıç Değerini Girin : "))
sayi2=int(input("Bitiş Değerini Girin : "))
 
toplam=0
for i in range(sayi1,sayi2+1):
  toplam+=i
 
ortalama = toplam / (sayi2-sayi1 + 1)
print("Sayıların Ortalaması: ",ortalama)
# 3.soru
    