# V08: Lösungen - Listen und Datenstrukturen – Teil 1

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: Zeitkomplexität vergleichen

**Lösung**:

| Operation | Array | Einfach verkettete Liste | Doppelt verkettete Liste |
|-----------|-------|---------------------------|---------------------------|
| Zugriff auf Element an Index i | **O(1)** | **O(n)** | **O(n)** |
| Suchen eines Werts | **O(n)** | **O(n)** | **O(n)** |
| Einfügen am Anfang | **O(n)** | **O(1)** | **O(1)** |
| Einfügen am Ende (mit Tail) | **O(1)** | **O(1)** | **O(1)** |
| Löschen am Anfang | **O(n)** | **O(1)** | **O(1)** |
| Löschen am Ende (mit Tail) | **O(1)** | **O(n)** | **O(1)** |

**Erklärung**:

**Arrays**:
- **Zugriff O(1)**: Direkte Berechnung der Speicheradresse über Index
- **Suchen O(n)**: Im schlimmsten Fall muss das gesamte Array durchlaufen werden
- **Einfügen am Anfang O(n)**: Alle Elemente müssen nach rechts verschoben werden
- **Einfügen am Ende O(1)**: Bei dynamischen Arrays mit freiem Platz einfach anhängen
- **Löschen am Anfang O(n)**: Alle Elemente müssen nach links verschoben werden
- **Löschen am Ende O(1)**: Einfach die Größe reduzieren, kein Verschieben nötig

**Einfach verkettete Listen**:
- **Zugriff O(n)**: Liste muss vom Anfang bis zum Index durchlaufen werden
- **Suchen O(n)**: Gesamte Liste muss durchlaufen werden
- **Einfügen am Anfang O(1)**: Neuer Knoten wird vor Head eingefügt, nur Pointer-Anpassung
- **Einfügen am Ende O(1)**: Mit Tail-Pointer direkt anhängen, Tail-Pointer aktualisieren
- **Löschen am Anfang O(1)**: Head-Pointer auf zweiten Knoten setzen
- **Löschen am Ende O(n)**: Vorletzten Knoten finden (durchlaufen nötig), dessen `next` auf `None` setzen

**Doppelt verkettete Listen**:
- **Zugriff O(n)**: Wie bei einfach verketteter Liste
- **Suchen O(n)**: Wie bei einfach verketteter Liste
- **Einfügen am Anfang O(1)**: Wie bei einfach verketteter Liste, zusätzlich `prev`-Pointer setzen
- **Einfügen am Ende O(1)**: Mit Tail-Pointer direkt anhängen
- **Löschen am Anfang O(1)**: Wie bei einfach verketteter Liste, zusätzlich `prev`-Pointer des neuen ersten Elements auf `None`
- **Löschen am Ende O(1)**: Mit Tail-Pointer: Tail auf vorletzten Knoten setzen (über `prev`-Pointer direkt erreichbar!)

**Häufige Fehler**:
- **Verwechslung von "mit Tail-Pointer" und "ohne Tail-Pointer"**: Ohne Tail-Pointer ist Einfügen am Ende bei verketteten Listen O(n), da die Liste durchlaufen werden muss
- **Übersehen des Unterschieds zwischen einfach und doppelt**: Bei einfach verketteter Liste ist Löschen am Ende O(n), bei doppelt verketteter O(1)
- **Arrays beim Einfügen**: Einfügen am Anfang oder in der Mitte ist O(n), nicht O(1)

---

### Lösung T2: Stack-Anwendungsfall analysieren

**Lösung**:

**Teilaufgabe a)**: Warum ein Stack?

Ein Stack ist ideal für die Klammer-Prüfung, weil das **LIFO-Prinzip** (Last In, First Out) perfekt zur Verschachtelungsstruktur von Klammern passt. Die zuletzt geöffnete Klammer muss als erste geschlossen werden. 

Benötigte Stack-Operationen:
- **Push**: Beim Öffnen einer Klammer wird diese auf den Stack gelegt
- **Pop**: Beim Schließen einer Klammer wird die oberste (zuletzt geöffnete) Klammer vom Stack genommen und geprüft, ob sie zum Klammertyp passt
- **IsEmpty**: Am Ende prüfen, ob alle Klammern geschlossen wurden (Stack muss leer sein)
- **Peek** (optional): Oberste Klammer ansehen, ohne sie zu entfernen

Das LIFO-Prinzip sorgt dafür, dass verschachtelte Klammern in der richtigen Reihenfolge geprüft werden: Die innerste Klammer wird zuerst geschlossen.

**Teilaufgabe b)**: Algorithmus

```
ALGORITHMUS Klammern_pruefen(ausdruck)
    Stack initialisieren (leer)
    
    FÜR jedes Zeichen z in ausdruck:
        WENN z ist öffnende Klammer ('(', '[', '{'):
            Push z auf Stack
        
        WENN z ist schließende Klammer (')', ']', '}'):
            WENN Stack ist leer:
                RETURN False  // Keine passende öffnende Klammer
            
            oeffnende_klammer = Pop vom Stack
            
            WENN oeffnende_klammer passt nicht zu z:
                RETURN False  // Falsche Verschachtelung
        
        // Andere Zeichen ignorieren
    
    WENN Stack ist leer:
        RETURN True  // Alle Klammern korrekt geschlossen
    SONST:
        RETURN False  // Nicht alle Klammern geschlossen
```

**Passende Klammern-Paare**:
- `(` passt zu `)`
- `[` passt zu `]`
- `{` passt zu `}`

**Teilaufgabe c)**: Stack-Entwicklung für `{[()]}`

```
Schritt  | Zeichen | Operation   | Stack-Inhalt       | Kommentar
---------|---------|-------------|--------------------|-----------------------
1        | {       | Push {      | [{]                | Öffne geschweifte Klammer
2        | [       | Push [      | [{, []             | Öffne eckige Klammer
3        | (       | Push (      | [{, [, (]          | Öffne runde Klammer
4        | )       | Pop → (     | [{, []             | Schließe runde Klammer (passt zu ()
5        | ]       | Pop → [     | [{]                | Schließe eckige Klammer (passt zu [)
6        | }       | Pop → {     | []                 | Schließe geschweifte Klammer (passt zu {)
7        | Ende    | Prüfe Stack | [] (leer)          | Stack leer → Gültig ✓
```

**Ergebnis**: Der Ausdruck `{[()]}` ist **gültig**, da der Stack am Ende leer ist und alle Klammerpaare korrekt verschachtelt waren.

**Beispiel für ungültigen Ausdruck** `([)]`:
```
Schritt  | Zeichen | Operation   | Stack-Inhalt       | Kommentar
---------|---------|-------------|--------------------|-----------------------
1        | (       | Push (      | [(]                | Öffne runde Klammer
2        | [       | Push [      | [(, []             | Öffne eckige Klammer
3        | )       | Pop → [     | [(]                | FEHLER: [ passt nicht zu ) ✗
```

**Ergebnis**: Ungültig, da die schließende `)` nicht zur obersten öffnenden Klammer `[` passt.

**Häufige Fehler**:
- **Vergessen, dass Stack leer sein muss**: Wenn nach Durchlauf noch Klammern im Stack sind, bedeutet das, dass nicht alle geschlossen wurden
- **Reihenfolge verwechseln**: Bei `([)]` wird oft übersehen, dass die `[` VOR der `)` geschlossen werden müsste
- **Zu viele schließende Klammern übersehen**: Wenn Stack leer ist und noch eine schließende Klammer kommt, ist der Ausdruck ungültig

---

### Lösung T3: Queue-Implementierung mit Array

