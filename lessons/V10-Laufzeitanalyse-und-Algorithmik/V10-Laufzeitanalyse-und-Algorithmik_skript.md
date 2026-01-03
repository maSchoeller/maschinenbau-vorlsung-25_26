# V10: Laufzeitanalyse & Algorithmik

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Verstehen, wie man die Effizienz von Algorithmen misst und vergleicht
> - Die O-Notation (Big-O) sicher anwenden können, um Zeitkomplexität zu beschreiben
> - Unterschiede zwischen Best-Case, Average-Case und Worst-Case Szenarien erkennen
> - Einfache Algorithmen analysieren und deren Laufzeitverhalten bestimmen
> - Grundlegende Sortieralgorithmen (Bubble Sort, Quick Sort, Merge Sort) verstehen
> - Funktionen in Python definieren und mit Parametern sowie Rückgabewerten arbeiten
> - Default-Parameter verwenden, um flexible Funktionsschnittstellen zu schaffen
> - Funktionen als First-Class-Objekte verstehen und einsetzen können

---

## Teil 1: Theorie - Laufzeitanalyse & Algorithmik

### Überblick

Die Informatik beschäftigt sich nicht nur mit der Frage, *ob* ein Problem lösbar ist, sondern auch damit, *wie effizient* eine Lösung ist. Zwei Programme können dieselbe Aufgabe erfüllen, aber eines davon benötigt vielleicht Sekunden, während das andere Stunden läuft. Besonders bei großen Datenmengen, wie sie im Maschinenbau bei Simulationen oder Sensorauswertungen anfallen, ist die Effizienz entscheidend.

Die **Laufzeitanalyse** hilft dabei, die Effizienz von Algorithmen zu bewerten. Ein **Algorithmus** ist eine präzise, endliche Folge von Anweisungen zur Lösung eines Problems. Die Laufzeitanalyse ermöglicht es, Algorithmen unabhängig von der Hardware oder Programmiersprache zu vergleichen. Zentrale Werkzeuge dafür sind die O-Notation (Big-O), die beschreibt, wie sich die Laufzeit eines Algorithmus mit wachsender Eingabegröße verhält, sowie die Unterscheidung zwischen Best-Case, Average-Case und Worst-Case Szenarien.

> [!NOTE]
> **Algorithmus**: Eine eindeutige Handlungsvorschrift zur Lösung eines Problems. Ein Algorithmus besteht aus einer endlichen Anzahl von Schritten, die in einer festgelegten Reihenfolge ausgeführt werden, und transformiert Eingabedaten in Ausgabedaten.

---

### Warum Laufzeitanalyse?

Bei kleinen Datenmengen (z.B. 10 Elemente) spielt die Effizienz eines Algorithmus oft keine große Rolle. Ein langsamer Algorithmus benötigt vielleicht 0,001 Sekunden, ein schneller 0,0001 Sekunden – der Unterschied ist kaum spürbar. Bei großen Datenmengen (z.B. 1 Million Elemente) kann jedoch ein ineffizienter Algorithmus Stunden oder Tage benötigen, während ein effizienter nur Sekunden braucht.

Die Laufzeitanalyse erlaubt es, das Verhalten von Algorithmen bei wachsenden Eingabegrößen vorherzusagen. Statt konkrete Zeitmessungen durchzuführen, die von Hardware, Betriebssystem und Implementierung abhängen, betrachtet man die Anzahl der elementaren Operationen (z.B. Vergleiche, Zuweisungen, Additionen) in Abhängigkeit von der Eingabegröße $n$.

> [!TIP]
> **Beispiel**: Ein Sortieralgorithmus, der bei 100 Elementen 10.000 Vergleiche benötigt, wird bei 1.000 Elementen nicht einfach 100.000 Vergleiche benötigen – je nach Algorithmus kann die Zahl drastisch höher oder niedriger sein. Die O-Notation hilft, dieses Wachstumsverhalten präzise zu beschreiben.

---

### Die O-Notation (Big-O)

Die **O-Notation** (auch Big-O genannt) beschreibt die obere Schranke des Wachstums der Laufzeit eines Algorithmus in Abhängigkeit von der Eingabegröße $n$. Sie abstrahiert von konstanten Faktoren und kleineren Termen, um das wesentliche Wachstumsverhalten zu erfassen.

> [!NOTE]
> **O-Notation (Big-O)**: Eine mathematische Notation zur Beschreibung des asymptotischen Verhaltens von Funktionen. Für eine Funktion $f(n)$ bedeutet $f(n) = O(g(n))$, dass es Konstanten $c > 0$ und $n_0 > 0$ gibt, sodass $f(n) \leq c \cdot g(n)$ für alle $n \geq n_0$ gilt. In der Praxis beschreibt $O(g(n))$ die maximale Wachstumsrate der Laufzeit.

**Warum konstante Faktoren ignoriert werden**: Die O-Notation interessiert sich für das asymptotische Verhalten, d.h. das Verhalten bei sehr großen $n$. Konstante Faktoren (z.B. ob ein Algorithmus $5n$ oder $10n$ Operationen benötigt) werden nicht berücksichtigt, da sie bei wachsendem $n$ weniger relevant sind als das grundlegende Wachstumsmuster (z.B. linear vs. quadratisch).

**Warum kleinere Terme ignoriert werden**: Bei einer Funktion wie $f(n) = 3n^2 + 5n + 10$ dominiert der Term $3n^2$ für große $n$ alle anderen Terme. Die O-Notation fokussiert auf den dominierenden Term und schreibt $O(n^2)$.

#### Häufige Komplexitätsklassen

Die folgende Tabelle zeigt die wichtigsten Komplexitätsklassen, sortiert von am effizientesten zu am ineffizientesten:

| O-Notation | Name | Beispiel | Beschreibung |
|------------|------|----------|--------------|
| $O(1)$ | Konstant | Zugriff auf Array-Element `arr[5]` | Laufzeit unabhängig von $n$ |
| $O(\log n)$ | Logarithmisch | Binäre Suche | Halbiert Suchbereich in jedem Schritt |
| $O(n)$ | Linear | Durchsuchen einer Liste | Laufzeit wächst proportional zu $n$ |
| $O(n \log n)$ | Linearithmisch | Merge Sort, Quick Sort (average) | Effiziente Sortieralgorithmen |
| $O(n^2)$ | Quadratisch | Bubble Sort, verschachtelte Schleifen | Laufzeit wächst quadratisch |
| $O(n^3)$ | Kubisch | Matrix-Multiplikation (naiv) | Drei verschachtelte Schleifen |
| $O(2^n)$ | Exponentiell | Rekursive Fibonacci (naiv) | Unpraktikabel für große $n$ |
| $O(n!)$ | Faktoriell | Brute-Force Traveling Salesman | Nur für sehr kleine $n$ |

