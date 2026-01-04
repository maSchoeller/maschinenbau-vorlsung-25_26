# V08: Übungsaufgaben - Listen und Datenstrukturen – Teil 1

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V08.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Zeitkomplexität vergleichen (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10 Minuten

Betrachte folgende Datenstrukturen: **Array**, **Einfach verkettete Liste** und **Doppelt verkettete Liste**.

Erstelle eine Tabelle, die für jede Datenstruktur die Zeitkomplexität der folgenden Operationen angibt:
1. Zugriff auf das Element an Index i
2. Suchen eines bestimmten Werts
3. Einfügen eines Elements am Anfang
4. Einfügen eines Elements am Ende (mit Tail-Pointer bei Listen)
5. Löschen des ersten Elements
6. Löschen des letzten Elements (mit Tail-Pointer bei doppelt verketteter Liste)

Verwende die O-Notation (z.B. O(1), O(n)).

**Hinweise**:
- Bei verketteten Listen gehen wir von einem vorhandenen Tail-Pointer aus (Verweis auf letztes Element)
- Beachte den Unterschied zwischen einfach und doppelt verketteten Listen beim Löschen am Ende

---

### Aufgabe T2: Stack-Anwendungsfall analysieren (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Ein Compiler muss prüfen, ob in einem Quellcode alle Klammern korrekt geschlossen sind. Dabei werden drei Klammertypen verwendet: runde `()`, eckige `[]` und geschweifte `{}`.

**Teilaufgabe a)**: Erkläre in eigenen Worten, warum ein **Stack** die ideale Datenstruktur für diese Aufgabe ist. Welche Stack-Operationen werden benötigt?

**Teilaufgabe b)**: Beschreibe den Algorithmus in Pseudocode oder Schritten. Wie entscheidest du, ob die Klammern korrekt sind?

**Teilaufgabe c)**: Zeige, wie der Stack sich bei der Verarbeitung des Ausdrucks `{[()]}` entwickelt (Push und Pop Operationen).

**Beispiele für korrekte Ausdrücke:**
- `()`
- `{[()]}`
- `([]{})[]`

**Beispiele für inkorrekte Ausdrücke:**
- `([)]` (falsche Reihenfolge)
- `{[(])}` (falsche Verschachtelung)
- `((())` (nicht alle geschlossen)

**Hinweise**:
- Überlege, was beim Öffnen einer Klammer passiert
- Überlege, was beim Schließen einer Klammer passiert
- Was bedeutet es, wenn der Stack am Ende nicht leer ist?

---

### Aufgabe T3: Queue-Implementierung mit Array (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 20-30 Minuten

Eine Queue kann mit einem Array implementiert werden. Ein einfacher Ansatz würde das Ende des Arrays für Enqueue verwenden und den Anfang für Dequeue. Dies ist ineffizient, da bei jedem Dequeue alle Elemente verschoben werden müssen.

**Teilaufgabe a)**: Erkläre das Problem dieser naiven Implementierung im Detail. Welche Zeitkomplexität hat Dequeue?

**Teilaufgabe b)**: Beschreibe die Lösung: **Zirkuläres Array (Ringpuffer)**. Erkläre, wie zwei Zeiger (Front und Rear) verwendet werden, um die Queue im Array zu verwalten.

**Teilaufgabe c)**: Gegeben sei ein Array der Größe 6. Die Queue-Operationen sind:
1. Enqueue(A)
2. Enqueue(B)
3. Enqueue(C)
4. Dequeue() → gibt A zurück
5. Dequeue() → gibt B zurück
6. Enqueue(D)
7. Enqueue(E)
8. Enqueue(F)
9. Enqueue(G)

Zeichne für jeden Schritt den Zustand des Arrays sowie die Positionen von Front und Rear. Verwende Modulo-Arithmetik, um die zirkuläre Natur zu zeigen.

**Teilaufgabe d)**: Wie unterscheidest du zwischen einer leeren Queue und einer vollen Queue, wenn beide durch `Front == Rear` charakterisiert sein könnten?

