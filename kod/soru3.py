#soru 3
sayi=int(input("Faktöriyeli hesaplanacak sayıyı giriniz: "))
faktoriyel = 1
for x in range(1,sayi+1):
    faktoriyel*=x
print("Faktöriyel:",faktoriyel)