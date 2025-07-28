# Caeser cipher
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char  # leave non-alphabetic characters unchanged
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example usage
if __name__ == "__main__":
    message = "Hello, World!"
    shift = 3

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted:", decrypted)
