#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: neutron
"""
import datetime


currentDate = datetime.date.today()
currentYear = currentDate.year
currentMonth = currentDate.month
currentDay = currentDate.day

myBirthday = datetime.datetime.strptime("2/30/1996","%m/%d/%Y").date()
birthMonth = myBirthday.month
birthYear = myBirthday.year
birthDay = myBirthday.day

expectedAge = 30

deathYear = birthYear + expectedAge

yearLeft = deathYear - currentYear

#print("You have "+ str(yearLeft)+ " years left of your life.")

deathDateString = str(birthMonth) + "/" + str(birthDay) + "/" + str(deathYear)
deathDate = datetime.datetime.strptime(deathDateString,"%m/%d/%Y").date()
daysLeft = deathDate - currentDate
print()
print()
print()
print("Hi Lakshay, You have exactly " + str(daysLeft.days) + \
      " days left of your life .")
print()
print()
print()

