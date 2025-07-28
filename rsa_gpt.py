import random

# Compute GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm for modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

# Primality check (basic)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a random prime number
def generate_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# Key generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # common choice
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = modinv(e, phi)

    return ((e, n), (d, n))  # public, private

# Encrypt a message (as integer)
def encrypt(msg, pub_key):
    e, n = pub_key
    cipher = pow(msg, e, n)
    return cipher

# Decrypt a message
def decrypt(ciphertext, priv_key):
    d, n = priv_key
    msg = pow(ciphertext, d, n)
    return msg

# Convert text to int and back
def text_to_int(text):
    return int.from_bytes(text.encode(), 'big')

def int_to_text(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode()

# Example usage
if __name__ == "__main__":
    public, private = generate_keys()
    print("Public Key:", public)
    print("Private Key:", private)

    message = "HELLO"
    msg_int = text_to_int(message)
    cipher = encrypt(msg_int, public)
    print("Encrypted:", cipher)

    decrypted = decrypt(cipher, private)
    print("Decrypted:", int_to_text(decrypted))
