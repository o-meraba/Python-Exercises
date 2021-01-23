#-*- encoding: utf-8 -*-

from sarki import *


def main():
    print("""
          ***************Şarkı Programına Hoşgeldiniz**********

İşlemler:

1. Şarkıları Listele

2. Şarkı Ara

3. Şarkı Ekle

4. Şarkı Sil

5. Şarkı Güncelle

6. Favoriler Listesine Şarkı Ekle

7. Favoriler Listesinden Şarkı Kaldır

8. Toplam Şarkı Süresini Göster
          
9. Rastgele Şarkı Seç

10. Karışık Liste Yap

Çıkmak için 'q' ya basınız.
*************************************""")
            
    sarkiUyg = SarkiUygulamasi()

    while True:
          try:
                islem = input("Işlem numarası giriniz:")
                if(str(islem).lower() == "q"):
                    print("Proğram sonlandırılıyor...")
                    break
               
                elif(int(islem) == 1): # Sarkilari listeleme
                    sarkiUyg.sarkilari_listele()     
               
                elif(int(islem) == 2): # Sarki arama
                    isim = input("Aramak istediğiniz şarkı ismi giriniz:")  
                    print("Şarkı Aranıyor...")
                    time.sleep(2)
                    sarkiUyg.sarki_ara(isim)       
               
                elif(int(islem) == 3): # Sarki ekleme
                    sarki_ismi = input("Şarkı ismi giriniz:")
                    sanatci_adi_soyadi = input("Sanatçı adı ve soyadı giriniz:")
                    album_adi = input("Albüm adı giriniz: ")
                    produksiyon_sirketi = input("Prodüksiyon şirketi giriniz: ")
                    sarki_suresi = int(input("Şarkı süresini giriniz (saniye olarak): "))
                    sarki_cikis_yili = input("Şarkı çıkış yılı giriniz: ")
                    yeni_sarki = Sarki(sarki_ismi, sanatci_adi_soyadi, album_adi, produksiyon_sirketi, sarki_suresi, sarki_cikis_yili)
                    print("Kitap ekleniyor...")
                    time.sleep(2)
                    sarkiUyg.sarki_ekle(yeni_sarki)
                    print("Şarkı eklendi.")

                elif(int(islem) == 4): # Sarki Silme
                    sarki_ismi = input("Hangi sarkıyı silmek istiyorsunuz:")
                    if (sarkiUyg.sarki_sil(sarki_ismi) == False):
                         print("Silmek istediğiniz şarkı bulunamadı.")
                    else:
                         cevap = input("Emin misiniz?(E/H):")
                         if(cevap.lower() == "e"):
                              print("Şarkı siliniyor...")
                              time.sleep(2)
                              sarkiUyg.sarki_sil(sarki_ismi)
                              print("Şarkı silindi.")
                         else:
                              print("Silme islemi iptal edildi.")
               
                elif(int(islem) == 5): # Sarki güncelleme
                    #sarki_ismi = input("Güncellenecek şarkı ismini giriniz: ")
                    pass 

                elif(int(islem) == 6): # Favori listesine sarki ekleme
                    pass
               
                elif(int(islem) == 7): # Favori Listesinden sarki kaldirma

                    pass
               
                elif(int(islem) == 8): # Toplam Sarki suresini gosterme
                    pass
               
                elif(int(islem) == 9): # Rastgele bir sarki secme
                    pass
               
                elif(int(islem) == 10): # Karisik bir liste yapma(10)

                    pass

                # ??? Dosyadan sarki bilgilerini DB'ye kaydetme


          except ValueError:
               print("Geçersiz işlem yaptınız. Tekrar seçim yapınız...")
               continue

main()