> [!TIP]
> **Veranschaulichung bei $n = 1.000$**:
> - $O(1)$: 1 Operation
> - $O(\log n)$: ca. 10 Operationen
> - $O(n)$: 1.000 Operationen
> - $O(n \log n)$: ca. 10.000 Operationen
> - $O(n^2)$: 1.000.000 Operationen
> - $O(2^n)$: $10^{301}$ Operationen (Universum hat nicht genug Atome!)

---

### Weitere Notationen: Omega und Theta

Neben der O-Notation gibt es auch **Omega-Notation** ($\Omega$) und **Theta-Notation** ($\Theta$):

> [!NOTE]
> **Omega-Notation ($\Omega$)**: Beschreibt die untere Schranke der Laufzeit. $f(n) = \Omega(g(n))$ bedeutet, dass $f(n)$ mindestens so schnell wächst wie $g(n)$. Dies ist das Best-Case-Szenario.

> [!NOTE]
> **Theta-Notation ($\Theta$)**: Beschreibt eine asymptotisch enge Schranke. $f(n) = \Theta(g(n))$ bedeutet, dass $f(n)$ sowohl $O(g(n))$ als auch $\Omega(g(n))$ ist. Die Laufzeit wächst exakt wie $g(n)$, sowohl im Best-Case als auch im Worst-Case.

In der Praxis wird meist die O-Notation verwendet, da sie das Worst-Case-Verhalten beschreibt, welches für die Systemauslegung am relevantesten ist.

---

### Best-Case, Average-Case, Worst-Case

Bei der Analyse von Algorithmen unterscheidet man drei Szenarien:

> [!NOTE]
> **Best-Case**: Das günstigste Eingabe-Szenario, bei dem der Algorithmus die wenigsten Operationen benötigt. Beispiel: Bei einer linearen Suche ist der Best-Case, dass das gesuchte Element an erster Position steht – nur eine Vergleichsoperation.

> [!NOTE]
> **Average-Case**: Das durchschnittliche Verhalten über alle möglichen Eingaben hinweg. Dies erfordert oft eine statistische Analyse und Annahmen über die Verteilung der Eingaben. Der Average-Case ist realistischer als der Best-Case, aber schwieriger zu berechnen.

> [!NOTE]
> **Worst-Case**: Das ungünstigste Eingabe-Szenario, bei dem der Algorithmus die meisten Operationen benötigt. Beispiel: Bei einer linearen Suche ist der Worst-Case, dass das gesuchte Element nicht vorhanden ist oder an letzter Position steht – $n$ Vergleichsoperationen.

Die Worst-Case-Analyse ist in der Praxis am wichtigsten, da sie garantiert, dass der Algorithmus niemals langsamer ist als angegeben. Für kritische Systeme (z.B. Echtzeitsysteme im Maschinenbau) muss sichergestellt sein, dass ein Algorithmus auch im Worst-Case schnell genug ist.

> [!TIP]
> **Beispiel - Lineare Suche**:
> ```
> Liste: [3, 7, 2, 9, 5]
> Suche nach 5:
> - Best-Case: Element ist an erster Position → 1 Vergleich
> - Average-Case: Element ist irgendwo in der Mitte → n/2 Vergleiche
> - Worst-Case: Element ist an letzter Position oder nicht vorhanden → n Vergleiche
> ```

---

### Analyse einfacher Algorithmen

Um die Laufzeit eines Algorithmus zu bestimmen, zählt man die elementaren Operationen in Abhängigkeit von der Eingabegröße $n$. Betrachten wir einige Beispiele:

#### Beispiel 1: Einfache Schleife

```python
def summe_bis_n(n):
    total = 0          # 1 Operation
    for i in range(n): # n Iterationen
        total += i     # 2 Operationen pro Iteration (Addition, Zuweisung)
    return total       # 1 Operation
```

**Analyse**:
- Initialisierung: 1 Operation
- Schleife läuft $n$-mal
- Pro Iteration: 2 Operationen
- Rückgabe: 1 Operation

Gesamt: $1 + n \cdot 2 + 1 = 2n + 2$ Operationen

**O-Notation**: $O(n)$ (konstante Faktoren und Terme ignoriert)

#### Beispiel 2: Verschachtelte Schleifen

```python
def summe_matrix(matrix):
    total = 0
    for zeile in matrix:        # n Iterationen (wenn Matrix n×n)
        for element in zeile:   # n Iterationen pro Zeile
            total += element    # 2 Operationen
    return total
```

**Analyse**:
- Äußere Schleife: $n$ Iterationen
- Innere Schleife: $n$ Iterationen pro äußerer Iteration
- Gesamt: $n \cdot n = n^2$ Iterationen

**O-Notation**: $O(n^2)$

#### Beispiel 3: Binäre Suche (Halbierungsstrategie)

```python
def binaere_suche(sortierte_liste, ziel):
    links, rechts = 0, len(sortierte_liste) - 1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if sortierte_liste[mitte] == ziel:
            return mitte
        elif sortierte_liste[mitte] < ziel:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return -1
```

**Analyse**:
- In jeder Iteration wird der Suchbereich halbiert
- Nach $k$ Iterationen: Suchbereich = $n / 2^k$
- Algorithmus endet, wenn Suchbereich = 1: $n / 2^k = 1 \Rightarrow k = \log_2(n)$

**O-Notation**: $O(\log n)$

> [!WARNING]
> **Häufiger Fehler**: Verwechslung von $O(n)$ und $O(\log n)$. Lineare Suche durchläuft alle Elemente (schlimmstenfalls), binäre Suche halbiert den Suchbereich in jedem Schritt. Bei 1.000 Elementen bedeutet das: Linear = 1.000 Vergleiche, Binär = ca. 10 Vergleiche.

---

### Rekursion und Rekursive Komplexität

**Rekursion** ist eine Programmiertechnik, bei der eine Funktion sich selbst aufruft. Rekursive Algorithmen können elegante Lösungen für Probleme liefern, haben aber oft eine höhere Laufzeitkomplexität als iterative Ansätze.