**Hinweise**:
- Bei einem zirkulären Array "wickelt" sich der Index beim Erreichen des Endes zurück an den Anfang
- Formel: `neuer_index = (alter_index + 1) % array_groesse`
- Es gibt verschiedene Ansätze zur Unterscheidung von leer/voll: Zähler-Variable, ein Platz bleibt ungenutzt, oder Flag

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Sensor-Messwerte-Erfassung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Listen erstellen, indexieren, `.append()`, `.insert()`, `.remove()`  
**Maschinenbau-Kontext**: Erfassung und Verwaltung von Sensor-Messwerten in Echtzeit

Schreibe ein Python-Programm zur **kontinuierlichen Erfassung von Temperatursensor-Daten** an einer Produktionsmaschine.

> [!NOTE]
> **Sensor-Datenerfassung**: In Produktionsanlagen erfassen Temperatursensoren kontinuierlich Betriebstemperaturen. Kritische Überwachung ist notwendig für:
> - Motortemperaturen (60-90°C normal, >100°C kritisch)
> - Lagertemperaturen (40-70°C normal)
> - Kühlmitteltemperaturen (15-25°C optimal)

**Aufgabe**:
Das Programm soll:
1. Eine leere Liste `temperaturen` erstellen
2. Benutzer-Eingaben (Temperaturwerte in °C) in einer Schleife einlesen und zur Liste hinzufügen
3. Eingabe "STOP" beendet die Erfassung
4. Nach jeder Eingabe die aktuelle Messwert-Liste ausgibt
5. Am Ende die Anzahl der Messwerte anzeigt
6. Prüft, ob kritische Temperaturen (>100°C) erfasst wurden und eine Warnung ausgibt

**Beispiel Ein-/Ausgabe**:
```
Temperatur eingeben (oder 'STOP'): 85.5
Messwerte: [85.5]
Temperatur eingeben (oder 'STOP'): 92.3
Messwerte: [85.5, 92.3]
Temperatur eingeben (oder 'STOP'): 78.1
Messwerte: [85.5, 92.3, 78.1]
Temperatur eingeben (oder 'STOP'): 105.2
Messwerte: [85.5, 92.3, 78.1, 105.2]
Temperatur eingeben (oder 'STOP'): STOP

═══════════════════════════════════
Erfassung beendet.
Gesamtanzahl: 4 Messwerte
⚠️  WARNUNG: Kritische Temperatur erfasst! (>100°C)
Maßnahme: Kühlung prüfen, Maschine ggf. abschalten
```

**Hinweise**:
- Verwende eine `while`-Schleife für die Eingabe
- Konvertiere Eingabe mit `float()` zu Dezimalzahl
- Nutze `any([t > 100 for t in temperaturen])` oder Schleife für kritische Temperatur-Prüfung

---

### Aufgabe P2: Vibrationsdaten-Analyse für Predictive Maintenance (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Listen, Schleifen, `.sort()`, `sorted()`, List Comprehensions  
**Maschinenbau-Kontext**: Schwingungsanalyse zur Früherkennung von Lagerschäden

Gegeben ist eine Liste von **Vibrations-Messwerten** (Beschleunigung in m/s²) eines Lagers:
```python
vibrationen = [2.5, 8.3, 5.1, 9.8, 3.7, 7.2, 12.4, 4.9, 6.5, 10.3]
```

> [!NOTE]
> **Vibrations-Monitoring**: Lager und Wellen erzeugen charakteristische Schwingungen. Erhöhte Vibrationen deuten auf Verschleiß, Unwucht oder Lagerschäden hin:
> - Normal: < 7 m/s²
> - Erhöht: 7-10 m/s²
> - Kritisch: > 10 m/s²

**Aufgabe**:
Schreibe ein Programm, das:
1. Die höchste und niedrigste Vibration findet und ausgibt
2. Die durchschnittliche Vibration berechnet und ausgibt
3. Alle kritischen Werte (>10 m/s²) in einer neuen Liste `kritisch` speichert (verwende List Comprehension)
4. Alle normalen Werte (<7 m/s²) in einer neuen Liste `normal` speichert (verwende List Comprehension)
5. Alle erhöhten Werte (7-10 m/s²) in einer Liste `erhoeht` speichert
6. Alle drei Listen sortiert ausgibt
7. Die ursprüngliche Liste sortiert (in-place) und ausgibt

