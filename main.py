import shutil
import sys
import importlib.util
from pathlib import Path
import urllib.request

JAHR = 2025
MAX_TAGE = 12
CODE_VERZEICHNIS = Path("Code")
DATEN_VERZEICHNIS = Path("data")
TEMPLATE_DATEI = Path("_template.py")


def hole_existierende_tage():
    """Gibt eine sortierte Liste der existierenden Tag-Nummern zurück"""
    tage = []
    for datei in CODE_VERZEICHNIS.glob(f"{JAHR}_*.py"):
        tag_str = datei.stem.split("_")[1]
        try:
            tage.append(int(tag_str))
        except ValueError:
            continue
    return sorted(tage)


def naechster_tag():
    """Gibt die Nummer des nächsten Tags zurück (1-12) oder None wenn alle existieren"""
    existierende = hole_existierende_tage()
    for tag in range(1, MAX_TAGE + 1):
        if tag not in existierende:
            return tag
    return None


def lade_puzzle_daten(tag_nummer):
    """Lädt die Puzzle-Daten von adventofcode.com"""
    url = f"https://adventofcode.com/{JAHR}/day/{tag_nummer}/input"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            daten = response.read().decode('utf-8')
            return daten
    except Exception as e:
        print(f"⚠️  Fehler beim Laden der Daten: {e}")
        return None


def lege_tag_an(tag_nummer):
    """Legt einen neuen Tag an: Kopiert Template und lädt Puzzle-Daten"""
    tag_str = f"{tag_nummer:02d}"
    ziel_code = CODE_VERZEICHNIS / f"{JAHR}_{tag_str}.py"
    ziel_daten = DATEN_VERZEICHNIS / f"AoC_{JAHR}.{tag_str}"

    # Template kopieren
    if not TEMPLATE_DATEI.exists():
        print(f"❌ Template-Datei '{TEMPLATE_DATEI}' nicht gefunden!")
        return False

    try:
        shutil.copy(TEMPLATE_DATEI, ziel_code)
        print(f"✅ Code-Datei erstellt: {ziel_code}")
    except Exception as e:
        print(f"❌ Fehler beim Kopieren des Templates: {e}")
        return False

    # Puzzle-Daten von AoC laden
    print(f"📥 Lade Puzzle-Daten von adventofcode.com...")
    daten = lade_puzzle_daten(tag_nummer)

    if daten:
        try:
            ziel_daten.write_text(daten)
            print(f"✅ Datendatei erstellt und gefüllt: {ziel_daten}")
        except Exception as e:
            print(f"❌ Fehler beim Schreiben der Datendatei: {e}")
            return False
    else:
        # Fallback: Datei mit Hinweis erstellen
        try:
            hinweis = (
                f"# Puzzle-Daten konnten nicht automatisch geladen werden.\n"
                f"# Bitte füge die Daten manuell von folgender URL ein:\n"
                f"# https://adventofcode.com/{JAHR}/day/{tag_nummer}/input\n"
                f"#\n"
                f"# Lösche diese Kommentarzeilen und füge die Puzzle-Daten hier ein.\n"
            )
            ziel_daten.write_text(hinweis)
            print(f"✅ Datendatei mit Hinweis erstellt: {ziel_daten}")
            print(f"⚠️  Bitte füge die Daten von https://adventofcode.com/{JAHR}/day/{tag_nummer}/input manuell ein!")
        except Exception as e:
            print(f"❌ Fehler beim Erstellen der Datendatei: {e}")
            return False

    return True


