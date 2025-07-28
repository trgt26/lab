#include <iostream>
#include <cmath>
using namespace std;

// Fast modular exponentiation
long long modExp(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;

    while (exp > 0) {
        if (exp % 2 == 1)  // if exponent is odd
            result = (result * base) % mod;

        base = (base * base) % mod;
        exp /= 2;
    }

    return result;
}

int main() {
    // Step 1: Common agreed values (public)
    long long p = 23;  // prime modulus
    long long g = 5;   // primitive root modulo p

    cout << "Publicly Shared Prime (p): " << p << endl;
    cout << "Publicly Shared Base (g): " << g << endl;

    // Step 2: Alice chooses private key
    long long a = 6;  // Alice's private key (kept secret)
    long long A = modExp(g, a, p);  // A = g^a mod p

    // Step 3: Bob chooses private key
    long long b = 15;  // Bob's private key (kept secret)
    long long B = modExp(g, b, p);  // B = g^b mod p

    // Exchange of A and B happens here (publicly)

    // Step 4: Each computes shared secret
    long long aliceSecret = modExp(B, a, p);  // (B)^a mod p
    long long bobSecret = modExp(A, b, p);    // (A)^b mod p

    cout << "\nAlice's Public Key (A): " << A << endl;
    cout << "Bob's Public Key (B): " << B << endl;

    cout << "\nAlice's Computed Shared Secret: " << aliceSecret << endl;
    cout << "Bob's Computed Shared Secret:   " << bobSecret << endl;

    if (aliceSecret == bobSecret)
        cout << "\n✅ Shared key exchange successful!" << endl;
    else
        cout << "\n❌ Something went wrong!" << endl;

    return 0;
}
