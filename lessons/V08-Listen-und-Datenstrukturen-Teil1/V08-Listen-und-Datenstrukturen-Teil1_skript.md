# V08: Listen und Datenstrukturen – Teil 1

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Grundlegende Datenstrukturen verstehen: Arrays, verkettete Listen, Stacks, Queues
> - LIFO- und FIFO-Prinzipien erkennen und anwenden können
> - Vor- und Nachteile verschiedener Datenstrukturen analysieren
> - Python-Listen erstellen, manipulieren und effizient nutzen
> - Unterschiede zwischen Listen und Tupeln verstehen und korrekt einsetzen
> - List Slicing und fortgeschrittene Indexierungstechniken beherrschen

---

## Teil 1: Theorie - Listen und Datenstrukturen

### Überblick

Datenstrukturen bilden das Rückgrat jeder Software. Die richtige Wahl der Datenstruktur entscheidet über Effizienz, Wartbarkeit und Korrektheit eines Programms. Diese Vorlesung behandelt fundamentale sequenzielle Datenstrukturen, die in nahezu jedem Softwareprojekt zum Einsatz kommen.

Die Wahl der passenden Datenstruktur hängt von mehreren Faktoren ab: Wie häufig werden Elemente hinzugefügt oder entfernt? Muss der Zugriff auf beliebige Positionen schnell sein? Ist die Reihenfolge wichtig? Werden Duplikate zugelassen? Diese Fragen führen uns zu unterschiedlichen Datenstrukturen mit jeweils spezifischen Stärken und Schwächen.

### Arrays: Die Basis sequenzieller Datenstrukturen

Ein **Array** ist eine zusammenhängende Folge von Elementen gleichen Typs im Speicher. Jedes Element kann über seinen **Index** (Position) direkt angesprochen werden. Arrays sind die fundamentalste Form sequenzieller Datenspeicherung in der Informatik.

> [!NOTE]
> Ein **Array** ist eine Datenstruktur mit fester oder variabler Größe, die Elemente in zusammenhängendem Speicher ablegt. Der Zugriff auf ein Element erfolgt über einen numerischen Index in konstanter Zeit O(1).

#### Eigenschaften von Arrays

Die zentrale Stärke von Arrays liegt im **direkten Zugriff** (auch Random Access genannt). Wenn das Array an Speicheradresse `A` beginnt und jedes Element `s` Bytes groß ist, liegt das Element an Index `i` an der Adresse `A + i * s`. Diese Berechnung benötigt konstante Zeit, unabhängig von der Array-Größe.

Arrays haben eine feste Größe, die bei der Erzeugung festgelegt wird. In Sprachen wie C oder Java muss diese Größe im Voraus bekannt sein. Moderne Sprachen wie Python oder Java verwenden **dynamische Arrays**, die automatisch wachsen können, wenn mehr Platz benötigt wird. Intern wird dabei ein neues, größeres Array angelegt und alle Elemente kopiert.

> [!TIP]
> **Visualisierung eines Arrays:**
> ```
> Index:    0      1      2      3      4
>         ┌──────┬──────┬──────┬──────┬──────┐
> Array:  │  42  │  17  │  93  │   8  │  55  │
>         └──────┴──────┴──────┴──────┴──────┘
> Speicher: 1000  1004  1008  1012  1016  (bei 4 Bytes pro Element)
> ```

#### Zeitkomplexität von Array-Operationen

Die **Zeitkomplexität** beschreibt, wie die Laufzeit einer Operation mit der Größe der Datenstruktur wächst. Bei Arrays ergeben sich folgende Komplexitäten:

- **Zugriff auf Element an Index `i`**: O(1) – konstante Zeit, da die Adresse direkt berechnet werden kann
- **Suchen eines Elements**: O(n) – im schlimmsten Fall muss das gesamte Array durchlaufen werden
- **Einfügen am Ende** (bei dynamischen Arrays mit freiem Platz): O(1) amortisiert
- **Einfügen am Anfang oder in der Mitte**: O(n) – alle nachfolgenden Elemente müssen verschoben werden
- **Löschen am Ende**: O(1) – einfach die Größe reduzieren
- **Löschen am Anfang oder in der Mitte**: O(n) – alle nachfolgenden Elemente müssen nachrutschen

> [!WARNING]
> **Häufiger Denkfehler**: Viele Anfänger glauben, dass Einfügen in ein Array immer O(1) ist. Das stimmt nur für das Ende bei dynamischen Arrays mit freiem Platz. Einfügen in der Mitte erfordert das Verschieben aller nachfolgenden Elemente und ist daher O(n).

#### Vor- und Nachteile von Arrays

**Vorteile:**
- Sehr schneller Zugriff auf beliebige Elemente durch Index
- Speicher-effizient durch zusammenhängenden Speicherblock
- Cache-freundlich durch lokale Speicheranordnung
- Einfache Implementierung und Verwendung

**Nachteile:**
- Feste Größe bei statischen Arrays, teure Größenanpassung bei dynamischen Arrays
- Einfügen und Löschen in der Mitte ist ineffizient
- Keine flexible Größenanpassung ohne Kopieren
- Bei dynamischen Arrays kann ungenutzter Speicher verschwendet werden

### Verkettete Listen: Flexible Alternative zu Arrays

Eine **verkettete Liste** (Linked List) speichert Elemente nicht zusammenhängend, sondern verstreut im Speicher. Jedes Element (Knoten) enthält neben den Daten einen Verweis (Pointer) auf den nächsten Knoten. Die Liste wird durch Verfolgen dieser Verweise traversiert.

> [!NOTE]
> Eine **verkettete Liste** ist eine Datenstruktur, bei der jedes Element (Knoten) einen Datenwert und einen Verweis auf das nächste Element enthält. Die Liste beginnt mit einem Kopf-Verweis (Head) auf das erste Element.

#### Einfach verkettete Liste

Bei einer **einfach verketteten Liste** hat jeder Knoten genau einen Verweis: auf den Nachfolger. Das letzte Element verweist auf `None` (oder `NULL`).

> [!TIP]
> **Visualisierung einer einfach verketteten Liste:**
> ```
> Head
>   ↓
> ┌─────┬───┐   ┌─────┬───┐   ┌─────┬───┐   ┌─────┬────┐
> │ 42  │ ●─┼──→│ 17  │ ●─┼──→│ 93  │ ●─┼──→│ 55  │None│
> └─────┴───┘   └─────┴───┘   └─────┴───┘   └─────┴────┘
> ```

**Struktur eines Knotens:**
```python
class Node:
    def __init__(self, data):
        self.data = data  # Datenwert
        self.next = None  # Verweis auf nächsten Knoten
```

#### Doppelt verkettete Liste

Eine **doppelt verkettete Liste** erweitert die einfache Liste um Rückwärtsverweise. Jeder Knoten hat zwei Verweise: einen auf den Nachfolger und einen auf den Vorgänger. Dies ermöglicht bidirektionales Traversieren.

> [!TIP]
> **Visualisierung einer doppelt verketteten Liste:**
> ```
>       Head
>         ↓
>   ┌───┬─────┬───┐     ┌───┬─────┬───┐     ┌───┬─────┬───┐
>   │None│ 42  │ ●─┼────→│ ●─┼─ 17 │ ●─┼────→│ ●─┼─ 93 │None│
>   └───┴─────┴───┘  ↙  └───┴─────┴───┘  ↙  └───┴─────┴───┘
>                  ←┘                   ←┘
> ```

**Struktur eines Knotens:**
```python
class DNode:
    def __init__(self, data):
        self.data = data       # Datenwert
        self.next = None       # Verweis vorwärts
        self.prev = None       # Verweis rückwärts
```

#### Zeitkomplexität verketteter Listen