> [!NOTE]
> **Rekursion**: Eine Funktion, die sich selbst aufruft, um ein Problem in kleinere Teilprobleme derselben Art zu zerlegen. Rekursion benötigt eine Abbruchbedingung (Basisfall), sonst entsteht eine Endlosschleife.

#### Beispiel: Fibonacci-Zahlen (naiv rekursiv)

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Analyse**:
- Für `fibonacci(n)` werden `fibonacci(n-1)` und `fibonacci(n-2)` aufgerufen
- Jeder Aufruf verzweigt sich in zwei weitere Aufrufe
- Ergibt einen binären Baum mit Höhe $n$
- Anzahl der Aufrufe: ca. $2^n$

**O-Notation**: $O(2^n)$ – exponentiell!

> [!WARNING]
> **Exponentielles Wachstum bei naiver Rekursion**: Die naive rekursive Fibonacci-Implementierung ist extrem ineffizient. Für `n=40` werden bereits über 1 Milliarde Funktionsaufrufe benötigt! Optimierte Varianten (z.B. mit Memoization oder iterativ) erreichen $O(n)$.

---

### Sortieralgorithmen im Vergleich

Sortieralgorithmen sind ein klassisches Beispiel zur Illustration unterschiedlicher Komplexitätsklassen. Wir betrachten drei grundlegende Algorithmen:

#### Bubble Sort

**Bubble Sort** vergleicht benachbarte Elemente und vertauscht sie, wenn sie in falscher Reihenfolge sind. Dieser Prozess wird wiederholt, bis keine Vertauschungen mehr nötig sind.

```python
def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
```

**Analyse**:
- Äußere Schleife: $n$ Durchläufe
- Innere Schleife: Im ersten Durchlauf $n-1$ Vergleiche, im zweiten $n-2$, etc.
- Gesamt: $(n-1) + (n-2) + \ldots + 1 = \frac{n(n-1)}{2} = \frac{n^2 - n}{2}$

**Komplexität**:
- **Best-Case**: $O(n)$ (Liste bereits sortiert, mit Optimierung)
- **Average-Case**: $O(n^2)$
- **Worst-Case**: $O(n^2)$

> [!NOTE]
> **Bubble Sort**: Ein einfacher, aber ineffizienter Sortieralgorithmus. Der Name kommt daher, dass große Elemente wie Blasen nach oben "blubbern". Bubble Sort ist stabil (erhält die Reihenfolge gleicher Elemente) und benötigt keinen zusätzlichen Speicher (in-place).

#### Quick Sort

**Quick Sort** wählt ein Pivot-Element und partitioniert die Liste in Elemente kleiner und größer als das Pivot. Anschließend wird rekursiv auf beide Teilbereiche Quick Sort angewendet.

```python
def quick_sort(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[len(liste) // 2]
    links = [x for x in liste if x < pivot]
    mitte = [x for x in liste if x == pivot]
    rechts = [x for x in liste if x > pivot]
    return quick_sort(links) + mitte + quick_sort(rechts)
```

**Analyse**:
- Im besten Fall wird die Liste immer in zwei gleich große Hälften geteilt
- Rekursionstiefe: $\log n$
- Pro Ebene: $O(n)$ Operationen (Partitionierung)
- Gesamt: $O(n \log n)$

**Komplexität**:
- **Best-Case**: $O(n \log n)$ (Pivot teilt Liste optimal)
- **Average-Case**: $O(n \log n)$
- **Worst-Case**: $O(n^2)$ (Pivot ist immer das kleinste/größte Element, z.B. bei bereits sortierter Liste mit schlechter Pivot-Wahl)

> [!NOTE]
> **Quick Sort**: Ein sehr effizienter Sortieralgorithmus, der im Durchschnitt $O(n \log n)$ erreicht. Quick Sort ist nicht stabil und arbeitet in-place (kann mit geringem zusätzlichem Speicher implementiert werden). Die Wahl des Pivots beeinflusst die Performance stark – gute Implementierungen verwenden randomisierte Pivots oder den Median-of-Three-Ansatz.

#### Merge Sort

**Merge Sort** teilt die Liste rekursiv in zwei Hälften, sortiert diese und verschmilzt (merged) sie anschließend.

```python
def merge_sort(liste):
    if len(liste) <= 1:
        return liste
    
    mitte = len(liste) // 2
    links = merge_sort(liste[:mitte])
    rechts = merge_sort(liste[mitte:])
    
    return merge(links, rechts)

def merge(links, rechts):
    ergebnis = []
    i = j = 0
    while i < len(links) and j < len(rechts):
        if links[i] < rechts[j]:
            ergebnis.append(links[i])
            i += 1
        else:
            ergebnis.append(rechts[j])
            j += 1
    ergebnis.extend(links[i:])
    ergebnis.extend(rechts[j:])
    return ergebnis
```

**Analyse**:
- Rekursionstiefe: $\log n$ (Liste wird immer halbiert)
- Pro Ebene: $O(n)$ Operationen (Mergen)
- Gesamt: $O(n \log n)$

**Komplexität**:
- **Best-Case**: $O(n \log n)$
- **Average-Case**: $O(n \log n)$
- **Worst-Case**: $O(n \log n)$ (garantiert!)

> [!NOTE]
> **Merge Sort**: Ein stabiler Sortieralgorithmus mit garantierter $O(n \log n)$ Laufzeit in allen Fällen. Der Nachteil ist der zusätzliche Speicherbedarf von $O(n)$ für die temporären Listen beim Mergen. Merge Sort ist die Basis für viele moderne Sortieralgorithmen (z.B. Timsort in Python).

#### Vergleich der Sortieralgorithmen

| Algorithmus | Best-Case | Average-Case | Worst-Case | Speicher | Stabil |
|-------------|-----------|--------------|------------|----------|--------|
| Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Ja |
| Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | Nein |
| Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | Ja |

> [!TIP]
> **Praktische Empfehlung**: 
> - Für kleine Datenmengen (< 50 Elemente): Einfache Algorithmen wie Insertion Sort sind ausreichend
> - Für große Datenmengen: Verwende Merge Sort oder Quick Sort
> - In Python: Nutze `sorted()` oder `.sort()` – diese verwenden Timsort, einen hybriden Algorithmus (Merge Sort + Insertion Sort) mit $O(n \log n)$ im Worst-Case

---

### Praktische Bedeutung für den Maschinenbau

