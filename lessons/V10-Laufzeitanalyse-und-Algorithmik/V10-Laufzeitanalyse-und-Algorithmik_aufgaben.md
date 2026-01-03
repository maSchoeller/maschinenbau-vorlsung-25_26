# V10: Übungsaufgaben - Laufzeitanalyse & Algorithmik

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V10.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Komplexitätsklassen erkennen (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10 Minuten

Bestimme die Zeitkomplexität (O-Notation) der folgenden Code-Fragmente:

**a)** 
```python
def funktion_a(n):
    summe = 0
    for i in range(n):
        summe += i
    return summe
```

**b)**
```python
def funktion_b(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

**c)**
```python
def funktion_c(n):
    i = n
    while i > 1:
        print(i)
        i = i // 2
```

**d)**
```python
def funktion_d(n):
    return n * (n + 1) // 2
```

**Hinweise**:
- Zähle die Anzahl der Operationen in Abhängigkeit von $n$
- Bei Schleifen: Wie oft wird der Schleifenkörper ausgeführt?
- Ignoriere konstante Faktoren und kleinere Terme

---

### Aufgabe T2: Algorithmus-Analyse mit Worst-Case (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Gegeben ist folgender Algorithmus zur Suche eines Elements in einer **unsortierten** Liste:

```python
def suche_element(liste, ziel):
    for i in range(len(liste)):
        if liste[i] == ziel:
            return i
    return -1
```

**a)** Bestimme die Zeitkomplexität für:
   - **Best-Case**: Welches Szenario ist das günstigste?
   - **Average-Case**: Was ist durchschnittlich zu erwarten?
   - **Worst-Case**: Welches Szenario ist das ungünstigste?

**b)** Wie viele Vergleichsoperationen werden im Worst-Case bei einer Liste mit 1.000 Elementen durchgeführt?

**c)** Vergleiche diesen Algorithmus mit der **binären Suche**:
   - Warum kann binäre Suche hier nicht verwendet werden?
   - Welche Zeitkomplexität hat binäre Suche im Worst-Case?
   - Bei welcher Listengröße macht der Unterschied zwischen linearer und binärer Suche einen deutlichen Unterschied?

**Hinweise**:
- Best-Case: Das gesuchte Element ist an der ersten Position
- Worst-Case: Das Element ist nicht vorhanden oder an letzter Position
- Binäre Suche benötigt eine sortierte Liste

---

### Aufgabe T3: Sortieralgorithmen vergleichen und visualisieren (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 25-30 Minuten

Betrachte die drei Sortieralgorithmen **Bubble Sort**, **Quick Sort** und **Merge Sort**.

**a)** Erstelle eine Tabelle, die die drei Algorithmen hinsichtlich folgender Kriterien vergleicht:
   - Zeitkomplexität (Best-Case, Average-Case, Worst-Case)
   - Speicherkomplexität
   - Stabilität (bleibt die Reihenfolge gleicher Elemente erhalten?)
   - Eignung für große Datenmengen

**b)** Zeichne ein **Programm-Ablauf-Plan (PAP)** für den Bubble-Sort-Algorithmus mit folgenden Schritten:
   - Eingabe: Unsortierte Liste
   - Prozess: Sortierung durch paarweise Vergleiche
   - Ausgabe: Sortierte Liste
   
   Verwende die Symbole aus V05/V06 (Prozess, Verzweigung, Schleife, Start/Ende).

**c)** **Szenario-Analyse**: Welcher Algorithmus ist in folgenden Situationen am besten geeignet?
   1. Liste mit 10 Millionen Elementen, Echtzeit-Sortierung erforderlich
   2. Liste mit 50 Elementen, einfache Implementierung gewünscht
   3. Liste mit 1 Million Elementen, bereits fast sortiert
   4. Liste mit 100.000 Elementen, garantierte $O(n \log n)$ Laufzeit erforderlich

**d)** **Fibonacci-Optimierung**: Die naive rekursive Fibonacci-Implementierung hat $O(2^n)$ Komplexität. Beschreibe eine Optimierungsstrategie (Stichwort: **Memoization**), die die Komplexität auf $O(n)$ reduziert. Erkläre die Idee in eigenen Worten.

**Hinweise**:
- Stabilität: Bleiben gleiche Elemente in ihrer ursprünglichen Reihenfolge?
- Merge Sort benötigt zusätzlichen Speicher für temporäre Listen
- Quick Sort hat im Durchschnitt $O(n \log n)$, im Worst-Case aber $O(n^2)$
- Memoization: Zwischenergebnisse speichern, um Neuberechnungen zu vermeiden

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Erste eigene Funktionen (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Funktionsdefinition mit `def`, `return`, Parameter

Schreibe drei einfache Funktionen:

**a)** Eine Funktion `berechne_rechteck_flaeche(laenge, breite)`, die die Fläche eines Rechtecks berechnet und zurückgibt.

**b)** Eine Funktion `ist_gerade(zahl)`, die prüft, ob eine Zahl gerade ist. Die Funktion soll `True` oder `False` zurückgeben.

**c)** Eine Funktion `temperatur_umrechnen(celsius)`, die Celsius in Fahrenheit umrechnet nach der Formel: $F = C \cdot 1.8 + 32$

**Beispiel Ein-/Ausgabe**:
```python
# a)
print(berechne_rechteck_flaeche(5, 3))  # 15

