# V03: Boolsche Algebra & Logische Schaltungen – Teil 1

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Die drei grundlegenden logischen Operatoren **AND**, **OR** und **NOT** verstehen und anwenden können
> - **Wahrheitstabellen** für logische Ausdrücke erstellen und interpretieren
> - Einfache **logische Schaltungen** analysieren und deren Funktionsweise nachvollziehen
> - Python-**Datentypen** (`int`, `float`, `str`, `bool`) unterscheiden und gezielt einsetzen
> - **Type Casting** und **Type Checking** mit `type()` und `isinstance()` durchführen
> - Den Unterschied zwischen **unveränderlichen** (immutable) und **veränderlichen** (mutable) Typen erklären
> - **Variablen-Scope** (lokal vs. global) verstehen und korrekt anwenden

---

## Teil 1: Theorie - Boolsche Algebra & Logische Schaltungen

### Überblick

Die **Boolsche Algebra** bildet das mathematische Fundament der digitalen Elektronik und damit aller modernen Computer. Der englische Mathematiker George Boole entwickelte im 19. Jahrhundert ein algebraisches System, das nur zwei Zustände kennt: **wahr** (1, true, high) und **falsch** (0, false, low). Dieses binäre System ermöglicht es, komplexe logische Zusammenhänge präzise zu beschreiben und technisch umzusetzen.

In dieser Vorlesung lernen Sie die drei fundamentalen logischen Operatoren kennen, mit denen sich jede beliebige logische Funktion aufbauen lässt. Diese Operatoren bilden die Grundlage für Prozessor-Architekturen, Speicherbausteine und alle digitalen Schaltungen in Computern, Smartphones und Industriesteuerungen.

> [!NOTE]
> **Boolsche Algebra**: Ein algebraisches System mit zwei Wahrheitswerten (0 und 1) und logischen Operationen, das die Grundlage der digitalen Elektronik bildet.

### Die drei fundamentalen logischen Operatoren

Die Boolsche Algebra kennt drei grundlegende Operatoren, aus denen sich alle komplexeren logischen Funktionen zusammensetzen lassen. Diese Operatoren verknüpfen einen oder mehrere Eingangswerte zu einem Ausgangswert.

#### Der AND-Operator (Logisches UND)

Der **AND-Operator** (auch **Konjunktion** genannt) verknüpft zwei Eingangswerte und liefert nur dann den Wert 1 (wahr), wenn **beide** Eingänge den Wert 1 haben. In allen anderen Fällen ist das Ergebnis 0 (falsch).

> [!NOTE]
> **AND-Operator**: Eine logische Verknüpfung, die nur dann wahr ist, wenn alle Eingänge wahr sind. Symbol: ∧ (mathematisch), & (Programmierung), • (Schaltungslogik).

Die **Wahrheitstabelle** für den AND-Operator zeigt alle möglichen Eingangskombinationen und die zugehörigen Ausgänge:

| A | B | A ∧ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

> [!TIP]
> **Alltagsbeispiel für AND**: Ein Auto startet nur, wenn der Schlüssel eingesteckt **UND** die Bremse getreten ist. Beide Bedingungen müssen erfüllt sein.

In der **Digitaltechnik** wird der AND-Operator durch ein **AND-Gatter** realisiert. Das Schaltsymbol nach IEEE-Standard (amerikanische Notation) zeigt eine charakteristische D-förmige Linie:

```
    A ────┐
          │╲
          │ ╲
          │  ╲───── A ∧ B
          │  ╱
          │ ╱
    B ────┘╱
```

Die **logische Gleichung** lautet: `Y = A ∧ B` oder häufig auch `Y = A · B` (Punkt-Schreibweise aus der klassischen Algebra).

> [!WARNING]
> **Häufiger Denkfehler**: Anfänger verwechseln oft AND mit OR. Merke: Bei AND müssen **alle** Bedingungen erfüllt sein – wie bei einer Tür mit mehreren Schlössern, die alle aufgeschlossen werden müssen.

#### Der OR-Operator (Logisches ODER)

Der **OR-Operator** (auch **Disjunktion** genannt) liefert den Wert 1 (wahr), wenn **mindestens einer** der Eingänge den Wert 1 hat. Nur wenn beide Eingänge 0 sind, ist auch das Ergebnis 0.

> [!NOTE]
> **OR-Operator**: Eine logische Verknüpfung, die wahr ist, wenn mindestens ein Eingang wahr ist. Symbol: ∨ (mathematisch), | (Programmierung), + (Schaltungslogik).

Die **Wahrheitstabelle** für den OR-Operator:

| A | B | A ∨ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   1   |

> [!TIP]
> **Alltagsbeispiel für OR**: Eine Lampe leuchtet, wenn der Wandschalter eingeschaltet **ODER** der Fernbedienungsschalter aktiviert ist. Es reicht, wenn eine der beiden Bedingungen erfüllt ist.

Das **OR-Gatter** in der Digitaltechnik wird durch ein Symbol mit geschwungener Eingangsseite dargestellt:

```
    A ────┐
          │)
          │ )
          │  )───── A ∨ B
          │ )
          │)
    B ────┘
```

Die **logische Gleichung** lautet: `Y = A ∨ B` oder `Y = A + B` (Plus-Schreibweise, aber Achtung: **nicht** die gewöhnliche arithmetische Addition!).

> [!WARNING]
> **Wichtige Unterscheidung**: In der Boolschen Algebra gilt `1 + 1 = 1` (nicht 2!), da OR bereits bei einem einzigen wahren Eingang wahr ist.

