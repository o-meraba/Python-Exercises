#-*- coding:utf-8 -*-


def futbolcu_ayirma():
    gs_liste=list()
    fb_liste=list()
    bjk_liste=list()
    with open("futbolcular.txt","r+",encoding='utf-8') as file:
         futbolcu_listesi=file.readlines()
         for futbolcu in futbolcu_listesi:
             futbolcu_bilgisi=futbolcu.split(",")
             futbolcu_adi=futbolcu_bilgisi[0]
             futbolcu_takimi=futbolcu_bilgisi[1].rstrip()
             print(futbolcu_bilgisi)
             if(futbolcu_takimi == "FB"):
               fb_liste.append(futbolcu + "\n") 
             elif(futbolcu_takimi == "GS"): 
               gs_liste.append(futbolcu + "\n") 
             elif(futbolcu_takimi == "BJK"): 
               bjk_liste.append(futbolcu + "\n") 
    with open("fb_listesi.txt","w",encoding='utf-8') as fb_file:
         fb_file.writelines(fb_liste)
    with open("gs_listesi.txt","w",encoding="utf-8") as gs_file:
         gs_file.writelines(gs_liste)
    with open("bjk_listesi.txt","w",encoding="utf-8") as bjk_file:
         bjk_file.writelines(bjk_liste)

def main():
    futbolcu_ayirma()

main()
