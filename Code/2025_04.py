from loader import GetData
aufgabe = GetData()

def horizontaler_zaehler(karte:list) -> list:
    reihen = [[0] * len(aufgabe.zeilen[0])]
    for zeile in karte:
        reihe = []
        for i, element in enumerate(zeile):
            horizontale_rollen = 1 if i > 0 and zeile[i - 1] == "@" else 0
            horizontale_rollen += 1 if i < len(zeile) - 1 and zeile[i + 1] == "@" else 0
            horizontale_rollen = -(horizontale_rollen + 1) if element == "@" else horizontale_rollen
            reihe.append(horizontale_rollen)
        reihen.append(reihe)
    reihen.append([0] * len(aufgabe.zeilen[0]))
    return reihen

def vertikaler_zaehler(karte:list) -> list:
    neue_reihen = []
    zaehler = 0
    for i, reihe in enumerate(karte):
        if i == 0 or i == len(karte) - 1:
            continue
        neue_reihe = ""
        for element, vor, nach in zip(reihe, karte[i - 1], karte[i + 1]):
            if element >= 0:
                neue_reihe += "."
                continue
            rollen = abs(element) - 1 + abs(vor) + abs(nach)
            if rollen >= 4:
                neue_reihe += "@"
                continue
            neue_reihe += "."
            zaehler += 1
        neue_reihen.append(neue_reihe)
    aufgabe.zaehler = zaehler
    return neue_reihen


def main():
    karte = aufgabe.zeilen
    i=0
    while i==0 or aufgabe.zaehler > 0:
        i+=1
        karte_mit_zahlen = horizontaler_zaehler(karte)
        karte = vertikaler_zaehler(karte_mit_zahlen)
        aufgabe.loesung2 += aufgabe.zaehler
        if i == 1:
            aufgabe.loesung1 = aufgabe.zaehler
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()