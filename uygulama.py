#1. Program - Python shell de çalışan 5 temel uygulama denemesi :)
metin = """
(1) Toplama yap
(2) Faktoriyel bul
(3) Öğrenci listesi işlemleri
(4) İngilizce sözlük işlemleri
(5) Asker oluştur :)

-------------------------
Lütfen Seçiminizi yapınız
Çıkmak için (q) ya basınız
"""

d ="Devam etmek için bir tuşa basınız"

go_on_champion = "Devam etmek için bir tuşa basınız!"

ogrenci_liste = ["Ali Taş", "Mehmet İnce", "Ayşe Uzun"]

def topla(a, b): # Toplama yapan fonksiyon :)
    return a + b

def factorial(a): # Faktoriyel hesaplayan fonksiyon reqursive yalnız :)
    if a < 2:
        return 1
    else:
        return a * factorial(a - 1)


while True: # Q veya q seçilmediği sürece program çalışır.

    print(metin)
    choice = input("Yapmak istediğiniz işlemi seçiniz: ")

    if choice == "1":
        number1 = int(input("1. sayıyı giriniz: "))
        number2 = int(input("2. sayıyı giriniz: "))
        print("Sonuç: ", topla(number1, number2))
        input(go_on_champion)

    elif choice == "2":
        factorial_number = int(input("Faktoriyelini bulmak istediğiniz sayıyı giriniz: "))
        print("Sonuç: ", factorial(factorial_number))
        input(go_on_champion)

    elif choice == "3":
        liste_metin = """
        (1) Çğrenci listesini görüntüle
        (2) Yeni öğrenci ekle
        (3) Öğrenci ismi düzenle
        (4) Listeden öğrenci sil
        (5) Çıkış.
        """

        while True:
            print(liste_metin)
            liste_secim = input("Yapmak istediğiniz işlemi seçiniz: ")

            if liste_secim == "1":
                print(ogrenci_liste)

            elif liste_secim == "2":
                ogrenci_isim = input("Eklemek istediğiniz öğrenciyi giriniz: ")
                ogrenci_liste.append(ogrenci_isim)
                print("{} isimli öğrenci başarıyla eklendi.".format(ogrenci_isim))
                input(go_on_champion)

            elif liste_secim == "3":
                ogrenci_sirasi = int(input("Düzenlemek istediğiniz öğrenci sıra numarası giriniz: "))
                print(ogrenci_liste[ogrenci_sirasi], "isimli öğrenciyi düzenliyorsunuz")
                ogrenci_duzenleme = input("Yeni ismi giriniz: ")
                ogrenci_liste[ogrenci_sirasi] = ogrenci_duzenleme



            elif liste_secim == "5":
                print("Liste menüsünden çıkıldı.")
                break
            else:
                print("Yanlış giriş.")


    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "Q" or choice == "q":
        print("Çıkılıyor....")
        break

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:")
