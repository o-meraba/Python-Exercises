#-*- coding: utf-8 -*-

"""file = open('bilgiler.txt','w') #eski bilgileri silip yeniden olusturur
file.write("Ömer Aba")
file= open('bilgiler.txt','a') #imlec sonuna ekler
file.write('Omer ABA\n')
"""

"""try:
  file=open('bilgiler.txt','r')
  for i in file:
      print(i,end = '')
  file.close()
except IOError:
  print('Dosya Bulunamadi..')
"""

"""file = open("bilgiler.txt",'r',encoding='utf-8')
icerik = file.read()
print('1.Okuma: Dosya icerigi:\n',icerik,sep="")

icerik2 = file.read()
print("2.Okuma: Dosya Icerigi:\n",icerik2,sep="")

file.close()
"""

'''file = open('bilgiler.txt','r',encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
'''


"""file = open('bilgiler.txt','r',encoding='utf-8')
print(file.readlines())
file.close()
"""

'''with open('bilgiler.txt','r') as file:
     print(file.readlines())
'''

'''with open('bilgiler.txt','r',encoding='utf-8') as file:
     file.seek(20)
     print(file.tell())
     #print(file.readline())
     print(file.read(10))
     print(file.tell())
'''
"""with open('bilgiler.txt','r+',encoding='utf-8') as file:
     print(file.read())
     file.seek(10)
     file.write("DENEME")
     print('*'*30)
     file.seek(0)
     print(file.read())
"""

"""with open('bilgiler.txt','a',encoding='utf-8') as file:
     file.write("Omer ABA\n")

with open('bilgiler.txt','r',encoding="utf-8") as file:
     print(file.read())
"""

"""with open("bilgiler.txt","r+",encoding="utf-8") as file:
    icerik = file.read()
    icerik = 'MERHABALAR\n' + icerik
    file.seek(0)
    file.write(icerik)

with open('bilgiler.txt','r+',encoding='utf-8') as file:
     print(file.read())
"""

'''with open('bilgiler.txt','r+',encoding='utf-8') as file:
     liste = file.readlines()
     liste.insert(3,'TAM DA ORTASI\n')
     file.seek(0)
     for satir in liste:
       file.write(satir)
with open("bilgiler.txt",'r+',encoding='utf-8') as file:
     print(file.read())
'''
     

with open('bilgiler.txt','r+',encoding='utf-8') as file:
     liste = file.readlines()
     liste.insert(3,'TAM DA ORTASI\n')
     file.seek(0)
     file.writelines(liste)

with open("bilgiler.txt",'r+',encoding='utf-8') as file:
     print(file.read())