- **Zugriff auf Element an Index `i`**: O(n) – Liste muss von Anfang bis Index durchlaufen werden
- **Suchen eines Elements**: O(n) – gesamte Liste muss durchlaufen werden
- **Einfügen am Anfang**: O(1) – neuer Knoten wird vor Head eingefügt
- **Einfügen am Ende**: O(n) bei einfacher Liste ohne Tail-Pointer, O(1) mit Tail-Pointer
- **Einfügen in der Mitte** (bei bekanntem Vorgängerknoten): O(1)
- **Löschen am Anfang**: O(1)
- **Löschen am Ende**: O(n) bei einfacher Liste, O(1) bei doppelt verketteter Liste mit Tail-Pointer
- **Löschen in der Mitte** (bei bekanntem Knoten): O(1) bei doppelt verketteter Liste, O(n) bei einfacher Liste

> [!WARNING]
> **Wichtige Einschränkung**: Bei verketteten Listen ist der Zugriff auf beliebige Positionen ineffizient. Es gibt keinen direkten Zugriff wie bei Arrays. Die Liste muss immer vom Anfang (oder bei doppelt verketteten Listen auch vom Ende) durchlaufen werden.

#### Vor- und Nachteile verketteter Listen

**Vorteile:**
- Effizientes Einfügen und Löschen am Anfang und (bei doppelt verketteten Listen) am Ende
- Dynamische Größe ohne Kopieren des gesamten Inhalts
- Kein verschwendeter Speicher durch Überdimensionierung
- Einfügen/Löschen in der Mitte ohne Verschieben vieler Elemente (wenn Knoten bekannt)

**Nachteile:**
- Kein direkter Zugriff auf Elemente (kein Random Access)
- Zusätzlicher Speicher für Verweise (Pointer Overhead)
- Schlechtere Cache-Lokalität durch verstreute Speicherung
- Komplexere Implementierung als Arrays
- Anfälliger für Programmierfehler (z.B. verlorene Verweise, Memory Leaks)

### Stacks: Das LIFO-Prinzip

Ein **Stack** (Stapel, Kellerspeicher) ist eine lineare Datenstruktur, die das **LIFO-Prinzip** (Last In, First Out) umsetzt. Das zuletzt hinzugefügte Element wird als erstes wieder entfernt – wie ein Stapel Teller, bei dem nur der oberste genommen werden kann.

> [!NOTE]
> Ein **Stack** ist eine abstrakte Datenstruktur mit zwei Hauptoperationen:
> - **Push**: Fügt ein Element oben auf den Stack hinzu
> - **Pop**: Entfernt das oberste Element vom Stack und gibt es zurück
> 
> Zugriff ist nur auf das oberste Element (Top) möglich.

#### Grundoperationen eines Stacks

Ein Stack bietet typischerweise folgende Operationen:

1. **Push(element)**: Legt ein neues Element auf den Stack (O(1))
2. **Pop()**: Entfernt das oberste Element und gibt es zurück (O(1))
3. **Peek() / Top()**: Gibt das oberste Element zurück, ohne es zu entfernen (O(1))
4. **IsEmpty()**: Prüft, ob der Stack leer ist (O(1))
5. **Size()**: Gibt die Anzahl der Elemente zurück (O(1) bei Zähler-Variable)

> [!TIP]
> **Visualisierung eines Stacks:**
> ```
>    Push(55)  →     Pop()    →
>                    ↓
>     ┌─────┐      ┌─────┐
>     │ 55  │  ←── │ 55  │
>     ├─────┤      ├─────┤
>     │ 93  │      │ 93  │
>     ├─────┤      ├─────┤
>     │ 17  │      │ 17  │
>     ├─────┤      ├─────┤
>     │ 42  │      │ 42  │
>     └─────┘      └─────┘
>      Stack         nach Pop(): Stack hat 93 oben
> ```

#### Anwendungsfälle von Stacks

Stacks sind in der Informatik allgegenwärtig:

**Funktionsaufrufe (Call Stack)**: Jedes laufende Programm verwendet einen Stack, um Funktionsaufrufe zu verwalten. Beim Aufruf einer Funktion wird ein neuer **Stack Frame** mit lokalen Variablen und Rücksprungadresse auf den Call Stack gelegt. Bei Rückkehr wird dieser Frame vom Stack entfernt.

**Rückgängig-Funktion (Undo)**: Textverarbeitungen und Bildbearbeitungsprogramme speichern Änderungen auf einem Stack. Bei "Rückgängig" wird die letzte Änderung vom Stack genommen und umgekehrt.

**Auswertung arithmetischer Ausdrücke**: Die **Reverse Polish Notation** (RPN) nutzt einen Stack zur Auswertung von Ausdrücken ohne Klammern. Der **Shunting-Yard-Algorithmus** konvertiert Infix-Notation (z.B. `3 + 4`) in RPN mithilfe eines Stacks.

**Tiefensuche (DFS) in Graphen**: Der Algorithmus verwendet einen Stack, um den aktuellen Pfad zu verfolgen und bei Sackgassen zurückzukehren.

**Parser und Compiler**: Die **Syntaxanalyse** von Programmiersprachen nutzt Stacks, um verschachtelte Strukturen (Klammern, Blöcke) zu verarbeiten.

**Browser-Historie**: Die Zurück-Funktion eines Browsers kann als Stack implementiert werden (obwohl moderne Browser komplexere Strukturen verwenden).

> [!WARNING]
> **Stack Overflow**: Wird ein Stack zu groß (z.B. bei zu tiefer Rekursion), kann der verfügbare Speicher überschritten werden. Dies führt zum berüchtigten **Stack Overflow Error**, der das Programm zum Absturz bringt.

### Queues: Das FIFO-Prinzip

Eine **Queue** (Warteschlange) ist eine lineare Datenstruktur, die das **FIFO-Prinzip** (First In, First Out) umsetzt. Das zuerst hinzugefügte Element wird als erstes wieder entfernt – wie eine Warteschlange an der Kasse.

> [!NOTE]
> Eine **Queue** ist eine abstrakte Datenstruktur mit zwei Hauptoperationen:
> - **Enqueue**: Fügt ein Element am Ende der Queue hinzu
> - **Dequeue**: Entfernt das vorderste Element der Queue und gibt es zurück
> 
> Zugriff ist nur auf das vorderste Element (Front) und das hinterste Element (Rear) möglich.

#### Grundoperationen einer Queue

Eine Queue bietet typischerweise folgende Operationen:

1. **Enqueue(element)**: Fügt ein Element am Ende der Queue hinzu (O(1))
2. **Dequeue()**: Entfernt das vorderste Element und gibt es zurück (O(1))
3. **Front() / Peek()**: Gibt das vorderste Element zurück, ohne es zu entfernen (O(1))
4. **IsEmpty()**: Prüft, ob die Queue leer ist (O(1))
5. **Size()**: Gibt die Anzahl der Elemente zurück (O(1) bei Zähler-Variable)

> [!TIP]
> **Visualisierung einer Queue:**
> ```
>    Enqueue(55) →
> 
>      Front                             Rear
>        ↓                                ↓
>     ┌─────┬─────┬─────┬─────┐       ┌─────┐
>     │ 42  │ 17  │ 93  │ 55  │  ←──  │ 55  │
>     └─────┴─────┴─────┴─────┘       └─────┘
>       ↑
>    Dequeue() entfernt 42
> 
>    Nach Dequeue():
>      Front              Rear
>        ↓                 ↓
>     ┌─────┬─────┬─────┐
>     │ 17  │ 93  │ 55  │
>     └─────┴─────┴─────┘
> ```

#### Implementierungsvarianten von Queues

**Array-basierte Queue**: Verwendet ein Array mit zwei Zeigern (Front und Rear). Problem: Beim Dequeue entsteht am Anfang ungenutzter Platz. Lösung: **Zirkuläres Array** (Ringpuffer), bei dem die Zeiger modulo Array-Länge inkrementiert werden.

**Verkettete Liste als Queue**: Nutzt eine einfach verkettete Liste mit Head (Front) und Tail (Rear). Enqueue fügt am Tail hinzu, Dequeue entfernt am Head. Beide Operationen sind O(1).

**Double-Ended Queue (Deque)**: Verallgemeinerung, die Einfügen und Entfernen an beiden Enden erlaubt. Kombiniert Stack- und Queue-Funktionalität.

#### Anwendungsfälle von Queues

Queues sind essentiell für viele Algorithmen und Systeme:

