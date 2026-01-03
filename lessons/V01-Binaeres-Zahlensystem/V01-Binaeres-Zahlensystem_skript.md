# V01: Binäres Zahlensystem

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Stellenwertsysteme verstehen und zwischen Dezimal-, Binär-, Hexadezimal- und Oktal-System umrechnen können
> - Binäre Rechenoperationen (Addition, Subtraktion) durchführen können
> - Das Zweierkomplement zur Darstellung negativer Zahlen verstehen und anwenden
> - Bit-Masken und grundlegende Bit-Manipulation beherrschen
> - Python installieren und die erste Programme mit `print()` und `input()` schreiben
> - Variablen in Python deklarieren, zuweisen und verwenden
> - Kommentare zur Code-Dokumentation einsetzen

---

## Teil 1: Theorie - Binäres Zahlensystem

### Überblick

Computer arbeiten ausschließlich mit elektrischen Signalen, die nur zwei Zustände kennen: Strom fließt oder Strom fließt nicht. Diese beiden Zustände werden als **Bit** mit den Werten 0 und 1 repräsentiert. Um mit Computern arbeiten zu können, müssen wir verstehen, wie Zahlen in diesem binären System dargestellt werden. Das **binäre Zahlensystem** bildet die fundamentale Grundlage der gesamten digitalen Datenverarbeitung. Ohne dieses Verständnis ist es unmöglich, die Funktionsweise von Prozessoren, Speichern und Algorithmen vollständig zu erfassen.

> [!NOTE]
> Ein **Bit** (Binary Digit) ist die kleinste Informationseinheit in der digitalen Datenverarbeitung und kann genau zwei Zustände annehmen: 0 oder 1.

In der Praxis arbeiten Ingenieure häufig mit verschiedenen Zahlensystemen, da bestimmte Systeme für bestimmte Anwendungen besser geeignet sind. Hexadezimal-Notation vereinfacht beispielsweise die Darstellung von Speicheradressen und Farbcodes erheblich.

### Stellenwertsysteme allgemein

Menschen verwenden im Alltag das **Dezimalsystem** (Basis 10), weil wir zehn Finger haben. Computer nutzen das **Binärsystem** (Basis 2), weil elektronische Schaltungen nur zwei stabile Zustände haben. Das Prinzip bleibt jedoch identisch: Jede Position einer Zahl repräsentiert eine Potenz der Basis.

> [!NOTE]
> Ein **Stellenwertsystem** ist eine Methode zur Darstellung von Zahlen, bei der jede Ziffer einen Wert hat, der von ihrer Position abhängt. Der Wert einer Position wird durch eine Potenz der Basis bestimmt.

Im Dezimalsystem hat die Zahl **2468** folgende Struktur:

$$2468_{10} = 2 \cdot 10^3 + 4 \cdot 10^2 + 6 \cdot 10^1 + 8 \cdot 10^0$$

$$= 2000 + 400 + 60 + 8 = 2468$$

Das gleiche Prinzip gilt für alle anderen Stellenwertsysteme. Die wichtigsten für die Informatik sind:

- **Binärsystem (Basis 2)**: Ziffern 0, 1
- **Oktalsystem (Basis 8)**: Ziffern 0-7
- **Dezimalsystem (Basis 10)**: Ziffern 0-9
- **Hexadezimalsystem (Basis 16)**: Ziffern 0-9, A-F (wobei A=10, B=11, C=12, D=13, E=14, F=15)

> [!TIP]
> **Beispiel: Die binäre Zahl 1011₂ im Detail**
> 
> $$1011_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0$$
> 
> $$= 8 + 0 + 2 + 1 = 11_{10}$$
> 
> Die Zweierpotenzen von rechts nach links: 1, 2, 4, 8, 16, 32, 64, 128, 256, ...

> [!WARNING]
> **Häufiger Fehler bei der Notation**: Ohne Angabe der Basis ist unklar, welches Zahlensystem gemeint ist. Die Zahl "101" könnte 101₁₀ (einhunderteins im Dezimalsystem) oder 101₂ (fünf im Binärsystem) bedeuten. Verwende daher immer einen Index zur Kennzeichnung der Basis (z.B. ₂ für binär, ₁₀ für dezimal, ₁₆ für hexadezimal) oder ein Präfix (0b für binär, 0x für hexadezimal in vielen Programmiersprachen).

### Umrechnung zwischen verschiedenen Zahlensystemen

Die Fähigkeit, schnell zwischen verschiedenen Zahlensystemen umzurechnen, ist eine zentrale Kompetenz für Informatiker und Ingenieure. Dabei gibt es systematische Verfahren, die sich auf alle Basis-Konvertierungen anwenden lassen.

#### Binär → Dezimal

Die Umrechnung von binär nach dezimal erfolgt durch Berechnung der Stellenwerte. Multipliziere jede Binärziffer mit der entsprechenden Zweierpotenz und addiere alle Ergebnisse.

> [!TIP]
> **Beispiel: 11010110₂ → Dezimal**
> 
> | Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
> |----------|---|---|---|---|---|---|---|---|
> | Binärziffer | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
> | Zweierpotenz | 2⁷ | 2⁶ | 2⁵ | 2⁴ | 2³ | 2² | 2¹ | 2⁰ |
> | Wert | 128 | 64 | 0 | 16 | 0 | 4 | 2 | 0 |
> 
> **Summe**: 128 + 64 + 16 + 4 + 2 = **214₁₀**

