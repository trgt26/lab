def xor_byte(byte, key):
    return byte ^ key

# ------------------ ECB ------------------
def ecb_encrypt(plaintext: bytes, key: int) -> bytes:
    return bytes([xor_byte(b, key) for b in plaintext])

def ecb_decrypt(ciphertext: bytes, key: int) -> bytes:
    return ecb_encrypt(ciphertext, key)  # XOR is symmetric

# ------------------ CBC ------------------
def cbc_encrypt(plaintext: bytes, key: int, iv: int) -> bytes:
    ciphertext = []
    prev = iv
    for b in plaintext:
        xored = b ^ prev
        enc = xor_byte(xored, key)
        ciphertext.append(enc)
        prev = enc
    return bytes(ciphertext)

def cbc_decrypt(ciphertext: bytes, key: int, iv: int) -> bytes:
    plaintext = []
    prev = iv
    for b in ciphertext:
        dec = xor_byte(b, key)
        plain = dec ^ prev
        plaintext.append(plain)
        prev = b
    return bytes(plaintext)

# ------------------ CFB ------------------
def cfb_encrypt(plaintext: bytes, key: int, iv: int) -> bytes:
    ciphertext = []
    feedback = iv
    for b in plaintext:
        out = xor_byte(feedback, key)
        c = b ^ out
        ciphertext.append(c)
        feedback = c
    return bytes(ciphertext)

def cfb_decrypt(ciphertext: bytes, key: int, iv: int) -> bytes:
    plaintext = []
    feedback = iv
    for b in ciphertext:
        out = xor_byte(feedback, key)
        p = b ^ out
        plaintext.append(p)
        feedback = b
    return bytes(plaintext)

# ------------------ OFB ------------------
def ofb_encrypt(plaintext: bytes, key: int, iv: int) -> bytes:
    ciphertext = []
    feedback = iv
    for b in plaintext:
        feedback = xor_byte(feedback, key)
        c = b ^ feedback
        ciphertext.append(c)
    return bytes(ciphertext)

def ofb_decrypt(ciphertext: bytes, key: int, iv: int) -> bytes:
    return ofb_encrypt(ciphertext, key, iv)  # OFB is symmetric

# ------------------ MAIN ------------------
def main():
    # Input from user
    plaintext_str = input("Enter plaintext (ASCII): ")
    key_str = input("Enter 8-bit binary key (e.g., 10101010): ")
    iv_str = input("Enter 8-bit binary IV (e.g., 00011111): ")

    # Convert input
    plaintext = plaintext_str.encode()
    key = int(key_str, 2)
    iv = int(iv_str, 2)

    print("\nPlaintext:", plaintext)

    # ECB
    ecb_ct = ecb_encrypt(plaintext, key)
    ecb_pt = ecb_decrypt(ecb_ct, key)
    print("\nECB Ciphertext:", ecb_ct)
    print("ECB Decrypted :", ecb_pt)

    # CBC
    cbc_ct = cbc_encrypt(plaintext, key, iv)
    cbc_pt = cbc_decrypt(cbc_ct, key, iv)
    print("\nCBC Ciphertext:", cbc_ct)
    print("CBC Decrypted :", cbc_pt)

    # CFB
    cfb_ct = cfb_encrypt(plaintext, key, iv)
    cfb_pt = cfb_decrypt(cfb_ct, key, iv)
    print("\nCFB Ciphertext:", cfb_ct)
    print("CFB Decrypted :", cfb_pt)

    # OFB
    ofb_ct = ofb_encrypt(plaintext, key, iv)
    ofb_pt = ofb_decrypt(ofb_ct, key, iv)
    print("\nOFB Ciphertext:", ofb_ct)
    print("OFB Decrypted :", ofb_pt)

if __name__ == "__main__":
    main()
