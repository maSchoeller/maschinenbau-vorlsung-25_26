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

### Aufgabe P1: Berechnungsfunktionen für Maschinenbau (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Funktionsdefinition mit `def`, `return`, Parameter  
**Maschinenbau-Kontext**: Grundlegende Berechnungen für Konstruktion und Fertigung

Schreibe drei Funktionen für häufige Maschinenbau-Berechnungen:

> [!NOTE]
> **Maschinenbau-Berechnungen**: Ingenieure führen täglich Standardberechnungen durch:
> - **Schnittgeschwindigkeit** (v): Drehzahl und Werkzeugdurchmesser bestimmen Bearbeitungsqualität
> - **Drehmoment-Leistung**: Motor-Auslegung für Antriebssysteme
> - **Spannungsberechnung**: Festigkeitsprüfung für Bauteile unter Belastung

**a)** Eine Funktion `berechne_schnittgeschwindigkeit(durchmesser_mm, drehzahl_umin)`, die die Schnittgeschwindigkeit in m/min berechnet.  
**Formel**: $v_c = \frac{\pi \cdot d \cdot n}{1000}$ (d in mm, n in U/min, v in m/min)

**b)** Eine Funktion `berechne_leistung(drehmoment_nm, drehzahl_umin)`, die die Leistung in kW berechnet.  
**Formel**: $P = \frac{M \cdot n}{9550}$ (M in Nm, n in U/min, P in kW)

**c)** Eine Funktion `berechne_zugspannung(kraft_n, querschnitt_mm2)`, die die Zugspannung in MPa berechnet.  
**Formel**: $\sigma = \frac{F}{A}$ (F in N, A in mm², σ in MPa)

**Beispiel Ein-/Ausgabe**:
```python
# a) Schnittgeschwindigkeit für Ø50mm Fräser bei 3000 U/min
print(berechne_schnittgeschwindigkeit(50, 3000))  # 471.24 m/min

# b) Leistung bei 100 Nm Drehmoment und 1500 U/min
print(berechne_leistung(100, 1500))  # 15.71 kW

# c) Zugspannung bei 50000 N Kraft auf 200 mm² Querschnitt
print(berechne_zugspannung(50000, 200))  # 250.0 MPa
```

**Hinweise**:
- Verwende `math.pi` für π oder den Wert 3.14159
- Runde Ergebnisse auf 2 Dezimalstellen mit `round(wert, 2)`
- Füge Docstrings hinzu mit Beschreibung und Einheiten

---

### Aufgabe P2: Werkzeugstandzeit-Berechnung mit Default-Parametern (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Default-Parameter, Keyword Arguments  
**Maschinenbau-Kontext**: Werkzeugstandzeit-Kalkulation für Produktionsplanung

Schreibe eine Funktion `berechne_werkzeugkosten_pro_stueck(stueckzahl, werkzeugkosten=50.0, standzeit=1000, nebenzeiten_min=0.5)`, die die Werkzeugkosten pro Werkstück berechnet.

> [!NOTE]
> **Werkzeugstandzeit**: Die Standzeit gibt an, wie viele Teile ein Werkzeug fertigen kann, bevor es verschleißt. Typische Werte:
> - Hartmetall-Fräser: 500-2000 Teile
> - HSS-Bohrer: 200-800 Teile
> - Wendeschneidplatten: 1000-5000 Teile
> 
> Die Werkzeugkosten pro Stück sind entscheidend für Kalkulation und Wirtschaftlichkeit.

**Parameter**:
- `stueckzahl`: Anzahl zu fertigender Werkstücke
- `werkzeugkosten`: Kosten pro Werkzeug in Euro (Standard: 50.0)
- `standzeit`: Anzahl Teile pro Werkzeug (Standard: 1000)
- `nebenzeiten_min`: Rüstzeit pro Werkzeugwechsel in Minuten (Standard: 0.5)

