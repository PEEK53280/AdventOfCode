from loader import GetData
aufgabe = GetData()

def main():
    positionen = {aufgabe.zeilen[0].index("S"): 1}
    for zeile in aufgabe.zeilen[1:]:
        if zeile.count(".") == len(zeile):
            continue
        neue_positionen = {}
        for position, anzahl in positionen.items():
            if zeile[position] == ".":
                neue_positionen[position] = neue_positionen.get(position, 0) + anzahl
            else:
                neue_positionen[position-1] = neue_positionen.get(position-1, 0) + anzahl
                neue_positionen[position+1] = neue_positionen.get(position+1, 0) + anzahl
                aufgabe.loesung1 += 1
        positionen = neue_positionen
    aufgabe.loesung2 = sum(positionen.values())
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()
