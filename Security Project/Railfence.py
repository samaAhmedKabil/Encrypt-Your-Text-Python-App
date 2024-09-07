def  encryp_railfence_cipher(plain_text, key):
    key = int(key)
    cipher_text = ''
    rail = [['\n' for i in range(len(plain_text))] for j in range(key)]
    direction_down = False
    row, col = 0, 0

    for i in range(len(plain_text)):
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = plain_text[i]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    for i in range(key):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                cipher_text += rail[i][j]
    return cipher_text


def decrypt_railfence_cipher(cipher_text, key):
    key = int(key)
    plain_text = ''
    rail = [['\n' for i in range(len(cipher_text))] for j in range(key)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    row, col = 0, 0
    for i in range(len(cipher_text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        if rail[row][col] != '*':
            plain_text += rail[row][col]
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return plain_text
