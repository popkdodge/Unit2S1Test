#!/usr/bin/env python



class Lambdastudents:
  def __init__(self, name, age, cohort_number, previous_job):
    self.name = name
    self.age = age
    self.cohort_number = cohort_number
    self.previous_job = previous_job
  def code(self):
    return print('Yes, I can code.')
  def info(self):
    return f'{self.name}, {self.age}, {self.cohort_number}, {self.previous_job}'

class DataSci(Lambdastudents):
  def __init__(self, name, age, cohort_number, previous_job):
    super().__init__(name, age, cohort_number, previous_job)

  def make_prediction(self):
    return "The weather for today is cloudy."

  def code(self):
    return "Yes, I can code: Python and do DS."
  