#### Dezimal → Binär

Die Umrechnung von dezimal nach binär erfolgt durch wiederholte Division durch 2 und Notieren der Reste. Die Reste ergeben von unten nach oben gelesen die Binärdarstellung.

> [!TIP]
> **Beispiel: 214₁₀ → Binär (Divisionsverfahren)**
> 
> ```
> 214 : 2 = 107 Rest 0  ↑
> 107 : 2 =  53 Rest 1  |
>  53 : 2 =  26 Rest 1  |
>  26 : 2 =  13 Rest 0  |
>  13 : 2 =   6 Rest 1  |
>   6 : 2 =   3 Rest 0  |
>   3 : 2 =   1 Rest 1  |
>   1 : 2 =   0 Rest 1  |
> ```
> 
> Die Reste von unten nach oben gelesen: **11010110₂**

#### Hexadezimal ↔ Binär

Die Umrechnung zwischen Hexadezimal und Binär ist besonders einfach, weil eine Hexadezimalziffer genau vier Binärziffern entspricht (da 16 = 2⁴).

> [!NOTE]
> **Hexadezimal-Binär Zuordnung**: Jede Hexadezimalziffer repräsentiert exakt 4 Bit (eine sogenannte **Nibble**). Diese 1:4 Beziehung macht Konvertierungen trivial.

> [!TIP]
> **Hexadezimal-Binär Tabelle**
> 
> | Hex | Binär | Dezimal | | Hex | Binär | Dezimal |
> |-----|-------|---------|---|-----|-------|---------|
> | 0 | 0000 | 0 | | 8 | 1000 | 8 |
> | 1 | 0001 | 1 | | 9 | 1001 | 9 |
> | 2 | 0010 | 2 | | A | 1010 | 10 |
> | 3 | 0011 | 3 | | B | 1011 | 11 |
> | 4 | 0100 | 4 | | C | 1100 | 12 |
> | 5 | 0101 | 5 | | D | 1101 | 13 |
> | 6 | 0110 | 6 | | E | 1110 | 14 |
> | 7 | 0111 | 7 | | F | 1111 | 15 |
> 
> **Beispiel Hex → Binär**: 3A7F₁₆
> 
> - 3 = 0011
> - A = 1010
> - 7 = 0111
> - F = 1111
> 
> Ergebnis: **0011 1010 0111 1111₂**

### Binäre Rechenoperationen

Computer führen alle Rechenoperationen binär durch. Die grundlegenden Operationen Addition und Subtraktion funktionieren nach den gleichen Prinzipien wie im Dezimalsystem, nur mit der Basis 2.

#### Binäre Addition

Die binäre Addition folgt einfachen Regeln. Wenn die Summe zweier Bits größer oder gleich 2 ist, entsteht ein **Übertrag** (Carry) zur nächsthöheren Stelle.

> [!NOTE]
> **Additionsregeln im Binärsystem**:
> - 0 + 0 = 0
> - 0 + 1 = 1
> - 1 + 0 = 1
> - 1 + 1 = 10₂ (0 mit Übertrag 1)
> - 1 + 1 + 1 (mit Übertrag) = 11₂ (1 mit Übertrag 1)

> [!TIP]
> **Beispiel: 10110₂ + 01011₂**
> 
> ```
>   Übertrag:  ¹ ¹¹
>              1 0 1 1 0
>            + 0 1 0 1 1
>            -----------
>            1 0 0 0 0 1
> ```
> 
> Schrittweise von rechts nach links:
> - Position 0: 0 + 1 = 1
> - Position 1: 1 + 1 = 0, Übertrag 1
> - Position 2: 1 + 0 + Übertrag 1 = 0, Übertrag 1
> - Position 3: 0 + 1 + Übertrag 1 = 0, Übertrag 1
> - Position 4: 1 + 0 + Übertrag 1 = 0, Übertrag 1
> - Position 5: Übertrag 1
> 
> Ergebnis: **100001₂** (Dezimal: 22 + 11 = 33)

#### Binäre Subtraktion

Die binäre Subtraktion funktioniert analog zur dezimalen Subtraktion mit Borgen (Borrow) von höherwertigen Stellen.

> [!NOTE]
> **Subtraktionsregeln im Binärsystem**:
> - 0 - 0 = 0
> - 1 - 0 = 1
> - 1 - 1 = 0
> - 0 - 1 = 1 mit Borgen von 1 von der nächsthöheren Stelle
> - 10₂ - 1 = 1

> [!TIP]
> **Beispiel: 10110₂ - 01011₂**
> 
> ```
>   Borgen:      ¹ ¹
>              1 0 1 1 0
>            - 0 1 0 1 1
>            -----------
>              0 1 0 1 1
> ```
> 
> Ergebnis: **01011₂** (Dezimal: 22 - 11 = 11)

> [!WARNING]
> **Negative Ergebnisse**: Die einfache Subtraktion kann keine negativen Zahlen darstellen. Wenn der Subtrahend größer ist als der Minuend, benötigen wir ein System zur Darstellung negativer Zahlen. Dafür verwendet man in der Informatik das **Zweierkomplement**, das im nächsten Abschnitt behandelt wird.

