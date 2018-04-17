import time
import random

class Kumanda():
    def __init__(self, tv_durumu="Kapalı", ses_seviyesi=0, kanal_listesi=["atv ","show"], aktif_kanal="atv"):
        self.tv_durumu=tv_durumu
        self.ses_seviyesi=ses_seviyesi
        self.kanal_listesi=kanal_listesi
        self.aktif_kanal=aktif_kanal

    def tv_ac(self):
        if(self.tv_durumu=="Açık"):
            print("Tv zaten açık")
        else:
            self.tv_durumu="Açık"
            print("Tv Açıldı.")
    def tv_kapat(self):
        if(self.tv_durumu=="Kapalı"):
            print("Tv zaten kapalı")
        else:
            self.tv_durumu=="Açık"
            print("Tv Kapatıldı.")
    def ses_ayarları(self):
        while True:
            cevap = input("sesi azalt:'<'\nSesi arttır:'>'\nÇıkış:'çıkış'")
            if(cevap == "<"):
                if(self.ses_seviyesi != 0):
                    self.ses_seviyesi -=1
                    print(self.ses_seviyesi)
            elif(cevap == '>'):
                if(self.ses_seviyesi != 32):
                    self.ses_seviyesi+=1
                    print(self.ses_seviyesi)
            else:
                print("Ses güncellendi:",self.ses_seviyesi)
                break



    def kanal_ekle(self,yeni_kanal):

        self.kanal_listesi.add(yeni_kanal)
        print("Yeni kanal ekleniyor...")
        time.sleep(2)
        print("Yeni kanal eklendi.")

    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.aktif_kanal = self.kanal_listesi[rastgele]
        print("Şuanki kanal:",self.aktif_kanal)

    def __len__(self):
       return len(self.kanal_listesi)


    def __str__(self):
        return "Tv Durumu:{}\nTv Ses Seviyesi:{}\nKanal Listesi:{}\nSuanki Kanal:{}".format(self.tv_durumu,self.ses_seviyesi,self.kanal_listesi,self.aktif_kanal)

kumanda = Kumanda()

print("""

Tv Uygulaması

1. Tv Aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Sayısını Öğrenme

6.Rastgele Kanala Geçme

7.TV Bilgileri Öğrenme

Çıkmak için 'q' tuşuna basınız..
""")


while True:
    islem = input("İşlemi Seciniz:")
    if(islem=='q'):
        print("Programdan çıkış yapılıyor...")
        break
    elif(islem=="1"):
        kumanda.tv_ac()
    elif(islem=="2"):
        kumanda.tv_kapat()
    elif(islem=="3"):
        kumanda.ses_ayarları()
    elif(islem=="4"):
        yeni_kanal=input("yeni kanal ismi giriniz:")
        kumanda.kanal_ekle(yeni_kanal)
    elif(islem=="5"):
        print("Kanal sayısı:",kumanda.__len__())
    elif(islem=="6"):
        kumanda.rastgele_kanal()
    elif(islem=="7"):
        print(kumanda)
    else:
        print("Yanlış girdiniz.. Tekrar Deneyiniz..")

