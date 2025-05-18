osszpenz=int(input("Írd be, hogy mennyi pénzed van:"))
while osszpenz!=0:
    koltenivaló=int(input("Mennyit szeretnél költeni belőle:"))
    if koltenivaló> osszpenz:
        print("Ennyit nem költhetsz, nincs ennyi pénzed!")
    else:
        print(f"Ennyi pénzed maradt: {osszpenz-koltenivaló}")
        osszpenz=osszpenz-koltenivaló