**Betriebssysteme**: Die **Prozess-Scheduler** verwenden Queues, um Ready-Prozesse zu verwalten. Der Scheduler entnimmt den ersten Prozess der Queue, führt ihn aus und reiht ihn ggf. wieder ein (Round-Robin-Scheduling).

**Netzwerk-Kommunikation**: Datenpakete werden in Queues gepuffert, wenn die Netzwerkbandbreite nicht ausreicht, um alle sofort zu senden.

**Druckerwarteschlangen**: Druckaufträge werden in einer Queue verwaltet und in der Reihenfolge des Eingangs abgearbeitet.

**Breitensuche (BFS) in Graphen**: Der Algorithmus verwendet eine Queue, um Knoten Ebene für Ebene zu durchlaufen.

**Asynchrone Datenverarbeitung**: Message Queues (z.B. RabbitMQ, Apache Kafka) entkoppeln Sender und Empfänger in verteilten Systemen.

**Simulation**: Warteschlangen-Modelle simulieren Systeme mit begrenzter Kapazität (z.B. Supermarkt-Kassen, Call-Center).

> [!TIP]
> **Mermaid-Diagramm: Vergleich Stack vs. Queue**
> ```mermaid
> graph LR
>     subgraph "Stack (LIFO)"
>         direction TB
>         S1[Push 1] --> S2[Push 2]
>         S2 --> S3[Push 3]
>         S3 -.Pop: 3.-> S4[Pop 2]
>         S4 -.Pop: 2.-> S5[Pop 1]
>     end
>     
>     subgraph "Queue (FIFO)"
>         direction LR
>         Q1[Enqueue 1] --> Q2[Enqueue 2]
>         Q2 --> Q3[Enqueue 3]
>         Q3 -.Dequeue: 1.-> Q4[Dequeue 2]
>         Q4 -.Dequeue: 2.-> Q5[Dequeue 3]
>     end
> ```

### Vergleich der Datenstrukturen

Die folgende Tabelle fasst die wichtigsten Eigenschaften zusammen:

| Datenstruktur | Zugriff | Suche | Einfügen Anfang | Einfügen Ende | Löschen Anfang | Löschen Ende | Hauptvorteil |
|---|---|---|---|---|---|---|---|
| **Array** | O(1) | O(n) | O(n) | O(1)* | O(n) | O(1) | Schneller direkter Zugriff |
| **Verkettete Liste** | O(n) | O(n) | O(1) | O(1)** | O(1) | O(1)*** | Effizientes Einfügen/Löschen |
| **Stack** | O(1)**** | O(n) | O(1) | – | O(1) | – | LIFO-Semantik |
| **Queue** | O(1)***** | O(n) | – | O(1) | O(1) | – | FIFO-Semantik |

*Bei dynamischen Arrays amortisiert  
**Bei einfacher Liste mit Tail-Pointer  
***Bei doppelt verketteter Liste mit Tail-Pointer  
****Nur auf Top-Element  
*****Nur auf Front-Element

### Wann welche Datenstruktur verwenden?

Die Wahl der richtigen Datenstruktur ist eine zentrale Design-Entscheidung:

**Verwende Arrays/Listen**, wenn:
- Häufiger Zugriff auf beliebige Positionen nötig ist
- Die Reihenfolge der Elemente wichtig ist
- Iterieren über alle Elemente die Hauptoperation ist
- Die Größe weitgehend konstant ist oder Größenänderungen selten sind

**Verwende verkettete Listen**, wenn:
- Häufiges Einfügen und Löschen am Anfang oder in der Mitte erfolgt
- Die Größe stark variiert
- Kein direkter Zugriff auf Positionen benötigt wird
- Speicher-Fragmentierung vermieden werden soll

**Verwende Stacks**, wenn:
- LIFO-Semantik benötigt wird (letztes Element zuerst)
- Rückgängig-Funktionalität implementiert werden soll
- Rekursion iterativ simuliert werden soll
- Auswertung von Ausdrücken oder Parsing erfolgt

**Verwende Queues**, wenn:
- FIFO-Semantik benötigt wird (erstes Element zuerst)
- Aufgaben in der Reihenfolge ihrer Ankunft bearbeitet werden sollen
- Pufferung von Datenströmen erforderlich ist
- Breitensuche oder Level-Order-Traversierung durchgeführt wird

### Zusammenfassung Theorie

Die fundamentalen Datenstrukturen Arrays, verkettete Listen, Stacks und Queues bilden die Basis für komplexere Strukturen. Arrays bieten schnellen Zugriff über Indizes, während verkettete Listen flexibles Einfügen und Löschen ermöglichen. Stacks implementieren das LIFO-Prinzip für Situationen, in denen das zuletzt hinzugefügte Element zuerst verarbeitet wird. Queues folgen dem FIFO-Prinzip und eignen sich für Warteschlangen und Pufferung.

Die Zeitkomplexität verschiedener Operationen unterscheidet sich erheblich zwischen den Strukturen. Arrays ermöglichen O(1)-Zugriff, aber O(n)-Einfügen in der Mitte. Verkettete Listen ermöglichen O(1)-Einfügen am Anfang, aber O(n)-Zugriff auf beliebige Positionen. Die Wahl der richtigen Datenstruktur basiert auf den häufigsten Operationen im konkreten Anwendungsfall.

Das Verständnis dieser grundlegenden Strukturen ist essentiell für die Entwicklung effizienter Software. In der nächsten Vorlesung werden wir komplexere Strukturen wie Bäume und Hash-Tabellen behandeln, die auf diesen Grundlagen aufbauen.

---

## Teil 2: Python-Praxis - Listen & Datenstrukturen

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

Python bietet mit **Listen** eine vielseitige und mächtige eingebaute Datenstruktur, die Arrays, Stacks und Queues kombiniert. Listen sind dynamisch, können Elemente unterschiedlichen Typs enthalten und bieten eine Fülle von Methoden zur Manipulation. In diesem Praxis-Teil lernen wir Listen von Grund auf kennen und nutzen sie für verschiedene Anwendungsfälle.

Zusätzlich behandeln wir **Tupel** als unveränderliche Alternative zu Listen und erkunden fortgeschrittene Techniken wie Slicing, Unpacking und Aliasing. Das Verständnis dieser Konzepte ist fundamental für professionelle Python-Entwicklung.

### Listen in Python: Grundlagen

Eine **Liste** in Python ist eine geordnete, veränderbare Sammlung von Elementen beliebigen Typs. Listen werden mit eckigen Klammern `[]` erstellt und können wachsen und schrumpfen.

#### Listen erstellen

> [!NOTE]
> **`list`-Datentyp (Built-in)**:
> - Veränderbare (mutable) Sequenz beliebiger Python-Objekte
> - Erstellen mit `[]` oder `list(iterable)`
> - Syntax: `[element1, element2, ...]`
> - Unterstützt gemischte Datentypen
> - Signatur: `list(iterable=None)` → `list`

> [!TIP]
> ```python
> # Leere Liste erstellen
> leere_liste = []
> auch_leer = list()
> 
> # Liste mit Elementen
> zahlen = [1, 2, 3, 4, 5]
> fruechte = ["Apfel", "Banane", "Kirsche"]
> 
> # Gemischte Typen (möglich, aber nicht empfohlen)
> gemischt = [42, "Hallo", 3.14, True, [1, 2]]
> 
> # Liste aus String erstellen
> buchstaben = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
> 
> # Liste aus range erstellen
> zahlenfolge = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
> ```

#### Zugriff auf Listen-Elemente

Listen unterstützen Indizierung wie Strings. Indizes beginnen bei 0 und negative Indizes zählen vom Ende.

> [!TIP]
> ```python
> fruechte = ["Apfel", "Banane", "Kirsche", "Dattel"]
> 
> # Positiver Index (von vorne)
> print(fruechte[0])   # "Apfel" (erstes Element)
> print(fruechte[2])   # "Kirsche"
> 
> # Negativer Index (von hinten)
> print(fruechte[-1])  # "Dattel" (letztes Element)
> print(fruechte[-2])  # "Kirsche"
> 
> # Index außerhalb des Bereichs → IndexError
> # print(fruechte[10])  # IndexError: list index out of range
> ```

