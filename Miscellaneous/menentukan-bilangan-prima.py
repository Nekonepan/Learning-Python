counter = 0
bilangan = int(input("Masukkan bilangan : "))

for i in range (1, bilangan + 1):
  if (bilangan / i == 0):
    counter += 1

if (counter == 2):
  print(f"Bilangan {bilangan} adalah prima")
else:
  print(f"Bilangan {bilangan} bukan prima")