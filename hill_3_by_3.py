def mod_inverse(a, m):
    """Modular inverse using Extended Euclidean Algorithm"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception('No modular inverse')

def matrix_mod_inv(matrix, modulus):
    """Find inverse of 3x3 matrix mod 26"""
    # Compute determinant
    det = (matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) -
           matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]) +
           matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0])) % modulus

    det_inv = mod_inverse(det, modulus)

    # Compute cofactor matrix
    cof = [[0]*3 for _ in range(3)]
    for r in range(3):
        for c in range(3):
            minor = [[matrix[i][j] for j in range(3) if j != c] for i in range(3) if i != r]
            cof[r][c] = ((-1) ** (r + c)) * (minor[0][0]*minor[1][1] - minor[0][1]*minor[1][0])

    # Transpose of cofactor (adjugate)
    adj = [[cof[j][i] for j in range(3)] for i in range(3)]

    # Multiply adjugate by det_inv mod 26
    inv = [[(adj[i][j] * det_inv) % modulus for j in range(3)] for i in range(3)]
    return inv

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper()]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

def chunk_text(text, size):
    if len(text) % size != 0:
        text += 'X' * (size - len(text) % size)
    return [text[i:i+size] for i in range(0, len(text), size)]

def multiply_matrix_vector(matrix, vector):
    result = []
    for row in matrix:
        value = sum(row[i] * vector[i] for i in range(3)) % 26
        result.append(value)
    return result

def encrypt(plaintext, key):
    chunks = chunk_text(plaintext.upper(), 3)
    ciphertext = ""
    for chunk in chunks:
        vector = text_to_numbers(chunk)
        result = multiply_matrix_vector(key, vector)
        ciphertext += numbers_to_text(result)
    return ciphertext

def decrypt(ciphertext, key):
    inv_key = matrix_mod_inv(key, 26)
    chunks = chunk_text(ciphertext.upper(), 3)
    plaintext = ""
    for chunk in chunks:
        vector = text_to_numbers(chunk)
        result = multiply_matrix_vector(inv_key, vector)
        plaintext += numbers_to_text(result)
    return plaintext

# 🔐 Example Key and Message
key = [
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
]  # This matrix is invertible mod 26

message = "ACT"

ciphertext = encrypt(message, key)
decrypted = decrypt(ciphertext, key)

print("Plaintext: ", message)
print("Encrypted: ", ciphertext)
print("Decrypted: ", decrypted)