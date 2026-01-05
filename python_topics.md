# Python Topics – Vorlesungs-Tracking

Diese Datei dient der **Konsistenz** über alle Vorlesungen hinweg: Welche **Python-Funktionen/Methoden/Module** wurden **wann** erstmals eingeführt?

## Regeln zur Pflege
- **Eintrag nur bei Erst-Einführung**: Wenn eine Funktion bereits existiert, wird sie nicht erneut eingetragen.
- Einträge möglichst **kanonisch** benennen:
  - Builtins: `print`, `len`, `range`
  - Modul-Funktionen: `math.sqrt`, `random.choice`, `pathlib.Path`
  - Methoden: `str.split`, `list.append`, `dict.get`
- Wenn bekannt: **Python-Version** angeben (z.B. „3.10+“).
- Wenn das Material als neue Vorlesung erzeugt wird: Vorlesungs-ID konsistent halten (z.B. `V01`, `V02`, …).

## Übersicht (Index)
| Vorlesung | Thema | Neu eingeführt (Auszug) |
|---|---|---|
| V01 | Python Get Started: Variablen, print, input | `print()`, `input()`, `int()`, `float()`, `str()`, `len()`, Variablen, Kommentare |
| V02 | Eingaben/Ausgaben & Formatierung | f-Strings, `.format()`, %-Operator, `print(sep, end, flush)`, Escape-Sequenzen, `open()`, `with`, Datei-I/O |
| V03 | Variablen Management & Datentypen | `type()`, `isinstance()`, `bool()`, `round()`, `id()`, `global`, `min()`, `max()`, Immutable vs. Mutable, Scope, Multiple Assignment |
| V04 | Logische Ausdrücke (Boolsche Algebra) | Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`), Logische Operatoren (`and`, `or`, `not`), Verkettete Vergleiche, Kurzschlussauswertung, Truthy/Falsy Values, `abs()`, `any()` (Vorschau) |
| V05 | Verzweigungen (if, if-elif-else) | `if`, `else`, `elif`, Ternärer Operator, `pass`, Einrückung als Syntax |
| V06 | Schleifen (for, while) – Teil 1 | `for`-Schleife, `while`-Schleife, `range()`, `enumerate()`, String-Iteration, Akkumulation, Zählen |
| V07 | Schleifen (for, while) – Teil 2 | `break`, `continue`, Loop `else`-Klausel, Verschachtelte Schleifen, List Comprehensions, `string` Modul, `random` Modul |
| V08 | Listen & Datenstrukturen | `list`, `tuple`, List-Methoden (`.append()`, `.insert()`, `.extend()`, `.remove()`, `.pop()`, `.clear()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()`), `sorted()`, `sum()`, `all()`, `any()`, `zip()`, Slicing, Unpacking, Aliasing vs. Copying |
| V09 | Try-Catch (Fehlerbehandlung) | `try`, `except`, `else`, `finally`, `raise`, Exception-Hierarchie, `ValueError`, `TypeError`, `KeyError`, `FileNotFoundError`, `PermissionError`, `IndexError`, `ZeroDivisionError`, `json` Modul |
| V10 | Methoden/Funktionen – Teil 1 | `def`-Statement, `return`-Statement, Parameter und Argumente, Default-Parameter, Keyword Arguments, Multiple Return Values, Funktionen als Objekte, Scope und LEGB-Regel, Docstrings |
| V11 | GPTs, LLMs & KI + Funktionen Teil 2 | Keyword-Only Arguments (`*`), `*args`, `**kwargs`, Unpacking-Operatoren, Lambda-Funktionen, `map()`, `filter()`, Type Hints (`typing`-Modul), Docstring-Stile (Google/NumPy), Fehlerbehandlung in Batches |
| V12 | Imports & Module | `import`, `from ... import`, `as`-Aliasing, `__name__`, `__main__`, `if __name__ == '__main__'`, Package-Struktur, `__init__.py`, `sys.path`, `venv`, `pip`, `requirements.txt`, `argparse` |
| V13 | Plots & Grafiken (Matplotlib) – Teil 1 | `matplotlib.pyplot`, `plt.plot()`, `plt.scatter()`, `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`, `plt.grid()`, `plt.show()`, `plt.xlim()`, `plt.ylim()`, `plt.axhline()`, `plt.axvline()`, `plt.errorbar()`, `plt.fill_between()`, `plt.subplots()`, `plt.tight_layout()`, `plt.savefig()`, `np.polyfit()`, `np.polyval()` |
| V14 | Plots & Grafiken (Matplotlib) – Teil 2 + XML | `plt.hist()`, `plt.boxplot()`, `plt.bar()` (grouped), `plt.barh()`, Polar/Radar Charts (`projection='polar'`), `xml.etree.ElementTree`, `ET.parse()`, `ET.fromstring()`, `.find()`, `.findall()`, `.text`, `pandas.read_csv()`, Multiple Data Formats (CSV, JSON, XML) |
| V15 | Netzwerktechnik & Industrielle Kommunikation | `socket`, `struct`, `ipaddress`, `socket.socket()`, `socket.bind()`, `socket.listen()`, `socket.accept()`, `socket.connect()`, `socket.send()`, `socket.recv()`, `struct.pack()`, `struct.unpack()`, `ipaddress.ip_address()`, `ipaddress.ip_network()`, Binary Data Processing, Network Protocols, CSV/JSON/XML for Industrial Data |
| V16 | Pandas & DataFrame-Operationen | `pandas`, `pd.read_csv()`, `pd.read_json()`, `pd.read_xml()`, `pd.DataFrame()`, `.head()`, `.tail()`, `.info()`, `.describe()`, `.shape`, `.columns`, `pd.to_datetime()`, Boolean Indexing, `.loc[]`, `.iloc[]`, `.query()`, `.isin()`, `.sort_values()`, `.groupby()`, `.agg()`, `.apply()`, Vectorization, `.iterrows()` (discouraged), Time Series Analysis |
| V17 | Kryptografie & Netzwerk-Programmierung Teil 1 | `socket`, `hashlib`, `socket.socket()`, `.bind()`, `.listen()`, `.accept()`, `.connect()`, `.send()`, `.sendall()`, `.recv()`, `.close()`, `.setsockopt()`, `.settimeout()`, `hashlib.sha256()`, `.hexdigest()`, TCP/IP, Client-Server-Architektur, Byte Encoding/Decoding |
| V19 | Datenbanken – Teil 1 | `sqlite3`, `sqlite3.connect()`, `.cursor()`, `.execute()`, `.executemany()`, `.fetchall()`, `.fetchone()`, `.fetchmany()`, `.commit()`, `.rollback()`, `.close()`, `row_factory`, `sqlite3.Row`, `sqlite3.IntegrityError`, `sqlite3.OperationalError`, Prepared Statements (`?`), Transactions (BEGIN/COMMIT/ROLLBACK), Context Managers (`with`), SQL (CREATE TABLE, INSERT, SELECT, UPDATE, DELETE, JOIN, GROUP BY, HAVING, Subqueries) |
| V20 | Datenbanken – Teil 2 | Prepared Statements (Named Placeholders `:name`), `cursor.rowcount`, UPDATE (SET WHERE), DELETE (WHERE CASCADE), Transaktionen (try/except/finally), SAVEPOINT, ROLLBACK TO, `cursor.description`, Aggregationen (COUNT/SUM/AVG/MIN/MAX mit GROUP BY, HAVING), JOINs (INNER, LEFT, mehrfach), Subqueries (WHERE IN, nested SELECT), Best Practices (Indizes auf FK, Error Handling, executemany, PRAGMA foreign_keys ON, LIMIT), `pd.pivot_table()`, `pd.to_excel()`, Context Manager (`__enter__`, `__exit__`), strftime Quartal-Extraktion |

---

# Details pro Vorlesung

## V01 (2026-01-01) – Python Get Started: Variablen, print, input

### Neu eingeführt

#### Builtins
- **`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`** (Python 3.0+)
  - Gibt Objekte auf die Standardausgabe (Konsole) aus
  - Mehrere Argumente werden durch `sep` getrennt (Standard: Leerzeichen)
  - Nach der Ausgabe wird `end` angehängt (Standard: Zeilenumbruch `\n`)
  - Signatur: `print(value1, value2, ..., sep=' ', end='\n')`
  - Beispiel: `print("Hallo", "Welt")` → `Hallo Welt`

- **`input(prompt='')`** (Python 3.0+)
  - Liest eine Zeile von der Standardeingabe (Tastatur)
  - Optional: Zeigt einen Prompt-Text an
  - Gibt **immer einen String** zurück
  - Signatur: `input(prompt)` → `str`
  - Beispiel: `name = input("Name: ")` wartet auf Eingabe

- **`int(x, base=10)`** (Built-in)
  - Konvertiert Wert `x` in eine Ganzzahl (Integer)
  - Optional: `base` gibt Zahlensystem an (2-36)
  - Kann Strings, Floats und andere Typen konvertieren
  - Wirft `ValueError` bei ungültiger Konvertierung
  - Beispiel: `int("42")` → `42`, `int(3.7)` → `3`

- **`float(x)`** (Built-in)
  - Konvertiert Wert `x` in eine Fließkommazahl
  - Akzeptiert Strings, Integers und andere numerische Typen
  - Wirft `ValueError` bei ungültiger Konvertierung
  - Beispiel: `float("3.14")` → `3.14`, `float(5)` → `5.0`

- **`str(object='')`** (Built-in)
  - Konvertiert ein Objekt in seine String-Repräsentation
  - Funktioniert mit nahezu allen Datentypen
  - Beispiel: `str(42)` → `"42"`, `str(3.14)` → `"3.14"`

- **`len(s)`** (Built-in)
  - Gibt die Länge (Anzahl der Elemente) eines Objekts zurück
  - Funktioniert mit Strings, Listen, Tuples, Dictionaries, etc.
  - Beispiel: `len("Hallo")` → `5`, `len("1011")` → `4`

#### Operatoren
- **Zuweisungsoperator `=`**
  - Weist einer Variable einen Wert zu
  - Syntax: `variable = wert`
  - Beispiel: `x = 42`

- **Arithmetische Operatoren: `+`, `-`, `*`, `/`**
  - Addition, Subtraktion, Multiplikation, Division
  - Beispiel: `5 + 3` → `8`, `10 / 2` → `5.0`

- **Potenzoperator `**`**
  - Berechnet Potenzen
  - Syntax: `basis ** exponent`
  - Beispiel: `2 ** 3` → `8`, `9 ** 0.5` → `3.0` (Quadratwurzel)

- **Zusammengesetzte Zuweisungsoperatoren: `+=`, `-=`, `*=`, `/=`**
  - Kurzschreibweise für `x = x op y`
  - Beispiel: `x += 1` entspricht `x = x + 1`

#### Konzepte und Sprachmerkmale
- **Variablen**
  - Benannte Speicherplätze für Werte
  - Keine explizite Deklaration notwendig
  - Naming-Regeln: Buchstaben, Ziffern, Unterstriche; nicht mit Ziffer beginnen; keine Keywords
  - Konvention: `snake_case` für Variablennamen

- **Dynamische Typisierung**
  - Typ einer Variable wird automatisch aus dem zugewiesenen Wert abgeleitet
  - Variablen können ihren Typ zur Laufzeit ändern
  - Keine Typdeklaration erforderlich

- **Kommentare**
  - Einzeilige Kommentare: `# Text`
  - Mehrzeilige Kommentare (Docstrings): `"""Text"""` oder `'''Text'''`
  - Werden vom Interpreter ignoriert
  - Dienen der Code-Dokumentation

- **String-Indexierung**
  - Zugriff auf einzelne Zeichen: `text[index]`
  - Indizes beginnen bei 0
  - Beispiel: `"Hallo"[0]` → `"H"`

#### Datentypen
- **`int`**: Ganzzahlen (beliebiger Größe in Python 3)
- **`float`**: Fließkommazahlen (IEEE 754 double precision)
- **`str`**: Zeichenketten (Unicode-Strings)
- **`bool`**: Wahrheitswerte `True` und `False` (werden in V04 ausführlich behandelt)

### Notizen
- Python 3.0+ verwendet automatisch Unicode-Strings
- Division `/` ergibt immer `float`, auch bei ganzzahligem Ergebnis
- Integer haben in Python 3 unbegrenzte Größe (nur durch Speicher limitiert)
- `input()` hat sich zwischen Python 2 und 3 geändert (Python 2: `raw_input()`)
- Empfohlene IDE für diese Vorlesung: Visual Studio Code mit Python-Extension

---

## V02 (2026-01-01) – Eingaben/Ausgaben & Formatierung

### Neu eingeführt

#### String-Formatierung

- **f-Strings (Formatted String Literals)** (Python 3.6+)
  - Moderne Methode zur String-Formatierung mit direkter Variablen-Einbettung
  - Syntax: `f"Text {variable}"` oder `f"Text {expression}"`
  - Formatspezifikationen nach Doppelpunkt: `f"{x:.2f}"` für 2 Dezimalstellen
  - Signatur: `f"...{expression:format_spec}..."`
  - Beispiel: `f"Pi ist {pi:.2f}"` → `"Pi ist 3.14"`

- **Formatspezifikationen in f-Strings**:
  - `{x:.2f}` – Fließkommazahl mit 2 Dezimalstellen (fixed-point)
  - `{x:.3e}` – Wissenschaftliche Notation (exponential) mit 3 Dezimalstellen
  - `{x:10.2f}` – Rechtsbündig in Feld der Breite 10 mit 2 Dezimalstellen
  - `{x:<10.2f}` – Linksbündig in Feld der Breite 10
  - `{x:^10.2f}` – Zentriert in Feld der Breite 10
  - `{x:,}` – Tausender-Trennzeichen (Komma)
  - `{x:_}` – Tausender-Trennzeichen (Unterstrich)
  - `{x:.1%}` – Prozentangabe (multipliziert mit 100, fügt % hinzu)
  - `{x:+.2f}` – Mit Vorzeichen anzeigen
  - `{x:08.2f}` – Mit führenden Nullen auffüllen auf Breite 8

- **`.format()`-Methode** (Python 2.6+, String-Methode)
  - Ältere, aber immer noch verwendete Formatierungsmethode
  - Platzhalter `{}` werden durch übergebene Argumente ersetzt
  - Positionsangabe: `"{0} {1}".format(a, b)` oder `"{1} {0}".format(a, b)`
  - Benannte Argumente: `"{name} ist {alter}".format(name="Ada", alter=25)`
  - Formatspezifikationen wie bei f-Strings: `"{:.2f}".format(pi)`
  - Signatur: `str.format(*args, **kwargs)` → `str`
  - Beispiel: `"Hallo {0}, du bist {1} Jahre alt".format("Bob", 30)`

- **%-Operator (Legacy, String Formatting)** (Python 1.x+)
  - Veraltete C-style Formatierung
  - Platzhalter: `%s` (String), `%d` (Integer), `%f` (Float), `%.2f` (Float mit 2 Dezimalstellen)
  - Syntax: `"Text %s" % (wert,)` oder `"Text %s %d" % (str_wert, int_wert)`
  - Signatur: `format_string % values` → `str`
  - Beispiel: `"Pi: %.2f" % (pi,)` → `"Pi: 3.14"`
  - **Nicht empfohlen für neuen Code** – verwende stattdessen f-Strings

#### Erweiterte `print()`-Funktionalität

- **`print()`-Parameter `sep`** (Python 3.0+)
  - Legt das Trennzeichen zwischen mehreren Argumenten fest
  - Standard: `sep=' '` (Leerzeichen)
  - Signatur: `print(*objects, sep=' ')`
  - Beispiel: `print("A", "B", "C", sep="-")` → `A-B-C`

- **`print()`-Parameter `end`** (Python 3.0+)
  - Legt an, was am Ende der Ausgabe angefügt wird
  - Standard: `end='\n'` (Zeilenumbruch)
  - Signatur: `print(*objects, end='\n')`
  - Beispiel: `print("Text", end="")` → kein Zeilenumbruch danach

- **`print()`-Parameter `flush`** (Python 3.3+)
  - Erzwingt sofortiges Schreiben der Ausgabe (ohne Pufferung)
  - Standard: `flush=False`
  - Signatur: `print(*objects, flush=False)`
  - Nützlich für Fortschrittsanzeigen oder Log-Ausgaben
  - Beispiel: `print("Lade...", end="", flush=True)`

#### Escape-Sequenzen und Spezial-Strings

- **Escape-Sequenzen**
  - `\n` – Zeilenumbruch (Newline)
  - `\t` – Tabulator (Tab)
  - `\\` – Backslash selbst
  - `\'` – Einfaches Anführungszeichen
  - `\"` – Doppeltes Anführungszeichen
  - `\r` – Carriage Return (Wagenrücklauf)
  - `\b` – Backspace
  - Beispiel: `"Zeile 1\nZeile 2"` → zwei Zeilen

- **Raw Strings (r-Strings)** (Python 2.0+)
  - Strings, in denen Backslashes nicht als Escape-Zeichen interpretiert werden
  - Syntax: `r"Text mit \backslash"`
  - Nützlich für Windows-Pfade und reguläre Ausdrücke
  - Beispiel: `r"C:\Users\Ada"` → `"C:\Users\Ada"` (keine Escape-Interpretation)

- **Mehrzeilige Strings (Triple Quotes)** (Python 1.0+)
  - Strings über mehrere Zeilen mit `"""..."""` oder `'''...'''`
  - Behalten alle Zeilenumbrüche und Einrückungen
  - Können auch als Docstrings verwendet werden
  - Beispiel:
    ```python
    text = """Zeile 1
    Zeile 2
    Zeile 3"""
    ```

#### Datei-Ein- und Ausgabe

- **`open(filename, mode='r', encoding=None)`** (Built-in)
  - Öffnet eine Datei und gibt ein File-Objekt zurück
  - Parameter `mode`:
    - `"r"` – Read (Lesen, Standard, Datei muss existieren)
    - `"w"` – Write (Schreiben, überschreibt existierende Datei, erstellt neue)
    - `"a"` – Append (Anhängen am Ende, erstellt neue Datei falls nicht existent)
    - `"r+"` – Read/Write (Lesen und Schreiben)
    - `"b"` – Binär-Modus (z.B. `"rb"`, `"wb"`)
  - Parameter `encoding`: z.B. `"utf-8"` (empfohlen für Textdateien)
  - Signatur: `open(file, mode='r', encoding=None, ...)` → `TextIOWrapper` (File-Objekt)
  - Beispiel: `datei = open("daten.txt", "r")`
  - **Wichtig**: Datei muss mit `.close()` geschlossen werden oder via `with`-Statement

- **File-Objekt-Methoden**:
  
  - **`.write(string)`** – Schreibt String in Datei
    - Gibt Anzahl geschriebener Zeichen zurück
    - Fügt **keine** automatischen Zeilenumbrüche hinzu (manuell `\n` anfügen)
    - Signatur: `file.write(s)` → `int`
    - Beispiel: `datei.write("Hallo Welt\n")`
  
  - **`.read(size=-1)`** – Liest gesamten Dateiinhalt (oder `size` Zeichen)
    - Parameter `size`: Anzahl zu lesender Zeichen (-1 = alles)
    - Gibt String zurück
    - Signatur: `file.read(size=-1)` → `str`
    - Beispiel: `inhalt = datei.read()`
  
  - **`.readline(size=-1)`** – Liest eine einzelne Zeile
    - Inkludiert den Zeilenumbruch `\n` am Ende
    - Gibt leeren String zurück bei EOF (End of File)
    - Signatur: `file.readline(size=-1)` → `str`
    - Beispiel: `zeile = datei.readline()`
  
  - **`.readlines(hint=-1)`** – Liest alle Zeilen als Liste von Strings
    - Jeder String endet mit `\n` (außer ggf. letzte Zeile)
    - Signatur: `file.readlines(hint=-1)` → `list[str]`
    - Beispiel: `zeilen = datei.readlines()`
  
  - **`.close()`** – Schließt die Datei
    - Gibt Ressourcen frei und schreibt gepufferte Daten
    - Nach `.close()` können keine weiteren Operationen durchgeführt werden
    - Signatur: `file.close()` → `None`
    - Beispiel: `datei.close()`

- **`with`-Statement (Context Manager)** (Python 2.5+)
  - Garantiert automatisches Schließen von Ressourcen (z.B. Dateien)
  - Syntax: `with open(filename, mode) as variable:`
  - Datei wird automatisch geschlossen, auch bei Fehlern im Block
  - **Best Practice**: Immer `with` verwenden statt manuellem `open()` und `.close()`
  - Signatur: `with expression as target:`
  - Beispiel:
    ```python
    with open("daten.txt", "r") as datei:
        inhalt = datei.read()
    # Datei ist hier automatisch geschlossen
    ```

#### String-Methoden (Ergänzungen)

- **`.upper()`** (String-Methode)
  - Konvertiert alle Buchstaben zu Großbuchstaben
  - Signatur: `str.upper()` → `str`
  - Beispiel: `"hallo".upper()` → `"HALLO"`

- **`.lower()`** (String-Methode)
  - Konvertiert alle Buchstaben zu Kleinbuchstaben
  - Signatur: `str.lower()` → `str`
  - Beispiel: `"HALLO".lower()` → `"hallo"`

- **`.strip(chars=None)`** (String-Methode)
  - Entfernt Whitespace (Leerzeichen, Tabs, Zeilenumbrüche) vom Anfang und Ende
  - Optional: Entfernt spezifische Zeichen aus `chars`
  - Signatur: `str.strip(chars=None)` → `str`
  - Beispiel: `"  Hallo  \n".strip()` → `"Hallo"`

- **`.split(sep=None, maxsplit=-1)`** (String-Methode)
  - Teilt String an Trennzeichen `sep` in Liste von Strings
  - Standard: `sep=None` (teilt an jedem Whitespace)
  - Signatur: `str.split(sep=None, maxsplit=-1)` → `list[str]`
  - Beispiel: `"a,b,c".split(",")` → `["a", "b", "c"]`

### Konzepte und Best Practices

- **f-Strings sind die empfohlene Methode** für String-Formatierung in Python 3.6+
  - Lesbarer, schneller und weniger fehleranfällig als `.format()` oder `%`
  - Verwende `.format()` nur, wenn der Format-String wiederverwendet wird
  - Verwende `%` nur bei Legacy-Code-Wartung

- **Dateien immer mit `with`-Statement öffnen**
  - Garantiert korrektes Schließen auch bei Fehlern
  - Verhindert Ressourcen-Lecks und Datenverlust
  - Bessere Lesbarkeit durch klare Scope-Definition

- **Escape-Sequenzen und Raw Strings**
  - Raw Strings (`r"..."`) für Windows-Pfade und reguläre Ausdrücke
  - Normale Strings mit Escape-Sequenzen für Text mit Spezialzeichen
  - Triple Quotes für mehrzeilige Texte und Docstrings

- **Append-Modus für Log-Dateien**
  - Verwende `"a"` statt `"w"` zum Anhängen, um Datenverlust zu vermeiden
  - `"w"` löscht existierenden Inhalt komplett

### Notizen

- f-Strings wurden in Python 3.6 eingeführt und sind seit Python 3.8 die empfohlene Methode
- Der `flush`-Parameter von `print()` ist erst seit Python 3.3 verfügbar
- `open()` unterstützt seit Python 3 standardmäßig Text-Modus mit Unicode (UTF-8)
- In Python 2 musste `io.open()` für Unicode-Support verwendet werden
- Windows verwendet `\r\n` als Zeilenumbruch, Unix/Linux/Mac `\n` – Python normalisiert dies automatisch im Text-Modus
- CSV-Dateien sollten ohne Leerzeichen nach Kommas geschrieben werden (Standard-Konvention)

---

## V03 (2026-01-01) – Variablen Management & Datentypen

### Neu eingeführt

#### Type Checking und Introspection

- **`type(obj)`** (Built-in)
  - Gibt den Datentyp des übergebenen Objekts zurück
  - Rückgabewert ist ein Typ-Objekt (z.B. `<class 'int'>`)
  - Signatur: `type(obj)` → `type`
  - Beispiel: `type(42)` → `<class 'int'>`, `type("Hallo")` → `<class 'str'>`
  - Verwendung für Typ-Vergleiche: `if type(x) == int:`

- **`isinstance(obj, classinfo)`** (Built-in)
  - Prüft, ob `obj` eine Instanz von `classinfo` ist
  - Berücksichtigt Vererbung (z.B. `bool` ist Subtyp von `int`)
  - `classinfo` kann auch Tupel von Typen sein
  - Signatur: `isinstance(obj, classinfo)` → `bool`
  - Beispiel: `isinstance(42, int)` → `True`, `isinstance(True, int)` → `True`
  - Bevorzugt gegenüber `type()` für Typ-Checks
  - Mehrere Typen: `isinstance(x, (int, float))` prüft, ob `x` int ODER float ist

- **`id(obj)`** (Built-in)
  - Gibt die Identität (Speicheradresse) eines Objekts zurück
  - Rückgabewert ist eine eindeutige Integer-ID
  - Nützlich zur Demonstration von Mutability/Immutability
  - Signatur: `id(obj)` → `int`
  - Beispiel: `id("Hallo")` → `140234567890123` (Adresse variiert)
  - Zwei Objekte mit gleicher ID sind **dasselbe** Objekt im Speicher

#### Type Casting (Erweitert)

- **`bool(x)`** (Built-in)
  - Konvertiert Wert `x` in Boolean (`True` oder `False`)
  - Bereits in V01 als Datentyp erwähnt, hier als Casting-Funktion vertieft
  - **Falsy Values**: `0`, `0.0`, `""`, `[]`, `None`, `False` → `False`
  - **Truthy Values**: Alle anderen Werte → `True`
  - Signatur: `bool(x)` → `bool`
  - Beispiel: `bool(0)` → `False`, `bool(42)` → `True`, `bool("")` → `False`
  - Wichtig: `bool("0")` → `True` (String "0" ist nicht leer!)