**Lösung**:

**Teilaufgabe a)**: Problem der naiven Implementierung

Bei der naiven Implementierung wird das Ende des Arrays für Enqueue verwendet und der Anfang für Dequeue:
- **Enqueue**: `array.append(element)` → O(1), kein Problem
- **Dequeue**: `element = array[0]; array = array[1:]` → **O(n)**, großes Problem!

Das Problem: Beim Entfernen des ersten Elements müssen **alle** verbleibenden Elemente um eine Position nach links verschoben werden. Bei n Elementen bedeutet das n-1 Kopiervorgänge.

**Beispiel**:
```
Initial: [A, B, C, D, E]
Nach Dequeue von A: [B, C, D, E]  // B→Position 0, C→Position 1, D→Position 2, E→Position 3
```
Alle vier Elemente (B, C, D, E) mussten verschoben werden → **O(n)**.

Bei vielen Dequeue-Operationen (z.B. 1000 Mal) summiert sich dies zu O(n²) Gesamtkomplexität, was inakzeptabel ist.

**Alternative naive Lösung mit umgekehrter Reihenfolge** (Anfang für Enqueue, Ende für Dequeue):
- **Enqueue am Anfang**: `array.insert(0, element)` → O(n), alle Elemente verschieben
- **Dequeue am Ende**: `array.pop()` → O(1)

Hier ist Enqueue ineffizient. Beide Operationen sollten aber O(1) sein.

**Teilaufgabe b)**: Zirkuläres Array (Ringpuffer)

Die Lösung ist ein **zirkuläres Array**, bei dem zwei Zeiger die Queue verwalten:
- **Front**: Index des ersten Elements (wird bei Dequeue gelesen und inkrementiert)
- **Rear**: Index, an dem das nächste Element eingefügt wird (wird bei Enqueue beschrieben und inkrementiert)

**Zirkularität**: Wenn ein Zeiger das Ende des Arrays erreicht, "wickelt" er sich zurück an den Anfang. Dies wird mit **Modulo-Arithmetik** erreicht:
```
neuer_index = (alter_index + 1) % array_groesse
```

**Beispiel mit Array-Größe 6**:
```
Index 0  1  2  3  4  5
      [_, _, _, _, _, _]
```
Wenn `Rear` bei Index 5 steht und inkrementiert wird:
```
Rear = (5 + 1) % 6 = 0  // Wickelt sich zurück an den Anfang
```

**Operationen**:
- **Enqueue(element)**:
  ```
  array[Rear] = element
  Rear = (Rear + 1) % array_groesse
  ```
  Zeitkomplexität: O(1)

- **Dequeue()**:
  ```
  element = array[Front]
  Front = (Front + 1) % array_groesse
  return element
  ```
  Zeitkomplexität: O(1)

**Vorteil**: Beide Operationen sind O(1), da keine Elemente verschoben werden müssen. Leere Plätze im Array werden wiederverwendet.

**Teilaufgabe c)**: Visualisierung der Operationen

**Anfangszustand**:
```
Array-Größe: 6
Index:  0   1   2   3   4   5
Array: [_] [_] [_] [_] [_] [_]
Front = 0, Rear = 0 (beide am Anfang)
```

**Schritt 1: Enqueue(A)**
```
Array: [A] [_] [_] [_] [_] [_]
        ^   ^
      Front Rear (nach Increment: Rear = 1)
Front = 0, Rear = 1
```

**Schritt 2: Enqueue(B)**
```
Array: [A] [B] [_] [_] [_] [_]
        ^       ^
      Front     Rear
Front = 0, Rear = 2
```

**Schritt 3: Enqueue(C)**
```
Array: [A] [B] [C] [_] [_] [_]
        ^           ^
      Front         Rear
Front = 0, Rear = 3
```

**Schritt 4: Dequeue() → gibt A zurück**
```
Array: [_] [B] [C] [_] [_] [_]
            ^       ^
          Front     Rear
Front = 1, Rear = 3
(A wurde nicht gelöscht, aber Front zeigt jetzt auf B)
```

**Schritt 5: Dequeue() → gibt B zurück**
```
Array: [_] [_] [C] [_] [_] [_]
                ^   ^
              Front Rear
Front = 2, Rear = 3
```

**Schritt 6: Enqueue(D)**
```
Array: [_] [_] [C] [D] [_] [_]
                ^       ^
              Front     Rear
Front = 2, Rear = 4
```

**Schritt 7: Enqueue(E)**
```
Array: [_] [_] [C] [D] [E] [_]
                ^           ^
              Front         Rear
Front = 2, Rear = 5
```

**Schritt 8: Enqueue(F)**
```
Array: [_] [_] [C] [D] [E] [F]
                ^               ^
              Front        Rear (zeigt hinter Ende)
Front = 2, Rear = 0 (nach (5+1) % 6 = 0, wickelt sich zurück!)
```

**Schritt 9: Enqueue(G)** – Zirkuläre Nutzung des freien Platzes
```
Array: [G] [_] [C] [D] [E] [F]
            ^   ^
          Rear  Front
Front = 2, Rear = 1
```

**Wichtig**: Index 0 wurde wiederverwendet! Die Queue nutzt jetzt die Indizes 2-5 und 0.

**Teilaufgabe d)**: Unterscheidung leer vs. voll

Das Problem: Bei `Front == Rear` könnte die Queue sowohl leer als auch voll sein:
- **Leer**: Wenn keine Elemente vorhanden sind
- **Voll**: Wenn alle Plätze belegt sind und Rear wieder bei Front ankommt

**Lösung 1: Zähler-Variable**
```python
count = 0  # Anzahl der Elemente

# Bei Enqueue:
count += 1
if count > array_groesse:
    # Queue voll

# Bei Dequeue:
count -= 1

# Prüfung:
is_empty = (count == 0)
is_full = (count == array_groesse)
```

**Lösung 2: Ein Platz bleibt ungenutzt**
Verwende nur `array_groesse - 1` Plätze. Die Queue ist voll, wenn `(Rear + 1) % array_groesse == Front`.
```python
is_empty = (Front == Rear)
is_full = ((Rear + 1) % array_groesse == Front)
```

**Beispiel**:
```
Array-Größe: 6, aber nur 5 Elemente speichern
Array: [A] [B] [C] [D] [E] [_]
        ^                   ^
      Front               Rear
(Rear + 1) % 6 = 0 = Front → Voll!
```

**Lösung 3: Flag-Variable**
```python
is_empty_flag = True

# Bei Enqueue:
is_empty_flag = False

# Bei Dequeue:
if Front == Rear nach Pop:
    is_empty_flag = True
```

**Empfehlung**: Zähler-Variable ist am einfachsten und erlaubt direkte Größenabfrage.

**Lösungsweg Schritt für Schritt**:
1. **Problem erkennen**: Naive Implementierung ist ineffizient (O(n) für Dequeue)
2. **Idee**: Zwei Zeiger verwenden, kein Verschieben von Elementen
3. **Herausforderung**: Array-Ende erreicht, aber Platz am Anfang frei
4. **Lösung**: Zirkuläres Array mit Modulo-Arithmetik
5. **Zusatzproblem**: Unterscheidung leer/voll bei `Front == Rear`
6. **Feinabstimmung**: Zähler, ungenutzter Platz oder Flag

**Alternative Lösungsansätze**:
- **Verkettete Liste als Queue**: Kein Array nötig, dynamische Größe, O(1) für beide Operationen
- **Dynamisches Array-Resizing**: Bei Vollständigkeit Array verdoppeln, aber Overhead beim Kopieren