### Negative Zahlen im Computer: Das Zweierkomplement

Computer müssen sowohl positive als auch negative Zahlen darstellen können. Das **Zweierkomplement** ist die Standardmethode zur Darstellung negativer Zahlen in Computern, weil es arithmetische Operationen extrem vereinfacht.

> [!NOTE]
> Das **Zweierkomplement** ist eine Methode zur Darstellung negativer ganzer Zahlen in binärer Form. Das höchstwertige Bit (MSB - Most Significant Bit) dient als Vorzeichenbit: 0 bedeutet positiv, 1 bedeutet negativ. Diese Darstellung ermöglicht es, Subtraktion als Addition mit negativen Zahlen durchzuführen, was die Hardware-Implementierung erheblich vereinfacht.

#### Bildung des Zweierkomplements

Um das Zweierkomplement einer Zahl zu bilden, gibt es zwei äquivalente Methoden:

**Methode 1: Invertieren und 1 addieren**
1. Invertiere alle Bits (0 → 1, 1 → 0)
2. Addiere 1 zum Ergebnis

**Methode 2: Von rechts lesen**
1. Kopiere alle Bits von rechts bis einschließlich der ersten 1
2. Invertiere alle übrigen Bits links davon

> [!TIP]
> **Beispiel: Zweierkomplement von 5 (bei 8 Bit)**
> 
> Positive Darstellung: 00000101₂
> 
> **Methode 1:**
> - Invertieren: 11111010₂
> - Plus 1: 11111011₂
> 
> **Ergebnis**: 11111011₂ repräsentiert **-5** im Zweierkomplement
> 
> **Probe**: 00000101₂ + 11111011₂ = 100000000₂
> 
> Der 9. Bit (Überlauf) wird ignoriert → 00000000₂ = 0 ✓

#### Wertebereich beim Zweierkomplement

Mit n Bits können im Zweierkomplement Zahlen von $-2^{n-1}$ bis $2^{n-1} - 1$ dargestellt werden.

> [!TIP]
> **Wertebereiche nach Bit-Anzahl**
> 
> | Bit-Anzahl | Von | Bis | Anzahl Werte |
> |------------|-----|-----|--------------|
> | 4 Bit | -8 | +7 | 16 |
> | 8 Bit | -128 | +127 | 256 |
> | 16 Bit | -32.768 | +32.767 | 65.536 |
> | 32 Bit | -2.147.483.648 | +2.147.483.647 | ~4,3 Mrd. |
> | 64 Bit | -9.223.372.036.854.775.808 | +9.223.372.036.854.775.807 | ~18,4 Trillionen |

> [!WARNING]
> **Integer Overflow**: Wenn das Ergebnis einer Operation den darstellbaren Wertebereich überschreitet, tritt ein **Überlauf** (Overflow) auf. Bei 8-Bit-Zahlen im Zweierkomplement würde 127 + 1 = -128 ergeben, was logisch falsch ist. Moderne Programmiersprachen wie Python verwenden automatisch größere Datentypen, aber in Sprachen wie C/C++ oder in Hardware-naher Programmierung muss der Programmierer explizit auf Überläufe achten.

### Praktische Anwendung: Bit-Masken und Bit-Manipulation

**Bit-Manipulation** bezeichnet Operationen auf einzelnen Bits oder Bit-Gruppen. Diese Techniken sind in der System-Programmierung, Embedded Systems und Performance-kritischen Anwendungen unverzichtbar.

> [!NOTE]
> Eine **Bit-Maske** ist ein Bitmuster, das verwendet wird, um bestimmte Bits zu isolieren, zu setzen oder zu löschen. Bit-Masken nutzen die logischen Bit-Operatoren AND, OR, XOR und NOT.

#### Bitweise Operatoren

Die wichtigsten bitweisen Operatoren sind:

- **AND (&)**: Beide Bits müssen 1 sein → Ergebnis 1
- **OR (|)**: Mindestens ein Bit muss 1 sein → Ergebnis 1
- **XOR (^)**: Genau ein Bit muss 1 sein → Ergebnis 1
- **NOT (~)**: Invertiert alle Bits
- **Left Shift (<<)**: Verschiebt Bits nach links (entspricht Multiplikation mit 2ⁿ)
- **Right Shift (>>)**: Verschiebt Bits nach rechts (entspricht Division durch 2ⁿ)

> [!TIP]
> **Beispiel: Typische Anwendungen von Bit-Operationen**
> 
> **1. Bestimmtes Bit prüfen (Bit n lesen)**
> ```
> Zahl:  10110110
> Maske: 00100000  (Bit 5 prüfen)
> AND:   00100000  → Bit 5 ist gesetzt
> ```
> 
> **2. Bestimmtes Bit setzen (Bit n auf 1 setzen)**
> ```
> Zahl:  10010110
> Maske: 00100000  (Bit 5 setzen)
> OR:    10110110  → Bit 5 ist jetzt 1
> ```
> 
> **3. Bestimmtes Bit löschen (Bit n auf 0 setzen)**
> ```
> Zahl:  10110110
> Maske: 11011111  (Bit 5 löschen, NOT von 00100000)
> AND:   10010110  → Bit 5 ist jetzt 0
> ```
> 
> **4. Bestimmtes Bit umschalten (Toggle)**
> ```
> Zahl:  10110110
> Maske: 00100000  (Bit 5 umschalten)
> XOR:   10010110  → Bit 5 ist umgekehrt
> ```

