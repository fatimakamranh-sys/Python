import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
length = int(input("how long do you want your password")) 
print(f"Your password: {generate_password(length)}")   