#-*- coding: utf-8 -*-

from kutuphane import *

print("""*************************
Kutuphane Programina Hosgeldiniz

Islemler:

1. Kitaplari Goster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baski Guncelle

Cikmak icin 'q' ya basin.

********************************""")

kutuphane = Kutuphane()

while True:
    islem= input("Islem numarasi giriniz:")
    if(islem == "q"):
       print("Program Sonlandiriliyor")
       break

    elif(int(islem) == 1):
         kutuphane.kitaplari_goster()

    elif(int(islem) == 2):
         isim = input("Sorgulamak istediginiz kitap adi giriniz: ")
         print("Kitap sorgulaniyor....")
         time.sleep(2)
         kutuphane.kitap_sorgula(isim)

    elif(int(islem) == 3):
         isim = input("Kitap ismi giriniz: ")
         yazar = input("Yazar giriniz: ")
         yayinevi = input("Yayinevi giriniz: ")
         tur = input("Tür giriniz: ")
         baski = int(input("Baski giriniz: "))

         yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
         print("Kitap ekleniyor...")
         time.sleep(2)
         kutuphane.kitap_ekle(yeni_kitap)
         print("Kitap eklendi.")

    elif(int(islem) == 4):
         isim = input("Hangi kitabi silmek istiyorsunuz: ")
         cevap = input("Emin  misiniz?(E/H)")
         if(cevap.lower() == "e"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi..")
         else:
           print("Silme islemi iptal edildi.")
         
    elif(int(islem) == 5):
         isim = input("Hangi kitabin baskisini yukseltmek istiyorsunuz: ")
         print("Baski yukseltiliyor...")
         time.sleep(2)
         kutuphane.baski_yukselt(isim)
         print("Baski yükseltildi..")

    else:
       print("Yanlis bir secim yaptiniz.. Tekrar Secim yapiniz..")