> [!TIP]
> **Beispiel: Shift-Operationen**
> 
> **Left Shift (Multiplikation)**
> ```
> 00001010₂ (10₁₀) << 2 = 00101000₂ (40₁₀)
> → Äquivalent zu: 10 × 2² = 10 × 4 = 40
> ```
> 
> **Right Shift (Division)**
> ```
> 00101000₂ (40₁₀) >> 2 = 00001010₂ (10₁₀)
> → Äquivalent zu: 40 ÷ 2² = 40 ÷ 4 = 10
> ```

> [!WARNING]
> **Vorzeichenbehaftete Right Shifts**: Bei vorzeichenbehafteten Zahlen (signed integers) gibt es zwei Arten von Right Shift:
> - **Logischer Shift**: Füllt links mit 0 auf
> - **Arithmetischer Shift**: Füllt links mit dem Vorzeichenbit auf (erhält das Vorzeichen)
> 
> In Python ist der Right Shift immer arithmetisch für negative Zahlen. In C/C++ hängt das Verhalten vom Compiler ab.

### Zusammenfassung Theorie

Das binäre Zahlensystem bildet die Grundlage der digitalen Datenverarbeitung. Computer arbeiten ausschließlich mit Bits (0 und 1), weil elektronische Schaltungen nur zwei stabile Zustände kennen. Die Umrechnung zwischen verschiedenen Stellenwertsystemen (binär, dezimal, hexadezimal, oktal) ist eine fundamentale Fähigkeit für jeden Informatiker. Besonders die Hexadezimal-Darstellung ist in der Praxis wichtig, da sie eine kompakte Schreibweise für Binärzahlen bietet.

Binäre Rechenoperationen funktionieren nach den gleichen Prinzipien wie im Dezimalsystem, nur mit der Basis 2. Das Zweierkomplement ist die Standardmethode zur Darstellung negativer Zahlen in Computern, da es arithmetische Operationen vereinfacht und keine separate Subtraktions-Hardware erfordert. Bit-Manipulation mit Masken und bitweisen Operatoren ist ein mächtiges Werkzeug für effiziente Programmierung, besonders in hardwarenahen Anwendungen.

---

## Teil 2: Python-Praxis - Python Get Started

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

Python ist eine der beliebtesten Programmiersprachen weltweit und besonders für Anfänger geeignet. Die Syntax ist klar und lesbar, was Python zur idealen Sprache für den Einstieg in die Programmierung macht. In dieser ersten Python-Lektion lernen wir die Grundlagen: Installation, erste Programme und die fundamentalen Konzepte Variablen, Ein- und Ausgabe.

Python wird in vielen Bereichen eingesetzt: Datenanalyse, Maschinelles Lernen, Webentwicklung, Automatisierung, wissenschaftliches Rechnen und vieles mehr. Als Maschinenbau-Ingenieur wirst du Python häufig für Berechnungen, Simulationen und Datenauswertung verwenden.

> [!NOTE]
> **Python** ist eine interpretierte, objektorientierte Hochsprache mit dynamischer Typisierung. "Interpretiert" bedeutet, dass Python-Code nicht kompiliert werden muss, sondern direkt ausgeführt wird. "Dynamische Typisierung" bedeutet, dass Variablen zur Laufzeit ihren Typ ändern können.

### Installation und Entwicklungsumgebungen

Bevor wir programmieren können, müssen wir Python installieren. Die aktuelle Version ist Python 3.12 (Stand Januar 2026). Python 2 ist veraltet und sollte nicht mehr verwendet werden.

#### Python installieren

