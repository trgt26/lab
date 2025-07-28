def mod_inverse(a, m):
    """Find modular inverse of a mod m using brute-force"""
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception(f"No modular inverse for {a} mod {m}")

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

def chunk_text(text, size):
    text = text.upper().replace(" ", "")
    if len(text) % size != 0:
        text += 'X' * (size - len(text) % size)
    return [text[i:i+size] for i in range(0, len(text), size)]

def matrix_mul_2x2(matrix, vector):
    """Multiplies 2x2 matrix with 2x1 vector"""
    return [
        (matrix[0][0]*vector[0] + matrix[0][1]*vector[1]) % 26,
        (matrix[1][0]*vector[0] + matrix[1][1]*vector[1]) % 26
    ]

def matrix_inverse_2x2(matrix):
    """Find inverse of 2x2 matrix modulo 26"""
    det = (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26
    det_inv = mod_inverse(det, 26)

    # Adjugate and apply modular inverse
    inv = [
        [( matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26],
        [(-matrix[1][0] * det_inv) % 26, ( matrix[0][0] * det_inv) % 26]
    ]
    # Ensure all elements are positive mod 26
    for i in range(2):
        for j in range(2):
            inv[i][j] %= 26
    return inv

def encrypt(plaintext, key_matrix):
    chunks = chunk_text(plaintext, 2)
    ciphertext = ''
    for pair in chunks:
        nums = text_to_numbers(pair)
        encrypted_nums = matrix_mul_2x2(key_matrix, nums)
        ciphertext += numbers_to_text(encrypted_nums)
    return ciphertext

def decrypt(ciphertext, key_matrix):
    inverse_matrix = matrix_inverse_2x2(key_matrix)
    chunks = chunk_text(ciphertext, 2)
    plaintext = ''
    for pair in chunks:
        nums = text_to_numbers(pair)
        decrypted_nums = matrix_mul_2x2(inverse_matrix, nums)
        plaintext += numbers_to_text(decrypted_nums)
    return plaintext

# Example usage
key = [
    [3, 3],
    [2, 5]
]  # Must be invertible mod 26

message = "HI"
cipher = encrypt(message, key)
plain = decrypt(cipher, key)

print("Original:", message)
print("Encrypted:", cipher)
print("Decrypted:", plain)