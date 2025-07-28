import random

# Modular exponentiation
def mod_exp(base, exponent, mod):
    return pow(base, exponent, mod)

# Generate a large prime (simplified for demo)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=1000, end=5000):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# Diffie-Hellman Key Exchange
def diffie_hellman():
    # Step 1: Agree on public parameters
    p = generate_prime()
    g = random.randint(2, p - 2)

    print(f"Public prime (p): {p}")
    print(f"Primitive root (g): {g}")

    # Step 2: Alice generates private/public keys
    a = random.randint(2, p - 2)
    A = mod_exp(g, a, p)

    # Step 3: Bob generates private/public keys
    b = random.randint(2, p - 2)
    B = mod_exp(g, b, p)

    # Step 4: Exchange public keys and compute shared secrets
    shared_secret_alice = mod_exp(B, a, p)
    shared_secret_bob = mod_exp(A, b, p)

    print(f"\nAlice's Public Key: {A}")
    print(f"Bob's Public Key:   {B}")
    print(f"\nShared Secret (Alice): {shared_secret_alice}")
    print(f"Shared Secret (Bob):   {shared_secret_bob}")

    assert shared_secret_alice == shared_secret_bob, "Shared secrets do not match!"

if __name__ == "__main__":
    diffie_hellman()