#### Der NOT-Operator (Logische Negation)

Der **NOT-Operator** (auch **Negation** oder **Inversion** genannt) ist ein **einstelliger** (unärer) Operator. Er kehrt den Eingangswert um: Aus 0 wird 1, aus 1 wird 0.

> [!NOTE]
> **NOT-Operator**: Ein logischer Operator, der den Eingangswert invertiert (umkehrt). Symbol: ¬ (mathematisch), ~ (Programmierung), Überstrich (Schaltungslogik: Ā).

Die **Wahrheitstabelle** für den NOT-Operator ist besonders einfach:

| A | ¬A |
|---|----|
| 0 | 1  |
| 1 | 0  |

> [!TIP]
> **Alltagsbeispiel für NOT**: Ein Türöffner ist aktiv, wenn der Not-Aus-Schalter **NICHT** gedrückt ist. Die Negation kehrt den Zustand um.

Das **NOT-Gatter** (auch **Inverter** genannt) wird durch ein Dreieck-Symbol mit einem kleinen Kreis am Ausgang dargestellt. Der Kreis symbolisiert die Invertierung:

```
    A ────▷○───── ¬A
```

Die **logische Gleichung** lautet: `Y = ¬A` oder `Y = Ā` (A mit Überstrich) oder manchmal `Y = A'` (A mit Apostroph).

### Wahrheitstabellen: Systematische Analyse logischer Ausdrücke

**Wahrheitstabellen** sind das zentrale Werkzeug zur systematischen Analyse und Darstellung logischer Funktionen. Sie zeigen für alle möglichen Eingangskombinationen das jeweilige Ausgangsergebnis.

> [!NOTE]
> **Wahrheitstabelle**: Eine tabellarische Übersicht, die für alle möglichen Eingangskombinationen den zugehörigen Ausgangswert einer logischen Funktion angibt.

#### Anzahl der Zeilen in einer Wahrheitstabelle

Bei $n$ Eingangsvariablen gibt es $2^n$ mögliche Kombinationen. Jede Kombination entspricht einer Zeile in der Wahrheitstabelle:

- 1 Variable: $2^1 = 2$ Zeilen (0, 1)
- 2 Variablen: $2^2 = 4$ Zeilen (00, 01, 10, 11)
- 3 Variablen: $2^3 = 8$ Zeilen (000, 001, 010, ..., 111)
- 4 Variablen: $2^4 = 16$ Zeilen

> [!TIP]
> **Systematisches Vorgehen**: Beginne bei der ersten Spalte und wechsle zwischen 0 und 1 nach jeweils $2^{n-1}$ Zeilen. In der zweiten Spalte nach $2^{n-2}$ Zeilen, usw. So entsteht automatisch die richtige Reihenfolge.

#### Beispiel: Wahrheitstabelle für A ∧ (B ∨ C)

Betrachten wir den zusammengesetzten Ausdruck `A ∧ (B ∨ C)`. Diese Funktion hat drei Eingänge (A, B, C) und benötigt daher 8 Zeilen:

| A | B | C | B ∨ C | A ∧ (B ∨ C) |
|---|---|---|-------|-------------|
| 0 | 0 | 0 |   0   |      0      |
| 0 | 0 | 1 |   1   |      0      |
| 0 | 1 | 0 |   1   |      0      |
| 0 | 1 | 1 |   1   |      0      |
| 1 | 0 | 0 |   0   |      0      |
| 1 | 0 | 1 |   1   |      1      |
| 1 | 1 | 0 |   1   |      1      |
| 1 | 1 | 1 |   1   |      1      |

**Vorgehen beim Erstellen**:
1. Alle Eingangskombinationen systematisch auflisten (8 Zeilen für 3 Variablen)
2. Zwischenergebnis `B ∨ C` berechnen (OR-Verknüpfung von B und C)
3. Endergebnis `A ∧ (B ∨ C)` durch AND-Verknüpfung von A mit dem Zwischenergebnis

> [!WARNING]
> **Klammerung beachten**: Die Reihenfolge der Auswertung ist entscheidend! `A ∧ (B ∨ C)` ist **nicht** dasselbe wie `(A ∧ B) ∨ C`. Arbeite immer von innen nach außen, wie bei mathematischen Klammern.

### Einfache logische Schaltungen

Logische Operatoren werden in der Digitaltechnik durch **Gatter** (engl. Gates) realisiert. Ein Gatter ist eine elektronische Schaltung, die eine logische Funktion umsetzt. Mehrere Gatter lassen sich zu komplexeren Schaltungen kombinieren.

#### Beispiel 1: Serienschaltung zweier Schalter

Zwei **in Serie geschaltete** Schalter entsprechen einem AND-Gatter. Der Strom fließt nur, wenn **beide** Schalter geschlossen sind.

```
    +V ─── Schalter A ─── Schalter B ─── Lampe ─── GND
```

**Logische Funktion**: `Lampe = A ∧ B`

Die Lampe leuchtet nur, wenn sowohl Schalter A als auch Schalter B geschlossen sind.

> [!TIP]
> **Technische Anwendung**: Sicherheitsschaltungen in Maschinen verwenden oft AND-Logik. Die Maschine startet nur, wenn alle Schutztüren geschlossen sind **UND** der Startknopf gedrückt wird.

#### Beispiel 2: Parallelschaltung zweier Schalter

