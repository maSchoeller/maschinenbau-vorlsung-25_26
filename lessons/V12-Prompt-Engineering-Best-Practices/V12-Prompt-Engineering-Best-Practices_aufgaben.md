# V12: Übungsaufgaben - Prompt Engineering & Imports

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V12.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Prompt-Anatomie analysieren (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Analysiere den folgenden Prompt und identifiziere die vier Kernkomponenten (Kontext, Aufgabe, Format, Constraints):

```
Du bist ein erfahrener Python-Entwickler. Erstelle eine Funktion zur 
Berechnung der Fakultät einer Zahl. Die Funktion soll Type Hints haben, 
einen Docstring im Google Style enthalten und rekursiv implementiert 
sein. Maximale Länge: 15 Zeilen.
```

**Fragen**:
1. Was ist der Kontext in diesem Prompt?
2. Was ist die konkrete Aufgabe?
3. Welches Format wird verlangt?
4. Welche Constraints sind definiert?

**Hinweise**:
- Überlege, welche Informationen dem Modell Hintergrund liefern
- Identifiziere die Aktion, die ausgeführt werden soll
- Achte auf strukturelle Anforderungen
- Finde alle Einschränkungen und Regeln

---

### Aufgabe T2: Prompt-Verbesserung (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Verbessere den folgenden vagen Prompt systematisch, indem du alle vier Komponenten ergänzt:

**Ursprünglicher Prompt**:
```
Erkläre Sortieralgorithmen.
```

**Aufgaben**:
1. Füge einen klaren Kontext hinzu (z.B. Rolle, Zielgruppe)
2. Präzisiere die Aufgabe
3. Definiere ein konkretes Format
4. Setze sinnvolle Constraints

Schreibe den verbesserten Prompt und erkläre kurz, warum jede Änderung den Prompt verbessert.

**Hinweise**:
- Denke an die SMART-Kriterien: Spezifisch, Messbar, Erreichbar, Relevant, Terminiert
- Berücksichtige verschiedene Lerntypen (visuell, textuell)
- Überlege, welche Informationen ein LLM benötigt, um präzise zu antworten

---

### Aufgabe T3: Few-Shot Learning Design (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Entwerfe einen Few-Shot-Prompt für folgende Aufgabe:

**Ziel**: Ein LLM soll aus Kunden-Reviews automatisch extrahieren:
- Sentiment (positiv/neutral/negativ)
- Hauptthema (Produkt/Lieferung/Service/Preis)
- Handlungsempfehlung (keine/Antworten/Eskalieren)

**Aufgaben**:
1. Erstelle 3 repräsentative Beispiele (Few-Shot)
2. Jedes Beispiel sollte ein anderes Sentiment haben
3. Jedes Beispiel sollte alle drei Informationen demonstrieren
4. Formuliere den vollständigen Prompt mit Kontext, Aufgabe, Format und Constraints
5. Begründe kurz, warum du diese Beispiele gewählt hast

**Hinweise**:
- Beispiele sollten realistisch sein
- Decke verschiedene Edge Cases ab (z.B. gemischtes Sentiment)
- Achte auf konsistente Formatierung der Beispiele
- Überlege, welche Beispiele dem Modell helfen, die Aufgabe zu verallgemeinern

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Erstes eigenes Modul (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Module, Funktionen

Erstelle ein Modul `greetings.py` mit folgenden Funktionen:

1. `begruessung(name: str) -> str`: Gibt "Hallo, [name]!" zurück
2. `verabschiedung(name: str) -> str`: Gibt "Tschüss, [name]!" zurück
3. `formelle_begruessung(titel: str, nachname: str) -> str`: Gibt "Guten Tag, [titel] [nachname]" zurück

**Anforderungen**:
- Jede Funktion hat Type Hints
- Jede Funktion hat einen einzeiligen Docstring
- Das Modul hat einen Modul-Docstring

Erstelle dann eine `main.py`, die das Modul importiert und alle Funktionen testet.

**Beispiel Ein-/Ausgabe**:
```python
# main.py
import greetings

print(greetings.begruessung("Anna"))  # "Hallo, Anna!"
print(greetings.formelle_begruessung("Dr.", "Müller"))  # "Guten Tag, Dr. Müller"
```

**Hinweise**:
- Modul-Docstring steht an erster Stelle in der Datei
- Verwende f-Strings für String-Formatierung

---

### Aufgabe P2: `if __name__ == "__main__":` anwenden (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Module, `if __name__`

Erstelle ein Modul `calculator.py` mit grundlegenden Rechenoperationen:

**Funktionen**:
- `addiere(a: float, b: float) -> float`
- `subtrahiere(a: float, b: float) -> float`
- `multipliziere(a: float, b: float) -> float`
- `dividiere(a: float, b: float) -> float`  (mit ZeroDivisionError-Behandlung)

**Anforderungen**:
1. Jede Funktion hat Type Hints und Docstrings
2. Im `if __name__ == "__main__":`-Block:
   - Implementiere eine einfache Benutzerinteraktion
   - Lese zwei Zahlen vom Benutzer ein
   - Lese eine Operation ein (+, -, *, /)
   - Führe die Operation aus und gib das Ergebnis aus
3. Das Modul soll sowohl als Skript als auch als Bibliothek nutzbar sein

**Beispiel Ausführung als Skript**:
```bash
$ python calculator.py
Erste Zahl: 10
Zweite Zahl: 5
Operation (+, -, *, /): *
Ergebnis: 50.0
```

**Beispiel Import als Modul**:
```python
from calculator import multipliziere
print(multipliziere(10, 5))  # 50.0
```

---

### Aufgabe P3: Package-Struktur aufbauen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: Packages, `__init__.py`

Erstelle ein Package `text_tools` mit folgender Struktur:

```
text_tools/
├── __init__.py
├── formatters.py
└── validators.py
```

**`formatters.py`**:
- `upper_first(text: str) -> str`: Macht ersten Buchstaben groß
- `snake_case(text: str) -> str`: Konvertiert zu snake_case (z.B. "Hello World" → "hello_world")

**`validators.py`**:
- `ist_email_gueltig(email: str) -> bool`: Prüft einfache E-Mail-Validierung (enthält @, hat Text davor/danach)
- `ist_passwort_sicher(passwort: str) -> bool`: Mindestens 8 Zeichen, mindestens ein Großbuchstabe, eine Zahl

**`__init__.py`**:
- Importiere alle Funktionen, sodass sie direkt aus `text_tools` importiert werden können

**Hauptprogramm `main.py`**:
- Teste alle Funktionen

**Beispiel Ein-/Ausgabe**:
```python
from text_tools import upper_first, ist_email_gueltig

print(upper_first("hallo"))  # "Hallo"
print(ist_email_gueltig("test@example.com"))  # True
```

**Hinweise**:
- Snake-Case-Konvertierung: Leerzeichen durch Unterstriche ersetzen, alles lowercase
- E-Mail-Validierung: Einfache Prüfung reicht (kein Regex nötig)

---

### Aufgabe P4: Relative und absolute Imports (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Packages, relative Imports

Erstelle eine Package-Hierarchie für eine kleine Datenverarbeitungs-Bibliothek:

**Struktur**:
```
data_processing/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── reader.py
│   └── writer.py
└── utils/
    ├── __init__.py
    ├── validators.py
    └── transformers.py
```

**Implementierung**:

**`core/reader.py`**:
- `lese_zeilen(dateiname: str) -> list[str]`: Liest Datei zeilenweise

**`core/writer.py`**:
- `schreibe_zeilen(dateiname: str, zeilen: list[str]) -> None`: Schreibt Zeilen in Datei

**`utils/validators.py`**:
- `ist_nicht_leer(zeile: str) -> bool`: Prüft, ob Zeile nicht leer ist

**`utils/transformers.py`**:
- Importiere `ist_nicht_leer` aus `validators.py` mit **relativem Import**
- `filtere_leere_zeilen(zeilen: list[str]) -> list[str]`: Filtert leere Zeilen mit `ist_nicht_leer`
- `zu_grossbuchstaben(zeilen: list[str]) -> list[str]`: Konvertiert alle Zeilen zu Großbuchstaben

**Hauptprogramm `main.py`**:
- Nutze **absolute Imports** aus dem Package
- Lese eine Testdatei ein
- Filtere leere Zeilen
- Konvertiere zu Großbuchstaben
- Schreibe in neue Datei

**Anforderungen**:
1. `transformers.py` nutzt relative Imports für `validators.py`
2. `main.py` nutzt absolute Imports
3. Alle Funktionen haben Type Hints und Docstrings
4. Implementiere Error Handling (FileNotFoundError)

**Hinweise**:
- Relativer Import: `from .validators import ist_nicht_leer`
- Absoluter Import: `from data_processing.core.reader import lese_zeilen`

---

### Aufgabe P5: Modul mit venv und Dependencies (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: venv, pip, Module, Error Handling

Erstelle ein kleines Projekt, das externe Dependencies nutzt und sauber strukturiert ist.

**Projekt: Wetter-CLI-Tool**

**Ziel**: Ein Kommandozeilen-Tool, das Wetterdaten von einer API abruft und formatiert ausgibt.

**Anforderungen**:

**1. Projekt-Struktur**:
```
weather_cli/
├── venv/  (gitignored)
├── weather_cli/
│   ├── __init__.py
│   ├── api.py
│   ├── formatter.py
│   └── cli.py
├── tests/
│   ├── __init__.py
│   └── test_formatter.py
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

**2. Implementierung**:

**`weather_cli/api.py`**:
- Nutze die Library `requests` (muss via pip installiert werden)
- Funktion `hole_wetter(stadt: str) -> dict`: Simuliere API-Call (gibt Mock-Daten zurück, kein echter API-Key nötig)
- Mock-Daten Format: `{"stadt": stadt, "temperatur": 20, "bedingungen": "Sonnig"}`

**`weather_cli/formatter.py`**:
- Funktion `formatiere_wetter(wetter: dict) -> str`: Formatiert Wetter-Dict als lesbaren Text

**`weather_cli/cli.py`**:
- Funktion `main()`: Hauptlogik für CLI
- Nutze `argparse` für Kommandozeilen-Argumente
- Argument: `--stadt` (erforderlich)

**`main.py`**:
- Einstiegspunkt: Ruft `cli.main()` auf mit `if __name__ == "__main__":`

**`requirements.txt`**:
- Liste alle Dependencies (requests, etc.)

**`.gitignore`**:
- `venv/`, `__pycache__/`, `*.pyc`

**`README.md`**:
- Setup-Anweisungen (venv erstellen, dependencies installieren, Nutzung)

**3. Schritte**:
1. Erstelle virtuelle Umgebung: `python -m venv venv`
2. Aktiviere venv
3. Installiere `requests`: `pip install requests`
4. Exportiere Dependencies: `pip freeze > requirements.txt`
5. Implementiere alle Module
6. Teste: `python main.py --stadt Berlin`

**Beispiel Ein-/Ausgabe**:
```bash
$ python main.py --stadt Berlin
Wetter in Berlin:
Temperatur: 20°C
Bedingungen: Sonnig
```

**Bonus-Challenge**:
- Implementiere Unit-Tests für `formatter.py` in `tests/test_formatter.py`
- Nutze `pytest` (weitere Dependency)

**Hinweise**:
- Für Mock-API: Einfach ein Dictionary zurückgeben, kein echter API-Call
- `argparse` ist Teil der Standard Library
- Vergiss nicht, `__init__.py` in allen Package-Verzeichnissen zu erstellen
