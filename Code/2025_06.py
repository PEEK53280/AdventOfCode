from itertools import zip_longest
from math import prod
from loader import GetData
aufgabe = GetData()

def main():
    for rechnung in list(zip(*[zeile.split() for zeile in aufgabe.zeilen])):
        *operanden, operator = rechnung
        aufgabe.loesung1 += sum(map(int, operanden)) if operator == "+" else prod(map(int, operanden))

    faktoren = []
    for spalte in list(zip_longest(*[zeile for zeile in aufgabe.zeilen]))[:-1]:
        if all(zeichen == ' ' for zeichen in spalte):
            continue
        *operanden, operator = spalte
        operand = int(''.join(operand for operand in operanden))
        if operator in ("+", "*"):
            aufgabe.loesung2 += prod(faktoren)
            faktoren = []
            befehl = "addiere" if operator == "+" else "multipliziere"
        if befehl == "addiere":
            aufgabe.loesung2 += operand
        else:
            faktoren.append(operand)
    aufgabe.loesung2 += prod(faktoren)
    return aufgabe

if __name__ == "__main__":
    main().final()