> [!WARNING]
> **IndexError vermeiden**: Prüfe vor Zugriff, ob der Index gültig ist:
> ```python
> if 0 <= index < len(liste):
>     element = liste[index]
> ```
> Oder nutze `try-except` für Fehlerbehandlung (wird in V09 behandelt).

### Listen-Methoden: Elemente hinzufügen

Python-Listen bieten mehrere Methoden zum Hinzufügen von Elementen.

#### `.append()` – Element am Ende hinzufügen

> [!NOTE]
> **`list.append(element)`** (List-Methode):
> - Fügt ein einzelnes Element am Ende der Liste hinzu
> - Modifiziert die Liste **in-place** (kein Rückgabewert, gibt `None` zurück)
> - Zeitkomplexität: O(1) amortisiert
> - Signatur: `list.append(x)` → `None`

> [!TIP]
> ```python
> fruechte = ["Apfel", "Banane"]
> 
> fruechte.append("Kirsche")
> print(fruechte)  # ['Apfel', 'Banane', 'Kirsche']
> 
> # Auch Listen können hinzugefügt werden (als einzelnes Element!)
> fruechte.append(["Erdbeere", "Himbeere"])
> print(fruechte)  # ['Apfel', 'Banane', 'Kirsche', ['Erdbeere', 'Himbeere']]
> ```

> [!WARNING]
> **Häufiger Fehler**: `append()` gibt `None` zurück, nicht die modifizierte Liste!
> ```python
> # Falsch:
> fruechte = fruechte.append("Orange")  # fruechte wird None!
> 
> # Richtig:
> fruechte.append("Orange")  # Liste wird direkt modifiziert
> ```

#### `.insert()` – Element an bestimmter Position einfügen

> [!NOTE]
> **`list.insert(index, element)`** (List-Methode):
> - Fügt ein Element an Position `index` ein
> - Alle nachfolgenden Elemente rutschen nach rechts
> - Zeitkomplexität: O(n) – alle nachfolgenden Elemente müssen verschoben werden
> - Signatur: `list.insert(i, x)` → `None`

> [!TIP]
> ```python
> zahlen = [1, 2, 4, 5]
> 
> # Füge 3 an Index 2 ein
> zahlen.insert(2, 3)
> print(zahlen)  # [1, 2, 3, 4, 5]
> 
> # Am Anfang einfügen
> zahlen.insert(0, 0)
> print(zahlen)  # [0, 1, 2, 3, 4, 5]
> 
> # Index größer als Länge → fügt am Ende ein
> zahlen.insert(100, 99)
> print(zahlen)  # [0, 1, 2, 3, 4, 5, 99]
> ```

#### `.extend()` – Mehrere Elemente hinzufügen

> [!NOTE]
> **`list.extend(iterable)`** (List-Methode):
> - Fügt alle Elemente aus einem Iterable am Ende hinzu
> - Entspricht mehrfachem `append()`, aber effizienter
> - Zeitkomplexität: O(k), wobei k die Anzahl hinzugefügter Elemente ist
> - Signatur: `list.extend(iterable)` → `None`

> [!TIP]
> ```python
> liste1 = [1, 2, 3]
> liste2 = [4, 5, 6]
> 
> # extend() fügt Elemente einzeln hinzu
> liste1.extend(liste2)
> print(liste1)  # [1, 2, 3, 4, 5, 6]
> 
> # Vergleich mit append():
> liste3 = [1, 2, 3]
> liste3.append(liste2)
> print(liste3)  # [1, 2, 3, [4, 5, 6]] (Liste als Element!)
> 
> # extend() mit anderen Iterables
> liste1.extend("AB")
> print(liste1)  # [1, 2, 3, 4, 5, 6, 'A', 'B']
> ```

#### Listen verketten mit `+`-Operator

> [!NOTE]
> **`+`-Operator für Listen**:
> - Erzeugt eine **neue** Liste durch Konkatenation
> - Ursprüngliche Listen bleiben unverändert
> - Zeitkomplexität: O(n + m), wobei n und m die Längen sind
> - Syntax: `liste1 + liste2` → neue Liste

> [!TIP]
> ```python
> liste1 = [1, 2, 3]
> liste2 = [4, 5, 6]
> 
> # Verkettung erzeugt neue Liste
> neue_liste = liste1 + liste2
> print(neue_liste)  # [1, 2, 3, 4, 5, 6]
> print(liste1)      # [1, 2, 3] (unverändert)
> 
> # Mehrfache Verkettung
> result = [1] + [2, 3] + [4, 5]
> print(result)  # [1, 2, 3, 4, 5]
> ```

> [!WARNING]
> **Performance-Unterschied**: `extend()` modifiziert die Liste in-place (effizienter), während `+` eine neue Liste erstellt (benötigt mehr Speicher und Zeit):
> ```python
> # Effizient:
> liste.extend(andere_liste)
> 
> # Weniger effizient (neue Liste wird erstellt):
> liste = liste + andere_liste
> ```

### Listen-Methoden: Elemente entfernen

#### `.remove()` – Erstes Vorkommen entfernen

> [!NOTE]
> **`list.remove(value)`** (List-Methode):
> - Entfernt das **erste** Vorkommen des Werts aus der Liste
> - Wirft `ValueError`, wenn der Wert nicht gefunden wird
> - Zeitkomplexität: O(n) – Liste muss durchsucht werden
> - Signatur: `list.remove(x)` → `None`

> [!TIP]
> ```python
> fruechte = ["Apfel", "Banane", "Kirsche", "Banane"]
> 
> fruechte.remove("Banane")
> print(fruechte)  # ['Apfel', 'Kirsche', 'Banane'] (nur erste Banane entfernt)
> 
> # Entfernen eines nicht vorhandenen Elements → ValueError
> # fruechte.remove("Orange")  # ValueError: list.remove(x): x not in list
> ```

> [!WARNING]
> **ValueError abfangen**: Prüfe vorher, ob das Element existiert:
> ```python
> if "Orange" in fruechte:
>     fruechte.remove("Orange")
> ```

#### `.pop()` – Element an Index entfernen

> [!NOTE]
> **`list.pop(index=-1)`** (List-Methode):
> - Entfernt das Element an `index` und gibt es zurück
> - Standard: `index=-1` (letztes Element)
> - Wirft `IndexError`, wenn Index ungültig ist
> - Zeitkomplexität: O(n) für beliebigen Index, O(1) für letztes Element
> - Signatur: `list.pop(i=-1)` → Element

> [!TIP]
> ```python
> zahlen = [10, 20, 30, 40, 50]
> 
> # Letztes Element entfernen
> letztes = zahlen.pop()
> print(letztes)  # 50
> print(zahlen)   # [10, 20, 30, 40]
> 
> # Element an Index 1 entfernen
> element = zahlen.pop(1)
> print(element)  # 20
> print(zahlen)   # [10, 30, 40]
> 
> # Stack-Verhalten simulieren
> stack = [1, 2, 3]
> stack.append(4)  # Push
> top = stack.pop()  # Pop → 4
> ```

#### `.clear()` – Alle Elemente entfernen

> [!NOTE]
> **`list.clear()`** (List-Methode):
> - Entfernt alle Elemente aus der Liste
> - Liste wird leer, aber das Listenobjekt bleibt bestehen
> - Zeitkomplexität: O(n)
> - Signatur: `list.clear()` → `None`

> [!TIP]
> ```python
> zahlen = [1, 2, 3, 4, 5]
> zahlen.clear()
> print(zahlen)  # []
> print(len(zahlen))  # 0
> 
> # Alternative: Neuzuweisung
> zahlen = []  # Erzeugt neue leere Liste
> ```

#### `del`-Statement – Elemente oder Slices löschen

> [!NOTE]
> **`del`-Statement**:
> - Löscht Elemente an bestimmten Indizes oder Slices
> - Kann auch die gesamte Variable löschen
> - Zeitkomplexität: O(n) für Element in der Mitte, O(1) für letztes Element
> - Syntax: `del liste[index]` oder `del liste[start:stop]`