**Häufige Fehler**:
- **Modulo vergessen**: Ohne `% array_groesse` läuft der Index über die Array-Grenzen
- **Leer/Voll-Bedingung übersehen**: Ohne Zusatzlogik kann man leer und voll nicht unterscheiden
- **Alte Daten nicht überschreiben**: Beim Enqueue muss der Platz überschrieben werden, auch wenn dort noch alte Daten stehen

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: Sensor-Messwerte-Erfassung

**Vollständiger Code**:
```python
temperaturen = []

while True:
    eingabe = input("Temperatur eingeben (oder 'STOP'): ")
    
    if eingabe.upper() == "STOP":
        break
    
    temp = float(eingabe)
    temperaturen.append(temp)
    print(f"Messwerte: {temperaturen}")

print("\n" + "═" * 35)
print("Erfassung beendet.")
print(f"Gesamtanzahl: {len(temperaturen)} Messwerte")

if any(t > 100 for t in temperaturen):
    print("⚠️  WARNUNG: Kritische Temperatur erfasst! (>100°C)")
    print("Maßnahme: Kühlung prüfen, Maschine ggf. abschalten")
else:
    print("✅ Alle Temperaturen im Normbereich")
```

**Erklärung**:

`.append()` fügt Messwerte zur Liste hinzu. `any()` mit Generator-Expression prüft effizient auf kritische Werte. `float()` konvertiert String-Eingabe zu Dezimalzahl.

---

### Lösung P2: Vibrationsdaten-Analyse für Predictive Maintenance

**Vollständiger Code**:
```python
vibrationen = [2.5, 8.3, 5.1, 9.8, 3.7, 7.2, 12.4, 4.9, 6.5, 10.3]

print("═" * 39)
print("  Vibrations-Analyse - Lager #42")
print("═" * 39)

# Extremwerte und Durchschnitt
print(f"Max. Vibration: {max(vibrationen)} m/s²")
print(f"Min. Vibration: {min(vibrationen)} m/s²")
print(f"Durchschnitt: {sum(vibrationen) / len(vibrationen):.1f} m/s²")

# Klassifikation mit List Comprehensions
kritisch = sorted([v for v in vibrationen if v > 10])
erhoeht = sorted([v for v in vibrationen if 7 <= v <= 10])
normal = sorted([v for v in vibrationen if v < 7])

print(f"\n⚠️  Kritische Werte (>10 m/s²): {kritisch}")
print(f"🟡 Erhöhte Werte (7-10 m/s²): {erhoeht}")
print(f"✅ Normale Werte (<7 m/s²): {normal}")

# Bewertung
if kritisch:
    print("\nBEWERTUNG: ❌ LAGER KRITISCH")
    print("Empfehlung: Wartung einplanen, Lager austauschen")
elif erhoeht:
    print("\nBEWERTUNG: 🟡 LAGER ÜBERWACHEN")
else:
    print("\nBEWERTUNG: ✅ LAGER OK")

# In-place sortieren
vibrationen.sort()
print(f"\nSortierte Werte: {vibrationen}")
```

**Erklärung**:

List Comprehensions mit Bedingungen filtern Werte effizient. `sorted()` erstellt neue Liste, `.sort()` sortiert in-place. `max()`, `min()`, `sum()` sind Built-in-Funktionen für Listen.

---

### Lösung P3: NC-Programm-Validator mit Stack

**Vollständiger Code**:
```python
def nc_struktur_gueltig(programm):
    stack = []
    paare = {'L11': 'L10', 'P101': 'P100', 'ENDIF': 'IF'}
    oeffnend = ['L10', 'P100', 'IF']
    
    for befehl in programm:
        if befehl in oeffnend:
            stack.append(befehl)
        elif befehl in paare:
            if not stack or stack.pop() != paare[befehl]:
                return False
    
    return len(stack) == 0

# Tests
print(nc_struktur_gueltig(["L10", "L11"]))                    # True
print(nc_struktur_gueltig(["L10", "P100", "P101", "L11"]))    # True
print(nc_struktur_gueltig(["IF", "L10", "L11", "ENDIF"]))     # True
print(nc_struktur_gueltig(["L10", "P100", "L11", "P101"]))    # False
print(nc_struktur_gueltig(["L10", "IF", "L11", "ENDIF"]))     # False
```

**Erklärung**:

Stack (Liste) mit `.append()` und `.pop()` verwaltet Verschachtelung. Dictionary `paare` mappt schließende zu öffnenden Befehlen. `not stack` prüft auf leeren Stack. Am Ende muss Stack leer sein.

---

### Lösung P4: Materialprüfungs-Datenbank

**Vollständiger Code**:
```python
proben_ids = ["S235-001", "AlMg3-002", "X5CrNi-003", "S235-004", "AlMg3-005"]
zugfestigkeit = [360, 250, 520, 370, 245]
streckgrenze = [235, 180, 210, 240, 175]

def durchschnitt(werte):
    return sum(werte) / len(werte)

def beste_drei(proben, werte):
    sortiert = sorted(zip(proben, werte), key=lambda x: x[1], reverse=True)
    return [p for p, v in sortiert[:3]]

def materialklassifikation(zugfestigkeiten):
    klassen = {'Niedrig': 0, 'Mittel': 0, 'Hoch': 0, 'Sehr hoch': 0}
    for rm in zugfestigkeiten:
        if rm < 300:
            klassen['Niedrig'] += 1
        elif rm < 450:
            klassen['Mittel'] += 1
        elif rm < 600:
            klassen['Hoch'] += 1
        else:
            klassen['Sehr hoch'] += 1
    return klassen

def verhaeltnis_berechnen(zugfest, streck):
    return [round(rm / re, 2) for rm, re in zip(zugfest, streck)]

# Ausgabe
print("═" * 39)
print("  Materialprüfungs-Datenbank")
print("═" * 39)
print(f"Ø Zugfestigkeit: {durchschnitt(zugfestigkeit):.1f} MPa")
print(f"Ø Streckgrenze: {durchschnitt(streckgrenze):.1f} MPa")

print(f"\nTop 3 Zugfestigkeit: {beste_drei(proben_ids, zugfestigkeit)}")
print(f"Top 3 Streckgrenze: {beste_drei(proben_ids, streckgrenze)}")

print("\nFestigkeitsklassifikation:")
for klasse, anzahl in materialklassifikation(zugfestigkeit).items():
    print(f"  {klasse}: {anzahl}")

print("\nVerhältnis Rm/Re (Verfestigungspotential):")
verhaeltnisse = verhaeltnis_berechnen(zugfestigkeit, streckgrenze)
for probe, verh in zip(proben_ids, verhaeltnisse):
    print(f"  {probe}: {verh}")
```

**Erklärung**:

`zip()` kombiniert Listen elementweise. `lambda x: x[1]` extrahiert zweiten Wert für Sortierung. `reverse=True` sortiert absteigend. List Comprehension mit `zip()` berechnet Verhältnisse parallel.

---

### Lösung P5: CNC-Programm-Editor mit Undo/Redo

