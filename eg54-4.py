#-*- coding: utf-8 -*-

def number_to_string(number):
    birler_basamagi=int(number)%10
    onlar_basamagi=int(number)/10
    if(birler_basamagi==0):
      birler_basamagi_string=' '

    if(birler_basamagi==1):
      birler_basamagi_string='bir'

    if(birler_basamagi==2):
      birler_basamagi_string='iki'

    if(birler_basamagi==3):
      birler_basamagi_string='üc'

    if(birler_basamagi==4):
      birler_basamagi_string='dort'

    if(birler_basamagi==5):
      birler_basamagi_string='bes'

    if(birler_basamagi==6):
      birler_basamagi_string='alti'

    if(birler_basamagi==7):
      birler_basamagi_string='yedi'

    if(birler_basamagi==8):
      birler_basamagi_string='sekiz'

    if(birler_basamagi==9):
      birler_basamagi_string='dokuz'

    if(onlar_basamagi==1):
       onlar_basamagi_string='on'

    if(onlar_basamagi==2):
       onlar_basamagi_string='yirmi'

    if(onlar_basamagi==3):
       onlar_basamagi_string='otuz'

    if(onlar_basamagi==4):
       onlar_basamagi_string='kirk'

    if(onlar_basamagi==5):
       onlar_basamagi_string='elli'

    if(onlar_basamagi==6):
       onlar_basamagi_string='altmis'

    if(onlar_basamagi==7):
       onlar_basamagi_string='yetmis'

    if(onlar_basamagi==8):
       onlar_basamagi_string='seksen'

    if(onlar_basamagi==9):
       onlar_basamagi_string='doksan'

    result=onlar_basamagi_string + ' ' +birler_basamagi_string
    return result


def main():
    number=int(input('Iki basamakli bi sayi giriniz:'))
    print(number_to_string(number))

main()
