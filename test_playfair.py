import string
def generate_key_matrix(key):
    key = key.replace("I", "J")
    added = set()
    matrix = []
    for char in key.upper():
        if char not in added:
            added.add(char)
            matrix.append(char)
    
    for char in string.ascii_uppercase:
        if char not in added:
            added.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]
def pre_process(text):
    text = text.upper().replace("I", "J")
    text = ''.join(filter(str.isalpha, text))
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'X' + text[i + 1:]
    if len(text) % 2 != 0:
        text += 'X'
    return text
def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None, None
def encrypt_decrypt(matrix, a, b, ed):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    # print(f"Positions: {a} at ({row_a}, {col_a}), {b} at ({row_b}, {col_b})")
    if row_a == row_b:
        return matrix[row_a][(col_a + ed) % 5] + matrix[row_b][(col_b + ed) % 5]
    elif col_a == col_b:
        return matrix[(row_a + ed) % 5][col_a] + matrix[(row_b + ed) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]
def playfair_encrypt(text, key):
    matrix = generate_key_matrix(key)
    text = pre_process(text)
    cyphertext = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        # print(f"Encrypting pair: {a}, {b}")
        cyphertext += encrypt_decrypt(matrix, a, b, 1)
    return cyphertext
def playfair_decrypt(text, key):
    matrix = generate_key_matrix(key)
    plaintext = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        plaintext += encrypt_decrypt(matrix, a, b, -1)
    return plaintext
key = "PLAYFAIR"
text = "JJII"
print("Original Text:", text)
cyphertext = playfair_encrypt(text, key)
print("Encrypted:", cyphertext)
plaintext = playfair_decrypt(cyphertext, key)
print("Decrypted:", plaintext)
