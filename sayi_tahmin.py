#-*- coding: utf-8 -*-
import random

def sayi_tahmin(random_sayi):
    print(random_sayi)
    score=10
    while(score>0):   
     guess_number=int(input("Please enter your guess number:"))
     if(guess_number<random_sayi):
       print('Enter bigger number')
       score-=1
       print('Last trying count:',score)
       continue
     if(guess_number>random_sayi):
       print('Enter smaller number')
       score-=1
       print('Last trying count:',score)
       continue
     if(guess_number==random_sayi):
       print('Congrulations... Your score is ',score*10)
       break
    if(score<1):
       print('You are lost') 

def main():
    random_number=int(random.randrange(1,100))
    sayi_tahmin(random_number)


main()
