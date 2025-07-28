def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            used.add(char)
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def process_text(text):
    text = text.upper().replace("J", "I")
    processed = ""
    i = 0
    print(text)
    while i < len(text):
        a = text[i]
        b = ''
        print(i)
        if i + 1 < len(text):
            b = text[i + 1]

        if a == b or not b:
            b = 'X'
            i += 1
        else:
            i += 2
        processed += a + b
    return processed

def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(plaintext, key):
    matrix = generate_matrix(key)
    plaintext = process_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_pair(plaintext[i], plaintext[i+1], matrix)

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i], ciphertext[i+1], matrix)

    return plaintext

# Example
key = "MONARCHY"
plaintext = "abc"
ciphertext = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(ciphertext, key)

print("Key Matrix:")
for row in generate_matrix(key):
    print(row)

print("\nPlaintext:", plaintext)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted)
