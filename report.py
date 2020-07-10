
from lambdastu import Lambdastudents, DataSci
import random

name = ['Noah', 'Rob', 'J', 'Sasana', 'Dave']
age = [26, 37, 30, 23, 31]
cohort_number = [16, 16, 16, 16, 16]
previous_job = ['Fintech Guru', 'Cook',  'Mailmain', 'Shoplify Store Owner', 'Cool Hippie']
reportlist = []
print('+++++++++++++++++++++++++++++++')
print('Here is a report of a student.')
print('+++++++++++++++++++++++++++++++')
for i in range(len(name)):
  user = Lambdastudents(name[i], age[i], cohort_number[i], previous_job[i])
  reportlist.append(user)
 
for k in range(len(name)):
  print(reportlist[k].info())
  print('______')
r = random.randint(0, len(reportlist)-1)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(f'HERE IS A RANDOM STUDENT {reportlist[r].info()}')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#print(f'HERE IS A RANDOM STUDENT {reportlist[r].name}, {reportlist[r].age}, {reportlist[r].cohort_number}, {reportlist[r].previous_job}')




