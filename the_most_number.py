# -*- coding: utf-8-*-

first_number=float(input('Enter first number:'))
second_number=float(input('Enter second number:'))
third_number=float(input('Enter third number:'))

the_biggest_number=first_number
if(the_biggest_number<second_number):
  the_biggest_number=second_number
if(the_biggest_number<third_number):
  the_biggest_number=third_number

print("The biggest number:",the_biggest_number)