**Erwartete Ausgabe (ungefähr)**:
```
═══════════════════════════════════
  Vibrations-Analyse - Lager #42
═══════════════════════════════════
Max. Vibration: 12.4 m/s²
Min. Vibration: 2.5 m/s²
Durchschnitt: 7.1 m/s²

⚠️  Kritische Werte (>10 m/s²): [10.3, 12.4]
🟡 Erhöhte Werte (7-10 m/s²): [7.2, 8.3, 9.8]
✅ Normale Werte (<7 m/s²): [2.5, 3.7, 4.9, 5.1, 6.5]

BEWERTUNG: ❌ LAGER KRITISCH
Empfehlung: Wartung einplanen, Lager austauschen
```

**Hinweise**:
- `max()` und `min()` für Extremwerte
- `sum()` und `len()` für Durchschnitt
- List Comprehensions mit Bedingung: `[x for x in liste if bedingung]`
- Für erhöhte Werte: `[x for x in liste if 7 <= x <= 10]`
- `sorted()` für neue sortierte Liste, `.sort()` für in-place Sortierung

---

### Aufgabe P3: NC-Programm-Validator mit Stack (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-30 Minuten  
**Vorkenntnisse**: Listen als Stack, `.append()`, `.pop()`, Schleifen, Verzweigungen  
**Maschinenbau-Kontext**: Validierung von CNC-Programm-Strukturen (Schleifen, Unterprogramme)

Implementiere einen **NC-Programm-Validator**, der die Struktur von CNC-Programmen prüft.

> [!NOTE]
> **CNC-Programmstruktur**: CNC-Programme (G-Code) verwenden strukturierte Blöcke:
> - Schleifen: `L10` ... `L11` (Loop Start/End)
> - Unterprogramme: `P100` ... `P101` (Program Call/Return)
> - Bedingungen: `IF` ... `ENDIF`
> - Korrekte Verschachtelung ist essentiell für fehlerfreie Ausführung

**Aufgabe**:
Schreibe eine Funktion `nc_struktur_gueltig(programm)`, die:
- Einen String mit NC-Struktur-Befehlen als Parameter erhält
- `True` zurückgibt, wenn alle Blöcke korrekt verschachtelt sind
- `False` zurückgibt, wenn Blöcke falsch verschachtelt, nicht geschlossen oder in falscher Reihenfolge sind
- Eine Python-Liste als Stack verwendet

**Struktur-Befehle**:
- Öffnende Befehle: `L10` (Loop), `P100` (Program), `IF` (Condition)
- Schließende Befehle: `L11` (End Loop), `P101` (End Program), `ENDIF` (End Condition)

**Algorithmus**:
1. Erstelle einen leeren Stack (Liste)
2. Durchlaufe jeden Befehl im Programm
3. Bei öffnendem Befehl: Push auf Stack
4. Bei schließendem Befehl:
   - Wenn Stack leer: Return `False`
   - Pop vom Stack und prüfe, ob die Befehlstypen zusammenpassen
   - Wenn nicht: Return `False`
5. Am Ende: Stack muss leer sein (alle Blöcke geschlossen)

**Testfälle**:
```python
print(nc_struktur_gueltig(["L10", "L11"]))                    # True
print(nc_struktur_gueltig(["L10", "P100", "P101", "L11"]))    # True
print(nc_struktur_gueltig(["IF", "L10", "L11", "ENDIF"]))     # True
print(nc_struktur_gueltig(["L10", "IF", "ENDIF", "L11"]))     # True
print(nc_struktur_gueltig(["L10", "P100", "L11", "P101"]))    # False (falsche Reihenfolge)
print(nc_struktur_gueltig(["L10", "IF", "L11", "ENDIF"]))     # False (falsche Verschachtelung)
print(nc_struktur_gueltig(["L10", "L10", "L11"]))             # False (nicht alle geschlossen)
print(nc_struktur_gueltig(["L11"]))                           # False (nur schließend)
print(nc_struktur_gueltig([]))                                # True (leer ist gültig)
```

**Hinweise**:
- Definiere Dictionary für passende Paare: `paare = {'L11': 'L10', 'P101': 'P100', 'ENDIF': 'IF'}`
- Prüfe auf öffnende Befehle: `befehl in ['L10', 'P100', 'IF']`
- Prüfe auf schließende Befehle: `befehl in ['L11', 'P101', 'ENDIF']`
- Verwende `.append()` für Push und `.pop()` für Pop