- **`round(number, ndigits=None)`** (Built-in)
  - Rundet eine Zahl auf `ndigits` Dezimalstellen
  - Ohne `ndigits`: Rundet zur nächsten Ganzzahl
  - Verwendet "Banker's Rounding" (Round Half to Even) bei `.5`
  - Signatur: `round(number, ndigits=None)` → `float` oder `int`
  - Beispiel: `round(3.14159, 2)` → `3.14`, `round(2.5)` → `2` (Banker's Rounding!)
  - Unterschied zu `int()`: `round()` rundet mathematisch, `int()` schneidet ab

#### Min/Max-Funktionen

- **`min(iterable)` / `min(*args)`** (Built-in)
  - Gibt das kleinste Element aus einem Iterable oder mehreren Argumenten zurück
  - Signatur: `min(iterable)` → Element oder `min(arg1, arg2, ...)` → Element
  - Beispiel: `min([5, 2, 8])` → `2`, `min(5, 2, 8)` → `2`
  - Funktioniert mit allen vergleichbaren Typen (int, float, str, etc.)
  - Bei Strings: Lexikographischer Vergleich

- **`max(iterable)` / `max(*args)`** (Built-in)
  - Gibt das größte Element aus einem Iterable oder mehreren Argumenten zurück
  - Signatur: `max(iterable)` → Element oder `max(arg1, arg2, ...)` → Element
  - Beispiel: `max([5, 2, 8])` → `8`, `max(5, 2, 8)` → `8`
  - Funktioniert analog zu `min()`

#### String-Methoden (Validierung und Analyse)

- **`str.isdigit()`** (String-Methode)
  - Prüft, ob alle Zeichen im String Ziffern sind (0-9)
  - Gibt `False` zurück bei leerem String
  - Signatur: `str.isdigit()` → `bool`
  - Beispiel: `"123".isdigit()` → `True`, `"12.3".isdigit()` → `False`, `"-5".isdigit()` → `False`
  - Nützlich zur Validierung vor `int()`-Konvertierung

- **`str.isalpha()`** (String-Methode)
  - Prüft, ob alle Zeichen im String Buchstaben sind (a-z, A-Z, Unicode-Buchstaben)
  - Gibt `False` zurück bei leerem String oder wenn Ziffern/Leerzeichen enthalten
  - Signatur: `str.isalpha()` → `bool`
  - Beispiel: `"Hallo".isalpha()` → `True`, `"Hallo123".isalpha()` → `False`

- **`str.isupper()`** (String-Methode)
  - Prüft, ob alle Buchstaben im String Großbuchstaben sind
  - Ignoriert Nicht-Buchstaben-Zeichen (Ziffern, Leerzeichen, etc.)
  - Gibt `False` zurück, wenn keine Buchstaben vorhanden
  - Signatur: `str.isupper()` → `bool`
  - Beispiel: `"HALLO".isupper()` → `True`, `"HALLO123".isupper()` → `True`, `"Hallo".isupper()` → `False`

- **`str.islower()`** (String-Methode)
  - Prüft, ob alle Buchstaben im String Kleinbuchstaben sind
  - Ignoriert Nicht-Buchstaben-Zeichen
  - Gibt `False` zurück, wenn keine Buchstaben vorhanden
  - Signatur: `str.islower()` → `bool`
  - Beispiel: `"hallo".islower()` → `True`, `"hallo123".islower()` → `True`, `"Hallo".islower()` → `False`

- **`str.lstrip(chars=None)`** (String-Methode)
  - Entfernt Zeichen vom **linken** Ende des Strings
  - Parameter `chars`: Zu entfernende Zeichen (Standard: Whitespace)
  - Signatur: `str.lstrip(chars=None)` → `str`
  - Beispiel: `"  Hallo".lstrip()` → `"Hallo"`, `"-42".lstrip('-')` → `"42"`
  - Verwandt: `.rstrip()` (rechts), `.strip()` (beide Seiten, bereits in V02)

- **`str.count(sub)`** (String-Methode)
  - Zählt, wie oft der Substring `sub` im String vorkommt
  - Überlappungen werden nicht gezählt
  - Signatur: `str.count(sub)` → `int`
  - Beispiel: `"Hallo".count('l')` → `2`, `"3.14.15".count('.')` → `2`

#### Variablen-Scope

- **`global`-Keyword** (Keyword)
  - Deklariert eine Variable als global innerhalb einer Funktion
  - Ermöglicht Modifikation globaler Variablen aus Funktionen heraus
  - Syntax: `global variable_name`
  - Verwendung:
    ```python
    counter = 0
    def increment():
        global counter  # Ohne global würde neue lokale Variable erzeugt
        counter += 1
    ```
  - **Warnung**: Sparsam verwenden! Globale Variablen erschweren Debugging und Testing
  - Bevorzuge Funktionsparameter und Rückgabewerte

#### Konzepte und Sprachmerkmale

- **Immutable vs. Mutable**
  - **Immutable (unveränderlich)**: Objekte können nach Erzeugung nicht geändert werden
    - Typen: `int`, `float`, `str`, `bool`, `tuple`
    - Operationen erzeugen neue Objekte
    - Beispiel: `text = text + "!"` erzeugt neuen String
  - **Mutable (veränderlich)**: Objekte können nach Erzeugung modifiziert werden
    - Typen: `list`, `dict`, `set` (werden in V08 ausführlich behandelt)
    - Operationen ändern Objekt in-place
    - Beispiel: `liste.append(4)` ändert existierende Liste
  - Bedeutung: Beeinflusst Performance, Seiteneffekte und Verwendbarkeit als Dictionary-Keys

- **Variablen-Scope**
  - **Globaler Scope**: Variablen außerhalb von Funktionen, überall sichtbar
  - **Lokaler Scope**: Variablen innerhalb von Funktionen, nur dort sichtbar
  - **LEGB-Regel**: Local → Enclosing → Global → Built-in (Reihenfolge der Namensauflösung)
  - Lokale Variablen überdecken gleichnamige globale Variablen

- **Multiple Assignment**
  - Mehreren Variablen gleichzeitig denselben Wert zuweisen
  - Syntax: `x = y = z = wert`
  - Beispiel: `a = b = c = 0` setzt alle drei auf 0
  - **Vorsicht bei mutable Typen**: `a = b = []` → beide zeigen auf dieselbe Liste!

- **Value Unpacking (Tuple Unpacking)**
  - Mehrere Werte gleichzeitig verschiedenen Variablen zuweisen
  - Syntax: `x, y, z = wert1, wert2, wert3`
  - Intern arbeitet Python mit Tupeln: `(x, y) = (1, 2)`
  - Beispiel: `a, b = 10, 20` oder Variablen tauschen: `a, b = b, a`
  - Funktioniert auch mit Funktionsrückgaben: `min_val, max_val = min(liste), max(liste)`
  - **Fehler**: Anzahl der Variablen muss mit Anzahl der Werte übereinstimmen

### Konzepte und Best Practices

- **`isinstance()` bevorzugen**: Für Typ-Checks bevorzuge `isinstance()` statt `type()`, da es Vererbung berücksichtigt
- **Banker's Rounding beachten**: `round(2.5)` ergibt `2`, nicht `3` (Round Half to Even Strategie)
- **Unveränderlichkeit verstehen**: String-Operationen sind ineffizient in Schleifen, da neue Objekte erzeugt werden
- **`global` sparsam verwenden**: Globale Variablen erschweren Wartung. Bevorzuge Parameter und Rückgabewerte
- **Validierung vor Konvertierung**: Prüfe mit `.isdigit()` oder ähnlichen Methoden vor `int()`/`float()`, um `ValueError` zu vermeiden
- **Falsy Values kennen**: `bool("0")` ist `True` (nicht-leerer String), aber `bool(0)` ist `False`

### Notizen

- `isinstance()` wurde in Python 2.2 eingeführt und ist seit Python 3 die empfohlene Methode für Typ-Checks
- `round()` verwendet seit Python 3 "Banker's Rounding" (IEEE 754), in Python 2 war es "Round Half Up"
- `id()` gibt die CPython-Speicheradresse zurück; in anderen Python-Implementierungen kann es eine andere eindeutige ID sein
- Boolean-Datentyp `bool` ist ein Subtyp von `int`: `True + True` ergibt `2`
- Listen-Operationen (`.append()`, etc.) werden in V08 ausführlich behandelt, hier nur für Mutability-Demonstration verwendet
- String-Methoden für Validierung (`.isdigit()`, `.isalpha()`) sind hilfreich, decken aber nicht alle Fälle ab (z.B. negative Zahlen benötigen `.lstrip('-')`)
---

## V04 (2026-01-02) – Logische Ausdrücke (Boolsche Algebra)

### Neu eingeführt

#### Vergleichsoperatoren

- **`==` (Gleichheit / Equality)**
  - Prüft, ob zwei Werte gleich sind
  - Gibt `True` oder `False` zurück
  - Signatur: `a == b` → `bool`
  - Beispiel: `5 == 5` → `True`, `5 == 10` → `False`
  - **Wichtig**: `==` ist Vergleich, `=` ist Zuweisung!

- **`!=` (Ungleichheit / Not Equal)**
  - Prüft, ob zwei Werte unterschiedlich sind
  - Signatur: `a != b` → `bool`
  - Beispiel: `5 != 10` → `True`, `5 != 5` → `False`

- **`<` (Kleiner als / Less Than)**
  - Prüft, ob linker Wert kleiner als rechter ist
  - Signatur: `a < b` → `bool`
  - Beispiel: `5 < 10` → `True`, `10 < 5` → `False`

- **`>` (Größer als / Greater Than)**
  - Prüft, ob linker Wert größer als rechter ist
  - Signatur: `a > b` → `bool`
  - Beispiel: `10 > 5` → `True`, `5 > 10` → `False`

- **`<=` (Kleiner oder gleich / Less or Equal)**
  - Prüft, ob linker Wert kleiner oder gleich rechter ist
  - Signatur: `a <= b` → `bool`
  - Beispiel: `5 <= 10` → `True`, `5 <= 5` → `True`, `10 <= 5` → `False`

- **`>=` (Größer oder gleich / Greater or Equal)**
  - Prüft, ob linker Wert größer oder gleich rechter ist
  - Signatur: `a >= b` → `bool`
  - Beispiel: `10 >= 5` → `True`, `5 >= 5` → `True`, `5 >= 10` → `False`

**Eigenschaften:**
- Funktionieren mit Zahlen, Strings (lexikographisch), und anderen vergleichbaren Typen
- Liefern immer Boolean-Werte (`True` oder `False`)
- Können verkettet werden (siehe unten)

#### Logische Operatoren

- **`and` (Logisches UND / Logical AND)**
  - Gibt `True` zurück, wenn **beide** Operanden `True` sind
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `False`
  - Signatur: `a and b` → `bool`
  - Beispiel: `True and True` → `True`, `True and False` → `False`
  - Wahrheitstabelle:
    | A | B | A and B |
    |---|---|---------|
    | False | False | False |
    | False | True | False |
    | True | False | False |
    | True | True | True |

- **`or` (Logisches ODER / Logical OR)**
  - Gibt `True` zurück, wenn **mindestens ein** Operand `True` ist
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `True`
  - Signatur: `a or b` → `bool`
  - Beispiel: `True or False` → `True`, `False or False` → `False`
  - Wahrheitstabelle:
    | A | B | A or B |
    |---|---|--------|
    | False | False | False |
    | False | True | True |
    | True | False | True |
    | True | True | True |

- **`not` (Logische Negation / Logical NOT)**
  - Kehrt Boolean-Wert um (`True` → `False`, `False` → `True`)
  - Signatur: `not a` → `bool`
  - Beispiel: `not True` → `False`, `not False` → `True`
  - Wahrheitstabelle:
    | A | not A |
    |---|-------|
    | False | True |
    | True | False |

#### Bitweise Operatoren (Einführung)

- **`^` (Bitweises XOR für Integer)**
  - Führt XOR-Operation auf Bit-Ebene durch
  - Signatur: `a ^ b` → `int`
  - Beispiel: `5 ^ 3` → `6` (binär: `0101 ^ 0011 = 0110`)
  - Nützlich für Bit-Manipulation, Verschlüsselung, Paritätsprüfung
  - **Hinweis**: Für Boolean-XOR verwende `a != b`

#### Konzepte und Sprachmerkmale

- **Verkettete Vergleiche (Chained Comparisons)** (Python-spezifisches Feature)
  - Python erlaubt mathematische Notation für Bereichsprüfungen
  - Syntax: `a < b < c` statt `a < b and b < c`
  - Beispiel: `10 <= alter <= 100` prüft Bereich [10, 100]
  - Funktioniert mit beliebig vielen Vergleichen: `a < b < c < d`
  - **Vorteil**: Lesbarer und effizienter (Mittelwert wird nur einmal ausgewertet)
  - Beispiele:
    ```python
    18 <= alter < 65   # Erwachsen, nicht Senior
    0 < x <= 100       # Positiv und nicht über 100
    x == y == z        # Alle drei gleich
    ```

- **Kurzschlussauswertung (Short-Circuit Evaluation / Lazy Evaluation)**
  - Python wertet logische Ausdrücke von links nach rechts aus
  - Bricht ab, sobald Ergebnis feststeht
  - **Bei `and`**: Wenn linker Operand `False`, wird rechter **nicht** ausgewertet
    - `False and x` → `False` (x wird ignoriert)
    - `True and x` → x wird ausgewertet
  - **Bei `or`**: Wenn linker Operand `True`, wird rechter **nicht** ausgewertet
    - `True or x` → `True` (x wird ignoriert)
    - `False or x` → x wird ausgewertet
  - **Vorteile**:
    - Performance: Spart unnötige Berechnungen
    - Sicherheit: Verhindert Fehler (z.B. Division durch Null)
  - Beispiel:
    ```python
    if x != 0 and y / x > 10:  # Kein ZeroDivisionError!
        # Division wird nur ausgeführt, wenn x != 0
    ```

- **Operator-Präzedenz (Operator Precedence)**
  - Reihenfolge der Auswertung logischer Operatoren (höchste → niedrigste Priorität):
    1. **Vergleichsoperatoren**: `==`, `!=`, `<`, `>`, `<=`, `>=`
    2. **`not`**: Negation
    3. **`and`**: Konjunktion
    4. **`or`**: Disjunktion
  - Beispiel:
    ```python
    not x and y     # = (not x) and y
    x or y and z    # = x or (y and z)
    ```
  - **Best Practice**: Klammern verwenden für Klarheit!
    ```python
    (x > 0 and y > 0) or (z > 0 and w > 0)  # Explizit und lesbar
    ```

- **Truthy und Falsy Values (Truth Value Testing)**
  - Jedes Python-Objekt kann in Boolean-Kontext als `True` oder `False` interpretiert werden
  - **Falsy Values** (werden als `False` interpretiert):
    - `False` (der Boolean-Wert selbst)
    - `None` (das Null-Objekt)
    - Numerische Nullen: `0`, `0.0`, `0j` (komplexe Null)
    - Leere Sequenzen: `""` (leerer String), `[]` (leere Liste), `()` (leeres Tupel)
    - Leere Collections: `{}` (leeres Dictionary), `set()` (leeres Set)
  - **Truthy Values** (werden als `True` interpretiert):
    - Alle anderen Werte!
    - Nicht-null Zahlen: `1`, `-5`, `3.14`
    - Nicht-leere Strings: `"Hallo"`, `"0"` (String "0" ist **truthy**!)
    - Nicht-leere Collections: `[1, 2]`, `{"key": "value"}`
  - **Anwendung**: Kompakte Existenz- und Leerprüfungen
    ```python
    if liste:              # Statt: if len(liste) > 0:
        print("Nicht leer")
    
    if not benutzer:       # Statt: if benutzer is None:
        print("Nicht angemeldet")
    ```
  - **Wichtig**: `if x:` ist nicht das gleiche wie `if x is not None:`
    - `if x:` ist `False` für `0`, `""`, `[]`, etc.
    - `if x is not None:` ist nur `False` für `None`

- **De Morgan'sche Gesetze in Python**
  - Umformungsregeln für logische Ausdrücke
  - **Gesetz 1**: `not (a and b)` = `(not a) or (not b)`
  - **Gesetz 2**: `not (a or b)` = `(not a) and (not b)`
  - Nützlich zur Vereinfachung komplexer Bedingungen
  - Beispiel:
    ```python
    # Kompliziert:
    if not (ist_student or ist_senior):
        pass
    
    # Vereinfacht mit De Morgan:
    if not ist_student and not ist_senior:
        pass
    ```

#### Built-in Funktionen (Vorschau/Erwähnt)

- **`abs(x)`** (Built-in) - *Erwähnt in Beispielen*
  - Gibt den Absolutbetrag (Betrag ohne Vorzeichen) einer Zahl zurück
  - Signatur: `abs(x)` → `number`
  - Beispiel: `abs(-5)` → `5`, `abs(3.14)` → `3.14`
  - Nützlich für Distanzberechnungen und Toleranzprüfungen bei Floats

- **`any(iterable)`** (Built-in) - *Als Vorschau erwähnt, wird in V08 ausführlich behandelt*
  - Gibt `True` zurück, wenn mindestens ein Element im Iterable `True` ist
  - Signatur: `any(iterable)` → `bool`
  - Beispiel: `any([False, True, False])` → `True`
  - Äquivalent zu mehrfachen `or`-Verknüpfungen
  - Wird in V04 in Passwort-Beispielen verwendet (Vorschau)

### Konzepte und Best Practices

- **Klammern für Lesbarkeit**: Auch wenn Python klare Präzedenzregeln hat, verbessern Klammern die Lesbarkeit erheblich
  ```python
  # Funktioniert, aber schwer lesbar:
  if x > 0 and y > 0 or z > 0
  
  # Besser mit Klammern:
  if (x > 0 and y > 0) or z > 0
  ```

- **`==` vs. `=` nicht verwechseln**:
  - `=` ist Zuweisung: `x = 5`
  - `==` ist Vergleich: `x == 5`
  - Häufiger Anfängerfehler: `if x = 5:` → `SyntaxError`

- **Verkettete Vergleiche nutzen**: Pythonischer und lesbarer als `and`-Verknüpfungen
  ```python
  # Gut:
  if 18 <= alter < 65:
  
  # Funktioniert, aber weniger lesbar:
  if alter >= 18 and alter < 65:
  ```

- **Kurzschlussauswertung für Performance**: "Billige" Checks zuerst bei `and`
  ```python
  # Gut: Einfacher Check zuerst
  if benutzer_eingeloggt and aufwaendige_berechnung():
      pass
  
  # Schlecht: Teure Operation wird immer ausgeführt
  if aufwaendige_berechnung() and benutzer_eingeloggt:
      pass
  ```

- **Truthy/Falsy idiomatisch nutzen**:
  ```python
  # Pythonisch:
  if liste:
      print("Liste nicht leer")
  
  # Explizit (umständlich):
  if len(liste) > 0:
      print("Liste nicht leer")
  ```

- **Float-Vergleiche mit Toleranz**: Wegen Rundungsfehlern nie direkt `==` verwenden
  ```python
  # Problematisch:
  if 0.1 + 0.2 == 0.3:  # False!
  
  # Richtig mit Toleranz:
  if abs((0.1 + 0.2) - 0.3) < 1e-10:  # True
  ```

- **Explizite None-Checks**: Unterscheide zwischen Falsy und None
  ```python
  # Prüft auf Falsy (0, "", [], None, etc.):
  if not x:
      pass
  
  # Prüft nur auf None:
  if x is None:
      pass
  ```

### Notizen

- Verkettete Vergleiche sind ein Python-spezifisches Feature (in vielen anderen Sprachen nicht verfügbar)
- Kurzschlussauswertung ist in Python garantiert (im Gegensatz zu manchen anderen Sprachen)
- Die Unterscheidung zwischen Truthy/Falsy ist fundamental für pythonischen Code-Stil
- `bool` ist ein Subtyp von `int` in Python: `True == 1` und `False == 0` sind wahr
- Bei `and`/`or` mit nicht-Boolean-Werten: Rückgabewert ist der zuletzt ausgewertete Wert, nicht zwingend `True`/`False`
  - `"" or "Hallo"` → `"Hallo"` (nicht `True`!)
  - `5 and 10` → `10` (nicht `True`!)
  - Dieses Verhalten wird für Default-Werte genutzt: `x = eingabe or "Standard"`
- XOR gibt es nicht als logischen Operator für Booleans; verwende `!=` für Boolean-XOR
- Float-Vergleiche sind problematisch wegen IEEE 754 Rundungsfehlern (siehe V02)

---

## V05 (2026-01-02) – Verzweigungen (if, if-elif-else)

### Neu eingeführt

#### Kontrollstrukturen: Bedingte Ausführung

- **`if`-Anweisung** (Python Keyword)
  - Führt einen Codeblock nur aus, wenn eine Bedingung `True` ist
  - Syntax: `if Bedingung:`
  - Erfordert Doppelpunkt nach der Bedingung
  - Der Codeblock muss eingerückt sein (Standard: 4 Leerzeichen)
  - Signatur: `if expression:`
  - Beispiel:
    ```python
    if alter >= 18:
        print("Volljährig")
    ```

- **`else`-Klausel** (Python Keyword)
  - Definiert einen alternativen Codeblock, der ausgeführt wird, wenn die if-Bedingung `False` ist
  - Syntax: `else:`
  - Kein Bedingungsausdruck (keine Klammer nach else)
  - Signatur: `else:`
  - Beispiel:
    ```python
    if temperatur <= 0:
        print("Gefroren")
    else:
        print("Nicht gefroren")
    ```
  - **Wichtig**: else ist optional – eine if-Anweisung kann auch ohne else existieren

- **`elif`-Klausel** (Python Keyword, Abkürzung für "else if")
  - Fügt zusätzliche Bedingungen nach einem `if` hinzu
  - Syntax: `elif Bedingung:`
  - Wird nur geprüft, wenn alle vorherigen Bedingungen `False` waren
  - Ermöglicht mehrfache Verzweigungen (mehr als zwei Pfade)
  - Beliebig viele elif-Klauseln möglich
  - Signatur: `elif expression:`
  - Beispiel:
    ```python
    if punkte >= 90:
        note = "Sehr gut"
    elif punkte >= 80:
        note = "Gut"
    elif punkte >= 70:
        note = "Befriedigend"
    else:
        note = "Nicht bestanden"
    ```
  - **Wichtig**: Nur der erste erfüllte Zweig wird ausgeführt, alle weiteren werden übersprungen

#### Ternärer Operator (Conditional Expression)

- **Ternärer Operator** (Python 2.5+, Sprachkonstrukt)
  - Kompakte Schreibweise für einfache if-else-Zuweisungen in einer Zeile
  - Syntax: `wert_wenn_wahr if Bedingung else wert_wenn_falsch`
  - Die Bedingung steht in der Mitte, davor der True-Wert, danach der False-Wert
  - Signatur: `expression1 if condition else expression2` → Wert
  - Beispiel:
    ```python
    # Normale Schreibweise:
    if x >= 0:
        absolut = x
    else:
        absolut = -x
    
    # Ternärer Operator:
    absolut = x if x >= 0 else -x
    ```
  - Weitere Beispiele:
    ```python
    status = "Aktiv" if ist_eingeloggt else "Inaktiv"
    maximum = a if a > b else b
    print(f"Du bist {'volljährig' if alter >= 18 else 'minderjährig'}")
    ```
  - **Best Practice**: Nur für einfache, einzeilige Entscheidungen verwenden

#### Platzhalter-Statement

- **`pass`-Statement** (Python Keyword)
  - Eine Null-Operation, die nichts tut
  - Dient als syntaktischer Platzhalter für leere Codeblöcke
  - Python erlaubt keine leeren Blöcke – `pass` verhindert `IndentationError`
  - Syntax: `pass`
  - Signatur: `pass`
  - Beispiel:
    ```python
    if benutzer_rolle == "Admin":
        pass  # TODO: Admin-Funktionen implementieren
    elif benutzer_rolle == "Moderator":
        pass  # TODO: Moderator-Funktionen implementieren
    else:
        print("Normaler Benutzer")
    ```
  - **Verwendungszwecke**:
    - Platzhalter während der Entwicklung
    - Explizites "nichts tun" (z.B. in Ausnahmebehandlung)
    - Syntaxanforderung bei leeren Funktionen/Klassen (wird in späteren Vorlesungen relevant)

#### Konzepte und Sprachmerkmale

- **Einrückung als Syntax** (Python-spezifisches Merkmal)
  - Python verwendet **Whitespace (Einrückung)** zur Definition von Codeblöcken
  - Standard: 4 Leerzeichen pro Einrückungsebene
  - **Konsistenz ist verpflichtend**: Mische niemals Leerzeichen und Tabs
  - Alle Zeilen eines Blocks müssen gleich eingerückt sein
  - Falsche Einrückung führt zu `IndentationError`
  - Beispiel:
    ```python
    if bedingung:
        # Dieser Block ist eingerückt (Teil des if)
        anweisung1
        anweisung2
        if nested_bedingung:
            # Verschachtelt: doppelte Einrückung
            anweisung3
    # Hier endet der Block (keine Einrückung mehr)
    ```
  - **Vorteil**: Erzwingt lesbaren Code, keine geschweiften Klammern nötig
  - **Nachteil**: Kann bei Copy-Paste zu Fehlern führen, wenn Einrückung nicht passt

- **Verschachtelte Bedingungen** (Nesting)
  - if-Anweisungen können innerhalb anderer if-Anweisungen platziert werden
  - Jede Verschachtelungsebene erhöht die Einrückung um 4 Leerzeichen
  - Beispiel:
    ```python
    if ist_premium:
        if bestellwert >= 100:
            rabatt = 0.20
        else:
            rabatt = 0.10
    else:
        if bestellwert >= 100:
            rabatt = 0.05
        else:
            rabatt = 0.0
    ```
  - **Best Practice**: Vermeide zu tiefe Verschachtelung (max. 2-3 Ebenen)
  - **Alternative**: Logische Operatoren (`and`, `or`) oder frühe Returns (in Funktionen)

- **Reihenfolge der Bedingungen** (Evaluation Order)
  - Bei if-elif-else werden Bedingungen **von oben nach unten** geprüft
  - **Sobald eine Bedingung `True` ist**, wird der Block ausgeführt und alle weiteren Bedingungen übersprungen
  - Wichtig für **überlappende Bedingungen**: Spezifischere Bedingungen zuerst
  - Beispiel:
    ```python
    # Richtig: Von spezifisch zu allgemein
    if x > 100:
        print("Sehr groß")
    elif x > 50:
        print("Groß")
    elif x > 0:
        print("Positiv")
    
    # Falsch: Zu allgemeine Bedingung zuerst
    if x > 0:
        print("Positiv")  # Fängt ALLE positiven Zahlen, auch > 100
    elif x > 100:
        print("Sehr groß")  # Wird nie erreicht!
    ```

- **Mehrere separate if vs. if-elif-else**
  - **Mehrere separate if**: Alle Bedingungen werden immer geprüft
    ```python
    if temperatur < 0:
        print("Gefroren")
    if temperatur >= 0 and temperatur < 20:
        print("Kühl")
    if temperatur >= 20:
        print("Warm")
    # Alle drei if-Blöcke werden geprüft (ineffizient)
    ```
  - **if-elif-else**: Nur bis zur ersten erfüllten Bedingung
    ```python
    if temperatur < 0:
        print("Gefroren")
    elif temperatur < 20:
        print("Kühl")
    else:
        print("Warm")
    # Nur die erste zutreffende Bedingung wird ausgeführt (effizienter)
    ```
  - **Wann welches?**
    - Verwende **separate if**, wenn Bedingungen **unabhängig** sind (mehrere können gleichzeitig zutreffen)
    - Verwende **if-elif-else**, wenn Bedingungen **sich gegenseitig ausschließen**

### Konzepte und Best Practices

- **Doppelpunkt nicht vergessen**: Nach `if`, `elif`, `else` ist der Doppelpunkt syntaktisch erforderlich
- **Konsistente Einrückung**: Immer 4 Leerzeichen verwenden, keine Tabs mischen
- **`==` für Vergleiche, `=` für Zuweisungen**: Häufiger Anfängerfehler
- **Spezifische Bedingungen zuerst**: Bei if-elif-else von spezifisch zu allgemein prüfen
- **elif statt mehrerer if**: Für sich ausschließende Fälle effizienter
- **Ternärer Operator sparsam**: Nur für einfache, gut lesbare Fälle
- **Verschachtelung begrenzen**: Nicht tiefer als 2-3 Ebenen, sonst refaktorieren

### Notizen

- Python 2.5 führte den ternären Operator ein (PEP 308), vorher gab es nur `and`/`or`-Workarounds
- Die Einrückungssyntax ist eine der charakteristischen Eigenschaften von Python, inspiriert von ABC
- `pass` ist auch in Funktionen, Klassen und Exception-Handling nützlich (wird in späteren Vorlesungen behandelt)
- Die Kombination von if-elif-else mit logischen Operatoren aus V04 ermöglicht sehr ausdrucksstarke Bedingungen
- Bedingte Ausführung ist eine der drei Grundstrukturen der strukturierten Programmierung (Sequenz, Verzweigung, Schleife)

---

## V06 (2026-01-02) – Schleifen (for, while) – Teil 1

### Neu eingeführt

#### Kontrollstrukturen: Schleifen

- **`for`-Schleife** (Python Keyword)
  - Iteriert über alle Elemente einer Sequenz (Iterable)
  - Syntax: `for variable in iterable:`
  - Der Schleifenkörper muss eingerückt sein (Standard: 4 Leerzeichen)
  - Die Schleifenvariable erhält in jedem Durchlauf den Wert des aktuellen Elements
  - Signatur: `for variable in iterable:`
  - Beispiel:
    ```python
    for i in range(5):
        print(i)  # Gibt 0, 1, 2, 3, 4 aus
    ```
  - **Wichtig**: Die Schleifenvariable sollte nicht im Schleifenkörper modifiziert werden (hat keine Auswirkung auf die Iteration)

- **`while`-Schleife** (Python Keyword)
  - Wiederholt einen Codeblock, solange eine Bedingung `True` ist
  - Syntax: `while bedingung:`
  - Kopfgesteuerte Schleife: Bedingung wird vor jedem Durchlauf geprüft
  - Der Schleifenkörper muss eingerückt sein
  - Signatur: `while condition:`
  - Beispiel:
    ```python
    x = 0
    while x < 5:
        print(x)
        x += 1  # Wichtig: Bedingung muss irgendwann False werden
    ```
  - **Warnung**: Ohne korrekte Abbruchbedingung entsteht eine Endlos-Schleife

#### Built-in Funktionen

- **`range(start=0, stop, step=1)`** (Built-in, Python 3.0+)
  - Erzeugt eine Sequenz von Ganzzahlen
  - In Python 3 ist `range()` ein spezieller Typ (kein Generator), der speicher-effizient arbeitet
  - Parameter:
    - `start`: Startwert (inklusive, Standard: 0)
    - `stop`: Endwert (exklusive, erforderlich)
    - `step`: Schrittweite (Standard: 1, kann auch negativ sein)
  - Signatur: `range(stop)` oder `range(start, stop)` oder `range(start, stop, step)` → `range`
  - Beispiel: `range(5)` → 0, 1, 2, 3, 4
  - Beispiel: `range(1, 6)` → 1, 2, 3, 4, 5
  - Beispiel: `range(0, 10, 2)` → 0, 2, 4, 6, 8
  - Beispiel: `range(10, 0, -1)` → 10, 9, 8, ..., 1 (Countdown)
  - **Wichtig**: `stop` ist immer exklusive

- **`enumerate(iterable, start=0)`** (Built-in)
  - Gibt ein Iterator-Objekt zurück, das Tupel aus Index und Wert erzeugt
  - Ermöglicht gleichzeitigen Zugriff auf Index und Element beim Iterieren
  - Parameter:
    - `iterable`: Die Sequenz, über die iteriert wird
    - `start`: Startwert für den Index (Standard: 0)
  - Signatur: `enumerate(iterable, start=0)` → `enumerate`
  - Rückgabe: Iterator von Tupeln `(index, element)`
  - Beispiel: 
    ```python
    fruechte = ['Apfel', 'Banane', 'Kirsche']
    for i, frucht in enumerate(fruechte):
        print(f"{i}: {frucht}")
    # Ausgabe:
    # 0: Apfel
    # 1: Banane
    # 2: Kirsche
    ```
  - Beispiel mit `start=1`:
    ```python
    for nr, frucht in enumerate(fruechte, start=1):
        print(f"{nr}. {frucht}")
    # Ausgabe:
    # 1. Apfel
    # 2. Banane
    # 3. Kirsche
    ```

#### Konzepte und Sprachmerkmale

- **String-Iteration**
  - Strings sind in Python Sequenzen von Zeichen
  - Die `for`-Schleife kann direkt über Zeichen eines Strings iterieren
  - Syntax: `for zeichen in text:`
  - Beispiel:
    ```python
    for buchstabe in "Python":
        print(buchstabe)  # P, y, t, h, o, n
    ```
  - Nützlich für Textanalyse, Validierung, Zeichenzählung

- **Akkumulation (Accumulation)**
  - Schrittweises Aufbauen eines Ergebnisses über mehrere Schleifendurchläufe
  - Variable wird vor der Schleife initialisiert und in jedem Durchlauf aktualisiert
  - **Summation**: `summe = 0`, dann `summe += wert`
  - **Produkt**: `produkt = 1`, dann `produkt *= wert`
  - **String-Konkatenation**: `text = ""`, dann `text += zeichen` (ineffizient, siehe Warnung in V06-Skript)
  - **Wichtig**: Korrekte Initialisierung (0 für Addition, 1 für Multiplikation)

- **Zählen (Counting)**
  - Spezialfall der Akkumulation: Häufigkeit von Ereignissen zählen
  - Variable wird mit 0 initialisiert
  - Bei jedem relevanten Ereignis: `zaehler += 1`
  - Beispiel: Gerade Zahlen zählen mit `if zahl % 2 == 0: anzahl_gerade += 1`

- **Endlos-Schleifen vermeiden**
  - Eine `while`-Schleife muss eine Abbruchbedingung haben, die irgendwann `False` wird
  - Häufiger Fehler: Schleifenvariable wird nicht im Schleifenkörper modifiziert
  - Checkliste:
    1. Wird die relevante Variable im Schleifenkörper geändert?
    2. Führt die Änderung dazu, dass die Bedingung irgendwann `False` wird?
    3. Gibt es einen garantierten Abbruch?
  - Notfall-Abbruch in der Konsole: Strg+C (KeyboardInterrupt)

- **`for` vs. `while`: Wann welche?**
  - **`for`**: Wenn Anzahl der Durchläufe bekannt oder über Sequenz iteriert wird
  - **`while`**: Wenn Anzahl der Durchläufe unbekannt, abhängig von dynamischer Bedingung
  - **`for`** ist idiomatischer für Iterationen über Collections
  - **`while`** ist idiomatischer für Eingabevalidierung und ereignisgesteuerte Schleifen

### Konzepte und Best Practices

- **`range()` exklusive Obergrenze**: `range(10)` erzeugt 0-9, nicht 0-10. Für 1-10: `range(1, 11)`
- **Schleifenvariable in `for` nicht modifizieren**: Hat keine Auswirkung auf die Iteration, da sie in jedem Durchlauf neu zugewiesen wird
- **Akkumulation richtig initialisieren**: `summe = 0` für Addition, `produkt = 1` für Multiplikation
- **String-Konkatenation in Schleifen vermeiden**: Ineffizient wegen Immutability. Besser: Liste aufbauen und mit `.join()` verbinden (V08)
- **`enumerate()` statt manueller Indexzählung**: Pythonischer und fehlerresistenter
- **Abbruchbedingungen in `while` sorgfältig prüfen**: Endlos-Schleifen sind ein häufiger Fehler

### Notizen

- `range()` in Python 2 erzeugte eine Liste, in Python 3 ein spezielles Range-Objekt (speicher-effizienter)
- `enumerate()` wurde in Python 2.3 eingeführt
- Die `for`-Schleife in Python entspricht eher einer "for-each"-Schleife in anderen Sprachen (iteriert über Elemente, nicht über Indizes)
- Python hat keine klassische C-Style `for(i=0; i<n; i++)`-Schleife, `for i in range(n)` ist das Äquivalent
- `while True:` mit `break` ist ein idiomatisches Muster für "mindestens einmal ausführen" (fußgesteuerte Schleife)
- Fortgeschrittene Schleifenkonzepte (`break`, `continue`, `else` bei Schleifen, List Comprehensions) werden in V07 behandelt

---

## V07 (2026-01-03) – Schleifen (for, while) – Teil 2

### Neu eingeführt

#### Schleifensteuerungs-Statements

- **`break`-Statement** (Python Keyword, Python 1.0+)
  - Bricht die umschließende Schleife sofort ab
  - Führt zur Ausführung des Codes nach der Schleife
  - Bei verschachtelten Schleifen: Bricht nur die innerste Schleife ab
  - Syntax: `break`
  - Signatur: `break`
  - Beispiel:
    ```python
    for i in range(10):
        if i == 5:
            break  # Schleife endet bei i=5
        print(i)  # Gibt 0, 1, 2, 3, 4 aus
    ```
  - **Verwendung**: Vorzeitiger Schleifenabbruch bei erfüllter Bedingung (z.B. Suche erfolgreich)

- **`continue`-Statement** (Python Keyword, Python 1.0+)
  - Überspringt den Rest des aktuellen Schleifendurchlaufs
  - Springt sofort zur nächsten Iteration (bei `for`) oder zur Bedingungsprüfung (bei `while`)
  - Syntax: `continue`
  - Signatur: `continue`
  - Beispiel:
    ```python
    for i in range(10):
        if i % 2 == 0:
            continue  # Überspringe gerade Zahlen
        print(i)  # Gibt nur 1, 3, 5, 7, 9 aus
    ```
  - **Verwendung**: Überspringen ungültiger/ungewünschter Elemente ohne tiefe Verschachtelung

#### Loop `else`-Klausel

- **Loop `else`-Klausel** (Python Sprachfeature, Python 1.0+)
  - `else`-Block nach Schleife wird ausgeführt, wenn Schleife **normal** beendet wurde (ohne `break`)
  - Funktioniert sowohl mit `for` als auch `while`-Schleifen
  - Syntax: 
    ```python
    for item in iterable:
        if bedingung:
            break
    else:
        # Wird nur ausgeführt, wenn break NICHT aufgerufen wurde
        pass
    ```
  - Signatur: `for/while ... else:`
  - Beispiel (Primzahl-Test):
    ```python
    n = 29
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} ist keine Primzahl")
            break
    else:
        # else wird nur ausgeführt, wenn kein break kam
        print(f"{n} ist eine Primzahl")
    ```
  - **Semantik**: "Wenn Schleife nicht unterbrochen wurde, dann..."
  - **Verwendung**: Suchen mit Erfolgsprüfung, Validierung aller Elemente

#### List Comprehensions

- **List Comprehension** (Python Sprachfeature, Python 2.0+, PEP 202)
  - Kompakte Syntax zum Erstellen von Listen aus Iterables
  - Syntax: `[expression for item in iterable]`
  - Mit Bedingung: `[expression for item in iterable if condition]`
  - Signatur: `[expr for var in iterable if condition]` → `list`
  - Beispiel:
    ```python
    # Klassische Schleife:
    quadrate = []
    for i in range(10):
        quadrate.append(i ** 2)
    
    # List Comprehension:
    quadrate = [i ** 2 for i in range(10)]
    ```
  - Mit Filter:
    ```python
    # Nur gerade Quadrate:
    gerade_quadrate = [i ** 2 for i in range(10) if i % 2 == 0]
    ```
  - **Vorteile**: Kürzer, lesbarer, oft schneller als explizite Schleife
  - **Wichtig**: Nur für einfache Transformationen verwenden; bei komplexer Logik normale Schleife bevorzugen

- **Verschachtelte List Comprehensions** (Python 2.0+)
  - Mehrere `for`-Klauseln für mehrdimensionale Iteration
  - Syntax: `[expr for item1 in iter1 for item2 in iter2]`
  - Entspricht verschachtelten Schleifen: äußere Schleife zuerst, innere danach
  - Beispiel:
    ```python
    # Klassisch:
    paare = []
    for x in [1, 2, 3]:
        for y in ['a', 'b']:
            paare.append((x, y))
    
    # List Comprehension:
    paare = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
    # Ergebnis: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]
    ```

#### Set und Dictionary Comprehensions (Vorschau)

- **Set Comprehension** (Python 2.7+ / 3.0+, PEP 274)
  - Analog zu List Comprehension, erstellt aber ein Set (eindeutige Elemente)
  - Syntax: `{expression for item in iterable if condition}`
  - Beispiel: `eindeutige_buchstaben = {c.lower() for c in "Hallo Welt"}`
  - **Hinweis**: Wird in V07 erwähnt, aber erst in V08 ausführlich behandelt

- **Dictionary Comprehension** (Python 2.7+ / 3.0+, PEP 274)
  - Erstellt Dictionaries mit Schlüssel-Wert-Paaren
  - Syntax: `{key_expr: value_expr for item in iterable if condition}`
  - Beispiel: `quadrate_dict = {x: x**2 for x in range(5)}`  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  - **Hinweis**: Wird in V07 erwähnt, aber erst in V08 ausführlich behandelt

#### Module: `string`

- **`string`-Modul** (Standard Library)
  - Enthält vordefinierte Konstanten für Zeichensets
  - Import: `import string`
  
  - **`string.ascii_uppercase`** (Konstante)
    - String mit allen Großbuchstaben: `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
    - Beispiel: `import string; print(string.ascii_uppercase)`
  
  - **`string.ascii_lowercase`** (Konstante)
    - String mit allen Kleinbuchstaben: `'abcdefghijklmnopqrstuvwxyz'`
    - Beispiel: `kleinbuchstaben = string.ascii_lowercase`
  
  - **`string.ascii_letters`** (Konstante)
    - Kombination aus `ascii_lowercase` und `ascii_uppercase`
    - Beispiel: `buchstaben = string.ascii_letters`
  
  - **`string.digits`** (Konstante)
    - String mit allen Ziffern: `'0123456789'`
    - Beispiel: `ziffern = string.digits`
  
  - **`string.punctuation`** (Konstante)
    - String mit allen ASCII-Satzzeichen: `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
    - Beispiel: `sonderzeichen = string.punctuation`
  
  - **Verwendung**: Nützlich für Passwortgenerierung, Validierung, Zeichenfilterung

#### Module: `random`

- **`random`-Modul** (Standard Library)
  - Funktionen zur Erzeugung von Zufallszahlen und zufälligen Auswahlen
  - Import: `import random`
  
  - **`random.choice(seq)`** (Funktion)
    - Wählt ein zufälliges Element aus einer nicht-leeren Sequenz
    - Signatur: `random.choice(seq)` → Element
    - Beispiel: `zufalls_buchstabe = random.choice('ABCDE')`
    - Wirft `IndexError` bei leerer Sequenz
  
  - **`random.shuffle(liste)`** (Funktion)
    - Mischt die Liste **in-place** (modifiziert Original)
    - Gibt `None` zurück
    - Signatur: `random.shuffle(x)` → `None`
    - Beispiel:
      ```python
      karten = ['A', 'K', 'D', 'B']
      random.shuffle(karten)
      print(karten)  # ['D', 'A', 'B', 'K'] (zufällige Reihenfolge)
      ```
    - **Wichtig**: Funktioniert nur mit veränderbaren Sequenzen (Listen, nicht Strings/Tupel)
  
  - **`random.randint(a, b)`** (Funktion)
    - Gibt zufällige Ganzzahl N mit `a <= N <= b` zurück (beide Grenzen inklusive!)
    - Signatur: `random.randint(a, b)` → `int`
    - Beispiel: `wuerfel = random.randint(1, 6)`  # 1, 2, 3, 4, 5 oder 6
    - **Unterschied zu `range()`**: Beide Grenzen sind inklusive!

#### Reguläre Ausdrücke (Einführung)

- **`re`-Modul** (Standard Library)
  - Modul für reguläre Ausdrücke (Pattern Matching)
  - Import: `import re`
  
  - **`re.split(pattern, string)`** (Funktion)
    - Teilt String an allen Stellen, die dem Pattern entsprechen
    - Signatur: `re.split(pattern, string, maxsplit=0, flags=0)` → `list[str]`
    - Beispiel:
      ```python
      import re
      text = "Hallo! Wie geht es? Gut."
      saetze = re.split(r'[.!?]+', text)
      # Ergebnis: ['Hallo', ' Wie geht es', ' Gut', '']
      ```
    - Pattern `r'[.!?]+'`: Ein oder mehr Satzzeichen (`.`, `!`, `?`)
  
  - **`re.findall(pattern, string)`** (Funktion)
    - Findet alle nicht-überlappenden Vorkommen des Patterns
    - Gibt Liste von Strings zurück
    - Signatur: `re.findall(pattern, string, flags=0)` → `list[str]`
    - Beispiel:
      ```python
      zahlen = re.findall(r'\b\d+(?:[.,]\d+)?\b', "Preis: 19,99 und 5.50")
      # Ergebnis: ['19,99', '5.50']
      ```
    - Pattern-Erklärung:
      - `\b`: Wortgrenze
      - `\d+`: Eine oder mehr Ziffern
      - `(?:[.,]\d+)?`: Optional: Komma/Punkt gefolgt von Ziffern
  
  - **Hinweis**: Reguläre Ausdrücke werden in V07 nur grundlegend eingeführt; ausführliche Behandlung erfolgt in späteren Vorlesungen

#### Konzepte und Sprachmerkmale

- **Verschachtelte Schleifen (Nested Loops)**
  - Schleife innerhalb einer anderen Schleife
  - Jede Iteration der äußeren Schleife führt alle Iterationen der inneren Schleife aus
  - Syntax:
    ```python
    for i in range(3):
        for j in range(3):
            print(f"({i}, {j})")
    ```
  - **Komplexität**: O(n × m) für zwei Schleifen mit n und m Iterationen
  - **Verwendung**: Mehrdimensionale Datenstrukturen, Kombinationen, Muster

- **`break` in verschachtelten Schleifen**
  - `break` bricht nur die **innerste** Schleife ab
  - Äußere Schleife läuft weiter
  - Beispiel:
    ```python
    for i in range(3):
        for j in range(3):
            if j == 1:
                break  # Bricht nur die j-Schleife ab
            print(f"({i}, {j})")
    # Ausgabe: (0, 0), (1, 0), (2, 0)
    ```
  - **Workaround für "break beide Schleifen"**: Flag-Variable oder Funktion mit `return`

- **Generator Expressions** (Python 2.4+, Vorschau)
  - Ähnlich List Comprehension, aber mit runden Klammern: `(expr for item in iter)`
  - Erzeugt Generator statt Liste (lazy evaluation, speicher-effizienter)
  - Beispiel: `summe = sum(i**2 for i in range(1000000))`
  - **Hinweis**: Wird in V07 nur erwähnt, ausführliche Behandlung in späteren Vorlesungen

### Konzepte und Best Practices

- **`break` für Erfolgsprüfung mit `else`**: Idiomatisches Pattern für "element gefunden" vs. "nicht gefunden"
- **`continue` statt tiefer Verschachtelung**: Verbessert Lesbarkeit durch "early skip"
- **List Comprehensions für einfache Transformationen**: Kürzer und oft performanter als explizite Schleifen
- **Reguläre Schleifen für komplexe Logik**: List Comprehensions sollten nicht zu komplex werden (max. 1-2 Zeilen)
- **`string`-Modul für Zeichensets**: Besser als manuelles `'ABCDEFG...'` (weniger fehleranfällig, internationale Unterstützung)
- **`random.shuffle()` modifiziert in-place**: Keine Zuweisung nötig (`random.shuffle(liste)`, nicht `liste = random.shuffle(liste)`)

### Notizen

- `break` und `continue` existieren seit Python 1.0
- Loop `else` ist ein einzigartiges Python-Feature, das in vielen anderen Sprachen nicht existiert
- List Comprehensions wurden in Python 2.0 eingeführt (PEP 202)
- Set und Dict Comprehensions wurden in Python 2.7/3.0 hinzugefügt (PEP 274)
- `random.randint(a, b)` ist **inklusive** beider Grenzen (anders als `range()`)
- Generator Expressions wurden in Python 2.4 eingeführt (PEP 289)
- Reguläre Ausdrücke sind mächtiges Werkzeug, können aber schwer lesbar werden – verwende sie sparsam

---

## V08 (2026-01-03) – Listen & Datenstrukturen

### Neu eingeführt

#### Datentypen

- **`list`** (Built-in Typ, Python 1.0+)
  - Veränderbare (mutable) Sequenz, die beliebige Objekte aufnehmen kann
  - Elemente können unterschiedliche Datentypen haben
  - Zugriff über Index (0-basiert)
  - Syntax: `[element1, element2, ...]` oder `list(iterable)`
  - Signatur: `list()` → leere Liste oder `list(iterable)` → Liste aus Iterable
  - Beispiel: `zahlen = [1, 2, 3, 4, 5]`, `gemischt = [1, "Hallo", 3.14, True]`
  - **Wichtig**: Listen sind mutable – Änderungen wirken auf das Original-Objekt

- **`tuple`** (Built-in Typ, Python 1.0+)
  - Unveränderbare (immutable) Sequenz, ähnlich wie Listen
  - Nach Erstellung können Elemente nicht mehr geändert, hinzugefügt oder entfernt werden
  - Verwendung: Für Daten, die nicht verändert werden sollen (z.B. Koordinaten)
  - Syntax: `(element1, element2, ...)` oder `tuple(iterable)`
  - Bei einem Element: `(element,)` – Komma erforderlich!
  - Signatur: `tuple()` → leeres Tupel oder `tuple(iterable)` → Tupel aus Iterable
  - Beispiel: `koordinaten = (3, 4)`, `farbe = (255, 128, 0)`, `ein_element = (42,)`
  - **Vorteile**: Schneller als Listen, können als Dictionary-Keys verwendet werden, schützen vor unbeabsichtigten Änderungen

---

## V09 (2026-01-03) – Listen & Datenstrukturen – Teil 2 / Try-Catch (Fehlerbehandlung)

### Neu eingeführt

#### Fehlerbehandlung (Exception Handling)

- **`try`-Statement** (Python Keyword, Python 1.0+)
  - Definiert einen Codeblock, in dem Fehler (Exceptions) auftreten können
  - Syntax: `try:`
  - Muss mindestens einen `except`-Block oder einen `finally`-Block haben
  - Signatur: `try:`
  - Beispiel:
    ```python
    try:
        zahl = int(input("Zahl: "))
        ergebnis = 10 / zahl
        print(f"Ergebnis: {ergebnis}")
    except ValueError:
        print("Ungültige Eingabe!")
    except ZeroDivisionError:
        print("Division durch 0!")
    ```
  - **Wichtig**: Exceptions werden vom engsten passenden `except`-Block abgefangen

- **`except`-Klausel** (Python Keyword, Python 1.0+)
  - Definiert Fehlerbehandlung für spezifische Exception-Typen
  - Syntax: `except ExceptionType:` oder `except (Type1, Type2):` oder `except ExceptionType as e:`
  - Kann mehrfach verwendet werden für verschiedene Exception-Typen
  - Signatur: `except [ExceptionType [as variable]]:`
  - Beispiele:
    ```python
    except ValueError:                    # Fängt ValueError ab
        pass
    
    except (TypeError, KeyError):         # Fängt beide Typen ab
        pass
    
    except FileNotFoundError as e:        # Zugriff auf Exception-Objekt
        print(f"Fehler: {e}")
    ```
  - **Best Practice**: Spezifische Exceptions vor generischen abfangen

- **`else`-Klausel (bei try)** (Python Keyword, Python 1.0+)
  - Wird ausgeführt, wenn **keine** Exception im `try`-Block auftritt
  - Syntax: `else:` (nach allen `except`-Klauseln, vor `finally`)
  - Optional, aber nützlich zur Trennung von "erfolgreicher Code" und "Fehlerbehandlung"
  - Signatur: `else:`
  - Beispiel:
    ```python
    try:
        datei = open("daten.txt", "r")
    except FileNotFoundError:
        print("Datei nicht gefunden")
    else:
        # Wird nur ausgeführt, wenn open() erfolgreich war
        inhalt = datei.read()
        datei.close()
    ```
  - **Vorteil**: Code im `else`-Block wird nicht von `except` abgefangen

- **`finally`-Klausel** (Python Keyword, Python 2.5+)
  - Wird **immer** ausgeführt, unabhängig davon, ob Exception auftrat oder nicht
  - Syntax: `finally:` (nach allen `except` und `else`-Klauseln)
  - Verwendung: Aufräumarbeiten (Dateien schließen, Verbindungen trennen)
  - Signatur: `finally:`
  - Beispiel:
    ```python
    try:
        datei = open("daten.txt", "r")
        inhalt = datei.read()
    except FileNotFoundError:
        print("Datei nicht gefunden")
    finally:
        # Wird IMMER ausgeführt, auch bei Exception
        if 'datei' in locals():
            datei.close()
    ```
  - **Wichtig**: Wird auch ausgeführt bei `return`, `break` oder `continue` im `try`-Block

- **`raise`-Statement** (Python Keyword, Python 1.0+)
  - Wirft eine Exception (explizit)
  - Syntax: `raise ExceptionType(message)` oder `raise` (in `except`-Block zum Weiterwerfen)
  - Signatur: `raise [ExceptionType[(args)]]`
  - Beispiele:
    ```python
    raise ValueError("Ungültiger Wert")
    
    if alter < 0:
        raise ValueError("Alter darf nicht negativ sein")
    
    try:
        # Code...
    except ValueError:
        print("Fehler aufgetreten")
        raise  # Wirft die gleiche Exception weiter
    ```
  - **Verwendung**: Validierung, benutzerdefinierte Fehler signalisieren

#### Exception-Typen (Built-in)

- **`Exception`** (Built-in Klasse)
  - Basisklasse für alle benutzerdefinierten Exceptions
  - Sollte nicht direkt geworfen werden, sondern als Basis für eigene Exceptions dienen
  - Signatur: `class MeineException(Exception):`
  - Beispiel:
    ```python
    class AlterFehler(Exception):
        """Exception für ungültige Alterswerte."""
        pass
    ```

- **`ValueError`** (Built-in Exception)
  - Wird geworfen, wenn Funktion richtigen Typ, aber ungültigen Wert erhält
  - Beispiele: `int("abc")`, `math.sqrt(-1)` (ohne complex)
  - Signatur: `ValueError(message)`
  - Verwendung: Validierung von Werten
  - Beispiel: `raise ValueError("Zahl muss positiv sein")`

- **`TypeError`** (Built-in Exception)
  - Wird geworfen bei falschen Datentypen
  - Beispiele: `"5" + 5`, `len(42)`, `dict[0]` (bei nicht-dict)
  - Signatur: `TypeError(message)`
  - Verwendung: Typ-Validierung
  - Beispiel: `raise TypeError("Argument muss String sein")`

- **`KeyError`** (Built-in Exception)
  - Wird geworfen bei Zugriff auf nicht-existierenden Dictionary-Key
  - Beispiel: `{'a': 1}['b']`
  - Signatur: `KeyError(key)`
  - Verwendung: Dictionary-Zugriff absichern
  - Alternative: `.get(key, default)` statt `[key]`

- **`FileNotFoundError`** (Built-in Exception, Python 3.3+)
  - Wird geworfen, wenn Datei nicht existiert
  - Unterklasse von `OSError`
  - Beispiel: `open("nicht_vorhanden.txt")`
  - Signatur: `FileNotFoundError(message)`
  - Verwendung: Datei-Operationen absichern

- **`PermissionError`** (Built-in Exception, Python 3.3+)
  - Wird geworfen bei fehlenden Zugriffsrechten
  - Unterklasse von `OSError`
  - Beispiel: `open("/root/secret.txt")` ohne Root-Rechte
  - Signatur: `PermissionError(message)`
  - Verwendung: Datei-/Verzeichnis-Operationen absichern

- **`IndexError`** (Built-in Exception)
  - Wird geworfen bei Zugriff außerhalb der Sequenz-Grenzen
  - Beispiel: `[1, 2, 3][10]`
  - Signatur: `IndexError(message)`
  - Verwendung: List-/Tupel-Zugriff validieren

- **`ZeroDivisionError`** (Built-in Exception)
  - Wird geworfen bei Division durch Null
  - Beispiel: `10 / 0`
  - Signatur: `ZeroDivisionError(message)`
  - Verwendung: Division absichern

#### Module und Funktionen

- **`json`-Modul** (Standard Library, Python 2.6+)
  - Modul zum Arbeiten mit JSON-Daten (JavaScript Object Notation)
  - Import: `import json`
  
  - **`json.load(file_object)`** (Funktion)
    - Liest JSON aus einer geöffneten Datei
    - Signatur: `json.load(fp)` → `object` (dict, list, str, int, float, bool, None)
    - Beispiel:
      ```python
      with open("config.json", "r") as datei:
          daten = json.load(datei)
      ```
    - Wirft `json.JSONDecodeError` bei ungültigem JSON
  
  - **`json.dump(obj, file_object)`** (Funktion)
    - Schreibt Python-Objekt als JSON in eine Datei
    - Signatur: `json.dump(obj, fp, indent=None, ensure_ascii=True)`
    - Parameter:
      - `indent`: Anzahl Leerzeichen für Formatierung (z.B. `4`)
      - `ensure_ascii`: `False` für Umlaute/Unicode-Zeichen
    - Beispiel:
      ```python
      daten = {"name": "Alice", "alter": 25}
      with open("daten.json", "w") as datei:
          json.dump(daten, datei, indent=4, ensure_ascii=False)
      ```
  
  - **`json.JSONDecodeError`** (Exception, Python 3.5+)
    - Exception bei ungültigem JSON-Format
    - Unterklasse von `ValueError`
    - Enthält Details über Fehlerposition
    - Beispiel:
      ```python
      try:
          daten = json.loads("{invalid json}")
      except json.JSONDecodeError as e:
          print(f"JSON-Fehler in Zeile {e.lineno}, Spalte {e.colno}")
      ```

#### Konzepte und Sprachmerkmale

- **Exception-Hierarchie**
  - Alle Exceptions erben von `BaseException`
  - Benutzerdefinierte Exceptions sollten von `Exception` erben
  - Hierarchie-Beispiel:
    ```
    BaseException
    ├── Exception
    │   ├── ValueError
    │   ├── TypeError
    │   ├── KeyError
    │   ├── OSError
    │   │   ├── FileNotFoundError
    │   │   └── PermissionError
    │   └── ... (viele weitere)
    └── SystemExit, KeyboardInterrupt, ... (sollten selten abgefangen werden)
    ```
  - **Best Practice**: Fange niemals `BaseException` ab (würde auch `KeyboardInterrupt` abfangen)

- **Benutzerdefinierte Exceptions**
  - Eigene Exception-Klassen durch Ableitung von `Exception`
  - Syntax:
    ```python
    class MeineException(Exception):
        """Docstring erklärt den Zweck."""
        pass
    ```
  - Erweiterte Version mit `__init__`:
    ```python
    class ValidationError(Exception):
        def __init__(self, feld, wert):
            self.feld = feld
            self.wert = wert
            super().__init__(f"Ungültiger Wert '{wert}' für Feld '{feld}'")
    ```
  - **Verwendung**: Domänenspezifische Fehler modellieren

- **Exception-Objekt zugreifen**
  - `except ExceptionType as e:` ermöglicht Zugriff auf Exception-Objekt
  - Exception-Objekte haben `.args`-Attribut (Tupel mit Argumenten)
  - String-Repräsentation: `str(e)` gibt Fehlermeldung zurück
  - Beispiel:
    ```python
    try:
        int("abc")
    except ValueError as e:
        print(f"Fehlertyp: {type(e).__name__}")  # ValueError
        print(f"Fehlermeldung: {e}")             # invalid literal...
        print(f"Args: {e.args}")                  # ("invalid literal...",)
    ```

- **Multiple Exception-Typen**
  - Syntax: `except (Type1, Type2, Type3) as e:`
  - Fängt alle genannten Typen mit einem Block ab
  - Beispiel:
    ```python
    try:
        # Code...
    except (ValueError, TypeError, KeyError) as e:
        print(f"Eingabefehler: {e}")
    ```

- **Best Practices für Exception Handling**
  - **Spezifisch abfangen**: `except ValueError:` statt `except:`
  - **Nicht leer lassen**: `pass` nur wenn bewusst nichts getan werden soll
  - **Nicht alles abfangen**: `except Exception:` nur in seltenen Fällen
  - **Exceptions dokumentieren**: Docstrings sollten mögliche Exceptions auflisten
  - **Fail Fast**: Validiere früh, wirf Exceptions sofort
  - **else für Erfolgsfall**: Trenne normalen Code von Fehlerbehandlung
  - **finally für Cleanup**: Ressourcen immer freigeben

### Notizen

- `try-except` existiert seit Python 1.0, `finally` seit Python 2.5, `else` seit Python 1.5
- `FileNotFoundError` und `PermissionError` wurden in Python 3.3 eingeführt (vorher: `IOError` oder `OSError`)
- `json.JSONDecodeError` wurde in Python 3.5 hinzugefügt
- `with`-Statement (Context Manager) ist oft besser als manuelles `try-finally` für Ressourcen-Management
- Exception-Handling hat Overhead – verwende es nur wo nötig, nicht für normalen Programmfluss
- Python folgt dem EAFP-Prinzip: "Easier to Ask for Forgiveness than Permission" (try-except statt vorherige Prüfung)
- Alternativen zu try-except:
  - `.get(key, default)` für Dictionaries statt `try-except KeyError`
  - `.isdigit()` vor `int()` statt `try-except ValueError`
  - `if os.path.exists()` vor `open()` (aber Race Condition möglich!)

#### List-Methoden

- **`.append(element)`** (List-Methode)
  - Fügt ein Element am Ende der Liste hinzu (in-place)
  - Gibt `None` zurück (modifiziert Original)
  - Signatur: `list.append(x)` → `None`
  - Beispiel: `zahlen = [1, 2, 3]; zahlen.append(4)` → `zahlen` ist jetzt `[1, 2, 3, 4]`
  - **Zeitkomplexität**: O(1) – Amortized Constant Time

- **`.insert(index, element)`** (List-Methode)
  - Fügt ein Element an einer bestimmten Position ein (in-place)
  - Elemente ab `index` werden nach rechts verschoben
  - Signatur: `list.insert(i, x)` → `None`
  - Beispiel: `zahlen = [1, 3, 4]; zahlen.insert(1, 2)` → `zahlen` ist jetzt `[1, 2, 3, 4]`
  - **Zeitkomplexität**: O(n) – Linear, da Elemente verschoben werden müssen

- **`.extend(iterable)`** (List-Methode)
  - Fügt alle Elemente aus einem Iterable am Ende der Liste hinzu (in-place)
  - Gibt `None` zurück
  - Signatur: `list.extend(iterable)` → `None`
  - Beispiel: `a = [1, 2]; a.extend([3, 4])` → `a` ist jetzt `[1, 2, 3, 4]`
  - Unterschied zu `.append()`: `.append([3, 4])` würde die Liste als **ein** Element hinzufügen → `[1, 2, [3, 4]]`
  - **Zeitkomplexität**: O(k), wobei k die Länge des Iterables ist

- **`.remove(element)`** (List-Methode)
  - Entfernt das **erste** Vorkommen eines Elements (in-place)
  - Wirft `ValueError`, wenn Element nicht gefunden
  - Signatur: `list.remove(x)` → `None`
  - Beispiel: `zahlen = [1, 2, 3, 2]; zahlen.remove(2)` → `zahlen` ist jetzt `[1, 3, 2]`
  - **Zeitkomplexität**: O(n) – Muss Liste durchsuchen

- **`.pop(index=-1)`** (List-Methode)
  - Entfernt und gibt das Element an Position `index` zurück (in-place)
  - Standard: `index=-1` (letztes Element)
  - Wirft `IndexError`, wenn Index außerhalb des Bereichs
  - Signatur: `list.pop([i])` → Element
  - Beispiel: `zahlen = [1, 2, 3]; x = zahlen.pop()` → `x` ist `3`, `zahlen` ist `[1, 2]`
  - Beispiel: `zahlen = [1, 2, 3]; x = zahlen.pop(0)` → `x` ist `1`, `zahlen` ist `[2, 3]`
  - **Zeitkomplexität**: O(1) für letztes Element, O(n) für andere Positionen
  - **Verwendung**: Stack-Operationen (Push mit `.append()`, Pop mit `.pop()`)

- **`.clear()`** (List-Methode, Python 3.3+)
  - Entfernt alle Elemente aus der Liste (in-place)
  - Gibt `None` zurück
  - Signatur: `list.clear()` → `None`
  - Beispiel: `zahlen = [1, 2, 3]; zahlen.clear()` → `zahlen` ist jetzt `[]`
  - Äquivalent zu `del zahlen[:]` oder `zahlen = []` (aber `.clear()` ist expliziter)

- **`.index(element, start=0, end=len(liste))`** (List-Methode)
  - Gibt den Index des **ersten** Vorkommens eines Elements zurück
  - Wirft `ValueError`, wenn Element nicht gefunden
  - Optional: Suche in Slice `[start:end]`
  - Signatur: `list.index(x[, start[, end]])` → `int`
  - Beispiel: `zahlen = [1, 2, 3, 2]; zahlen.index(2)` → `1`
  - Beispiel: `zahlen.index(2, 2)` → `3` (Suche ab Index 2)
  - **Zeitkomplexität**: O(n) – Lineare Suche

- **`.count(element)`** (List-Methode)
  - Zählt, wie oft ein Element in der Liste vorkommt
  - Signatur: `list.count(x)` → `int`
  - Beispiel: `zahlen = [1, 2, 3, 2, 2]; zahlen.count(2)` → `3`
  - **Zeitkomplexität**: O(n) – Muss gesamte Liste durchlaufen

- **`.sort(key=None, reverse=False)`** (List-Methode)
  - Sortiert die Liste **in-place** (modifiziert Original)
  - Gibt `None` zurück
  - Parameter:
    - `key`: Funktion, die auf jedes Element angewendet wird zur Sortierung (z.B. `key=len` für Sortierung nach Länge)
    - `reverse`: `True` für absteigende Sortierung
  - Signatur: `list.sort(key=None, reverse=False)` → `None`
  - Beispiel: `zahlen = [3, 1, 4, 1, 5]; zahlen.sort()` → `zahlen` ist `[1, 1, 3, 4, 5]`
  - Beispiel: `zahlen.sort(reverse=True)` → `zahlen` ist `[5, 4, 3, 1, 1]`
  - Beispiel: `woerter = ['aa', 'bbb', 'c']; woerter.sort(key=len)` → `['c', 'aa', 'bbb']`
  - **Zeitkomplexität**: O(n log n) – Timsort-Algorithmus
  - **Unterschied zu `sorted()`**: `.sort()` modifiziert Liste, `sorted()` gibt neue Liste zurück

- **`.reverse()`** (List-Methode)
  - Kehrt die Reihenfolge der Elemente um **in-place**
  - Gibt `None` zurück
  - Signatur: `list.reverse()` → `None`
  - Beispiel: `zahlen = [1, 2, 3]; zahlen.reverse()` → `zahlen` ist `[3, 2, 1]`
  - **Zeitkomplexität**: O(n)

- **`.copy()`** (List-Methode, Python 3.3+)
  - Erstellt eine **flache Kopie** (shallow copy) der Liste
  - Gibt neue Liste zurück
  - Signatur: `list.copy()` → `list`
  - Beispiel: `original = [1, 2, 3]; kopie = original.copy(); kopie.append(4)` → `original` ist `[1, 2, 3]`, `kopie` ist `[1, 2, 3, 4]`
  - Äquivalent zu `liste[:]` oder `list(liste)`
  - **Wichtig**: Bei verschachtelten Listen werden nur die äußeren Referenzen kopiert (shallow copy)!

#### Built-in Funktionen

- **`sorted(iterable, key=None, reverse=False)`** (Built-in, Python 2.4+)
  - Gibt eine **neue sortierte Liste** zurück (Original bleibt unverändert)
  - Funktioniert mit jedem Iterable (Listen, Tupel, Strings, etc.)
  - Parameter wie bei `.sort()`: `key` und `reverse`
  - Signatur: `sorted(iterable, key=None, reverse=False)` → `list`
  - Beispiel: `zahlen = [3, 1, 4]; sortiert = sorted(zahlen)` → `sortiert` ist `[1, 3, 4]`, `zahlen` ist `[3, 1, 4]`
  - Beispiel: `sorted("python")` → `['h', 'n', 'o', 'p', 't', 'y']`
  - **Unterschied zu `.sort()`**: `sorted()` gibt neue Liste zurück, `.sort()` modifiziert Original
  - **Zeitkomplexität**: O(n log n)

- **`sum(iterable, start=0)`** (Built-in)
  - Berechnet die Summe aller Elemente in einem Iterable
  - Parameter `start`: Startwert (Standard: 0), wird zur Summe addiert
  - Signatur: `sum(iterable, start=0)` → `number`
  - Beispiel: `sum([1, 2, 3, 4, 5])` → `15`
  - Beispiel: `sum([1, 2, 3], 10)` → `16` (10 + 1 + 2 + 3)
  - **Funktioniert nicht** mit Strings (verwende `.join()` stattdessen)
  - **Zeitkomplexität**: O(n)

- **`all(iterable)`** (Built-in, Python 2.5+)
  - Gibt `True` zurück, wenn **alle** Elemente im Iterable `True` sind (oder Iterable leer)
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `False`
  - Signatur: `all(iterable)` → `bool`
  - Beispiel: `all([True, True, True])` → `True`
  - Beispiel: `all([True, False, True])` → `False`
  - Beispiel: `all([])` → `True` (Leeres Iterable ist `True`)
  - **Verwendung**: Prüfung, ob alle Bedingungen erfüllt sind
  - Beispiel: `all(x > 0 for x in zahlen)` prüft, ob alle Zahlen positiv

- **`any(iterable)`** (Built-in, Python 2.5+)
  - Gibt `True` zurück, wenn **mindestens ein** Element im Iterable `True` ist
  - Nutzt Kurzschlussauswertung: Stoppt bei erstem `True`
  - Signatur: `any(iterable)` → `bool`
  - Beispiel: `any([False, True, False])` → `True`
  - Beispiel: `any([False, False, False])` → `False`
  - Beispiel: `any([])` → `False` (Leeres Iterable ist `False`)
  - **Verwendung**: Prüfung, ob mindestens eine Bedingung erfüllt ist
  - Beispiel: `any(c.isupper() for c in passwort)` prüft, ob Passwort Großbuchstaben enthält
  - **Hinweis**: Wurde in V04 als Vorschau erwähnt, hier vollständig eingeführt

- **`zip(*iterables)`** (Built-in, Python 2.0+)
  - Verknüpft mehrere Iterables zu einem Iterator von Tupeln
  - Jedes Tupel enthält die i-ten Elemente aller Iterables
  - Stoppt bei kürzestem Iterable
  - Signatur: `zip(*iterables)` → `zip`
  - Beispiel: 
    ```python
    namen = ["Alice", "Bob", "Charlie"]
    alter = [25, 30, 35]
    for name, age in zip(namen, alter):
        print(f"{name} ist {age} Jahre alt")
    # Alice ist 25 Jahre alt
    # Bob ist 30 Jahre alt
    # Charlie ist 35 Jahre alt
    ```
  - Beispiel: `list(zip([1, 2, 3], ['a', 'b', 'c']))` → `[(1, 'a'), (2, 'b'), (3, 'c')]`
  - **Verwendung**: Paralleles Iterieren über mehrere Listen, Verknüpfung von Daten
  - **Zeitkomplexität**: O(1) pro Element (lazy evaluation)

#### Operatoren

- **`+` (Konkatenation)** – Für Listen
  - Verknüpft zwei Listen zu einer neuen Liste
  - Original-Listen bleiben unverändert
  - Signatur: `list1 + list2` → `list`
  - Beispiel: `[1, 2] + [3, 4]` → `[1, 2, 3, 4]`
  - **Unterschied zu `.extend()`**: `+` erstellt neue Liste, `.extend()` modifiziert Original

- **`*` (Repetition)** – Für Listen
  - Wiederholt eine Liste n-mal
  - Signatur: `list * n` → `list`
  - Beispiel: `[0] * 5` → `[0, 0, 0, 0, 0]`
  - Beispiel: `[1, 2] * 3` → `[1, 2, 1, 2, 1, 2]`
  - **Warnung**: Bei verschachtelten Listen werden Referenzen kopiert!
    - `[[0]] * 3` erstellt **drei Referenzen** auf dieselbe innere Liste!
    - Änderungen an einer wirken auf alle: `liste[0].append(1)` ändert alle drei!

- **`in` (Membership-Operator)** – Prüfung auf Enthaltensein
  - Prüft, ob ein Element in einer Sequenz enthalten ist
  - Signatur: `element in sequence` → `bool`
  - Beispiel: `2 in [1, 2, 3]` → `True`
  - Beispiel: `5 in [1, 2, 3]` → `False`
  - **Zeitkomplexität**: O(n) für Listen (lineares Durchsuchen)

- **`del`-Statement** – Löschen von Elementen
  - Löscht Elemente oder Slices aus einer Liste (in-place)
  - Syntax: `del liste[index]` oder `del liste[start:end]`
  - Beispiel: `zahlen = [1, 2, 3, 4]; del zahlen[1]` → `zahlen` ist `[1, 3, 4]`
  - Beispiel: `del zahlen[1:3]` → `zahlen` ist `[1, 4]`
  - **Unterschied zu `.remove()`**: `del` arbeitet mit Index, `.remove()` mit Wert

#### Konzepte und Sprachmerkmale

- **Slicing (Ausschnitte)** – Teile einer Sequenz extrahieren
  - Syntax: `sequence[start:end:step]`
  - Parameter:
    - `start`: Startindex (inklusive, Standard: 0)
    - `end`: Endindex (exklusive, Standard: len(sequence))
    - `step`: Schrittweite (Standard: 1)
  - Beispiel: `zahlen = [0, 1, 2, 3, 4, 5]`
    - `zahlen[1:4]` → `[1, 2, 3]` (Elemente 1 bis 3)
    - `zahlen[:3]` → `[0, 1, 2]` (Erste drei)
    - `zahlen[3:]` → `[3, 4, 5]` (Ab Index 3)
    - `zahlen[::2]` → `[0, 2, 4]` (Jedes zweite)
    - `zahlen[::-1]` → `[5, 4, 3, 2, 1, 0]` (Umgekehrt)
    - `zahlen[-3:]` → `[3, 4, 5]` (Letzte drei)
  - **Wichtig**: Slicing erstellt eine **Kopie**, modifiziert nicht das Original
  - **Zeitkomplexität**: O(k), wobei k die Länge des Slices ist

- **Unpacking (Entpacken)** – Tupel/Listen in Variablen zerlegen
  - Bereits in V03 für Tupel erwähnt, hier für Listen erweitert
  - Syntax: `a, b, c = [1, 2, 3]`
  - Beispiel: `koordinaten = (3, 4); x, y = koordinaten` → `x` ist `3`, `y` ist `4`
  - **Extended Unpacking** (Python 3.0+, PEP 3132):
    - Syntax: `a, *rest, c = [1, 2, 3, 4, 5]`
    - `rest` sammelt alle mittleren Elemente als Liste
    - Beispiel: `erste, *mitte, letzte = [1, 2, 3, 4, 5]` → `erste` ist `1`, `mitte` ist `[2, 3, 4]`, `letzte` ist `5`
  - **Verwendung**: Funktionsrückgaben, Datenaustausch, parallele Zuweisungen

- **Aliasing vs. Copying (Referenzen vs. Kopien)**
  - **Aliasing**: Zwei Variablen zeigen auf dasselbe Objekt
    ```python
    a = [1, 2, 3]
    b = a  # b ist Alias von a
    b.append(4)  # Ändert auch a!
    # a ist jetzt [1, 2, 3, 4]
    ```
  - **Copying**: Neue unabhängige Liste erstellen
    ```python
    a = [1, 2, 3]
    b = a.copy()  # oder b = a[:] oder b = list(a)
    b.append(4)  # Ändert nur b
    # a ist weiterhin [1, 2, 3], b ist [1, 2, 3, 4]
    ```
  - **Shallow vs. Deep Copy**:
    - **Shallow Copy**: Kopiert nur äußere Struktur, innere Objekte werden referenziert
      ```python
      a = [[1, 2], [3, 4]]
      b = a.copy()
      b[0].append(99)  # Ändert auch a[0]!
      # a ist [[1, 2, 99], [3, 4]]
      ```
    - **Deep Copy**: Rekursive Kopie aller Ebenen (Modul `copy.deepcopy()`, wird später behandelt)

- **Listen als Stacks (LIFO)** – Last In, First Out
  - `.append(element)` für Push (Element hinzufügen)
  - `.pop()` für Pop (letztes Element entfernen und zurückgeben)
  - Beispiel:
    ```python
    stack = []
    stack.append(1)  # Push
    stack.append(2)  # Push
    x = stack.pop()  # Pop → x ist 2
    ```
  - **Zeitkomplexität**: O(1) für beide Operationen

- **Listen als Queues (FIFO)** – First In, First Out
  - `.append(element)` für Enqueue (am Ende hinzufügen)
  - `.pop(0)` für Dequeue (erstes Element entfernen)
  - **Warnung**: `.pop(0)` ist ineffizient (O(n)), da alle Elemente verschoben werden
  - **Bessere Alternative**: `collections.deque` (wird später behandelt)

### Konzepte und Best Practices

- **`.sort()` vs. `sorted()`**: 
  - `.sort()` für In-Place-Sortierung (spart Speicher, Original verloren)
  - `sorted()` für neue sortierte Liste (Original bleibt erhalten)
- **`.append()` vs. `.extend()`**:
  - `.append(x)` fügt `x` als **ein** Element hinzu (auch wenn `x` eine Liste ist)
  - `.extend(iterable)` fügt alle Elemente von `iterable` hinzu
- **Slicing für Kopien**: `kopie = original[:]` ist idiomatisch für flache Kopie
- **Negative Indizes**: `liste[-1]` ist letztes Element, `liste[-2]` ist vorletztes
- **Vorsicht bei Aliasing**: `b = a` erstellt **keine** Kopie, sondern nur eine weitere Referenz
- **`in` für Existenzprüfung**: Idiomatischer als manuelles Durchsuchen mit Schleife
- **List Comprehensions** (aus V07) kombinieren gut mit neuen Funktionen:
  - `[x for x in zahlen if x > 0]` – Filtern
  - `[x**2 for x in zahlen]` – Transformieren
- **`zip()` für parallele Listen**: Eleganter als manuelle Index-Verwaltung

### Notizen

- Listen wurden in Python 1.0 eingeführt und sind eine der grundlegendsten Datenstrukturen
- `.clear()` und `.copy()` wurden erst in Python 3.3 hinzugefügt
- `sorted()`, `all()`, `any()` wurden in Python 2.4/2.5 hinzugefügt
- `zip()` in Python 2 gab eine Liste zurück, in Python 3 einen Iterator (speicher-effizienter)
- Extended Unpacking (`*rest`) wurde in Python 3.0 eingeführt (PEP 3132)
- Timsort (der Sortieralgorithmus in `.sort()` und `sorted()`) ist ein hybrider Algorithmus (Merge Sort + Insertion Sort)
- Listen haben dynamische Größe und amortisierte O(1) Append-Zeit (Speicher wird bei Bedarf verdoppelt)
- Tupel sind immutable, aber wenn sie mutable Objekte enthalten (z.B. Listen), können diese modifiziert werden
- `collections.deque` (Double-Ended Queue) ist effizienter für Queue-Operationen als Listen (wird in späteren Vorlesungen behandelt)
---

## V10 (2026-01-03) – Methoden/Funktionen – Teil 1

### Neu eingeführt

#### Funktions-Definition und Aufruf

- **`def`-Statement** (Python Keyword, Python 1.0+)
  - Definiert eine neue Funktion (benutzerdefinierten Code-Block)
  - Syntax: `def funktionsname(parameter1, parameter2, ...):`
  - Funktionskörper muss eingerückt sein (Standard: 4 Leerzeichen)
  - Signatur: `def name(params):` → Funktion wird erstellt, aber nicht ausgeführt
  - Beispiel:
    ```python
    def begruesse(name):
        print(f"Hallo, {name}!")
    ```
  - **Wichtig**: Funktion wird erst bei Aufruf ausgeführt: `begruesse("Ada")`

- **`return`-Statement** (Python Keyword, Python 1.0+)
  - Beendet die Funktionsausführung und gibt einen Wert zurück
  - Syntax: `return wert` oder `return wert1, wert2, ...` (mehrere Werte als Tupel)
  - Ohne `return`: Funktion gibt implizit `None` zurück
  - Signatur: `return [expression]`
  - Beispiel:
    ```python
    def addiere(a, b):
        return a + b  # Gibt Summe zurück
    ```
  - **Wichtig**: Code nach `return` wird nicht ausgeführt (unreachable code)

#### Parameter und Argumente

- **Positionaler Parameter** (Konzept)
  - Parameter werden durch ihre Position in der Funktionsdefinition identifiziert
  - Beim Aufruf müssen Argumente in derselben Reihenfolge übergeben werden
  - Beispiel:
    ```python
    def teile(zaehler, nenner):
        return zaehler / nenner
    
    teile(10, 2)  # zaehler=10, nenner=2 → 5.0
    teile(2, 10)  # zaehler=2, nenner=10 → 0.2 (andere Reihenfolge!)
    ```

- **Keyword Argument** (Konzept, Python 1.0+)
  - Argumente werden mit Parameternamen übergeben: `funktionsname(param=wert)`
  - Reihenfolge spielt keine Rolle, wenn alle Argumente als Keywords übergeben werden
  - Syntax: `funktionsname(param1=wert1, param2=wert2)`
  - Beispiel:
    ```python
    def teile(zaehler, nenner):
        return zaehler / nenner
    
    teile(zaehler=10, nenner=2)  # 5.0
    teile(nenner=2, zaehler=10)  # 5.0 (gleiche Reihenfolge egal)
    ```
  - **Regel**: Positionale Argumente müssen vor Keyword-Argumenten stehen
  - **Fehler**: `teile(zaehler=10, 2)` → `SyntaxError`
  - **Richtig**: `teile(10, nenner=2)`

- **Default-Parameter** (Konzept, Python 1.0+)
  - Parameter mit Standard-Wert in der Funktionsdefinition
  - Syntax: `def funktion(param=default_wert):`
  - Können beim Aufruf weggelassen werden → Default-Wert wird verwendet
  - Beispiel:
    ```python
    def berechne_preis(netto, mwst=0.19):
        return netto * (1 + mwst)
    
    berechne_preis(100)          # 119.0 (Standard-MwSt 19%)
    berechne_preis(100, 0.07)    # 107.0 (reduzierte MwSt 7%)
    berechne_preis(100, mwst=0)  # 100.0 (keine MwSt)
    ```
  - **Regel**: Parameter ohne Default müssen vor Parametern mit Default stehen
  - **Fehler**: `def funktion(a=10, b):` → `SyntaxError`
  - **Richtig**: `def funktion(b, a=10):`

- **Multiple Return Values** (Konzept, nutzt Tuples)
  - Funktion kann mehrere Werte als Tupel zurückgeben
  - Syntax: `return wert1, wert2, wert3`
  - Beim Aufruf: Tuple Unpacking verwenden
  - Beispiel:
    ```python
    def min_max(liste):
        return min(liste), max(liste)
    
    # Unpacking:
    minimum, maximum = min_max([3, 1, 4, 1, 5])
    # minimum=1, maximum=5
    
    # Oder als Tupel:
    ergebnis = min_max([3, 1, 4, 1, 5])
    # ergebnis=(1, 5)
    ```

#### Funktionen als Objekte

- **Funktionen als First-Class Objects** (Konzept)
  - Funktionen sind in Python reguläre Objekte (wie int, str, list)
  - Können Variablen zugewiesen werden
  - Können als Argumente übergeben werden (Higher-Order Functions)
  - Können als Rückgabewerte verwendet werden
  - Beispiel:
    ```python
    def verdopple(x):
        return x * 2
    
    # Funktion einer Variable zuweisen (ohne Klammern!):
    meine_funktion = verdopple
    print(meine_funktion(5))  # 10
    
    # Als Argument übergeben:
    def wende_an(funktion, wert):
        return funktion(wert)
    
    print(wende_an(verdopple, 7))  # 14
    ```
  - **Wichtig**: `verdopple` (ohne Klammern) ist die Funktion selbst, `verdopple()` ruft sie auf

#### Scope und Namensauflösung

- **LEGB-Regel** (Konzept, Python 2.0+)
  - Reihenfolge der Namensauflösung in Python
  - **L**ocal: Lokale Variablen innerhalb der aktuellen Funktion
  - **E**nclosing: Variablen in umschließenden Funktionen (Closures)
  - **G**lobal: Globale Variablen auf Modul-Ebene
  - **B**uilt-in: Eingebaute Namen (print, len, etc.)
  - Python sucht Namen in dieser Reihenfolge von innen nach außen
  - Beispiel:
    ```python
    x = "global"  # Global
    
    def aeussere():
        x = "enclosing"  # Enclosing
        
        def innere():
            x = "local"  # Local
            print(x)  # "local" (findet zuerst Local)
        
        innere()
        print(x)  # "enclosing"
    
    aeussere()
    print(x)  # "global"
    ```
  - **Built-in Beispiel**: `len` ist Built-in, kann aber überschrieben werden (nicht empfohlen!)
    ```python
    len([1, 2, 3])  # 3 (Built-in)
    len = "Hallo"   # Überschreibt Built-in (schlecht!)
    # len([1, 2, 3])  # TypeError: 'str' object is not callable
    ```

#### Dokumentation

- **Docstring** (Konzept, Python 1.0+)
  - Dokumentations-String direkt nach Funktionsdefinition
  - Wird in Triple-Quotes geschrieben: `"""..."""` oder `'''...'''`
  - Beschreibt Funktion, Parameter, Rückgabewert, Beispiele
  - Syntax: Erste Zeile nach `def` muss der Docstring sein
  - Zugriff: `funktionsname.__doc__` oder `help(funktionsname)`
  - Beispiel:
    ```python
    def berechne_flaeche(laenge, breite):
        """
        Berechnet die Fläche eines Rechtecks.
        
        Parameter:
            laenge (float): Länge des Rechtecks
            breite (float): Breite des Rechtecks
        
        Rückgabewert:
            float: Fläche (Länge × Breite)
        
        Beispiele:
            >>> berechne_flaeche(5, 3)
            15
            >>> berechne_flaeche(10, 2.5)
            25.0
        """
        return laenge * breite
    
    # Docstring anzeigen:
    print(berechne_flaeche.__doc__)
    help(berechne_flaeche)
    ```
  - **Best Practice**: Immer Docstrings für öffentliche Funktionen schreiben
  - **Format**: Google Style, NumPy Style oder reStructuredText sind verbreitet

#### Module (Verwendung)

- **`time`-Modul** (Standard Library)
  - Modul für Zeit-bezogene Funktionen
  - Import: `import time`
  
  - **`time.time()`** (Funktion)
    - Gibt aktuelle Zeit in Sekunden seit Unix-Epoch (1. Januar 1970) zurück
    - Signatur: `time.time()` → `float`
    - Verwendung: Zeitmessung durch Differenz von zwei `time.time()`-Aufrufen
    - Beispiel:
      ```python
      import time
      
      start = time.time()
      # ... Code, dessen Laufzeit gemessen werden soll ...
      ende = time.time()
      
      dauer = ende - start
      print(f"Laufzeit: {dauer:.4f} Sekunden")
      ```
    - **Genauigkeit**: System-abhängig, typischerweise Mikrosekunden-Bereich

### Konzepte und Best Practices

- **Funktionsnamen**: Verwende `snake_case` (Kleinbuchstaben mit Unterstrichen)
- **Einzeilige Funktionen**: Nur wenn wirklich trivial, sonst mehrzeilig für Lesbarkeit
- **Return vs. Print**: Funktionen sollten Werte zurückgeben, nicht ausgeben (testbarer, wiederverwendbarer)
- **Reine Funktionen**: Bevorzuge Funktionen ohne Seiteneffekte (keine globalen Variablen ändern)
- **Parameterzahl**: Max. 4-5 Parameter empfohlen, sonst Dictionary oder Objekt übergeben
- **Default-Parameter Warnung**: Mutable Defaults (`def func(liste=[]):`) sind gefährlich! Verwende `None` stattdessen:
  ```python
  # Falsch:
  def fuege_hinzu(element, liste=[]):
      liste.append(element)
      return liste
  
  # Richtig:
  def fuege_hinzu(element, liste=None):
      if liste is None:
          liste = []
      liste.append(element)
      return liste
  ```

### Notizen

- `def` und `return` existieren seit Python 1.0
- Keyword Arguments existieren seit Python 1.0
- LEGB-Regel wurde in Python 2.0 formalisiert mit Nested Scopes (PEP 227)
- Docstrings existieren seit Python 1.0, aber PEP 257 (Docstring Conventions) kam später
- Type Hints (PEP 484, Python 3.5+) sind optional und werden in V11 behandelt
- `*args` und `**kwargs` für variable Argumentanzahl werden in V11 behandelt
- Lambda-Funktionen (anonyme Funktionen) werden in V11 behandelt
- Decorators und Generator-Funktionen sind fortgeschrittene Themen für spätere Vorlesungen

---

## V11 (2026-01-02) – GPTs, LLMs & Künstliche Intelligenz + Methoden/Funktionen – Teil 2

### Neu eingeführt

#### Erweiterte Funktionsparameter

- **Keyword-Only Arguments** (Konzept, Python 3.0+)
  - Parameter, die **nur** als Keyword-Argumente übergeben werden können (nicht positionsbasiert)
  - Syntax: Parameter nach einem alleinstehenden `*` in der Funktionsdefinition
  - Erzwingt explizite Benennung → erhöht Lesbarkeit und verhindert Verwechslungen
  - Beispiel:
    ```python
    def log_nachricht(nachricht, *, level="INFO", timestamp=True):
        # level und timestamp MÜSSEN als Keywords übergeben werden
        pass
    
    # Korrekt:
    log_nachricht("Server gestartet", level="DEBUG", timestamp=False)
    
    # Fehler:
    log_nachricht("Test", "DEBUG", True)  # TypeError!
    ```
  - **Best Practice**: Bei Funktionen mit vielen optionalen Parametern oder wenn Verwechslungsgefahr besteht

- **`*args` (Variable Positional Arguments)** (Python 1.0+, Konzept)
  - Sammelt beliebig viele positionale Argumente in ein Tupel
  - Syntax: `def funktion(*args):`
  - Name `args` ist Konvention (kann beliebig sein, `*` ist entscheidend)
  - Signatur: `*args` → `tuple`
  - Beispiel:
    ```python
    def summiere(*zahlen):
        return sum(zahlen)
    
    summiere(1, 2, 3)        # 6
    summiere(10, 20, 30, 40) # 100
    summiere()               # 0 (leeres Tupel)
    ```
  - **Zugriff**: Wie auf normales Tupel: `args[0]`, `len(args)`, Iteration mit `for`

- **`**kwargs` (Variable Keyword Arguments)** (Python 1.0+, Konzept)
  - Sammelt beliebig viele Keyword-Argumente in ein Dictionary
  - Syntax: `def funktion(**kwargs):`
  - Name `kwargs` ist Konvention (kann beliebig sein, `**` ist entscheidend)
  - Signatur: `**kwargs` → `dict`
  - Beispiel:
    ```python
    def zeige_einstellungen(**einstellungen):
        for key, value in einstellungen.items():
            print(f"{key}: {value}")
    
    zeige_einstellungen(modell="gpt-4", temperatur=0.7, max_tokens=500)
    # Ausgabe:
    # modell: gpt-4
    # temperatur: 0.7
    # max_tokens: 500
    ```
  - **Zugriff**: Dictionary-Methoden: `kwargs.get()`, `kwargs.keys()`, `kwargs['key']`

- **Vollständige Parametersignatur** (Konzept, Python 3.0+)
  - Reihenfolge in Funktionsdefinition (alle optional außer regulären Parametern):
    1. Reguläre positionale Parameter: `def func(a, b):`
    2. Default-Parameter: `def func(a, b=10):`
    3. `*args` (variable positionale): `def func(a, b=10, *args):`
    4. Keyword-Only Parameter: `def func(a, b=10, *args, x, y=20):`
    5. `**kwargs` (variable Keywords): `def func(a, b=10, *args, x, y=20, **kwargs):`
  - Beispiel:
    ```python
    def komplexe_funktion(pflicht, optional=10, *args, kw_only, kw_default=20, **kwargs):
        print(f"pflicht: {pflicht}")
        print(f"optional: {optional}")
        print(f"args: {args}")
        print(f"kw_only: {kw_only}")
        print(f"kw_default: {kw_default}")
        print(f"kwargs: {kwargs}")
    
    komplexe_funktion(1, 2, 3, 4, kw_only=5, kw_default=6, extra1=7, extra2=8)
    # pflicht: 1
    # optional: 2
    # args: (3, 4)
    # kw_only: 5
    # kw_default: 6
    # kwargs: {'extra1': 7, 'extra2': 8}
    ```

#### Unpacking-Operatoren

- **`*` Unpacking Operator für Iterables** (Python 3.5+, erweitert)
  - Entpackt Iterables (Listen, Tuples, Sets) in Funktionsaufrufe oder andere Sequenzen
  - Verwendung 1: Beim Funktionsaufruf
    ```python
    def addiere(a, b, c):
        return a + b + c
    
    zahlen = [10, 20, 30]
    ergebnis = addiere(*zahlen)  # Entspricht: addiere(10, 20, 30)
    ```
  - Verwendung 2: In Sequenzen (Python 3.5+)
    ```python
    liste1 = [1, 2, 3]
    liste2 = [4, 5, 6]
    kombiniert = [*liste1, *liste2]  # [1, 2, 3, 4, 5, 6]
    ```
  - **Wichtig**: Unterschied zwischen Definition (`*args`) und Aufruf (`*liste`)

- **`**` Unpacking Operator für Dictionaries** (Python 3.5+, erweitert)
  - Entpackt Dictionaries in Funktionsaufrufe oder andere Dictionaries
  - Verwendung 1: Beim Funktionsaufruf
    ```python
    def konfiguriere(modell, temperatur, max_tokens):
        print(f"{modell}, temp={temperatur}, tokens={max_tokens}")
    
    einstellungen = {"modell": "gpt-4", "temperatur": 0.7, "max_tokens": 500}
    konfiguriere(**einstellungen)  # Entspricht: konfiguriere(modell="gpt-4", ...)
    ```
  - Verwendung 2: Dictionary Merging (Python 3.5+)
    ```python
    standard = {"a": 1, "b": 2}
    custom = {"b": 99, "c": 3}
    merged = {**standard, **custom}  # {'a': 1, 'b': 99, 'c': 3}
    ```
  - **Reihenfolge**: Bei Merging überschreibt späteres Dictionary frühere Keys

#### Lambda-Funktionen (Anonyme Funktionen)

- **`lambda`-Ausdruck** (Python Keyword, Python 1.0+)
  - Erstellt anonyme (unbenannte) Einzeiler-Funktion
  - Syntax: `lambda parameter: ausdruck`
  - Kann nur **einen einzigen Ausdruck** enthalten (kein Statement wie `if`/`for` mit Blöcken)
  - Signatur: `lambda x: x * 2` → Funktion, die Eingabe verdoppelt
  - Beispiel:
    ```python
    # Normale Funktion:
    def quadrat(x):
        return x ** 2
    
    # Äquivalente Lambda:
    quadrat = lambda x: x ** 2
    
    print(quadrat(5))  # 25
    ```
  - **Häufige Verwendung**: Als Argument für Higher-Order Functions (`map`, `filter`, `sorted`)
  - **Best Practice**: Nur für triviale, einzeilige Operationen; bei Komplexität benannte Funktion bevorzugen

#### Funktionale Programmierung

- **`map(funktion, iterable)`** (Built-in, Python 2.0+)
  - Wendet Funktion auf jedes Element eines Iterables an
  - Gibt Iterator zurück (nicht Liste!) → mit `list()` konvertieren für sofortige Auswertung
  - Signatur: `map(func, iterable)` → `map object` (Iterator)
  - Beispiel:
    ```python
    zahlen = [1, 2, 3, 4, 5]
    quadrate = map(lambda x: x ** 2, zahlen)
    print(list(quadrate))  # [1, 4, 9, 16, 25]
    
    # Mit normaler Funktion:
    def verdopple(x):
        return x * 2
    
    ergebnis = list(map(verdopple, zahlen))  # [2, 4, 6, 8, 10]
    ```
  - **Alternative**: List Comprehension ist oft pythonischer: `[x**2 for x in zahlen]`

- **`filter(funktion, iterable)`** (Built-in, Python 2.0+)
  - Filtert Elemente, für die die Funktion `True` zurückgibt
  - Gibt Iterator zurück → mit `list()` konvertieren
  - Signatur: `filter(func, iterable)` → `filter object` (Iterator)
  - Beispiel:
    ```python
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gerade = filter(lambda x: x % 2 == 0, zahlen)
    print(list(gerade))  # [2, 4, 6, 8, 10]
    
    # Mit Boolean-Funktion:
    def ist_positiv(x):
        return x > 0
    
    werte = [-5, 3, -2, 7, 0, 4]
    positive = list(filter(ist_positiv, werte))  # [3, 7, 4]
    ```
  - **Alternative**: List Comprehension mit `if`: `[x for x in zahlen if x % 2 == 0]`
  - **Unterschied zu `map`**: `map` transformiert, `filter` selektiert

#### Type Hints (Typen-Annotationen)

- **Type Hints** (Konzept, PEP 484, Python 3.5+)
  - Optionale Typ-Annotationen für Parameter und Rückgabewerte
  - Werden zur Laufzeit **nicht** erzwungen (nur für statische Analyse mit Tools wie `mypy`)
  - Syntax: `def funktion(param: typ) -> rueckgabetyp:`
  - Beispiel:
    ```python
    def addiere(a: int, b: int) -> int:
        return a + b
    
    def begruessung(name: str, alter: int) -> str:
        return f"Hallo {name}, du bist {alter} Jahre alt"
    ```
  - **Vorteile**: IDE-Support (Autocomplete), Dokumentation, statische Typ-Prüfung
  - **Wichtig**: Python ignoriert Type Hints zur Laufzeit! `addiere("a", "b")` wirft keinen Fehler (erst bei `"a" + "b"` → `"ab"`, nicht Fehler, aber falsche Semantik)

- **`typing`-Modul** (Standard Library, Python 3.5+)
  - Modul für komplexere Type Hints (Container, Optionals, Unions, etc.)
  - Import: `from typing import List, Dict, Optional, Any, Union, Tuple, Callable`
  
  - **`List[typ]`** (Python 3.5-3.8, ab 3.9: `list[typ]`)
    - Type Hint für Liste mit Elementen eines bestimmten Typs
    - Beispiel: `def summiere(zahlen: List[int]) -> int:`
    - Ab Python 3.9: `def summiere(zahlen: list[int]) -> int:` (lowercase)
  
  - **`Dict[key_typ, value_typ]`** (Python 3.5-3.8, ab 3.9: `dict[...]`)
    - Type Hint für Dictionary
    - Beispiel: `def zähle_wörter(text: str) -> Dict[str, int]:`
    - Ab Python 3.9: `dict[str, int]`
  
  - **`Optional[typ]`** (Python 3.5+)
    - Equivalent zu `Union[typ, None]` (Wert kann entweder `typ` oder `None` sein)
    - Beispiel:
      ```python
      from typing import Optional
      
      def finde_nutzer(id: int) -> Optional[str]:
          if id > 0:
              return "Alice"
          return None  # Gültig, da Optional
      ```
  
  - **`Any`** (Python 3.5+)
    - Akzeptiert jeden Typ (wie ungetypt)
    - Beispiel: `def debug_ausgabe(wert: Any) -> None:`
    - **Verwendung**: Wenn Typ wirklich beliebig sein kann (sparsam verwenden)
  
  - **`Union[typ1, typ2, ...]`** (Python 3.5+, ab 3.10: `typ1 | typ2`)
    - Wert kann einer von mehreren Typen sein
    - Beispiel: `def verarbeite(wert: Union[int, float, str]) -> str:`
    - Ab Python 3.10: `def verarbeite(wert: int | float | str) -> str:`
  
  - **`Callable[[arg_typen], rueckgabetyp]`** (Python 3.5+)
    - Type Hint für Funktionen als Parameter
    - Beispiel:
      ```python
      from typing import Callable
      
      def wende_an(funktion: Callable[[int], int], wert: int) -> int:
          return funktion(wert)
      
      wende_an(lambda x: x * 2, 5)  # 10
      ```

#### Docstring-Formate

- **Google Style Docstring** (Convention)
  - Strukturiertes Format für Docstrings (weit verbreitet, lesbar)
  - Syntax:
    ```python
    def funktion(param1, param2):
        """
        Kurze Beschreibung (eine Zeile).
        
        Längere Beschreibung über mehrere Zeilen...
        
        Args:
            param1 (typ): Beschreibung von param1
            param2 (typ): Beschreibung von param2
        
        Returns:
            typ: Beschreibung des Rückgabewerts
        
        Raises:
            ExceptionType: Wann diese Exception geworfen wird
        
        Examples:
            >>> funktion(1, 2)
            3
        """
        pass
    ```
  - **Sektionen**: `Args`, `Returns`, `Raises`, `Examples`, `Notes`, `Yields` (für Generatoren)
  - **Tool-Support**: Sphinx (mit Napoleon Extension), MkDocs

- **NumPy Style Docstring** (Convention)
  - Alternative zu Google Style (vor allem in wissenschaftlicher Community)
  - Syntax:
    ```python
    def funktion(param1, param2):
        """
        Kurze Beschreibung (eine Zeile).
        
        Längere Beschreibung...
        
        Parameters
        ----------
        param1 : typ
            Beschreibung von param1
        param2 : typ
            Beschreibung von param2
        
        Returns
        -------
        typ
            Beschreibung des Rückgabewerts
        
        Examples
        --------
        >>> funktion(1, 2)
        3
        """
        pass
    ```
  - **Unterschied**: Sektionen mit Unterstrichen statt Doppelpunkten
  - **Tool-Support**: Sphinx (mit Napoleon), numpydoc

#### JSON-Modul (Erweitert)

- **`json.dump(obj, file, indent=None, ensure_ascii=True)`** (Methode aus V09, erweiterte Verwendung)
  - Schreibt Python-Objekt als JSON in Datei
  - **Neu in V11**: Parameter `indent` und `ensure_ascii` für Formatierung
  - `indent=4`: Formatiert JSON mit 4-Leerzeichen-Einrückung (lesbar)
  - `ensure_ascii=False`: Erlaubt Unicode-Zeichen (Umlaute, Emojis) statt Escape-Sequenzen
  - Beispiel:
    ```python
    import json
    
    daten = {"name": "Müller", "alter": 30, "emoji": "😊"}
    
    with open("daten.json", "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)
    
    # Datei-Inhalt:
    # {
    #     "name": "Müller",
    #     "alter": 30,
    #     "emoji": "😊"
    # }
    ```

#### DateTime-Modul (Erweitert)

- **`datetime.datetime.isoformat()`** (Methode, Python 2.3+)
  - Konvertiert `datetime`-Objekt in ISO 8601 String-Format
  - Format: `"YYYY-MM-DDTHH:MM:SS.ffffff"`
  - Signatur: `datetime_obj.isoformat()` → `str`
  - Beispiel:
    ```python
    from datetime import datetime
    
    jetzt = datetime.now()
    iso_string = jetzt.isoformat()
    print(iso_string)  # "2026-01-02T15:30:45.123456"
    ```
  - **Verwendung**: Serialisierung für JSON (datetime ist nicht JSON-serialisierbar)

- **`datetime.datetime.strftime(format)`** (Methode, Python 1.5+, erweiterte Verwendung in V11)
  - Formatiert `datetime`-Objekt als String mit benutzerdefiniertem Format
  - Signatur: `datetime_obj.strftime(format_string)` → `str`
  - **Häufige Format-Codes**:
    - `%Y`: Jahr (4-stellig, z.B. 2026)
    - `%m`: Monat (01-12)
    - `%d`: Tag (01-31)
    - `%H`: Stunde (00-23, 24h-Format)
    - `%M`: Minute (00-59)
    - `%S`: Sekunde (00-59)
  - Beispiel:
    ```python
    from datetime import datetime
    
    jetzt = datetime.now()
    formatiert = jetzt.strftime("%Y-%m-%d %H:%M:%S")
    print(formatiert)  # "2026-01-02 15:30:45"
    
    # Custom Format:
    formatiert2 = jetzt.strftime("%d.%m.%Y um %H:%M Uhr")
    print(formatiert2)  # "02.01.2026 um 15:30 Uhr"
    ```

### Konzepte und Best Practices

- **Keyword-Only Arguments**: Bei Funktionen mit >3 Parametern oder bei Verwechslungsgefahr
- **`*args`/`**kwargs`**: Für flexible APIs, aber nicht übertreiben (Lesbarkeit!)
- **Lambda vs. `def`**: Lambda nur für triviale Einzeiler, sonst benannte Funktion
- **List Comprehension vs. `map`/`filter`**: List Comprehensions sind pythonischer und oft lesbarer
- **Type Hints**: Immer für öffentliche APIs, optional für interne Hilfsfunktionen
- **Docstrings**: Google Style oder NumPy Style konsistent im Projekt verwenden
- **JSON + datetime**: Immer `.isoformat()` für datetime-Serialisierung nutzen
- **Fehlertoleranz**: Bei Batch-Verarbeitung `try-except` für Einzelfehler, nicht gesamte Batch abbrechen

### Häufige Fehler (Gotchas)

- **Keyword-Only ohne `*`**: Vergessen, `*` vor Keyword-Only Parametern zu setzen
- **`*args` nach Keywords**: `*args` muss vor Keyword-Only Parametern stehen
- **Lambda mit Statements**: Lambda erlaubt nur Ausdrücke, keine `if`-Blöcke oder `for`-Schleifen
- **`map`/`filter` ohne `list()`**: Vergessen, Iterator zu konvertieren → nur `<map object>` wird ausgegeben
- **Type Hints als Runtime-Check**: Type Hints werden **nicht** zur Laufzeit geprüft!
- **Mutable Defaults mit `**kwargs`**: `**kwargs` ist kein Mutable Default Problem, aber Vorsicht bei Modifikation
- **JSON + datetime**: Direktes `json.dump()` mit datetime wirft `TypeError` → erst `.isoformat()`

### Notizen

- `*args` und `**kwargs` existieren seit Python 1.0, aber Best Practices haben sich entwickelt
- Keyword-Only Arguments (nach `*`) wurden in Python 3.0 eingeführt (PEP 3102)
- Lambda existiert seit Python 1.0
- `map` und `filter` existieren seit Python 2.0 (vorher andere Implementierung)
- Type Hints wurden in Python 3.5 eingeführt (PEP 484)
- `typing`-Modul wurde in Python 3.5 hinzugefügt, viele Typen in 3.9+ vereinfacht
- `|` als Union-Operator ab Python 3.10 (PEP 604)

---

## V12 (2026-01-03) – Imports & Code auf mehrere Dateien verteilen

### Module und Imports

- **`import module_name`** (Statement, Python 1.0+)
  - Importiert ein komplettes Modul
  - Zugriff auf Modul-Inhalte mit `module_name.funktion()`
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    import math
    print(math.sqrt(16))  # 4.0
    
    import greetings  # Eigenes Modul
    print(greetings.begruessung("Anna"))  # "Hallo, Anna!"
    ```

- **`from module import name1, name2`** (Statement, Python 1.0+)
  - Importiert spezifische Namen aus einem Modul
  - Direkte Nutzung ohne Modul-Präfix
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    from math import sqrt, pi
    print(sqrt(16))  # 4.0, ohne math.
    print(pi)  # 3.14159...
    
    from greetings import begruessung
    print(begruessung("Max"))  # Direkter Zugriff
    ```

- **`from module import *`** (Statement, Python 1.0+)
  - Importiert alle öffentlichen Namen aus einem Modul
  - **NICHT EMPFOHLEN** für Production-Code (Namespace Pollution)
  - **Neu eingeführt in V12**
  - Nur für interaktive Sessions oder explizit kontrollierte `__all__`
  - Beispiel:
    ```python
    from math import *
    print(sqrt(16))  # 4.0, aber unklar woher sqrt kommt
    ```

- **`import module as alias`** (Statement, Python 2.0+)
  - Importiert Modul mit Alias-Namen
  - Nützlich bei langen Modulnamen oder Namenskonflikten
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    import numpy as np  # Standard-Konvention
    import pandas as pd  # Standard-Konvention
    
    import greetings as gr
    print(gr.begruessung("Lisa"))
    ```

- **`from module import name as alias`** (Statement, Python 2.0+)
  - Importiert spezifischen Namen mit Alias
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    from math import sqrt as square_root
    print(square_root(16))  # 4.0
    ```

### Eigene Module erstellen

- **Modul-Docstring** (Convention, Python 1.0+)
  - Docstring an erster Stelle der Datei (nach Shebang/Encoding)
  - Beschreibt Zweck des Moduls
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    """
    Greetings-Modul für Begrüßungen.
    
    Dieses Modul bietet Funktionen für verschiedene Grußformeln.
    """
    
    def begruessung(name: str) -> str:
        """Gibt eine Begrüßung zurück."""
        return f"Hallo, {name}!"
    ```

- **`if __name__ == "__main__":`** (Pattern, Python 1.0+)
  - Prüft, ob Modul direkt ausgeführt oder importiert wird
  - `__name__ == "__main__"`: Direkter Aufruf (z.B. `python script.py`)
  - `__name__ == "module_name"`: Import (z.B. `import script`)
  - **Neu eingeführt in V12**
  - **Verwendung**: Code, der nur bei direkter Ausführung laufen soll (Tests, CLI, etc.)
  - Beispiel:
    ```python
    def addiere(a: float, b: float) -> float:
        """Addiert zwei Zahlen."""
        return a + b
    
    # Läuft nur bei direkter Ausführung:
    if __name__ == "__main__":
        print("Teste addiere()...")
        print(addiere(5, 3))  # 8.0
    
    # Bei Import wird dieser Block NICHT ausgeführt
    ```

### Packages

- **`__init__.py`** (Datei, Python 1.5+)
  - Macht Verzeichnis zu einem Python-Package
  - Kann leer sein oder Initialisierungscode/Imports enthalten
  - **Neu eingeführt in V12**
  - **Zweck**: Package-Definition, Public API definieren
  - Beispiel:
    ```python
    # text_tools/__init__.py
    """text_tools Package für Textverarbeitung."""
    
    from .formatters import upper_first, snake_case
    from .validators import ist_email_gueltig
    
    __all__ = ['upper_first', 'snake_case', 'ist_email_gueltig']
    ```

- **`__all__`** (Variable, Python 1.5+)
  - Liste von Namen, die bei `from package import *` exportiert werden
  - Definiert Public API eines Moduls/Packages
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    # module.py
    __all__ = ['funktion_a', 'funktion_b']
    
    def funktion_a():
        pass
    
    def funktion_b():
        pass
    
    def _interne_funktion():  # Nicht in __all__, also privat
        pass
    ```

- **Relative Imports** (Syntax, Python 2.5+)
  - Imports relativ zur aktuellen Package-Position
  - Nur innerhalb von Packages, nicht in Top-Level-Skripten
  - **Neu eingeführt in V12**
  - **Syntax**:
    - `.module`: Gleiches Package
    - `..module`: Parent-Package
    - `..sibling.module`: Geschwister-Package
  - Beispiel:
    ```python
    # data_processing/utils/transformers.py
    from .validators import ist_nicht_leer  # Gleiches Package (utils/)
    from ..core.reader import lese_zeilen   # Parent-Package (data_processing/)
    ```

- **Absolute Imports** (Syntax, Python 1.0+, Best Practice ab Python 2.5+)
  - Imports mit vollständigem Pfad vom Package-Root
  - Empfohlen für Imports von außen und in Main-Skripten
  - **Neu eingeführt in V12** (als Best Practice)
  - Beispiel:
    ```python
    # main.py
    from data_processing.core.reader import lese_zeilen
    from data_processing.utils.transformers import filtere_leere_zeilen
    ```

### Virtuelle Umgebungen

- **`python -m venv venv_name`** (Kommando, Python 3.3+)
  - Erstellt virtuelle Python-Umgebung
  - Isoliert Packages pro Projekt
  - **Neu eingeführt in V12**
  - Beispiel:
    ```bash
    # Virtuelle Umgebung erstellen:
    python -m venv venv
    
    # Aktivieren:
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    
    # Deaktivieren:
    deactivate
    ```

- **`pip freeze`** (Kommando, pip 1.0+)
  - Listet alle installierten Packages mit exakten Versionen
  - **Neu eingeführt in V12**
  - **Verwendung**: Dependencies für Reproduzierbarkeit dokumentieren
  - Beispiel:
    ```bash
    # Aktuelle Packages auflisten:
    pip freeze
    
    # In requirements.txt schreiben:
    pip freeze > requirements.txt
    ```

- **`requirements.txt`** (Convention, pip 1.0+)
  - Datei mit Liste aller Projekt-Dependencies
  - Format: `package==version`
  - **Neu eingeführt in V12**
  - Beispiel:
    ```txt
    requests==2.31.0
    pytest==7.4.3
    numpy==1.24.0
    ```
  - Installation: `pip install -r requirements.txt`

### Argparse (CLI-Tool)

- **`argparse.ArgumentParser()`** (Klasse, Python 2.7+/3.2+)
  - Erstellt Parser für Kommandozeilen-Argumente
  - Teil der Standard-Library
  - **Neu eingeführt in V12**
  - Beispiel:
    ```python
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Mein CLI-Tool'
    )
    parser.add_argument('--stadt', required=True, help='Name der Stadt')
    parser.add_argument('--einfach', action='store_true', help='Einfache Ausgabe')
    
    args = parser.parse_args()
    print(args.stadt)  # Zugriff auf Argumente
    ```

- **`parser.add_argument()`** (Methode, Python 2.7+/3.2+)
  - Fügt Kommandozeilen-Argument zum Parser hinzu
  - **Neu eingeführt in V12**
  - **Parameter**:
    - `name`: Name des Arguments (z.B. `'--option'`)
    - `required`: Ob Argument erforderlich ist (Boolean)
    - `help`: Hilfetext für `--help`
    - `action`: Spezielle Aktion (z.B. `'store_true'` für Flags)
    - `type`: Datentyp (z.B. `int`, `float`)
    - `default`: Standardwert
  - Beispiel:
    ```python
    parser.add_argument('--zahl', type=int, default=0, help='Eine Zahl')
    parser.add_argument('--verbose', action='store_true', help='Verbose-Modus')
    ```

### Konzepte und Best Practices

- **Import-Stile**:
  - `import module`: Klarster Stil, immer sichtbar woher Code kommt
  - `from module import name`: Kürzer, gut bei häufiger Nutzung
  - `import module as alias`: Standard bei langen Namen (numpy → np)
  - **Vermeiden**: `from module import *` (außer interaktiv)

- **Modul vs. Package**:
  - **Modul**: Einzelne `.py` Datei
  - **Package**: Verzeichnis mit `__init__.py`

- **Relative vs. Absolute Imports**:
  - **Innerhalb Package**: Relative Imports (`.`, `..`)
  - **Von außen/Main**: Absolute Imports
  - **Faustregel**: Bei Unsicherheit absolute Imports

- **Virtuelle Umgebungen**:
  - **Immer** pro Projekt eine venv erstellen
  - `requirements.txt` pflegen für Reproduzierbarkeit
  - venv/ in `.gitignore`

- **Package-Struktur**:
  - Flache Hierarchie bevorzugen (max. 2-3 Ebenen)
  - `__all__` definieren für klare Public API
  - `__init__.py` für Convenience-Imports nutzen

- **CLI mit argparse**:
  - Nutze `description` und `help` für gute UX
  - `required=True` für essentielle Argumente
  - `action='store_true'` für Boolean-Flags

### Häufige Fehler (Gotchas)

- **Relativer Import im Top-Level-Skript**: Funktioniert nicht, nur absolute Imports
- **`__init__.py` vergessen**: Verzeichnis ist kein Package → ImportError
- **Zirkuläre Imports**: Module A und B importieren sich gegenseitig → ImportError
- **venv nicht aktiviert**: Packages werden in System-Python installiert
- **Modul-Name kollidiert mit Standard-Library**: Eigenes `math.py` überschreibt Standard `math`
- **`import *` und Namenskonflikte**: Unklar, woher Namen kommen
- **Relative Imports mit zu vielen `..`**: Verlässt Package-Root → ValueError

### Notizen

- Python 2 hatte implizite relative Imports (problematisch), Python 3 nur explizite
- `__init__.py` war bis Python 3.3 zwingend, ab 3.3+ optional (Namespace Packages)
- Best Practice: Trotzdem `__init__.py` nutzen für explizite Package-Definition
- `venv` ist seit Python 3.3+ in Standard-Library, vorher `virtualenv` als Drittanbieter-Tool
- `pip freeze` zeigt **alle** installierten Packages, auch transitive Dependencies
- Alternative zu `requirements.txt`: `Pipenv` (Pipfile), `Poetry` (pyproject.toml)
- Google/NumPy Docstring-Stile sind Konventionen, nicht Teil der Python-Spezifikation
- Für Production-Code: `mypy` für statische Typ-Prüfung, `pydantic` für Runtime-Validierung
- Lambda, `map`, `filter` stammen aus funktionalen Programmiersprachen (Lisp-Einfluss)

---

## V13 (2026-01-03) – Plots & Grafiken (Matplotlib) – Teil 1

### Neu eingeführt

#### matplotlib.pyplot Modul

- **`import matplotlib.pyplot as plt`** (Modul-Import, Python 3.5+)
  - Standard-Import für Matplotlib's Plot-Funktionalität
  - **Neu eingeführt in V13**
  - `pyplot` ist die MATLAB-ähnliche State-Machine-Schnittstelle
  - Alias `plt` ist Konvention (wie `np` für NumPy)
  - Installation: `pip install matplotlib`
  - Beispiel:
    ```python
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()
    ```

#### Plot-Funktionen

- **`plt.plot(x, y, fmt, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt einen Linienplot (oder Marker-Plot)
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `x`, `y`: Daten für X- und Y-Achse (Listen, Arrays, etc.)
    - `fmt`: Format-String (optional) – kombiniert Farbe, Marker, Linienstil
    - `color` oder `c`: Farbe (`'red'`, `'r'`, `'#FF0000'`, `(1,0,0)`)
    - `linestyle` oder `ls`: Linienstil (`'-'`, `'--'`, `':'`, `'-.'`)
    - `linewidth` oder `lw`: Liniendicke (Float)
    - `marker`: Marker-Stil (`'o'`, `'s'`, `'^'`, `'*'`, etc.)
    - `markersize` oder `ms`: Marker-Größe
    - `label`: Label für Legende (String)
    - `alpha`: Transparenz (0-1)
  - Format-String-Syntax: `[color][marker][linestyle]`, z.B. `'ro-'` (rot, Kreise, durchgezogen)
  - Beispiel:
    ```python
    plt.plot([1, 2, 3], [1, 4, 9], 'ro-', label='Quadratzahlen')
    plt.plot([1, 2, 3], [1, 2, 3], 'b--', linewidth=2, label='Linear')
    ```

- **`plt.scatter(x, y, s=None, c=None, marker='o', **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt einen Scatter-Plot (Punktdiagramm)
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `x`, `y`: Daten für X- und Y-Achse
    - `s`: Marker-Größe (Skalar oder Array, in Punkten²)
    - `c`: Farbe (Skalar, Sequenz oder Array für Colormap)
    - `marker`: Marker-Stil
    - `alpha`: Transparenz
    - `edgecolors`: Farbe des Marker-Rands
    - `linewidth` oder `linewidths`: Dicke des Marker-Rands
    - `cmap`: Colormap (z.B. `'viridis'`, `'plasma'`)
    - `vmin`, `vmax`: Wertebereich für Colormap
    - `zorder`: Zeichenreihenfolge
  - Unterschied zu `plot()`: Keine Verbindungslinien zwischen Punkten
  - Beispiel:
    ```python
    plt.scatter([1, 2, 3], [1, 4, 9], s=100, c='red', marker='o')
    plt.scatter([1, 2, 3], [2, 5, 10], s=[50, 100, 150], c=[1, 2, 3], cmap='viridis')
    ```

- **`plt.show()`** (Funktion, Matplotlib 1.0+)
  - Zeigt alle aktuellen Plots in einem interaktiven Fenster an
  - **Neu eingeführt in V13**
  - **Blockierend**: Wartet, bis Fenster geschlossen wird
  - In Jupyter Notebooks optional (Plots werden automatisch angezeigt)
  - In Skripten: **Notwendig**, damit Plots sichtbar werden
  - Beispiel:
    ```python
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()  # Öffnet Fenster
    ```

#### Achsenbeschriftungen und Titel

- **`plt.xlabel(label, fontdict=None, labelpad=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Beschriftung für die X-Achse
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `label`: Text für X-Achse (String)
    - `fontsize`: Schriftgröße
    - `fontweight`: Schriftgewicht (`'normal'`, `'bold'`)
    - `color`: Textfarbe
  - Beispiel:
    ```python
    plt.xlabel('Zeit (Sekunden)', fontsize=12)
    plt.xlabel('Temperatur (°C)', fontweight='bold')
    ```

- **`plt.ylabel(label, fontdict=None, labelpad=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Beschriftung für die Y-Achse
  - **Neu eingeführt in V13**
  - Gleiche Parameter wie `xlabel()`
  - Beispiel:
    ```python
    plt.ylabel('Geschwindigkeit (m/s)', fontsize=12)
    plt.ylabel('Anzahl', color='blue')
    ```

- **`plt.title(label, fontdict=None, loc='center', pad=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Titel für den Plot
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `label`: Titel-Text
    - `fontsize`: Schriftgröße
    - `fontweight`: Schriftgewicht (`'bold'`, etc.)
    - `loc`: Position (`'left'`, `'center'`, `'right'`)
    - `pad`: Abstand zum Plot (in Punkten)
  - Beispiel:
    ```python
    plt.title('Temperaturverlauf über 24 Stunden', fontsize=14, fontweight='bold')
    ```

#### Legende und Gitter

- **`plt.legend(loc='best', **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Zeigt Legende für geplottetem Daten an
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `loc`: Position (`'best'`, `'upper right'`, `'lower left'`, `'center'`, etc.)
    - `fontsize`: Schriftgröße
    - `frameon`: Ob Rahmen angezeigt wird (Boolean)
    - `shadow`: Schatten-Effekt (Boolean)
    - `ncol`: Anzahl Spalten
  - Benötigt `label`-Parameter in `plot()` oder `scatter()`
  - Beispiel:
    ```python
    plt.plot([1, 2, 3], [1, 4, 9], label='Daten A')
    plt.plot([1, 2, 3], [2, 5, 10], label='Daten B')
    plt.legend(loc='upper left', fontsize=10)
    ```

- **`plt.grid(visible=None, which='major', axis='both', **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Aktiviert/deaktiviert Gitterlinien
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `visible`: `True` oder `False` (vor 3.5: `b` für boolean)
    - `which`: `'major'`, `'minor'`, oder `'both'`
    - `axis`: `'both'`, `'x'`, oder `'y'`
    - `color`: Farbe der Gitterlinien
    - `linestyle`: Linienstil (`'-'`, `'--'`, `':'`)
    - `linewidth`: Liniendicke
    - `alpha`: Transparenz
  - Beispiel:
    ```python
    plt.grid(True)  # Aktiviert Gitter mit Standardeinstellungen
    plt.grid(True, alpha=0.3, linestyle='--')  # Transparentes gestricheltes Gitter
    ```

#### Achsen-Anpassung

- **`plt.xlim(left=None, right=None)`** (Funktion, Matplotlib 1.0+)
  - Setzt Bereich der X-Achse
  - **Neu eingeführt in V13**
  - **Parameter**: `left`, `right` (Zahlen oder `None` für Auto)
  - Kann auch als Getter verwendet werden: `xmin, xmax = plt.xlim()`
  - Beispiel:
    ```python
    plt.xlim(0, 10)  # X-Achse von 0 bis 10
    plt.xlim(left=0)  # Nur Minimum setzen, Maximum automatisch
    ```

- **`plt.ylim(bottom=None, top=None)`** (Funktion, Matplotlib 1.0+)
  - Setzt Bereich der Y-Achse
  - **Neu eingeführt in V13**
  - Gleiche Logik wie `xlim()`
  - Beispiel:
    ```python
    plt.ylim(0, 100)  # Y-Achse von 0 bis 100
    plt.ylim(bottom=0)  # Nur Minimum setzen
    ```

- **`plt.xticks(ticks=None, labels=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Position und Beschriftung der X-Achsen-Ticks
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `ticks`: Liste der Tick-Positionen
    - `labels`: Liste der Tick-Beschriftungen (Strings)
    - `rotation`: Drehwinkel der Labels (Grad)
    - `fontsize`: Schriftgröße
  - Beispiel:
    ```python
    plt.xticks([0, 5, 10, 15, 20])  # Nur diese Werte anzeigen
    plt.xticks(range(0, 25, 3))  # 0, 3, 6, 9, ..., 24
    plt.xticks([1, 2, 3], ['Jan', 'Feb', 'Mär'], rotation=45)  # Custom Labels
    ```

- **`plt.yticks(ticks=None, labels=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Position und Beschriftung der Y-Achsen-Ticks
  - **Neu eingeführt in V13**
  - Gleiche Parameter wie `xticks()`
  - Beispiel:
    ```python
    plt.yticks([0, 25, 50, 75, 100])
    ```

#### Referenzlinien und -bereiche

- **`plt.axhline(y=0, xmin=0, xmax=1, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Zeichnet horizontale Linie über die gesamte X-Achse
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `y`: Y-Position der Linie
    - `xmin`, `xmax`: Relative Position (0-1) auf X-Achse
    - `color`: Linienfarbe
    - `linestyle`: Linienstil
    - `linewidth`: Liniendicke
    - `label`: Label für Legende
  - Beispiel:
    ```python
    plt.axhline(y=20, color='red', linestyle='--', label='Soll-Temperatur')
    plt.axhline(y=0, color='black', linewidth=0.8)  # Nulllinie
    ```

- **`plt.axvline(x=0, ymin=0, ymax=1, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Zeichnet vertikale Linie über die gesamte Y-Achse
  - **Neu eingeführt in V13**
  - **Parameter**: Analog zu `axhline()`, aber mit `x` statt `y`
  - Beispiel:
    ```python
    plt.axvline(x=64, color='red', linestyle='--', label='L1 Grenze')
    ```

- **`plt.axhspan(ymin, ymax, xmin=0, xmax=1, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Schattiert horizontalen Bereich (zwischen zwei Y-Werten)
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `ymin`, `ymax`: Y-Bereich in Datenkoordinaten
    - `xmin`, `xmax`: Relative Position (0-1) auf X-Achse
    - `color`: Füllfarbe
    - `alpha`: Transparenz
  - Beispiel:
    ```python
    plt.axhspan(18, 22, alpha=0.2, color='green', label='Normbereich')
    ```

- **`plt.axvspan(xmin, xmax, ymin=0, ymax=1, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Schattiert vertikalen Bereich (zwischen zwei X-Werten)
  - **Neu eingeführt in V13**
  - **Parameter**: Analog zu `axhspan()`, aber X und Y vertauscht
  - Beispiel:
    ```python
    plt.axvspan(135.65, 160, color='red', alpha=0.15, label='Kritischer Bereich')
    ```

#### Erweiterte Plot-Funktionen

- **`plt.errorbar(x, y, yerr=None, xerr=None, fmt='', **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt Plot mit Fehlerbalken (Error Bars)
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `x`, `y`: Daten
    - `yerr`: Y-Fehler (Skalar, Array, oder `[unten, oben]`)
    - `xerr`: X-Fehler (analog zu `yerr`)
    - `fmt`: Format-String (wie bei `plot()`)
    - `ecolor`: Farbe der Error Bars
    - `capsize`: Länge der "Caps" (horizontale Endlinien)
    - `capthick`: Dicke der Caps
    - `elinewidth`: Dicke der Error Bars
  - Beispiel:
    ```python
    plt.errorbar([1, 2, 3], [10, 20, 30], yerr=[1, 2, 3], 
                 fmt='o-', capsize=5, label='Messdaten')
    ```

- **`plt.fill_between(x, y1, y2=0, where=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Schattiert Bereich zwischen zwei Kurven
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `x`: X-Daten
    - `y1`, `y2`: Untere und obere Kurve (oder `y2=0` für Füllung bis X-Achse)
    - `where`: Boolean-Array zur selektiven Füllung
    - `alpha`: Transparenz
    - `color`: Füllfarbe
    - `interpolate`: Interpolation an Übergängen (Boolean)
  - Beispiel:
    ```python
    plt.fill_between([1, 2, 3], [1, 4, 9], [2, 5, 10], alpha=0.3, color='blue')
    ```

- **`plt.text(x, y, s, fontdict=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Platziert Text an beliebiger Position im Plot
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `x`, `y`: Position in Datenkoordinaten
    - `s`: Text-String
    - `fontsize`: Schriftgröße
    - `fontweight`: Schriftgewicht
    - `color`: Textfarbe
    - `bbox`: Box um Text herum (Dictionary)
    - `ha`: Horizontale Ausrichtung (`'left'`, `'center'`, `'right'`)
    - `va`: Vertikale Ausrichtung (`'top'`, `'center'`, `'bottom'`)
  - Beispiel:
    ```python
    plt.text(5, 10, "Wichtiger Punkt", fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
    ```

#### Subplots und Layout

- **`plt.subplots(nrows=1, ncols=1, figsize=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt Figure und ein Grid von Subplots
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `nrows`, `ncols`: Anzahl Zeilen und Spalten
    - `figsize`: Gesamtgröße als Tupel `(breite, höhe)` in Zoll
    - `sharex`, `sharey`: Achsen zwischen Subplots teilen (Boolean)
  - **Rückgabe**: `(fig, axes)` – Figure-Objekt und Axes-Array
  - Beispiel:
    ```python
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot([1, 2, 3], [1, 4, 9])
    ax2.scatter([1, 2, 3], [2, 5, 10])
    ```

- **`plt.figure(num=None, figsize=None, dpi=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt neue Figure (Zeichenfläche)
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `num`: Figure-Nummer (Integer oder String)
    - `figsize`: Größe `(breite, höhe)` in Zoll
    - `dpi`: Auflösung (Dots Per Inch)
  - Beispiel:
    ```python
    plt.figure(figsize=(12, 6))
    plt.plot([1, 2, 3], [1, 4, 9])
    ```

- **`plt.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)`** (Funktion, Matplotlib 1.1+)
  - Passt Subplot-Parameter automatisch an, damit nichts abgeschnitten wird
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `pad`: Abstand zu Figure-Rand
    - `h_pad`, `w_pad`: Abstand zwischen Subplots (horizontal/vertikal)
  - Sollte **nach** allen Plots aufgerufen werden
  - Beispiel:
    ```python
    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot([1, 2, 3], [1, 4, 9])
    ax2.plot([1, 2, 3], [2, 5, 10])
    plt.tight_layout()  # Optimiert Layout
    ```

#### Skalierung und Speichern

- **`plt.xscale(value, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Skalierung der X-Achse
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `value`: `'linear'`, `'log'`, `'symlog'`, `'logit'`
    - `base`: Basis für logarithmische Skala (z.B. `base=2` oder `base=10`)
  - Beispiel:
    ```python
    plt.xscale('log')  # Logarithmische X-Achse (Basis 10)
    plt.xscale('log', base=2)  # Logarithmische X-Achse (Basis 2)
    ```

- **`plt.yscale(value, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Skalierung der Y-Achse
  - **Neu eingeführt in V13**
  - Gleiche Parameter wie `xscale()`
  - Beispiel:
    ```python
    plt.yscale('log')  # Logarithmische Y-Achse
    ```

- **`plt.savefig(fname, dpi=None, format=None, bbox_inches=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Speichert aktuellen Plot als Bild-Datei
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `fname`: Dateiname (String) – Format wird aus Endung abgeleitet
    - `dpi`: Auflösung (z.B. `dpi=300` für hohe Qualität)
    - `format`: Explizites Format (`'png'`, `'pdf'`, `'svg'`, `'jpg'`)
    - `bbox_inches`: `'tight'` schneidet Whitespace ab
    - `transparent`: Transparenter Hintergrund (Boolean)
  - **Muss vor `plt.show()`** aufgerufen werden!
  - Beispiel:
    ```python
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.savefig('plot.png', dpi=300, bbox_inches='tight')
    plt.show()
    ```

- **`plt.colorbar(mappable=None, cax=None, ax=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Fügt Colorbar (Farbskala) zu Plot hinzu
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `mappable`: Plot-Objekt mit Farb-Mapping (z.B. von `scatter()` oder `imshow()`)
    - `label`: Beschriftung der Colorbar
    - `orientation`: `'vertical'` oder `'horizontal'`
  - Beispiel:
    ```python
    scatter = plt.scatter([1, 2, 3], [1, 4, 9], c=[1, 2, 3], cmap='viridis')
    plt.colorbar(scatter, label='Werte')
    ```

#### NumPy-Funktionen (für Matplotlib genutzt)

- **`numpy.polyfit(x, y, deg)`** (NumPy, Python 2.6+)
  - Berechnet Polynom-Koeffizienten für Least-Squares-Fit
  - **Neu eingeführt in V13** (als Teil von Matplotlib-Workflows)
  - **Parameter**:
    - `x`, `y`: Datenpunkte
    - `deg`: Grad des Polynoms (1 = linear, 2 = quadratisch, ...)
  - **Rückgabe**: Array der Koeffizienten `[a_n, a_{n-1}, ..., a_1, a_0]`
  - Beispiel:
    ```python
    import numpy as np
    koeff = np.polyfit([1, 2, 3], [2, 4, 5], deg=1)  # Lineare Regression
    # koeff ≈ [1.5, 0.5] → y = 1.5x + 0.5
    ```

- **`numpy.polyval(p, x)`** (NumPy, Python 2.6+)
  - Wertet Polynom an gegebenen Punkten aus
  - **Neu eingeführt in V13**
  - **Parameter**:
    - `p`: Koeffizienten-Array (von `polyfit()`)
    - `x`: X-Werte (Skalar oder Array)
  - Beispiel:
    ```python
    koeff = [1.5, 0.5]  # y = 1.5x + 0.5
    y = np.polyval(koeff, [1, 2, 3])  # y = [2.0, 3.5, 5.0]
    ```

- **`numpy.linspace(start, stop, num=50)`** (NumPy, Python 2.0+)
  - Erstellt Array mit gleichmäßig verteilten Werten
  - **Neu eingeführt in V13** (als Alternative zu List Comprehensions)
  - **Parameter**:
    - `start`, `stop`: Bereich (beide inklusive!)
    - `num`: Anzahl der Werte
  - Beispiel:
    ```python
    x = np.linspace(0, 10, 21)  # 21 Werte von 0 bis 10
    # x = [0, 0.5, 1.0, 1.5, ..., 9.5, 10.0]
    ```

### Konzepte und Best Practices

- **Plot-Workflow**:
  1. Daten vorbereiten (Listen, Arrays)
  2. Plot erstellen (`plot()`, `scatter()`, etc.)
  3. Anpassungen (Titel, Labels, Legende, Gitter)
  4. Optional: Speichern (`savefig()`)
  5. Anzeigen (`show()`)

- **Format-String-Syntax**:
  - **Farben**: `'r'` (rot), `'b'` (blau), `'g'` (grün), `'k'` (schwarz), `'y'` (gelb), `'c'` (cyan), `'m'` (magenta)
  - **Marker**: `'o'` (Kreis), `'s'` (Quadrat), `'^'` (Dreieck), `'*'` (Stern), `'+'` (Plus), `'x'` (Kreuz)
  - **Linienstile**: `'-'` (durchgezogen), `'--'` (gestrichelt), `':'` (gepunktet), `'-.'` (Strich-Punkt)
  - Beispiel: `'ro-'` = rote Kreise mit durchgezogener Linie

- **Transparenz (alpha)**:
  - Wert zwischen 0 (unsichtbar) und 1 (vollständig opak)
  - Nützlich für: Überlappende Plots, Hintergrund-Schattierungen, Unsicherheitsbereiche
  - Beispiel: `alpha=0.3` für 30% Deckkraft

- **Zeichenreihenfolge (zorder)**:
  - Höhere Werte werden "oben" gezeichnet
  - Standard: `plot()` und `scatter()` haben `zorder=2`
  - Nützlich, um wichtige Elemente in den Vordergrund zu bringen
  - Beispiel: `plt.scatter(..., zorder=5)` liegt über `plt.plot(..., zorder=2)`

- **Subplots vs. Figure**:
  - **`plt.figure()`**: Erstellt leere Figure, Plots werden sequenziell hinzugefügt
  - **`plt.subplots()`**: Erstellt Figure + Grid von Axes → Moderner, empfohlen
  - Mit Subplots: `ax1.plot()` statt `plt.plot()`

- **Logarithmische Skalen**:
  - **Wann verwenden?**: Daten mit großem Wertebereich (mehrere Größenordnungen)
  - **Basis 10 (Standard)**: Gute Wahl für wissenschaftliche Daten
  - **Basis 2**: Gut für Computer-Größen (KB, MB, GB, ...)
  - **Wichtig**: Nur für strikt positive Werte (log(0) und log(negative) sind undefiniert)

- **Matplotlib Installation**:
  ```bash
  pip install matplotlib
  ```

- **Backend-Probleme beheben**:
  - Falls Plot-Fenster nicht erscheint: Backend setzen
  ```python
  import matplotlib
  matplotlib.use('TkAgg')  # oder 'Qt5Agg', 'GTK3Agg'
  import matplotlib.pyplot as plt
  ```

- **Jupyter Notebooks**:
  - Plots werden automatisch inline angezeigt
  - `plt.show()` optional
  - Für interaktive Plots: `%matplotlib widget`

### Häufige Fehler (Gotchas)

- **Listen mit unterschiedlichen Längen**:
  ```python
  plt.plot([1, 2, 3], [1, 4, 9, 16])  # ValueError: x and y must have same first dimension
  ```

- **Legende ohne Labels**:
  ```python
  plt.plot([1, 2, 3], [1, 4, 9])  # Kein label!
  plt.legend()  # Legende ist leer
  ```

- **savefig() nach show()**:
  ```python
  plt.plot([1, 2, 3], [1, 4, 9])
  plt.show()
  plt.savefig('plot.png')  # Speichert leeren Plot!
  ```
  **Lösung**: `savefig()` immer **vor** `show()` aufrufen.

- **Logarithmische Skala mit Null-Werten**:
  ```python
  plt.plot([0, 1, 2], [0, 10, 100])
  plt.yscale('log')  # Warnung/Fehler: log(0) undefiniert
  ```

- **fill_between() mit falscher Reihenfolge**:
  ```python
  plt.fill_between(x, obere_grenze, untere_grenze)  # FALSCH!
  plt.fill_between(x, untere_grenze, obere_grenze)  # RICHTIG
  ```

- **Matplotlib nicht installiert**:
  ```python
  import matplotlib.pyplot as plt  # ModuleNotFoundError
  ```
  **Lösung**: `pip install matplotlib`

- **plt.plot() vs. ax.plot() mischen**:
  ```python
  fig, ax = plt.subplots()
  plt.plot([1, 2, 3], [1, 4, 9])  # Zeichnet NICHT in ax!
  # Richtig: ax.plot([1, 2, 3], [1, 4, 9])
  ```

### Notizen

- Matplotlib basiert auf MATLAB's Plotting-API (daher der Name und die Syntax)
- Zwei Schnittstellen: **pyplot** (State-Machine, einfach) und **Object-Oriented** (explizit, flexibel)
- Standard-Farbzyklen: `C0` bis `C9` (automatische Farb-Rotation)
- Colormap-Konventionen: `'viridis'` (Standard seit 2.0), `'plasma'`, `'inferno'`, `'magma'` (wahrnehmungs-uniform)
- `plt.savefig()` unterstützt: PNG, PDF, SVG, EPS, PS, JPG/JPEG
- DPI: 72 (Screen), 150 (Draft), 300 (Publication), 600 (High-Quality Print)
- `tight_layout()` löst die meisten Layout-Probleme, aber nicht alle (bei komplexen Layouts: `constrained_layout` oder manuell)
- Alternative zu Matplotlib: Seaborn (high-level), Plotly (interaktiv), Bokeh (Web)
- Für 3D-Plots: `from mpl_toolkits.mplot3d import Axes3D`
- Für Animationen: `from matplotlib.animation import FuncAnimation`

---

## V14 (2026-01-03) – Betriebssysteme & Rechnerarchitektur – Teil 2 / Plots & Grafiken (Matplotlib) – Teil 2

### Neu eingeführt

#### Matplotlib Bar Charts

- **`plt.bar(x, height, width=0.8, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt vertikales Balkendiagramm für kategorische Daten
  - Parameter:
    - `x`: Positionen der Balken (Liste oder Array)
    - `height`: Höhen der Balken
    - `width`: Breite der Balken (Standard: 0.8)
    - `color`: Farbe(n) der Balken
    - `edgecolor`: Farbe der Balkenränder
    - `alpha`: Transparenz (0-1)
    - `label`: Label für Legende
  - Signatur: `plt.bar(x, height, width=0.8, **kwargs)` → `BarContainer`
  - Beispiel:
    ```python
    sprachen = ['Python', 'Java', 'C++']
    beliebtheit = [85, 65, 55]
    plt.bar(sprachen, beliebtheit, color='steelblue', edgecolor='black')
    ```

- **`plt.barh(y, width, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt horizontales Balkendiagramm
  - Parameter analog zu `plt.bar()`, aber `y` statt `x` und `width` statt `height`
  - Signatur: `plt.barh(y, width, **kwargs)` → `BarContainer`
  - Beispiel: `plt.barh(['A', 'B', 'C'], [10, 20, 15])`

- **`bottom`-Parameter für gestapelte Bar Charts** (Parameter, Matplotlib 1.0+)
  - Gibt Startposition (Höhe) für Balken an
  - Ermöglicht gestapelte Balkendiagramme
  - Beispiel:
    ```python
    plt.bar(kategorien, werte1, label='Dataset 1')
    plt.bar(kategorien, werte2, bottom=werte1, label='Dataset 2')  # Stapelt auf werte1
    ```

#### Matplotlib Histogramme

- **`plt.hist(x, bins=10, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Erstellt Histogramm zur Visualisierung von Häufigkeitsverteilungen
  - Parameter:
    - `x`: Daten (Liste oder Array)
    - `bins`: Anzahl der Bins oder Liste von Bin-Grenzen
    - `range`: Tuple `(min, max)` für Wertebereich
    - `density`: `True` für normalisierte Dichte (Fläche = 1)
    - `cumulative`: `True` für kumulatives Histogramm
    - `color`: Füllfarbe
    - `edgecolor`: Randfarbe
    - `alpha`: Transparenz
  - Signatur: `plt.hist(x, bins=10, **kwargs)` → `(n, bins, patches)`
  - Beispiel:
    ```python
    daten = np.random.normal(100, 15, 1000)
    plt.hist(daten, bins=30, color='lightblue', edgecolor='black')
    ```

- **`bins`-Parameter (erweitert)** (Parameter)
  - Integer: Anzahl der Bins
  - Sequenz: Explizite Bin-Grenzen `[min, ..., max]`
  - String: Automatische Bin-Wahl (`'auto'`, `'sturges'`, `'fd'`, `'scott'`)
  - Beispiel: `bins='auto'` für intelligente Bin-Anzahl

- **`density`-Parameter** (Parameter)
  - `True`: Normalisiert Histogramm zu Wahrscheinlichkeitsdichte (Fläche = 1)
  - Nützlich zum Vergleich von Datensätzen unterschiedlicher Größe
  - Beispiel: `plt.hist(daten, density=True)`

- **`cumulative`-Parameter** (Parameter)
  - `True`: Erstellt kumulatives Histogramm
  - Zeigt Summe aller Werte bis zu jedem Bin
  - Beispiel: `plt.hist(daten, cumulative=True)`

#### Matplotlib Subplots (erweitert)

- **`plt.subplot(nrows, ncols, index)`** (Funktion, Matplotlib 1.0+)
  - Erstellt Subplot in Grid-Position (MATLAB-Style)
  - Parameter:
    - `nrows`: Anzahl Zeilen im Grid
    - `ncols`: Anzahl Spalten im Grid
    - `index`: Position des Subplots (1-basiert!)
  - Signatur: `plt.subplot(nrows, ncols, index)` → `Axes`
  - Beispiel:
    ```python
    plt.subplot(2, 2, 1)  # Oben links
    plt.plot([1, 2, 3])
    plt.subplot(2, 2, 2)  # Oben rechts
    plt.bar([1, 2], [3, 4])
    ```

- **`plt.subplots(nrows=1, ncols=1, figsize=None, **kwargs)`** (Funktion, Matplotlib 1.0+, erweiterte Verwendung)
  - Erstellt Figure und Grid von Subplots (objektorientierter Ansatz)
  - Parameter:
    - `nrows`, `ncols`: Anzahl Zeilen/Spalten
    - `figsize`: Tuple `(breite, höhe)` in Zoll
    - `sharex`, `sharey`: Achsen zwischen Subplots teilen (Boolean)
  - Rückgabe: `(fig, axes)` – Figure-Objekt und Axes-Array
  - Signatur: `plt.subplots(nrows, ncols, figsize)` → `(Figure, Axes/ndarray)`
  - Beispiel:
    ```python
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes[0, 0].plot([1, 2, 3])
    axes[0, 1].bar([1, 2], [3, 4])
    ```

- **`plt.subplot2grid(shape, loc, colspan=1, rowspan=1, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Flexiblere Subplot-Positionierung mit variablen Größen
  - Parameter:
    - `shape`: Tuple `(nrows, ncols)` des Grids
    - `loc`: Tuple `(row, col)` für Startposition (0-basiert)
    - `colspan`, `rowspan`: Wie viele Spalten/Zeilen der Subplot umfasst
  - Signatur: `plt.subplot2grid(shape, loc, **kwargs)` → `Axes`
  - Beispiel:
    ```python
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)  # Breiter Plot
    ax2 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)  # Hoher Plot
    ```

- **`GridSpec` (Klasse)** (Klasse, `matplotlib.gridspec`, Matplotlib 1.0+)
  - Noch flexibleres Grid-Layout für komplexe Subplot-Anordnungen
  - Import: `from matplotlib.gridspec import GridSpec`
  - Signatur: `GridSpec(nrows, ncols, **kwargs)` → `GridSpec`-Objekt
  - Beispiel:
    ```python
    from matplotlib.gridspec import GridSpec
    fig = plt.figure(figsize=(12, 8))
    gs = GridSpec(3, 3, figure=fig)
    ax1 = fig.add_subplot(gs[0:2, :])  # Oben, volle Breite
    ax2 = fig.add_subplot(gs[2, 0])    # Unten links
    ```

#### Matplotlib Achsenskalierungen

- **`plt.xscale(value, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Skalierung der X-Achse
  - Parameter:
    - `value`: `'linear'`, `'log'`, `'symlog'`, `'logit'`
    - `base`: Basis für logarithmische Skala (z.B. `base=2` oder `base=10`)
  - Signatur: `plt.xscale(value, **kwargs)` → `None`
  - Beispiel:
    ```python
    plt.xscale('log')  # Logarithmische X-Achse (Basis 10)
    plt.xscale('log', base=2)  # Basis 2
    ```

- **`plt.yscale(value, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Setzt Skalierung der Y-Achse
  - Parameter und Verwendung analog zu `plt.xscale()`
  - Signatur: `plt.yscale(value, **kwargs)` → `None`
  - Beispiel: `plt.yscale('log')`

- **`plt.loglog(x, y, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Kurzform für Plot mit beiden Achsen logarithmisch
  - Äquivalent zu `plt.plot()` + `plt.xscale('log')` + `plt.yscale('log')`
  - Signatur: `plt.loglog(x, y, **kwargs)` → Liste von `Line2D`
  - Beispiel:
    ```python
    x = np.logspace(0, 5, 100)
    y = x ** 2
    plt.loglog(x, y, 'ro-')
    ```

#### Matplotlib Annotationen

- **`plt.annotate(text, xy, xytext=None, arrowprops=None, **kwargs)`** (Funktion, Matplotlib 1.0+)
  - Fügt Text mit Pfeil zu einem Punkt hinzu
  - Parameter:
    - `text`: Annotationstext (String)
    - `xy`: Koordinaten des annotierten Punktes (Tuple)
    - `xytext`: Koordinaten des Textes (Tuple, optional)
    - `textcoords`: Koordinatensystem für `xytext` (`'offset points'`, `'data'`, etc.)
    - `arrowprops`: Dictionary mit Pfeilkonfiguration
    - `bbox`: Dictionary für Rahmen um Text
    - `fontsize`: Schriftgröße
  - Signatur: `plt.annotate(text, xy, **kwargs)` → `Annotation`
  - Beispiel:
    ```python
    plt.annotate('Maximum', 
                 xy=(5, 10), 
                 xytext=(3, 8),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    ```

- **`arrowprops`-Dictionary** (Parameter-Dictionary)
  - Konfiguration für Annotationspfeil
  - Keys:
    - `facecolor`: Pfeilfarbe
    - `shrink`: Abstand zu Punkt und Text (0-1)
    - `width`: Pfeilbreite
    - `arrowstyle`: Pfeilstil (`'->'`, `'-|>'`, `'<->'`, `'fancy'`, etc.)
    - `connectionstyle`: Verbindungsstil (`'arc3,rad=0.3'` für Kurve)
    - `lw` oder `linewidth`: Liniendicke
  - Beispiel:
    ```python
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', color='black', lw=1.5)
    ```

- **`bbox`-Dictionary (für Annotationen)** (Parameter-Dictionary)
  - Konfiguration für Rahmen um Annotationstext
  - Keys:
    - `boxstyle`: Form (`'round'`, `'round,pad=0.5'`, `'square'`, `'rarrow'`, etc.)
    - `facecolor`: Füllfarbe
    - `edgecolor`: Rahmenfarbe
    - `alpha`: Transparenz (0-1)
  - Beispiel:
    ```python
    bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7)
    ```

#### NumPy-Funktionen (für Matplotlib genutzt)

- **`np.logspace(start, stop, num=50, base=10.0)`** (NumPy-Funktion)
  - Erzeugt Array mit logarithmisch verteilten Werten
  - Werte: `base^start` bis `base^stop`
  - Parameter:
    - `start`: Exponent für Startwert
    - `stop`: Exponent für Endwert
    - `num`: Anzahl der Werte
    - `base`: Basis (Standard: 10)
  - Signatur: `np.logspace(start, stop, num)` → `ndarray`
  - Beispiel:
    ```python
    x = np.logspace(0, 3, 4)  # [10^0, 10^1, 10^2, 10^3] = [1, 10, 100, 1000]
    ```

- **`np.argmax(array)`** (NumPy-Funktion)
  - Gibt Index des maximalen Werts im Array zurück
  - Signatur: `np.argmax(a, axis=None)` → `int` oder `ndarray`
  - Beispiel:
    ```python
    arr = [10, 25, 5, 30]
    idx = np.argmax(arr)  # idx = 3 (Position von 30)
    ```

- **`np.argmin(array)`** (NumPy-Funktion)
  - Gibt Index des minimalen Werts im Array zurück
  - Signatur: `np.argmin(a, axis=None)` → `int` oder `ndarray`
  - Beispiel:
    ```python
    arr = [10, 5, 25, 30]
    idx = np.argmin(arr)  # idx = 1 (Position von 5)
    ```

- **`np.cumsum(array)`** (NumPy-Funktion)
  - Berechnet kumulative Summe entlang Array
  - Jedes Element ist Summe aller vorherigen + aktuelles Element
  - Signatur: `np.cumsum(a, axis=None)` → `ndarray`
  - Beispiel:
    ```python
    arr = [1, 2, 3, 4]
    cumsum = np.cumsum(arr)  # [1, 3, 6, 10]
    ```

#### Erweiterte savefig-Optionen

- **`transparent`-Parameter für `plt.savefig()`** (Parameter, Matplotlib 1.0+)
  - Speichert Plot mit transparentem Hintergrund
  - Nützlich für Overlays auf farbigen Hintergründen
  - Beispiel:
    ```python
    plt.savefig('plot.png', dpi=300, transparent=True)
    ```

### Konzepte und Best Practices

- **Bar Charts**: Ideal für kategorische Daten und Vergleiche. Gruppierte Bar Charts für mehrere Datensätze, gestapelte für Teilmengen.
- **Histogramme**: Zeigen Häufigkeitsverteilungen. Bin-Anzahl entscheidend (Faustregel: √n bis 2√n Bins).
- **Logarithmische Achsen**: Unerlässlich bei Daten über mehrere Größenordnungen (z.B. 1 bis 1.000.000).
- **Subplots**: `plt.subplots()` ist moderner als `plt.subplot()`. Verwende `tight_layout()` immer.
- **Annotationen**: Heben wichtige Datenpunkte hervor. `arrowprops` und `bbox` für professionelles Aussehen.
- **Speicherformate**: PNG für Web (mit mind. 150 DPI), PDF/SVG für Publikationen (Vektoren).

### Notizen

- `plt.bar()` und `plt.hist()` existieren seit Matplotlib 1.0
- `GridSpec` ermöglicht komplexeste Subplot-Layouts, aber `plt.subplots()` reicht meist aus
- Logarithmische Achsen zeigen Powerlaws (y = x^k) als Geraden im log-log-Plot
- `np.logspace()` ist das log-Äquivalent zu `np.linspace()`
- Bei Histogrammen: `density=True` für Wahrscheinlichkeitsdichte, `cumulative=True` für CDF
- Annotationen mit `textcoords='offset points'` für pixelgenaue Positionierung
- Transparenter Hintergrund (`transparent=True`) funktioniert mit PNG und PDF, nicht mit JPG

---

## V15 (2026-01-04) – Netzwerktechnik Grundlagen & Protokolle – Teil 1 / Große Datenmengen verarbeiten – Teil 1

### Neu eingeführt

#### Generator-Funktionen und yield

- **`yield`-Statement** (Python Keyword, Python 2.2+)
  - Pausiert Funktionsausführung und gibt Wert zurück, behält aber Zustand
  - Wandelt Funktion in einen Generator um (lazy evaluation)
  - Syntax: `yield wert`
  - Signatur: `yield expression`
  - Beispiel:
    ```python
    def countdown(n):
        while n > 0:
            yield n
            n -= 1
    
    for i in countdown(5):
        print(i)  # 5, 4, 3, 2, 1
    ```
  - **Unterschied zu `return`**: `yield` pausiert und setzt fort, `return` beendet vollständig
  - **Verwendung**: Memory-effiziente Daten-Pipelines, große Dateiverarbeitung

- **Generator-Funktionen** (Konzept, Python 2.2+)
  - Funktionen mit mindestens einem `yield`-Statement
  - Geben Generator-Objekt zurück (Iterator)
  - **Lazy Evaluation**: Werte werden bei Bedarf berechnet, nicht alle auf einmal
  - **Memory-Effizienz**: O(1) Speicher statt O(n) für Listen
  - Beispiel:
    ```python
    def lies_grosse_datei(dateiname):
        with open(dateiname, 'r') as datei:
            for zeile in datei:
                yield zeile.strip()
    
    # Nur eine Zeile zur Zeit im Speicher
    for zeile in lies_grosse_datei('huge.txt'):
        verarbeite(zeile)
    ```

- **Generator-Pipelines** (Pattern, Python 2.2+)
  - Verkettung mehrerer Generatoren für Daten-Transformation
  - Jeder Generator nimmt vorherigen als Input
  - Beispiel:
    ```python
    def lies_zeilen(datei):
        for zeile in datei:
            yield zeile
    
    def filtere_leere(zeilen):
        for zeile in zeilen:
            if zeile.strip():
                yield zeile
    
    def zu_grossbuchstaben(zeilen):
        for zeile in zeilen:
            yield zeile.upper()
    
    # Pipeline:
    with open('data.txt') as f:
        pipeline = zu_grossbuchstaben(filtere_leere(lies_zeilen(f)))
        for zeile in pipeline:
            print(zeile)
    ```

#### Iterator-Protokoll

- **Iterator-Protokoll** (Konzept, Python 2.2+)
  - Zwei Methoden erforderlich: `__iter__()` und `__next__()`
  - `__iter__()`: Gibt Iterator-Objekt zurück (oft `self`)
  - `__next__()`: Gibt nächstes Element zurück oder wirft `StopIteration`
  - Beispiel:
    ```python
    class CountDown:
        def __init__(self, start):
            self.current = start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            self.current -= 1
            return self.current + 1
    
    for i in CountDown(3):
        print(i)  # 3, 2, 1
    ```

- **Iterator vs. Iterable** (Konzept)
  - **Iterable**: Objekt mit `__iter__()`, das Iterator zurückgibt
    - Kann mehrfach durchlaufen werden
    - Beispiele: Liste, Tuple, String, Dictionary
  - **Iterator**: Objekt mit `__iter__()` (gibt `self` zurück) und `__next__()`
    - Kann nur einmal durchlaufen werden (exhausted danach)
    - Beispiele: Generator, file object, enumerate-Objekt
  - **Regel**: Jeder Iterator ist Iterable, aber nicht jedes Iterable ist Iterator
  - Beispiel:
    ```python
    liste = [1, 2, 3]  # Iterable (nicht Iterator)
    iter1 = iter(liste)  # Iterator
    print(list(iter1))  # [1, 2, 3]
    print(list(iter1))  # [] (exhausted!)
    print(list(liste))  # [1, 2, 3] (funktioniert immer)
    ```

#### Built-in Funktionen

- **`iter(iterable)`** (Built-in, Python 2.2+)
  - Gibt Iterator-Objekt für ein Iterable zurück
  - Ruft intern `iterable.__iter__()` auf
  - Signatur: `iter(iterable)` → `iterator`
  - Beispiel:
    ```python
    liste = [1, 2, 3]
    iterator = iter(liste)
    print(next(iterator))  # 1
    print(next(iterator))  # 2
    ```

- **`next(iterator, default=None)`** (Built-in, Python 2.6+)
  - Gibt nächstes Element des Iterators zurück
  - Wirft `StopIteration` wenn exhausted (außer `default` angegeben)
  - Ruft intern `iterator.__next__()` auf
  - Signatur: `next(iterator[, default])` → Element
  - Beispiel:
    ```python
    it = iter([1, 2])
    print(next(it))  # 1
    print(next(it))  # 2
    print(next(it, 'Ende'))  # 'Ende' (statt StopIteration)
    ```

#### CSV-Modul

- **`csv`-Modul** (Standard Library, Python 2.3+)
  - Modul zum Lesen und Schreiben von CSV-Dateien
  - Import: `import csv`
  - **Wichtig**: Bei Schreiben unter Windows `newline=''` erforderlich

- **`csv.reader(csvfile, delimiter=',', **kwargs)`** (Funktion, Python 2.3+)
  - Liest CSV-Datei und gibt Iterator von Listen zurück
  - Jede Zeile ist Liste von Strings
  - Parameter:
    - `csvfile`: Datei-Objekt (geöffnet mit `open()`)
    - `delimiter`: Trennzeichen (Standard: `','`)
    - `quotechar`: Quote-Zeichen (Standard: `'"'`)
    - `skipinitialspace`: Whitespace nach delimiter ignorieren (Boolean)
  - Signatur: `csv.reader(csvfile, **fmtparams)` → `csv.reader` (Iterator)
  - Beispiel:
    ```python
    import csv
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for zeile in reader:
            print(zeile)  # ['Alice', '25', 'Berlin']
    ```

- **`csv.writer(csvfile, delimiter=',', **kwargs)`** (Funktion, Python 2.3+)
  - Schreibt Daten in CSV-Format
  - Parameter:
    - `csvfile`: Datei-Objekt (mit `newline=''` öffnen!)
    - `delimiter`: Trennzeichen (Standard: `','`)
  - Methoden:
    - `.writerow(row)`: Schreibt eine Zeile (Liste oder Tuple)
    - `.writerows(rows)`: Schreibt mehrere Zeilen (Liste von Listen)
  - Signatur: `csv.writer(csvfile, **fmtparams)` → `csv.writer`
  - Beispiel:
    ```python
    import csv
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Alter'])
        writer.writerow(['Bob', '30'])
    ```

- **`csv.DictReader(csvfile, fieldnames=None, **kwargs)`** (Klasse, Python 2.3+)
  - Liest CSV mit Header als Dictionary pro Zeile
  - Erste Zeile wird als Feldnamen verwendet (außer `fieldnames` angegeben)
  - Rückgabe: Iterator von `OrderedDict` (Python 2) oder `dict` (Python 3.8+)
  - Parameter:
    - `csvfile`: Datei-Objekt
    - `fieldnames`: Liste von Feldnamen (optional, Standard: erste Zeile)
  - Signatur: `csv.DictReader(csvfile, fieldnames=None, **fmtparams)` → Iterator
  - Beispiel:
    ```python
    import csv
    with open('students.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['Name'], row['Alter'])
            # {'Name': 'Alice', 'Alter': '25', 'Stadt': 'Berlin'}
    ```

- **`csv.DictWriter(csvfile, fieldnames, **kwargs)`** (Klasse, Python 2.3+)
  - Schreibt Dictionaries als CSV mit benannten Feldern
  - Parameter:
    - `csvfile`: Datei-Objekt (mit `newline=''`!)
    - `fieldnames`: Liste von Feldnamen (legt Spaltenreihenfolge fest)
    - `extrasaction`: Was bei extra Keys tun (`'raise'` oder `'ignore'`)
  - Methoden:
    - `.writeheader()`: Schreibt Header-Zeile
    - `.writerow(rowdict)`: Schreibt Dictionary als Zeile
    - `.writerows(rowdicts)`: Schreibt mehrere Dictionaries
  - Signatur: `csv.DictWriter(csvfile, fieldnames, **fmtparams)` → `csv.DictWriter`
  - Beispiel:
    ```python
    import csv
    with open('output.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Alter'])
        writer.writeheader()
        writer.writerow({'Name': 'Charlie', 'Alter': 28})
    ```

#### itertools-Funktionen (erweitert)

- **`itertools.tee(iterable, n=2)`** (Funktion, Python 2.4+)
  - Klont Iterator/Iterable in `n` unabhängige Kopien
  - Ermöglicht mehrfache Iteration über denselben Datenstream
  - **Warnung**: Speicher-Overhead, da Werte zwischengespeichert werden
  - Signatur: `itertools.tee(iterable, n=2)` → `tuple` von Iteratoren
  - Beispiel:
    ```python
    import itertools
    
    def lies_daten(datei):
        for zeile in datei:
            yield zeile
    
    daten = lies_daten(open('data.txt'))
    it1, it2, it3 = itertools.tee(daten, 3)
    
    # it1, it2, it3 können unabhängig voneinander durchlaufen werden
    summe = sum(int(x) for x in it1)
    maximum = max(int(x) for x in it2)
    durchschnitt = sum(int(x) for x in it3) / len(list(it3))
    ```

#### Konzepte und Best Practices

- **Generator vs. List Comprehension**:
  - Generator: `(x**2 for x in range(1000000))` → O(1) Speicher
  - List Comprehension: `[x**2 for x in range(1000000)]` → O(n) Speicher
  - Verwende Generator für große Datenmengen oder wenn nicht alle Werte benötigt

- **Generator Exhaustion**:
  - Generatoren können nur einmal durchlaufen werden
  - `list(gen)` konvertiert zu Liste (exhausted danach)
  - Für mehrfache Nutzung: Generator-Funktion erneut aufrufen oder `itertools.tee()` nutzen

- **CSV und newline**:
  - Unter Windows ist `newline=''` beim Öffnen für csv.writer **zwingend**
  - Verhindert doppelte Zeilenumbrüche (`\r\r\n` statt `\r\n`)
  - Bei Lesen optional, bei Schreiben erforderlich

- **DictReader vs. reader**:
  - `csv.reader`: Einfacher, schneller, gibt Listen zurück
  - `csv.DictReader`: Lesbarer, selbstdokumentierend, gibt Dictionaries zurück
  - Bevorzuge DictReader für Übersichtlichkeit, außer Performance kritisch

- **Generator-Pipelines**:
  - Ideal für Datentransformationen (Extract-Transform-Load)
  - Jeder Generator sollte eine klare Verantwortlichkeit haben (Single Responsibility)
  - Beispiel: `validiere → transformiere → aggregiere → exportiere`

### Notizen

- `yield` wurde in Python 2.2 eingeführt (PEP 255), Generator Expressions in Python 2.4 (PEP 289)
- `csv`-Modul ist seit Python 2.3 Teil der Standard-Library
- `next()` Built-in wurde in Python 2.6 hinzugefügt (vorher nur `iterator.next()` Methode)
- `itertools.tee()` wurde in Python 2.4 eingeführt
- Generatoren haben minimalen Overhead: ~136 Bytes Basis + Zustandsspeicher
- `csv.DictReader` gibt seit Python 3.8+ reguläre `dict` zurück (vorher `OrderedDict`)
- Generator Expressions sind syntaktisch identisch zu List Comprehensions, aber mit `()` statt `[]`
- Bei sehr großen CSV-Dateien (GB-Bereich): Chunks mit `pandas.read_csv(chunksize=...)` erwägen

---

## V17 (TBD) – Kryptografie & Netzwerk-Programmierung Teil 1

### Neu eingeführt

#### Module: `socket`

- **`socket`-Modul** (Standard Library, Python 1.x+)
  - Modul für Low-Level Netzwerk-Programmierung mit Sockets
  - Ermöglicht TCP/IP- und UDP-Kommunikation
  - Import: `import socket`

#### Socket-Funktionen und Klassen

- **`socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)`** (Konstruktor)
  - Erstellt ein Socket-Objekt
  - Parameter:
    - `family`: Adressfamilie (Standard: `socket.AF_INET` für IPv4)
    - `type`: Socket-Typ (Standard: `socket.SOCK_STREAM` für TCP)
    - `proto`: Protokoll (Standard: 0, automatische Auswahl)
  - Signatur: `socket.socket(family, type, proto)` → `socket object`
  - Beispiel: `server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - Muss mit `.close()` geschlossen werden oder via `with`-Statement

#### Socket-Konstanten

- **`socket.AF_INET`** (Konstante)
  - Adressfamilie für IPv4
  - Verwendet als `family`-Parameter in `socket.socket()`
  - Beispiel: `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`

- **`socket.AF_INET6`** (Konstante, erwähnt)
  - Adressfamilie für IPv6
  - Beispiel: `socket.socket(socket.AF_INET6, socket.SOCK_STREAM)`

- **`socket.SOCK_STREAM`** (Konstante)
  - Socket-Typ für TCP (verbindungsorientiert, zuverlässig)
  - Verwendet als `type`-Parameter
  - Garantiert Reihenfolge und Zustellung der Pakete

- **`socket.SOCK_DGRAM`** (Konstante, erwähnt)
  - Socket-Typ für UDP (verbindungslos, unzuverlässig)
  - Beispiel: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`

- **`socket.SOL_SOCKET`** (Konstante)
  - Socket-Level für `.setsockopt()`
  - Bezeichnet Socket-Ebene (nicht Protokoll-Ebene)
  - Beispiel: `socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`

- **`socket.SO_REUSEADDR`** (Konstante)
  - Option zum Wiederverwenden von Adressen
  - Verhindert "Address already in use"-Fehler nach Server-Neustart
  - Beispiel: `server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`

#### Server-Socket-Methoden

- **`socket.bind(address)`** (Methode)
  - Bindet Socket an eine Adresse (IP, Port)
  - Nur für Server-Sockets erforderlich
  - Parameter: `address` ist Tupel `(host, port)`
  - Signatur: `socket.bind((host, port))` → `None`
  - Beispiel: `server_socket.bind(("localhost", 8000))`
  - Wirft `OSError` bei bereits belegtem Port

- **`socket.listen(backlog)`** (Methode)
  - Aktiviert Server-Modus und wartet auf eingehende Verbindungen
  - Parameter: `backlog` = Max. Anzahl wartender Verbindungen in Queue
  - Signatur: `socket.listen(backlog)` → `None`
  - Beispiel: `server_socket.listen(5)`
  - Muss nach `.bind()` und vor `.accept()` aufgerufen werden

- **`socket.accept()`** (Methode)
  - Wartet auf eingehende Client-Verbindung (blockierend)
  - Gibt Tupel zurück: `(client_socket, client_address)`
  - Signatur: `socket.accept()` → `(socket object, address info)`
  - Beispiel:
    ```python
    client_socket, client_address = server_socket.accept()
    print(f"Verbunden mit {client_address}")
    ```
  - **Wichtig**: Blockiert, bis Client verbindet (oder Timeout gesetzt)

#### Client-Socket-Methoden

- **`socket.connect(address)`** (Methode)
  - Verbindet zu einem Server (nur Client-Sockets)
  - Parameter: `address` ist Tupel `(host, port)`
  - Signatur: `socket.connect((host, port))` → `None`
  - Beispiel: `client_socket.connect(("localhost", 8000))`
  - Wirft `ConnectionRefusedError` wenn Server nicht erreichbar
  - Wirft `socket.timeout` bei gesetztem Timeout

#### Datenübertragung

- **`socket.send(bytes)`** (Methode)
  - Sendet Daten über Socket
  - Gibt Anzahl **tatsächlich gesendeter** Bytes zurück (kann weniger sein!)
  - Signatur: `socket.send(bytes)` → `int`
  - Beispiel:
    ```python
    nachricht = "Hallo"
    bytes_gesendet = client_socket.send(nachricht.encode("utf-8"))
    ```
  - **Wichtig**: Kann weniger Bytes senden als übergeben (z.B. bei vollem Buffer)

- **`socket.sendall(bytes)`** (Methode)
  - Sendet alle Daten über Socket (wiederholt `.send()` intern)
  - Garantiert Versand aller Bytes (oder Exception)
  - Gibt `None` zurück
  - Signatur: `socket.sendall(bytes)` → `None`
  - Beispiel: `client_socket.sendall("Hallo Server".encode("utf-8"))`
  - **Best Practice**: Bevorzuge `.sendall()` statt `.send()` für vollständigen Versand

- **`socket.recv(bufsize)`** (Methode)
  - Empfängt Daten vom Socket (max. `bufsize` Bytes)
  - Blockiert, bis Daten verfügbar oder Verbindung geschlossen
  - Gibt leeren Byte-String `b''` zurück bei geschlossener Verbindung
  - Signatur: `socket.recv(bufsize)` → `bytes`
  - Beispiel:
    ```python
    daten = client_socket.recv(1024)  # Max. 1024 Bytes
    if daten:
        nachricht = daten.decode("utf-8")
    ```
  - **Wichtig**: Gibt möglicherweise weniger als `bufsize` Bytes zurück
  - **Typischer Wert**: 1024, 4096 oder 8192 Bytes

#### Socket-Verwaltung

- **`socket.close()`** (Methode)
  - Schließt Socket und gibt Ressourcen frei
  - Signatur: `socket.close()` → `None`
  - Beispiel: `client_socket.close()`
  - **Best Practice**: Immer in `finally`-Block oder via `with`-Statement

- **`socket.setsockopt(level, optname, value)`** (Methode)
  - Setzt Socket-Optionen
  - Parameter:
    - `level`: `socket.SOL_SOCKET` (Socket-Ebene)
    - `optname`: Option (z.B. `socket.SO_REUSEADDR`)
    - `value`: Wert (1 für aktivieren, 0 für deaktivieren)
  - Signatur: `socket.setsockopt(level, optname, value)` → `None`
  - Beispiel: `server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
  - **Verwendung**: `SO_REUSEADDR` verhindert "Address already in use" nach Server-Neustart

- **`socket.settimeout(value)`** (Methode)
  - Setzt Timeout für blockierende Operationen
  - Parameter: `value` in Sekunden (float), `None` für unendlich
  - Signatur: `socket.settimeout(value)` → `None`
  - Beispiel: `client_socket.settimeout(5.0)`  # 5 Sekunden Timeout
  - Wirft `socket.timeout` Exception bei Timeout

#### Exceptions

- **`socket.timeout`** (Exception)
  - Wird geworfen bei Timeout während Socket-Operationen
  - Tritt auf bei `.recv()`, `.accept()`, `.connect()` mit gesetztem Timeout
  - Unterklasse von `OSError`
  - Beispiel:
    ```python
    try:
        daten = client_socket.recv(1024)
    except socket.timeout:
        print("Timeout beim Empfang")
    ```

- **`ConnectionRefusedError`** (Built-in Exception, erwähnt)
  - Wird bei `.connect()` geworfen, wenn Server nicht erreichbar
  - Beispiel: `client_socket.connect(("localhost", 9999))`  # Port nicht offen

- **`OSError`** (erwähnt im Kontext von Sockets)
  - Basis-Exception für Socket-Fehler (z.B. "Address already in use")
  - Viele Socket-Exceptions sind Unterklassen von `OSError`

#### Module: `hashlib`

- **`hashlib`-Modul** (Standard Library, Python 2.5+)
  - Modul für kryptografische Hash-Funktionen
  - Import: `import hashlib`
  - Unterstützt SHA-1, SHA-256, SHA-512, MD5, etc.

- **`hashlib.sha256(data=b'')`** (Konstruktor)
  - Erstellt SHA-256 Hash-Objekt
  - Parameter: `data` optional (Byte-String zum initialen Hashen)
  - Signatur: `hashlib.sha256(data)` → `hash object`
  - Beispiel:
    ```python
    hash_object = hashlib.sha256("Hallo".encode("utf-8"))
    hash_hex = hash_object.hexdigest()
    ```
  - **Wichtig**: Input muss Byte-String sein (`.encode()` verwenden)

- **`hash_object.hexdigest()`** (Methode)
  - Gibt Hash als Hexadezimal-String zurück
  - Signatur: `hash.hexdigest()` → `str`
  - Beispiel: `hash_object.hexdigest()` → `"3a7bd..."`
  - **Verwendung**: Für Menschen-lesbare Hash-Repräsentation

- **`hash_object.digest()`** (Methode, erwähnt)
  - Gibt Hash als Byte-String zurück
  - Signatur: `hash.digest()` → `bytes`
  - Beispiel: `hash_object.digest()` → `b'\x3a\x7b...'`
  - **Verwendung**: Für binäre Weiterverarbeitung

#### Konzepte und Sprachmerkmale

- **TCP/IP Client-Server-Architektur**
  - **Server**: Bindet an Port, hört auf Verbindungen, akzeptiert Clients
  - **Client**: Verbindet zu Server-IP/Port
  - Ablauf:
    1. Server: `socket()` → `.bind()` → `.listen()` → `.accept()` (wartet)
    2. Client: `socket()` → `.connect()` (verbindet)
    3. Server: `.accept()` gibt Client-Socket zurück
    4. Beide: `.send()` / `.recv()` für Datenaustausch
    5. Beide: `.close()` zum Beenden

- **Byte Encoding/Decoding**
  - Sockets übertragen **nur Bytes**, keine Strings
  - **Encoding**: String → Bytes mit `.encode("utf-8")`
  - **Decoding**: Bytes → String mit `.decode("utf-8")`
  - Beispiel:
    ```python
    # Senden:
    socket.sendall("Hallo".encode("utf-8"))
    
    # Empfangen:
    daten = socket.recv(1024)
    text = daten.decode("utf-8")
    ```
  - **Standard-Encoding**: UTF-8 (unterstützt alle Unicode-Zeichen)

- **Multi-Client-Server**
  - Einfacher Server kann nur einen Client gleichzeitig bedienen
  - **Lösungen**:
    - **Sequenziell**: `.accept()` in Schleife (ein Client nach dem anderen)
    - **Threading**: Jeder Client bekommt eigenen Thread (wird in V17 verwendet)
    - **Asynchron**: `asyncio` (wird in späteren Vorlesungen behandelt)
  - Beispiel (sequenziell):
    ```python
    while True:
        client_socket, _ = server_socket.accept()
        # Bearbeite Client
        client_socket.close()
    ```

- **HMAC-ähnliche Authentifizierung**
  - **Konzept**: Nachricht + Secret Key → Hash
  - **Verwendung**: Integrität und Authentizität sicherstellen
  - **Ablauf**:
    1. Client berechnet Hash aus Daten + Secret Key
    2. Client sendet Daten + Hash
    3. Server berechnet erwarteten Hash aus empfangenen Daten + Secret Key
    4. Server vergleicht: Empfangener Hash == Erwarteter Hash?
  - **Sicherheit**: Ohne Secret Key kann Hash nicht gefälscht werden
  - Beispiel:
    ```python
    data_string = f"{befehl}|{maschine_id}|{SECRET_KEY}"
    hash_value = hashlib.sha256(data_string.encode()).hexdigest()
    ```

### Konzepte und Best Practices

- **`.sendall()` bevorzugen**: Garantiert vollständigen Versand, `.send()` kann partiell senden
- **SO_REUSEADDR für Server**: Verhindert "Address already in use" nach Neustart
- **Immer `.close()` aufrufen**: Sockets sind Systemressourcen, müssen freigegeben werden
- **Timeouts setzen**: Verhindert unendliches Warten (z.B. bei nicht-reagierendem Client)
- **UTF-8 für Encoding**: Standard für Textübertragung, unterstützt alle Unicode-Zeichen
- **JSON für strukturierte Daten**: Besser als eigenes Protokoll (siehe P2-P5 in V17)
- **Leere Bytes `b''` bedeuten geschlossene Verbindung**: Prüfung mit `if not daten:`
- **Buffer-Größe 1024/4096**: Übliche Werte für `.recv()`, abhängig von Nachrichtengröße

### Notizen

- `socket`-Modul existiert seit Python 1.x (sehr alt, grundlegend)
- `hashlib` wurde in Python 2.5 eingeführt (ersetzt altes `md5`/`sha` Module)
- Socket-Programmierung ist plattformübergreifend (Windows, Linux, macOS)
- Für echte HMAC-Authentifizierung: `hmac`-Modul verwenden (standardisierter)
- `socket` ist Low-Level; für HTTP: `requests`, `urllib`, `http.server` bevorzugen
- TCP garantiert Reihenfolge und Zustellung, UDP nicht (UDP ist schneller)
- `.recv()` kann weniger Bytes zurückgeben als angefordert (bei großen Daten mehrfach aufrufen)
- Für produktive Server: Frameworks wie Flask, FastAPI statt raw Sockets
- SHA-256 ist kryptografisch sicher (Kollisionsresistenz, One-Way)
- Mit-Statement für Sockets: `with socket.socket() as s:` automatisches `.close()`

---

## V18 (2026-01-05) – Kryptografie Teil 2 & Netzwerk-Programmierung Teil 2

### Neu eingeführt

#### `hashlib`-Modul (Ergänzung zu V17)

- **`hashlib.sha256()`** (bereits in V17 erwähnt, hier vollständig eingeführt)
  - Erstellt SHA-256-Hash-Objekt
  - Signatur: `hashlib.sha256([data])` → Hash-Objekt
  - Verwendung: Hash-Objekt mit `.update(data)` füttern, `.hexdigest()` für finalen Hash

- **Hash-Objekt-Methoden**:
  - **`.update(data)`**: Fügt Daten zum Hash hinzu (für blockweises Hashen großer Dateien)
  - **`.hexdigest()`**: Gibt Hash als Hexadezimal-String zurück
  - **`.digest()`**: Gibt Hash als Bytes zurück

#### `requests`-Bibliothek (Drittanbieter-Bibliothek)

- **Installation**: `pip install requests`
- **Import**: `import requests`

**HTTP-Request-Methoden**:

- **`requests.get(url, params=None, headers=None, timeout=None, verify=True)`**
  - Sendet HTTP-GET-Request
  - Signatur: `requests.get(url, **kwargs)` → `Response`
  - Beispiel: `response = requests.get("https://api.example.com", params={"key": "value"}, timeout=5)`

- **`requests.post(url, data=None, json=None, headers=None, timeout=None, verify=True)`**
  - Sendet HTTP-POST-Request mit Daten im Body
  - `json=`-Parameter für JSON-Daten (automatische Serialisierung)
  - Signatur: `requests.post(url, **kwargs)` → `Response`
  - Beispiel: `response = requests.post("https://api.example.com", json={"sensor": "temp_01", "value": 75.3}, timeout=5)`

- **`requests.put(url, data=None, json=None, headers=None, timeout=None)`**
  - Sendet HTTP-PUT-Request (Ressource ersetzen)
  - Signatur: `requests.put(url, **kwargs)` → `Response`

- **`requests.patch(url, data=None, json=None, headers=None, timeout=None)`**
  - Sendet HTTP-PATCH-Request (Ressource teilweise aktualisieren)
  - Signatur: `requests.patch(url, **kwargs)` → `Response`

- **`requests.delete(url, headers=None, timeout=None)`**
  - Sendet HTTP-DELETE-Request (Ressource löschen)
  - Signatur: `requests.delete(url, **kwargs)` → `Response`

- **`requests.head(url, headers=None, timeout=None)`**
  - Sendet HTTP-HEAD-Request (nur Header abrufen, kein Body)
  - Signatur: `requests.head(url, **kwargs)` → `Response`

**Response-Objekt-Attribute und -Methoden**:

- **`response.status_code`** (Attribut)
  - HTTP-Status-Code als Integer (z.B. 200, 404, 500)
  - Typ: `int`

- **`response.text`** (Attribut)
  - Response-Body als String (automatische Dekodierung)
  - Typ: `str`

- **`response.content`** (Attribut)
  - Response-Body als Bytes (für binäre Daten wie Bilder, PDFs)
  - Typ: `bytes`

- **`response.json()`** (Methode)
  - Parst Response-Body als JSON und gibt Python-Dictionary/Liste zurück
  - Wirft `JSONDecodeError` bei ungültigem JSON
  - Signatur: `response.json()` → `dict | list`

- **`response.headers`** (Attribut)
  - Response-Header als Dictionary-ähnliches Objekt (case-insensitive)
  - Typ: `CaseInsensitiveDict`

- **`response.url`** (Attribut)
  - Finale URL nach Redirects
  - Typ: `str`

- **`response.ok`** (Attribut)
  - Boolean, `True` wenn Status-Code 200-399, sonst `False`
  - Typ: `bool`

- **`response.raise_for_status()`** (Methode)
  - Wirft `HTTPError`-Exception bei Status-Codes 4xx oder 5xx
  - Keine Aktion bei 2xx/3xx
  - Signatur: `response.raise_for_status()` → `None`

- **`response.elapsed`** (Attribut)
  - Dauer der Request als `timedelta`-Objekt
  - Typ: `datetime.timedelta`

- **`response.encoding`** (Attribut)
  - Zeichenkodierung der Response (z.B. `"utf-8"`)
  - Kann gesetzt werden, um Dekodierung zu beeinflussen
  - Typ: `str`

**Exception-Typen (requests.exceptions)**:

- **`requests.exceptions.Timeout`**
  - Exception bei Timeout (Connection- oder Read-Timeout überschritten)

- **`requests.exceptions.ConnectionError`**
  - Exception bei Verbindungsfehlern (z.B. keine Netzwerkverbindung, DNS-Fehler)

- **`requests.exceptions.HTTPError`**
  - Exception bei 4xx/5xx Status-Codes (nur wenn `.raise_for_status()` aufgerufen wurde)

- **`requests.exceptions.TooManyRedirects`**
  - Exception bei zu vielen Redirects (Standard-Limit: 30)

- **`requests.exceptions.RequestException`**
  - Basis-Exception für alle `requests`-Fehler (kann als Catch-All verwendet werden)

- **`requests.exceptions.JSONDecodeError`**
  - Exception bei ungültigem JSON in `.json()` (erbt von `json.JSONDecodeError`)

#### `bcrypt`-Bibliothek (Drittanbieter-Bibliothek, für Passwort-Hashing)

- **Installation**: `pip install bcrypt`
- **Import**: `import bcrypt`

- **`bcrypt.hashpw(password, salt)`**
  - Erstellt bcrypt-Hash für Passwort
  - `password` muss als Bytes vorliegen (`.encode("utf-8")`)
  - `salt` wird mit `bcrypt.gensalt()` generiert
  - Signatur: `bcrypt.hashpw(password: bytes, salt: bytes)` → `bytes`
  - Beispiel: `hashed = bcrypt.hashpw("Passwort123".encode("utf-8"), bcrypt.gensalt())`

- **`bcrypt.gensalt(rounds=12)`**
  - Generiert neuen zufälligen Salt
  - `rounds` bestimmt Rechenaufwand (höher = langsamer = sicherer, Standard: 12)
  - Signatur: `bcrypt.gensalt(rounds=12)` → `bytes`

- **`bcrypt.checkpw(password, hashed)`**
  - Prüft, ob Passwort mit Hash übereinstimmt
  - Beide Argumente müssen Bytes sein
  - Signatur: `bcrypt.checkpw(password: bytes, hashed: bytes)` → `bool`
  - Beispiel: `if bcrypt.checkpw("Passwort123".encode("utf-8"), hashed): print("Korrekt")`

#### `os.environ`-Zugriff (Standard Library, für Umgebungsvariablen)

- **`os.environ.get(key, default=None)`**
  - Liest Umgebungsvariable
  - Gibt `default` zurück, wenn Variable nicht existiert
  - Signatur: `os.environ.get(key, default=None)` → `str | None`
  - Beispiel: `api_key = os.environ.get("API_KEY", "default_key")`

### Konzepte und Sprachmerkmale

- **HTTP-Protokoll**: Request-Response-Modell, Methoden (GET, POST, PUT, DELETE), Status-Codes (2xx Erfolg, 4xx Client-Fehler, 5xx Server-Fehler)
- **REST-APIs**: Representational State Transfer, standardisiertes API-Design mit HTTP-Methoden und JSON
- **JSON-Verarbeitung**: `.json()` konvertiert Response automatisch zu Python-Dictionary/Liste
- **Timeout**: Immer Timeout setzen bei `requests` (z.B. `timeout=5`), sonst kann Request unendlich warten
- **Status-Code-Prüfung**: `.raise_for_status()` wirft Exception bei 4xx/5xx, oder manuelle Prüfung mit `.status_code`
- **Error Handling**: `Timeout`, `ConnectionError`, `HTTPError`, `JSONDecodeError` abfangen
- **Header**: Metadaten wie `User-Agent`, `Accept`, `Authorization`, `Content-Type`
- **Query-Parameter**: `params={"key": "value"}` erzeugt URL mit `?key=value`
- **POST mit JSON**: `json=`-Parameter für automatische JSON-Serialisierung + `Content-Type: application/json`
- **Pagination**: Große Datensätze in Seiten abrufen (Loop über `page`-Parameter)
- **Umgebungsvariablen**: API-Keys nie im Code hardcoden, sondern aus `os.environ` lesen
- **TLS-Zertifikate**: `verify=True` (Standard) prüft Zertifikate, `verify=False` deaktiviert (nur für Entwicklung!)

### Best Practices

- **Immer Timeout setzen**: `requests.get(url, timeout=5)` verhindert hängende Requests
- **Status-Codes prüfen**: `.raise_for_status()` oder manuell `.status_code` prüfen
- **JSONDecodeError abfangen**: `.json()` kann fehlschlagen bei ungültigem JSON
- **API-Keys aus Umgebung**: `os.environ.get("API_KEY")` statt Hardcoding
- **TLS verifizieren**: `verify=True` in Produktion, niemals deaktivieren
- **User-Agent setzen**: Manche APIs blocken Requests ohne User-Agent
- **`json=`-Parameter für POST**: Automatische Serialisierung + Content-Type-Header

### Notizen

- `requests` ist nicht Teil der Standard Library (Drittanbieter-Bibliothek)
- `bcrypt` ist nicht Teil der Standard Library (Drittanbieter-Bibliothek)
- `hashlib` ist Teil der Standard Library seit Python 2.5
- `requests` ist der de-facto Standard für HTTP in Python (Kenneth Reitz, 2011)
- `bcrypt` implementiert den Blowfish-basierten Passwort-Hashing-Algorithmus
- SHA-256 alleine ist zu schnell für Passwort-Hashing (bcrypt ist absichtlich langsam)
- HTTP ist zustandslos (jede Request ist unabhängig)
- HTTPS = HTTP über TLS (Port 443 statt Port 80)
- Status-Codes: 2xx Erfolg, 3xx Redirect, 4xx Client-Fehler, 5xx Server-Fehler
- GET ist idempotent und safe, POST ist weder idempotent noch safe
- JSON ist leichtgewichtiger als XML (modernes Standard-Datenformat für APIs)
- Forward Secrecy (TLS 1.2+): Vergangene Verbindungen bleiben auch bei kompromittiertem Server-Key sicher
- PKI: Certificate Authorities (CAs) bilden Vertrauenskette für TLS-Zertifikate

---

## V19 (2026-01-04) – Datenbanken – Teil 1 / Datenbankverbindung & SQL – Teil 1

### Neu eingeführt

#### Module: `sqlite3`

- **`sqlite3`-Modul** (Standard Library, Python 2.5+)
  - Modul für SQLite-Datenbankverwaltung (serverlose, dateibasierte SQL-Datenbank)
  - Implementiert DB-API 2.0 (PEP 249)
  - Import: `import sqlite3`
  - **SQLite-Version**: In Python integriert (keine separate Installation)

#### Datenbankverbindung

- **`sqlite3.connect(database, timeout=5.0, isolation_level='DEFERRED', **kwargs)`** (Funktion)
  - Erstellt Verbindung zu SQLite-Datenbank (erzeugt Datei, falls nicht vorhanden)
  - Parameter:
    - `database`: Dateiname (z.B. `'maschinen.db'`) oder `':memory:'` für In-Memory-DB
    - `timeout`: Wartezeit in Sekunden bei Locked Database
    - `isolation_level`: Transaktionsverhalten (`'DEFERRED'`, `'IMMEDIATE'`, `'EXCLUSIVE'`, `None` für Autocommit)
  - Signatur: `sqlite3.connect(database, **kwargs)` → `Connection`
  - Beispiel: `conn = sqlite3.connect('produktionsdb.db')`
  - **Wichtig**: Connection muss mit `.close()` geschlossen werden oder via `with`-Statement

#### Connection-Methoden

- **`connection.cursor()`** (Methode)
  - Erstellt Cursor-Objekt für SQL-Ausführung
  - Signatur: `connection.cursor()` → `Cursor`
  - Beispiel: `cursor = conn.cursor()`
  - **Wichtig**: Ein Cursor ist notwendig für alle SQL-Operationen

- **`connection.commit()`** (Methode)
  - Speichert (committed) alle Änderungen seit letztem Commit
  - Signatur: `connection.commit()` → `None`
  - Beispiel: `conn.commit()`
  - **Nur nötig bei**: INSERT, UPDATE, DELETE (nicht bei SELECT)

- **`connection.rollback()`** (Methode)
  - Macht alle Änderungen seit letztem Commit rückgängig
  - Signatur: `connection.rollback()` → `None`
  - Beispiel: `conn.rollback()`
  - **Verwendung**: Bei Fehlern in Transaktionen

- **`connection.close()`** (Methode)
  - Schließt Datenbankverbindung und gibt Ressourcen frei
  - Signatur: `connection.close()` → `None`
  - Beispiel: `conn.close()`
  - **Best Practice**: Immer in `finally`-Block oder via `with`-Statement

- **`connection.row_factory`** (Attribut)
  - Bestimmt, wie Zeilen von `fetchall()` zurückgegeben werden
  - Standard: `None` (Tupel)
  - Mit `sqlite3.Row`: Dictionary-ähnlicher Zugriff nach Spaltennamen
  - Signatur: `connection.row_factory = sqlite3.Row`
  - Beispiel:
    ```python
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT Name, Alter FROM Mitarbeiter')
    row = cursor.fetchone()
    print(row['Name'])  # Zugriff nach Spaltenname
    ```

#### Cursor-Methoden

- **`cursor.execute(sql, parameters=())`** (Methode)
  - Führt einzelne SQL-Anweisung aus
  - Parameter werden mit `?` Platzhaltern übergeben (Prepared Statement)
  - Signatur: `cursor.execute(sql, parameters)` → `Cursor`
  - Beispiel:
    ```python
    cursor.execute('INSERT INTO Maschinen (Name, Baujahr) VALUES (?, ?)', ('CNC-01', 2020))
    cursor.execute('SELECT * FROM Maschinen WHERE Baujahr > ?', (2015,))
    ```
  - **Wichtig**: NIEMALS String-Formatierung für SQL verwenden (SQL-Injection!)

- **`cursor.executemany(sql, seq_of_parameters)`** (Methode)
  - Führt SQL-Anweisung für jede Zeile in Sequenz aus (Batch-Insert)
  - Signatur: `cursor.executemany(sql, seq_of_parameters)` → `Cursor`
  - Beispiel:
    ```python
    daten = [('CNC-01', 2020), ('Drehbank-02', 2018), ('Fräse-03', 2022)]
    cursor.executemany('INSERT INTO Maschinen (Name, Baujahr) VALUES (?, ?)', daten)
    ```
  - **Performance**: Deutlich schneller als einzelne `.execute()` in Schleife

- **`cursor.fetchall()`** (Methode)
  - Gibt alle Zeilen des Result Sets als Liste zurück
  - Signatur: `cursor.fetchall()` → `list` (von Tupeln oder `sqlite3.Row`)
  - Beispiel:
    ```python
    cursor.execute('SELECT * FROM Maschinen')
    zeilen = cursor.fetchall()
    for zeile in zeilen:
        print(zeile)
    ```
  - **Warnung**: Lädt alle Zeilen in Speicher (bei großen Result Sets: `.fetchmany()` oder Iteration)

- **`cursor.fetchone()`** (Methode)
  - Gibt nächste Zeile des Result Sets zurück oder `None` bei Ende
  - Signatur: `cursor.fetchone()` → `tuple` / `sqlite3.Row` / `None`
  - Beispiel:
    ```python
    cursor.execute('SELECT * FROM Maschinen WHERE ID = ?', (5,))
    zeile = cursor.fetchone()
    if zeile:
        print(zeile)
    ```

- **`cursor.fetchmany(size=cursor.arraysize)`** (Methode)
  - Gibt bis zu `size` Zeilen des Result Sets zurück
  - Signatur: `cursor.fetchmany(size)` → `list`
  - Beispiel:
    ```python
    cursor.execute('SELECT * FROM Messdaten')
    while True:
        zeilen = cursor.fetchmany(1000)
        if not zeilen:
            break
        verarbeite(zeilen)
    ```
  - **Verwendung**: Memory-effiziente Verarbeitung großer Result Sets

- **`cursor.close()`** (Methode)
  - Schließt Cursor und gibt Ressourcen frei
  - Signatur: `cursor.close()` → `None`
  - Beispiel: `cursor.close()`

#### Exception-Typen (sqlite3)

- **`sqlite3.Error`** (Exception)
  - Basis-Exception für alle sqlite3-Fehler
  - Beispiel:
    ```python
    try:
        cursor.execute('SELECT * FROM NichtVorhandenTabelle')
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
    ```

- **`sqlite3.IntegrityError`** (Exception)
  - Wird geworfen bei Verletzung von Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK)
  - Unterklasse von `sqlite3.Error`
  - Beispiel:
    ```python
    try:
        cursor.execute('INSERT INTO Maschinen (ID, Name) VALUES (1, "CNC")')
        cursor.execute('INSERT INTO Maschinen (ID, Name) VALUES (1, "Drehbank")')  # Duplikat!
    except sqlite3.IntegrityError:
        print("Constraint-Verletzung: ID bereits vorhanden")
    ```

- **`sqlite3.OperationalError`** (Exception)
  - Wird geworfen bei operationalen Fehlern (Tabelle existiert nicht, Syntax-Fehler, Locked Database)
  - Unterklasse von `sqlite3.Error`
  - Beispiel:
    ```python
    try:
        cursor.execute('SELECT * FROM NichtVorhandenTabelle')
    except sqlite3.OperationalError as e:
        print(f"SQL-Fehler: {e}")
    ```

#### Konzepte und Sprachmerkmale

- **Prepared Statements mit `?` Platzhaltern**
  - **Syntax**: `cursor.execute('SELECT * FROM Tabelle WHERE Spalte = ?', (wert,))`
  - **Vorteile**:
    - Verhindert SQL-Injection (automatisches Escaping)
    - Performance-Vorteil bei wiederholter Ausführung (Query Plan Caching)
  - **NIEMALS**: String-Formatierung verwenden (`f"SELECT * FROM Tabelle WHERE Spalte = '{wert}'"` ist unsicher!)
  - Beispiel:
    ```python
    # FALSCH (SQL-Injection!):
    name = input("Name: ")
    cursor.execute(f"SELECT * FROM Maschinen WHERE Name = '{name}'")
    
    # RICHTIG:
    cursor.execute('SELECT * FROM Maschinen WHERE Name = ?', (name,))
    ```

- **Transaktionen mit BEGIN/COMMIT/ROLLBACK**
  - **BEGIN**: Startet Transaktion (implizit bei erstem INSERT/UPDATE/DELETE)
  - **COMMIT**: Speichert Änderungen dauerhaft (`.commit()`)
  - **ROLLBACK**: Macht Änderungen rückgängig (`.rollback()`)
  - **ACID-Eigenschaften**:
    - **Atomicity** (Atomarität): Alles oder nichts
    - **Consistency** (Konsistenz): Nur gültige Zustände
    - **Isolation** (Isolierung): Transaktionen beeinflussen sich nicht
    - **Durability** (Dauerhaftigkeit): Committed Daten überleben Crash
  - Beispiel:
    ```python
    try:
        cursor.execute('UPDATE Lagerbestand SET Menge = Menge - 10 WHERE ID = 5')
        cursor.execute('INSERT INTO Buchungen (Artikel_ID, Menge) VALUES (5, -10)')
        conn.commit()  # Beide Operationen erfolgreich
    except sqlite3.Error:
        conn.rollback()  # Bei Fehler: Beide zurückrollen
    ```

- **Context Manager (`with`-Statement für Connections)**
  - **Syntax**: `with sqlite3.connect('db.db') as conn:`
  - **Vorteil**: Automatisches `.commit()` bei Erfolg und `.close()` am Ende
  - **Bei Exception**: Automatisches `.rollback()`
  - Beispiel:
    ```python
    with sqlite3.connect('maschinen.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Maschinen (Name) VALUES (?)', ('CNC-07',))
        # Kein manuelles conn.commit() nötig
    # Connection wird automatisch geschlossen
    ```

- **`sqlite3.Row` für Dictionary-ähnlichen Zugriff**
  - Ermöglicht Zugriff nach Spaltennamen statt Index
  - **Setup**: `conn.row_factory = sqlite3.Row`
  - Beispiel:
    ```python
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT Name, Alter FROM Mitarbeiter')
    row = cursor.fetchone()
    print(row['Name'])  # Statt row[0]
    print(dict(row))    # Konvertierung zu echtem Dictionary
    ```

#### SQL-Statements (DDL, DML, DQL)

- **CREATE TABLE** (SQL DDL – Data Definition Language)
  - Erstellt neue Tabelle mit Spalten und Constraints
  - Syntax:
    ```sql
    CREATE TABLE IF NOT EXISTS Tabellenname (
        Spalte1 TYP CONSTRAINTS,
        Spalte2 TYP CONSTRAINTS,
        ...,
        PRIMARY KEY (Spalte1),
        FOREIGN KEY (Spalte2) REFERENCES AndereTabelle(Spalte)
    );
    ```
  - **Datentypen**: `INTEGER`, `REAL`, `TEXT`, `BLOB` (SQLite hat nur diese 4 + `NULL`)
  - **Constraints**:
    - `PRIMARY KEY`: Primärschlüssel (eindeutig, NOT NULL)
    - `AUTOINCREMENT`: Auto-inkrementierende Integer-ID
    - `NOT NULL`: Wert muss angegeben werden
    - `UNIQUE`: Wert muss eindeutig sein
    - `CHECK (bedingung)`: Validierungsbedingung
    - `DEFAULT wert`: Standardwert bei fehlendem Wert
    - `FOREIGN KEY`: Fremdschlüssel-Beziehung
  - Beispiel:
    ```python
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Maschinen (
            Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Typ TEXT NOT NULL,
            Baujahr INTEGER CHECK (Baujahr >= 1900),
            Aktiv INTEGER DEFAULT 1
        )
    ''')
    ```

- **INSERT** (SQL DML – Data Manipulation Language)
  - Fügt neue Zeile(n) in Tabelle ein
  - Syntax: `INSERT INTO Tabelle (Spalte1, Spalte2) VALUES (?, ?)`
  - Beispiel:
    ```python
    cursor.execute('INSERT INTO Maschinen (Name, Typ, Baujahr) VALUES (?, ?, ?)', ('CNC-01', 'Fräse', 2020))
    ```

- **SELECT** (SQL DQL – Data Query Language)
  - Ruft Daten aus Tabelle(n) ab
  - **Basis-Syntax**: `SELECT Spalte1, Spalte2 FROM Tabelle WHERE Bedingung`
  - **Klauseln**:
    - `WHERE`: Filtert Zeilen nach Bedingung
    - `ORDER BY Spalte ASC/DESC`: Sortiert Ergebnisse
    - `LIMIT n`: Begrenzt Anzahl Ergebnisse
    - `GROUP BY Spalte`: Gruppiert für Aggregationen
    - `HAVING Bedingung`: Filtert Gruppen (nach GROUP BY)
  - Beispiel:
    ```python
    cursor.execute('SELECT Name, Baujahr FROM Maschinen WHERE Baujahr > ? ORDER BY Baujahr DESC', (2015,))
    ```

- **UPDATE** (SQL DML)
  - Ändert existierende Zeilen
  - Syntax: `UPDATE Tabelle SET Spalte = ? WHERE Bedingung`
  - Beispiel:
    ```python
    cursor.execute('UPDATE Maschinen SET Aktiv = 0 WHERE Maschinen_ID = ?', (5,))
    ```

- **DELETE** (SQL DML)
  - Löscht Zeilen aus Tabelle
  - Syntax: `DELETE FROM Tabelle WHERE Bedingung`
  - Beispiel:
    ```python
    cursor.execute('DELETE FROM Maschinen WHERE Aktiv = 0')
    ```

- **JOINs** (SQL DQL)
  - Verknüpft Daten aus mehreren Tabellen
  - **INNER JOIN**: Nur Zeilen mit Übereinstimmung in beiden Tabellen
  - **LEFT JOIN**: Alle Zeilen aus linker Tabelle + Übereinstimmungen aus rechter
  - Syntax:
    ```sql
    SELECT m.Name, w.Datum, w.Beschreibung
    FROM Maschinen m
    INNER JOIN Wartungen w ON m.Maschinen_ID = w.Maschinen_ID
    WHERE m.Typ = 'Fräse'
    ```

- **GROUP BY + HAVING** (SQL DQL – Aggregation)
  - `GROUP BY`: Gruppiert Zeilen für Aggregat-Funktionen
  - `HAVING`: Filtert Gruppen (ähnlich zu WHERE, aber nach Gruppierung)
  - **Aggregat-Funktionen**: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT Typ, COUNT(*) AS Anzahl, AVG(Baujahr) AS Durchschnitt_Baujahr
        FROM Maschinen
        GROUP BY Typ
        HAVING COUNT(*) > 2
        ORDER BY Anzahl DESC
    ''')
    ```

- **Subqueries (Unterabfragen)** (SQL DQL)
  - Query innerhalb einer Query
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT Name FROM Maschinen
        WHERE Baujahr > (SELECT AVG(Baujahr) FROM Maschinen)
    ''')
    ```

- **Indexes** (Performance-Optimierung)
  - Erstellt Index für schnellere Abfragen
  - Syntax: `CREATE INDEX index_name ON Tabelle(Spalte)`
  - Beispiel:
    ```python
    cursor.execute('CREATE INDEX idx_maschinen_typ ON Maschinen(Typ)')
    ```
  - **Trade-off**: Schnellere SELECTs vs. langsamere INSERTs/UPDATEs

### Konzepte und Best Practices

- **Immer Prepared Statements verwenden**: `?` Platzhalter statt String-Formatierung (verhindert SQL-Injection)
- **Transaktionen für kritische Operationen**: `.commit()` bei Erfolg, `.rollback()` bei Fehler
- **`with`-Statement für Connections**: Automatisches Cleanup und Rollback bei Exceptions
- **`row_factory = sqlite3.Row`**: Macht Code lesbarer (Zugriff nach Spaltennamen)
- **Constraints in Schema definieren**: NOT NULL, UNIQUE, CHECK statt Python-Validierung
- **`.executemany()` für Batch-Inserts**: Deutlich schneller als Schleife mit `.execute()`
- **`.fetchmany()` für große Result Sets**: Verhindert Speicherprobleme
- **Indexes sparsam verwenden**: Nur auf häufig gefilterte Spalten (WHERE, JOIN)

### Notizen

- `sqlite3` ist seit Python 2.5 Teil der Standard Library
- SQLite ist serverlos (Datenbank = einzelne Datei auf Festplatte)
- SQLite eignet sich für: Embedded Systems, Desktop-Anwendungen, kleine bis mittlere Webanwendungen
- SQLite ist NICHT geeignet für: Hochfrequente Writes von vielen Clients, sehr große Datenmengen (>100 GB)
- `:memory:` als Datenbanknamen erstellt In-Memory-DB (verloren nach Programm-Ende)
- Foreign Key Constraints sind standardmäßig DEAKTIVIERT in SQLite (aktivieren mit `PRAGMA foreign_keys = ON;`)
- SQLite hat keine echten Datentypen: INTEGER, REAL, TEXT, BLOB sind "Type Affinities" (flexibler als echte Typen)
- `AUTOINCREMENT` sollte nur bei PRIMARY KEY INTEGER verwendet werden (hat Performance-Overhead)
- Alternativen zu SQLite: PostgreSQL, MySQL, MariaDB (für größere Anwendungen)

---
## V20 (2026-01-04) – Datenbanken – Teil 2 / Datenbankverbindung & SQL – Teil 2

### Neu eingeführt

#### sqlite3-Modul (Erweitert)

- **Named Placeholders** (`:name`-Syntax für Prepared Statements)
  - Alternative zu `?` Platzhaltern mit benannten Parametern
  - Syntax: `:parametername` im SQL-String, Dictionary als Parameter
  - Signatur: `cursor.execute(sql, {"name": wert})` → `Cursor`
  - Beispiel:
    ```python
    cursor.execute('''
        UPDATE Maschinen 
        SET Status = :status 
        WHERE Name = :name
    ''', {"status": "Wartung", "name": "CNC-01"})
    ```
  - **Vorteil**: Bessere Lesbarkeit bei vielen Parametern, Reihenfolge egal

- **`cursor.rowcount`** (Attribut)
  - Gibt Anzahl betroffener Zeilen der letzten Operation zurück
  - Typ: `int`
  - Bei SELECT: -1 (nicht verfügbar), bei INSERT/UPDATE/DELETE: Anzahl geänderter Zeilen
  - Beispiel:
    ```python
    cursor.execute('UPDATE Maschinen SET Status = ? WHERE Baujahr < ?', ('Außer Betrieb', 2010))
    print(f"{cursor.rowcount} Maschinen aktualisiert")
    ```

- **`cursor.description`** (Attribut)
  - Gibt Spaltenbeschreibung des Result Sets zurück
  - Typ: `tuple` von 7-Tupeln `(name, type_code, display_size, internal_size, precision, scale, null_ok)`
  - Meistens nur `name` (Index 0) relevant
  - Beispiel:
    ```python
    cursor.execute('SELECT Name, Typ, Baujahr FROM Maschinen LIMIT 1')
    spaltennamen = [desc[0] for desc in cursor.description]
    # ['Name', 'Typ', 'Baujahr']
    ```

#### SQL-Statements (Erweitert)

- **UPDATE mit SET WHERE** (SQL DML, erweitert)
  - Mehrere Spalten gleichzeitig aktualisieren
  - Bedingte Updates mit komplexen WHERE-Klauseln
  - Beispiel:
    ```python
    cursor.execute('''
        UPDATE Wartungen 
        SET Kosten = Kosten * 1.10, 
            Typ = 'Reparatur' 
        WHERE Maschinen_ID = ? AND Datum < ?
    ''', (maschine_id, stichtag))
    ```

- **DELETE mit CASCADE** (SQL DML, erweitert)
  - Automatisches Löschen abhängiger Zeilen in anderen Tabellen
  - Erfordert `PRAGMA foreign_keys = ON;` in SQLite
  - Schema-Definition mit `ON DELETE CASCADE`:
    ```python
    cursor.execute('''
        CREATE TABLE Wartungen (
            Wartungs_ID INTEGER PRIMARY KEY,
            Maschinen_ID INTEGER,
            FOREIGN KEY (Maschinen_ID) 
                REFERENCES Maschinen(Maschinen_ID) 
                ON DELETE CASCADE
        )
    ''')
    ```
  - Beispiel:
    ```python
    # Aktiviert Foreign Key Constraints
    cursor.execute('PRAGMA foreign_keys = ON')
    
    # Löscht Maschine + automatisch alle zugehörigen Wartungen
    cursor.execute('DELETE FROM Maschinen WHERE Maschinen_ID = ?', (5,))
    ```

- **Transaktionen mit SAVEPOINT/ROLLBACK TO** (SQL Transaktionskontrolle)
  - Zwischenpunkte innerhalb einer Transaktion setzen
  - Ermöglicht partielles Rollback (nicht alles zurückrollen)
  - Beispiel:
    ```python
    cursor.execute('BEGIN')
    cursor.execute('UPDATE Konto SET Betrag = Betrag - 100 WHERE ID = 1')
    
    cursor.execute('SAVEPOINT nach_abbuchung')
    
    try:
        cursor.execute('UPDATE Konto SET Betrag = Betrag + 100 WHERE ID = 2')
        # Fehler tritt auf...
        raise ValueError("Empfängerkonto gesperrt")
    except ValueError:
        cursor.execute('ROLLBACK TO nach_abbuchung')  # Nur zweites UPDATE zurück
    
    conn.commit()  # Erste Abbuchung bleibt
    ```

#### Aggregationen mit GROUP BY und HAVING

- **GROUP BY mit mehreren Spalten**
  - Gruppierung nach kombinierten Werten
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT Typ, Baujahr, COUNT(*) AS Anzahl
        FROM Maschinen
        GROUP BY Typ, Baujahr
        ORDER BY Typ, Baujahr
    ''')
    ```

- **HAVING-Klausel für Gruppen-Filter**
  - Filtert Gruppen nach Aggregationsergebnis (WHERE filtert vor Gruppierung)
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT Maschinen_ID, AVG(Temperatur) AS Avg_Temp
        FROM Messdaten
        GROUP BY Maschinen_ID
        HAVING AVG(Temperatur) > 80
    ''')
    ```

- **Aggregat-Funktionen**:
  - **`COUNT(*)`**: Zählt alle Zeilen (inkl. NULL)
  - **`COUNT(Spalte)`**: Zählt Zeilen mit NOT NULL Werten
  - **`SUM(Spalte)`**: Summe aller Werte
  - **`AVG(Spalte)`**: Durchschnitt (Mittelwert)
  - **`MIN(Spalte)`**: Kleinster Wert
  - **`MAX(Spalte)`**: Größter Wert

#### JOINs (Erweitert)

- **INNER JOIN** (Nur Übereinstimmungen)
  - Gibt nur Zeilen zurück, die in beiden Tabellen Matches haben
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT m.Name AS Maschine, w.Datum, w.Typ, w.Kosten
        FROM Maschinen m
        INNER JOIN Wartungen w ON m.Maschinen_ID = w.Maschinen_ID
        WHERE m.Typ = 'CNC-Fräse'
    ''')
    ```

- **LEFT JOIN (LEFT OUTER JOIN)** (Alle links + Matches)
  - Gibt alle Zeilen der linken Tabelle zurück + Matches aus rechter
  - Bei keinem Match: Spalten der rechten Tabelle sind `NULL`
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT m.Name, COUNT(w.Wartungs_ID) AS Anzahl_Wartungen
        FROM Maschinen m
        LEFT JOIN Wartungen w ON m.Maschinen_ID = w.Maschinen_ID
        GROUP BY m.Maschinen_ID
    ''')
    # Zeigt auch Maschinen OHNE Wartungen (Anzahl = 0)
    ```

- **Mehrfache JOINs** (3+ Tabellen verbinden)
  - Verkettung mehrerer JOIN-Operationen
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT 
            m.Name AS Maschine,
            w.Datum,
            w.Typ AS Wartungstyp,
            t.Name AS Techniker,
            t.Spezialisierung
        FROM Wartungen w
        INNER JOIN Maschinen m ON w.Maschinen_ID = m.Maschinen_ID
        INNER JOIN Techniker t ON w.Techniker_ID = t.Techniker_ID
        WHERE w.Kosten > 1000
        ORDER BY w.Datum DESC
    ''')
    ```

#### Subqueries (Unterabfragen)

- **Subquery in WHERE-Klausel**
  - Nutzt Ergebnis einer inneren Query für Filter
  - Beispiel mit `WHERE IN`:
    ```python
    cursor.execute('''
        SELECT Name, Baujahr 
        FROM Maschinen
        WHERE Maschinen_ID IN (
            SELECT Maschinen_ID 
            FROM Wartungen 
            WHERE Kosten > 5000
        )
    ''')
    ```

- **Nested SELECT (Subquery im SELECT)**
  - Berechnet Wert für jede Zeile mit Subquery
  - Beispiel:
    ```python
    cursor.execute('''
        SELECT 
            Name,
            Baujahr,
            (SELECT COUNT(*) 
             FROM Wartungen w 
             WHERE w.Maschinen_ID = m.Maschinen_ID) AS Wartungen_Gesamt
        FROM Maschinen m
    ''')
    ```

#### Best Practices (Erweitert)

- **Indizes auf Foreign Keys**
  - Verbessert JOIN-Performance erheblich
  - Syntax: `CREATE INDEX idx_tabelle_spalte ON Tabelle(Spalte)`
  - Beispiel:
    ```python
    cursor.execute('CREATE INDEX idx_wartungen_maschine ON Wartungen(Maschinen_ID)')
    cursor.execute('CREATE INDEX idx_messdaten_maschine ON Messdaten(Maschinen_ID)')
    ```

- **Error Handling mit try-except-finally**
  - Robuste Transaktions-Verwaltung
  - Beispiel:
    ```python
    try:
        cursor.execute('BEGIN')
        cursor.execute('UPDATE ...')
        cursor.execute('INSERT ...')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Fehler: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    ```

- **`executemany()` für Batch-Operations**
  - Deutlich schneller als Schleife mit `.execute()`
  - Beispiel:
    ```python
    daten = [(name, typ, jahr) for ...]
    cursor.executemany('''
        INSERT INTO Maschinen (Name, Typ, Baujahr) 
        VALUES (?, ?, ?)
    ''', daten)
    ```

- **PRAGMA foreign_keys ON**
  - Muss bei jedem Connection-Start aktiviert werden
  - SQLite deaktiviert Foreign Key Constraints standardmäßig
  - Beispiel:
    ```python
    conn = sqlite3.connect('db.db')
    conn.execute('PRAGMA foreign_keys = ON')
    ```

- **LIMIT für große Result Sets**
  - Verhindert Memory-Probleme bei großen Abfragen
  - Beispiel:
    ```python
    cursor.execute('SELECT * FROM Messdaten ORDER BY Zeitstempel DESC LIMIT 100')
    ```

#### Pandas-Integration

- **`pd.pivot_table()`** (pandas-Funktion)
  - Erstellt Pivot-Tabelle (Kreuztabelle) aus DataFrame
  - Parameter:
    - `data`: Source DataFrame
    - `values`: Zu aggregierende Spalte
    - `index`: Zeilen-Gruppierung
    - `columns`: Spalten-Gruppierung
    - `aggfunc`: Aggregationsfunktion (`'mean'`, `'sum'`, `'count'`, etc.)
  - Signatur: `pd.pivot_table(data, values, index, columns, aggfunc)` → `DataFrame`
  - Beispiel:
    ```python
    pivot = pd.pivot_table(
        df, 
        values='Kosten', 
        index='Maschinentyp', 
        columns='Jahr', 
        aggfunc='mean'
    )
    ```

- **`pd.to_excel()`** (DataFrame-Methode)
  - Exportiert DataFrame als Excel-Datei
  - Erfordert `openpyxl` Bibliothek
  - Signatur: `df.to_excel(filename, sheet_name, index)` → `None`
  - Beispiel:
    ```python
    df.to_excel('wartungskosten_analyse.xlsx', sheet_name='Kosten', index=True)
    ```

#### Context Manager (Benutzerdefiniert)

- **`__enter__()`-Methode** (Magic Method)
  - Wird beim Eintritt in `with`-Block aufgerufen
  - Gibt Ressource zurück (oft `self`)
  - Signatur: `__enter__(self)` → `object`
  - Beispiel:
    ```python
    class DatenbankVerbindung:
        def __init__(self, db_name):
            self.db_name = db_name
            self.conn = None
        
        def __enter__(self):
            self.conn = sqlite3.connect(self.db_name)
            self.conn.execute('PRAGMA foreign_keys = ON')
            return self.conn
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()
    
    # Verwendung:
    with DatenbankVerbindung('produktionsdb.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Maschinen')
    # Automatisches commit/rollback und close
    ```

- **`__exit__(exc_type, exc_val, exc_tb)`-Methode** (Magic Method)
  - Wird beim Verlassen des `with`-Blocks aufgerufen (auch bei Exceptions)
  - Parameter:
    - `exc_type`: Exception-Typ (oder `None`)
    - `exc_val`: Exception-Wert (oder `None`)
    - `exc_tb`: Traceback (oder `None`)
  - Signatur: `__exit__(self, exc_type, exc_val, exc_tb)` → `bool` (optional)
  - Return `True` unterdrückt Exception (selten gewünscht)

#### datetime-Erweiterung

- **`strftime()` für Quartal-Extraktion**
  - Formatierung von datetime-Objekten als String
  - Quartal berechnen: `Q{(monat-1)//3 + 1}`
  - Beispiel:
    ```python
    from datetime import datetime
    
    datum = datetime(2024, 7, 15)
    quartal = f"Q{(datum.month - 1) // 3 + 1}"  # "Q3"
    jahr_quartal = f"{datum.year}-{quartal}"    # "2024-Q3"
    
    # Verwendung in SQL-Query:
    cursor.execute('''
        SELECT 
            strftime('%Y', Datum) AS Jahr,
            'Q' || ((CAST(strftime('%m', Datum) AS INTEGER) - 1) / 3 + 1) AS Quartal,
            SUM(Kosten) AS Gesamtkosten
        FROM Wartungen
        GROUP BY Jahr, Quartal
    ''')
    ```

### Konzepte und Best Practices

- **Named Placeholders für Lesbarkeit**: Bei vielen Parametern übersichtlicher als `?`
- **`cursor.rowcount` nach Änderungen prüfen**: Validierung, dass Operation erfolgreich war
- **CASCADE für referentielle Integrität**: Verhindert Waisen-Zeilen (Orphaned Records)
- **SAVEPOINT für komplexe Transaktionen**: Ermöglicht partielles Rollback
- **HAVING vs WHERE**: WHERE filtert vor Gruppierung, HAVING filtert nach Aggregation
- **LEFT JOIN für "auch ohne Match"**: Zeigt alle Zeilen der linken Tabelle
- **Indizes auf JOIN-Spalten**: Kritisch für Performance bei großen Tabellen
- **`executemany()` für Batch-Operations**: 10-100x schneller als Schleife
- **Context Manager für Ressourcen**: Garantiert cleanup auch bei Exceptions

### Notizen

- Named Placeholders (`:name`) existieren seit Python 2.5 (sqlite3-Einführung)
- `cursor.rowcount` gibt bei SELECT in SQLite immer -1 zurück (DB-API 2.0 Limitation)
- CASCADE DELETE erfordert `PRAGMA foreign_keys = ON` pro Connection (nicht persistent)
- SAVEPOINT ist Teil des SQL-92 Standards (nicht SQLite-spezifisch)
- GROUP BY + HAVING ist SQL-Standard (existiert in allen RDBMS)
- LEFT JOIN kann zu Cartesian Product führen bei fehlerhaften ON-Bedingungen
- Subqueries können Performance-Probleme verursachen (oft mit JOINs optimierbar)
- `pd.pivot_table()` ist mächtiges Werkzeug für OLAP-artige Analysen
- Context Manager mit `__enter__`/`__exit__` ist Python 2.5+ Feature (PEP 343)
- SQLite `strftime()` unterstützt nicht alle datetime-Formate (limitierter als Python)

---