def fuehre_tag_aus(tag_nummer):
    """Führt die main()-Funktion eines Tags aus"""
    tag_str = f"{tag_nummer:02d}"
    code_datei = CODE_VERZEICHNIS / f"{JAHR}_{tag_str}.py"

    if not code_datei.exists():
        print(f"❌ Tag {tag_str} existiert nicht!")
        return

    print(f"\n{'='*60}")
    print(f"  Tag {tag_str} - {JAHR}")
    print(f"{'='*60}\n")

    # Code-Verzeichnis zum Python-Path hinzufügen (für loader import)
    code_pfad = str(CODE_VERZEICHNIS.absolute())
    if code_pfad not in sys.path:
        sys.path.insert(0, code_pfad)

    # Absoluten Pfad VOR chdir berechnen!
    code_datei_absolut = code_datei.absolute()

    # Working Directory ins Code-Verzeichnis ändern (für relative Pfade in loader)
    import os
    urspruengliches_cwd = os.getcwd()
    os.chdir(CODE_VERZEICHNIS)

    try:
        # Modul dynamisch importieren und ausführen
        modul_name = f"{JAHR}_{tag_str}"
        spec = importlib.util.spec_from_file_location(modul_name, code_datei_absolut)
        modul = importlib.util.module_from_spec(spec)
        sys.modules[modul_name] = modul

        spec.loader.exec_module(modul)
        if hasattr(modul, 'main'):
            aufgabe = modul.main()
            if hasattr(aufgabe, 'final'):
                aufgabe.final()
    except Exception as e:
        print(f"❌ Fehler beim Ausführen von Tag {tag_str}: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Working Directory zurücksetzen
        os.chdir(urspruengliches_cwd)


def zeige_tage():
    """Zeigt alle existierenden Tage an (zweispaltig)"""
    tage = hole_existierende_tage()
    if not tage:
        print("❌ Noch keine Tage vorhanden!")
        return

    print(f"\n📅 Vorhandene Tage ({len(tage)}/{MAX_TAGE}):")
    for i in range(0, len(tage), 2):
        zeile = f"  • Tag {tage[i]:02d}"
        if i + 1 < len(tage):
            zeile += f"    • Tag {tage[i+1]:02d}"
        print(zeile)
    print()


def zeige_menu():
    """Zeigt das Hauptmenü und verarbeitet Eingaben"""
    while True:
        print("\n" + "="*60)
        print("  🎄 Advent of Code 2025 - Hauptmenü 🎄")
        print("="*60)

        zeige_tage()

        print("Optionen:")
        print("  • Gib eine Tag-Nummer ein (01-12) um den Tag auszuführen")
        print("  • ALLE - Alle Tage nacheinander ausführen")
        print("  • ANLEGEN - Neuen Tag anlegen")
        print("  • EXIT - Beenden")
        print()

        eingabe = input("Deine Wahl: ").strip().upper()

        if eingabe == "EXIT":
            print("Tschüss! 👋")
            break
        elif eingabe == "ALLE":
            tage = hole_existierende_tage()
            for tag in tage:
                fuehre_tag_aus(tag)
        elif eingabe == "ANLEGEN":
            naechster = naechster_tag()
            if naechster is None:
                print("✅ Alle 12 Tage sind bereits angelegt!")
            else:
                print(f"\n📝 Lege Tag {naechster:02d} an...")
                if lege_tag_an(naechster):
                    print(f"✅ Tag {naechster:02d} erfolgreich angelegt!")
        else:
            # Versuche als Tag-Nummer zu interpretieren
            try:
                tag = int(eingabe)
                if 1 <= tag <= MAX_TAGE:
                    fuehre_tag_aus(tag)
                else:
                    print(f"❌ Tag muss zwischen 01 und {MAX_TAGE} liegen!")
            except ValueError:
                print("❌ Ungültige Eingabe!")


def main():
    """Hauptfunktion"""
    print("\n🎄 Willkommen bei Advent of Code 2025! 🎄\n")

    # Prüfe ob Verzeichnisse existieren
    if not CODE_VERZEICHNIS.exists():
        print(f"❌ Code-Verzeichnis '{CODE_VERZEICHNIS}' nicht gefunden!")
        return
    if not DATEN_VERZEICHNIS.exists():
        print(f"❌ Daten-Verzeichnis '{DATEN_VERZEICHNIS}' nicht gefunden!")
        return

    # Prüfe ob nächster Tag angelegt werden soll
    naechster = naechster_tag()
    if naechster is not None:
        existierende = len(hole_existierende_tage())
        print(f"Du hast {existierende}/{MAX_TAGE} Tage angelegt.")
        antwort = input(f"Möchtest du Tag {naechster:02d} anlegen? (j/n): ").strip().lower()
        if antwort in ['j', 'ja', 'y', 'yes']:
            if lege_tag_an(naechster):
                print(f"✅ Tag {naechster:02d} erfolgreich angelegt!")
            print()

    # Zeige Menü
    zeige_menu()


if __name__ == "__main__":
    main()