**Formel**: 
- Anzahl Werkzeugwechsel: $\text{Wechsel} = \lceil \frac{\text{Stückzahl}}{\text{Standzeit}} \rceil - 1$
- Werkzeugkosten pro Stück: $\frac{\text{Wechsel} \cdot \text{Werkzeugkosten}}{\text{Stückzahl}}$

**Beispiel Ein-/Ausgabe**:
```python
# Mit Default-Werten: 2000 Teile
print(berechne_werkzeugkosten_pro_stueck(2000))  # 0.025 Euro/Stück (1 Wechsel)

# Mit angepasster Standzeit
print(berechne_werkzeugkosten_pro_stueck(5000, standzeit=500))  # 0.09 Euro/Stück

# Mit allen Parametern
print(berechne_werkzeugkosten_pro_stueck(10000, werkzeugkosten=120.0, standzeit=2000))  # 0.048 Euro/Stück

# Keyword Arguments
print(berechne_werkzeugkosten_pro_stueck(stueckzahl=3000, werkzeugkosten=80.0, standzeit=1500))  # 0.0267 Euro/Stück
```

**Hinweise**:
- Verwende `math.ceil()` für Aufrunden
- Runde das Ergebnis auf 4 Dezimalstellen
- Teste Grenzfälle (z.B. Stückzahl < Standzeit)

---

### Aufgabe P3: Werkzeugsuche in Magazin mit Performance-Analyse (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: Funktionen, Schleifen, `return`  
**Maschinenbau-Kontext**: CNC-Werkzeugmagazin-Verwaltung mit Suchzeitanalyse

Implementiere eine Funktion `suche_werkzeug(magazin, werkzeug_id)`, die ein Werkzeug im CNC-Magazin sucht und Statistiken zur Suchzeit liefert.

> [!NOTE]
> **CNC-Werkzeugmagazin**: Moderne CNC-Maschinen haben Werkzeugmagazine mit 24-120 Plätzen. Die Suchzeit beeinflusst:
> - Werkzeugwechselzeit (typisch 2-6 Sekunden)
> - Gesamt-Zykluszeit
> - Produktivität
> 
> Häufig verwendete Werkzeuge sollten auf vorderen Positionen liegen.

**Erweiterte Anforderungen**:
- Zähle die Anzahl der Vergleiche und gib sie zurück
- Die Funktion soll drei Werte zurückgeben: `(position, vergleiche, gefunden)`
- Position ist 1-basiert (erster Platz = 1)

**Beispiel Ein-/Ausgabe**:
```python
magazin = [101, 205, 310, 405, 210, 115, 320, 208, 412, 505]
# Werkzeug-IDs: T101 (Bohrer Ø10), T205 (Fräser Ø20), etc.

position, vergleiche, gefunden = suche_werkzeug(magazin, 405)
print(f"Werkzeug T{405} an Position {position} nach {vergleiche} Vergleichen (Status: {gefunden})")
# Werkzeug T405 an Position 4 nach 4 Vergleichen (Status: True)

position, vergleiche, gefunden = suche_werkzeug(magazin, 505)
print(f"Werkzeug T{505} an Position {position} nach {vergleiche} Vergleichen (Status: {gefunden})")
# Werkzeug T505 an Position 10 nach 10 Vergleichen (Status: True)

position, vergleiche, gefunden = suche_werkzeug(magazin, 999)
print(f"Werkzeug T{999} nicht gefunden nach {vergleiche} Vergleichen (Status: {gefunden})")
# Werkzeug T999 nicht gefunden nach 10 Vergleichen (Status: False)
```

**Hinweise**:
- Verwende `enumerate(magazin, start=1)` für 1-basierte Positionen
- Zähle Vergleiche in jedem Durchlauf
- Gib `(0, vergleiche, False)` zurück wenn nicht gefunden
- Best-Case: O(1), Worst-Case: O(n), Average-Case: O(n/2)

