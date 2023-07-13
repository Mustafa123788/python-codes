defkullanici = "Yazilimcibebe"
defparola = "1234"
while(True):
    kullanici = input("Kullanıcı adı: ")
    parola = input("Parola: ")
    if ((kullanici == defkullanici) and (parola == defparola)):
        print("Hoşgeldiniz",kullanici)
        break
    elif ((kullanici != defkullanici) and (parola == defparola)):
        print("Kullanıcı adınızı yanlış girdiniz: ")
    elif ((kullanici == defkullanici) and (parola != defparola)):
        print("Şifreyi mi unuttunuz")
        print("Şifreyi değiştirmek istermisiniz(E/H):")
        cevap = input()
        if (cevap == "E"):
            yeniparola = input("Yeni parola: ")
            print("Lütfen bekleyin")
            defparola = yeniparola
            print("Şifre başarıyla değiştirildi")
    else:
       print("Tekrar deneyin")