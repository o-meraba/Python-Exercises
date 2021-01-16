#Created Date:16-01-2021
#Author: OmerAba
#There are four level for random multiply questions
#You can choose your level from 1 to 4 /Level1-->(1-25) Level2-->(25-50) Level3-->(50-75) Level4-->(75-100)

import random



def generate_randoms(option):
   if(option == 1):
    a = random.randint(1, 25)
    b = random.randint(1, 25)

   elif(option == 2): 
     a = random.randint(25, 50)
     b = random.randint(25, 50)

   elif(option == 3):
     a = random.randint(50, 75)
     b = random.randint(50, 75)

   elif(option == 4):
     a = random.randint(75, 100)
     b = random.randint(75, 100)
   
   carp=lambda x,y : x*y 
   print("{} x {} : ".format(a,b))
   
   return carp(a,b)



def main():

  while(1):  # For infinite loop

   # Print options
   print("""1) Basic (1 - 25) 
          \n2) Beginner (25 - 50)
          \n3) Intermadiate (50 - 75)
          \n4) Advance (75 - 100) 
         """)
   
   option = int(input("Please enter your option (9 for quit):"))  # Enter Option

   if(option == 9): # To check option for quit from program
      print("Good Bye, See you soon again..")
      break
   else:      
      result=generate_randoms(option) # To get result from generate_randoms function with entered option

   answer=int(input('Enter your answer:\n')) # To request an answer for question
   
   if(answer== result):  # To check answer
     print('Congrats...\n')
   else:
     print("Your answer isn't correct.\n")
   
main() # To execute Main Function