---

### Aufgabe P4: Fibonacci-Drehzahl-Sequenz mit Performance-Analyse (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Rekursion, Funktionen, Performance-Messung  
**Maschinenbau-Kontext**: Spindeldrehzahl-Optimierung mit Fibonacci-Reihe

Implementiere Drehzahl-Sequenzen auf Basis der Fibonacci-Folge für Spindeldrehzahl-Tests und vergleiche verschiedene Algorithmen.

> [!NOTE]
> **Fibonacci in der Fertigung**: Die Fibonacci-Folge wird in der Fertigung für:
> - **Drehzahl-Tests**: Systematische Variation bei Schnittversuchen (500, 800, 1300, 2100 U/min...)
> - **Feed-Rate-Optimierung**: Schrittweise Erhöhung der Vorschubgeschwindigkeit
> - **Golden Ratio Search**: Optimaler Suchbereich für Parameter
> 
> Die Folge bietet ausgewogene Schrittweiten ohne zu große Sprünge.

**a)** **Naive Rekursion**: `fibonacci_rekursiv(n)` - bereits implementiert (siehe Aufgabenstellung oben)

**b)** **Iterative Lösung für Drehzahl-Sequenz**: `fibonacci_drehzahl_iterativ(n, basis=500)`
- Verwende eine Schleife statt Rekursion
- Berechne Drehzahl-Sequenz: basis × Fibonacci(i)
- Nutze zwei Variablen für die letzten beiden Werte

**c)** **Performance-Vergleich mit Spindeldrehzahlen**:
```python
import time

# Teste Sequenz-Generierung für 10, 20, 30 Stufen
for stufen in [10, 20, 30]:
    start = time.time()
    drehzahlen = [fibonacci_drehzahl_iterativ(i, 500) for i in range(stufen)]
    ende = time.time()
    print(f"{stufen} Stufen: {ende - start:.6f}s - Max. Drehzahl: {max(drehzahlen)} U/min")
```

**d)** **Bonus - Memoization für große Sequenzen**:
```python
def fibonacci_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]
```

**Beispiel Ein-/Ausgabe**:
```python
# Drehzahl-Sequenz (Basis 500 U/min)
for i in range(1, 11):
    drehzahl = 500 * fibonacci_rekursiv(i)
    print(f"Stufe {i}: {drehzahl} U/min")

# Output:
# Stufe 1: 500 U/min
# Stufe 2: 500 U/min
# Stufe 3: 1000 U/min
# Stufe 4: 1500 U/min
# Stufe 5: 2500 U/min
# ...
# Stufe 10: 27500 U/min

# Performance-Vergleich:
# Rekursiv (n=30): ~2-3 Sekunden
# Iterativ (n=30): < 0.001 Sekunden
# Memo (n=30): ~0.001 Sekunden
```

**Hinweise**:
- Fibonacci-Drehzahlen eignen sich für systematische Tests
- Die iterative Lösung ist O(n) vs. rekursiv O(2^n)
- Memoization reduziert redundante Berechnungen

---

### Aufgabe P5: Produktionsreihenfolge-Optimierer mit Sortieralgorithmen (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 50-60 Minuten  
**Vorkenntnisse**: Funktionen, Schleifen, Listen, Algorithmen  
**Maschinenbau-Kontext**: Fertigungsplanung mit Prioritäts-Sortierung

Implementiere ein Programm, das Fertigungsaufträge nach verschiedenen Kriterien sortiert und die Algorithmen-Performance visualisiert.

> [!NOTE]
> **Produktionsreihenfolge**: In der Fertigung müssen Aufträge priorisiert werden nach:
> - **Liefertermin** (Earliest Due Date - EDD)
> - **Bearbeitungszeit** (Shortest Processing Time - SPT)
> - **Priorität** (kritische Kunden, Eilaufträge)
> - **Setup-Zeit** (ähnliche Werkzeuge/Materialien zusammen)
> 
> Optimale Reihenfolge minimiert Durchlaufzeit und Terminüberschreitungen.

