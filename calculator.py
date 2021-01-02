#Hesap Makinesi
"""print('*'*30)
i=0
for i in range(10):
	print('*'+' '*28 +'*')
	i+=1
print('*'*30)
"""

print(""" 
Welcome to Calculator Program
1. Plus
2. Minus
3. Divided By
4. Multiply
""")
first_number=int(input('Please input an integer first number:'))
second_number=int(input('Please input an integer second number :'))
option=int(input('Please choose an option(1-4):'))

if(option==1):
   print("Result is:{}".format(first_number+second_number))
elif(option==2):
   print("Result is:{}".format(first_number-second_number))
elif(option==3):
   print("Result is:{}".format(first_number//second_number))
elif(option==4):
   print("Result is:{}".format(first_number*second_number))
else:
   print("There isn't option that you chose. Run again...")
