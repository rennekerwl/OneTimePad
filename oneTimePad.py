import random
import string
import sys

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

def load_cipher(cipherFile):
    cFile = open(cipherFile, 'r')
    cipher = file.read()
    cFile.close()
    return cipher

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


def main():
    while True:
        eOrD = input('(E)ncrypt or (D)ecrypt or (Q)uit?')
        if eOrD == 'E':
            genOrNot = input('(G)enerate a pseudorandom key or (L)oad key?')
            if genOrLoad == 'G':
                message = get_message()
                key = generate_key(message)
                ciphertext = generate_ciphertext(message, key)
                print('Ciphertext:')
                print(ciphertext)
                saveOrNot = input('(S)ave a copy of the key & ciphertext or (N)ot?')
                if saveOrNot == 'S':
                    save_key(key)
                    save_cipher(ciphertext)
            elif genOrLoad == 'L':
                message = get_message()
                keyFile = input('Filename of key?')
                key = load_key(keyFile)
                ciphertext = generate_ciphertext(message, key)
                saveOrNot = input('(S)ave a copy of the ciphertext or (N)ot?')
                if saveOrNot == 'S':
                    save_cipher(ciphertext)
        if eOrD == 'D':
            cipherByHandOrLoad = input('(T)ype ciphertext by hand or (L)oad it?')
            if cipherByHandOrLoad == 'T':
                cipherText = input('Ciphertext: ')
                keyByHandOrLoad = input('(T)ype in key by hand or (L)oad it?')
                if keyByHandOrLoad == 'T':
                    key = input('Key: ')
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
                elif keyByHandOrLoad == 'L':
                    keyFile = input('What is the name of the key file?')
                    key = read_key(keyFile)
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
            elif cipherByHandOrLoad == 'L':
                cipherFile = input('What is the name of the ciphertext file?')
                keyByHandOrLoad = input('(T)ype in key by hand or (L)oad it?')
                if keyByHandOrLoad == 'T':
                    key = input('Key: ')
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
                elif keyByHandOrLoad == 'L':
                    keyFile = input('What is the name of the key file?')
                    key = read_key(keyFile)
                    clearText = decode_cipher(cipherText, key)
                    print(clearText)
        elif eOrD == 'Q':
            sys.exit()
        else:
            print('Not a valid choice')

if __name__ == __main__:
    main()
