#-*- coding: utf-8 -*-

from kutuphane import *

def main():
  print("""***************************
**Kütüphane Programına Hoşgeldiniz**

Işlemler:

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Güncelle

Çıkmak için 'q' ya basın.

**********************************""")

  kutuphane = Kutuphane()

  while True:
    try:
        islem= input("Işlem numarası giriniz:")
        if(str(islem).lower() == "q"):
            print("Program Sonlandırılıyor...")
            break

        elif(int(islem) == 1):
            kutuphane.kitaplari_goster()

        elif(int(islem) == 2):
            isim = input("Sorgulamak istediğiniz kitap adı giriniz: ")
            print("Kitap sorgulanıyor....")
            time.sleep(2)
            kutuphane.kitap_sorgula(isim)

        elif(int(islem) == 3): # To add new book
            isim = input("Kitap ismi giriniz: ")
            yazar = input("Yazar giriniz: ")
            yayinevi = input("Yayınevi giriniz: ")
             tur = input("Tür giriniz: ")
            baski = int(input("Baskı giriniz: "))
            sayfa_sayisi = int(input("Sayfa sayısı giriniz: "))
            kitap_fiyati = int(input("Kitap fiyatini giriniz: "))
            yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski, sayfa_sayisi, kitap_fiyati)
            print("Kitap ekleniyor...")
            time.sleep(2)
            kutuphane.kitap_ekle(yeni_kitap)
            print("Kitap eklendi.")

        elif(int(islem) == 4):
            isim = input("Hangi kitabi silmek istiyorsunuz: ")
            if(kutuphane.kitap_sil(isim) == False):
                print("Silmek istediğiniz kitap bulunamadı. Tekrar deneyiniz..")
            else:
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

    except ValueError:
           print("Gecersiz islem.. Tekrar giriniz..")
           continue
#test
main()
