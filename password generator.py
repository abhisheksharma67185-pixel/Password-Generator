import random 
import string
string.ascii_letters = ("qwertyuiopasdfghjklzxcvbnm")
print(string.ascii_letters[1:26])
string.digits = "0123456789"
print(string.digits[0:9])
string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'
print(string.punctuation[1:9])
pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

while True:
    print('1: generate password')
    print('2: generate password with custom length')
    print('3: quit')
    choice = input('enter choice:')
    if choice == '1':
        password_chars = []
        for i in range (12):
            char = random.choice(pool)
            password_chars.append(char)
            password = ''.join(password_chars) 
            print(f'generated: {password}')
            input('press enter')
    elif choice == '2':
        length = int(input('enter length'))
        password_chars = []
        for i in range (length):
            char = random.choice(pool)
            password_chars.append(char)
            password = ''.join(password_chars) 
            print(f'generated: {password}')
            input('press enter')
        input('press enter')
    elif choice == '3':
        break