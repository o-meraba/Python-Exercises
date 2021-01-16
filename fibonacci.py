#*-* coding: utf-8 *-*
i=1

number=int(input('please enter your number:'))
first_number=1
second_number=1
liste=[first_number,second_number]
if(not(number==0 or number==1) and number>=0):
  for i in range(2,number):
	first_number,second_number=second_number,first_number+second_number
	liste.append(second_number)
print(liste)
print(type(liste))
