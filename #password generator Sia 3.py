#password generator Sia 3
import string
import random
print("----------------------------------------")
print("this is Sia's password generator")
print("Please enter the desired number of characters")
lenght = int(input())
lower= string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation
total = upper + num + symbol + lower
password = ""
for index in range(lenght):
    password=password+random.choice(total)
print("password: {}".format(password))