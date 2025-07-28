# Block Cipher

def xor(bits1, bits2):
    """XOR two binary strings of equal length"""
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bits1, bits2))

def str_to_bin(text):
    """Convert string to list of 8-bit binary strings"""
    return [format(ord(char), '08b') for char in text]

def bin_to_str(blocks):
    """Convert list of binary strings back to ASCII text"""
    return ''.join(chr(int(block, 2)) for block in blocks)

# ECB Mode
def ecb_encrypt(blocks, key):
    return [xor(block, key) for block in blocks]

def ecb_decrypt(ciphertext, key):
    return [xor(block, key) for block in ciphertext]

# CBC Mode
def cbc_encrypt(blocks, key, iv):
    ciphertext = []
    prev = iv
    for block in blocks:
        xored = xor(block, prev)
        cipher = xor(xored, key)
        ciphertext.append(cipher)
        prev = cipher
    return ciphertext

def cbc_decrypt(ciphertext, key, iv):
    plaintext = []
    prev = iv
    for cipher in ciphertext:
        decrypted = xor(cipher, key)
        plain = xor(decrypted, prev)
        plaintext.append(plain)
        prev = cipher
    return plaintext

# CFB Mode
def cfb_encrypt(blocks, key, iv):
    ciphertext = []
    prev = iv
    for block in blocks:
        encrypted = xor(prev, key)
        cipher = xor(block, encrypted)
        ciphertext.append(cipher)
        prev = cipher
    return ciphertext

def cfb_decrypt(ciphertext, key, iv):
    plaintext = []
    prev = iv
    for cipher in ciphertext:
        encrypted = xor(prev, key)
        plain = xor(cipher, encrypted)
        plaintext.append(plain)
        prev = cipher
    return plaintext

# OFB Mode
def ofb_encrypt(blocks, key, iv):
    ciphertext = []
    prev = xor(iv, key)
    for block in blocks:
        cipher = xor(block, prev)
        ciphertext.append(cipher)
        prev = xor(prev, key)
    return ciphertext

def ofb_decrypt(ciphertext, key, iv):
    plaintext = []
    prev = xor(iv, key)
    for cipher in ciphertext:
        plain = xor(cipher, prev)
        plaintext.append(plain)
        prev = xor(prev, key)
    return plaintext

# ---------- Run Example ----------
plaintext = "hello world sdfds fsdf"
key = '10101010'  # 8-bit key
iv  = '00001111'  # 8-bit IV

# Convert to binary
plain_blocks = str_to_bin(plaintext)

# Encrypt
ecb_c = ecb_encrypt(plain_blocks, key)
cbc_c = cbc_encrypt(plain_blocks, key, iv)
cfb_c = cfb_encrypt(plain_blocks, key, iv)
ofb_c = ofb_encrypt(plain_blocks, key, iv)

# Decrypt
ecb_p = ecb_decrypt(ecb_c, key)
cbc_p = cbc_decrypt(cbc_c, key, iv)
cfb_p = cfb_decrypt(cfb_c, key, iv)
ofb_p = ofb_decrypt(ofb_c, key, iv)

# Show Results
print("Plaintext       :", plaintext)
print("Binary Blocks   :", plain_blocks)
print("Key             :", key)
print("IV              :", iv)
print("\n--- Encryption Results ---")
print("ECB Ciphertext  :", ecb_c)
print("CBC Ciphertext  :", cbc_c)
print("CFB Ciphertext  :", cfb_c)
print("OFB Ciphertext  :", ofb_c)

print("\n--- Decryption Results ---")
print("ECB Decrypted   :", bin_to_str(ecb_p))
print("CBC Decrypted   :", bin_to_str(cbc_p))
print("CFB Decrypted   :", bin_to_str(cfb_p))
print("OFB Decrypted   :", bin_to_str(ofb_p))
