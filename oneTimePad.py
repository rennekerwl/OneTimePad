import random
import string

def get_message():
    message = input('Message: ')
    return message

def generate_key(message):
    key = ''
    for letter in message:
        randLetter = random.choice(string.ascii_letters)
        key += randLetter
    return key

def save_key(key):
    keyFile = open('key.txt', 'w')
    keyFile.write(key)
    keyFile.close()

def read_key(keyFile):
    file = open(keyFile, 'w')
    key = file.read()
    file.close()
    return key

def generate_ciphertext(message, key):
    messageNumbers = []
    keyNumbers = []
    cipherNumbers = []
    cipherText = ''

    for letter in message:
        messageNumbers.append(ord(letter))

    for letter in key:
        keyNumbers.append(ord(letter))

    for i in range(len(keyNumbers)):
        cipherNumbers.append(messageNumbers[i] ^ keyNumbers[i])

    for number in cipherNumbers:
        cipherText += chr(number)

    return cipherText

def save_cipher(cipherText):
    cipherFile = open('ciphertext.txt', 'w')
    cipherFile.write(cipherText)
    cipherFile.close()

def decode_cipher(cipherText, key):
    messageNumbers = []
    keyNumbers = []
    cipherNumbers = []
    clearText = ''

    for letter in cipherText:
        cipherNumbers.append(ord(letter))

    for letter in key:
        keyNumbers.append(ord(letter))

    for i in range(len(keyNumbers)):
        messageNumbers.append(cipherNumbers[i] ^ keyNumbers[i])

    for number in messageNumbers:
        clearText += chr(number)

    return clearText


message = get_message()
print('message: ', message)
key = generate_key(message)
print('key: ', key)
cipherText = generate_ciphertext(message, key)
print('ciphertext: ', cipherText)
clearText = decode_cipher(cipherText, key)
print('cleartext: ', clearText)