# b)
print(ist_gerade(4))   # True
print(ist_gerade(7))   # False

# c)
print(temperatur_umrechnen(0))    # 32.0
print(temperatur_umrechnen(100))  # 212.0
```

**Hinweise**:
- Verwende aussagekräftige Funktionsnamen
- Füge Docstrings hinzu (optional, aber empfohlen)
- Teste jede Funktion mit mehreren Werten

---

### Aufgabe P2: Funktionen mit Default-Parametern (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Default-Parameter, Keyword Arguments

Schreibe eine Funktion `berechne_kraftstoffkosten(strecke, verbrauch=7.0, preis=1.80)`, die die Kraftstoffkosten für eine Fahrt berechnet.

**Parameter**:
- `strecke`: Zurückgelegte Strecke in Kilometern
- `verbrauch`: Durchschnittsverbrauch in Litern pro 100 km (Standard: 7.0)
- `preis`: Kraftstoffpreis pro Liter in Euro (Standard: 1.80)

**Formel**: $\text{Kosten} = \frac{\text{Strecke}}{100} \cdot \text{Verbrauch} \cdot \text{Preis}$

**Beispiel Ein-/Ausgabe**:
```python
# Mit Default-Werten
print(berechne_kraftstoffkosten(200))  # 25.2 (200/100 * 7.0 * 1.80)

# Mit angepasstem Verbrauch
print(berechne_kraftstoffkosten(200, verbrauch=5.5))  # 19.8

# Mit allen Parametern
print(berechne_kraftstoffkosten(300, verbrauch=8.0, preis=2.00))  # 48.0

# Keyword Arguments in beliebiger Reihenfolge
print(berechne_kraftstoffkosten(strecke=150, preis=1.95, verbrauch=6.5))  # 19.0125
```

**Hinweise**:
- Runde das Ergebnis auf 2 Dezimalstellen mit `round(wert, 2)`
- Teste verschiedene Aufrufvarianten (nur Strecke, mit Keyword Arguments, etc.)
- Füge einen aussagekräftigen Docstring hinzu

---

### Aufgabe P3: Lineare Suche implementieren (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: Funktionen, Schleifen, `return`

Implementiere eine Funktion `lineare_suche(liste, ziel)`, die ein Element in einer Liste sucht und den Index zurückgibt (oder `-1`, wenn nicht gefunden).

**Erweiterte Anforderungen**:
- Zähle die Anzahl der Vergleiche und gib sie zurück (zusätzlich zum Index)
- Die Funktion soll zwei Werte zurückgeben: `(index, vergleiche)`

**Beispiel Ein-/Ausgabe**:
```python
zahlen = [3, 7, 2, 9, 5, 1, 8]

index, vergleiche = lineare_suche(zahlen, 9)
print(f"Element gefunden an Index {index} nach {vergleiche} Vergleichen")
# Element gefunden an Index 3 nach 4 Vergleichen

index, vergleiche = lineare_suche(zahlen, 1)
print(f"Element gefunden an Index {index} nach {vergleiche} Vergleichen")
# Element gefunden an Index 5 nach 6 Vergleichen

index, vergleiche = lineare_suche(zahlen, 99)
print(f"Element gefunden an Index {index} nach {vergleiche} Vergleichen")
# Element gefunden an Index -1 nach 7 Vergleichen (nicht gefunden)
```

**Hinweise**:
- Verwende eine `for`-Schleife mit `enumerate()` für Index-Zugriff
- Zähle in jedem Schleifendurchlauf den Vergleichszähler hoch
- Gib zwei Werte als Tupel zurück: `return index, vergleiche`

---

### Aufgabe P4: Fibonacci mit und ohne Optimierung (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Rekursion, Funktionen, Dictionaries (optional)

Implementiere die Fibonacci-Folge auf drei verschiedene Arten und vergleiche die Performance.

**a)** **Naive Rekursion**: `fibonacci_rekursiv(n)`
```python
def fibonacci_rekursiv(n):
    """Berechnet die n-te Fibonacci-Zahl (naiv rekursiv)."""
    if n <= 1:
        return n
    return fibonacci_rekursiv(n-1) + fibonacci_rekursiv(n-2)
