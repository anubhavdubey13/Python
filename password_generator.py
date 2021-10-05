# Random Password Generator

# I am laughing as I am coding this XD
# This is gonna be simple yet fun
# Idk if there is a way to crack randomly generated passwords

# PS: With Quantum Computing, no password is secure enough right now :)

# Will be using secrets library instead of default pseudo-random numbers
# They claim to be suited for this purpose. Sue them if something goes wrong

import secrets

# Testing out different commands
# secrets.choice()
# secrets.token_hex(256)
# secrets.token_hex(256)
# secrets.SystemRandom()
# secrets.choice()
# secrets.token_bytes(34)
# secrets.randbits(64)

# Idk if my logic makes any sense but I am trying to compound the pseudorandomness here
# If someone has a supercomputer please test the difference between time to break this password
# vs something just generated at once by, say, secrets.token_hex(256)[0:password_length]

def password_generator():
    password_length = int(input('Enter password length: '))
    i=0
    password = ''
    while i < password_length:
        j = secrets.randbelow(256)
        mining = secrets.token_hex(256)
        # print(mining,'  ' ,j)
        if secrets.randbelow(512)%2 == 0:
            password += mining[j]
        else:
            password += mining[j].upper()
        i += 1
    print(password)

password_generator()

# Planning to host this somewhere and may be add a few more things
# https://www.thesecurityfactory.be/password-cracking-speed/