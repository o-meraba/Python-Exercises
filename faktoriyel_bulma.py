#-*- coding: utf-8 *-*

value=int(input("Enter a number for faktorial:"))
result=1

if(value==0 or value==1):
  result=1
if(value>1):
  for i in range(1,value+1):
    result*=i

print("{}! result is {}".format(value,result))
