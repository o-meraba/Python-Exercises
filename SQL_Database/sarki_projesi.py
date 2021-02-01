#-*- encoding: utf-8 -*-

from sarki import *


# def favorilere_ekle(isim):
#  return isim
  

def main():
    print("""
          ***************Şarkı Programına Hoşgeldiniz**********

İşlemler:

1. Şarkıları Listele

2. Şarkı Ara

3. Şarkı Ekle

4. Şarkı Sil

5. Favoriler Listesine Şarkı Ekle

6. Favoriler Listesinden Şarkı Kaldır

7. Toplam Şarkı Süresini Göster
          
8. Rastgele Şarkı Seç

9. Karışık Liste Yap

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
                    yeni_sarki = SarkiKayit(sarki_ismi, sanatci_adi_soyadi, album_adi, produksiyon_sirketi, sarki_suresi, sarki_cikis_yili)
                    print("Şarkı ekleniyor...")
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
              
                     

                elif(int(islem) == 5): # Favori listesine sarki ekleme
                    sarki_ismi = input("Favori listenize eklemek istediğiniz şarkıyı yazın: ")
                    result = sarkiUyg.favorilere_ekle(sarki_ismi)

                    if(result == True):
                      print('Sarki Eklendi.')

                    elif(result == "Sarki_eklidir"):
                      print("Şarkı favorilere eklidir.")

                    else:
                      print("Eklemek istediğiniz şarkı bulunamadı.")
                      
               
                elif(int(islem) == 6): # Favori Listesinden sarki kaldirma
                    favorilerden_sil("Hello")
                    pass
               
                elif(int(islem) == 7): # Toplam Sarki suresini gosterme
                    pass
               
                elif(int(islem) == 8): # Rastgele bir sarki secme
                    pass
               
                elif(int(islem) == 9): # Karisik bir liste yapma(10)

                    pass

                # ??? Dosyadan sarki bilgilerini DB'ye kaydetme


          except ValueError:
               print("Geçersiz işlem yaptınız. Tekrar seçim yapınız...")
               continue
          except NameError:
                raise

main()
