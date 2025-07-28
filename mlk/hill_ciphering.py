# Python3 code to implement Hill Cipher Encryption and Decryption

keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]

# Function to generate key matrix
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to encrypt the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += keyMatrix[i][x] * messageVector[x][j]
            cipherMatrix[i][j] %= 26

# Function to get determinant of 3x3 matrix
def determinant(matrix):
    det = (matrix[0][0]*((matrix[1][1]*matrix[2][2]) - (matrix[1][2]*matrix[2][1])) -
           matrix[0][1]*((matrix[1][0]*matrix[2][2]) - (matrix[1][2]*matrix[2][0])) +
           matrix[0][2]*((matrix[1][0]*matrix[2][1]) - (matrix[1][1]*matrix[2][0])))
    return det % 26

# Function to find modular inverse of a number modulo 26
def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Function to get cofactor matrix
def getCofactor(mat, p, q):
    temp = []
    for i in range(3):
        if i != p:
            row = []
            for j in range(3):
                if j != q:
                    row.append(mat[i][j])
            temp.append(row)
    return (temp[0][0]*temp[1][1] - temp[0][1]*temp[1][0]) % 26

# Function to get adjugate matrix
def adjugateMatrix(mat):
    adj = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            sign = (-1) ** (i + j)
            adj[j][i] = (sign * getCofactor(mat, i, j)) % 26  # Transpose + Cofactor
    return adj

# Function to inverse the key matrix
def inverseKeyMatrix(mat):
    det = determinant(mat)
    inv_det = modInverse(det, 26)
    if inv_det == -1:
        raise ValueError("Key matrix is not invertible")
    adj = adjugateMatrix(mat)
    inv = [[(adj[i][j] * inv_det) % 26 for j in range(3)] for i in range(3)]
    return inv

# Decryption function
def decrypt(cipherText, key):
    getKeyMatrix(key)
    invKey = inverseKeyMatrix(keyMatrix)

    # Convert ciphertext to vector
    cipherVec = [[ord(cipherText[i]) % 65] for i in range(3)]

    # Multiply inverse key with cipher vector
    decryptedVec = [[0] for _ in range(3)]
    for i in range(3):
        for j in range(1):
            for x in range(3):
                decryptedVec[i][j] += invKey[i][x] * cipherVec[x][j]
            decryptedVec[i][j] %= 26

    # Convert back to text
    decryptedText = ''.join([chr(decryptedVec[i][0] + 65) for i in range(3)])
    print("Decrypted Text:", decryptedText)

# Main driver
def main():
    message = "MAL"
    key = "GYBNQKURP"

    print("Original Message:", message)
    HillCipher(message, key)

    cipherText = ''.join([chr(cipherMatrix[i][0] + 65) for i in range(3)])
    decrypt(cipherText, key)

# Encryption wrapper
def HillCipher(message, key):
    getKeyMatrix(key)
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    encrypt(messageVector)
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    print("Ciphertext:", "".join(CipherText))

if __name__ == "__main__":
    main()
