# -*- coding: utf-8 -*-

def cift_kontrol(sayi):
    if(sayi%2 == 0):
      return sayi
    else:
       raise ValueError

     


def main():
    #value = int(input('Sayi giriniz:'))
    liste=[32,2,1,4,7,12,35,91,42]
    for i in liste:
       try:
        print(cift_kontrol(i))
       except ValueError:
         pass
main()
