import sqlite3
import time

class Kitap():

      def __init__(self, isim, yazar, yayinevi, tur, baski, sayfa_sayisi, kitap_fiyati):
         
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
        self.sayfa_sayisi = sayfa_sayisi
        self.kitap_fiyati = kitap_fiyati

      def __str__(self):
        
        return "Kitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\nSayfa Sayısı: {}".format(self.isim, self.yazar, self.yayinevi, self.tur, self.baski, self.sayfa_sayisi, self.kitap_fiyati)


class Kutuphane():

      def __init__(self):
          self.baglanti_olustur()
         

      def baglanti_olustur(self):
          self.baglanti = sqlite3.connect("kutuphane.db")
          self.cursor = self.baglanti.cursor()
          sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT, yazar TEXT, yayinevi TEXT, tur TEXT, baski INT, sayfa_sayisi INT, kitap_fiyati INT)"
          self.cursor.execute(sorgu)
          self.baglanti.commit()

      def baglanti_kes(self):
          self.baglanti.close()

      def kitaplari_goster(self):
          sorgu = "Select * from kitaplar"
          self.cursor.execute(sorgu)
          kitaplar = self.cursor.fetchall()
          if(len(kitaplar) == 0):
             print("Kütüphanede kitap bulunmuyor...")
             
          else:
             for i in kitaplar:
                  kitap = Kitap(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                  print("************************")
                  print(kitap) 
                                   
      def kitap_sorgula(self,isim):
          sorgu = "Select * from kitaplar where isim = ?"
          self.cursor.execute(sorgu,(isim,))
          kitaplar = self.cursor.fetchall()
          if(len(kitaplar) == 0):
             print("Bu isimde bir kitap bulunmuyor..")
          else:
             kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4], kitaplar[0][5], kitaplar[0][6])
             print(kitap)

      def kitap_ekle(self,kitap):
          sorgu = "INSERT INTO kitaplar VALUES(?, ?, ?, ?, ?, ?, ?)"
          self.cursor.execute(sorgu,(kitap.isim, kitap.yazar, kitap.yayinevi, kitap.tur, kitap.baski, kitap.sayfa_sayisi, kitap.kitap_fiyati))
          self.baglanti.commit()

      def kitap_sil(self,isim):
          kontrol_sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
          self.cursor.execute(kontrol_sorgu, (isim,))
          kitaplar = self.cursor.fetchall()
          if(len(kitaplar) == 0):
               return False
          else:
               
               sorgu = "DELETE FROM kitaplar WHERE isim = ?"
               self.cursor.execute(sorgu,(isim,))
               self.baglanti.commit()
               return True

      def baski_yukselt(self,isim):
          sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
          self.cursor.execute(sorgu,(isim,))
          kitaplar = self.cursor.fetchall()
          if(len(kitaplar) == 0):
             print("Boyle bir kitap bulunmuyor...")
          else:
             baski = kitaplar[0][4]
             baski += 1
             sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
             self.cursor.execute(sorgu2,(baski,isim))
             self.baglanti.commit()
  
