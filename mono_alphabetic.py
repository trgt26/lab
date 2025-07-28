# Mono Alphabetic cipher
import string
import random

# Generate a random substitution key
def generate_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# Invert the key for decryption
def invert_key(key):
    return {v: k for k, v in key.items()}

# Encrypt using monoalphabetic cipher
def mono_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext.upper():
        if char in key:
            ciphertext += key[char]
        else:
            ciphertext += char  # Keep punctuation, spaces, etc.
    return ciphertext

# Decrypt using monoalphabetic cipher
def mono_decrypt(ciphertext, key):
    reversed_key = invert_key(key)
    plaintext = ""
    for char in ciphertext.upper():
        if char in reversed_key:
            plaintext += reversed_key[char]
        else:
            plaintext += char
    return plaintext

# Example usage
if __name__ == "__main__":
    key = generate_key()
    print("Encryption Key:", key)

    message = "HELLO WORLD"
    encrypted = mono_encrypt(message, key)
    print("Encrypted:", encrypted)

    decrypted = mono_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
