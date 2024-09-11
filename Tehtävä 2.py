nimet = set()
while True:
    nimi = input("Anna nimi:")

    if nimi == "":
        break

    if nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")

print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)