**Anforderungen**:

**a)** Implementiere Sortieralgorithmen für Fertigungsaufträge:
```python
# Datenstruktur: Auftrag
auftrag = {
    "id": "A001",
    "bearbeitungszeit_min": 45,
    "prioritaet": 2,  # 1=hoch, 2=mittel, 3=niedrig
    "liefertermin_tage": 5
}
```

- `bubble_sort_auftraege(auftraege, kriterium)`: Sortiert nach Kriterium (z.B. "bearbeitungszeit_min")
- `selection_sort_auftraege(auftraege, kriterium)`: Alternative Sortierung
- Hilfsfunktion: `tausche(liste, i, j)`

**b)** Erweitere um **Tracing und Statistiken**:
- Zähle Vergleiche und Tauschoperationen
- Gib nach jedem Tausch den Zustand aus (Auftrags-IDs)
- Berechne Gesamt-Durchlaufzeit

**c)** Hauptprogramm mit Produktionsdaten:
```python
auftraege = [
    {"id": "A001", "bearbeitungszeit_min": 64, "prioritaet": 2, "liefertermin_tage": 10},
    {"id": "A002", "bearbeitungszeit_min": 34, "prioritaet": 1, "liefertermin_tage": 3},
    {"id": "A003", "bearbeitungszeit_min": 25, "prioritaet": 3, "liefertermin_tage": 15},
    {"id": "A004", "bearbeitungszeit_min": 12, "prioritaet": 1, "liefertermin_tage": 2},
    {"id": "A005", "bearbeitungszeit_min": 22, "prioritaet": 2, "liefertermin_tage": 7},
]

# Sortiere nach Bearbeitungszeit (SPT-Regel)
sortiert, stats = bubble_sort_auftraege(auftraege.copy(), "bearbeitungszeit_min")
print(f"SPT-Reihenfolge: {[a['id'] for a in sortiert]}")
print(f"Statistik: {stats['vergleiche']} Vergleiche, {stats['tausche']} Tauschvorgänge")

# Sortiere nach Liefertermin (EDD-Regel)
sortiert, stats = selection_sort_auftraege(auftraege.copy(), "liefertermin_tage")
print(f"EDD-Reihenfolge: {[a['id'] for a in sortiert]}")
```

**Beispiel Ein-/Ausgabe**:
```
=== BUBBLE SORT: Bearbeitungszeit (SPT) ===
Start: [A001, A002, A003, A004, A005]
Schritt 1: Tausche A001 ↔ A002 → [A002, A001, A003, A004, A005]
Schritt 2: Tausche A001 ↔ A003 → [A002, A003, A001, A004, A005]
...
Sortiert: [A004, A005, A003, A002, A001]
Gesamt-Durchlaufzeit: 157 Minuten
Vergleiche: 10, Tauschvorgänge: 6

=== SELECTION SORT: Liefertermin (EDD) ===
Sortiert: [A004, A002, A005, A001, A003]
Durchlaufzeit: 157 Minuten
Vergleiche: 10, Tauschvorgänge: 4
```

**Bonus-Challenge**:
- Implementiere **Quick Sort** für große Auftragsmengen (>100 Aufträge)
- Füge Visualisierung mit Gantt-Chart (ASCII-Art) hinzu
- Berechne Verspätungen: `max(0, durchlaufzeit - liefertermin)`
- Erstelle Funktion `generiere_auftraege(anzahl)` für Testdaten

**Hinweise**:
- Verwende `.copy()` für Original-Erhaltung
- Selection Sort: Finde Minimum und tausche
- Dictionary für Stats: `{"vergleiche": 0, "tausche": 0}`
- Durchlaufzeit: Summe aller Bearbeitungszeiten

---

