#-*- encoding: utf-8 -*-

import sqlite3
import time


class Sarki():
      
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
		sorgu = "CREATE TABLE IF NOT EXISTS sarkilar (sarki_ismi TEXT, sanatci_adi_soyadi TEXT, album_adi TEXT, produksiyon_sirketi TEXT, sarki_suresi INT, sarki_cikis_yili INT)"
		self.cursor.execute(sorgu)
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
			for  i in sarkilar:
				sarki = Sarki(i[0], i[1], i[2], i[3], i[4], i[5])
				print("****************")
				print(sarki)

	def sarki_ara(self,isim):
		sorgu = "Select * from sarkilar where sarki_ismi = ?"
		self.cursor.execute(sorgu,(isim, ))
		sarkilar = self.cursor.fetchall()
		if(len(sarkilar) == 0):
			print("Bu isimde bir şarkı bulunmuyor.")

		else:
			sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3], sarkilar[0][4], sarkilar[0][5])
			print(sarki)		

	def sarki_ekle(self, sarki):
		sorgu = "INSERT INTO sarkilar VALUES(?, ?, ?, ?, ?, ?)"
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

	def sarki_guncelle():
		pass

	def favorilere_ekle():
		pass

	def favorilerden_sil():
		pass

	def toplam_sarki_suresi():
		pass

	def rastgele_sarki_sec():
		pass

	def karisik_liste_yap():
		pass
