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

### Aufgabe P1: Listen-Grundlagen (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Listen erstellen, indexieren, `.append()`, `.insert()`, `.remove()`

Schreibe ein Python-Programm, das:
1. Eine leere Liste `einkaufsliste` erstellt
2. Die Benutzer-Eingabe in einer Schleife einliest und zur Liste hinzufügt, bis "fertig" eingegeben wird
3. Nach jeder Eingabe die aktuelle Liste ausgibt
4. Am Ende die Anzahl der Artikel anzeigt
5. Prüft, ob "Milch" auf der Liste steht und eine entsprechende Nachricht ausgibt

**Beispiel Ein-/Ausgabe**:
```
Artikel eingeben (oder 'fertig' zum Beenden): Brot
Einkaufsliste: ['Brot']
Artikel eingeben (oder 'fertig' zum Beenden): Milch
Einkaufsliste: ['Brot', 'Milch']
Artikel eingeben (oder 'fertig' zum Beenden): Käse
Einkaufsliste: ['Brot', 'Milch', 'Käse']
Artikel eingeben (oder 'fertig' zum Beenden): fertig

Gesamtanzahl: 3 Artikel
Milch ist auf der Liste!
```

**Hinweise**:
- Verwende eine `while`-Schleife für die Eingabe
- Nutze den `in`-Operator für die Milch-Prüfung

---

### Aufgabe P2: Listen sortieren und filtern (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Listen, Schleifen, `.sort()`, `sorted()`, List Comprehensions

Gegeben ist eine Liste von Messwerten (Temperaturen in °C):
```python
temperaturen = [22.5, 18.3, 25.1, 19.8, 23.7, 17.2, 26.4, 21.9, 20.5, 24.3]
```

Schreibe ein Programm, das:
1. Die höchste und niedrigste Temperatur findet und ausgibt
2. Die Durchschnittstemperatur berechnet und ausgibt
3. Alle Temperaturen über 23°C in einer neuen Liste `warm` speichert (verwende List Comprehension)
4. Alle Temperaturen unter 20°C in einer neuen Liste `kuehl` speichert (verwende List Comprehension)
5. Beide Listen sortiert ausgibt (Original bleibt unverändert)
6. Die ursprüngliche Liste sortiert (in-place) und ausgibt

**Erwartete Ausgabe (ungefähr)**:
```
Höchste Temperatur: 26.4°C
Niedrigste Temperatur: 17.2°C
Durchschnitt: 22.0°C

Warme Tage (>23°C): [23.7, 24.3, 25.1, 26.4]
Kühle Tage (<20°C): [17.2, 18.3, 19.8]

Originalliste sortiert: [17.2, 18.3, 19.8, 20.5, 21.9, 22.5, 23.7, 24.3, 25.1, 26.4]
```

**Hinweise**:
- `max()` und `min()` für Extremwerte
- `sum()` und `len()` für Durchschnitt
- List Comprehensions mit Bedingung: `[x for x in liste if bedingung]`
- `sorted()` für neue sortierte Liste, `.sort()` für in-place Sortierung

---

### Aufgabe P3: Stack-Implementierung für Klammerprüfung (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-30 Minuten  
**Vorkenntnisse**: Listen als Stack, `.append()`, `.pop()`, Schleifen, Verzweigungen

Implementiere die Klammer-Prüfung aus Theorie-Aufgabe T2 in Python.

Schreibe eine Funktion `klammern_gueltig(ausdruck)`, die:
- Einen String mit Klammern als Parameter erhält
- `True` zurückgibt, wenn alle Klammern korrekt sind
- `False` zurückgibt, wenn Klammern falsch verschachtelt, nicht geschlossen oder in falscher Reihenfolge sind
- Eine Python-Liste als Stack verwendet

**Algorithmus**:
1. Erstelle einen leeren Stack (Liste)
2. Durchlaufe jeden Charakter im String
3. Bei öffnender Klammer `(`, `[`, `{`: Push auf Stack
4. Bei schließender Klammer `)`, `]`, `}`:
   - Wenn Stack leer: Return `False` (keine passende öffnende Klammer)
   - Pop vom Stack und prüfe, ob die Klammertypen zusammenpassen
   - Wenn nicht: Return `False`
5. Am Ende: Stack muss leer sein (alle Klammern geschlossen)

**Testfälle**:
```python
print(klammern_gueltig("()"))           # True
print(klammern_gueltig("()[]{}"))       # True
print(klammern_gueltig("{[()]}"))       # True
print(klammern_gueltig("([{}])"))       # True
print(klammern_gueltig("([)]"))         # False (falsche Reihenfolge)
print(klammern_gueltig("{[(])}"))       # False (falsche Verschachtelung)
print(klammern_gueltig("((())"))        # False (nicht alle geschlossen)
print(klammern_gueltig(")"))            # False (nur schließende Klammer)
print(klammern_gueltig(""))             # True (leerer String ist gültig)
```

**Hinweise**:
- Definiere ein Dictionary für passende Klammerpaare: `paare = {')': '(', ']': '[', '}': '{'}`
- Prüfe, ob ein Zeichen eine öffnende Klammer ist: `zeichen in '([{'`
- Prüfe, ob ein Zeichen eine schließende Klammer ist: `zeichen in ')]}'`
- Verwende `.append()` für Push und `.pop()` für Pop

