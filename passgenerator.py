# project1
MyFirstProject
import random
#creating a randomly secured password genrator
number = "1234567890"
special_cha = "!@#$%&" #special characters
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password_len = 12 #length of the password
all_character = number + alphabet + special_cha
my_password = "".join(random.sample(all_character, password_len))
print(my_password)
