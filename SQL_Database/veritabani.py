import sqlite3 
import time

con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (kitap_ismi TEXT, yazar TEXT, yayinevi TEXT, sayfaSayisi INT )")
    con.commit()

def deger_ekle(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim, yazar, yayinevi, sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("Select * from kitaplik")
    data = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri....")
    for i in data:
        print(i)

def verileri_al_2():
    cursor.execute("Select isim, yazar FROM kitaplik")
    data = cursor.fetchall()
    print('Kitaplik Tablosunun Bilgileri...')
    for i in data:
        print(i)

def verileri_al_3(yayinevi):
    cursor.execute("SELECT * FROM kitaplik WHERE yayinevi=?",(yayinevi,))
    data = cursor.fetchall()
    print("Kitaplik Tablosunun Bilgileri..")
    for i in data:
        print(i)

def yayinevi_guncelle(yayinevi1,yayinevi2):
    cursor.execute("Update kitaplik set yayinevi = ? where Yayinevi = ? ",(yayinevi1, yayinevi2,))
    con.commit()

def veri_sil(yazar_adi):
    cursor.execute("Delete FROM kitaplik where yazar = ?", (yazar_adi,))
    con.commit()
 

def main():

    tablo_olustur()
    print('''**** HOSGELDINIZ **** 
            \n1)Kayit yapma
            \n2)Listeleme
            \n3)Listeleme 2
            \n4)Listeleme 3
            \n5)Yayinevi Guncelle
            \n6)Yazar bilgisiyle sil\n''')
    secim = int(input('Seciminiz:'))
    if(secim == 1):
        kitap_ismi = input("Kitap ismi giriniz: ")
        yazar = input("Yazar ismi giriniz: ")
        yayinevi = input("Yayinevi: ")
        sayfa_sayisi = int(input("Sayfa sayisi giriniz: "))
        deger_ekle(isim, yazar, yayinevi, sayfa_sayisi)
    elif(secim == 2):    
        verileri_al()

    elif(secim == 3):
        verileri_al_2()

    elif(secim == 4):
        yayin_evi = input("Yayin evi giriniz:")
        verileri_al_3(yayin_evi)

    elif(secim == 5):
        yayin_evi1 = input("Yayinevi yeni ismi giriniz:") 
        yayin_evi2 = input("Yayinevi eski ismi giriniz: ")
        yayinevi_guncelle(yayin_evi1,yayin_evi2)
        print('Guncellendi...')

    elif(secim == 6):
        yazar_adi = input("Yazar adi giriniz:")
        veri_sil(yazar_adi)

    con.close()


main()
