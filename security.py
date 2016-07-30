"""
    encryption and decryption of strings using AES ciphers
"""
import Crypto.Random
from Crypto.Cipher import AES
import hashlib
import config

def generate_key(password, salt, iterations):
    assert iterations > 0
    key = password + salt
    for i in range(iterations):
        key = hashlib.sha256(key).digest()
    return key

def pad_text(text, multiple):
    extra_bytes = len(text) % multiple
    padding_size = multiple - extra_bytes
    padding = chr(padding_size) * padding_size
    padded_text = text + padding
    return padded_text

def unpad_text(padded_text):
    padding_size = ord(padded_text[-1])
    text = padded_text[:-padding_size]
    return text

def encrypt(plaintext, password):
    salt = Crypto.Random.get_random_bytes(config.saltSize)
    key = generate_key(password, salt, config.numberOfIterations)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad_text(plaintext, config.AESMultiple)
    ciphertext = cipher.encrypt(padded_plaintext)
    ciphertext_with_salt = salt + ciphertext
    return ciphertext_with_salt

def decrypt(ciphertext, password):
    salt = ciphertext[0:config.saltSize]
    ciphertext_sans_salt = ciphertext[config.saltSize:]
    key = generate_key(password, salt, config.numberOfIterations)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext_sans_salt)
    plaintext = unpad_text(padded_plaintext)
    return plaintext

def test():
    testText = "Hey this is awesome"
    passwd = "Apple"
    ecpText = encrypt(testText, passwd)
    print "Ecrypt = ", ecpText, '\n'
    print "Decrpt = ", decrypt(ecpText, passwd), '\n'

if __name__ == "__main__":
    test()