> [!TIP]
> ```python
> zahlen = [0, 1, 2, 3, 4, 5]
> 
> # Einzelnes Element löschen
> del zahlen[0]
> print(zahlen)  # [1, 2, 3, 4, 5]
> 
> # Slice löschen
> del zahlen[1:3]
> print(zahlen)  # [1, 4, 5]
> 
> # Gesamte Variable löschen (Variable existiert danach nicht mehr)
> del zahlen
> # print(zahlen)  # NameError: name 'zahlen' is not defined
> ```

### Listen durchsuchen und abfragen

#### `.index()` – Position eines Elements finden

> [!NOTE]
> **`list.index(value, start=0, stop=len)`** (List-Methode):
> - Gibt den Index des **ersten** Vorkommens von `value` zurück
> - Wirft `ValueError`, wenn der Wert nicht gefunden wird
> - Optional: Suche in Teilbereich `[start:stop]`
> - Zeitkomplexität: O(n)
> - Signatur: `list.index(x, start=0, stop=len)` → `int`

> [!TIP]
> ```python
> fruechte = ["Apfel", "Banane", "Kirsche", "Banane"]
> 
> index = fruechte.index("Banane")
> print(index)  # 1 (erstes Vorkommen)
> 
> # Suche ab Index 2
> index2 = fruechte.index("Banane", 2)
> print(index2)  # 3 (zweites Vorkommen)
> 
> # Element nicht vorhanden → ValueError
> # fruechte.index("Orange")  # ValueError
> ```

#### `.count()` – Häufigkeit eines Elements zählen

> [!NOTE]
> **`list.count(value)`** (List-Methode):
> - Zählt, wie oft `value` in der Liste vorkommt
> - Gibt 0 zurück, wenn Element nicht vorhanden
> - Zeitkomplexität: O(n)
> - Signatur: `list.count(x)` → `int`

> [!TIP]
> ```python
> zahlen = [1, 2, 3, 2, 4, 2, 5]
> 
> anzahl = zahlen.count(2)
> print(anzahl)  # 3
> 
> # Element nicht vorhanden
> print(zahlen.count(99))  # 0
> ```

#### `in`-Operator – Prüfen, ob Element vorhanden ist

> [!NOTE]
> **`in`-Operator für Listen**:
> - Prüft, ob ein Wert in der Liste enthalten ist
> - Gibt `True` oder `False` zurück
> - Zeitkomplexität: O(n)
> - Syntax: `value in liste` → `bool`

> [!TIP]
> ```python
> fruechte = ["Apfel", "Banane", "Kirsche"]
> 
> if "Banane" in fruechte:
>     print("Banane ist vorhanden")
> 
> if "Orange" not in fruechte:
>     print("Orange ist nicht vorhanden")
> 
> # Auch für Bedingungen in Comprehensions
> ergebnis = [f for f in fruechte if "a" in f]
> print(ergebnis)  # ['Banane']
> ```

### Listen sortieren und umkehren

#### `.sort()` – Liste in-place sortieren

> [!NOTE]
> **`list.sort(key=None, reverse=False)`** (List-Methode):
> - Sortiert die Liste **in-place** (modifiziert Original)
> - `key`: Optionale Funktion zur Berechnung des Sortierschlüssels
> - `reverse=True`: Absteigende Sortierung
> - Zeitkomplexität: O(n log n) (Timsort-Algorithmus)
> - Signatur: `list.sort(key=None, reverse=False)` → `None`

> [!TIP]
> ```python
> zahlen = [3, 1, 4, 1, 5, 9, 2]
> 
> # Aufsteigend sortieren
> zahlen.sort()
> print(zahlen)  # [1, 1, 2, 3, 4, 5, 9]
> 
> # Absteigend sortieren
> zahlen.sort(reverse=True)
> print(zahlen)  # [9, 5, 4, 3, 2, 1, 1]
> 
> # Strings sortieren (lexikographisch)
> woerter = ["Zebra", "Apfel", "Banane"]
> woerter.sort()
> print(woerter)  # ['Apfel', 'Banane', 'Zebra']
> 
> # Nach Länge sortieren (key-Funktion)
> woerter.sort(key=len)
> print(woerter)  # ['Apfel', 'Zebra', 'Banane']
> ```

#### `sorted()` – Neue sortierte Liste erstellen

> [!NOTE]
> **`sorted(iterable, key=None, reverse=False)`** (Built-in Funktion):
> - Erstellt eine **neue** sortierte Liste
> - Original bleibt unverändert
> - Funktioniert mit jedem Iterable (Liste, String, Tuple, etc.)
> - Zeitkomplexität: O(n log n)
> - Signatur: `sorted(iterable, key=None, reverse=False)` → `list`

> [!TIP]
> ```python
> zahlen = [3, 1, 4, 1, 5]
> 
> sortiert = sorted(zahlen)
> print(sortiert)  # [1, 1, 3, 4, 5]
> print(zahlen)    # [3, 1, 4, 1, 5] (Original unverändert)
> 
> # String sortieren (gibt Liste zurück!)
> buchstaben = sorted("python")
> print(buchstaben)  # ['h', 'n', 'o', 'p', 't', 'y']
> 
> # Zurück zu String
> sortiert_string = ''.join(sorted("python"))
> print(sortiert_string)  # "hnopty"
> ```

> [!WARNING]
> **Unterschied `sort()` vs. `sorted()`**:
> - `.sort()` modifiziert die Liste direkt und gibt `None` zurück
> - `sorted()` gibt eine neue Liste zurück und lässt das Original unverändert
> ```python
> # Falsch:
> zahlen = zahlen.sort()  # zahlen wird None!
> 
> # Richtig (in-place):
> zahlen.sort()
> 
> # Richtig (neue Liste):
> sortierte_zahlen = sorted(zahlen)
> ```

#### `.reverse()` – Liste umkehren

> [!NOTE]
> **`list.reverse()`** (List-Methode):
> - Kehrt die Reihenfolge der Elemente **in-place** um
> - Gibt `None` zurück
> - Zeitkomplexität: O(n)
> - Signatur: `list.reverse()` → `None`

> [!TIP]
> ```python
> zahlen = [1, 2, 3, 4, 5]
> 
> zahlen.reverse()
> print(zahlen)  # [5, 4, 3, 2, 1]
> 
> # Alternative mit Slicing (erzeugt neue Liste)
> zahlen2 = [1, 2, 3, 4, 5]
> umgekehrt = zahlen2[::-1]
> print(umgekehrt)  # [5, 4, 3, 2, 1]
> print(zahlen2)    # [1, 2, 3, 4, 5] (Original unverändert)
> ```

### List Slicing: Teilbereiche extrahieren

**Slicing** erlaubt den Zugriff auf Teilbereiche einer Liste. Die Syntax ist `liste[start:stop:step]`.

> [!NOTE]
> **List Slicing**:
> - Extrahiert einen Teilbereich: `liste[start:stop:step]`
> - `start`: Startindex (inklusive, Standard: 0)
> - `stop`: Endindex (exklusive, Standard: len(liste))
> - `step`: Schrittweite (Standard: 1)
> - Erzeugt eine **neue** Liste (Shallow Copy)
> - Signatur: `liste[start:stop:step]` → neue `list`

> [!TIP]
> ```python
> zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
> 
> # Grundlegendes Slicing
> print(zahlen[2:5])    # [2, 3, 4] (Index 2 bis 4)
> print(zahlen[:5])     # [0, 1, 2, 3, 4] (Anfang bis 4)
> print(zahlen[5:])     # [5, 6, 7, 8, 9] (Ab 5 bis Ende)
> print(zahlen[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (Komplette Liste kopieren)
> 
> # Mit Schrittweite
> print(zahlen[::2])    # [0, 2, 4, 6, 8] (Jedes zweite Element)
> print(zahlen[1::2])   # [1, 3, 5, 7, 9] (Jedes zweite, ab Index 1)
> print(zahlen[::3])    # [0, 3, 6, 9] (Jedes dritte)
> 
> # Negative Schrittweite (rückwärts)
> print(zahlen[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (Liste umkehren)
> print(zahlen[7:2:-1]) # [7, 6, 5, 4, 3] (Von 7 bis 3, rückwärts)
> 
> # Negative Indizes
> print(zahlen[-3:])    # [7, 8, 9] (Letzte 3 Elemente)
> print(zahlen[:-3])    # [0, 1, 2, 3, 4, 5, 6] (Alle außer letzte 3)
> ```

