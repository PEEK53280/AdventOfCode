import inspect
from pathlib import Path
from datetime import date
import time

class GetData:
    def __init__(self):
        self.caller = self._caller()
        self.jahr, self.tag = self._split()
        self.datum = self._datum()
        self.zeilen = self._laden()
        self.text = self._volltext()
        self.hallo = f"Advent of Code {self.jahr} - Tag {self.tag}"
        self.startzeit = time.perf_counter()
        print(self.hallo)

    @staticmethod
    def _caller():
        return inspect.stack()[2].filename

    def _split(self):
        return Path(self.caller).stem.split("_")

    def _laden(self):
        with open(f"../data/AoC_{self.jahr}.{self.tag}", 'r') as datei:
            return [zeile for zeile in datei]

    def _volltext(self):
        return "\n".join(self.zeilen)

    def _datum(self):
        return date(int(self.jahr), 12, int(self.tag))

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def __getattr__(self, name):
        super().__setattr__(name, 0)
        return 0

    def __str__(self):
        def get_loesung(name):
            return str(getattr(self, name)) if name in self.__dict__ else "nicht gelöst"
        return f"Lösung Aufgabe 1: {get_loesung('loesung1')}\nLösung Aufgabe 2: {get_loesung('loesung2')}\n"

    def final(self):
        print(self, f"Dauer: {(time.perf_counter() - self.startzeit):.4f} Sekunden")