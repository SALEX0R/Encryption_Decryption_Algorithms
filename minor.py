import math

# Global variables for Hill Cipher
encrypt = [[0] for _ in range(3)]
decrypt = [[0] for _ in range(3)]
a = [[0] for _ in range(3)]
b = [[0] for _ in range(3)]
mes = [[0] for _ in range(3)]
c = [[0] for _ in range(3)]
data = ""
key = 0
count = 0

# Global variables for Playfair Cipher
key_pf = ""
play = [[0] * 5 for _ in range(5)]
ct = ""
txt = ""


# Function for Hill Cipher encryption
def hill_encryption():
    global encrypt
    for i in range(3):
        for j in range(1):
            for k in range(3):
                encrypt[i][j] += a[i][k] * mes[k][j]

    print("\nEncrypted string is:", end=" ")
    for i in range(3):
        print(chr(int(math.fmod(encrypt[i][0], 26) + 97)), end="")


# Function for Hill Cipher decryption
def hill_decryption():
    global decrypt
    hill_inverse()

    for i in range(3):
        for j in range(1):
            for k in range(3):
                decrypt[i][j] += b[i][k] * encrypt[k][j]

    print("\nDecrypted string is:", end=" ")
    for i in range(3):
        print(chr(int(math.fmod(decrypt[i][0], 26) + 97)), end="")
    print()


# Function to calculate the inverse of the matrix
def hill_inverse():
    global b
    for i in range(3):
        for j in range(3):
            if i == j:
                b[i][j] = 1
            else:
                b[i][j] = 0

    for k in range(3):
        for i in range(3):
            p = c[i][k]
            q = c[k][k]

            for j in range(3):
                if i != k:
                    c[i][j] = c[i][j] * q - p * c[k][j]
                    b[i][j] = b[i][j] * q - p * b[k][j]

    for i in range(3):
        for j in range(3):
            b[i][j] = b[i][j] / c[i][i]

    print("\nInverse Matrix is:")
    for i in range(3):
        for j in range(3):
            print(int(b[i][j]), end="")
        print()


# Function for Hill Cipher key and message input
def hill_getKeyMessage():
    global a, c, mes
    print("Enter 3x3 matrix for key (It should be invertible):")
    for i in range(3):
        for j in range(3):
            a[i][j] = float(input())

    c = [row[:] for row in a]

    msg = input("Enter a 3 letter string: ")
    for i in range(3):
        mes[i][0] = ord(msg[i]) - 97


# Function for Playfair Cipher encryption
def encryption_pf(pt):
    global play, ct
    print("\nPlain text:", pt)
    play_fair_cipher()
    j = 1
    i = 0
    while i < len(pt):
        row1, row2, col1, col2, p, q = 0, 0, 0, 0, 0, 0
        p = ord(pt[i])
        q = ord(pt[j])
        print("\t", pt[i], pt[j], "=", end="")
        if p == ord('j'):
            p = ord('i')
        if q == ord('j'):
            q = ord('i')
        for k in range(5):
            for l in range(5):
                if play[k][l] == p:
                    row1, col1 = k, l
                if play[k][l] == q:
                    row2, col2 = k, l
        if row1 == row2:
            if col2 == 4:
                ct[i] = chr(ord(play[row1][(col1 + 1) % 5]) + 97)
                ct[j] = chr(ord(play[row2][0]) + 97)
            else:
                ct[i] = chr(ord(play[row1][(col1 + 1) % 5]) + 97)
                ct[j] = chr(ord(play[row2][(col2 + 1) % 5]) + 97)
            print(ct[i], ct[j], end="")
        elif col1 == col2:
            if row2 == 4:
                ct[i] = chr(ord(play[(row1 + 1) % 5][col1]) + 97)
                ct[j] = chr(ord(play[0][col2]) + 97)
            else:
                ct[i] = chr(ord(play[(row1 + 1) % 5][col1]) + 97)
                ct[j] = chr(ord(play[(row2 + 1) % 5][col2]) + 97)
            print(ct[i], ct[j], end="")
        else:
            ct[i] = chr(ord(play[row1][col2]) + 97)
            ct[j] = chr(ord(play[row2][col1]) + 97)
            print(ct[i], ct[j], end="")
        i += 2
        j += 2
    print("\n\nEncrypted Message:", ct)


