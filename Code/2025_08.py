from bisect import insort
import itertools
from loader import GetData
aufgabe = GetData()

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, i, j):
    ri, rj = find(parent, i), find(parent, j)
    if ri != rj:
        if rank[ri] < rank[rj]:
            parent[ri] = rj
        else:
            parent[rj] = ri
            if rank[ri] == rank[rj]:
                rank[ri] += 1

def baue_netzwerke(dosen, distanzen):
    n = len(dosen)
    parent = list(range(n))
    rank = [0] * n

    for idx1, idx2, _ in distanzen:
        union(parent, rank, idx1, idx2)

    netzwerke = {}
    for i in range(n):
        wurzel = find(parent, i)
        netzwerke.setdefault(wurzel, []).append(i)
    return list(netzwerke.values())

def main():
    dosen = [[int(x) for x in dose.strip().split(",")] for dose in aufgabe.zeilen]

    distanzen = []
    for (idx1, dose1), (idx2, dose2) in itertools.combinations(enumerate(dosen), 2):
        distanz = sum((a - b) ** 2 for a, b in zip(dose1, dose2))
        if len(distanzen) < 1000 or distanzen[-1][1]:
            insort(distanzen, [idx1, idx2, distanz], key=lambda x: x[2])
            (len(distanzen) > 1000) and distanzen.pop()

    netzwerke = baue_netzwerke(dosen, distanzen)
    netzwerke = sorted(netzwerke, key=len, reverse=True)
    for n in netzwerke:
        print(len(n))
#164475
    return aufgabe

if __name__ == "__main__":
    main()
    aufgabe.final()