---

### Aufgabe P4: Materialprüfungs-Datenbank (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Slicing, List Comprehensions, `zip()`, Unpacking  
**Maschinenbau-Kontext**: Verwaltung und Analyse von Materialprüfungs-Daten

Schreibe ein Programm zur Verwaltung von **Zugversuchs-Ergebnissen** verschiedener Materialproben.

**Teilaufgabe a)**: Erstelle drei Listen:
```python
proben_ids = ["S235-001", "AlMg3-002", "X5CrNi-003", "S235-004", "AlMg3-005"]
zugfestigkeit = [360, 250, 520, 370, 245]  # in MPa
streckgrenze = [235, 180, 210, 240, 175]   # in MPa
```

**Teilaufgabe b)**: Implementiere folgende Funktionen:

1. `durchschnitt(werte)`: Berechnet den Durchschnitt einer Werteliste
   
2. `beste_drei(proben, werte)`: Gibt die IDs der drei besten Proben zurück (höchste Werte)
   - **Hinweis**: Verwende `zip()`, `sorted()` mit `key`-Parameter (absteigend!), und Slicing
   
3. `materialklassifikation(zugfestigkeiten)`: Zählt Materialien in Festigkeitsklassen:
   - Niedrig: < 300 MPa
   - Mittel: 300-450 MPa
   - Hoch: 450-600 MPa
   - Sehr hoch: > 600 MPa
   - Gibt Dictionary zurück: `{'Niedrig': 2, 'Mittel': 2, ...}`

4. `verhaeltnis_berechnen(zugfest, streck)`: Berechnet für jede Probe das Verhältnis Zugfestigkeit/Streckgrenze
   - **Hinweis**: Verwende `zip()` und List Comprehension

**Teilaufgabe c)**: Verwende die Funktionen und gib aus:
```
═══════════════════════════════════
  Materialprüfungs-Datenbank
═══════════════════════════════════
Ø Zugfestigkeit: 349.0 MPa
Ø Streckgrenze: 208.0 MPa

Top 3 Zugfestigkeit: ['X5CrNi-003', 'S235-004', 'S235-001']
Top 3 Streckgrenze: ['S235-004', 'S235-001', 'X5CrNi-003']

Festigkeitsklassifikation:
  Niedrig: 2
  Mittel: 2
  Hoch: 1
  Sehr hoch: 0

Verhältnis Rm/Re (Verfestigungspotential):
  S235-001: 1.53
  AlMg3-002: 1.39
  X5CrNi-003: 2.48
  S235-004: 1.54
  AlMg3-005: 1.40
```

**Hinweise**:
- Bei `beste_drei()`: `sorted(zip(proben, werte), key=lambda x: x[1], reverse=True)[:3]`
- Bei `materialklassifikation()`: Nutze Bedingungen und zähle mit Dictionary
- `round(wert, 2)` für Rundung auf 2 Dezimalstellen

---

### Aufgabe P5: CNC-Programm-Editor mit Undo/Redo (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Listen als Stack, Funktionen, String-Manipulation  
**Maschinenbau-Kontext**: Vereinfachter NC-Code-Editor mit Historie-Verwaltung

Implementiere ein vereinfachtes **Undo/Redo-System** für einen NC-Code-Editor mit zwei Stacks.

> [!NOTE]
> **NC-Code-Editor**: Professionelle CNC-Steuerungen bieten Undo/Redo für Programmänderungen. Dies verhindert Fehler beim Editieren von teuren Bearbeitungsprogrammen. Jede Zeile entspricht einem NC-Befehl (z.B. `G01 X100 Y50 F500`).

**Anforderungen**:

1. Das System verwaltet eine NC-Code-Zeile (String)
2. Unterstützte Operationen:
   - `befehl_hinzufuegen(code)`: Fügt NC-Befehl am Ende hinzu
   - `zeichen_loeschen(anzahl)`: Löscht die letzten `anzahl` Zeichen
   - `undo()`: Macht die letzte Operation rückgängig
   - `redo()`: Stellt die letzte rückgängig gemachte Operation wieder her
   - `anzeigen()`: Zeigt den aktuellen NC-Code

