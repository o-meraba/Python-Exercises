#-*- coding: utf-8 -*-

def toplam_deger():
   sum=0
   while(1):
    value=input('Please enter a value(q for quite):')
    print(type(value))
    if(value=='q'):
      break
    elif(int(value)>0):
      sum+=int(value)
      print("Sum value:",sum)
    else:
      print("Your value isn't a valid value. Please enter a new value. ")


toplam_deger()