# Function for Playfair Cipher decryption
def decryption_pf(pt):
    global play, ct
    print("\nCipher text:", pt)
    j = 1
    i = 0
    while i < len(pt):
        row1, row2, col1, col2, p, q = 0, 0, 0, 0, 0, 0
        p = ord(pt[i])
        q = ord(pt[j])
        print("\t", pt[i], pt[j], "=", end="")
        if p == ord('j'):
            p = ord('i')
        if q == ord('j'):
            q = ord('i')
        for k in range(5):
            for l in range(5):
                if play[k][l] == p:
                    row1, col1 = k, l
                if play[k][l] == q:
                    row2, col2 = k, l
        if row1 == row2:
            if col2 == 0:
                ct[i] = chr(ord(play[row1][(col1 - 1) % 5]) + 97)
                ct[j] = chr(ord(play[row2][4]) + 97)
            else:
                ct[i] = chr(ord(play[row1][(col1 - 1) % 5]) + 97)
                ct[j] = chr(ord(play[row2][(col2 - 1) % 5]) + 97)
            print(ct[i], ct[j], end="")
        elif col1 == col2:
            if row2 == 0:
                ct[i] = chr(ord(play[(row1 - 1) % 5][col1]) + 97)
                ct[j] = chr(ord(play[4][col2]) + 97)
            else:
                ct[i] = chr(ord(play[(row1 - 1) % 5][col1]) + 97)
                ct[j] = chr(ord(play[(row2 - 1) % 5][col2]) + 97)
            print(ct[i], ct[j], end="")
        else:
            ct[i] = chr(ord(play[row1][col2]) + 97)
            ct[j] = chr(ord(play[row2][col1]) + 97)
            print(ct[i], ct[j], end="")
        i += 2
        j += 2
    print("\n\nDecrypted Message:", ct)


# Function to fill Playfair Cipher matrix
def play_fair_cipher():
    global key_pf, play
    print("\nEnter key:", end=" ")
    key_pf = input()
    key_pf += "abcdefghiklmnopqrstuvwxyz"
    key_pf = "".join(sorted(set(key_pf), key=key_pf.index))
    size = len(key_pf)
    k = 0
    for i in range(5):
        for j in range(5):
            play[i][j] = key_pf[k]
            k += 1


# Function for Hill Cipher key and message input
def hill_getKeyMessage():
    global a, c, mes
    print("Enter 3x3 matrix for key (It should be invertible):")
    for i in range(3):
        for j in range(3):
            a[i][j] = float(input())
            c[i][j] = a[i][j]

    msg = input("Enter a 3-letter string: ")
    for i in range(3):
        mes[i][0] = ord(msg[i]) - 97


# Function for Caesar Cipher encryption
def caesar_cipher_encryption():
    global data, key
    encrypted_data = ""
    for count in range(len(data)):
        temp = data[count]
        if 'a' <= temp <= 'z':
            temp = chr(((ord(temp) + key - ord('a')) % 26) + ord('a'))
        elif 'A' <= temp <= 'Z':
            temp = chr(((ord(temp) + key - ord('A')) % 26) + ord('A'))
        encrypted_data += temp
    print("\nEncrypted Message:", encrypted_data)


# Function for Caesar Cipher decryption
def caesar_cipher_decryption():
    global data, key
    decrypted_data = ""
    for count in range(len(data)):
        temp = data[count]
        if 'a' <= temp <= 'z':
            temp = chr(((ord(temp) - key - ord('a')) % 26) + ord('a'))
        elif 'A' <= temp <= 'Z':
            temp = chr(((ord(temp) - key - ord('A')) % 26) + ord('A'))
        decrypted_data += temp
    print("\nDecrypted Message:", decrypted_data)


# Function for input in Caesar Cipher
def cc_getmessage():
    global data
    data = input("Enter a String: ")


# Function for key input in Caesar Cipher
def cc_key_input():
    global key
    key = int(input("Enter a Key: "))