Im Maschinenbau fallen häufig große Datenmengen an:

- **Simulation**: Finite-Elemente-Analysen generieren Millionen von Datenpunkten
- **Sensorik**: Messdaten von Sensoren müssen in Echtzeit verarbeitet werden
- **Optimierung**: Parameteroptimierung erfordert das Testen vieler Kombinationen
- **Bildverarbeitung**: Kamerabilder in der Qualitätskontrolle müssen schnell analysiert werden

Die Wahl des richtigen Algorithmus kann den Unterschied zwischen praktischer Nutzbarkeit und Unpraktikabilität bedeuten. Ein ineffizienter Algorithmus mit $O(n^2)$ kann bei 1 Million Datenpunkten Stunden benötigen, während ein effizienter mit $O(n \log n)$ nur Sekunden braucht.

> [!WARNING]
> **Vorzeitige Optimierung vermeiden**: Donald Knuth sagte: "Premature optimization is the root of all evil." Optimiere erst, wenn ein Performance-Problem identifiziert ist. Schreibe zuerst lesbaren, korrekten Code. Profiling-Tools helfen, Engpässe zu identifizieren.

---

### Zusammenfassung Theorie

Die Laufzeitanalyse ist ein zentrales Werkzeug zur Bewertung der Effizienz von Algorithmen. Die O-Notation abstrahiert von Hardware-Details und ermöglicht den Vergleich von Algorithmen unabhängig von der konkreten Implementierung. Konstante Faktoren werden ignoriert, da das asymptotische Wachstum bei großen Eingabegrößen dominiert.

Die wichtigsten Komplexitätsklassen sind $O(1)$ (konstant), $O(\log n)$ (logarithmisch), $O(n)$ (linear), $O(n \log n)$ (linearithmisch), $O(n^2)$ (quadratisch) und $O(2^n)$ (exponentiell). Effiziente Algorithmen haben meist $O(n \log n)$ oder besser, während $O(n^2)$ und höher bei großen Datenmengen problematisch werden.

Best-Case, Average-Case und Worst-Case beschreiben das Verhalten unter verschiedenen Eingabebedingungen. Die Worst-Case-Analyse ist in der Praxis am wichtigsten, da sie garantierte obere Schranken liefert.

Sortieralgorithmen illustrieren die Unterschiede zwischen Komplexitätsklassen: Bubble Sort ist einfach, aber ineffizient ($O(n^2)$), während Quick Sort und Merge Sort im Durchschnitt $O(n \log n)$ erreichen. Merge Sort garantiert diese Laufzeit auch im Worst-Case, benötigt aber zusätzlichen Speicher.

Rekursive Algorithmen können elegant sein, bergen aber Risiken: Naive rekursive Implementierungen (z.B. Fibonacci) können exponentielles Wachstum aufweisen. Optimierungen wie Memoization oder iterative Varianten sind dann notwendig.

Die Wahl des richtigen Algorithmus ist entscheidend für die praktische Nutzbarkeit, insbesondere bei großen Datenmengen im Maschinenbau. Profiling-Tools helfen, Performance-Engpässe zu identifizieren, bevor vorzeitige Optimierung betrieben wird.

---

## Teil 2: Python-Praxis - Methoden/Funktionen – Teil 1

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

Funktionen sind eines der fundamentalsten Werkzeuge der Programmierung. Sie ermöglichen es, Code zu strukturieren, wiederverwendbar zu machen und komplexe Probleme in kleinere, verständliche Einheiten zu zerlegen. In dieser Lektion lernen wir, eigene Funktionen in Python zu definieren und anzuwenden.

Eine **Funktion** ist ein benannter Codeblock, der eine spezifische Aufgabe erfüllt. Funktionen können Parameter (Eingaben) entgegen nehmen, Operationen durchführen und Ergebnisse (Ausgaben) zurückgeben. Durch die Verwendung von Funktionen wird Code lesbarer, wartbarer und testbarer. Statt denselben Code mehrfach zu schreiben, definiert man ihn einmal in einer Funktion und ruft diese bei Bedarf auf – das entspricht dem DRY-Prinzip ("Don't Repeat Yourself") aus V07.

In dieser ersten von zwei Vorlesungen über Funktionen konzentrieren wir uns auf die Grundlagen: Funktionsdefinition, Parameter, Rückgabewerte und Default-Parameter. In V11 werden wir fortgeschrittenere Konzepte wie `*args`, `**kwargs`, Lambda-Funktionen und Type Hints behandeln.

> [!NOTE]
> **Funktion (Function)**: Ein wiederverwendbarer Codeblock, der eine spezifische Aufgabe erfüllt. Funktionen werden mit dem Schlüsselwort `def` definiert, haben einen Namen, können Parameter entgegennehmen und Werte zurückgeben.

---

### Funktionen definieren mit `def`

In Python werden Funktionen mit dem Schlüsselwort `def` (define) definiert. Die grundlegende Syntax lautet:

```python
def funktionsname(parameter1, parameter2):
    """Docstring: Beschreibt, was die Funktion macht."""
    # Funktionskörper
    anweisung1
    anweisung2
    return ergebnis
```

**Bestandteile**:
1. **`def`**: Schlüsselwort zur Funktionsdefinition
2. **Funktionsname**: Benenne Funktionen aussagekräftig mit `snake_case`
3. **Parameter**: Eingabewerte in Klammern (optional, kann leer sein)
4. **Doppelpunkt**: Leitet den Funktionskörper ein
5. **Docstring**: Optional, aber empfohlen – dokumentiert die Funktion
6. **Funktionskörper**: Eingerückter Code (4 Leerzeichen)
7. **`return`**: Optional – gibt einen Wert zurück

> [!TIP]
> **Beispiel: Einfache Funktion ohne Parameter**
> ```python
> def gruesse():
>     """Gibt eine Begrüßung aus."""
>     print("Hallo, willkommen in der Vorlesung!")
> 
> # Funktionsaufruf
> gruesse()  # Ausgabe: Hallo, willkommen in der Vorlesung!
> ```

> [!TIP]
> **Beispiel: Funktion mit Parametern**
> ```python
> def berechne_flaeche(laenge, breite):
>     """Berechnet die Fläche eines Rechtecks."""
>     flaeche = laenge * breite
>     return flaeche
> 
> # Funktionsaufruf
> ergebnis = berechne_flaeche(5, 3)
> print(f"Fläche: {ergebnis}")  # Ausgabe: Fläche: 15
> ```

