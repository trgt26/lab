#include<bits/stdc++.h>
using namespace  std;
string key = "QWERTYUIOPASDFGHJKLZXCVBNM";

map<char,char> en_map, dec_map;

void initialize_map(){
    for(int i=0;i<26;i++){
        en_map[i + 'A'] = key[i];
        dec_map[key[i]] = 'A' + i;
    }
}


string encrypt(string plain){
    string cipher = "";

    for(auto c : plain){
        if(isalpha(c)){
            cipher += en_map[toupper(c)];
        }
        else{
            cipher += c;
        }
    }

    return cipher;
}

string decrypt(string cipher){
    string plain = "";

    for(auto c : cipher){
        if(isalpha(c)){
            plain += dec_map[c];
        }
        else{
            plain += c;
        }
    }

    return plain;
}

int main(){

    initialize_map();
    string plain;
    getline(cin,plain);


    string cipher = encrypt(plain);

    cout<<cipher<<endl;

    plain = decrypt(cipher);

    cout<<plain<<endl;
}