# Function for Railfence Cipher encryption
def rail_encryption(plain_text, symkey):
    msg_len = len(plain_text)
    rail_matrix = [['*' for _ in range(msg_len)] for _ in range(symkey)]
    row, coloumn, y = 0, 0, -1

    for i in range(msg_len):
        rail_matrix[row][coloumn] = plain_text[i]
        if row == 0 or row == symkey - 1:
            y = y * (-1)
        row = row + y
        coloumn += 1

    print("\nEncrypted Message:", end=" ")
    for i in range(symkey):
        for j in range(msg_len):
            if rail_matrix[i][j] != '*':
                print(rail_matrix[i][j], end="")


# Function for Railfence Cipher decryption
def rail_decryption(cipher_text, symkey):
    mes_len = len(cipher_text)
    rail_matrix = [['@' for _ in range(mes_len)] for _ in range(symkey)]
    row, coloumn, y, m = 0, 0, -1, 0

    for i in range(mes_len):
        rail_matrix[row][coloumn] = '#'
        if row == 0 or row == symkey - 1:
            y = y * (-1)
        row = row + y

    for i in range(symkey):
        for j in range(mes_len):
            if rail_matrix[i][j] == '#':
                rail_matrix[i][j] = cipher_text[m]
                m += 1
        row = coloumn = 0
        y = -1

    print("\nDecrypted Message:", end=" ")
    for i in range(mes_len):
        print(rail_matrix[row][coloumn], end="")
        if row == 0 or row == symkey - 1:
            y = y * (-1)
        row = row + y
        coloumn += 1


# Function for Railfence Cipher key and message input
def hill_getKeyMessage():
    global a, c, mes
    print("Enter 3x3 matrix for key (It should be invertible):")
    for i in range(3):
        for j in range(3):
            a[i][j] = float(input())
            c[i][j] = a[i][j]

    msg = input("Enter a 3-letter string: ")
    for i in range(3):
        mes[i][0] = ord(msg[i]) - 97


# Function for Railfence Cipher key and message input
def myfair():
    global txt, ct
    print("~PLAY_FAIR_CIPHER~")
    print("Enter Plain Text:")
    txt = input()
    size = len(txt)
    txt = txt.replace(" ", "")

    count = 0
    for i in range(size):
        if txt[i] != '*':
            txt = txt[:count] + txt[i] + txt[count:]
            count += 1

    size = len(txt)
    if size % 2 != 0:
        txt += 'x'

    print("Plain Text After Removing the space:", txt)
    print("Message for Encryption is:", end=" ")
    for i in range(size):
        print(txt[i], end="")
        if i % 2 != 0:
            print(" ", end="")
    choice_fill()


# Function for Railfence Cipher key and message input
def choice_fill():
    global ct
    flag = 0
    while True:
        print("\nPress 1 for Encryption")
        print("Press 2 for Decryption")
        print("Press 0 for exit")
        choice = int(input())
        if choice == 1:
            encryption_pf(txt)
            flag = 1
        elif choice == 2:
            if flag == 1:
                decryption_pf(ct)
            else:
                print("First Perform Encryption")
        elif choice == 0:
            return
        else:
            print("\nPlease enter a valid choice")


if __name__ == "__main__":
    print("\tSYMMETRIC ENCRYPTION AND DECRYPTION")
    print("\t1. PRESS 1 FOR HILL CIPHER")
    print("\t2. PRESS 2 FOR RAILFENCE")
    print("\t3. PRESS 3 FOR CAESAR CIPHER")
    print("\t4. PRESS 4 FOR PLAY FAIR")

    choice = int(input())
    
    if choice == 1:
        print("HILL CIPHER")
        hill_getKeyMessage()
        hill_encryption()
        hill_decryption()
    elif choice == 2:
        print("RAILFENCE CIPHER")
        plain_text = input("Enter the plain_text text: ")
        symkey = int(input("Enter the symkey (<length(plain_text)): "))
        print(f"Original Message: {plain_text}")
        rail_encryption(plain_text, symkey)
        cipher_text = input("Enter the cipher text: ")
        rail_decryption(cipher_text, symkey)
    elif choice == 3:
        print("CAESAR CIPHER")
        cc_getmessage()
        cc_key_input()
        while True:
            print("\n1. Encryption")
            print("2. Decryption")
            print("3. Exit")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                caesar_cipher_encryption()
            elif choice == 2:
                caesar_cipher_decryption()
            elif choice == 3:
                break
            else:
                print("\nPlease select a correct option:")
    elif choice == 4:
        myfair()
    else:
        print("\nPlease select a correct option")
