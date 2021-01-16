#Created Date:16-01-2021
#Author: OmerAba
#There are four level for random multiply questions
#You can choose your level from 1 to 4 /Level1-->(1-25) Level2-->(25-50) Level3-->(50-75) Level4-->(75-100)

import random # To import random module


# To generate randoms with entered option and return result multiply of two number
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
   
   carp=lambda x,y : x*y # To multiply two number using LAMBDA
   print("{} x {} : ".format(a,b))
   
   return carp(a,b)



def main():

 
 while(1):  # For infinite loop

   try: # To catch errors
     # Print options
     print("""1) Basic (1 - 25) 
            \n2) Beginner (25 - 50)
            \n3) Intermadiate (50 - 75)
            \n4) Advance (75 - 100) 
           """)
   
     option = int(input("Please enter your option (9 for quit):"))  # Enter Option

     if(option == 9): # To check option for quit from program
        print("\n***Good Bye, See you soon again..***\n")
        break
     elif(option == 1 or option == 2 or option == 3 or option == 4):      
        result=generate_randoms(option) # To get result from generate_randoms function with entered option
     else:
       print('***************************')
       print("WRONG OPTION, please enter your option again..")
       print('***************************')
       continue
     answer=int(input('Enter your answer:\n')) # To request an answer for question
   
     if(answer== result):  # To check answer
       print('***************************')
       print('      Congrats...')
       print('***************************')
    
     else:
       print('***************************')
       print(" Your answer isn't correct.")
       print(" Correct answer is {}.".format(result))

   except SyntaxError: # To catch SyntaxError
       print('***************************')
       print("WRONG INPUT, please enter input again...")     
       print('***************************')
       continue      

   except NameError: # To catch NameError 
       print('***************************')
       print("WRONG INPUT, please enter input again...")     
       print('***************************')
       continue     


main() # To execute Main Function
