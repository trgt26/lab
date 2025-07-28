#include <iostream>
#include <string>
using namespace std;

// Encrypt the plaintext using Caesar Cipher
string encrypt(string text, int key) {
    string result = "";

    for (char c : text) {
        if (isupper(c)) {
            result += char((c - 'A' + key) % 26 + 'A');
        } else if (islower(c)) {
            result += char((c - 'a' + key) % 26 + 'a');
        } else {
            result += c; // Keep spaces or punctuation unchanged
        }
    }

    return result;
}

// Decrypt the ciphertext using Caesar Cipher
string decrypt(string text, int key) {
    string result = "";

    for (char c : text) {
        if (isupper(c)) {
            result += char((c - 'A' - key + 26) % 26 + 'A');
        } else if (islower(c)) {
            result += char((c - 'a' - key + 26) % 26 + 'a');
        } else {
            result += c;
        }
    }

    return result;
}

int main() {
    string plaintext;
    int key;

    cout << "Enter the plaintext: ";
    getline(cin, plaintext);

    cout << "Enter the key (0-25): ";
    cin >> key;

    string encrypted = encrypt(plaintext, key);
    cout << "Encrypted text: " << encrypted << endl;

    string decrypted = decrypt(encrypted, key);
    cout << "Decrypted text: " << decrypted << endl;

    return 0;
}
