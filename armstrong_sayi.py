#-*- coding: utf-8 -*-

def armstrong_sayi_bul():
    number1=int(input('Please enter a number:'))
    number2=number1    
    rakamlar=list()
    sum=0
    while(number1>0):
	   rakamlar.append(number1%10)
	   number1=number1//10
    rakamlar.reverse()
    print(rakamlar)

    for i in rakamlar:
	sum+=(i**len(rakamlar))
    if(sum==number2):
	print("Sayi armstrong sayidir.")
    else:
        print('Sayi armstrong degildir')

armstrong_sayi_bul()
