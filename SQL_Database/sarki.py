#-*- encoding: utf-8 -*-

import sqlite3
import time


class Sarki():
      
    def __init__(self, sarki_id, sarki_ismi, sanatci_adi_soyadi, album_adi, produksiyon_sirketi, sarki_suresi, sarki_cikis_yili):
     
      	self.sarki_id = sarki_id
      	self.sarki_ismi = sarki_ismi
      	self.sanatci_adi_soyadi = sanatci_adi_soyadi
      	self.album_adi = album_adi
      	self.produksiyon_sirketi = produksiyon_sirketi
      	self.sarki_suresi = sarki_suresi
      	self.sarki_cikis_yili = sarki_cikis_yili
      	
    def __str__(self):
    	
    	return "Sarkı Id: {}\nŞarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon: {}\nŞarkı Süresi: {}\nŞarkı Çıkış yılı {}\n".format(self.sarki_id, self.sarki_ismi, self.sanatci_adi_soyadi, self.album_adi, self.produksiyon_sirketi, self.sarki_suresi, self.sarki_cikis_yili)
    
class SarkiKayit():
      
    def __init__(self, sarki_ismi, sanatci_adi_soyadi, album_adi, produksiyon_sirketi, sarki_suresi, sarki_cikis_yili):
    
      	self.sarki_ismi = sarki_ismi
      	self.sanatci_adi_soyadi = sanatci_adi_soyadi
      	self.album_adi = album_adi
      	self.produksiyon_sirketi = produksiyon_sirketi
      	self.sarki_suresi = sarki_suresi
      	self.sarki_cikis_yili = sarki_cikis_yili
      	
    def __str__(self):
    	
    	return "Şarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon: {}\nŞarkı Süresi: {}\nŞarkı Çıkış yılı {}\n".format(self.sarki_ismi, self.sanatci_adi_soyadi, self.album_adi, self.produksiyon_sirketi, self.sarki_suresi, self.sarki_cikis_yili)
    


class SarkiUygulamasi():

	def __init__(self):
		self.baglanti_olustur()

	def baglanti_olustur(self):
		self.baglanti = sqlite3.connect('sarki_database.db')
		self.cursor = self.baglanti.cursor()
		sarki_tablo_olusturma_sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (sarki_id INTEGER PRIMARY KEY, sarki_ismi TEXT, sanatci_adi_soyadi TEXT, album_adi TEXT, produksiyon_sirketi TEXT, sarki_suresi INT, sarki_cikis_yili INT)"
		favoriler_tablo_olusturma_sorgu = "CREATE TABLE IF NOT EXISTS favoriSarkilar (favori_id INTEGER PRIMARY KEY, sarki_id INTEGER)"
		self.cursor.execute(sarki_tablo_olusturma_sorgu)
		self.cursor.execute(favoriler_tablo_olusturma_sorgu)
		self.baglanti.commit()

	def baglanti_kes(self):
		self.baglanti.close()

	def sarkilari_listele(self):
		sorgu = "Select * from sarkilar"
		self.cursor.execute(sorgu)
		sarkilar = self.cursor.fetchall()
		if(len(sarkilar) == 0):
			print("Şarkı yok")
		else:
			print(sarkilar[0])
			for  i in sarkilar:
				sarki = Sarki(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
				print("****************")
				print(sarki)

	def sarki_ara(self,isim):
		sorgu = "Select * from sarkilar where sarki_ismi = ?"
		self.cursor.execute(sorgu,(isim, ))
		sarkilar = self.cursor.fetchall()
		if(len(sarkilar) == 0):
			print("Bu isimde bir şarkı bulunmuyor.")

		else:
			sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4], sarkilar[0][5], sarkilar[0][6])
			print(sarki)		

	def sarki_ekle(self, sarki):
		sorgu = "INSERT INTO sarkilar(sarki_ismi, sanatci_adi_soyadi, album_adi, produksiyon_sirketi, sarki_suresi, sarki_cikis_yili) VALUES(?, ?, ?, ?, ?, ?)"
		self.cursor.execute(sorgu, (sarki.sarki_ismi, sarki.sanatci_adi_soyadi, sarki.album_adi, sarki.produksiyon_sirketi, sarki.sarki_suresi, sarki.sarki_cikis_yili))
		self.baglanti.commit()

	def sarki_sil(self, sarki_ismi):
		kontrol_sorgu = "SELECT * FROM sarkilar WHERE sarki_ismi = ?"
		self.cursor.execute(kontrol_sorgu, (sarki_ismi,))
		sarkilar = self.cursor.fetchall()
		if(len(sarkilar) == 0):
			return False

		else:
			sorgu = "DELETE FROM sarkilar WHERE sarki_ismi = ?"
			self.cursor.execute(sorgu,(sarki_ismi, ))
			self.baglanti.commit()
			return True

	def favorilere_ekle(self, sarki_ismi):
		kontrol_sorgu = "SELECT * FROM sarkilar WHERE sarki_ismi = ?"
		self.cursor.execute(kontrol_sorgu, (sarki_ismi,))
		sarki_bilgileri = self.cursor.fetchall()

		if(len(sarki_bilgileri) == 0):
			return False

		else:
			sarki_id = sarki_bilgileri[0][0]
			sarki_kontrol_sorgu = 'SELECT * FROM favoriSarkilar WHERE sarki_id = ?'
			self.cursor.execute(sarki_kontrol_sorgu, (sarki_id, ))
			result = self.cursor.fetchall()

			if(result == []):
				favorilere_ekle_sorgu = "INSERT INTO favoriSarkilar (sarki_id) VALUES( ? )"
				self.cursor.execute(favorilere_ekle_sorgu,(sarki_id,))
				self.baglanti.commit()
				return True

			else:
				return "Sarki_eklidir"			
		
	def favorilerden_sil(self, sarki_ismi):
		kontrol_sorgu = "SELECT sarki_id FROM sarkilar WHERE sarki_ismi = ?"
		self.cursor.execute(kontrol_sorgu,(sarki_ismi,))
		sarki_id = self.cursor.fetchall()

		if (len(sarki_id) == 0):
			return False
		else:
			
		
	def toplam_sarki_suresi():
		pass

	def rastgele_sarki_sec():
		pass

	def karisik_liste_yap():
		pass
