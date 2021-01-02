#-*- coding: utf-8 -*-
midterm_exam_mark_first=int(input("Please Enter Your Midterm Exam Mark First:"))
midterm_exam_mark_second=int(input("Please Enter Your Midterm Exam Mark Second:"))
final_exam_mark=int(input("Please Enter Your Final Exam Mark:"))

result=(midterm_exam_mark_first*30 + midterm_exam_mark_second*30 + final_exam_mark*40)/100
print("Your result is:{}\n".format(result))
if(result>=90):
  print('AA')
elif(result>=85):
  print('BA')
elif(result>=80):
  print('BB')
elif(result>=75):
  print('CB')
elif(result>=70):
  print('CC')
elif(result>=65):
  print('DC')
elif(result>=60):
  print('DD')
elif(result>=55):
  print('FD')
elif(result<55):
  print('FF')
