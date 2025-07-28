#include <bits/stdc++.h>
using namespace std;

const int SIZE = 5;

// Function to prepare key matrix
void generateMatrix(string key, char matrix[SIZE][SIZE]) {
    set<char> used;

    string cur_key = "";
    for(auto c : key){
        if(c != 'j'){
            cur_key += c;
        }
    }
    key = cur_key;

    string filledKey = "";
    for (char c : key) {
        c = tolower(c);
        if (!used.count(c) && isalpha(c)) {
            used.insert(c);
            filledKey += c;
        }
    }

    for (char c = 'a'; c <= 'z'; ++c) {
        if (c == 'j') continue;
        if (!used.count(c)) {
            filledKey += c;
            used.insert(c);
        }
    }

    int index = 0;
    for (int i = 0; i < SIZE; ++i)
        for (int j = 0; j < SIZE; ++j)
            matrix[i][j] = filledKey[index++];
}

// Function to find position of character in matrix
void findPosition(char matrix[SIZE][SIZE], char ch, int &row, int &col) {
    if (ch == 'j') ch = 'i'; // Treat 'j' as 'i'
    for (int i = 0; i < SIZE; ++i)
        for (int j = 0; j < SIZE; ++j)
            if (matrix[i][j] == ch) {
                row = i;
                col = j;
                return;
            }
}

// Function to prepare digraphs (two-letter groups)
vector<pair<char, char>> prepareText(string text, bool forEncryption) {
    vector<pair<char, char>> digraphs;
    string cleaned = "";
    for (char c : text) {
        if (isalpha(c)) {
            cleaned += tolower(c == 'j' ? 'i' : c);
        }
    }

    for (size_t i = 0; i < cleaned.length(); ++i) {
        char a = cleaned[i];
        char b = (i + 1 < cleaned.length()) ? cleaned[i + 1] : 'x';

        if (a == b) {
            b = 'x';
        } else {
            ++i;
        }
        digraphs.emplace_back(a, b);
    }

    return digraphs;
}

// Encrypt a message
string encrypt(string text, char matrix[SIZE][SIZE]) {
    auto digraphs = prepareText(text, true);
    string result = "";

    for (auto &p : digraphs) {
        int r1, c1, r2, c2;
        findPosition(matrix, p.first, r1, c1);
        findPosition(matrix, p.second, r2, c2);

        if (r1 == r2) {
            result += matrix[r1][(c1 + 1) % SIZE];
            result += matrix[r2][(c2 + 1) % SIZE];
        } else if (c1 == c2) {
            result += matrix[(r1 + 1) % SIZE][c1];
            result += matrix[(r2 + 1) % SIZE][c2];
        } else {
            result += matrix[r1][c2];
            result += matrix[r2][c1];
        }
    }

    return result;
}

// Decrypt a message
string decrypt(string text, char matrix[SIZE][SIZE]) {
    auto digraphs = prepareText(text, false);
    string result = "";

    for (auto &p : digraphs) {
        int r1, c1, r2, c2;
        findPosition(matrix, p.first, r1, c1);
        findPosition(matrix, p.second, r2, c2);

        if (r1 == r2) {
            result += matrix[r1][(c1 - 1 + SIZE) % SIZE];
            result += matrix[r2][(c2 - 1 + SIZE) % SIZE];
        } else if (c1 == c2) {
            result += matrix[(r1 - 1 + SIZE) % SIZE][c1];
            result += matrix[(r2 - 1 + SIZE) % SIZE][c2];
        } else {
            result += matrix[r1][c2];
            result += matrix[r2][c1];
        }
    }

    return result;
}

void displayMatrix(char matrix[SIZE][SIZE]) {
    cout << "Playfair Key Matrix:\n";
    for (int i = 0; i < SIZE; ++i) {
        for (int j = 0; j < SIZE; ++j) {
            cout << matrix[i][j] << ' ';
        }
        cout << '\n';
    }
}

int main() {
    string key, plaintext;

    cout << "Enter the key: ";
    getline(cin, key);

    cout << "Enter the plaintext: ";
    getline(cin, plaintext);

    char matrix[SIZE][SIZE];
    generateMatrix(key, matrix);
    displayMatrix(matrix);

    string encrypted = encrypt(plaintext, matrix);
    cout << "\nEncrypted text: " << encrypted << endl;

    string decrypted = decrypt(encrypted, matrix);
    cout << "Decrypted text: " << decrypted << endl;

    return 0;
}
