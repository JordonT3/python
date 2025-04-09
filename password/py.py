import random  

import string


num_passwords = int(input("How many passwords would you like to generate? "))
password_length = int(input("How long should each password be? "))

characters = string.ascii_letters + string.digits + string.punctuation

print("\nHere are your passwords:")
for i in range(num_passwords):
    password = ''
    for j in range(password_length):
        password += random.choice(characters)
    print(password)