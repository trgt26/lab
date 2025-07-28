import numpy as np

def mod_inverse(a, m):
    """Modular inverse using extended Euclidean algorithm"""
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise Exception("Modular inverse does not exist")

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(int(n) + ord('A')) for n in numbers)

def chunk_text(text, size=3):
    text = text.upper().replace(" ", "")
    if len(text) % size != 0:
        text += 'X' * (size - len(text) % size)
    return [text[i:i+size] for i in range(0, len(text), size)]

def encrypt(plaintext, key_matrix):
    chunks = chunk_text(plaintext, 3)
    encrypted = []
    for block in chunks:
        vector = np.array(text_to_numbers(block)).reshape(3, 1)
        result = np.dot(key_matrix, vector) % 26
        encrypted.extend(result.flatten())
    return numbers_to_text(encrypted)

def decrypt(ciphertext, key_matrix):
    # Compute inverse key matrix mod 26
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)
    
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    key_inv = (det_inv * adjugate) % 26

    chunks = chunk_text(ciphertext, 3)
    decrypted = []
    for block in chunks:
        vector = np.array(text_to_numbers(block)).reshape(3, 1)
        result = np.dot(key_inv, vector) % 26
        decrypted.extend(result.flatten())
    return numbers_to_text(decrypted)

# ✅ Example key (must be invertible mod 26)
key = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

# 🔡 Plaintext
plaintext = "ACT"
ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("Plaintext:  ", plaintext)
print("Encrypted:  ", ciphertext)
print("Decrypted:  ", decrypted)