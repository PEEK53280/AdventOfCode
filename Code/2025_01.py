from loader import GetData
aufgabe = GetData()

def main():
    position = 50
    for zeile in aufgabe.zeilen:
        richtung, runden, distanz = zeile[0], *divmod(int(zeile[1:]), 100)
        if richtung == "L":
            runden += int(distanz >= position > 0)
            position = (position - distanz) % 100
        else:
            runden += int(distanz >= 100 - position)
            position = (position + distanz) % 100
        aufgabe.loesung1 += int(position == 0)
        aufgabe.loesung2 += runden
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()