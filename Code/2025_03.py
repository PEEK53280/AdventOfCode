from loader import GetData
aufgabe = GetData()

def solver(bank:str, batterien:int)->int:
    auswahl = ""
    for i in range(1, batterien):
        batterie = max(bank[:-(batterien - i)])
        bank = bank.split(batterie, 1)[1]
        auswahl += batterie
    return int(auswahl+max(bank))

def main():
    for speicher in aufgabe.zeilen:
        aufgabe.loesung1 += solver(bank=speicher, batterien=2)
        aufgabe.loesung2 += solver(bank=speicher, batterien=12)
    aufgabe.final()

if __name__ == "__main__":
    main()
