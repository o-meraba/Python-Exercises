# -*- coding: utf-8 -*-


def main():
    liste = ['101','123a','aaa','202','303','aa12','404']
    for i in liste:
        try:
          print(int(i))

        except ValueError:
           pass        
    


main()
