#-*- coding: utf-8 -*-

def aliquot_find(number):
    aliquot_liste=list()
    for i in range(2,number+1):
          if(number%i==0):
             aliquot_liste.append(i)
    return aliquot_liste


def asal_sayi(number): 
      for i in range(1,number+1):
        if(number%i==0):
           continue


def ebob(number1,number2):
    liste_number1=aliquot_find(number1)
    liste_number2=aliquot_find(number2)
    ebob_number=1
    for i in liste_number1:
      for j in liste_number2:
           if(i==j and ebob_number<i):
              ebob_number=i
    return ebob_number


def ekok(number1,number2):
   

def main():
    print('*'*30)
    option=int(input('Please enter 1 for EBOB or 2 for EKOK'))
    number1=int(input('Please enter first number:'))
    number2=int(input('Please enter second number:'))

    if(option==1):
      print('EBOB:',ebob(number1,number2))
    if(option==2):
      #print('EKOK:',ekok(number1,number2))
      ekok(number1,number2)
      
main()
