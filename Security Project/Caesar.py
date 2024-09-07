def encrypt_caesar(plainText,key):
    intKey = int(key)
    result = ""
 
    for i in range(len(plainText)):
        char = plainText[i]
 
        if (char.isupper()):
            result += chr((ord(char) + intKey - 65) % 26 + 65)
 
        else:
            result += chr((ord(char) + intKey - 97) % 26 + 97)
 
    return result


def decrypt_caesar(cipher, key):
    intKey = int(key)
    message = ""
    
    for i in cipher:
        if i.isupper():
            message += chr((ord(i) - intKey - 65) % 26 + 65)
        elif i.islower():
            message += chr((ord(i) - intKey - 97) % 26 + 97)
        else:
            message+=" "
    return message