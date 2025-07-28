#include<bits/stdc++.h>

using namespace std;

const int a = 2;
const int b = 3;
const int p = 97;  // prime modulus
const pair<int, int> G = {3, 6};  // base point

// Modular inverse using Extended Euclidean Algorithm
int inverse_mod(int a,int b, int &x, int &y){
    if(b == 0){
        x = 1, y = 0;
        return a;
    }
    int x1, y1;
    int gcd = inverse_mod(b,a%b, x1, y1);

    x = y1;
    y = x1 - (a/b)*y1;
    return gcd;
}


int modinv(int a, int p) {
    int x, y;
    int g = inverse_mod(a, p, x, y);
    if (g != 1) {
        throw runtime_error("Modular inverse does not exist");
    }
    return (x % p + p) % p;  // Ensure positive result
}

// ECC Point addition
pair<int, int> ecc_add(pair<int, int> P, pair<int, int> Q) {
    if (P.first == -1 && P.second == -1) return Q;
    if (Q.first == -1 && Q.second == -1) return P;

    int x1 = P.first, y1 = P.second;
    int x2 = Q.first, y2 = Q.second;

    if (x1 == x2 && y1 != y2)
        return {-1, -1};  // Point at infinity

    int m;
    if (P == Q) {
        int num = (3 * x1 * x1 + a) % p;
        int den = modinv(2 * y1, p);
        m = (num * den) % p;
    } else {
        int num = (y2 - y1 + p) % p;
        int den = modinv((x2 - x1 + p) % p, p);
        m = (num * den) % p;
    }

    int x3 = (m * m - x1 - x2 + p * 3) % p;
    int y3 = (m * (x1 - x3 + p) - y1 + p * 2) % p;

    return {x3, y3};
}

// Scalar multiplication (Double and Add)
pair<int, int> scalar_mult(int k, pair<int, int> P) {
    pair<int, int> result = {-1, -1};  // Point at infinity
    pair<int, int> addend = P;

    while (k > 0) {
        if (k & 1)
            result = ecc_add(result, addend);
        addend = ecc_add(addend, addend);
        k >>= 1;
    }

    return result;
}

// Generate keypair
pair<int, pair<int, int>> generate_keypair(int private_key) {
    pair<int, int> public_key = scalar_mult(private_key, G);
    return {private_key, public_key};
}

// Print a point
void print_point(const string& label, pair<int, int> P) {
    if (P.first == -1)
        cout << label << ": Point at Infinity" << endl;
    else
        cout << label << ": (" << P.first << ", " << P.second << ")" << endl;
}

int main() {
    cout << "== ECDH Key Exchange ==\n";

    // Alice's key
    int alice_private = 7;
    auto [privA, pubA] = generate_keypair(alice_private);
    print_point("Alice's Public Key", pubA);

    // Bob's key
    int bob_private = 11;
    auto [privB, pubB] = generate_keypair(bob_private);
    print_point("Bob's Public Key", pubB);

    // Shared secret computation
    pair<int, int> alice_shared = scalar_mult(privA, pubB);
    pair<int, int> bob_shared = scalar_mult(privB, pubA);

    print_point("Alice's Shared Secret", alice_shared);
    print_point("Bob's Shared Secret", bob_shared);

    if (alice_shared == bob_shared)
        cout << "Shared Secret Match" << endl;
    else
        cout << "Shared Secret does not Match" << endl;

    return 0;
}
