#-*- coding: utf-8 -*-
def aliquot_find(number):
    aliquots=list()
    for i in range(1,number):
        if(number%(i)==0):
          aliquots.append(i)
    return aliquots


    

def perfect_number_find():
    perfect_numbers_list=list()
    for i in range(1,10000):
      sum=0
      for j in aliquot_find(i):
         sum+=j
      if(sum==i):
         perfect_numbers_list.append(i)

    return perfect_numbers_list



def main():
    print(perfect_number_find())



main()