**Wichtige Regeln**:
- Funktionsnamen folgen denselben Regeln wie Variablennamen (Buchstaben, Ziffern, Unterstrich; nicht mit Ziffer beginnen)
- Verwende aussagekräftige Namen: `berechne_volumen()` statt `func1()`
- Konvention: `snake_case` für Funktionsnamen
- Der Funktionskörper muss eingerückt sein

> [!WARNING]
> **Häufiger Fehler**: Funktionsdefinition ohne Doppelpunkt führt zu `SyntaxError`:
> ```python
> def meine_funktion()  # Falsch: Doppelpunkt fehlt!
>     print("Test")
> ```

---

### Parameter und Argumente

**Parameter** sind Variablen in der Funktionsdefinition, die Eingabewerte entgegennehmen. **Argumente** sind die konkreten Werte, die beim Funktionsaufruf übergeben werden.

```python
def addiere(a, b):  # a und b sind Parameter
    return a + b

ergebnis = addiere(5, 3)  # 5 und 3 sind Argumente
```

> [!NOTE]
> **Parameter vs. Argumente**: **Parameter** sind Platzhalter in der Funktionsdefinition. **Argumente** sind die tatsächlichen Werte, die beim Aufruf übergeben werden. Oft werden die Begriffe synonym verwendet, technisch gibt es aber einen Unterschied.

#### Positional Arguments (Positionale Argumente)

Standardmäßig werden Argumente in der Reihenfolge zugeordnet, in der sie übergeben werden:

```python
def beschreibe_person(name, alter, beruf):
    print(f"{name} ist {alter} Jahre alt und arbeitet als {beruf}.")

beschreibe_person("Alice", 30, "Ingenieurin")
# Ausgabe: Alice ist 30 Jahre alt und arbeitet als Ingenieurin.
```

> [!WARNING]
> **Reihenfolge ist entscheidend**: Wenn du die Reihenfolge vertauschst, kann das zu unerwarteten Ergebnissen führen:
> ```python
> beschreibe_person(30, "Alice", "Ingenieurin")
> # Ausgabe: 30 ist Alice Jahre alt und arbeitet als Ingenieurin.
> # Falsch! Reihenfolge wurde vertauscht.
> ```

#### Keyword Arguments (Benannte Argumente)

Argumente können auch mit ihrem Parameter-Namen übergeben werden. Das macht den Code lesbarer und unabhängig von der Reihenfolge:

```python
beschreibe_person(name="Bob", beruf="Maschinenbauer", alter=28)
# Reihenfolge spielt keine Rolle!
# Ausgabe: Bob ist 28 Jahre alt und arbeitet als Maschinenbauer.
```

**Best Practice**: Verwende Keyword Arguments für bessere Lesbarkeit, besonders bei vielen Parametern:

```python
# Weniger lesbar:
ergebnis = berechne_kraft(9.81, 10, 0.5, True)

# Besser lesbar:
ergebnis = berechne_kraft(beschleunigung=9.81, masse=10, reibung=0.5, inklusive_luftwiderstand=True)
```

---

### Rückgabewerte mit `return`

Funktionen können Werte mit dem `return`-Statement zurückgeben. Das Programm springt nach `return` sofort aus der Funktion heraus.

> [!NOTE]
> **`return`-Statement**: Beendet die Funktionsausführung und gibt optional einen Wert an den Aufrufer zurück. Ohne `return` gibt eine Funktion implizit `None` zurück.

> [!TIP]
> **Beispiel: Funktion mit Rückgabewert**
> ```python
> def quadrat(x):
>     """Berechnet das Quadrat einer Zahl."""
>     return x ** 2
> 
> ergebnis = quadrat(5)
> print(ergebnis)  # Ausgabe: 25
> ```

#### Mehrere Rückgabewerte

Python ermöglicht es, mehrere Werte gleichzeitig zurückzugeben (als Tupel):

```python
def kreisberechnung(radius):
    """Berechnet Umfang und Fläche eines Kreises."""
    import math
    umfang = 2 * math.pi * radius
    flaeche = math.pi * radius ** 2
    return umfang, flaeche  # Gibt Tupel zurück

u, f = kreisberechnung(5)
print(f"Umfang: {u:.2f}, Fläche: {f:.2f}")
# Ausgabe: Umfang: 31.42, Fläche: 78.54
```

> [!TIP]
> **Unpacking bei mehreren Rückgabewerten**:
> ```python
> # Variante 1: Unpacking in separate Variablen
> umfang, flaeche = kreisberechnung(5)
> 
> # Variante 2: Als Tupel empfangen
> ergebnis = kreisberechnung(5)
> print(ergebnis)  # (31.41592653589793, 78.53981633974483)
> print(ergebnis[0])  # Umfang
> print(ergebnis[1])  # Fläche
> ```

#### Funktionen ohne explizites `return`

Wenn eine Funktion kein `return`-Statement hat oder `return` ohne Wert aufgerufen wird, gibt sie implizit `None` zurück:

```python
def sage_hallo(name):
    print(f"Hallo, {name}!")
    # Kein return-Statement

ergebnis = sage_hallo("Alice")
print(ergebnis)  # Ausgabe: None
```

> [!WARNING]
> **Häufiger Fehler**: `print()` ist kein `return`!
> ```python
> def addiere_falsch(a, b):
>     print(a + b)  # Gibt nichts zurück, nur Ausgabe!
> 
> ergebnis = addiere_falsch(3, 4)
> # Ausgabe: 7
> print(ergebnis)  # None (Funktion gibt nichts zurück!)
> 
> # Richtig:
> def addiere_richtig(a, b):
>     return a + b
> 
> ergebnis = addiere_richtig(3, 4)
> print(ergebnis)  # 7
> ```

---

### Default-Parameter (Standardwerte)

Funktionen können Default-Werte für Parameter definieren. Diese werden verwendet, wenn beim Aufruf kein Argument übergeben wird.

> [!NOTE]
> **Default-Parameter**: Parameter mit vordefinierten Werten in der Funktionsdefinition. Wenn beim Funktionsaufruf kein Argument für diesen Parameter übergeben wird, wird der Default-Wert verwendet.

