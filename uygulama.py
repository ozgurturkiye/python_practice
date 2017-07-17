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

def topla(a, b):
    return a + b

def factorial(a):
    if a < 2:
        return 1
    else:
        return a * factorial(a - 1)


while True:

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
        pass

    elif choice == "4":
        pass

    elif choice == "5":
        pass

    elif choice == "Q" or choice == "q":
        print("Çıkılıyor....")
        break

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", metin)
