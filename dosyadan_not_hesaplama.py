#-*- coding=utf-8 -*-


def harf_notu_hesaplama(result):
    if(result>=90):
      harf_notu='AA'
    elif(result>=85):
      harf_notu='BA'
    elif(result>=80):
      harf_notu='BB'
    elif(result>=75):
      harf_notu='CB'
    elif(result>=70):
      harf_notu='CC'
    elif(result>=65):
      harf_notu='DC'
    elif(result>=60):
      harf_notu='DD'
    elif(result>=55):
      harf_notu='FD'
    elif(result<55):
      harf_notu='FF'
    else:
      pass
    return harf_notu


def dosyadan_not_okuma():
   with open('not_listesi.txt','r+',encoding='utf-8') as file:
    isim_not_listesi=file.readlines()
    yeni_liste=list()

   for ogrenci in isim_not_listesi:
      ogrenci_not_listesi=ogrenci.split(',')
      ogrenci_ad_soyad=ogrenci_not_listesi[0]
      vize1=int(ogrenci_not_listesi[1])
      vize2=int(ogrenci_not_listesi[2])
      final=int(ogrenci_not_listesi[3])
      ortalama=int(vize1*0.3 + vize2*0.3 + final*0.4)
      harf_notu=harf_notu_hesaplama(ortalama)
      yeni_liste.append(ogrenci_ad_soyad+'>>>>>>>>>>>>> :'+ harf_notu + '\n')
   with open('yeni_not_listesi.txt','w',encoding='utf-8') as file2:
      file2.writelines(yeni_liste)
   with open('yeni_not_listesi.txt','r+',encoding='utf-8') as result_file:
      print(result_file.read())


def main():

     dosyadan_not_okuma()



main()