> [!WARNING]
> **Slicing erstellt Shallow Copy**: Bei Listen mit veränderbaren Objekten werden nur die Referenzen kopiert:
> ```python
> original = [[1, 2], [3, 4]]
> kopie = original[:]
> 
> kopie[0][0] = 99  # Ändert auch das Original!
> print(original)   # [[99, 2], [3, 4]]
> ```
> Für Deep Copy: `import copy; kopie = copy.deepcopy(original)`

#### Slicing zum Modifizieren von Listen

Slicing kann auch auf der linken Seite einer Zuweisung verwendet werden, um Teilbereiche zu ersetzen.

> [!TIP]
> ```python
> zahlen = [0, 1, 2, 3, 4, 5]
> 
> # Bereich ersetzen
> zahlen[1:4] = [10, 20, 30]
> print(zahlen)  # [0, 10, 20, 30, 4, 5]
> 
> # Bereich mit weniger Elementen ersetzen (Liste schrumpft)
> zahlen[1:4] = [99]
> print(zahlen)  # [0, 99, 4, 5]
> 
> # Bereich löschen
> zahlen[1:3] = []
> print(zahlen)  # [0, 5]
> 
> # Einfügen ohne Löschen (leerer Slice)
> zahlen[1:1] = [1, 2, 3, 4]
> print(zahlen)  # [0, 1, 2, 3, 4, 5]
> ```

### Tupel: Unveränderliche Listen

**Tupel** sind wie Listen, aber **immutable** (unveränderlich). Nach der Erzeugung können keine Elemente hinzugefügt, entfernt oder geändert werden.

> [!NOTE]
> **`tuple`-Datentyp (Built-in)**:
> - Unveränderbare (immutable) Sequenz beliebiger Python-Objekte
> - Erstellen mit `()` oder einfach durch Komma-Trennung
> - Syntax: `(element1, element2, ...)` oder `element1, element2, ...`
> - Unterstützt Indizierung und Slicing (schreibgeschützt)
> - Signatur: `tuple(iterable=None)` → `tuple`

> [!TIP]
> ```python
> # Tupel erstellen
> punkt = (10, 20)
> farben = ("Rot", "Grün", "Blau")
> 
> # Ohne Klammern (Tuple Packing)
> koordinaten = 5, 10, 15
> print(type(koordinaten))  # <class 'tuple'>
> 
> # Ein-Element-Tupel (Komma erforderlich!)
> single = (42,)  # Tupel
> kein_tupel = (42)  # Integer!
> print(type(single))     # <class 'tuple'>
> print(type(kein_tupel)) # <class 'int'>
> 
> # Leeres Tupel
> leer = ()
> auch_leer = tuple()
> 
> # Zugriff wie bei Listen
> print(punkt[0])  # 10
> print(farben[-1])  # "Blau"
> 
> # Slicing funktioniert
> print(farben[1:])  # ('Grün', 'Blau')
> ```

> [!WARNING]
> **Tupel sind unveränderlich**:
> ```python
> punkt = (10, 20)
> # punkt[0] = 15  # TypeError: 'tuple' object does not support item assignment
> # punkt.append(30)  # AttributeError: 'tuple' object has no attribute 'append'
> ```
> Um ein Tupel zu "ändern", muss ein neues erstellt werden:
> ```python
> punkt = (15, 20)  # Neues Tupel, alte Referenz überschrieben
> ```

#### Wann Tupel statt Listen verwenden?

**Verwende Tupel**, wenn:
- Daten unveränderlich sein sollen (z.B. Koordinaten, Konfigurationswerte)
- Als Dictionary-Keys (Listen sind nicht hashable, Tupel schon)
- Für Funktionsrückgaben mehrerer Werte
- Speicher-Effizienz wichtig ist (Tupel sind leichter als Listen)
- Schutz vor versehentlicher Modifikation gewünscht ist

> [!TIP]
> ```python
> # Tupel als Dictionary-Keys
> positionen = {
>     (0, 0): "Start",
>     (10, 5): "Checkpoint",
>     (20, 20): "Ziel"
> }
> 
> # Multiple Return Values
> def min_max(zahlen):
>     return min(zahlen), max(zahlen)
> 
> minimum, maximum = min_max([3, 1, 4, 1, 5])
> print(minimum, maximum)  # 1 5
> ```

### List Unpacking und Tuple Unpacking

**Unpacking** erlaubt das Entpacken von Sequenzen in mehrere Variablen.

> [!NOTE]
> **Sequence Unpacking**:
> - Weist Elemente einer Sequenz mehreren Variablen zu
> - Anzahl der Variablen muss mit Anzahl der Elemente übereinstimmen (oder `*` verwenden)
> - Funktioniert mit Listen, Tupeln, Strings, etc.
> - Syntax: `var1, var2, var3 = sequenz`

> [!TIP]
> ```python
> # Einfaches Unpacking
> punkt = (10, 20)
> x, y = punkt
> print(x, y)  # 10 20
> 
> # Liste unpacken
> farben = ["Rot", "Grün", "Blau"]
> rot, gruen, blau = farben
> 
> # Variablen tauschen (sehr pythonisch!)
> a, b = 5, 10
> a, b = b, a  # Tausch ohne temporäre Variable
> print(a, b)  # 10 5
> 
> # Unpacking mit * (Rest-Elemente sammeln)
> zahlen = [1, 2, 3, 4, 5]
> erste, *rest, letzte = zahlen
> print(erste)  # 1
> print(rest)   # [2, 3, 4]
> print(letzte) # 5
> 
> # Nur interessante Elemente extrahieren
> _, zweite, *_, vorletzte, _ = [1, 2, 3, 4, 5, 6]
> print(zweite, vorletzte)  # 2 5
> ```

> [!WARNING]
> **ValueError bei falscher Anzahl**:
> ```python
> punkt = (10, 20, 30)
> # x, y = punkt  # ValueError: too many values to unpack (expected 2)
> 
> # Richtig mit * oder alle Variablen angeben
> x, y, z = punkt
> # oder
> x, y, *rest = punkt
> ```

### Listen-Aliasing und Kopieren

Wenn eine Liste einer anderen Variable zugewiesen wird, wird nur eine **Referenz** kopiert, nicht die Liste selbst.

> [!NOTE]
> **Aliasing** (Referenz-Zuweisung):
> - Zuweisung `liste2 = liste1` erstellt **keine** Kopie
> - Beide Variablen zeigen auf dasselbe Listenobjekt
> - Änderungen über eine Variable beeinflussen die andere

> [!TIP]
> ```python
> liste1 = [1, 2, 3]
> liste2 = liste1  # Aliasing, keine Kopie!
> 
> liste2.append(4)
> print(liste1)  # [1, 2, 3, 4] (auch liste1 ist geändert!)
> print(liste2)  # [1, 2, 3, 4]
> 
> # Prüfen, ob selbes Objekt
> print(liste1 is liste2)  # True
> print(id(liste1) == id(liste2))  # True
> ```

#### Listen kopieren

Um eine echte Kopie zu erstellen, gibt es mehrere Möglichkeiten:

> [!TIP]
> ```python
> original = [1, 2, 3]
> 
> # Methode 1: Slicing
> kopie1 = original[:]
> 
> # Methode 2: list()-Konstruktor
> kopie2 = list(original)
> 
> # Methode 3: .copy()-Methode
> kopie3 = original.copy()
> 
> # Alle drei sind unabhängige Kopien
> kopie1.append(4)
> print(original)  # [1, 2, 3] (unverändert)
> print(kopie1)    # [1, 2, 3, 4]
> 
> # Prüfen: Verschiedene Objekte
> print(original is kopie1)  # False
> ```

