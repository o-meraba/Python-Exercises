# -*- coding: utf-8 -*-

def mukemmel_sayi_kontrol():
    #number=int(input('Please enter the number for check:')) #for check from input number
    #if(number>0):
      for number in range(1,10000):
        sum=0
        carpanlar=list()
	for i in range(1,number):
          if((number%i)==0):
	    carpanlar.append(i)
        for j in carpanlar:
	  sum+=j
        if(sum==number):
	  print("{} sayisi bir mukemmel sayidir.".format(number))
          print(carpanlar)

	#else:
	 # print("{} sayisi bir mukemmel sayi degildir.".format(number))
  
	
    
mukemmel_sayi_kontrol()
