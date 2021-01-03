# -*- coding: utf-8 -*-

print('Welcome to ATM - Automated Teller MAchine\n')
print('''Main\n
1.Deposit
2.Withdraw
3.Balance Inquiry
''')

balance=0

while(1):
	option=int(input('Please choose your option(9 for exit):'))

	if(option==9):
	  print("Have a nice day")
	  break
	if(option==1): #deposit option
	  deposit_value=input('Please enter your deposit value:')
	  balance+=deposit_value
	  print('Your deposit have just added your balance.')
	if(option==2): #withdraw option
	  withdraw_value=input('Please enter your withdraw value:')
	  if(balance>=withdraw_value):
	    balance-=withdraw_value
	    print('Your money have just withdrawed.')
	  else:
	    print("There isn't enough money for withdrawing. Please enter again")

	if(option==3): #balance inquiry option
	   print('Your Balance is:{}'.format(balance))

