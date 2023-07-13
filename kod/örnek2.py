kenar1=int(input("İlk kenarı giriniz: "))
kenar2=int(input("İkinci kenarı giriniz: "))
kenar3=int(input("Üçüncü kenarı giriniz: "))
if(kenar1==kenar2 and  kenar1==kenar3 and kenar2==kenar3):
    print("Eşkenar üçgen")
elif(kenar1==kenar2 or  kenar1==kenar3 or kenar2==kenar3):
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")