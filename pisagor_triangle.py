#-*- coding: utf-8 -*-

def find_pisagor_triangle():
     list_pisagor=list()
     for i in range(1,101):
       for j in range(1,101):
         c = ((i**2)+(j**2))**0.5
         if(c==int(c)):
           list_pisagor.append((i,j,int(c)))
     return list_pisagor


def main():
   print( find_pisagor_triangle())


main()
