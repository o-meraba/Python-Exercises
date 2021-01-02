#-*- coding: utf-8 -*-

#Kullanıcıdan aldığınız boy ve kilo değerlerine göre 
#kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

weight=float(input('Enter your weight(k):'))
length=float(input('Enter your length(m-eg(1.72)):'))
index=float(weight/(length*length))
print('Your weight(k):{0}, Your length(m):{1} and Your body index:{2}'.format(weight,length,weight/(length*length)))

if(index<18.5):
  print('Thin')
elif(index>18.5 and index<25):
  print('Normal')
elif(index>25 and index<30):
  print('Over Weight')
elif(index>30):
  print('Obese')