> [!TIP]
> **Beispiel: Funktion mit Default-Parametern**
> ```python
> def gruesse(name, grusskarte="Hallo"):
>     """Begrüßt eine Person mit anpassbarer Grußformel."""
>     print(f"{grusskarte}, {name}!")
> 
> # Aufruf mit Default-Wert
> gruesse("Alice")  # Ausgabe: Hallo, Alice!
> 
> # Aufruf mit eigenem Wert
> gruesse("Bob", "Guten Tag")  # Ausgabe: Guten Tag, Bob!
> 
> # Aufruf mit Keyword Argument
> gruesse("Charlie", grusskarte="Moin")  # Ausgabe: Moin, Charlie!
> ```

**Wichtige Regeln**:
1. **Parameter mit Default-Werten müssen nach Parametern ohne Default stehen**:
   ```python
   # Richtig:
   def funktion(a, b, c=10, d=20):
       pass
   
   # Falsch:
   def funktion(a, c=10, b, d=20):  # SyntaxError!
       pass
   ```

2. **Default-Werte werden nur einmal bei Funktionsdefinition ausgewertet**:
   ```python
   def funktion(x=[]):  # Vorsicht: Liste wird nur einmal erstellt!
       x.append(1)
       return x
   
   print(funktion())  # [1]
   print(funktion())  # [1, 1] – Dieselbe Liste!
   ```

> [!WARNING]
> **Mutable Default-Werte vermeiden**: Verwende niemals mutable Objekte (Listen, Dictionaries) als Default-Werte:
> ```python
> # Falsch:
> def fuege_element_hinzu(element, liste=[]):
>     liste.append(element)
>     return liste
> 
> print(fuege_element_hinzu(1))  # [1]
> print(fuege_element_hinzu(2))  # [1, 2] – Unerwartetes Verhalten!
> 
> # Richtig:
> def fuege_element_hinzu(element, liste=None):
>     if liste is None:
>         liste = []
>     liste.append(element)
>     return liste
> 
> print(fuege_element_hinzu(1))  # [1]
> print(fuege_element_hinzu(2))  # [2] – Neue Liste jedes Mal
> ```

#### Praktisches Beispiel: Funktion mit mehreren Default-Parametern

```python
def berechne_zinseszins(kapital, zinssatz=0.05, jahre=10):
    """
    Berechnet das Endkapital nach Zinseszins.
    
    kapital: Anfangskapital in Euro
    zinssatz: Jährlicher Zinssatz (Standard: 5% = 0.05)
    jahre: Anlagedauer in Jahren (Standard: 10)
    """
    endkapital = kapital * (1 + zinssatz) ** jahre
    return endkapital

# Verschiedene Aufrufvarianten:
print(berechne_zinseszins(1000))  # Standard: 5%, 10 Jahre
# Ausgabe: 1628.89

print(berechne_zinseszins(1000, 0.03))  # 3%, 10 Jahre
# Ausgabe: 1343.92

print(berechne_zinseszins(1000, zinssatz=0.07, jahre=5))  # 7%, 5 Jahre
# Ausgabe: 1402.55
```

---

### Funktionen als First-Class-Objekte

In Python sind Funktionen "First-Class-Objekte" (First-Class Citizens). Das bedeutet, dass Funktionen wie jede andere Variable behandelt werden können:

> [!NOTE]
> **First-Class-Objekte**: Objekte, die zur Laufzeit dynamisch erzeugt, als Argument übergeben, als Rückgabewert zurückgegeben und Variablen zugewiesen werden können. In Python sind Funktionen First-Class-Objekte.

1. **Funktionen können Variablen zugewiesen werden**:
   ```python
   def addiere(a, b):
       return a + b
   
   # Funktion einer Variable zuweisen
   rechne = addiere
   print(rechne(3, 4))  # Ausgabe: 7
   ```

2. **Funktionen können als Argumente übergeben werden**:
   ```python
   def wende_operation_an(funktion, a, b):
       """Wendet eine übergebene Funktion auf zwei Werte an."""
       return funktion(a, b)
   
   def multipliziere(x, y):
       return x * y
   
   ergebnis = wende_operation_an(multipliziere, 5, 3)
   print(ergebnis)  # Ausgabe: 15
   ```

3. **Funktionen können als Rückgabewerte zurückgegeben werden**:
   ```python
   def erzeuge_multiplikator(faktor):
       """Gibt eine Funktion zurück, die mit 'faktor' multipliziert."""
       def multipliziere(x):
           return x * faktor
       return multipliziere
   
   verdopple = erzeuge_multiplikator(2)
   verdreifache = erzeuge_multiplikator(3)
   
   print(verdopple(10))  # Ausgabe: 20
   print(verdreifache(10))  # Ausgabe: 30
   ```

> [!TIP]
> **Praktische Anwendung – Sortierung mit `key`-Parameter**:
> Die `sorted()`-Funktion und `.sort()`-Methode akzeptieren einen `key`-Parameter, der eine Funktion ist:
> ```python
> # Sortiere nach Länge der Strings
> woerter = ["Python", "ist", "eine", "tolle", "Sprache"]
> sortiert = sorted(woerter, key=len)
> print(sortiert)  # ['ist', 'eine', 'tolle', 'Python', 'Sprache']
> 
> # Sortiere Tupel nach zweitem Element
> punkte = [(1, 5), (3, 2), (2, 8)]
> sortiert = sorted(punkte, key=lambda x: x[1])
> print(sortiert)  # [(3, 2), (1, 5), (2, 8)]
> ```
> (Lambda-Funktionen werden in V11 ausführlich behandelt)

---

### Scope und Variablen-Sichtbarkeit

Variablen innerhalb einer Funktion sind **lokal** und außerhalb nicht sichtbar. Variablen außerhalb von Funktionen sind **global**.

> [!NOTE]
> **Lokaler Scope**: Variablen, die innerhalb einer Funktion definiert werden, existieren nur während der Funktionsausführung und sind außerhalb nicht sichtbar.

> [!NOTE]
> **Globaler Scope**: Variablen, die außerhalb aller Funktionen definiert werden, sind im gesamten Programm sichtbar.

> [!TIP]
> **Beispiel: Lokale vs. Globale Variablen**
> ```python
> x = 10  # Globale Variable
> 
> def meine_funktion():
>     x = 5  # Lokale Variable (überdeckt die globale)
>     print(f"Innerhalb der Funktion: x = {x}")
> 
> meine_funktion()  # Ausgabe: Innerhalb der Funktion: x = 5
> print(f"Außerhalb der Funktion: x = {x}")  # Ausgabe: Außerhalb der Funktion: x = 10
> ```

#### LEGB-Regel

