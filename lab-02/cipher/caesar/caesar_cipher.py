from .alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        pass

    def encrypt_text(self, plain_text, key):
        result = ""
        for char in plain_text:
            if char.isalpha():
                shift = key % 26
                if char.isupper():
                    result += chr((ord(char) - 65 + shift) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += char
        return result

    def decrypt_text(self, cipher_text, key):
        return self.encrypt_text(cipher_text, -key)