**Vollständiger Code**:
```python
nc_code = ""
undo_stack = []
redo_stack = []

def speichere_zustand():
    undo_stack.append(nc_code)
    redo_stack.clear()

def befehl_hinzufuegen(code):
    global nc_code
    speichere_zustand()
    nc_code += code

def zeichen_loeschen(anzahl):
    global nc_code
    speichere_zustand()
    nc_code = nc_code[:-anzahl] if anzahl <= len(nc_code) else ""

def undo():
    global nc_code
    if undo_stack:
        redo_stack.append(nc_code)
        nc_code = undo_stack.pop()

def redo():
    global nc_code
    if redo_stack:
        undo_stack.append(nc_code)
        nc_code = redo_stack.pop()

def anzeigen():
    print(f"NC-Code: '{nc_code}'")

# Test
befehl_hinzufuegen("G01 X100")
anzeigen()  # "G01 X100"

befehl_hinzufuegen(" Y50")
anzeigen()  # "G01 X100 Y50"

zeichen_loeschen(4)
anzeigen()  # "G01 X100"

undo()
anzeigen()  # "G01 X100 Y50"

redo()
anzeigen()  # "G01 X100"
```

**Erklärung**:

Zwei Stacks speichern Zustände. `global` ermöglicht Funktionszugriff auf Modul-Variable. String-Slicing `[:-anzahl]` entfernt letzte Zeichen. `.clear()` leert Redo-Stack bei neuer Änderung.

**Häufige Fehler**:
- **Fehler**: Redo-Stack nicht leeren bei neuer Änderung
  - **Warum falsch**: Alte Redo-Historie bleibt ungültig nach neuer Änderung
  - **Richtig**: `redo_stack.clear()` in `speichere_zustand()`
    print(f"Einkaufsliste: {einkaufsliste}")

# Anzahl anzeigen
print(f"\nGesamtanzahl: {len(einkaufsliste)} Artikel")

# Prüfen, ob Milch auf der Liste steht
if "Milch" in einkaufsliste:
    print("Milch ist auf der Liste!")
else:
    print("Milch ist nicht auf der Liste.")
```

**Erklärung**:

1. **Liste erstellen**: `einkaufsliste = []` erstellt eine leere Liste

2. **Endlos-Schleife mit Abbruchbedingung**: 
   ```python
   while True:
       artikel = input(...)
       if artikel.lower() == "fertig":
           break
   ```
   - `while True` erstellt eine Endlos-Schleife
   - `.lower()` macht die Eingabe klein, sodass "Fertig", "FERTIG", "fertig" alle akzeptiert werden
   - `break` beendet die Schleife

3. **Element hinzufügen**: `.append(artikel)` fügt den Artikel am Ende der Liste hinzu

4. **Liste anzeigen**: f-String mit Liste wird automatisch formatiert

5. **Länge ermitteln**: `len(einkaufsliste)` gibt die Anzahl der Elemente zurück

6. **Mitgliedschaftstest**: `"Milch" in einkaufsliste` prüft, ob der String "Milch" in der Liste vorhanden ist

**Warum diese Lösung?**

- **`while True` mit `break`**: Idiomatisches Python-Muster für "wiederhole, bis Bedingung erfüllt"
- **`.lower()` für robuste Eingabe**: Benutzer kann "fertig" in jeder Schreibweise eingeben
- **`in`-Operator**: Einfachster Weg zur Prüfung der Mitgliedschaft, O(n) Zeitkomplexität

**Häufige Fehler**:
- **Vergessen von `.lower()`**: 
  ```python
  # Falsch:
  if artikel == "fertig":  # Funktioniert nicht bei "Fertig"
  
  # Richtig:
  if artikel.lower() == "fertig":
  ```

- **Schreibweise "Milch"**: Groß-/Kleinschreibung muss exakt übereinstimmen. Für robuste Prüfung:
  ```python
  if any(artikel.lower() == "milch" for artikel in einkaufsliste):
  ```

- **Liste nicht initialisiert**: Ohne `einkaufsliste = []` gibt es einen `NameError` bei `.append()`

**Erweiterte Variante** (mit case-insensitive Milch-Prüfung):
```python
einkaufsliste = []

while True:
    artikel = input("Artikel eingeben (oder 'fertig' zum Beenden): ")
    
    if artikel.lower() == "fertig":
        break
    
    einkaufsliste.append(artikel)
    print(f"Einkaufsliste: {einkaufsliste}")

print(f"\nGesamtanzahl: {len(einkaufsliste)} Artikel")

# Case-insensitive Prüfung
if any(artikel.lower() == "milch" for artikel in einkaufsliste):
    print("Milch ist auf der Liste!")
else:
    print("Milch ist nicht auf der Liste.")
```

---

### Lösung P2: Listen sortieren und filtern

**Vollständiger Code**:
```python
# Gegeben
temperaturen = [22.5, 18.3, 25.1, 19.8, 23.7, 17.2, 26.4, 21.9, 20.5, 24.3]

# 1. Höchste und niedrigste Temperatur
hoechste = max(temperaturen)
niedrigste = min(temperaturen)
print(f"Höchste Temperatur: {hoechste}°C")
print(f"Niedrigste Temperatur: {niedrigste}°C")

# 2. Durchschnitt berechnen
durchschnitt = sum(temperaturen) / len(temperaturen)
print(f"Durchschnitt: {durchschnitt:.1f}°C")  # .1f für 1 Dezimalstelle

# 3. Warme Tage (>23°C) mit List Comprehension
warm = [t for t in temperaturen if t > 23]
print(f"\nWarme Tage (>23°C): {sorted(warm)}")

# 4. Kühle Tage (<20°C) mit List Comprehension
kuehl = [t for t in temperaturen if t < 20]
print(f"Kühle Tage (<20°C): {sorted(kuehl)}")

# 5. Original mit sorted() sortieren (neue Liste)
sortiert = sorted(temperaturen)
print(f"\nOriginalliste sortiert: {sortiert}")

# 6. Original in-place sortieren mit .sort()
temperaturen.sort()
print(f"Temperaturen nach .sort(): {temperaturen}")
```

**Ausgabe**:
```
Höchste Temperatur: 26.4°C
Niedrigste Temperatur: 17.2°C
Durchschnitt: 22.0°C

Warme Tage (>23°C): [23.7, 24.3, 25.1, 26.4]
Kühle Tage (<20°C): [17.2, 18.3, 19.8]

Originalliste sortiert: [17.2, 18.3, 19.8, 20.5, 21.9, 22.5, 23.7, 24.3, 25.1, 26.4]
Temperaturen nach .sort(): [17.2, 18.3, 19.8, 20.5, 21.9, 22.5, 23.7, 24.3, 25.1, 26.4]
```

**Erklärung**:

**Schritt 1 & 2**: `max()`, `min()`, `sum()`, `len()`
- Built-in Funktionen für numerische Operationen
- `sum(temperaturen) / len(temperaturen)` berechnet arithmetisches Mittel
- Alternative für Durchschnitt (Python 3.4+): `import statistics; statistics.mean(temperaturen)`

**Schritt 3 & 4**: List Comprehensions mit Filter
```python
warm = [t for t in temperaturen if t > 23]
```
- Syntax: `[ausdruck for variable in iterable if bedingung]`
- Entspricht:
  ```python
  warm = []
  for t in temperaturen:
      if t > 23:
          warm.append(t)
  ```
- **Vorteil**: Kompakt, lesbar, oft performanter

**Schritt 5**: `sorted()` – neue sortierte Liste
- `sorted(temperaturen)` gibt neue Liste zurück
- Original bleibt unverändert
- Funktioniert mit jedem Iterable (Liste, Tuple, String, etc.)

**Schritt 6**: `.sort()` – in-place Sortierung
- `temperaturen.sort()` modifiziert die Liste direkt
- Gibt `None` zurück
- Nur für Listen verfügbar (nicht für Tupel oder Strings)

**Konzepte in dieser Lösung**:
- **List Comprehensions**: Kompakte Listenverarbeitung mit Filter
- **`sorted()` vs. `.sort()`**: Neue Liste vs. Modifikation
- **Built-in Aggregatfunktionen**: `max()`, `min()`, `sum()`
- **String-Formatierung**: f-Strings mit Format-Spezifikationen (`.1f` für eine Dezimalstelle)

**Schritt-für-Schritt Durchlauf** (List Comprehension für `warm`):
```python
temperaturen = [22.5, 18.3, 25.1, 19.8, 23.7, ...]

