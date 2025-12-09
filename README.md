# 🎄 Advent of Code 2025

Meine Lösungen für [Advent of Code 2025](https://adventofcode.com/2025)

## Was ist Advent of Code?

**Advent of Code** ist ein jährlicher Adventskalender mit Programmier-Rätseln von Eric Wastl. Vom 1. bis 25. Dezember wird täglich ein neues Puzzle veröffentlicht, das mit beliebigen Programmiersprachen gelöst werden kann.

🔗 **Website**: [adventofcode.com](https://adventofcode.com)

## Installation & Setup

### Voraussetzungen

- Python 3.9+
- pip

### Virtual Environment einrichten

```bash
# Virtual Environment erstellen
python -m venv .venv

# Virtual Environment aktivieren
# Linux/macOS:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# Dependencies installieren (falls vorhanden)
pip install -r requirements.txt  # optional, aktuell keine externen Abhängigkeiten
```

### Ohne Virtual Environment

Das Projekt verwendet nur die Python Standard Library, kann also auch ohne venv ausgeführt werden. Empfohlen wird jedoch die Verwendung einer venv.

## Projektstruktur

```
AoC/
├── main.py              # Hauptmenü zum Verwalten und Ausführen der Lösungen
├── _template.py         # Template für neue Tage
├── Code/
│   ├── loader.py        # Hilfsklasse zum Laden der Puzzle-Daten
│   ├── 2025_01.py       # Lösung für Tag 1
│   ├── 2025_02.py       # Lösung für Tag 2
│   └── ...
└── data/
    ├── AoC_2025.01      # Puzzle-Daten für Tag 1
    ├── AoC_2025.02      # Puzzle-Daten für Tag 2
    └── ...
```

## Verwendung

### Hauptmenü starten

```bash
python main.py
```

### Funktionen

Das Hauptmenü bietet folgende Optionen:

- **Tag ausführen**: Gib eine Tag-Nummer (01-12) ein, um die Lösung auszuführen
- **ALLE**: Führt alle vorhandenen Lösungen nacheinander aus
- **ANLEGEN**: Erstellt einen neuen Tag (kopiert Template + lädt Puzzle-Daten)
- **EXIT**: Beendet das Programm

### Neuen Tag anlegen

Beim Start oder über die Menüoption "ANLEGEN" wird:
1. Das Template nach `Code/2025_XX.py` kopiert
2. Versucht, die Puzzle-Daten automatisch zu laden
3. Bei Fehler eine Datei mit Hinweis erstellt

### Einzelne Lösung direkt ausführen

```bash
cd Code
python 2025_01.py
```

## Technische Details

- **Sprache**: Python 3
- **Konvention**: Alle Code-Elemente (Variablen, Funktionen, Kommentare) auf Deutsch
- **GetData-Klasse**: Zentrale Hilfsklasse in `loader.py` zum Laden und Verarbeiten der Puzzle-Daten

## Jahr 2025

Dieses Projekt enthält Lösungen für maximal 12 Tage im Jahr 2025.

---

⭐ Viel Spaß beim Rätseln! ⭐