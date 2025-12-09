from loader import GetData
aufgabe = GetData()

def eingabe_parsen():
    frisch = set()
    zutaten = set()
    for zeile in aufgabe.zeilen:
        zeile=zeile.strip()
        if "-" in zeile:
            start, ende = map(int, zeile.split("-"))
            frisch.add((start, ende))
            continue
        if zeile == "":
            continue
        zutaten.add(int(zeile))
    aufgabe.frisch = sorted(frisch)
    aufgabe.zutaten = sorted(zutaten)

def kumuliere_frische_bereiche():
    bereiche = []
    aktuelle_start, aktuelles_ende = aufgabe.frisch[0]
    for i, (start, ende) in enumerate(aufgabe.frisch[1:]):
        if start <= aktuelles_ende + 1:
            aktuelles_ende = max(aktuelles_ende, ende)
        else:
            bereiche.append((aktuelle_start, aktuelles_ende))
            aktuelle_start, aktuelles_ende = start, ende
    bereiche.append((aktuelle_start, aktuelles_ende))
    aufgabe.frisch = bereiche

def aufgabe1():
    for zutat in aufgabe.zutaten:
        for start, ende in aufgabe.frisch:
            if start <= zutat <= ende:
                aufgabe.loesung1 += 1
                break

def aufgabe2():
    for start, ende in aufgabe.frisch:
        aufgabe.loesung2 += (ende - start + 1)

def main():
    eingabe_parsen()
    kumuliere_frische_bereiche()
    aufgabe1()
    aufgabe2()
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()