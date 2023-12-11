import random, string
import os 

password_length = int(input("Type in the wanted length of your password: "))

password_characters = string.ascii_letters + string.digits + string.punctuation

password = []

for x in range(password_length):
    password.append(random.choice(password_characters))

print(''.join(password))

os.system("pause")