Zwei **parallel geschaltete** Schalter entsprechen einem OR-Gatter. Der Strom fließt, wenn **mindestens einer** der Schalter geschlossen ist.

```
    +V ─┬─── Schalter A ───┬─── Lampe ─── GND
        │                  │
        └─── Schalter B ───┘
```

**Logische Funktion**: `Lampe = A ∨ B`

Die Lampe leuchtet, wenn Schalter A oder Schalter B (oder beide) geschlossen sind.

> [!TIP]
> **Technische Anwendung**: Wechselschaltungen in Häusern erlauben es, eine Lampe von mehreren Stellen aus zu steuern. Dies basiert auf OR-Logik (bzw. deren Erweiterungen).

#### Beispiel 3: Kombinierte Schaltung

Betrachten wir eine Schaltung mit der Funktion `Y = (A ∧ B) ∨ C`:

```
    A ────┐
          │╲
          │ ╲──┐
          │  ╱  │
    B ────┘╱   │)
               │ )
               │  )───── Y = (A ∧ B) ∨ C
          C ───┤ )
               │)
```

Diese Schaltung besteht aus einem AND-Gatter (A und B) gefolgt von einem OR-Gatter, das das AND-Ergebnis mit C verknüpft.

**Wahrheitstabelle**:

| A | B | C | A ∧ B | (A ∧ B) ∨ C |
|---|---|---|-------|-------------|
| 0 | 0 | 0 |   0   |      0      |
| 0 | 0 | 1 |   0   |      1      |
| 0 | 1 | 0 |   0   |      0      |
| 0 | 1 | 1 |   0   |      1      |
| 1 | 0 | 0 |   0   |      0      |
| 1 | 0 | 1 |   0   |      1      |
| 1 | 1 | 0 |   1   |      1      |
| 1 | 1 | 1 |   1   |      1      |

**Interpretation**: Der Ausgang Y ist wahr, wenn entweder (A und B beide wahr sind) oder C wahr ist.

> [!NOTE]
> **Schaltungsentwurf**: Komplexe logische Funktionen werden systematisch in Gatter-Schaltungen umgesetzt. Jeder logische Operator entspricht einem Gatter, und die Gatter werden entsprechend der Klammersetzung verschaltet.

### Praktische Anwendungen Boolscher Algebra

Die Boolsche Algebra und logische Schaltungen finden sich überall in der modernen Technik:

1. **Prozessor-Architektur**: Jede Rechenoperation in einem Prozessor basiert auf Millionen miteinander verschalteten Gattern. Eine einfache Addition wird durch komplexe Kombinationen von AND-, OR- und NOT-Gattern realisiert.

2. **Speicherbausteine**: RAM und Flash-Speicher verwenden logische Gatter, um Daten zu speichern und abzurufen. Ein einzelnes Bit im Speicher wird durch eine Schaltung aus Gattern gehalten.

3. **Steuerungstechnik**: Industrielle SPS (Speicherprogrammierbare Steuerungen) verwenden Boolsche Logik, um Fertigungsanlagen zu steuern. Sensorsignale werden logisch verknüpft, um Aktoren zu schalten.

4. **Datenübertragung**: Fehlererkennungs- und Fehlerkorrektur-Codes in Netzwerken und Speichermedien basieren auf Boolscher Algebra (z.B. Paritätsbits, CRC-Prüfsummen).

5. **Software-Entwicklung**: Bedingungen in Programmiersprachen (`if`, `while`) basieren direkt auf Boolscher Algebra. Jede Verzweigung im Programmablauf entspricht einer logischen Verknüpfung.

> [!TIP]
> **Vom Gatter zum Prozessor**: Ein moderner Prozessor enthält mehrere Milliarden Transistoren, die zu logischen Gattern zusammengeschaltet sind. Die fundamentalen Operationen AND, OR und NOT bilden die Basis für alle höheren Funktionen.

### Zusammenfassung Theorie

Die wichtigsten Erkenntnisse dieses Theorieteils:

- Die **Boolsche Algebra** kennt nur zwei Zustände (0 und 1, falsch und wahr) und bildet das Fundament der Digitaltechnik.
- Die drei **fundamentalen Operatoren** sind **AND** (wahr nur wenn alle Eingänge wahr), **OR** (wahr wenn mindestens ein Eingang wahr) und **NOT** (Invertierung).
- **Wahrheitstabellen** stellen alle möglichen Eingangskombinationen und die zugehörigen Ausgänge systematisch dar. Bei $n$ Eingängen gibt es $2^n$ Zeilen.
- **Logische Schaltungen** setzen Boolsche Ausdrücke mit elektronischen Gattern um. Serienschaltungen entsprechen AND, Parallelschaltungen entsprechen OR.
- Die Anwendungen reichen von einzelnen Schaltungen bis zu komplexen Prozessoren mit Milliarden von Gattern.

---

## Teil 2: Python-Praxis - Variablen Management & Datentypen

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

In den vorherigen Vorlesungen haben wir Variablen bereits verwendet und mit verschiedenen Datentypen gearbeitet. In dieser Lektion vertiefen wir das Verständnis für Pythons **Typsystem** und lernen, wie wir Variablen gezielt verwalten, Typen konvertieren und überprüfen können.

Python ist eine **dynamisch typisierte** Sprache: Der Typ einer Variable wird zur Laufzeit automatisch aus dem zugewiesenen Wert abgeleitet. Dies unterscheidet Python von **statisch typisierten** Sprachen wie C oder Java, wo Variablen einen festen, vorab deklarierten Typ haben. Dynamische Typisierung macht Python flexibel und einfach zu schreiben, erfordert aber ein gutes Verständnis der verschiedenen Datentypen und ihrer Eigenschaften.