**Windows:**
1. Besuche [python.org/downloads](https://python.org/downloads)
2. Lade den neuesten Python 3 Installer herunter
3. Führe den Installer aus und aktiviere die Option "Add Python to PATH"
4. Überprüfe die Installation mit `python --version` in der Kommandozeile

**macOS:**
Python 3 ist auf modernen macOS-Versionen vorinstalliert. Falls nicht, verwende Homebrew:
```bash
brew install python3
```

**Linux:**
Python 3 ist auf den meisten Linux-Distributionen vorinstalliert:
```bash
python3 --version
```

Falls nicht installiert:
```bash
sudo apt-get install python3  # Debian/Ubuntu
sudo dnf install python3      # Fedora
```

#### Entwicklungsumgebungen

Für die Programmierung in Python gibt es verschiedene Entwicklungsumgebungen (IDEs):

**IDLE** (Python's Integrated Development and Learning Environment)
- Kommt mit Python-Installation
- Einfach für Anfänger
- Begrenzte Funktionalität

**Visual Studio Code (VS Code)**
- Kostenloser, moderner Code-Editor von Microsoft
- Exzellente Python-Unterstützung mit Erweiterungen
- Empfohlen für diese Vorlesung

**PyCharm**
- Professionelle IDE speziell für Python
- Community Edition ist kostenlos
- Viele fortgeschrittene Features

**Jupyter Notebook**
- Interaktive Umgebung für Datenanalyse
- Mischt Code, Visualisierungen und Text
- Besonders für wissenschaftliche Anwendungen

> [!TIP]
> Für diese Vorlesung empfehlen wir **Visual Studio Code** mit der Python-Erweiterung. VS Code bietet eine gute Balance zwischen Einfachheit und Funktionalität.

### Erste Programme: Ausgabe mit print()

Das erste Programm, das man in jeder Programmiersprache schreibt, ist traditionell "Hello, World!". Es demonstriert die grundlegendste Funktionalität: Text ausgeben.

> [!NOTE]
> Die **print()**-Funktion gibt Text oder Werte auf der Konsole (Terminal) aus. Sie ist eine der wichtigsten Funktionen für Debugging und Benutzerkommunikation.

> [!TIP]
> **Beispiel: Das erste Python-Programm**
> 
> ```python
> # Das klassische "Hello, World!" Programm
> print("Hello, World!")
> ```
> 
> **Ausgabe:**
> ```
> Hello, World!
> ```

Die `print()`-Funktion kann verschiedene Datentypen ausgeben und mehrere Argumente verarbeiten:

> [!TIP]
> **Beispiel: Verschiedene Verwendungen von print()**
> 
> ```python
> # Text ausgeben
> print("Willkommen zur Informatik-Vorlesung!")
> 
> # Zahlen ausgeben
> print(42)
> print(3.14159)
> 
> # Mehrere Werte ausgeben (automatisch durch Leerzeichen getrennt)
> print("Die Antwort ist", 42)
> 
> # Berechnungen direkt ausgeben
> print("5 + 3 =", 5 + 3)
> 
> # Leere Zeile ausgeben
> print()
> ```
> 
> **Ausgabe:**
> ```
> Willkommen zur Informatik-Vorlesung!
> 42
> 3.14159
> Die Antwort ist 42
> 5 + 3 = 8
> 
> ```

> [!NOTE]
> **String (Zeichenkette)**: Ein String ist eine Sequenz von Zeichen, die in Anführungszeichen eingeschlossen ist. In Python können sowohl einfache (`'...'`) als auch doppelte (`"..."`) Anführungszeichen verwendet werden. Beide sind äquivalent, aber konsistente Verwendung verbessert die Lesbarkeit.

> [!WARNING]
> **Syntaxfehler bei fehlenden Anführungszeichen**: Wenn du Text ohne Anführungszeichen verwendest, interpretiert Python dies als Variablennamen oder Schlüsselwort. Dies führt zu einem Fehler:
> 
> ```python
> print(Hello)  # Fehler: NameError: name 'Hello' is not defined
> print("Hello")  # Korrekt
> ```

### Variablen deklarieren und zuweisen

**Variablen** sind benannte Speicherplätze im Arbeitsspeicher, die Werte aufnehmen können. Sie sind fundamental für jede Art von Programmierung, da sie es ermöglichen, Daten zu speichern und später wiederzuverwenden.

> [!NOTE]
> Eine **Variable** ist ein symbolischer Name für einen Wert im Speicher. In Python wird eine Variable durch Zuweisung mit dem Gleichheitszeichen (`=`) erstellt. Python verwendet **dynamische Typisierung**, was bedeutet, dass der Typ einer Variable automatisch aus dem zugewiesenen Wert abgeleitet wird.

> [!TIP]
> **Beispiel: Variablen erstellen und verwenden**
> 
> ```python
> # Variable mit Zahl erstellen
> alter = 25
> print("Ich bin", alter, "Jahre alt")
> 
> # Variable mit Text erstellen
> name = "Anna"
> print("Mein Name ist", name)
> 
> # Variable mit Kommazahl erstellen
> pi = 3.14159
> print("Pi ist ungefähr", pi)
> 
> # Variablen in Berechnungen verwenden
> radius = 5
> umfang = 2 * pi * radius
> print("Der Umfang eines Kreises mit Radius", radius, "ist", umfang)
> ```
> 
> **Ausgabe:**
> ```
> Ich bin 25 Jahre alt
> Mein Name ist Anna
> Pi ist ungefähr 3.14159
> Der Umfang eines Kreises mit Radius 5 ist 31.4159
> ```

#### Regeln für Variablennamen

Python hat klare Regeln und Konventionen für Variablennamen:

**Obligatorische Regeln (Syntaxvorgaben):**
- Namen dürfen nur Buchstaben (a-z, A-Z), Ziffern (0-9) und Unterstriche (_) enthalten
- Namen dürfen nicht mit einer Ziffer beginnen
- Namen dürfen keine Python-Schlüsselwörter sein (z.B. `if`, `for`, `while`, `def`)
- Groß- und Kleinschreibung wird unterschieden (`alter` ≠ `Alter`)

**Konventionen (PEP 8 - Python Style Guide):**
- Verwende aussagekräftige Namen: `geschwindigkeit` statt `g`
- Verwende `snake_case` für Variablennamen: `maximale_geschwindigkeit`
- Vermeide einzelne Buchstaben außer für Zähler (`i`, `j`, `k`) oder Koordinaten (`x`, `y`, `z`)
- Verwende englische Namen für Code, der geteilt wird

> [!TIP]
> **Beispiel: Gültige und ungültige Variablennamen**
> 
> ```python
> # Gültige Namen
> alter = 25
> max_geschwindigkeit = 120
> temperatur_celsius = 22.5
> istGueltig = True
> _internal_value = 42
> 
> # Ungültige Namen
> # 1alter = 25           # Fehler: beginnt mit Ziffer
> # max-geschwindigkeit = 120  # Fehler: Bindestrich nicht erlaubt
> # for = 5              # Fehler: 'for' ist ein Schlüsselwort
> # max geschwindigkeit = 120  # Fehler: Leerzeichen nicht erlaubt
> ```

> [!WARNING]
> **Überschreiben von Built-in-Namen**: Python hat vordefinierte Funktionen wie `print`, `len`, `sum` etc. Verwende diese Namen nicht als Variablen, da du sonst die ursprüngliche Funktion überschreibst:
> 
> ```python
> # Schlecht: Überschreibt die print-Funktion
> print = 42
> print("Hello")  # Fehler: 'int' object is not callable
> ```

#### Variablen neu zuweisen und überschreiben

Variablen können jederzeit neue Werte zugewiesen bekommen. Der alte Wert wird dabei überschrieben.

> [!TIP>
> **Beispiel: Variablen aktualisieren**
> 
> ```python
> # Variable erstellen
> zaehler = 0
> print("Zaehler:", zaehler)
> 
> # Wert ändern
> zaehler = 5
> print("Zaehler:", zaehler)
> 
> # Variable in ihrer eigenen Berechnung verwenden
> zaehler = zaehler + 1
> print("Zaehler:", zaehler)
> 
> # Kurzschreibweise für zaehler = zaehler + 1
> zaehler += 1
> print("Zaehler:", zaehler)
> ```
> 
> **Ausgabe:**
> ```
> Zaehler: 0
> Zaehler: 5
> Zaehler: 6
> Zaehler: 7
> ```

> [!NOTE]
> **Zuweisungsoperator vs. Gleichheit**: Das Gleichheitszeichen (`=`) ist in Python der **Zuweisungsoperator**, nicht das mathematische Gleichheitszeichen. `x = 5` bedeutet "weise der Variable x den Wert 5 zu", nicht "x ist gleich 5". Für Gleichheitsvergleiche verwendet man den `==` Operator (wird in V04 behandelt).

### Benutzereingaben mit input() einlesen

Programme werden erst dann wirklich nützlich, wenn sie mit Benutzern interagieren können. Die `input()`-Funktion ermöglicht es, Daten vom Benutzer einzulesen.

> [!NOTE]
> Die **input()**-Funktion pausiert die Programmausführung und wartet auf eine Eingabe des Benutzers. Der Benutzer tippt Text ein und bestätigt mit Enter. Die Funktion gibt den eingegebenen Text als String zurück.

> [!TIP]
> **Beispiel: Einfache Benutzereingabe**
> 
> ```python
> # Benutzer nach seinem Namen fragen
> name = input("Wie ist dein Name? ")
> print("Hallo", name, "!")
> 
> # Benutzer nach seinem Alter fragen
> alter = input("Wie alt bist du? ")
> print("Du bist", alter, "Jahre alt.")
> ```
> 
> **Interaktion:**
> ```
> Wie ist dein Name? Max
> Hallo Max !
> Wie alt bist du? 22
> Du bist 22 Jahre alt.
> ```

> [!WARNING]
> **input() gibt immer einen String zurück**: Auch wenn der Benutzer eine Zahl eingibt, wird diese als String (Text) zurückgegeben. Für Berechnungen muss der String in eine Zahl konvertiert werden:
> 
> ```python
> # Falsch: Versucht, Strings zu addieren
> zahl1 = input("Erste Zahl: ")  # Benutzer gibt "5" ein
> zahl2 = input("Zweite Zahl: ") # Benutzer gibt "3" ein
> summe = zahl1 + zahl2
> print("Summe:", summe)  # Ausgabe: "53" statt 8!
> 
> # Richtig: Konvertierung in Ganzzahl
> zahl1 = int(input("Erste Zahl: "))  # "5" wird zu 5
> zahl2 = int(input("Zweite Zahl: "))  # "3" wird zu 3
> summe = zahl1 + zahl2
> print("Summe:", summe)  # Ausgabe: 8
> ```

> [!NOTE]
> **Type Casting (Typkonvertierung)**: Python bietet Funktionen zur Konvertierung zwischen Datentypen:
> - `int()` konvertiert zu Ganzzahl (Integer)
> - `float()` konvertiert zu Fließkommazahl
> - `str()` konvertiert zu String (Text)
> 
> Diese Funktionen werden ausführlich in V03 behandelt.

> [!TIP]
> **Beispiel: Praktisches Programm mit Eingabe und Berechnung**
> 
> ```python
> # Programm zur Berechnung der Kreisfläche
> print("=== Kreisflächen-Rechner ===")
> 
> # Radius vom Benutzer einlesen
> radius_text = input("Gib den Radius in cm ein: ")
> radius = float(radius_text)  # String in Fließkommazahl umwandeln
> 
> # Fläche berechnen
> pi = 3.14159
> flaeche = pi * radius * radius
> 
> # Ergebnis ausgeben
> print("Ein Kreis mit Radius", radius, "cm hat eine Fläche von", flaeche, "cm²")
> ```
> 
> **Interaktion:**
> ```
> === Kreisflächen-Rechner ===
> Gib den Radius in cm ein: 5
> Ein Kreis mit Radius 5.0 cm hat eine Fläche von 78.53975 cm²
> ```

### Kommentare für lesbaren Code

**Kommentare** sind Textzeilen im Code, die vom Python-Interpreter ignoriert werden. Sie dienen ausschließlich der Dokumentation und helfen Menschen, den Code zu verstehen.

> [!NOTE]
> **Kommentare** sind Erklärungen im Code für menschliche Leser, die von Python nicht ausgeführt werden. Einzeilige Kommentare beginnen mit `#`, mehrzeilige Kommentare werden mit dreifachen Anführungszeichen (`"""..."""` oder `'''...'''`) erstellt.

> [!TIP]
> **Beispiel: Verschiedene Arten von Kommentaren**
> 
> ```python
> # Dies ist ein einzeiliger Kommentar
> 
> # Kommentare können verwendet werden, um Code zu erklären
> geschwindigkeit = 100  # in km/h
> 
> # Kommentare können auch Code temporär deaktivieren
> # print("Diese Zeile wird nicht ausgeführt")
> 
> # Mehrzeiliger Kommentar (Docstring)
> """
> Dies ist ein mehrzeiliger Kommentar.
> Er kann sich über mehrere Zeilen erstrecken.
> Wird häufig für Dokumentation am Anfang von Dateien oder Funktionen verwendet.
> """
> 
> # Praktisches Beispiel mit Kommentaren
> # Berechnung der Beschleunigungszeit
> v_end = 100      # Endgeschwindigkeit in km/h
> v_start = 0      # Startgeschwindigkeit in km/h
> a = 3.5          # Beschleunigung in m/s²
> 
> # Umrechnung km/h in m/s: durch 3.6 teilen
> v_end_ms = v_end / 3.6
> v_start_ms = v_start / 3.6
> 
> # Zeit berechnen: t = (v_end - v_start) / a
> zeit = (v_end_ms - v_start_ms) / a
> 
> print("Beschleunigungszeit:", zeit, "Sekunden")
> ```

> [!WARNING]
> **Kommentare sinnvoll einsetzen**: Kommentare sollten erklären **warum** etwas getan wird, nicht **was** getan wird (das sieht man am Code). Schlechte Kommentare sind redundant oder veraltet:
> 
> ```python
> # Schlecht: Kommentar beschreibt nur, was offensichtlich ist
> x = 5  # setze x auf 5
> 
> # Gut: Kommentar erklärt den Zweck oder Kontext
> x = 5  # maximale Anzahl an Wiederholungsversuchen
> 
> # Schlecht: Veralteter Kommentar (Code wurde geändert, Kommentar nicht)
> # Berechne die Summe
> produkt = a * b  # Das ist jetzt ein Produkt, nicht eine Summe!
> 
> # Gut: Kommentar erklärt unklare Logik
> # Teile durch 3.6, um km/h in m/s umzurechnen (1 km/h = 1000m/3600s = 1/3.6 m/s)
> geschwindigkeit_ms = geschwindigkeit_kmh / 3.6
> ```

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: Fehlende Anführungszeichen bei Strings**
> 
> ```python
> # Falsch
> print(Hallo Welt)  # NameError: name 'Hallo' is not defined
> 
> # Richtig
> print("Hallo Welt")
> ```
> 
> **Lösung**: Strings müssen immer in Anführungszeichen stehen.

> [!WARNING]
> **Fehler 2: Variablenname mit Ziffer beginnen**
> 
> ```python
> # Falsch
> 1_wert = 42  # SyntaxError: invalid syntax
> 
> # Richtig
> wert_1 = 42
> wert1 = 42
> ```
> 
> **Lösung**: Variablennamen dürfen nicht mit einer Ziffer beginnen.

> [!WARNING]
> **Fehler 3: Vergessen, input() in Zahl zu konvertieren**
> 
> ```python
> # Falsch
> alter = input("Alter: ")  # Benutzer gibt "25" ein
> in_fuenf_jahren = alter + 5  # TypeError: can only concatenate str (not "int") to str
> 
> # Richtig
> alter = int(input("Alter: "))
> in_fuenf_jahren = alter + 5
> print("In 5 Jahren bist du", in_fuenf_jahren, "Jahre alt")
> ```
> 
> **Lösung**: Verwende `int()` oder `float()` um Eingaben in Zahlen zu konvertieren.

> [!WARNING]
> **Fehler 4: Variablen vor der Zuweisung verwenden**
> 
> ```python
> # Falsch
> print(ergebnis)  # NameError: name 'ergebnis' is not defined
> ergebnis = 42
> 
> # Richtig
> ergebnis = 42
> print(ergebnis)
> ```
> 
> **Lösung**: Variablen müssen vor ihrer Verwendung einen Wert zugewiesen bekommen haben.

> [!WARNING]
> **Fehler 5: Tippfehler bei Variablennamen**
> 
> ```python
> # Falsch
> geschwindigkeit = 100
> print(geschwindigkiet)  # NameError: name 'geschwindigkiet' is not defined
> 
> # Richtig
> geschwindigkeit = 100
> print(geschwindigkeit)
> ```
> 
> **Lösung**: Achte auf exakte Schreibweise. Moderne IDEs wie VS Code markieren unbekannte Variablennamen.

### Zusammenfassung Python

Python ist eine anfängerfreundliche, aber mächtige Programmiersprache, die in vielen Bereichen eingesetzt wird. Die Installation ist einfach, und moderne IDEs wie Visual Studio Code bieten exzellente Unterstützung. Die `print()`-Funktion ermöglicht Ausgaben auf der Konsole und ist essentiell für Debugging und Benutzerinteraktion.

Variablen sind benannte Speicherplätze, die Werte aufnehmen können. Python verwendet dynamische Typisierung, sodass Variablentypen automatisch erkannt werden. Variablennamen müssen bestimmte Regeln befolgen und sollten aussagekräftig gewählt werden. Die `input()`-Funktion liest Benutzereingaben als String ein. Für numerische Berechnungen muss der String mit `int()` oder `float()` konvertiert werden.

Kommentare dokumentieren Code für menschliche Leser und werden von Python ignoriert. Gute Kommentare erklären das "Warum", nicht das "Was". Sie sind essentiell für wartbaren, verständlichen Code, besonders in Team-Projekten.

### Neue Python-Funktionen/Methoden

Die folgenden Python-Funktionen und Konzepte wurden in dieser Lektion **erstmals eingeführt**:

#### Built-in Functions
- **`print(*objects, sep=' ', end='\n')`** (Python 3.0+)
  - Gibt Werte auf der Standardausgabe (Konsole) aus
  - Mehrere Argumente werden durch `sep` (Standard: Leerzeichen) getrennt
  - Nach der Ausgabe wird `end` angehängt (Standard: Zeilenumbruch)

- **`input(prompt='')`** (Python 3.0+)
  - Liest eine Zeile Text von der Standardeingabe (Tastatur)
  - Zeigt optional einen Prompt-Text an
  - Gibt immer einen String zurück

- **`int(x)`** (Built-in)
  - Konvertiert einen Wert in eine Ganzzahl (Integer)
  - Kann Strings und Floats konvertieren
  - Wirft `ValueError` bei ungültiger Konvertierung

- **`float(x)`** (Built-in)
  - Konvertiert einen Wert in eine Fließkommazahl
  - Kann Strings und Integers konvertieren
  - Wirft `ValueError` bei ungültiger Konvertierung

- **`str(x)`** (Built-in)
  - Konvertiert einen Wert in einen String
  - Funktioniert mit fast allen Datentypen

#### Operatoren
- **Zuweisungsoperator `=`**
  - Weist einer Variable einen Wert zu
  - Links steht der Variablenname, rechts der Wert

- **Zusammengesetzte Zuweisungsoperatoren: `+=`, `-=`, `*=`, `/=`**
  - Kurzschreibweise für `x = x + y` → `x += y`
  - Funktioniert mit allen arithmetischen Operatoren

#### Konzepte
- **Variablen**: Benannte Speicherplätze für Werte
- **Dynamische Typisierung**: Typ wird automatisch aus dem Wert abgeleitet
- **Kommentare**: `#` für einzeilige, `"""..."""` für mehrzeilige Kommentare

---

## Weiterführende Ressourcen

### Theorie

**Bücher und Online-Ressourcen:**
- *Code: The Hidden Language of Computer Hardware and Software* von Charles Petzold - Exzellente Einführung in binäre Systeme und Computer-Grundlagen
- Khan Academy: [Computer Science - How Computers Work](https://www.khanacademy.org/computing/computer-science) - Interaktive Lektionen zu Binärsystem und Computern
- [Binary Tutorial (Stanford CS)](https://web.stanford.edu/class/cs101/bits-bytes.html) - Ausführliches Stanford-Tutorial zu Bits und Bytes

**Interaktive Tools:**
- [RapidTables Binary Calculator](https://www.rapidtables.com/calc/math/binary-calculator.html) - Online-Rechner für binäre Operationen
- [Binary Game](https://learningcontent.cisco.com/games/binary/index.html) - Spielerisches Lernen der Binär-Dezimal-Umrechnung
- [IEEE 754 Visualizer](https://www.h-schmidt.net/FloatConverter/IEEE754.html) - Visualisierung von Fließkommazahlen (Vorbereitung auf V02)

### Python

**Offizielle Dokumentation:**
- [Python Official Tutorial](https://docs.python.org/3/tutorial/) - Das offizielle Python-Tutorial
- [Python Built-in Functions](https://docs.python.org/3/library/functions.html) - Dokumentation aller Built-in-Funktionen

**Interaktive Lernplattformen:**
- [Python Tutor](http://pythontutor.com/) - Visualisiert Schritt-für-Schritt, was im Speicher passiert
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3) - Interaktives Python-Tutorial
- [Real Python Tutorials](https://realpython.com/) - Hochwertige Python-Tutorials für alle Levels

**Bücher für Anfänger:**
- *Python Crash Course* von Eric Matthes - Praktische Einführung mit Projekten
- *Automate the Boring Stuff with Python* von Al Sweigart - Python für Automatisierung (kostenlos online verfügbar)

**YouTube-Kanäle:**
- [Corey Schafer](https://www.youtube.com/user/schafer5) - Exzellente Python-Tutorials
- [Programming with Mosh](https://www.youtube.com/c/programmingwithmosh) - Anfängerfreundliche Python-Videos
