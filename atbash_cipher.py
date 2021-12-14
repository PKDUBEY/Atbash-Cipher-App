# Python program to Atbash Cipher App
class AtbashCipher:
    def encrypt_dycrypt_char(self, plaintext_char):
        # checking if the character is an alphabet
        if plaintext_char.isalpha():
            # checking if character is upper case
            if plaintext_char.isupper():
                ascii_diff_with_char = ord(plaintext_char) - ord('A')
                plaintext_char = ord('Z') - ascii_diff_with_char
            # for lowercase character
            else:
                ascii_diff_with_char = ord(plaintext_char) - ord('a')
                plaintext_char = ord('z') - ascii_diff_with_char
            plaintext_char = chr(plaintext_char)

        return plaintext_char

    # Reading each character of the text

    def encrypt_dycrypt(self, text):
        new_text = ''
        for char in text:
            new_text += self.encrypt_dycrypt_char(char)

        return new_text


if __name__ == '__main__':
    # taking user input to encrypt
    obj = AtbashCipher()
    plaintext = input('Type your message:')
    ciphertext = obj.encrypt_dycrypt(plaintext)
    print(f'Ciphertext: {ciphertext}')