### Die vier grundlegenden Datentypen

Python bietet mehrere eingebaute Datentypen (Built-in Types). Die vier wichtigsten für den Einstieg sind `int`, `float`, `str` und `bool`.

#### Integer (`int`) – Ganzzahlen

Der Datentyp **Integer** (`int`) repräsentiert **ganze Zahlen** ohne Nachkommastellen. In Python 3 haben Integers keine Größenbeschränkung – sie können beliebig groß werden, begrenzt nur durch den verfügbaren Arbeitsspeicher.

> [!NOTE]
> **Integer (`int`)**: Ein Datentyp für ganze Zahlen (positiv, negativ oder null) ohne Nachkommastellen. Python 3 unterstützt beliebig große Integers.

> [!TIP]
> ```python
> # Integer-Beispiele
> alter = 25
> jahr = 2026
> temperatur_celsius = -5
> sehr_grosse_zahl = 123456789012345678901234567890
> 
> print(f"Alter: {alter}, Typ: {type(alter)}")
> # Ausgabe: Alter: 25, Typ: <class 'int'>
> ```

**Eigenschaften von Integers**:
- Keine Nachkommastellen
- Unbegrenzte Größe in Python 3 (in Python 2 gab es `int` und `long`)
- Arithmetische Operationen ergeben wieder Integers, außer Division (`/`)

> [!WARNING]
> **Division erzeugt Float**: Die Division mit `/` erzeugt **immer** einen Float, auch wenn das Ergebnis ganzzahlig ist: `10 / 2` ergibt `5.0`, nicht `5`. Für ganzzahlige Division verwende `//` (Floor Division).

#### Float (`float`) – Fließkommazahlen

Der Datentyp **Float** (`float`) repräsentiert **Fließkommazahlen** mit Nachkommastellen. Python verwendet intern den IEEE 754 Double Precision Standard (64 Bit), den wir in V02 ausführlich behandelt haben.

> [!NOTE]
> **Float (`float`)**: Ein Datentyp für Zahlen mit Dezimalstellen (Fließkommazahlen). Python verwendet IEEE 754 Double Precision (64 Bit).

> [!TIP]
> ```python
> # Float-Beispiele
> pi = 3.14159
> temperatur = -12.5
> wissenschaftliche_notation = 6.022e23  # Avogadro-Konstante
> sehr_klein = 1.5e-10
> 
> print(f"Pi: {pi}, Typ: {type(pi)}")
> # Ausgabe: Pi: 3.14159, Typ: <class 'float'>
> ```

**Eigenschaften von Floats**:
- Erlauben Nachkommastellen
- Wissenschaftliche Notation möglich: `1.5e3` = $1.5 \times 10^3$ = `1500.0`
- Begrenzte Präzision (ca. 15-17 Dezimalstellen)
- Rundungsfehler möglich (siehe V02)

> [!WARNING]
> **Rundungsfehler**: Floats haben begrenzte Präzision. `0.1 + 0.2` ergibt `0.30000000000000004`, nicht exakt `0.3`. Für Geld-Berechnungen verwende das `decimal`-Modul!

#### String (`str`) – Zeichenketten

Der Datentyp **String** (`str`) repräsentiert **Zeichenketten** (Text). Strings sind in Python **unveränderlich** (immutable) – einmal erzeugt, kann ihr Inhalt nicht mehr geändert werden.

> [!NOTE]
> **String (`str`)**: Ein Datentyp für Textdaten (Zeichenketten). Strings sind unveränderlich (immutable) und werden mit Anführungszeichen definiert.

> [!TIP]
> ```python
> # String-Beispiele
> name = "Ada Lovelace"
> einzeilig = 'Python ist toll'
> mehrzeilig = """Dies ist ein
> mehrzeiliger String
> über mehrere Zeilen."""
> 
> print(f"Name: {name}, Typ: {type(name)}")
> # Ausgabe: Name: Ada Lovelace, Typ: <class 'str'>
> ```

**Eigenschaften von Strings**:
- Definiert mit `"..."` oder `'...'` (beides gleichwertig)
- Mehrzeilige Strings mit `"""..."""` oder `'''...'''`
- Unveränderlich: `text[0] = 'X'` führt zu einem Fehler
- Umfangreiche String-Methoden verfügbar (`.upper()`, `.lower()`, `.split()`, etc.)

> [!WARNING]
> **Unveränderlichkeit**: Strings können nicht verändert werden. Operationen wie `text.upper()` erzeugen einen **neuen** String, der originale bleibt unverändert. Weise das Ergebnis einer Variable zu: `text = text.upper()`.

#### Boolean (`bool`) – Wahrheitswerte

Der Datentyp **Boolean** (`bool`) repräsentiert **Wahrheitswerte**. Es gibt nur zwei mögliche Werte: `True` (wahr) und `False` (falsch). Booleans sind das Herzstück von Bedingungen und logischen Ausdrücken.

> [!NOTE]
> **Boolean (`bool`)**: Ein Datentyp für Wahrheitswerte mit nur zwei möglichen Werten: `True` (wahr) und `False` (falsch). Wichtig: Großschreibung beachten!

> [!TIP]
> ```python
> # Boolean-Beispiele
> ist_student = True
> ist_abgeschlossen = False
> ergebnis = (5 > 3)  # True, da 5 größer als 3
> 
> print(f"Student: {ist_student}, Typ: {type(ist_student)}")
> # Ausgabe: Student: True, Typ: <class 'bool'>
> ```

