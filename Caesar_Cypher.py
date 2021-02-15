# variables for later
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
# Retrieve Strings
file = open('TextDoc.txt', 'r')
text = file.readlines()


# Encryption
def encryption(strings):
    encrypted = []
    newword = ''
    for i in range(len(strings)):
        strings[i] = strings[i].rstrip('\n')
        for s in range(len(strings[i])):
            if strings[i][s].lower() in alphabet:
                if strings[i][s].isupper():
                    newword += alphabet[(alphabet.index(strings[i][s].lower()) + 10) % 26].upper()
                elif strings[i][s].islower():
                    newword += alphabet[(alphabet.index(strings[i][s].lower()) + 10) % 26].lower()
            else:
                newword += strings[i][s]
        encrypted.append(newword)
        newword = ''
    return encrypted


# Decryption
def decryption(strings):
    decrypted = []
    newword = ''
    for i in range(len(strings)):
        for s in range(len(strings[i])):
            if strings[i][s].lower() in alphabet:
                if strings[i][s].isupper():
                    newword += alphabet[(alphabet.index(strings[i][s].lower()) - 10) % 26].upper()
                elif strings[i][s].islower():
                    newword += alphabet[(alphabet.index(strings[i][s].lower()) - 10) % 26].lower()
            else:
                newword += strings[i][s]
        decrypted.append(newword)
        newword = ''
    return decrypted
# Logic


encrypted_strings = encryption(text)
print(f'The encrypted strings are: ')
for string in encrypted_strings:
    print(string)

decrypted_strings = decryption(encrypted_strings)
print('\nThe decrypted strings are: ')
for string in decrypted_strings:
    print(string)
