# Elliptic Curve

import random

# Curve Parameters (Example, NOT secure)
p = 2**127 - 1
a = 0
b = 3

# Example base point G (generator)
G = (1, 2)

# Modular inverse using Extended Euclidean Algorithm
def modinv(k, p):
    if k == 0:
        raise ZeroDivisionError('Division by zero')
    if k < 0:
        return p - modinv(-k, p)
    s, old_s = 0, 1
    r, old_r = p, k
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    return old_s % p

# Point addition on elliptic curve
def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    if P == Q:
        return point_double(P)

    if P[0] == Q[0] and (P[1] + Q[1]) % p == 0:
        return None  # Point at infinity

    m = ((Q[1] - P[1]) * modinv(Q[0] - P[0], p)) % p
    x_r = (m**2 - P[0] - Q[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p
    return (x_r, y_r)

# Point doubling
def point_double(P):
    if P is None:
        return None
    m = ((3 * P[0]**2 + a) * modinv(2 * P[1], p)) % p
    x_r = (m**2 - 2 * P[0]) % p
    y_r = (m * (P[0] - x_r) - P[1]) % p
    return (x_r, y_r)

# Scalar multiplication
def scalar_mult(k, P):
    result = None  # Point at infinity
    addend = P
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_double(addend)
        k >>= 1
    return result

# ECC Key Generation
def generate_keypair():
    private_key = random.randint(1, p - 1)
    public_key = scalar_mult(private_key, G)
    return private_key, public_key

# Example usage
if __name__ == "__main__":
    print("Elliptic Curve: y^2 = x^3 + {}x + {} mod {}".format(a, b, p))
    print("Base Point G:", G)

    # Alice's keys
    alice_priv, alice_pub = generate_keypair()
    print("\nAlice's Private Key:", alice_priv)
    print("Alice's Public Key: ", alice_pub)

    # Bob's keys
    bob_priv, bob_pub = generate_keypair()
    print("\nBob's Private Key:", bob_priv)
    print("Bob's Public Key: ", bob_pub)

    # Shared secret (ECDH key agreement)
    alice_shared = scalar_mult(alice_priv, bob_pub)
    bob_shared = scalar_mult(bob_priv, alice_pub)

    print("\nShared Secret (Alice):", alice_shared)
    print("Shared Secret (Bob):  ", bob_shared)
