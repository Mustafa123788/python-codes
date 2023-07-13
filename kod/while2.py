from random import randint
rand=randint(1, 100)
sayac=0
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında bir sayı giriniz(0 çıkış): "))
    if (sayi==0):
        print("Oyunu iptal ettiniz")
        break
    elif sayi < rand:
        print("Daha yüksek bir sayı girin")
    elif sayi > rand:
        print("Daha düşük bir sayı girin")
        continue
    else:
        print("Rastgele seçilen sayı!",rand)
        print("Tahmin sayınız",sayac)