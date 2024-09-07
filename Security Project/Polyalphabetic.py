def polyalphabetic_cipher(plaintext, key):
    key = key.upper()
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ''.join(chr(((ord(ch) - ord('A')) + (ord(key[i % len(key)]) - ord('A'))) % 26 + ord('A')) for i, ch in enumerate(plaintext))
    return ciphertext

def polyalphabetic_decipher(ciphertext, key):
    key = key.upper()
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ''.join(chr(((ord(ch) - ord('A')) - (ord(key[i % len(key)]) - ord('A'))) % 26 + ord('A')) for i, ch in enumerate(ciphertext))
    return plaintext