**Starter-Code**:
```python
def klammern_gueltig(ausdruck):
    """
    Prüft, ob Klammern in einem Ausdruck korrekt verschachtelt sind.
    
    Args:
        ausdruck: String mit Klammern
    
    Returns:
        True, wenn gültig, sonst False
    """
    stack = []
    paare = {')': '(', ']': '[', '}': '{'}
    
    # Dein Code hier
    
    return len(stack) == 0  # Stack muss am Ende leer sein
```

---

### Aufgabe P4: Listen-Manipulation und Slicing (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Slicing, List Comprehensions, `zip()`, Unpacking

Schreibe ein Programm zur Verwaltung von Schüler-Noten.

**Teilaufgabe a)**: Erstelle drei Listen:
```python
namen = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
noten_mathe = [1.7, 2.3, 1.0, 2.7, 1.3]
noten_physik = [2.0, 1.7, 1.3, 3.0, 2.3]
```

**Teilaufgabe b)**: Implementiere folgende Funktionen:

1. `durchschnitt(noten)`: Berechnet den Durchschnitt einer Notenliste
   
2. `beste_drei(namen, noten)`: Gibt die Namen der drei besten Schüler zurück (niedrigste Noten)
   - **Hinweis**: Verwende `zip()`, `sorted()` mit `key`-Parameter, und Slicing
   
3. `notenverteilung(noten)`: Zählt, wie viele Noten in jedem Bereich liegen:
   - Sehr gut: 1.0 - 1.5
   - Gut: 1.6 - 2.5
   - Befriedigend: 2.6 - 3.5
   - Ausreichend: 3.6 - 4.0
   - Gibt Dictionary zurück: `{'Sehr gut': 2, 'Gut': 3, ...}`

4. `kombiniere_noten(noten1, noten2)`: Berechnet für jeden Schüler den Durchschnitt aus beiden Fächern
   - **Hinweis**: Verwende `zip()` und List Comprehension

**Teilaufgabe c)**: Verwende die Funktionen und gib aus:
```
Durchschnitt Mathe: 1.8
Durchschnitt Physik: 2.06

Beste 3 in Mathe: ['Charlie', 'Eve', 'Alice']
Beste 3 in Physik: ['Charlie', 'Bob', 'Alice']

Notenverteilung Mathe:
  Sehr gut: 3
  Gut: 2
  Befriedigend: 0
  Ausreichend: 0

Kombinierte Durchschnittsnoten:
  Alice: 1.85
  Bob: 2.0
  Charlie: 1.15
  Diana: 2.85
  Eve: 1.8
```

**Hinweise**:
- Bei `beste_drei()`: `sorted(zip(namen, noten), key=lambda x: x[1])[:3]`
- Bei `notenverteilung()`: Nutze Bedingungen und zähle mit Zähler-Variablen oder `sum()`
- `round(wert, 2)` für Rundung auf 2 Dezimalstellen

---

### Aufgabe P5: Undo/Redo-System mit Stack (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Listen als Stack, Klassen (Vorschau auf spätere Vorlesungen, hier vereinfacht mit Funktionen)

Implementiere ein vereinfachtes **Undo/Redo-System** für einen Text-Editor mit zwei Stacks.

**Anforderungen**:

1. Das System verwaltet eine Textzeile (String)
2. Unterstützte Operationen:
   - `einfuegen(text)`: Fügt Text am Ende hinzu
   - `loeschen(anzahl)`: Löscht die letzten `anzahl` Zeichen
   - `undo()`: Macht die letzte Operation rückgängig
   - `redo()`: Stellt die letzte rückgängig gemachte Operation wieder her
   - `anzeigen()`: Zeigt den aktuellen Text

3. Verwende zwei Stacks:
   - `undo_stack`: Speichert alle Zustände (Historie)
   - `redo_stack`: Speichert rückgängig gemachte Zustände

**Implementierung**:

Erstelle folgende Funktionen (verwende globale Listen für die Stacks):

```python
# Globale Variablen
text = ""
undo_stack = []
redo_stack = []

def speichere_zustand():
    """Speichert den aktuellen Zustand im Undo-Stack."""
    # Implementierung

def einfuegen(neuer_text):
    """Fügt Text hinzu."""
    # Implementierung

def loeschen(anzahl):
    """Löscht die letzten 'anzahl' Zeichen."""
    # Implementierung

def undo():
    """Macht die letzte Änderung rückgängig."""
    # Implementierung

def redo():
    """Stellt die letzte rückgängig gemachte Änderung wieder her."""
    # Implementierung

def anzeigen():
    """Zeigt den aktuellen Text."""
    # Implementierung
```

**Testprogramm**:
```python
einfuegen("Hallo")
anzeigen()  # "Hallo"

einfuegen(" Welt")
anzeigen()  # "Hallo Welt"

loeschen(5)
anzeigen()  # "Hallo"

undo()
anzeigen()  # "Hallo Welt"

undo()
anzeigen()  # "Hallo"

redo()
anzeigen()  # "Hallo Welt"

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

