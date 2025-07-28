# Diffie Hellman cipher
p = None
g = None

def primitive_root(p : int) :
    st = set(range(1, p))
    for i in range(2, p) :
        tmp = set()
        for j in range(1, p) :
            tmp.add(pow(i, j, p))
        if(tmp == st): return i
    return None

def generate_public_key(pr : int):
    return pow(g, pr, p) 

def generate_shared_key(pu : int, pr: int):
    return pow(pu, pr, p)

def diffie_hellman() :
    # Not Good Practice
    global g, p
    p = int(input("Enter a Prime: "))
    g = primitive_root(p)
    pr_alice = int(input("Enter Alice Private Key: "))
    pr_bob = int(input("Enter Bob Private Key: "))

    pu_alice = generate_public_key(pr_alice)
    pu_bob = generate_public_key(pr_bob)

    print(pu_alice)
    print(pu_bob)

    shared_alice = generate_shared_key(pu_bob, pr_alice)
    shared_bob = generate_shared_key(pu_alice, pr_bob)
    print("Shared (alice): ", shared_alice)
    print("Shared (Bob): ", shared_bob)
    if(shared_alice == shared_bob) :
        print("correct")
    else :
        print("incorrect")
diffie_hellman()

