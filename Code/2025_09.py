import itertools
import shapely
from loader import GetData
aufgabe = GetData()

def main():
    punkte = [tuple(map(int, zeile.strip().split(','))) for zeile in aufgabe.zeilen]
    poly = shapely.Polygon(punkte)
    for (x1, y1), (x2, y2) in itertools.combinations(punkte, 2):
        fläche = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        aufgabe.loesung1 = max(aufgabe.loesung1, fläche)
        rect = shapely.box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        aufgabe.loesung2 = max(aufgabe.loesung2, fläche) if poly.contains(rect) else aufgabe.loesung2
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()