# Schritt 1: 22.5 > 23? Nein, nicht hinzufügen
# Schritt 2: 18.3 > 23? Nein
# Schritt 3: 25.1 > 23? Ja → warm = [25.1]
# Schritt 4: 19.8 > 23? Nein
# Schritt 5: 23.7 > 23? Ja → warm = [25.1, 23.7]
# ...
# Ergebnis: warm = [25.1, 23.7, 26.4, 24.3] (unsortiert!)
```

Deshalb: `sorted(warm)` für sortierte Ausgabe.

**Häufige Fehler**:
- **`.sort()` Rückgabewert verwenden**:
  ```python
  # Falsch:
  sortiert = temperaturen.sort()  # sortiert wird None!
  
  # Richtig (in-place):
  temperaturen.sort()
  
  # Richtig (neue Liste):
  sortiert = sorted(temperaturen)
  ```

- **List Comprehension ohne Filter**:
  ```python
  # Falsch (kein Filter):
  warm = [t for t in temperaturen]  # Kopiert alle
  
  # Richtig:
  warm = [t for t in temperaturen if t > 23]
  ```

- **Division durch Null vergessen zu prüfen**: Bei leeren Listen würde `len()` 0 sein → `ZeroDivisionError`

---

### Lösung P3: Stack-Implementierung für Klammerprüfung

**Vollständiger Code**:
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
    
    # Dictionary für passende Klammerpaare (schließend → öffnend)
    paare = {')': '(', ']': '[', '}': '{'}
    
    for zeichen in ausdruck:
        # Öffnende Klammer: Push auf Stack
        if zeichen in '([{':
            stack.append(zeichen)
        
        # Schließende Klammer: Pop und prüfen
        elif zeichen in ')]}':
            # Stack leer? → Keine passende öffnende Klammer
            if not stack:
                return False
            
            # Oberste Klammer vom Stack nehmen
            oeffnende = stack.pop()
            
            # Prüfen, ob Klammertypen zusammenpassen
            if paare[zeichen] != oeffnende:
                return False
    
    # Am Ende muss Stack leer sein (alle Klammern geschlossen)
    return len(stack) == 0


# Testfälle
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

**Ausgabe**:
```
True
True
True
True
False
False
False
False
True
```

**Erklärung**:

**Datenstruktur**:
```python
stack = []  # Python-Liste als Stack
paare = {')': '(', ']': '[', '}': '{'}  # Mapping schließend → öffnend
```
- Dictionary für schnelles Lookup: Welche öffnende Klammer gehört zur schließenden?

**Algorithmus**:

1. **Öffnende Klammer** (`(`, `[`, `{`):
   ```python
   if zeichen in '([{':
       stack.append(zeichen)  # Push auf Stack
   ```
   - Alle öffnenden Klammern werden auf den Stack gelegt
   - O(1) Operation

2. **Schließende Klammer** (`)`, `]`, `}`):
   ```python
   elif zeichen in ')]}':
       if not stack:
           return False  # Keine passende öffnende Klammer
       
       oeffnende = stack.pop()
       
       if paare[zeichen] != oeffnende:
           return False  # Falsches Paar
   ```
   - Prüfe, ob Stack leer ist (keine öffnende Klammer vorhanden)
   - Pop oberste Klammer vom Stack
   - Prüfe, ob sie zum aktuellen Klammertyp passt

3. **Ende**: Stack muss leer sein
   ```python
   return len(stack) == 0
   ```
   - Wenn noch Klammern im Stack sind, wurden sie nicht alle geschlossen

**Warum diese Lösung?**

- **LIFO-Prinzip**: Stack stellt sicher, dass die zuletzt geöffnete Klammer zuerst geschlossen wird
- **Dictionary für Paare**: Elegante Zuordnung schließend → öffnend, vermeidet lange if-elif-Ketten
- **Early Return**: Bei Fehler sofort `False` zurückgeben, spart unnötige Prüfungen

**Schritt-für-Schritt Durchlauf** für `{[()]}`:

```
Zeichen | Stack vor | Operation      | Stack nach | Ergebnis
--------|-----------|----------------|------------|----------
{       | []        | Push {         | [{]        | -
[       | [{]       | Push [         | [{, []     | -
(       | [{, []    | Push (         | [{, [, (]  | -
)       | [{, [, (] | Pop → ( passt  | [{, []     | -
]       | [{, []    | Pop → [ passt  | [{]        | -
}       | [{]       | Pop → { passt  | []         | -
Ende    | []        | Stack leer?    | []         | True ✓
```

**Schritt-für-Schritt Durchlauf** für `([)]` (ungültig):

```
Zeichen | Stack vor | Operation      | Stack nach | Ergebnis
--------|-----------|----------------|------------|----------
(       | []        | Push (         | [(]        | -
[       | [(]       | Push [         | [(, []     | -
)       | [(, []    | Pop → [        | [(]        | FEHLER: [ != (
```
Rückgabe: `False` (schließende `)` passt nicht zu öffnender `[`)

**Konzepte in dieser Lösung**:
- **Stack mit Liste**: `.append()` für Push, `.pop()` für Pop
- **Dictionary**: Mapping für Klammerpaare
- **String-Mitgliedschaft**: `zeichen in '([{'` prüft Zugehörigkeit
- **Early Return**: Vorzeitiger Abbruch bei Fehler
- **Truthy/Falsy**: `if not stack:` statt `if len(stack) == 0:`

**Häufige Fehler**:
- **Pop bei leerem Stack vergessen zu prüfen**:
  ```python
  # Falsch (führt zu IndexError):
  oeffnende = stack.pop()  # Wenn stack leer ist!
  
  # Richtig:
  if not stack:
      return False
  oeffnende = stack.pop()
  ```

- **Paare-Dictionary verkehrt herum**:
  ```python
  # Falsch:
  paare = {'(': ')', '[': ']', '{': '}'}  # öffnend → schließend
  
  # Richtig:
  paare = {')': '(', ']': '[', '}': '{'}  # schließend → öffnend
  ```
  Wir brauchen das Mapping von der schließenden zur öffnenden Klammer!

- **Stack-Leerheit am Ende nicht prüfen**:
  ```python
  # Falsch:
  return True  # Auch wenn Stack nicht leer!
  
  # Richtig:
  return len(stack) == 0  # oder: return not stack
  ```

**Alternative Lösung** (mit expliziten if-elif-Ketten):
```python
def klammern_gueltig_alt(ausdruck):
    stack = []
    
    for zeichen in ausdruck:
        if zeichen == '(':
            stack.append('(')
        elif zeichen == '[':
            stack.append('[')
        elif zeichen == '{':
            stack.append('{')
        elif zeichen == ')':
            if not stack or stack.pop() != '(':
                return False
        elif zeichen == ']':
            if not stack or stack.pop() != '[':
                return False
        elif zeichen == '}':
            if not stack or stack.pop() != '{':
                return False
    
    return len(stack) == 0
```

Diese Lösung ist weniger elegant, aber expliziter. Die Dictionary-Lösung ist pythonischer und skalierbarer (einfach neue Klammertypen hinzufügen).

---

### Lösung P4: Listen-Manipulation und Slicing

**Vollständiger Code**:
```python
# Gegeben
namen = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
noten_mathe = [1.7, 2.3, 1.0, 2.7, 1.3]
noten_physik = [2.0, 1.7, 1.3, 3.0, 2.3]

# Teilaufgabe b): Funktionen implementieren

def durchschnitt(noten):
    """Berechnet den Durchschnitt einer Notenliste."""
    return sum(noten) / len(noten)


def beste_drei(namen, noten):
    """
    Gibt die Namen der drei besten Schüler zurück (niedrigste Noten).
    
    Args:
        namen: Liste der Schülernamen
        noten: Liste der Noten
    
    Returns:
        Liste mit den drei besten Namen
    """
    # Verknüpfe Namen und Noten als Tupel-Paare
    paare = zip(namen, noten)
    
    # Sortiere nach Noten (zweites Element des Tupels)
    sortiert = sorted(paare, key=lambda x: x[1])
    
    # Nimm die ersten drei
    top_drei = sortiert[:3]
    
    # Extrahiere nur die Namen
    namen_top_drei = [name for name, _ in top_drei]
    
    return namen_top_drei


def notenverteilung(noten):
    """
    Zählt, wie viele Noten in jedem Bereich liegen.
    
    Returns:
        Dictionary mit Notenverteilung
    """
    verteilung = {
        'Sehr gut': 0,
        'Gut': 0,
        'Befriedigend': 0,
        'Ausreichend': 0
    }
    
    for note in noten:
        if 1.0 <= note <= 1.5:
            verteilung['Sehr gut'] += 1
        elif 1.6 <= note <= 2.5:
            verteilung['Gut'] += 1
        elif 2.6 <= note <= 3.5:
            verteilung['Befriedigend'] += 1
        elif 3.6 <= note <= 4.0:
            verteilung['Ausreichend'] += 1
    
    return verteilung


def kombiniere_noten(noten1, noten2):
    """
    Berechnet für jeden Schüler den Durchschnitt aus beiden Fächern.
    
    Args:
        noten1: Noten aus Fach 1
        noten2: Noten aus Fach 2
    
    Returns:
        Liste mit Durchschnittsnoten
    """
    # Berechne Durchschnitt für jedes Notenpaar
    durchschnitte = [(n1 + n2) / 2 for n1, n2 in zip(noten1, noten2)]
    return durchschnitte


# Teilaufgabe c): Verwendung der Funktionen

# Durchschnitte
print(f"Durchschnitt Mathe: {durchschnitt(noten_mathe):.2f}")
print(f"Durchschnitt Physik: {durchschnitt(noten_physik):.2f}\n")

# Beste 3
print(f"Beste 3 in Mathe: {beste_drei(namen, noten_mathe)}")
print(f"Beste 3 in Physik: {beste_drei(namen, noten_physik)}\n")

# Notenverteilung
verteilung_mathe = notenverteilung(noten_mathe)
print("Notenverteilung Mathe:")
for kategorie, anzahl in verteilung_mathe.items():
    print(f"  {kategorie}: {anzahl}")

# Kombinierte Noten
kombinierte = kombiniere_noten(noten_mathe, noten_physik)
print("\nKombinierte Durchschnittsnoten:")
for name, note in zip(namen, kombinierte):
    print(f"  {name}: {note:.2f}")
```

**Ausgabe**:
```
Durchschnitt Mathe: 1.80
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
  Bob: 2.00
  Charlie: 1.15
  Diana: 2.85
  Eve: 1.80
```

**Erklärung**:

**Funktion 1: `durchschnitt()`**
```python
def durchschnitt(noten):
    return sum(noten) / len(noten)
```
- Einfache Berechnung: Summe durch Anzahl
- Keine Fehlerbehandlung bei leerer Liste (würde `ZeroDivisionError` werfen)

**Funktion 2: `beste_drei()`** – Komplexeste Funktion
```python
def beste_drei(namen, noten):
    paare = zip(namen, noten)
    sortiert = sorted(paare, key=lambda x: x[1])
    top_drei = sortiert[:3]
    namen_top_drei = [name for name, _ in top_drei]
    return namen_top_drei
```

Schritt für Schritt:
1. **`zip(namen, noten)`**: Verknüpft parallele Listen zu Tupeln
   ```python
   # Beispiel:
   # namen = ["Alice", "Bob", "Charlie"]
   # noten = [1.7, 2.3, 1.0]
   # zip(...) → [("Alice", 1.7), ("Bob", 2.3), ("Charlie", 1.0)]
   ```

2. **`sorted(..., key=lambda x: x[1])`**: Sortiert nach zweitem Element (Note)
   - `lambda x: x[1]` ist anonyme Funktion, die das zweite Element des Tupels zurückgibt
   - `x[0]` wäre Name, `x[1]` ist Note
   ```python
   # Sortiert:
   # [("Charlie", 1.0), ("Alice", 1.7), ("Bob", 2.3)]
   ```

3. **`sortiert[:3]`**: Slicing nimmt erste drei Elemente
   ```python
   # Bei 5 Schülern:
   # [("Charlie", 1.0), ("Eve", 1.3), ("Alice", 1.7)]
   ```

4. **List Comprehension mit Unpacking**: `[name for name, _ in top_drei]`
   - `name, _` unpackt das Tupel, `_` ignoriert die Note
   - Extrahiert nur die Namen
   ```python
   # Ergebnis:
   # ["Charlie", "Eve", "Alice"]
   ```

**Alternative ohne Lambda** (expliziter):
```python
def beste_drei_alt(namen, noten):
    paare = list(zip(namen, noten))
    
    # Sortiere mit eigener Funktion
    def get_note(paar):
        return paar[1]
    
    sortiert = sorted(paare, key=get_note)
    top_drei = sortiert[:3]
    
    namen_top_drei = []
    for name, note in top_drei:
        namen_top_drei.append(name)
    
    return namen_top_drei
```

**Funktion 3: `notenverteilung()`**
```python
def notenverteilung(noten):
    verteilung = {'Sehr gut': 0, 'Gut': 0, 'Befriedigend': 0, 'Ausreichend': 0}
    
    for note in noten:
        if 1.0 <= note <= 1.5:
            verteilung['Sehr gut'] += 1
        elif 1.6 <= note <= 2.5:
            verteilung['Gut'] += 1
        elif 2.6 <= note <= 3.5:
            verteilung['Befriedigend'] += 1
        elif 3.6 <= note <= 4.0:
            verteilung['Ausreichend'] += 1
    
    return verteilung
```
- Dictionary mit Zählern initialisieren
- Für jede Note prüfen, in welchen Bereich sie fällt
- Entsprechenden Zähler inkrementieren
- Verkettete Vergleiche: `1.0 <= note <= 1.5` prüft beide Grenzen

**Alternative mit sum()** (kompakter):
```python
def notenverteilung_alt(noten):
    return {
        'Sehr gut': sum(1 for n in noten if 1.0 <= n <= 1.5),
        'Gut': sum(1 for n in noten if 1.6 <= n <= 2.5),
        'Befriedigend': sum(1 for n in noten if 2.6 <= n <= 3.5),
        'Ausreichend': sum(1 for n in noten if 3.6 <= n <= 4.0)
    }
```
- `sum(1 for n in noten if bedingung)` zählt Treffer
- Generator Expression mit `sum()` kombiniert

**Funktion 4: `kombiniere_noten()`**
```python
def kombiniere_noten(noten1, noten2):
    return [(n1 + n2) / 2 for n1, n2 in zip(noten1, noten2)]
```
- `zip(noten1, noten2)` verknüpft Notenpaare
- List Comprehension berechnet Durchschnitt jedes Paares
- Kompakt in einer Zeile

**Ausführliche Version**:
```python
def kombiniere_noten_verbose(noten1, noten2):
    durchschnitte = []
    
    for n1, n2 in zip(noten1, noten2):
        durchschnitt = (n1 + n2) / 2
        durchschnitte.append(durchschnitt)
    
    return durchschnitte
```

**Design-Entscheidungen**:
- **Funktionen statt Inline-Code**: Wiederverwendbarkeit, Testbarkeit, Lesbarkeit
- **List Comprehensions**: Kompakt für einfache Transformationen
- **`zip()` für parallele Listen**: Eleganter als manuelle Index-Verwaltung
- **Lambda vs. benannte Funktion**: Lambda für kurze, einmalige Verwendung

**Komplexitätsanalyse**:
- `durchschnitt()`: O(n) – einmal über Liste iterieren
- `beste_drei()`: O(n log n) – Sortieren dominiert
- `notenverteilung()`: O(n) – einmal über Liste iterieren
- `kombiniere_noten()`: O(n) – `zip()` und List Comprehension sind O(n)

**Häufige Fehler**:
- **`zip()` ohne `list()` bei Debugging**:
  ```python
  paare = zip(namen, noten)
  print(paare)  # <zip object at 0x...> (nicht hilfreich!)
  
  # Besser:
  paare = list(zip(namen, noten))
  print(paare)  # [('Alice', 1.7), ...]
  ```

- **Lambda-Syntax falsch**:
  ```python
  # Falsch:
  sorted(paare, key=lambda (name, note): note)  # SyntaxError in Python 3
  
  # Richtig:
  sorted(paare, key=lambda x: x[1])
  ```

- **Unpacking mit falscher Anzahl Variablen**:
  ```python
  # Falsch:
  for name in top_drei:  # name ist Tupel (name, note)
      print(name)  # ('Charlie', 1.0)
  
  # Richtig:
  for name, note in top_drei:
      print(name)  # "Charlie"
  ```

---

### Lösung P5: Undo/Redo-System mit Stack

**Vollständiger Code**:
```python
# Globale Variablen
text = ""
undo_stack = []
redo_stack = []

def speichere_zustand():
    """Speichert den aktuellen Zustand im Undo-Stack."""
    undo_stack.append(text)
    # Neue Änderung macht Redo ungültig
    redo_stack.clear()


def einfuegen(neuer_text):
    """Fügt Text hinzu."""
    global text
    
    # Aktuellen Zustand speichern (vor Änderung)
    speichere_zustand()
    
    # Text hinzufügen
    text += neuer_text
    
    print(f"Text nach Einfügen: '{text}'")


def loeschen(anzahl):
    """Löscht die letzten 'anzahl' Zeichen."""
    global text
    
    # Prüfen, ob genug Zeichen vorhanden sind
    if anzahl > len(text):
        print(f"Fehler: Kann nicht {anzahl} Zeichen löschen, nur {len(text)} vorhanden.")
        return
    
    # Aktuellen Zustand speichern (vor Änderung)
    speichere_zustand()
    
    # Zeichen löschen (Slicing: alle außer letzte 'anzahl')
    text = text[:-anzahl]
    
    print(f"Text nach Löschen von {anzahl} Zeichen: '{text}'")


def undo():
    """Macht die letzte Änderung rückgängig."""
    global text
    
    # Prüfen, ob Undo möglich ist
    if not undo_stack:
        print("Fehler: Keine Aktion zum Rückgängigmachen vorhanden.")
        return
    
    # Aktuellen Zustand in Redo-Stack speichern
    redo_stack.append(text)
    
    # Vorherigen Zustand wiederherstellen
    text = undo_stack.pop()
    
    print(f"Text nach Undo: '{text}'")


def redo():
    """Stellt die letzte rückgängig gemachte Änderung wieder her."""
    global text
    
    # Prüfen, ob Redo möglich ist
    if not redo_stack:
        print("Fehler: Keine Aktion zum Wiederherstellen vorhanden.")
        return
    
    # Aktuellen Zustand in Undo-Stack speichern
    undo_stack.append(text)
    
    # Redo-Zustand wiederherstellen
    text = redo_stack.pop()
    
    print(f"Text nach Redo: '{text}'")


def anzeigen():
    """Zeigt den aktuellen Text."""
    print(f"Aktueller Text: '{text}'")


# Testprogramm
print("=== Undo/Redo-System Test ===\n")

einfuegen("Hallo")
anzeigen()

print()
einfuegen(" Welt")
anzeigen()

print()
loeschen(5)
anzeigen()

print()
undo()
anzeigen()

print()
undo()
anzeigen()

print()
redo()
anzeigen()

print()
einfuegen("!")
anzeigen()

print()
undo()
anzeigen()
```

**Ausgabe**:
```
=== Undo/Redo-System Test ===

Text nach Einfügen: 'Hallo'
Aktueller Text: 'Hallo'

Text nach Einfügen: 'Hallo Welt'
Aktueller Text: 'Hallo Welt'

Text nach Löschen von 5 Zeichen: 'Hallo'
Aktueller Text: 'Hallo'

Text nach Undo: 'Hallo Welt'
Aktueller Text: 'Hallo Welt'

Text nach Undo: 'Hallo'
Aktueller Text: 'Hallo'

Text nach Redo: 'Hallo Welt'
Aktueller Text: 'Hallo Welt'

Text nach Einfügen: 'Hallo Welt!'
Aktueller Text: 'Hallo Welt!'

Text nach Undo: 'Hallo Welt'
Aktueller Text: 'Hallo Welt'
```

**Erklärung**:

**Architektur-Überblick**:
Das System verwendet **drei globale Variablen**:
1. **`text`**: Der aktuelle Text (String)
2. **`undo_stack`**: Liste mit früheren Zuständen (Geschichte)
3. **`redo_stack`**: Liste mit rückgängig gemachten Zuständen (für Wiederherstellen)

**Visualisierung** der Stacks während der Operationen:

```
Zustand                | text          | undo_stack         | redo_stack
-----------------------|---------------|--------------------|------------
Initial                | ""            | []                 | []
einfuegen("Hallo")     | "Hallo"       | [""]               | []
einfuegen(" Welt")     | "Hallo Welt"  | ["", "Hallo"]      | []
loeschen(5)            | "Hallo"       | ["", "Hallo", "Hallo Welt"] | []
undo()                 | "Hallo Welt"  | ["", "Hallo"]      | ["Hallo"]
undo()                 | "Hallo"       | [""]               | ["Hallo", "Hallo Welt"]
redo()                 | "Hallo Welt"  | ["", "Hallo"]      | ["Hallo"]
einfuegen("!")         | "Hallo Welt!" | ["", "Hallo", "Hallo Welt"] | []
```

**Schritt-für-Schritt Erklärung**:

**1. `speichere_zustand()`** – Zentrale Hilfsfunktion
```python
def speichere_zustand():
    undo_stack.append(text)     # Aktuellen Zustand speichern
    redo_stack.clear()          # Redo-Historie löschen
```
- Wird **vor jeder Änderung** aufgerufen
- Speichert den **aktuellen** Zustand (vor Änderung) im Undo-Stack
- Leert Redo-Stack: Neue Änderungen machen frühere Redos ungültig

**Wichtig**: Warum Redo löschen?
```
Zustand: "Hallo Welt"
Undo → "Hallo"          (redo_stack = ["Hallo Welt"])
Neue Änderung: +"!"     (redo_stack muss geleert werden!)
Sonst würde Redo zu "Hallo Welt" führen, obwohl jetzt "Hallo!" ist.
```

**2. `einfuegen(neuer_text)`** – Text hinzufügen
```python
def einfuegen(neuer_text):
    global text
    speichere_zustand()  # Vor Änderung: Zustand sichern
    text += neuer_text   # Änderung durchführen
    print(f"Text nach Einfügen: '{text}'")
```
- `global text`: Erlaubt Modifikation der globalen Variable
- Speichert **alten** Zustand im Undo-Stack
- Führt Änderung durch

**3. `loeschen(anzahl)`** – Zeichen löschen
```python
def loeschen(anzahl):
    global text
    
    if anzahl > len(text):
        print(f"Fehler: ...")
        return  # Frühes Beenden bei Fehler
    
    speichere_zustand()
    text = text[:-anzahl]  # Slicing: Alle außer letzte 'anzahl'
```
- **Validierung**: Prüft, ob genug Zeichen vorhanden sind
- **Slicing**: `text[:-5]` entfernt die letzten 5 Zeichen
  - `"Hallo Welt"[:-5]` → `"Hallo "`
  - Für `anzahl=0`: `text[:-0]` → `""` (löscht alles, Bug!)
  - **Fix**: `text = text[:-anzahl] if anzahl > 0 else text`

**4. `undo()`** – Änderung rückgängig machen
```python
def undo():
    global text
    
    if not undo_stack:
        print("Fehler: Keine Aktion zum Rückgängigmachen.")
        return
    
    redo_stack.append(text)       # Aktuellen Zustand für Redo sichern
    text = undo_stack.pop()       # Vorherigen Zustand wiederherstellen
```

**Algorithmus**:
1. Prüfe, ob Undo möglich ist (Stack nicht leer)
2. Speichere **aktuellen** Zustand in Redo-Stack (für mögliches Redo)
3. Hole **vorherigen** Zustand aus Undo-Stack (`.pop()`)
4. Setze `text` auf diesen Zustand

**Visualisierung**:
```
Vor Undo:   text = "Hallo Welt"
            undo_stack = ["", "Hallo"]
            redo_stack = []

Schritt 1:  redo_stack.append("Hallo Welt")
            redo_stack = ["Hallo Welt"]

Schritt 2:  text = undo_stack.pop()  # pop() gibt "Hallo" zurück
            text = "Hallo"
            undo_stack = [""]

Nach Undo:  text = "Hallo"
            undo_stack = [""]
            redo_stack = ["Hallo Welt"]
```

**5. `redo()`** – Rückgängig gemachte Änderung wiederherstellen
```python
def redo():
    global text
    
    if not redo_stack:
        print("Fehler: Keine Aktion zum Wiederherstellen.")
        return
    
    undo_stack.append(text)       # Aktuellen Zustand für Undo sichern
    text = redo_stack.pop()       # Redo-Zustand wiederherstellen
```

**Algorithmus** (spiegelbildlich zu Undo):
1. Prüfe, ob Redo möglich ist (Redo-Stack nicht leer)
2. Speichere **aktuellen** Zustand in Undo-Stack
3. Hole **Redo-Zustand** aus Redo-Stack
4. Setze `text` auf diesen Zustand

**Konzepte in dieser Lösung**:
- **Zwei Stacks**: Undo-Historie und Redo-Historie
- **Globale Variablen**: Einfache Lösung für Zustandsverwaltung (in größeren Projekten: Klassen verwenden)
- **LIFO-Prinzip**: Letzte Änderung wird zuerst rückgängig gemacht
- **Validierung**: Prüfung vor Stack-Operationen (`if not stack`)
- **Early Return**: Vorzeitiges Beenden bei Fehlern

**Design-Entscheidungen**:
- **Warum Zustand vor Änderung speichern?**: So können wir immer zum vorherigen Zustand zurückkehren
- **Warum Redo-Stack bei neuer Änderung löschen?**: Neue Änderungen machen frühere Redos irrelevant (Verzweigung in der Geschichte)
- **Warum globale Variablen?**: Einfachheit für diese Aufgabe. In echten Projekten: Objektorientierter Ansatz mit Klasse

**Alternative Lösungsansätze**:

**Ansatz 1: Klassen-basiert** (objektorientiert)
```python
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
    
    def einfuegen(self, neuer_text):
        self._speichere_zustand()
        self.text += neuer_text
    
    # ... weitere Methoden
```
- ✅ Vorteile: Kein `global`, bessere Kapselung, mehrere Editoren möglich
- ❌ Nachteile: Komplexer für diese Aufgabe

**Ansatz 2: Commands-Pattern** (fortgeschritten)
Speichere nicht Zustände, sondern Aktionen:
```python
class Command:
    def execute(self): pass
    def undo(self): pass

class InsertCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text
    
    def execute(self):
        self.editor.text += self.text
    
    def undo(self):
        self.editor.text = self.editor.text[:-len(self.text)]
```
- ✅ Vorteile: Speicher-effizienter (speichert Änderungen, nicht Zustände), erweiterbar
- ❌ Nachteile: Deutlich komplexer

**Häufige Fehler**:
- **`global` vergessen**:
  ```python
  def einfuegen(neuer_text):
      # text += neuer_text  # UnboundLocalError!
      global text  # Erforderlich!
      text += neuer_text
  ```

- **Reihenfolge vertauscht** (Zustand nach Änderung speichern):
  ```python
  # Falsch:
  text += neuer_text
  speichere_zustand()  # Speichert neuen Zustand, nicht alten!
  
  # Richtig:
  speichere_zustand()  # Speichert alten Zustand
  text += neuer_text
  ```

- **Pop bei leerem Stack**:
  ```python
  # Falsch:
  text = undo_stack.pop()  # IndexError bei leerem Stack!
  
  # Richtig:
  if not undo_stack:
      print("Fehler")
      return
  text = undo_stack.pop()
  ```

- **Redo-Stack bei Änderung nicht leeren**:
  - Führt zu inkonsistenter Historie (Redo zeigt auf veraltete Zustände)

**Bonus-Challenge Lösung** (Erweiterte Features):

```python
def anzeige_historie():
    """Zeigt alle Zustände im Undo-Stack."""
    print("Undo-Historie (älteste zuerst):")
    for i, zustand in enumerate(undo_stack):
        print(f"  {i}: '{zustand}'")
    print(f"Aktuell: '{text}'")


def ersetzen(alt, neu):
    """Ersetzt alle Vorkommen von 'alt' durch 'neu'."""
    global text
    speichere_zustand()
    text = text.replace(alt, neu)
    print(f"Text nach Ersetzen: '{text}'")


# Historie auf max. 10 Einträge beschränken (in speichere_zustand())
def speichere_zustand_begrenzt():
    """Speichert Zustand mit Begrenzung auf 10 Einträge."""
    undo_stack.append(text)
    
    # Ältesten Eintrag entfernen, wenn mehr als 10
    if len(undo_stack) > 10:
        undo_stack.pop(0)  # Entfernt erstes Element (ältestes)
    
    redo_stack.clear()
```

---

**Zusammenfassung der Lösungen P4 und P5**:

Diese Aufgaben kombinieren viele fortgeschrittene Konzepte:
- **P4**: `zip()`, `sorted()` mit `key`, Lambda-Funktionen, List Comprehensions, Dictionary-Operationen
- **P5**: Stack-Operationen, Zustandsverwaltung, globale Variablen, LIFO-Prinzip in der Praxis

Beide Aufgaben zeigen realitätsnahe Anwendungsfälle: Datenanalyse (P4) und Undo/Redo-Funktionalität (P5), die in fast jeder modernen Software zu finden ist.