3. Verwende zwei Stacks:
   - `undo_stack`: Speichert alle Zustände (Historie)
   - `redo_stack`: Speichert rückgängig gemachte Zustände

**Implementierung**:

Erstelle folgende Funktionen (verwende globale Listen für die Stacks):

```python
# Globale Variablen
nc_code = ""
undo_stack = []
redo_stack = []

def speichere_zustand():
    """Speichert den aktuellen Zustand im Undo-Stack."""
    # Implementierung

def befehl_hinzufuegen(code):
    """Fügt NC-Befehl hinzu."""
    # Implementierung

def zeichen_loeschen(anzahl):
    """Löscht die letzten 'anzahl' Zeichen."""
    # Implementierung

def undo():
    """Macht die letzte Änderung rückgängig."""
    # Implementierung

def redo():
    """Stellt die letzte rückgängig gemachte Änderung wieder her."""
    # Implementierung

def anzeigen():
    """Zeigt den aktuellen NC-Code."""
    # Implementierung
```

**Testprogramm**:
```python
befehl_hinzufuegen("G01 X100")
anzeigen()  # "G01 X100"

befehl_hinzufuegen(" Y50")
anzeigen()  # "G01 X100 Y50"

zeichen_loeschen(4)
anzeigen()  # "G01 X100"

undo()
anzeigen()  # "G01 X100 Y50"

undo()
anzeigen()  # "G01 X100"

redo()
anzeigen()  # "G01 X100 Y50"

befehl_hinzufuegen(" F500")
anzeigen()  # "G01 X100 Y50 F500"

undo()
anzeigen()  # "G01 X100 Y50"
```

**Algorithmus-Logik**:

- **Vor jeder Änderung**: Speichere aktuellen Zustand in `undo_stack`, leere `redo_stack` (neue Änderung macht Redo ungültig)
- **Bei Undo**: 
  1. Speichere aktuellen Zustand in `redo_stack`
  2. Pop vom `undo_stack` und stelle diesen Zustand wieder her
- **Bei Redo**:
  1. Speichere aktuellen Zustand in `undo_stack`
  2. Pop vom `redo_stack` und stelle diesen Zustand wieder her

**Hinweise**:
- Prüfe bei Undo/Redo, ob die jeweiligen Stacks leer sind
- Bei `zeichen_loeschen()`: Prüfe, ob genug Zeichen vorhanden sind
- Der `redo_stack` wird bei neuen Änderungen geleert: `redo_stack.clear()`

**Bonus-Challenge** (optional):
Erweitere das System um:
1. `anzeige_historie()`: Zeigt alle Zustände im Undo-Stack
2. Beschränke die Undo-Historie auf maximal 10 Einträge (FIFO: älteste wird entfernt)
3. Füge eine `befehl_ersetzen(alt, neu)`-Funktion hinzu, die alle Vorkommen von `alt` durch `neu` ersetzt

---

einfuegen("!")
anzeigen()  # "Hallo Welt!"

undo()
anzeigen()  # "Hallo Welt"
```

**Algorithmus-Logik**:

- **Vor jeder Änderung**: Speichere aktuellen Zustand in `undo_stack`, leere `redo_stack` (neue Änderung macht Redo ungültig)
- **Bei Undo**: 
  1. Speichere aktuellen Zustand in `redo_stack`
  2. Pop vom `undo_stack` und stelle diesen Zustand wieder her
- **Bei Redo**:
  1. Speichere aktuellen Zustand in `undo_stack`
  2. Pop vom `redo_stack` und stelle diesen Zustand wieder her

**Hinweise**:
- Prüfe bei Undo/Redo, ob die jeweiligen Stacks leer sind
- Bei `loeschen()`: Prüfe, ob genug Zeichen vorhanden sind
- Der `redo_stack` wird bei neuen Änderungen geleert: `redo_stack.clear()`

**Bonus-Challenge** (optional):
Erweitere das System um:
1. `anzeige_historie()`: Zeigt alle Zustände im Undo-Stack
2. Beschränke die Undo-Historie auf maximal 10 Einträge (FIFO: älteste wird entfernt)
3. Füge eine `ersetzen(alt, neu)`-Funktion hinzu, die alle Vorkommen von `alt` durch `neu` ersetzt

---