Python sucht Variablen in folgender Reihenfolge:
1. **L**ocal: Lokaler Scope (innerhalb der aktuellen Funktion)
2. **E**nclosing: Umschließender Scope (bei verschachtelten Funktionen)
3. **G**lobal: Globaler Scope (Modul-Ebene)
4. **B**uilt-in: Eingebaute Namen (z.B. `print`, `len`)

> [!WARNING]
> **`global`-Keyword sparsam verwenden**: Wie in V03 erwähnt, sollten globale Variablen vermieden werden. Bevorzuge Parameter und Rückgabewerte:
> ```python
> # Nicht empfohlen:
> counter = 0
> 
> def increment():
>     global counter
>     counter += 1
> 
> # Besser:
> def increment(counter):
>     return counter + 1
> 
> counter = 0
> counter = increment(counter)
> ```

---

### Docstrings: Funktionen dokumentieren

Docstrings sind mehrzeilige Strings, die direkt nach der Funktionsdefinition stehen und die Funktion dokumentieren. Sie sind über `help(funktionsname)` oder `funktionsname.__doc__` abrufbar.

> [!NOTE]
> **Docstring**: Ein String-Literal, das direkt nach der Funktionsdefinition steht und die Funktion dokumentiert. Docstrings verwenden Triple Quotes (`"""..."""`) und beschreiben, was die Funktion macht, welche Parameter sie hat und was sie zurückgibt.

> [!TIP]
> **Beispiel: Gut dokumentierte Funktion**
> ```python
> def berechne_bmi(gewicht, groesse):
>     """
>     Berechnet den Body-Mass-Index (BMI).
>     
>     Parameter:
>         gewicht (float): Körpergewicht in Kilogramm
>         groesse (float): Körpergröße in Metern
>     
>     Rückgabewert:
>         float: BMI-Wert (Gewicht / Größe²)
>     
>     Beispiel:
>         >>> berechne_bmi(70, 1.75)
>         22.86
>     """
>     return gewicht / (groesse ** 2)
> 
> # Docstring abrufen:
> print(berechne_bmi.__doc__)
> help(berechne_bmi)
> ```

**Best Practices für Docstrings**:
1. Beschreibe, **was** die Funktion macht (nicht **wie**)
2. Liste alle Parameter mit Typ und Bedeutung
3. Beschreibe den Rückgabewert
4. Füge bei Bedarf Beispiele hinzu
5. Erwähne mögliche Exceptions (z.B. `ValueError` bei ungültigen Eingaben)

---

### Praktische Anwendung: Algorithmik mit Funktionen

Funktionen sind das zentrale Werkzeug zur Strukturierung von Algorithmen. Betrachten wir die Sortieralgorithmen aus der Theorie als Python-Implementierungen:

#### Bubble Sort als Funktion

```python
def bubble_sort(liste):
    """
    Sortiert eine Liste mit dem Bubble-Sort-Algorithmus.
    
    Parameter:
        liste (list): Liste mit vergleichbaren Elementen
    
    Rückgabewert:
        list: Sortierte Kopie der Liste
    
    Zeitkomplexität: O(n²)
    """
    # Kopie erstellen, um Original nicht zu verändern
    sortierte_liste = liste.copy()
    n = len(sortierte_liste)
    
    for i in range(n):
        # Flag für Optimierung (frühzeitiger Abbruch)
        getauscht = False
        for j in range(0, n-i-1):
            if sortierte_liste[j] > sortierte_liste[j+1]:
                # Tausche benachbarte Elemente
                sortierte_liste[j], sortierte_liste[j+1] = sortierte_liste[j+1], sortierte_liste[j]
                getauscht = True
        # Wenn keine Tauschung stattfand, ist Liste sortiert
        if not getauscht:
            break
    
    return sortierte_liste

# Test:
zahlen = [64, 34, 25, 12, 22, 11, 90]
sortiert = bubble_sort(zahlen)
print(f"Original: {zahlen}")
print(f"Sortiert: {sortiert}")
```

#### Binäre Suche als Funktion

```python
def binaere_suche(sortierte_liste, ziel):
    """
    Sucht ein Element in einer sortierten Liste mit binärer Suche.
    
    Parameter:
        sortierte_liste (list): Sortierte Liste mit vergleichbaren Elementen
        ziel: Das gesuchte Element
    
    Rückgabewert:
        int: Index des Elements, oder -1 wenn nicht gefunden
    
    Zeitkomplexität: O(log n)
    Voraussetzung: Liste muss sortiert sein!
    """
    links, rechts = 0, len(sortierte_liste) - 1
    
    while links <= rechts:
        mitte = (links + rechts) // 2
        
        if sortierte_liste[mitte] == ziel:
            return mitte  # Gefunden!
        elif sortierte_liste[mitte] < ziel:
            links = mitte + 1  # Suche in rechter Hälfte
        else:
            rechts = mitte - 1  # Suche in linker Hälfte
    
    return -1  # Nicht gefunden

# Test:
zahlen = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
index = binaere_suche(zahlen, 11)
print(f"Element 11 gefunden an Index: {index}")  # 5

index = binaere_suche(zahlen, 8)
print(f"Element 8 gefunden an Index: {index}")  # -1 (nicht vorhanden)
```

---

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: Funktion aufrufen, bevor sie definiert ist**
> 
> ```python
> # Falsch:
> ergebnis = addiere(3, 4)  # NameError: name 'addiere' is not defined
> 
> def addiere(a, b):
>     return a + b
> ```
> 
> **Lösung**: Definiere Funktionen immer vor ihrer Verwendung, oder rufe sie innerhalb anderer Funktionen auf (die erst später aufgerufen werden).

> [!WARNING]
> **Fehler 2: `return` vergessen**
> 
> ```python
> def quadrat(x):
>     x ** 2  # Fehlt: return!
> 
> ergebnis = quadrat(5)
> print(ergebnis)  # None
> ```
> 
> **Lösung**: Verwende `return`, um Werte zurückzugeben.

> [!WARNING]
> **Fehler 3: Funktion mit und ohne `return` verwechseln**
> 
> ```python
> # Funktion mit Seiteneffekt (print):
> def zeige_ergebnis(x):
>     print(x ** 2)
> 
> # Funktion mit Rückgabewert:
> def berechne_ergebnis(x):
>     return x ** 2
> 
> # Verwechslung:
> ergebnis = zeige_ergebnis(5)  # Gibt 25 aus, aber ergebnis ist None!
> print(ergebnis * 2)  # TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
> ```
> 
> **Lösung**: Unterscheide klar zwischen Funktionen, die Werte zurückgeben, und solchen, die nur Seiteneffekte haben.

