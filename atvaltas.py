mertekegyseg=input("Milyen mértékegységben adod meg:")
szam=int(input("Írd be az átváltandó számot:"))
if mertekegyseg=="MB":
    print(f"Az eredmény:{szam/1024} GB")
elif mertekegyseg=="GB":
    print(f"Az eredmény:{szam*1024} MB")