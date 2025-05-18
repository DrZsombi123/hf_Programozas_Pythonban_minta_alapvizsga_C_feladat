konyvek = []
with open("konyvek-adatok.txt", "r", encoding="utf-8") as file:
    next(file) 
    for sor in file:
        adat = sor.strip().split(";")
        adat[2] = int(adat[2])
        adat[3] = int(adat[3])
        adat[4] = int(adat[4])
        konyvek.append(adat)

print(f"A listában {len(konyvek)} db könyv található!")

mufaj=input("Írj be egy műfajt: ")
szamlalo=0
oldalszama=0
for konyv in konyvek:
    if konyv[1]==mufaj:
        szamlalo+=1
        oldalszama+=konyv[2]
print(f"{szamlalo} db könyv tartozik ebbe a műfajba és oldalszáma:{oldalszama}")
talalat=False
for konyv in konyvek:
    ev = int(konyv[3])
    if 1699>= ev>=1600 and konyv[1]=="színmű":
        talalat=True
if talalat:
    print("1600 és 1699 között van színmű műfajban írt könyv")
else:
    print("1600 és 1699 között nincs színmű műfajban írt könyv")

def hossz(oldalszam):
    if oldalszam<200:
        return "rövid"
    elif oldalszam >=600:
        return "hosszú"
    else:
        return "közepes"

with open("negyezer-export.txt", "w", encoding="UTF-8") as f:
    for konyv in konyvek:
        if konyv[-1]==4000:
            f.write(f"{konyv[0]} ({hossz(konyv[2])})\n")