**Eigenschaften von Booleans**:
- Nur zwei Werte: `True` und `False` (Großschreibung zwingend!)
- Entstehen aus Vergleichen: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Intern sind Booleans Subtypen von `int`: `True` = 1, `False` = 0
- Verwenden in Bedingungen (`if`) und Schleifen (`while`)

> [!WARNING]
> **Großschreibung beachten**: `True` und `False` müssen großgeschrieben werden. `true` oder `false` sind **keine** gültigen Python-Werte und führen zu `NameError`.

### Type Casting: Datentypen konvertieren

Oft müssen wir Werte von einem Datentyp in einen anderen umwandeln. Python bietet hierfür die **Type Casting**-Funktionen `int()`, `float()`, `str()` und `bool()`.

> [!NOTE]
> **Type Casting**: Die explizite Konvertierung eines Wertes von einem Datentyp in einen anderen. Python führt manche Konvertierungen automatisch durch (implizites Casting), andere müssen explizit angefordert werden.

#### String zu Zahl: `int()` und `float()`

Die Funktionen `int()` und `float()` wandeln Strings in Zahlen um. Dies ist besonders wichtig, da `input()` immer einen String zurückgibt.

> [!TIP]
> ```python
> # String zu Integer
> alter_str = "25"
> alter_int = int(alter_str)
> print(f"{alter_int} + 1 = {alter_int + 1}")  # 26
> 
> # String zu Float
> temperatur_str = "23.5"
> temperatur_float = float(temperatur_str)
> print(f"Temperatur: {temperatur_float}°C")  # 23.5°C
> 
> # Mit Benutzereingabe
> eingabe = input("Gib eine Zahl ein: ")  # z.B. "42"
> zahl = int(eingabe)  # Konvertierung notwendig!
> print(f"Doppelt: {zahl * 2}")
> ```

> [!WARNING]
> **ValueError bei ungültiger Konvertierung**: Wenn der String keine gültige Zahl enthält, wirft Python einen `ValueError`:
> 
> ```python
> int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
> float("3.14.15")  # ValueError: could not convert string to float
> ```
> 
> **Lösung**: Prüfe die Eingabe vorher oder fange den Fehler mit `try-except` ab (kommt in V09).

#### Zahl zu String: `str()`

Die Funktion `str()` wandelt Zahlen (und andere Typen) in Strings um. Dies ist nützlich für String-Konkatenation und formatierte Ausgaben.

> [!TIP]
> ```python
> # Zahlen zu String
> alter = 25
> jahr = 2026
> 
> # Mit str() für Konkatenation
> nachricht = "Ich bin " + str(alter) + " Jahre alt."
> print(nachricht)  # Ich bin 25 Jahre alt.
> 
> # Besser: f-Strings (automatische Konvertierung)
> nachricht = f"Ich bin {alter} Jahre alt."
> print(nachricht)  # Ich bin 25 Jahre alt.
> ```

> [!WARNING]
> **Typ-Mismatch bei Konkatenation**: Man kann Strings nicht direkt mit Zahlen konkatenieren:
> 
> ```python
> "Alter: " + 25  # TypeError: can only concatenate str (not "int") to str
> ```
> 
> **Lösung**: Verwende `str(25)` oder (besser) f-Strings: `f"Alter: {25}"`.

#### Float zu Integer: Vorsicht bei Rundung

Die Konvertierung von Float zu Integer mit `int()` schneidet die Nachkommastellen **ab** (Floor-Operation für positive Zahlen, Ceiling für negative). Es findet **keine** kaufmännische Rundung statt!

> [!TIP]
> ```python
> # Float zu Integer (Abschneiden, nicht Runden!)
> print(int(3.7))   # 3 (nicht 4!)
> print(int(3.2))   # 3
> print(int(-2.9))  # -2 (nicht -3!)
> 
> # Für echtes Runden: round()
> print(round(3.7))   # 4
> print(round(3.2))   # 3
> print(round(2.5))   # 2 (Banker's Rounding bei .5)
> ```

> [!WARNING]
> **`int()` schneidet ab, rundet nicht**: Für mathematisch korrektes Runden verwende die `round()`-Funktion. `int()` entfernt einfach die Nachkommastellen.

#### Konvertierung zu Boolean: `bool()`

Die Funktion `bool()` konvertiert Werte zu Booleans. Python hat klare Regeln, welche Werte als `False` gelten (**Falsy Values**) und welche als `True` (**Truthy Values**).

> [!NOTE]
> **Falsy Values**: Werte, die in Boolschem Kontext als `False` interpretiert werden: `0`, `0.0`, `""` (leerer String), `[]` (leere Liste), `None`.
> 
> **Truthy Values**: Alle anderen Werte gelten als `True`.

> [!TIP]
> ```python
> # Falsy Values (ergeben False)
> print(bool(0))      # False
> print(bool(0.0))    # False
> print(bool(""))     # False (leerer String)
> print(bool(None))   # False
> 
> # Truthy Values (ergeben True)
> print(bool(42))     # True (jede Zahl ≠ 0)
> print(bool(-1))     # True (auch negative Zahlen)
> print(bool("Hallo")) # True (nicht-leerer String)
> print(bool(" "))    # True (String mit Leerzeichen ist nicht leer!)
> ```

### Type Checking: Datentypen überprüfen

