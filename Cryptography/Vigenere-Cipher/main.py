class Vigenere:
  def __init__(self, key):
    self.key = ''.join([c.upper() for c in key if c.isalpha()])

  def encrypt(self, text):
    out = ""
    j = 0
    for c in text:
      if c.isalpha():
        c = c.upper()
        out += chr(((ord(c) + ord(self.key[j]) - 2 * ord('A')) % 26) + ord('A'))

        j = (j + 1) % len(self.key)
      else:
        out += c
    return out;

  def decrypt(self, text):
    out = ""
    j = 0
    for c in text:
      if c.isalpha():
        c = c.upper()
        out += chr(((ord(c) - ord(self.key[j]) + 26) % 26) + ord('A'))
        j = (j + 1) % len(self.key)
      else:
        out += c
    return out

if __name__ == "__main__":
  cipher = Vigenere("LELAH")
  original = "UDAH DIEM DI RUMAH AJA NGGAK USAH KEMANA MANA"
  encrypted = cipher.encrypt(original)
  decrypted = cipher.decrypt(encrypted)
  print("Encrypted = ", encrypted)
  print("Decrypted = ", decrypted)