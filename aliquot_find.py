def aliquot_find(number):
    aliquots=list()
    for i in range(1,number+1):
     if(number%(i)==0):
          aliquots.append(i)
    return aliquots

def main():
    number=int(input('Enter a number:'))
    print(aliquot_find(number))

main()