Um den Typ einer Variable zur Laufzeit zu überprüfen, bietet Python zwei Hauptmethoden: `type()` und `isinstance()`.

#### `type()` – Typ einer Variable ermitteln

Die Funktion `type()` gibt den **exakten Typ** eines Objekts zurück.

> [!NOTE]
> **`type(obj)`**: Gibt den Datentyp des übergebenen Objekts zurück. Signatur: `type(obj)` → `type`.

> [!TIP]
> ```python
> # Type Checking mit type()
> x = 42
> y = 3.14
> z = "Hallo"
> 
> print(type(x))  # <class 'int'>
> print(type(y))  # <class 'float'>
> print(type(z))  # <class 'str'>
> 
> # Vergleich mit type()
> if type(x) == int:
>     print("x ist ein Integer")
> 
> # Direkter Vergleich
> print(type(x) == type(42))  # True
> ```

#### `isinstance()` – Überprüfung mit Vererbung

Die Funktion `isinstance()` prüft, ob ein Objekt eine **Instanz** eines bestimmten Typs (oder einer seiner Oberklassen) ist. Sie ist flexibler als `type()`, da sie **Vererbung** berücksichtigt.

> [!NOTE]
> **`isinstance(obj, classinfo)`**: Prüft, ob `obj` eine Instanz von `classinfo` ist. Berücksichtigt Vererbung. Signatur: `isinstance(obj, classinfo)` → `bool`.

> [!TIP]
> ```python
> # Type Checking mit isinstance()
> x = 42
> y = 3.14
> z = True  # bool ist Subtyp von int!
> 
> print(isinstance(x, int))   # True
> print(isinstance(y, float)) # True
> print(isinstance(z, int))   # True! bool erbt von int
> print(isinstance(z, bool))  # True
> 
> # Mehrere Typen gleichzeitig prüfen (Tupel)
> eingabe = "Hallo"
> if isinstance(eingabe, (int, float)):
>     print("eingabe ist eine Zahl")
> else:
>     print("eingabe ist keine Zahl")
> ```

> [!WARNING]
> **`type()` vs. `isinstance()`**: Verwende `isinstance()` für Typ-Checks, besonders wenn Vererbung eine Rolle spielt. `bool` ist ein Subtyp von `int`, daher ist `isinstance(True, int)` → `True`, aber `type(True) == int` → `False`.

### Unveränderliche vs. veränderliche Typen

Ein zentrales Konzept in Python ist die Unterscheidung zwischen **unveränderlichen** (immutable) und **veränderlichen** (mutable) Datentypen.

> [!NOTE]
> **Immutable (unveränderlich)**: Objekte, deren Wert nach der Erzeugung nicht mehr geändert werden kann. Operationen erzeugen neue Objekte. Beispiele: `int`, `float`, `str`, `tuple`, `bool`.
> 
> **Mutable (veränderlich)**: Objekte, deren Inhalt nach der Erzeugung verändert werden kann. Operationen modifizieren das Objekt direkt. Beispiele: `list`, `dict`, `set`.

#### Unveränderliche Typen: `int`, `float`, `str`, `bool`

Alle grundlegenden Datentypen (`int`, `float`, `str`, `bool`) sind **unveränderlich**. Wenn man sie "verändert", erzeugt Python im Hintergrund ein neues Objekt.

> [!TIP]
> ```python
> # Strings sind unveränderlich
> text = "Hallo"
> print(id(text))  # Speicheradresse, z.B. 140234567890123
> 
> text = text + " Welt"  # Erzeugt NEUEN String
> print(id(text))  # Andere Speicheradresse!
> 
> # Integers sind unveränderlich
> x = 10
> print(id(x))
> x = x + 1  # Erzeugt NEUEN Integer
> print(id(x))  # Andere Speicheradresse
> ```

**Warum ist das wichtig?**
- **Performance**: Unveränderliche Objekte können effizient geteilt werden (String Interning)
- **Sicherheit**: Unveränderliche Objekte können als Dictionary-Keys verwendet werden
- **Funktionsparameter**: Keine unerwarteten Seiteneffekte bei Funktionsaufrufen

> [!WARNING]
> **String-Modifikation ist ineffizient**: Viele String-Konkatenationen in Schleifen sind langsam, da jedes Mal ein neues Objekt erzeugt wird. Verwende stattdessen `''.join(liste)` oder f-Strings.

#### Veränderliche Typen: `list`, `dict`, `set`

Die Datenstrukturen `list`, `dict` und `set` (kommen in V08) sind **veränderlich**. Sie können nach ihrer Erzeugung modifiziert werden, ohne dass ein neues Objekt entsteht.

> [!TIP]
> ```python
> # Listen sind veränderlich
> zahlen = [1, 2, 3]
> print(id(zahlen))  # Speicheradresse
> 
> zahlen.append(4)  # Modifiziert DIESELBE Liste
> print(id(zahlen))  # GLEICHE Speicheradresse!
> print(zahlen)      # [1, 2, 3, 4]
> ```

**Konsequenzen**:
- **Seiteneffekte möglich**: Änderungen an einer Liste wirken sich auf alle Referenzen aus
- **Nicht als Dictionary-Keys**: Veränderliche Objekte können nicht als Keys verwendet werden
- **Funktionsparameter**: Vorsicht bei Funktionen, die Listen modifizieren!

### Variablen-Scope: Lokal vs. Global

