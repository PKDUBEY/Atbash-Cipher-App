# Python program to Atbash Cipher App

def encrypt_dycrypt_char(plaintext_char):
    #checking if the character is an alphabet
    if plaintext_char.isalpha():

        #checking if character is upper case
        if plaintext_char.isupper():
            ascii_diff_with_char = ord(plaintext_char) - ord('A')
            plaintext_char = ord('Z') - ascii_diff_with_char
        # for lowercase character
        else:
            ascii_diff_with_char = ord(plaintext_char) - ord('a')
            plaintext_char = ord('z') - ascii_diff_with_char
        plaintext_char= chr(plaintext_char)

    return plaintext_char

# Reading each character of the text
def encrypt_dycrypt(text):
    new_text = ''
    for char in text:
        new_text += encrypt_dycrypt_char(char)
    return new_text

# taking user input to encrypt
plaintext = input('Type your message:')
ciphertext = encrypt_dycrypt(plaintext)
print(f'Ciphertext: {ciphertext}')