> [!WARNING]
> **Shallow Copy vs. Deep Copy**:
> Die oben genannten Methoden erstellen nur **Shallow Copies**. Bei Listen mit veränderbaren Objekten werden nur die Referenzen kopiert:
> ```python
> original = [[1, 2], [3, 4]]
> kopie = original[:]
> 
> kopie[0][0] = 99
> print(original)  # [[99, 2], [3, 4]] (auch original geändert!)
> ```
> Für vollständige Kopien (Deep Copy):
> ```python
> import copy
> kopie = copy.deepcopy(original)
> 
> kopie[0][0] = 99
> print(original)  # [[1, 2], [3, 4]] (unverändert)
> ```

### List Comprehensions (Wiederholung und Vertiefung)

List Comprehensions wurden in V07 eingeführt, hier vertiefen wir sie im Kontext von Listen-Operationen.

> [!TIP]
> ```python
> # Quadratzahlen
> quadrate = [x**2 for x in range(10)]
> print(quadrate)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> 
> # Mit Bedingung (Filter)
> gerade = [x for x in range(20) if x % 2 == 0]
> print(gerade)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
> 
> # String-Verarbeitung
> woerter = ["Hallo", "Welt", "Python"]
> grossbuchstaben = [w.upper() for w in woerter]
> print(grossbuchstaben)  # ['HALLO', 'WELT', 'PYTHON']
> 
> # Verschachtelt
> matrix = [[i*j for j in range(3)] for i in range(3)]
> print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
> 
> # Komplexere Ausdrücke
> werte = [1, 2, 3, 4, 5]
> ergebnis = [x*2 if x % 2 == 0 else x for x in werte]
> print(ergebnis)  # [1, 4, 3, 8, 5]
> ```

### Weitere nützliche Built-in Funktionen für Listen

#### `len()` – Länge der Liste

Bereits in V01 eingeführt, hier im Kontext von Listen:

> [!TIP]
> ```python
> zahlen = [1, 2, 3, 4, 5]
> print(len(zahlen))  # 5
> 
> # Leere Liste
> print(len([]))  # 0
> ```

#### `sum()` – Summe aller Elemente

> [!NOTE]
> **`sum(iterable, start=0)`** (Built-in):
> - Berechnet die Summe aller Elemente
> - `start`: Startwert (wird zur Summe addiert)
> - Nur für numerische Werte
> - Signatur: `sum(iterable, start=0)` → `number`

> [!TIP]
> ```python
> zahlen = [1, 2, 3, 4, 5]
> print(sum(zahlen))  # 15
> 
> # Mit Startwert
> print(sum(zahlen, 10))  # 25
> 
> # Durchschnitt berechnen
> durchschnitt = sum(zahlen) / len(zahlen)
> print(durchschnitt)  # 3.0
> ```

#### `min()` und `max()` – Minimum und Maximum

Bereits in V03 eingeführt, hier mit Listen:

> [!TIP]
> ```python
> zahlen = [3, 1, 4, 1, 5, 9, 2]
> 
> print(min(zahlen))  # 1
> print(max(zahlen))  # 9
> 
> # Mit Strings (lexikographisch)
> woerter = ["Zebra", "Apfel", "Banane"]
> print(min(woerter))  # "Apfel"
> print(max(woerter))  # "Zebra"
> 
> # Mit key-Funktion (nach Länge)
> print(min(woerter, key=len))  # "Zebra" (oder "Apfel", beide 5 Zeichen)
> print(max(woerter, key=len))  # "Banane" (6 Zeichen)
> ```

#### `all()` und `any()` – Logische Prüfungen

> [!NOTE]
> **`all(iterable)`** (Built-in):
> - Gibt `True` zurück, wenn **alle** Elemente truthy sind
> - Leere Iterables geben `True` zurück (Vakuum-Wahrheit)
> - Signatur: `all(iterable)` → `bool`

> [!NOTE]
> **`any(iterable)`** (Built-in):
> - Gibt `True` zurück, wenn **mindestens ein** Element truthy ist
> - Leere Iterables geben `False` zurück
> - Signatur: `any(iterable)` → `bool`
> - Bereits in V04 als Vorschau erwähnt, hier vollständige Einführung

> [!TIP]
> ```python
> # all() - Alle müssen True sein
> zahlen = [2, 4, 6, 8]
> print(all(x % 2 == 0 for x in zahlen))  # True (alle gerade)
> 
> zahlen2 = [2, 3, 4]
> print(all(x % 2 == 0 for x in zahlen2))  # False (3 ist ungerade)
> 
> # any() - Mindestens eines muss True sein
> zahlen3 = [1, 3, 5, 6]
> print(any(x % 2 == 0 for x in zahlen3))  # True (6 ist gerade)
> 
> zahlen4 = [1, 3, 5]
> print(any(x % 2 == 0 for x in zahlen4))  # False (alle ungerade)
> 
> # Praktisches Beispiel: Passwort-Validierung
> passwort = "Abc123!"
> hat_grossbuchstabe = any(c.isupper() for c in passwort)
> hat_ziffer = any(c.isdigit() for c in passwort)
> lang_genug = len(passwort) >= 8
> 
> gueltig = all([hat_grossbuchstabe, hat_ziffer, lang_genug])
> print(gueltig)  # False (zu kurz)
> ```

#### `zip()` – Mehrere Iterables parallel durchlaufen

> [!NOTE]
> **`zip(*iterables)`** (Built-in):
> - Kombiniert mehrere Iterables zu Tupeln
> - Gibt Iterator zurück, der Tupel aus parallelen Elementen erzeugt
> - Stoppt bei kürzestem Iterable
> - Signatur: `zip(*iterables)` → `zip object` (Iterator)

> [!TIP]
> ```python
> namen = ["Alice", "Bob", "Charlie"]
> alter = [25, 30, 35]
> staedte = ["Berlin", "Hamburg", "München"]
> 
> # Paralleles Durchlaufen
> for name, age, stadt in zip(namen, alter, staedte):
>     print(f"{name} ({age}) aus {stadt}")
> # Ausgabe:
> # Alice (25) aus Berlin
> # Bob (30) aus Hamburg
> # Charlie (35) aus München
> 
> # zip() zu Liste konvertieren
> paare = list(zip(namen, alter))
> print(paare)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
> 
> # Unterschiedliche Längen (stoppt bei kürzestem)
> liste1 = [1, 2, 3]
> liste2 = ['a', 'b']
> print(list(zip(liste1, liste2)))  # [(1, 'a'), (2, 'b')]
> 
> # "Unzip" mit zip(*...)
> paare = [(1, 'a'), (2, 'b'), (3, 'c')]
> zahlen, buchstaben = zip(*paare)
> print(zahlen)      # (1, 2, 3)
> print(buchstaben)  # ('a', 'b', 'c')
> ```

### Stack-Operationen mit Listen

Python-Listen können direkt als Stack verwendet werden.

> [!TIP]
> ```python
> # Stack mit append() und pop()
> stack = []
> 
> # Push-Operationen
> stack.append(1)
> stack.append(2)
> stack.append(3)
> print(stack)  # [1, 2, 3]
> 
> # Pop-Operationen (LIFO)
> top = stack.pop()
> print(top)    # 3
> print(stack)  # [1, 2]
> 
> # Peek (ohne Entfernen)
> if stack:
>     top = stack[-1]
>     print(top)  # 2
> 
> # Prüfen, ob leer
> is_empty = len(stack) == 0
> # oder (idiomatischer):
> is_empty = not stack
> ```

### Queue-Operationen mit Listen (ineffizient!)

Listen können als Queue verwendet werden, aber **nicht effizient**.

> [!WARNING]
> **Performance-Problem**: `.pop(0)` ist O(n), da alle Elemente nach links verschoben werden müssen. Für effiziente Queues verwende `collections.deque` (wird in späteren Vorlesungen behandelt):
> ```python
> from collections import deque
> 
> queue = deque()
> queue.append(1)     # Enqueue: O(1)
> first = queue.popleft()  # Dequeue: O(1)
> ```

