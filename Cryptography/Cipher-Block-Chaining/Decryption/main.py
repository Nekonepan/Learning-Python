BLOCK_SIZE = 8

def xor_block(data, key):
    # Pad key or data to the shorter length to avoid Zip truncation or errors
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(data, key))

def decrypt_block(block, key):
    return xor_block(block, key)

# ------------------------------
key = "pashword"
# Ensure IV matches the BLOCK_SIZE
iv = "11111111"

# Contoh ciphertext tiruan
plaintext = "UNIVERSITAS"
while len(plaintext) % BLOCK_SIZE != 0:
    plaintext += " "

ciphertext = []
previous = iv
for i in range(0, len(plaintext), BLOCK_SIZE):
    block = plaintext[i:i+BLOCK_SIZE]
    key_block = key[:BLOCK_SIZE]
    xored = xor_block(block, previous)
    encrypted = xor_block(xored, key_block)
    ciphertext.append(encrypted)
    previous = encrypted

# ------------------------------
print("===== DEKRIPSI CBC =====")
recovered_plaintext = ""
previous = iv

for i in range(0, len(ciphertext)):
    block = ciphertext[i]
    key_block = key[:BLOCK_SIZE]
    print(f"\n===== BLOK {i + 1} =====")
    print("Cipher Block :", block.encode('utf-8', errors='replace'))
    print("Key :", key_block)

    # 1. Dekripsi blok menggunakan Key
    decrypted = decrypt_block(block, key_block)
    print("Hasil Dekripsi :", decrypted.encode('utf-8', errors='replace'))

    # 2. XOR hasil dekripsi dengan IV (untuk blok 1) atau Cipher Sebelumnya
    original_block = xor_block(decrypted, previous)
    print("Plaintext :", original_block)
    recovered_plaintext += original_block

    # Cipher block saat ini menjadi previous untuk blok berikutnya
    previous = block

# Menghapus padding spasi di akhir jika ada
recovered_plaintext = recovered_plaintext.rstrip()
print("\n==========================")
print("Plaintext Asli :", recovered_plaintext)