> [!WARNING]
> **Fehler 4: Mutable Default-Werte**
> 
> ```python
> def fuege_hinzu(element, liste=[]):
>     liste.append(element)
>     return liste
> 
> print(fuege_hinzu(1))  # [1]
> print(fuege_hinzu(2))  # [1, 2] – Unerwartetes Verhalten!
> ```
> 
> **Lösung**: Verwende `None` als Default und erstelle neue Objekte im Funktionskörper:
> ```python
> def fuege_hinzu(element, liste=None):
>     if liste is None:
>         liste = []
>     liste.append(element)
>     return liste
> ```

> [!WARNING]
> **Fehler 5: Falsche Parameterreihenfolge**
> 
> ```python
> def berechne_kraft(masse, beschleunigung=9.81):
>     return masse * beschleunigung
> 
> # Falsch:
> kraft = berechne_kraft(beschleunigung=5, 10)  # SyntaxError!
> ```
> 
> **Lösung**: Positionale Argumente müssen vor Keyword-Argumenten stehen:
> ```python
> kraft = berechne_kraft(10, beschleunigung=5)  # Richtig
> ```

---

### Zusammenfassung Python

Funktionen sind das zentrale Werkzeug zur Code-Strukturierung in Python. Sie ermöglichen wiederverwendbaren, lesbaren und testbaren Code. Eine Funktion wird mit `def` definiert, hat einen Namen, kann Parameter entgegennehmen und Werte mit `return` zurückgeben.

Parameter sind Platzhalter in der Funktionsdefinition, Argumente sind die konkreten Werte beim Aufruf. Python unterscheidet zwischen positionalen Argumenten (Reihenfolge wichtig) und Keyword-Argumenten (benannt, Reihenfolge egal). Default-Parameter ermöglichen optionale Argumente mit vordefinierten Werten, müssen aber nach Parametern ohne Default stehen.

Funktionen geben mit `return` Werte zurück. Mehrere Werte können als Tupel zurückgegeben werden. Ohne `return` gibt eine Funktion implizit `None` zurück. Wichtig: `print()` ist kein `return` – `print()` gibt nur aus, aber gibt keinen Wert zurück.

Python-Funktionen sind First-Class-Objekte: Sie können Variablen zugewiesen, als Argumente übergeben und als Rückgabewerte zurückgegeben werden. Dies ermöglicht mächtige Programmiertechniken wie Higher-Order Functions.

Variablen haben einen Scope: Lokale Variablen existieren nur innerhalb der Funktion, globale Variablen sind überall sichtbar. Die LEGB-Regel beschreibt die Reihenfolge der Namensauflösung. Vermeide das `global`-Keyword und bevorzuge Parameter/Rückgabewerte.

Docstrings dokumentieren Funktionen: Sie beschreiben, was die Funktion macht, welche Parameter sie hat und was sie zurückgibt. Gute Dokumentation ist essenziell für wartbaren Code.

Häufige Fehler umfassen vergessenes `return`, Verwechslung von Funktionen mit/ohne Rückgabewert, mutable Default-Werte und falsche Parameterreihenfolge. Diese lassen sich durch sorgfältige Planung und Tests vermeiden.

---

### Neue Python-Funktionen/Methoden

In dieser Vorlesung wurden folgende Python-Konzepte **neu eingeführt**:

#### Schlüsselwörter und Syntax

- **`def`-Statement** (Python Keyword)
  - Definiert eine Funktion
  - Syntax: `def funktionsname(parameter):`
  - Signatur: `def name(param1, param2=default):`
  - Beispiel: `def addiere(a, b): return a + b`

- **`return`-Statement** (Python Keyword)
  - Beendet Funktionsausführung und gibt Wert zurück
  - Syntax: `return wert` oder `return wert1, wert2` (Tupel)
  - Ohne Wert: `return` gibt `None` zurück
  - Signatur: `return [expression]`
  - Beispiel: `return x ** 2`

#### Konzepte

- **Funktionsdefinition**: Erstellen wiederverwendbarer Codeblöcke mit `def`
- **Parameter**: Platzhalter in der Funktionsdefinition
- **Argumente**: Konkrete Werte beim Funktionsaufruf
- **Positionale Argumente**: Reihenfolge beim Aufruf ist entscheidend
- **Keyword Arguments**: Benannte Argumente (Reihenfolge egal)
- **Default-Parameter**: Parameter mit Standardwerten (`def func(x=10)`)
- **Mehrere Rückgabewerte**: Return als Tupel (`return a, b`)
- **First-Class-Objekte**: Funktionen als Variablen, Argumente, Rückgabewerte
- **Lokaler vs. Globaler Scope**: Variablen-Sichtbarkeit
- **LEGB-Regel**: Local → Enclosing → Global → Built-in
- **Docstrings**: Funktionsdokumentation mit Triple Quotes

> [!NOTE]
> Lambda-Funktionen, `*args`, `**kwargs`, Type Hints und weitere fortgeschrittene Konzepte werden in V11 (Methoden/Funktionen – Teil 2) behandelt.

---

## Weiterführende Ressourcen

### Theorie

- **Introduction to Algorithms** (Cormen et al., MIT Press): Das Standardwerk zur Algorithmik
- **Grokking Algorithms** (Aditya Bhargava): Visuell ansprechende Einführung in Algorithmen
- **Big-O Cheat Sheet**: https://www.bigocheatsheet.com/ – Übersicht über Komplexitäten
- **VisuAlgo**: https://visualgo.net/ – Interaktive Visualisierungen von Algorithmen

### Python

- **Python Documentation - Defining Functions**: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- **Real Python - Defining Your Own Python Function**: https://realpython.com/defining-your-own-python-function/
- **PEP 257 - Docstring Conventions**: https://peps.python.org/pep-0257/
- **Python Function Arguments**: https://www.programiz.com/python-programming/function-argument

### Übungsmaterial

- **LeetCode**: https://leetcode.com/ – Algorithmus-Challenges (auch für Einsteiger)
- **HackerRank**: https://www.hackerrank.com/domains/python – Python-spezifische Übungen
- **Project Euler**: https://projecteuler.net/ – Mathematisch orientierte Programmier-Challenges

