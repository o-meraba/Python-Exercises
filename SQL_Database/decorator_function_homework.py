

def mukemmel_sayi(func):
	def wrapper():
		mukemmel_sayilar = []
		for number in range(1,1000):
			tam_bolenler_toplami = 0
			for i in range(1,number):
				if(number % i == 0):
					tam_bolenler_toplami += i
			if(number == tam_bolenler_toplami):
				mukemmel_sayilar.append(number)
		print(mukemmel_sayilar)
		func()

	return wrapper




@mukemmel_sayi
def asal_sayi_yazdir():
	asal_sayilar = []	
	for number in range(2,1000):
		value = True
		for i in range(2,number):	
			if(i != number):
				if( number % i == 0):
					value = False

		if(value == True):
			asal_sayilar.append(number)
	print("******ASAL SAYILAR******")
	print(asal_sayilar)


asal_sayi_yazdir()


