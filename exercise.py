'''
Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
'''
import random
def generate(digits):
    digits=[]
    rand=random.sample(range(100, 999, 5), 3)
    digits.append(rand)
    return digits
digits=[]
print(generate(digits))

'''
Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two 
lucky tickets from it as a winner.
'''

import random
def luckyWinner(lucky):
    rand=random.sample(range(99,999),100)
    lucky=random.sample(rand,2)
    return lucky
lucky=[]
print(luckyWinner(lucky))

'''
Exercise 3: Generate 6 digit random secure OTP
'''

import random
def otpGen(otp):
    otp=random.sample(range(100000,999999),1)
    return otp
otp=None
print(otpGen(otp))

'''
Exercise 4: Pick a random character from a given String
'''
import random
def pick_char(s):
    rand=random.choice(s)
    return rand
s="hello"
print(pick_char(s))

'''
Exercise 5: Generate a random string of length 5
'''
import random
import string
def generate_random_string(s):
    return ''.join(random.choices(string.ascii_letters, k=5))
s=''
print(generate_random_string(s))


'''
Exercise 6: Generate a random password of 10 characters with conditions
'''
import random
import string

def passwordGen():
    password = (
        random.choices(string.ascii_uppercase, k=2) +
        random.choices(string.digits, k=1) +
        random.choices(string.punctuation, k=1) +
        random.choices(string.ascii_letters + string.digits + string.punctuation, k=6)
    )
    random.shuffle(password)
    return ''.join(password)
print(passwordGen())

'''
Exercise 7: Calculate multiplication of two random float numbers
'''
import random
def mulFloat(n1,n2):
    return n1*n2
n1,n2=random.uniform(1,10),random.uniform(1,10)
print(mulFloat(n1,n2))

# '''
# Exercise 8: Generate a random secure token of 64 bytes and random URL
# '''
import secrets

def generate_secure_token():
    secure_token = secrets.token_hex(64)
    random_url = f"https://seedr.com/{secrets.token_urlsafe(16)}"
    return secure_token, random_url
print(generate_secure_token())

# '''Exercise 9: Roll a dice that always returns the same number
# '''

def fixed_dice_roll(value):
    return value  
value=3
print(fixed_dice_roll(value))

'''
Exercise 10: Generate a random date between given start and end dates
'''
import datetime
import random
def generate_random_date(start_date, end_date):
    random_days = random.randint(0, (end_date - start_date).days)
    return start_date + datetime.timedelta(days=random_days)
start_date=datetime.date(2025,1,1)
end_date=datetime.date(2025,1,31)
print(generate_random_date(start_date,end_date))