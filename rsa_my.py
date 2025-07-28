# RSA
import math
def generate_key() :
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    n = p*q
    phi = (p-1) * (q-1)
    
    e = None
    # e = int(input("Enter Public key: "))
    for i in range(phi):
        if math.gcd(i, phi) == 1:
            e = i
            break

    d = pow(e, -1, phi)
    return (e, n), (d, n)

def encrypt(m, pu):
    e, n = pu
    enc = pow(m, e, n)
    return enc

def decrypt(m, pr) :
    d, n = pr
    dc = pow(m, d, n)
    return dc

def rsa() :
    txt = input()
    pu, pr = generate_key()
    enc_txt = []
    for c in txt:
        c_nm = ord(c)
        enc_txt.append(encrypt(c_nm, pu))
    print(enc_txt)
    ans = ''
    for enc_nm in enc_txt:
        c = decrypt(enc_nm, pr)
        c = chr(c)
        ans += c
    print(ans)

def ct() :
    pu, pr = generate_key()
    print(pu)
    print(pr)
    m = int(input())
    dc = decrypt(m , pr)
    print(dc)
rsa()