Der **Scope** (Gültigkeitsbereich) einer Variable bestimmt, wo im Code auf sie zugegriffen werden kann. Python unterscheidet zwischen **lokalen** und **globalen** Variablen.

> [!NOTE]
> **Scope (Gültigkeitsbereich)**: Der Bereich im Code, in dem eine Variable sichtbar und verwendbar ist.
> 
> **Globale Variable**: Eine Variable, die außerhalb aller Funktionen definiert ist und im gesamten Modul sichtbar ist.
> 
> **Lokale Variable**: Eine Variable, die innerhalb einer Funktion definiert ist und nur dort sichtbar ist.

#### Globale Variablen

Variablen, die **außerhalb** von Funktionen definiert werden, sind **global** und können überall im Modul gelesen werden.

> [!TIP]
> ```python
> # Globale Variable
> sprache = "Python"
> 
> def zeige_sprache():
>     print(f"Ich programmiere in {sprache}")  # Zugriff auf globale Variable
> 
> zeige_sprache()  # Ich programmiere in Python
> print(sprache)   # Python (auch außerhalb der Funktion sichtbar)
> ```

#### Lokale Variablen

Variablen, die **innerhalb** einer Funktion definiert werden, sind **lokal** und nur innerhalb dieser Funktion sichtbar.

> [!TIP]
> ```python
> def berechne_summe():
>     # Lokale Variablen
>     a = 10
>     b = 20
>     summe = a + b
>     return summe
> 
> ergebnis = berechne_summe()  # 30
> print(ergebnis)
> 
> # print(a)  # NameError! a existiert außerhalb der Funktion nicht
> ```

> [!WARNING]
> **Namenskonflikte**: Wenn eine lokale Variable denselben Namen hat wie eine globale, **überdeckt** die lokale Variable die globale innerhalb der Funktion:
> 
> ```python
> x = "global"
> 
> def funktion():
>     x = "lokal"  # Neue lokale Variable, überdeckt globales x
>     print(x)     # lokal
> 
> funktion()
> print(x)  # global (globales x ist unverändert)
> ```

#### Das `global`-Keyword

Um eine **globale Variable innerhalb einer Funktion zu modifizieren**, muss sie mit dem `global`-Keyword deklariert werden.

> [!NOTE]
> **`global`-Keyword**: Deklariert, dass eine Variable innerhalb einer Funktion die globale Variable mit diesem Namen referenziert, nicht eine neue lokale Variable.

> [!TIP]
> ```python
> zaehler = 0  # Globale Variable
> 
> def inkrementiere():
>     global zaehler  # Referenz auf globale Variable
>     zaehler += 1
> 
> print(zaehler)  # 0
> inkrementiere()
> print(zaehler)  # 1
> inkrementiere()
> print(zaehler)  # 2
> ```

> [!WARNING]
> **`global` sparsam verwenden**: Globale Variablen, die von Funktionen verändert werden, machen Code schwer verständlich und fehleranfällig. Bevorzuge **Funktionsparameter und Rückgabewerte** statt globaler Variablen. Verwende `global` nur, wenn wirklich notwendig (z.B. für Zähler oder Konfiguration).

### Multiple Assignment und Value Unpacking

Python erlaubt elegante Kurzschreibweisen für die Zuweisung mehrerer Variablen gleichzeitig.

#### Multiple Assignment

Man kann **mehreren Variablen gleichzeitig denselben Wert** zuweisen:

> [!TIP]
> ```python
> # Mehrere Variablen mit demselben Wert
> x = y = z = 0
> print(x, y, z)  # 0 0 0
> 
> # Nützlich für Initialisierung
> summe = anzahl = 0
> ```

> [!WARNING]
> **Vorsicht bei mutable Typen**: Bei veränderlichen Typen (Listen) zeigen alle Variablen auf **dasselbe** Objekt:
> 
> ```python
> a = b = []  # Beide zeigen auf DIESELBE Liste!
> a.append(1)
> print(b)  # [1] - auch b ist betroffen!
> 
> # Besser: Separate Listen erzeugen
> a = []
> b = []
> ```

#### Value Unpacking (Tuple Unpacking)

Python erlaubt das **gleichzeitige Zuweisen mehrerer Werte** an mehrere Variablen in einer Zeile:

> [!NOTE]
> **Value Unpacking**: Das Zuweisen mehrerer Werte gleichzeitig durch komma-getrennte Notation. Intern arbeitet Python mit Tupeln.

> [!TIP]
> ```python
> # Mehrere Variablen gleichzeitig zuweisen
> x, y, z = 1, 2, 3
> print(x)  # 1
> print(y)  # 2
> print(z)  # 3
> 
> # Variablen tauschen (ohne temporäre Variable!)
> a, b = 10, 20
> print(f"Vorher: a={a}, b={b}")  # a=10, b=20
> 
> a, b = b, a  # Swap!
> print(f"Nachher: a={a}, b={b}")  # a=20, b=10
> 
> # Funktionsrückgaben unpacking
> def min_max(zahlen):
>     return min(zahlen), max(zahlen)
> 
> minimum, maximum = min_max([5, 2, 8, 1, 9])
> print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9
> ```

> [!WARNING]
> **Anzahl muss übereinstimmen**: Die Anzahl der Variablen links muss mit der Anzahl der Werte rechts übereinstimmen:
> 
> ```python
> x, y = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
> x, y, z = 1, 2  # ValueError: not enough values to unpack (expected 3, got 2)
> ```

### Häufige Fehler und Lösungen

#### Fehler 1: Type Mismatch bei Operationen

