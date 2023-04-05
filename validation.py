import time 
import re
from datetime import datetime

def name_v(name):
    while True:
        i=input(name)
        if i.isalpha():
            return i
        print("please Enter a valid name")   
        
        
def money_v(money):
    while True:
        i=input(money)
        if i.isdigit():
            return i
        print("please Enter a valid amount of money")            


def email_v(email):
    while True:
        i = input(email)
        if re.match(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', i):
            return i
        print("Please enter a valid email address")



def date_v(date):
    while True:
        i=input(date)
        if datetime.strptime(i,"%Y-%m-%d"):
            return i
        print("enter a valid date (YYYY-MM-DD)")



def phone_v(phone):
    while True:
        i=input(phone)
        if re.match(r'01[0125][0-9]{8}', i):
            return i
        print("enter a valid phone number")


def confirm_pw(confirm,password):
    while True:
        i=input(confirm)
        if i==password:
            return i
        print("passwords don't match")
    


