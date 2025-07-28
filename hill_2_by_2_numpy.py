# hill cipher
import numpy as np

def mod_inverse(a, m):
    """Modular inverse using extended Euclidean algorithm"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise Exception('No modular inverse exists')

def process_text(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'  # Padding if odd length
    return text

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join([chr(n + ord('A')) for n in numbers])

def encrypt(text, key_matrix):
    text = process_text(text)
    numbers = text_to_numbers(text)
    encrypted = []

    for i in range(0, len(numbers), 2):
        block = np.array([[numbers[i]], [numbers[i+1]]])
        cipher_block = np.dot(key_matrix, block) % 26
        encrypted.extend(cipher_block.flatten())

    return numbers_to_text(encrypted)

def decrypt(cipher, key_matrix):
    cipher = process_text(cipher)
    numbers = text_to_numbers(cipher)

    # Find inverse of key matrix modulo 26
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inv = mod_inverse(det, 26)
    
    adjugate = np.round(np.linalg.inv(key_matrix) * det).astype(int) % 26
    key_inv = (det_inv * adjugate) % 26

    decrypted = []

    for i in range(0, len(numbers), 2):
        block = np.array([[numbers[i]], [numbers[i+1]]])
        plain_block = np.dot(key_inv, block) % 26
        decrypted.extend(plain_block.flatten())

    return numbers_to_text(decrypted)

# Example usage
key = np.array([[3, 3],
                [2, 5]])  # Must be invertible mod 26

plaintext = "HELP"
cipher = encrypt(plaintext, key)
decrypted = decrypt(cipher, key)

print(f"Plaintext:  {plaintext}")
print(f"Ciphertext: {cipher}")
print(f"Decrypted:  {decrypted}")