> [!WARNING]
> **Fehler**: Versuch, inkompatible Typen zu verknüpfen:
> 
> ```python
> "Alter: " + 25  # TypeError: can only concatenate str (not "int") to str
> ```
> 
> **Lösung**: Verwende `str()` zur Konvertierung oder (besser) f-Strings:
> 
> ```python
> "Alter: " + str(25)  # Funktioniert
> f"Alter: {25}"       # Eleganter!
> ```

#### Fehler 2: Division durch Null

> [!WARNING]
> **Fehler**: Division durch Null ist mathematisch undefiniert:
> 
> ```python
> ergebnis = 10 / 0  # ZeroDivisionError: division by zero
> ```
> 
> **Lösung**: Prüfe den Nenner vor der Division:
> 
> ```python
> nenner = 0
> if nenner != 0:
>     ergebnis = 10 / nenner
> else:
>     print("Division durch Null nicht möglich!")
> ```

#### Fehler 3: Falsche Annahme über Unveränderlichkeit

> [!WARNING]
> **Fehler**: Annahme, dass String-Methoden den originalen String ändern:
> 
> ```python
> text = "hallo"
> text.upper()  # Erzeugt neuen String, ändert text nicht!
> print(text)   # hallo (unverändert)
> ```
> 
> **Lösung**: Weise das Ergebnis der Variable zu:
> 
> ```python
> text = "hallo"
> text = text.upper()  # Zuweisung nötig!
> print(text)  # HALLO
> ```

#### Fehler 4: Verwechslung von `=` und `==`

> [!WARNING]
> **Fehler**: Zuweisung (`=`) statt Vergleich (`==`) in Bedingungen:
> 
> ```python
> x = 5
> if x = 10:  # SyntaxError: invalid syntax
>     print("x ist 10")
> ```
> 
> **Lösung**: Verwende `==` für Vergleiche:
> 
> ```python
> x = 5
> if x == 10:  # Korrekt
>     print("x ist 10")
> ```

### Zusammenfassung Python

Die wichtigsten Erkenntnisse zu Variablen und Datentypen in Python:

- Die **vier grundlegenden Datentypen** sind `int` (Ganzzahlen), `float` (Fließkommazahlen), `str` (Strings) und `bool` (Wahrheitswerte).
- **Type Casting** mit `int()`, `float()`, `str()`, `bool()` konvertiert zwischen Datentypen. Achtung: `int()` schneidet Nachkommastellen ab, rundet nicht!
- **Type Checking** mit `type()` ermittelt den exakten Typ, `isinstance()` prüft unter Berücksichtigung von Vererbung.
- **Unveränderliche Typen** (`int`, `float`, `str`, `bool`, `tuple`) können nach Erzeugung nicht modifiziert werden. Operationen erzeugen neue Objekte.
- **Veränderliche Typen** (`list`, `dict`, `set`) können modifiziert werden, ohne dass neue Objekte entstehen.
- **Variablen-Scope**: Globale Variablen sind überall sichtbar, lokale nur innerhalb ihrer Funktion. `global`-Keyword ermöglicht Modifikation globaler Variablen in Funktionen.
- **Multiple Assignment** und **Value Unpacking** erlauben elegante Mehrfachzuweisungen: `x, y = 1, 2` oder Variablen-Tausch: `a, b = b, a`.

### Neue Python-Funktionen/Methoden

In dieser Lektion wurden folgende Python-Funktionen **neu eingeführt**:

- **`type(obj)`** (Built-in): Gibt den Datentyp des Objekts zurück. Signatur: `type(obj)` → `type`.
- **`isinstance(obj, classinfo)`** (Built-in): Prüft, ob `obj` eine Instanz von `classinfo` ist (berücksichtigt Vererbung). Signatur: `isinstance(obj, classinfo)` → `bool`.
- **`bool(x)`** (Built-in): Konvertiert Wert in Boolean (bereits in V01 erwähnt als Datentyp, hier als Casting-Funktion).
- **`round(number, ndigits=None)`** (Built-in): Rundet eine Zahl auf `ndigits` Dezimalstellen (Banker's Rounding). Signatur: `round(number, ndigits=None)` → `float` oder `int`.
- **`id(obj)`** (Built-in): Gibt die Identität (Speicheradresse) eines Objekts zurück. Signatur: `id(obj)` → `int`.
- **`global`-Keyword**: Deklariert Variable als global innerhalb einer Funktion.
- **`min(iterable)` / `max(iterable)`** (Built-in): Gibt das kleinste/größte Element zurück. Signatur: `min(iterable)` → Element, `max(iterable)` → Element.

---

## Weiterführende Ressourcen

### Theorie
- **Buch**: "Digital Design" von Morris Mano & Michael Ciletti (Kapitel 2: Boolsche Algebra)
- **Online**: "Boolean Algebra Tutorial" auf Electronics Tutorials: https://www.electronics-tutorials.ws/boolean/bool_1.html
- **Video**: "But what is a GPT?" von 3Blue1Brown (Bezug zu logischen Gattern): https://www.youtube.com/watch?v=wjZofJX0v4M

### Python
- **Python-Dokumentation**: Built-in Types: https://docs.python.org/3/library/stdtypes.html
- **Real Python Tutorial**: "Basic Data Types in Python": https://realpython.com/python-data-types/
- **Python-Dokumentation**: Type Hierarchy: https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
- **Tutorial**: "Python's type() and isinstance(): Validate Data Types": https://realpython.com/python-type-checking/
