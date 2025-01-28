'''
1. use the os and os.path modules to list the contents of your downloads folder  and indicate for each item 
whether it's a file or a folder (hint : use os.path.join)  
'''
import os

contents=os.path.expanduser("~/Downloads")
for dir in os.listdir(contents):
    path=os.path.join(contents,dir)
    if os.path.isfile(path):
        print(dir,"is file")
    if os.path.isdir(path):
        print(dir,"is folder")


'''
2. import  string module and print out all  ASCII letters defined in this module
'''

import string
print(string.ascii_letters)


'''
3. Import the sample() function from the random module and the ascii_letters attribute

of the string module. use these to randomly sample five letters and assign these

to a variable called five_letters
'''
from random import sample
from string import ascii_letters
five_letters=''.join(sample(ascii_letters,5))
print(five_letters)


'''
4. Take a input from the user a date for eg: 25/02/2020
    a.print output Date in format  Tuesday 25 February 2020
    b.print the day of the week of a given input  date
    c. Add 15 days and 23 hours to a given input date
    d. calculate the date 6 months from the current date
'''

from datetime import timedelta,datetime
from dateutil.relativedelta import relativedelta

dt=input("enter date in dd/mm/yyyy:")
date=datetime.strptime(dt,"%d/%m/%Y")
str_date=date.strftime("%A %d %B %Y")
print(str_date)


print("Day of the input date:",date.strftime('%A'))


addedDate=date+timedelta(days=15,hours=23)
print("added 15 days and 23 hrs:",addedDate.strftime("%A %d %B %Y %H:%M"))


cur_date = datetime.now()
sixMonths = cur_date + relativedelta(months=6)
print("Date after 6 Months:", sixMonths.strftime("%A %d %B %Y"))


'''
5. Create a game of rock paper and scissors where user will input one option
while second option is chosen by the computer(i.e your python program). Based
on the options select declare the result
1. user wins
2. computer wins
3. draw
 
if it is draw continue the game till one of them gets won
'''

import random

while True:
    choice = input("Enter your choice (rock/paper/scissors): ").lower()

    comp = random.choice(["rock", "paper", "scissors"])
    print("Computer choosed:", comp)

    if choice=="rock" or choice=="paper" or choice=="scissors":

        if choice == comp:
            print("Draw!")
            continue
        elif (choice == "rock" and comp == "scissors") or (choice == "scissors" and comp == "paper") or (choice == "paper" and comp == "rock"):
            print("You win!")
        else:
            print("Computer win!")
        
        break
    else:
        print("wrong input")

