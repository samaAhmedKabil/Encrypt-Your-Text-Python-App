def encrypt(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    x=""
    for char in key:
        if key != alphabet:
            x+=alphabet
    key+=x

    cipher = ''

    # Check for invalid inputs
    if plaintext is None or key is None:
        print("Invalid input")
        return None

    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            cipher += key[index]
        else:
            print("Invalid character:", char)
            return None  # Stop processing and return None for invalid characters

    return cipher





  
   

def decrypt(cipher, key):
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   key = key.lower()
   x=""
   for char in key:
        if key != alphabet:
            x+=alphabet
   key+=x
   decrypt_message = ''

    # Check for invalid inputs
   if cipher is None or key is None:
        print("Invalid input")
        return None

   for char in cipher:
        if char in alphabet:
            index = key.index(char)
            decrypt_message += alphabet[index]
        else:
            print("Invalid character:", char)
            return None  # Stop processing and return None for invalid characters

   return decrypt_message