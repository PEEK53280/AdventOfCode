import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from loader import GetData
aufgabe = GetData()

def parse_zeile(zeile):
    ziel = [1 if c == '#' else 0 for c in zeile[zeile.index('[')+1:zeile.index(']')]]
    knoepfe = [list(map(int, zeile[i+1:zeile.index(')', i)].split(',')))
               for i in range(len(zeile)) if zeile[i] == '(']
    return ziel, knoepfe

def parse_joltage(zeile):
    s, e = zeile.rfind('{'), zeile.rfind('}')
    return list(map(int, zeile[s+1:e].split(','))) if s != -1 else []

def finde_minimale_druecke_toggle(ziel, knoepfe):
    n_lichter, n_knoepfe = len(ziel), len(knoepfe)
    beste = float('inf')
    for maske in range(1 << n_knoepfe):
        zustand = [0] * n_lichter
        for i, k in enumerate(knoepfe):
            if maske & (1 << i):
                for idx in k:
                    if idx < n_lichter:
                        zustand[idx] ^= 1
        if zustand == ziel:
            beste = min(beste, maske.bit_count())
    return beste if beste != float('inf') else 0

def finde_minimale_druecke_joltage(ziel_joltage, knoepfe):
    n_zaehler, n_knoepfe = len(ziel_joltage), len(knoepfe)
    matrix = np.zeros((n_zaehler, n_knoepfe))
    for i, z in enumerate(knoepfe):
        matrix[[j for j in z if j < n_zaehler], i] = 1
    result = milp(c=np.ones(n_knoepfe), constraints=LinearConstraint(matrix, ziel_joltage, ziel_joltage),
                  bounds=Bounds(0, np.inf), integrality=np.ones(n_knoepfe))
    return int(np.sum(result.x)) if result.success else 0

def main():
    ergebnisse = [(parse_zeile(z), parse_joltage(z)) for z in aufgabe.zeilen if z.strip()]
    aufgabe.loesung1 = sum(finde_minimale_druecke_toggle(ziel, knoepfe) for (ziel, knoepfe), _ in ergebnisse)
    aufgabe.loesung2 = sum(finde_minimale_druecke_joltage(joltage, knoepfe) for (_, knoepfe), joltage in ergebnisse)
    return aufgabe

if __name__ == "__main__":
    main().final()