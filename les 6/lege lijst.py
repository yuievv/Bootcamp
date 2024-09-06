getallen = []

for i in range(6):
    getal = int(input(f"Voer getal {i+1} in: "))
    getallen.append(getal)

getallen.sort()

print("De lijst is:")
print(getallen)