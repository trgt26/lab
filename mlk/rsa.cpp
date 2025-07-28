#include<bits/stdc++.h>
using namespace std;
#define long long int

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

int mod_exp(int base,int exp,int mod){
    int result = 1;
    base %= mod;

    while(exp > 0){
        if(exp % 2 == 1){
            result *= base;
            result %= mod;
        }

        base *= base;
        base %= mod;
        exp /= 2;
    }

    return result;
}

int main(){
    int p = 61, q = 53;
    int n = p*q;

    int phi = (p-1) * (q-1);

    int e  = 17;
    int x,y;
    int gcd = inverse_mod(e,phi,x,y);
    x = (x + phi) % phi; 

    if(gcd != 1){
        cout<<"Inverse mod does not exits"<<endl;
        return -1;
    }

    int d = x;

    cout << "Public Key: (" << e << ", " << n << ")\n";
    cout << "Private Key: (" << d << ", " << n << ")\n";

    string message;
    getline(cin, message);
    vector<int> encrypted_message;

    for(auto c : message){
        int aschi_val = int(c);
        int cipher = mod_exp(aschi_val, e, n);
        encrypted_message.push_back(cipher);    
    }

    cout<<"Encrypted message : ";

    for(auto it : encrypted_message){
        cout<<it<<" ";
    }
    cout<<endl;


    string decrypted_message = "";

    for(auto it : encrypted_message){
        int val = mod_exp(it, d, n);
        char c = char(val);
        decrypted_message += c;
    }

    cout<<decrypted_message<<endl;
}