> [!TIP]
> ```python
> # Queue mit Listen (NICHT empfohlen für große Datenmengen!)
> queue = []
> 
> # Enqueue-Operationen
> queue.append(1)
> queue.append(2)
> queue.append(3)
> print(queue)  # [1, 2, 3]
> 
> # Dequeue-Operationen (FIFO)
> first = queue.pop(0)  # Ineffizient: O(n)!
> print(first)   # 1
> print(queue)   # [2, 3]
> 
> # Peek (ohne Entfernen)
> if queue:
>     front = queue[0]
>     print(front)  # 2
> ```

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: In-place Methoden geben None zurück**
> 
> Viele List-Methoden (`.append()`, `.sort()`, `.reverse()`, `.clear()`) modifizieren die Liste direkt und geben `None` zurück.
> 
> **Falsch:**
> ```python
> zahlen = [3, 1, 2]
> zahlen = zahlen.sort()  # zahlen wird None!
> ```
> 
> **Richtig:**
> ```python
> zahlen = [3, 1, 2]
> zahlen.sort()  # Liste wird direkt modifiziert
> # oder:
> sortiert = sorted(zahlen)  # Neue Liste erstellen
> ```

> [!WARNING]
> **Fehler 2: Liste während Iteration modifizieren**
> 
> Niemals eine Liste modifizieren, während man über sie iteriert!
> 
> **Falsch:**
> ```python
> zahlen = [1, 2, 3, 4, 5]
> for zahl in zahlen:
>     if zahl % 2 == 0:
>         zahlen.remove(zahl)  # Überspringt Elemente!
> ```
> 
> **Richtig (Methode 1: Über Kopie iterieren):**
> ```python
> zahlen = [1, 2, 3, 4, 5]
> for zahl in zahlen[:]:  # Iteriere über Kopie
>     if zahl % 2 == 0:
>         zahlen.remove(zahl)
> ```
> 
> **Richtig (Methode 2: List Comprehension):**
> ```python
> zahlen = [1, 2, 3, 4, 5]
> zahlen = [z for z in zahlen if z % 2 != 0]
> ```

> [!WARNING]
> **Fehler 3: Aliasing statt Kopieren**
> 
> Zuweisung erstellt keine Kopie, sondern nur eine Referenz.
> 
> **Falsch:**
> ```python
> liste1 = [1, 2, 3]
> liste2 = liste1  # Nur Referenz!
> liste2.append(4)
> print(liste1)  # [1, 2, 3, 4] (auch liste1 geändert!)
> ```
> 
> **Richtig:**
> ```python
> liste1 = [1, 2, 3]
> liste2 = liste1[:]  # oder list(liste1) oder liste1.copy()
> liste2.append(4)
> print(liste1)  # [1, 2, 3] (unverändert)
> ```

> [!WARNING]
> **Fehler 4: Index außerhalb des Bereichs**
> 
> **Lösung:** Prüfe Länge oder verwende `.get()` bei Dictionaries (V08, Teil 2):
> ```python
> if index < len(liste):
>     element = liste[index]
> ```

> [!WARNING]
> **Fehler 5: Verwechslung append() vs. extend()**
> 
> ```python
> liste = [1, 2, 3]
> liste.append([4, 5])
> print(liste)  # [1, 2, 3, [4, 5]] (Liste als Element!)
> 
> liste = [1, 2, 3]
> liste.extend([4, 5])
> print(liste)  # [1, 2, 3, 4, 5] (Elemente einzeln hinzugefügt)
> ```

### Zusammenfassung Python

Python-Listen sind mächtige, dynamische Datenstrukturen, die Arrays, Stacks und (ineffizient) Queues kombinieren. Listen unterstützen Indizierung, Slicing und zahlreiche Methoden zum Hinzufügen, Entfernen, Sortieren und Durchsuchen von Elementen. Wichtige Methoden sind `.append()` (O(1)), `.insert()` (O(n)), `.remove()` (O(n)), `.pop()` (O(1) am Ende, O(n) am Anfang), `.sort()` (O(n log n)) und `.reverse()` (O(n)).

Tupel sind unveränderliche Alternativen zu Listen und eignen sich für Daten, die nicht modifiziert werden sollen, sowie als Dictionary-Keys. List Slicing ermöglicht eleganten Zugriff auf Teilbereiche und das Erstellen von Kopien. List Comprehensions bieten kompakte Syntax für Transformationen und Filter.

Wichtige Konzepte sind Aliasing (Referenzen statt Kopien), Shallow vs. Deep Copy und die Unterscheidung zwischen in-place Methoden (geben `None` zurück) und Funktionen, die neue Objekte erstellen. Built-in Funktionen wie `sum()`, `all()`, `any()` und `zip()` erweitern die Möglichkeiten der Listen-Verarbeitung erheblich.

### Neue Python-Funktionen/Methoden

In dieser Vorlesung wurden folgende Python-APIs **neu** eingeführt:

#### Datentypen
- **`list`**: Veränderbare Sequenz, erstellt mit `[]` oder `list(iterable)`
- **`tuple`**: Unveränderbare Sequenz, erstellt mit `()` oder `tuple(iterable)`

#### List-Methoden
- **`list.append(x)`**: Element am Ende hinzufügen (O(1))
- **`list.insert(i, x)`**: Element an Index i einfügen (O(n))
- **`list.extend(iterable)`**: Mehrere Elemente hinzufügen (O(k))
- **`list.remove(x)`**: Erstes Vorkommen von x entfernen (O(n))
- **`list.pop(i=-1)`**: Element an Index entfernen und zurückgeben (O(n), O(1) am Ende)
- **`list.clear()`**: Alle Elemente entfernen (O(n))
- **`list.index(x, start=0, stop=len)`**: Index des ersten Vorkommens (O(n))
- **`list.count(x)`**: Anzahl der Vorkommen von x (O(n))
- **`list.sort(key=None, reverse=False)`**: In-place sortieren (O(n log n))
- **`list.reverse()`**: Reihenfolge umkehren (O(n))
- **`list.copy()`**: Shallow Copy erstellen (O(n))

#### Built-in Funktionen
- **`sorted(iterable, key=None, reverse=False)`**: Neue sortierte Liste erstellen
- **`sum(iterable, start=0)`**: Summe aller Elemente
- **`all(iterable)`**: True, wenn alle Elemente truthy
- **`any(iterable)`**: True, wenn mindestens ein Element truthy (vollständige Einführung, in V04 als Vorschau)
- **`zip(*iterables)`**: Mehrere Iterables zu Tupeln kombinieren

#### Operatoren
- **`+` für Listen**: Verkettung (neue Liste)
- **`*` für Listen**: Wiederholung (z.B. `[1, 2] * 3` → `[1, 2, 1, 2, 1, 2]`)
- **`in` für Listen**: Mitgliedschaftstest (O(n))
- **`del liste[index]`**: Element(e) löschen

#### Konzepte
- **List Slicing**: `liste[start:stop:step]`
- **Sequence Unpacking**: `a, b, c = [1, 2, 3]` oder `a, *rest, b = liste`
- **Aliasing vs. Kopieren**: Referenzen vs. echte Kopien
- **Shallow Copy vs. Deep Copy**: `copy.deepcopy()` für verschachtelte Strukturen

---

## Weiterführende Ressourcen

### Theorie
- **"Introduction to Algorithms" (CLRS)**: Kapitel über elementare Datenstrukturen
- **Wikipedia**: Artikel zu Arrays, Linked Lists, Stacks, Queues
- **Visualgo**: Interaktive Visualisierung von Datenstrukturen (https://visualgo.net/)
- **Big-O Cheat Sheet**: Komplexitäten verschiedener Datenstrukturen (https://www.bigocheatsheet.com/)

### Python
- **Python Documentation**: 
  - Built-in Types - List (https://docs.python.org/3/library/stdtypes.html#list)
  - Built-in Types - Tuple (https://docs.python.org/3/library/stdtypes.html#tuple)
- **Real Python**: "Python Lists and Tuples" Tutorial
- **Python Tutor**: Code-Visualisierung (https://pythontutor.com/) – hervorragend für Aliasing/Referenzen
- **Official Python Tutorial**: Data Structures (https://docs.python.org/3/tutorial/datastructures.html)
