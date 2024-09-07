import math
def encrypt_transposition_cipher(message, key):
    # Remove any spaces from the message
    message = message.replace(" ", "")

    # Calculate the number of columns based on the key length
    num_columns = math.ceil(len(message) / len(key))

    # Add padding to the message if necessary
    padding = num_columns * len(key) - len(message)
    message += "X" * padding

    # Create the grid
    grid = []
    for i in range(num_columns):
        start = i * len(key)
        end = start + len(key)
        grid.append(list(message[start:end]))

    # Encrypt the message by reading the grid row by row
    encrypted_message = []
    for k in key:
        column_index = int(k) - 1
        for row in grid:
            encrypted_message.append(row[column_index])

    return "".join(encrypted_message)

def decrypt_transposition_cipher(ciphertext, key):
    # Calculate the number of columns based on the key length
    num_columns = math.ceil(len(ciphertext) / len(key))

    # Create the grid
    grid = []
    for i in range(num_columns):
        grid.append([""] * len(key))

    # Fill the grid column by column
    column_index = 0
    for k in key:
        row_index = 0 
        while row_index < num_columns:
            grid[row_index][int(k) - 1] = ciphertext[column_index]
            row_index += 1
            column_index += 1

    # Decrypt the message by reading the grid column by column
    decrypted_message = []
    for row in grid:
        decrypted_message.extend(row)

    # Remove padding from the decrypted message
    decrypted_message = "".join(decrypted_message)
    decrypted_message = decrypted_message.replace("X", "")

    return decrypted_message