```

**b)** **Iterative Lösung**: `fibonacci_iterativ(n)`
- Verwende eine Schleife statt Rekursion
- Nutze zwei Variablen, um die letzten beiden Fibonacci-Zahlen zu speichern

**c)** **Performance-Vergleich**:
- Teste beide Funktionen mit `n = 10, 20, 30, 35`
- Messe die Zeit mit:
  ```python
  import time
  start = time.time()
  ergebnis = fibonacci_rekursiv(30)
  ende = time.time()
  print(f"Zeit: {ende - start:.4f} Sekunden")
  ```

**d)** **Bonus - Memoization (optional)**:
Implementiere eine optimierte rekursive Version mit Memoization (Zwischenergebnisse speichern):
```python
def fibonacci_memo(n, cache={}):
    # Deine Implementierung
    pass
```

**Beispiel Ein-/Ausgabe**:
```python
print(fibonacci_rekursiv(10))   # 55
print(fibonacci_iterativ(10))   # 55

# Performance-Test:
# fibonacci_rekursiv(35): ~3-5 Sekunden
# fibonacci_iterativ(35): < 0.001 Sekunden
```

**Hinweise**:
- Die naive rekursive Variante wird ab `n=35` sehr langsam
- Die iterative Lösung ist deutlich schneller: $O(n)$ statt $O(2^n)$
- Für Memoization: Prüfe, ob `n` bereits im Cache ist, bevor du rekursiv aufrufst

---

### Aufgabe P5: Sortieralgorithmus-Visualisierer (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 50-60 Minuten  
**Vorkenntnisse**: Funktionen, Schleifen, Listen, Debugging

Implementiere ein Programm, das verschiedene Sortieralgorithmen ausführt und deren Verhalten visualisiert (Konsolenausgabe).

**Anforderungen**:

**a)** Implementiere folgende Sortieralgorithmen als Funktionen:
- `bubble_sort(liste)`: Bubble Sort
- `selection_sort(liste)`: Selection Sort (zusätzlich zu Vorlesung)
- Eine Hilfsfunktion `tausche(liste, i, j)`, die zwei Elemente vertauscht

**b)** Erweitere die Funktionen um **Tracing**:
- Gib nach jedem Tausch den aktuellen Zustand der Liste aus
- Zähle die Anzahl der Vergleiche und Tauschoperationen
- Gib am Ende Statistiken aus

**c)** Hauptprogramm:
- Erstelle eine Funktion `vergleiche_sortierung(liste)`, die beide Algorithmen ausführt
- Verwende dieselbe unsortierte Liste für beide Algorithmen
- Gib die Anzahl der Operationen aus

**Beispiel Ein-/Ausgabe**:
```python
zahlen = [64, 34, 25, 12, 22, 11, 90]

print("=== BUBBLE SORT ===")
sortiert, stats = bubble_sort_visualisiert(zahlen.copy())
print(f"Vergleiche: {stats['vergleiche']}, Tauschvorgänge: {stats['tausche']}")

print("\n=== SELECTION SORT ===")
sortiert, stats = selection_sort_visualisiert(zahlen.copy())
print(f"Vergleiche: {stats['vergleiche']}, Tauschvorgänge: {stats['tausche']}")

# Mögliche Ausgabe (verkürzt):
# === BUBBLE SORT ===
# Start: [64, 34, 25, 12, 22, 11, 90]
# Schritt 1: [34, 64, 25, 12, 22, 11, 90]
# Schritt 2: [34, 25, 64, 12, 22, 11, 90]
# ...
# Sortiert: [11, 12, 22, 25, 34, 64, 90]
# Vergleiche: 21, Tauschvorgänge: 12
```

**Bonus-Challenge**:
- Implementiere zusätzlich **Quick Sort** (rekursiv)
- Füge eine Option hinzu, um die Visualisierung an/auszuschalten
- Erstelle eine Funktion, die zufällige Listen generiert: `generiere_liste(groesse, min_wert, max_wert)`

**Hinweise**:
- Verwende `.copy()`, um die Original-Liste nicht zu verändern
- Selection Sort: Finde in jedem Durchlauf das Minimum und tausche es an die richtige Position
- Verwende ein Dictionary für Statistiken: `stats = {'vergleiche': 0, 'tausche': 0}`
- Für Quick Sort: Nutze Rekursion und eine Hilfsfunktion `partition(liste, low, high)`

---

