import itertools
from loader import GetData
aufgabe = GetData()

def finde(eltern, i):
    if eltern[i] != i:
        eltern[i] = finde(eltern, eltern[i])
    return eltern[i]

def union(eltern, rang, i, j):
    ri, rj = finde(eltern, i), finde(eltern, j)
    if ri != rj:
        if rang[ri] < rang[rj]:
            eltern[ri] = rj
        else:
            eltern[rj] = ri
            if rang[ri] == rang[rj]:
                rang[ri] += 1
        return True  # Verbindung war erfolgreich
    return False  # Waren schon verbunden

def zaehle_circuits(eltern, n):
    """Zählt die Anzahl der verschiedenen Circuits"""
    wurzeln = set()
    for i in range(n):
        wurzeln.add(finde(eltern, i))
    return len(wurzeln)

def main():
    dosen = [[int(x) for x in dose.strip().split(",")] for dose in aufgabe.zeilen]
    distanzen = sorted([(sum((a - b) ** 2 for a, b in zip(dose1, dose2)), idx1, idx2, dose1[0], dose2[0])
                        for (idx1, dose1), (idx2, dose2) in itertools.combinations(enumerate(dosen), 2)])

    n = len(dosen)
    eltern = list(range(n))
    rang = [0] * n

    for distanz, idx1, idx2, x1, x2 in distanzen[:1000]:
        union(eltern, rang, idx1, idx2)
    netzwerke = {}
    for i in range(n):
        wurzel = finde(eltern, i)
        netzwerke.setdefault(wurzel, []).append(i)
    sortiert = sorted(netzwerke.values(), key=len, reverse=True)
    aufgabe.loesung1 = len(sortiert[0]) * len(sortiert[1]) * len(sortiert[2])

    for distanz, idx1, idx2, x1, x2 in distanzen[1000:]:
        if union(eltern, rang, idx1, idx2):
            if zaehle_circuits(eltern, n) == 1:
                aufgabe.loesung2 = x1 * x2
                break
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()