from loader import GetData
aufgabe = GetData()

def werte_generieren():
    aufgabe.werte = (str(wert) for element in aufgabe.text.split(",") for start, ende in [map(int, element.split("-"))] for wert in range(start, ende + 1))

def aufgabe1(data):
    aufgabe.loesung1 += int(data) if data[:len(data) // 2] == data[len(data) // 2:] else 0

def aufgabe2(data):
    for anzahl in range(2, len(data)+1):
        if len(data) % anzahl != 0:
            continue
        laenge = len(data) // anzahl
        if all(data[i * laenge:(i + 1) * laenge] == data[:laenge] for i in range(anzahl)):
            aufgabe.loesung2 += int(data)
            break

def main():
    werte_generieren()
    for wert in aufgabe.werte:
        if len(wert) %2 == 0:
            aufgabe1(wert)
        aufgabe2(wert)
    aufgabe.final()

if __name__ == "__main__":
    main()
