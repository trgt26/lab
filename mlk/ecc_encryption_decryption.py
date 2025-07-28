from typing import Tuple

# Elliptic curve over F_p
p = 17
a = 2
b = 2

# base point
G = (5, 1)

# message point
Pm = (6, 3)

# Alice's private key
alpha = 2

# Bob's private key
beta = 3

# Modular inverse
def modinv(x: int, p: int) -> int:
    return pow(x, p - 2, p)

# Point addition
def point_add(P: Tuple[int, int], Q: Tuple[int, int]) -> Tuple[int, int]:
    if P == (None, None): return Q
    if Q == (None, None): return P
    x1, y1 = P
    x2, y2 = Q
    if P == Q:
        # point doubling
        m = ((3*x1*x1 + a) * modinv(2*y1, p)) % p
    else:
        if x1 == x2 and (y1 + y2) % p == 0:
            return (None, None)  # point at infinity
        m = ((y2 - y1) * modinv(x2 - x1, p)) % p
    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p
    return (x3, y3)

# Scalar multiplication
def scalar_mult(k: int, P: Tuple[int, int]) -> Tuple[int, int]:
    R = (None, None)  # point at infinity
    while k > 0:
        if k % 2 == 1:
            R = point_add(R, P)
        P = point_add(P, P)
        k //= 2
    return R

# Public keys
PA = scalar_mult(alpha, G)
PB = scalar_mult(beta, G)

print(f"Public key of Alice (alpha*G): {PA}")
print(f"Public key of Bob (beta*G): {PB}")

# Encryption by Alice:
# A sends C_m = {Pm, Pm + alpha*PB}

C1 = Pm
alphaPB = scalar_mult(alpha, PB)
C2 = point_add(Pm, alphaPB)

ciphertext = (C1, C2)

print(f"Ciphertext C_m: {ciphertext}")

# Decryption by Bob:
# Computes C2 - beta*C1 = Pm
betaC1 = scalar_mult(beta, C1)
# negate y-coordinate of betaC1
neg_betaC1 = (betaC1[0], (-betaC1[1]) % p)
Pm_decrypted = point_add(C2, neg_betaC1)

print(f"Decrypted message point Pm: {Pm_decrypted}")

# Check
if Pm_decrypted == Pm:
    print("✅ Decryption successful, Pm matches original.")
else:
    print("❌ Decryption failed.")
