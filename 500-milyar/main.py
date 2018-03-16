import sys
import sqlite3
import random


class Question(): # Sorular sınıfı
  with sqlite3.connect('vt.sqlite') as vt:
    im = vt.cursor()

    im.execute("""SELECT * FROM questions WHERE difficulty = "1" """)
    question_easy = im.fetchall()
    question_easy = random.sample(question_easy, 3) # Rasgele üç örnek aldık

    im.execute("""SELECT * FROM questions WHERE difficulty = "2" """)
    question_normal = im.fetchall()
    question_normal = random.sample(question_normal, 3)

    im.execute("""SELECT * FROM questions WHERE difficulty = "3" """)
    question_hard = im.fetchall()
    question_hard = random.sample(question_hard, 3)

    questions = question_easy + question_normal + question_hard # Her bir zorluk derecesinden listeleri birleştir


class Announcer(): # Yarışma sunucusu sınıfı
  name = ""

  def __init__(self):
    self.name = "Özgür"

  def ask_question(self, arg1, arg2, arg3):
    print(arg1, arg2, arg3) # Soruyu göster

  def say_thanks(self):
    print("Tebrikler doğru cevap, toplam ödülünüz:", yarışmacı.level_money_price[yarışmacı.level])

  def say_good_bye(self):
    print("Yanlış Cevap! Yarışma bitti.")
    self.finish_programme()

  def finish_programme(self):
    sys.exit(0)


class Competitor(): # Yarışmacı
  name = ""
  level = 0 # Bu örnek niteliğine döndürülebilir mi?
  level_money_price = [0, 150, 500, 1000, 3000, 5000, 10000, 25000, 50000, 100000, 500000]

  def __init__(self):
    self.name = input("Lütfen adınızı giriniz: ")

  def answer_question(self):
    return input("Lütfen doğru şıkkı giriniz:").upper()

  def level_up(self):
    self.level += 1

  def level_control(self):
    if self.level == 15: # 5 soruyu da bilirse büyük ödülü kazanır
      print("Büyük ödülü kazandınız")
      sunucu.finish_programme()


sunucu = Announcer()
yarışmacı = Competitor()
sorular = Question()

# Burada soruları sıralayıp temiz bir liste yapıp for i in şeklinde kodu çalıştırsak çok süper olur. Tüm iş burada bitmiş sayılır o zaman :)

for soru, cevap, zorluk in sorular.questions:
  sunucu.ask_question(soru, cevap, zorluk) # Soru sor
  if yarışmacı.answer_question() == cevap: # Verilen cevap doğru şık ile aynı mı
    yarışmacı.level_up()
    yarışmacı.level_control()
    sunucu.say_thanks()
  else:
    sunucu.say_good_bye()
