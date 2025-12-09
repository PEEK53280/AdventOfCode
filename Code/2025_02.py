from loader import GetData
aufgabe = GetData()

def werte_generieren():
    return (str(wert) for element in aufgabe.text.split(",") for start, ende in [map(int, element.split("-"))] for wert in range(start, ende + 1))

def aufgabe1(data):
    if len(data) % 2 == 0:
        aufgabe.loesung1 += int(data) if data[:len(data) // 2] == data[len(data) // 2:] else 0

def aufgabe2(data):
    for anzahl in range(2, len(data) + 1):
        if len(data) % anzahl != 0:
            continue
        laenge = len(data) // anzahl
        if data[:laenge] * anzahl == data:
            aufgabe.loesung2 += int(data)
            break

def main():
    for wert in werte_generieren():
        aufgabe1(wert)
        aufgabe2(wert)
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()