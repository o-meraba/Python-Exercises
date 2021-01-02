#Kullanıcıdan aldığınız boy ve kilo değerlerine göre 
#kullanıcının beden kitle indeksini bulun.
#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

weight=float(input('Enter your weight(k):'))
length=float(input('Enter your length(m):'))

print('Your weight(k):{0}, Your length(m):{1} and Your body index:{2}'.format(weight,length,weight/(length*length)))
