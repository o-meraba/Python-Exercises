#-*- coding: utf-8 -*-


def carpim_tablosu():
    for i in range(1,11):
	for j in range(1,11):
	  print("{}x{}={}".format(i,j,i*j))
	print("*"*5)


carpim_tablosu()
