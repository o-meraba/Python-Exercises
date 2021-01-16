#-*- coding: utf-8 -*-

def prime_number_check(number):
           for i in range(2,int(number)):
              if(number%i==0):
                return False
           return True


def main():
  while(1):
        number=input('Enter a number for checking(q for quit):')
        check=0
        if(number=='q'):
          break
        if(prime_number_check(int(number)) and not int(number)==1):
          print('{} is a prime number'.format(number))
        else:
          print('{} is NOT a prime number'.format(number))


main()
