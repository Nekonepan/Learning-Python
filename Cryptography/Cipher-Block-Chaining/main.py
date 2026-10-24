BLOCK_SIZE = 8

def xor_block(data, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(data, key))

def encrypt_block(block, key):
    return xor_block(block, key)

# ------------------------------
plaintext = "UNIVERSITAS"
key = "password"
iv = "11111111"

# Padding
while len(plaintext) % BLOCK_SIZE != 0:
    plaintext += " "

ciphertext = []
previous = iv

print("===== ENKRIPSI CBC =====")

for i in range(0, len(plaintext), BLOCK_SIZE):
    block = plaintext[i:i+BLOCK_SIZE]
    key_block = key[:BLOCK_SIZE]
    print(f"\n===== BLOK {(i // BLOCK_SIZE) + 1} =====")
    print("Plaintext :", block)

    # Blok pertama menggunakan IV
    if i == 0:
        print("IV :", previous)
    else:
        print("Cipher Sebelumnya :", previous.encode())

    print("Key :", key_block)

    # XOR Plaintext dengan IV/Cipher Sebelumnya
    xored = xor_block(block, previous)
    print("Hasil XOR :", xored.encode())

    # Enkripsi
    encrypted = encrypt_block(xored, key_block)
    print("Cipher Block :", encrypted.encode())
    ciphertext.append(encrypted)

    # Cipher block menjadi previous block berikutnya
    previous = encrypted