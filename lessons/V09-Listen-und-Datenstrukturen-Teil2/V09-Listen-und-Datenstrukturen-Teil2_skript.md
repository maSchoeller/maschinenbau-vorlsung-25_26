# V09: Listen und Datenstrukturen – Teil 2

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Binärbäume und Binäre Suchbäume verstehen und anwenden können
> - Verschiedene Traversierungsalgorithmen (Inorder, Preorder, Postorder) kennenlernen
> - Hash-Tabellen und deren Funktionsweise nachvollziehen
> - Kollisionsbehandlungsstrategien (Chaining, Open Addressing) verstehen
> - Exceptions in Python gezielt behandeln und eigene werfen können
> - `try-except-else-finally` korrekt einsetzen
> - Best Practices für robuste Fehlerbehandlung anwenden

---

## Teil 1: Theorie - Listen und Datenstrukturen – Teil 2

### Überblick

In der vorherigen Vorlesung haben wir grundlegende Datenstrukturen wie Arrays, verkettete Listen, Stacks und Queues kennengelernt. Diese Vorlesung erweitert das Repertoire um hierarchische und hash-basierte Datenstrukturen. Bäume ermöglichen effiziente Such-, Einfüge- und Löschoperationen in sortierten Daten, während Hash-Tabellen nahezu konstanten Zugriff auf Elemente über Schlüssel bieten. Das Verständnis dieser Strukturen ist fundamental für die Entwicklung effizienter Algorithmen und bildet die Grundlage moderner Datenbanksysteme, Compiler und Netzwerk-Routing-Protokolle.

### Bäume: Grundkonzepte und Terminologie

Ein **Baum** ist eine hierarchische Datenstruktur, die aus **Knoten** (Nodes) besteht, die durch **Kanten** (Edges) verbunden sind. Bäume finden Anwendung in Dateisystemen, Entscheidungsbäumen in der KI, Syntaxbäumen in Compilern und vielen weiteren Bereichen.

> [!NOTE]
> **Baum (Tree)**: Eine hierarchische Datenstruktur mit einem **Wurzelknoten** (Root), von dem aus alle anderen Knoten erreichbar sind. Ein Baum enthält keine Zyklen – es gibt genau einen Pfad zwischen zwei beliebigen Knoten.

#### Fundamentale Begriffe

Jeder Baum besteht aus mehreren Komponenten, die durch präzise Terminologie beschrieben werden:

**Knoten (Node)**: Ein **Knoten** ist ein einzelnes Element im Baum, das einen Wert (Datum) speichert und Referenzen zu seinen Kind-Knoten enthält. Der oberste Knoten heißt **Wurzel** (Root). Knoten ohne Kinder heißen **Blätter** (Leaves).

**Kante (Edge)**: Eine **Kante** ist die Verbindung zwischen einem Elternknoten und einem seiner Kindknoten. Die Anzahl der Kanten im Baum ist immer `Anzahl Knoten - 1`.

**Pfad (Path)**: Ein **Pfad** ist eine Folge von Knoten, bei der jeder Knoten über eine Kante mit dem nächsten verbunden ist. Die **Pfadlänge** ist die Anzahl der Kanten im Pfad.

**Tiefe (Depth)**: Die **Tiefe** eines Knotens ist die Länge des Pfads von der Wurzel zu diesem Knoten. Die Wurzel hat Tiefe 0.

**Höhe (Height)**: Die **Höhe** eines Baums ist die maximale Tiefe aller Blätter. Ein Baum mit nur einem Knoten (der Wurzel) hat Höhe 0.

**Grad (Degree)**: Der **Grad** eines Knotens ist die Anzahl seiner Kindknoten. Der **Grad eines Baums** ist der maximale Grad aller Knoten.

> [!TIP]
> **Visualisierung eines Beispielbaums**:
> 
> ```mermaid
> graph TD
>     A[10<br/>Wurzel<br/>Tiefe: 0] --> B[5<br/>Tiefe: 1]
>     A --> C[15<br/>Tiefe: 1]
>     B --> D[3<br/>Tiefe: 2]
>     B --> E[7<br/>Tiefe: 2]
>     C --> F[12<br/>Tiefe: 2]
>     C --> G[20<br/>Tiefe: 2]
>     
>     style A fill:#e1f5ff
>     style D fill:#ffe1e1
>     style E fill:#ffe1e1
>     style F fill:#ffe1e1
>     style G fill:#ffe1e1
> ```
> 
> In diesem Baum:
> - **Wurzel**: Knoten 10 (Tiefe 0)
> - **Blätter**: Knoten 3, 7, 12, 20 (rot markiert)
> - **Höhe**: 2 (längster Pfad von Wurzel zu einem Blatt)
> - **Grad des Baums**: 2 (jeder Knoten hat maximal 2 Kinder)

### Binärbäume

Ein **Binärbaum** ist ein Baum, bei dem jeder Knoten maximal zwei Kinder hat. Diese werden als **linkes Kind** und **rechtes Kind** bezeichnet. Binärbäume sind die Grundlage für viele spezialisierte Varianten wie Binäre Suchbäume, AVL-Bäume und Heaps.

> [!NOTE]
> **Binärbaum (Binary Tree)**: Ein Baum, bei dem jeder Knoten maximal zwei Kindknoten hat. Die Position der Kinder ist relevant: Es wird zwischen linkem und rechtem Kind unterschieden.

#### Eigenschaften von Binärbäumen

Binärbäume können verschiedene strukturelle Eigenschaften aufweisen, die ihre Effizienz und Anwendbarkeit beeinflussen:

**Vollständiger Binärbaum (Full Binary Tree)**: Jeder Knoten hat entweder 0 oder 2 Kinder (keine Knoten mit nur einem Kind).

**Perfekter Binärbaum (Perfect Binary Tree)**: Alle inneren Knoten haben genau 2 Kinder, und alle Blätter befinden sich auf derselben Ebene. Dies ist die kompakteste Form und hat genau `2^(h+1) - 1` Knoten bei Höhe `h`.

**Kompletter Binärbaum (Complete Binary Tree)**: Alle Ebenen sind vollständig gefüllt, außer möglicherweise die letzte, die von links nach rechts gefüllt ist. Diese Eigenschaft wird in Heaps ausgenutzt, um effiziente Array-Repräsentationen zu ermöglichen.

**Degenerierter Baum (Degenerate Tree)**: Jeder Knoten hat nur ein Kind, wodurch der Baum zu einer linearen Liste degeneriert. Dies ist der ungünstigste Fall für Such-Operationen.

> [!TIP]
> **Vergleich verschiedener Binärbaum-Formen**:
> 
> ```mermaid
> graph TD
>     subgraph "Perfekter Binärbaum"
>     A1[A] --> B1[B]
>     A1 --> C1[C]
>     B1 --> D1[D]
>     B1 --> E1[E]
>     C1 --> F1[F]
>     C1 --> G1[G]
>     end
>     
>     subgraph "Degenerierter Baum"
>     A2[A] --> B2[B]
>     B2 --> C2[C]
>     C2 --> D2[D]
>     end
> ```
> 
> **Perfekter Baum**: Alle Ebenen vollständig gefüllt, maximale Balance.  
> **Degenerierter Baum**: Entspricht einer verketteten Liste, keine Vorteile gegenüber linearen Strukturen.

### Binäre Suchbäume (BST)

Ein **Binärer Suchbaum** (Binary Search Tree, BST) ist ein Binärbaum mit einer entscheidenden Ordnungseigenschaft: Für jeden Knoten gilt, dass alle Werte im linken Teilbaum kleiner und alle Werte im rechten Teilbaum größer sind als der Wert des Knotens selbst. Diese Eigenschaft ermöglicht effiziente Such-, Einfüge- und Löschoperationen.

> [!NOTE]
> **Binärer Suchbaum (BST)**: Ein Binärbaum, bei dem für jeden Knoten gilt:
> - Alle Werte im **linken Teilbaum** sind **kleiner** als der Wert des Knotens
> - Alle Werte im **rechten Teilbaum** sind **größer** als der Wert des Knotens
> - Diese Eigenschaft gilt rekursiv für alle Teilbäume

#### Operationen auf Binären Suchbäumen

Die Operationen auf BSTs nutzen die Ordnungseigenschaft, um effizient zu arbeiten:

**Suchen (Search)**: Um einen Wert zu finden, startet man an der Wurzel und vergleicht den gesuchten Wert mit dem aktuellen Knoten. Ist der gesuchte Wert kleiner, wird im linken Teilbaum weitergesucht, andernfalls im rechten. Dieser Prozess wiederholt sich, bis der Wert gefunden wird oder ein Blatt erreicht ist.

**Zeitkomplexität**: 
- **Best/Average Case**: O(log n) bei balanciertem Baum
- **Worst Case**: O(n) bei degeneriertem Baum (ähnlich linearer Liste)

**Einfügen (Insert)**: Ein neuer Wert wird eingefügt, indem man zunächst die Position sucht, an der er stehen müsste (wie beim Suchen). Sobald ein Blatt erreicht ist, wird der neue Knoten als Kind hinzugefügt.

**Zeitkomplexität**: Analog zur Suche – O(log n) im Average Case, O(n) im Worst Case.

**Löschen (Delete)**: Das Löschen ist die komplexeste Operation und umfasst drei Fälle:
1. **Knoten ist Blatt**: Einfach entfernen
2. **Knoten hat ein Kind**: Knoten durch sein Kind ersetzen
3. **Knoten hat zwei Kinder**: Finde den **Inorder-Nachfolger** (kleinster Wert im rechten Teilbaum) oder **Inorder-Vorgänger** (größter Wert im linken Teilbaum), kopiere dessen Wert in den zu löschenden Knoten und lösche den Nachfolger/Vorgänger rekursiv

**Zeitkomplexität**: O(log n) im Average Case, O(n) im Worst Case.

> [!TIP]
> **Beispiel eines Binären Suchbaums**:
> 
> ```mermaid
> graph TD
>     A[50] --> B[30]
>     A --> C[70]
>     B --> D[20]
>     B --> E[40]
>     C --> F[60]
>     C --> G[80]
>     
>     style A fill:#e1f5ff
>     style B fill:#fff4e1
>     style C fill:#fff4e1
> ```
> 
> **Eigenschaften**:
> - Linker Teilbaum von 50: {20, 30, 40} – alle < 50
> - Rechter Teilbaum von 50: {60, 70, 80} – alle > 50
> - **Suche nach 40**: 50 → 30 → 40 (3 Vergleiche)
> - **Suche nach 80**: 50 → 70 → 80 (3 Vergleiche)

> [!WARNING]
> **Balance ist entscheidend**: Ein unbalancierter BST (degeneriert) verliert seine Effizienzvorteile. In der Praxis werden daher **selbstbalancierende Bäume** wie AVL-Bäume oder Rot-Schwarz-Bäume verwendet, die automatisch die Balance nach Einfüge- und Löschoperationen wiederherstellen.

### Traversierung von Bäumen

Die **Traversierung** eines Baums bezeichnet den systematischen Besuch aller Knoten in einer definierten Reihenfolge. Es gibt drei fundamentale Traversierungsstrategien für Binärbäume, die sich darin unterscheiden, wann der Wurzelknoten relativ zu seinen Kindern besucht wird.

> [!NOTE]
> **Traversierung (Tree Traversal)**: Der Prozess, alle Knoten eines Baums genau einmal in einer bestimmten Reihenfolge zu besuchen. Die Wahl der Traversierungsart hängt vom Anwendungsfall ab (z.B. sortierte Ausgabe, Auswertung von Ausdrücken, Strukturanalyse).

#### Inorder-Traversierung (LWR)

Bei der **Inorder-Traversierung** wird zunächst der linke Teilbaum besucht, dann die Wurzel, dann der rechte Teilbaum. Die Reihenfolge ist: **Links → Wurzel → Rechts** (LWR).

**Algorithmus**:
1. Traversiere rekursiv den linken Teilbaum
2. Besuche die Wurzel (verarbeite den aktuellen Knoten)
3. Traversiere rekursiv den rechten Teilbaum

**Besonderheit bei BST**: Die Inorder-Traversierung eines Binären Suchbaums liefert die Werte in **aufsteigend sortierter Reihenfolge**. Dies macht sie besonders nützlich für Sortier- und Validierungsoperationen.

**Zeitkomplexität**: O(n) – jeder Knoten wird genau einmal besucht.

> [!TIP]
> **Inorder-Traversierung Beispiel**:
> 
> Gegeben ist folgender BST:
> 
> ```mermaid
> graph TD
>     A[50] --> B[30]
>     A --> C[70]
>     B --> D[20]
>     B --> E[40]
>     C --> F[60]
>     C --> G[80]
> ```
> 
> **Inorder-Reihenfolge**: 20 → 30 → 40 → 50 → 60 → 70 → 80  
> **Beachte**: Aufsteigend sortiert!

#### Preorder-Traversierung (WLR)

Bei der **Preorder-Traversierung** wird zunächst die Wurzel besucht, dann der linke Teilbaum, dann der rechte Teilbaum. Die Reihenfolge ist: **Wurzel → Links → Rechts** (WLR).

**Algorithmus**:
1. Besuche die Wurzel (verarbeite den aktuellen Knoten)
2. Traversiere rekursiv den linken Teilbaum
3. Traversiere rekursiv den rechten Teilbaum

**Anwendung**: Die Preorder-Traversierung wird verwendet, um die Struktur eines Baums zu kopieren oder einen Baum in eine Darstellung zu serialisieren, die später rekonstruiert werden kann. Sie entspricht der Reihenfolge, in der man einen Baum "von oben nach unten" aufbaut.

**Zeitkomplexität**: O(n)

> [!TIP]
> **Preorder-Traversierung Beispiel**:
> 
> Derselbe BST wie oben:
> 
> **Preorder-Reihenfolge**: 50 → 30 → 20 → 40 → 70 → 60 → 80  
> **Verwendung**: Baum-Kopie, Serialisierung, Präfix-Notation

#### Postorder-Traversierung (LRW)

Bei der **Postorder-Traversierung** wird zunächst der linke Teilbaum besucht, dann der rechte Teilbaum, dann die Wurzel. Die Reihenfolge ist: **Links → Rechts → Wurzel** (LRW).

**Algorithmus**:
1. Traversiere rekursiv den linken Teilbaum
2. Traversiere rekursiv den rechten Teilbaum
3. Besuche die Wurzel (verarbeite den aktuellen Knoten)

**Anwendung**: Die Postorder-Traversierung wird verwendet, um einen Baum zu löschen (Kinder zuerst, dann Eltern) oder um Ausdrücke in Postfix-Notation auszuwerten. Sie garantiert, dass ein Knoten erst verarbeitet wird, nachdem alle seine Nachkommen verarbeitet wurden.

**Zeitkomplexität**: O(n)

> [!TIP]
> **Postorder-Traversierung Beispiel**:
> 
> Derselbe BST wie oben:
> 
> **Postorder-Reihenfolge**: 20 → 40 → 30 → 60 → 80 → 70 → 50  
> **Verwendung**: Baum-Löschung, Postfix-Notation, Speicherfreigabe

#### Level-Order-Traversierung (Breitensuche)

Die **Level-Order-Traversierung** (auch **Breitensuche** oder BFS – Breadth-First Search genannt) besucht die Knoten ebenenweise von oben nach unten und innerhalb jeder Ebene von links nach rechts.

**Algorithmus** (iterativ mit Queue):
1. Füge die Wurzel in eine Queue ein
2. Solange die Queue nicht leer ist:
   - Entferne den vordersten Knoten aus der Queue
   - Besuche diesen Knoten (verarbeite ihn)
   - Füge seine Kindknoten (links, dann rechts) zur Queue hinzu

**Anwendung**: Level-Order-Traversierung wird verwendet, um die Struktur eines Baums ebenenweise zu analysieren oder den kürzesten Pfad in ungewichteten Graphen zu finden.

**Zeitkomplexität**: O(n)  
**Speicherkomplexität**: O(w), wobei w die maximale Breite des Baums ist

> [!TIP]
> **Level-Order-Traversierung Beispiel**:
> 
> Derselbe BST wie oben:
> 
> **Level-Order-Reihenfolge**: 50 → 30 → 70 → 20 → 40 → 60 → 80  
> **Verwendung**: Ebenenweise Ausgabe, Breitensuche, Strukturanalyse

> [!WARNING]
> **Wahl der Traversierung**: Die Wahl der Traversierungsart hängt stark vom Anwendungsfall ab:
> - **Inorder**: Sortierte Ausgabe bei BST
> - **Preorder**: Baum-Kopie, Serialisierung
> - **Postorder**: Baum-Löschung, Ausdrucks-Auswertung
> - **Level-Order**: Ebenenweise Verarbeitung, Breitensuche

### Hash-Tabellen: Grundprinzip

Eine **Hash-Tabelle** (Hash Table oder Hash Map) ist eine Datenstruktur, die **Schlüssel-Wert-Paare** speichert und nahezu konstanten Zugriff (O(1) im Average Case) ermöglicht. Sie ist eine der wichtigsten Datenstrukturen in der Informatik und wird in Datenbanken, Caches, Compilern und vielen weiteren Anwendungen eingesetzt.

> [!NOTE]
> **Hash-Tabelle (Hash Table)**: Eine Datenstruktur, die Schlüssel über eine **Hash-Funktion** auf Indizes in einem Array abbildet. Dies ermöglicht schnellen Zugriff, Einfügen und Löschen von Elementen anhand ihrer Schlüssel.

#### Hash-Funktionen

Das Herzstück jeder Hash-Tabelle ist die **Hash-Funktion**. Sie nimmt einen Schlüssel als Eingabe und berechnet daraus einen ganzzahligen **Hash-Wert**, der als Index in ein Array verwendet wird.

> [!NOTE]
> **Hash-Funktion**: Eine Funktion `h(key) → index`, die einen Schlüssel deterministisch auf einen Array-Index abbildet. Eine gute Hash-Funktion verteilt die Schlüssel gleichmäßig über den verfügbaren Speicherbereich, um Kollisionen zu minimieren.

**Eigenschaften einer guten Hash-Funktion**:
1. **Determinismus**: Derselbe Schlüssel erzeugt immer denselben Hash-Wert
2. **Gleichverteilung**: Schlüssel werden gleichmäßig über den Hash-Bereich verteilt
3. **Effizienz**: Die Berechnung des Hash-Werts ist schnell (O(1))
4. **Minimierung von Kollisionen**: Verschiedene Schlüssel sollten möglichst unterschiedliche Hash-Werte erzeugen

**Einfache Hash-Funktionen**:
- **Modulo-Methode**: `h(key) = key % table_size` (für ganzzahlige Schlüssel)
- **String-Hash**: Summiere ASCII-Werte der Zeichen, multipliziert mit Potenzen einer Primzahl
- **Multiplikative Methode**: `h(key) = floor(table_size * (key * A mod 1))`, wobei A eine Konstante (z.B. 0.618) ist

> [!TIP]
> **Beispiel einer einfachen Hash-Funktion für Strings**:
> 
> ```
> h("hello") = (h × 31^4 + e × 31^3 + l × 31^2 + l × 31 + o) % table_size
> ```
> 
> Die Zahl 31 ist eine beliebte Wahl (Primzahl, effiziente Berechnung als `x << 5 - x`).

#### Kollisionen

Eine **Kollision** tritt auf, wenn zwei unterschiedliche Schlüssel denselben Hash-Wert (Index) erzeugen. Kollisionen sind unvermeidlich, da der Schlüsselraum in der Regel größer ist als die Hash-Tabellen-Größe (Schubfachprinzip).

> [!NOTE]
> **Kollision (Collision)**: Situation, in der zwei verschiedene Schlüssel `k1` und `k2` denselben Hash-Wert erzeugen: `h(k1) = h(k2)`. Kollisionsbehandlung ist ein zentrales Problem beim Design von Hash-Tabellen.

### Kollisionsbehandlung: Chaining

**Chaining** (Verkettung) ist die klassische Methode zur Kollisionsbehandlung. Jede Zelle der Hash-Tabelle enthält nicht direkt ein Element, sondern eine **verkettete Liste** (oder eine andere Datenstruktur wie einen Baum), die alle Elemente mit demselben Hash-Wert speichert.

> [!NOTE]
> **Chaining**: Kollisionsbehandlungsstrategie, bei der jede Zelle der Hash-Tabelle eine verkettete Liste enthält. Alle Elemente mit demselben Hash-Wert werden in dieser Liste gespeichert.

**Funktionsweise**:
- **Einfügen**: Berechne `index = h(key)`, füge das Element am Anfang oder Ende der Liste bei `table[index]` hinzu
- **Suchen**: Berechne `index = h(key)`, durchsuche die Liste bei `table[index]` linear nach dem Schlüssel
- **Löschen**: Berechne `index = h(key)`, finde das Element in der Liste und entferne es

**Komplexität**:
- **Best Case**: O(1) – keine Kollision, Liste hat Länge 1
- **Average Case**: O(1 + α), wobei α = n/m (Anzahl Elemente / Tabellengröße) der **Ladefaktor** ist
- **Worst Case**: O(n) – alle Elemente kollidieren, eine einzige Liste der Länge n

**Vorteile**:
- Einfach zu implementieren
- Tabelle muss nie vollständig sein, kann über 100% Auslastung gehen
- Geeignet für dynamisch wachsende Datenmengen

**Nachteile**:
- Zusätzlicher Speicher für Listenzeiger
- Cache-ineffizient durch Pointer-Dereferenzierung
- Performance degradiert bei hohem Ladefaktor

> [!TIP]
> **Chaining-Visualisierung**:
> 
> ```mermaid
> graph LR
>     subgraph Hash-Tabelle
>     A[Index 0] --> L1[Key: 10<br/>Value: A]
>     B[Index 1] --> L2[Key: 21<br/>Value: B] --> L3[Key: 31<br/>Value: C]
>     C[Index 2] --> L4[Key: 12<br/>Value: D]
>     D[Index 3]
>     end
> ```
> 
> Annahme: `h(key) = key % 10`  
> **Kollision** bei Index 1: Schlüssel 21 und 31 haben beide `h(k) = 1`

### Kollisionsbehandlung: Open Addressing

Bei **Open Addressing** (offene Adressierung) werden alle Elemente direkt in der Hash-Tabelle selbst gespeichert, nicht in separaten Listen. Bei einer Kollision wird nach einem alternativen freien Platz in der Tabelle gesucht, indem eine **Sondierungssequenz** (Probing Sequence) verwendet wird.

> [!NOTE]
> **Open Addressing**: Kollisionsbehandlungsstrategie, bei der alle Elemente direkt in der Hash-Tabelle gespeichert werden. Bei einer Kollision wird systematisch nach einem freien Platz gesucht.

#### Linear Probing

**Linear Probing** ist die einfachste Open-Addressing-Strategie. Bei einer Kollision wird linear durch die Tabelle gegangen: `h(key), h(key)+1, h(key)+2, ...`, bis ein freier Platz gefunden wird.

**Sondierungsformel**: `h'(key, i) = (h(key) + i) % table_size`, wobei i = 0, 1, 2, ...

**Vorteile**:
- Sehr cache-freundlich (sequenzieller Speicherzugriff)
- Einfach zu implementieren
- Keine zusätzlichen Zeiger erforderlich

**Nachteile**:
- **Primary Clustering**: Es entstehen lange zusammenhängende Bereiche belegter Zellen, was die Suchzeit erhöht
- Tabelle darf nicht zu voll werden (üblich: Ladefaktor < 0.7)

#### Quadratic Probing

**Quadratic Probing** verwendet eine quadratische Funktion zur Sondierung: `h(key), h(key)+1², h(key)+2², h(key)+3², ...`

**Sondierungsformel**: `h'(key, i) = (h(key) + c₁·i + c₂·i²) % table_size`, wobei c₁ und c₂ Konstanten sind

**Vorteile**:
- Reduziert Primary Clustering
- Bessere Verteilung als Linear Probing

**Nachteile**:
- **Secondary Clustering**: Schlüssel mit demselben Hash-Wert folgen derselben Sondierungssequenz
- Kompliziertere Implementierung
- Nicht alle Zellen werden garantiert untersucht

#### Double Hashing

**Double Hashing** verwendet eine zweite Hash-Funktion zur Berechnung der Schrittweite: `h(key), h(key)+h₂(key), h(key)+2·h₂(key), ...`

**Sondierungsformel**: `h'(key, i) = (h(key) + i · h₂(key)) % table_size`

**Anforderungen an h₂**:
- `h₂(key)` darf nie 0 sein
- `h₂(key)` sollte relativ prim zu `table_size` sein (oft: `table_size` ist Primzahl)

**Vorteile**:
- Eliminiert sowohl Primary als auch Secondary Clustering
- Beste Verteilung unter den Open-Addressing-Methoden
- Annähernd gleichmäßige Sondierung

**Nachteile**:
- Etwas komplexere Implementierung
- Zusätzliche Hash-Funktion muss berechnet werden

> [!TIP]
> **Vergleich der Probing-Strategien**:
> 
> | Strategie | Clustering | Cache-Effizienz | Komplexität |
> |-----------|-----------|----------------|-------------|
> | Linear Probing | Stark (Primary) | Sehr gut | Einfach |
> | Quadratic Probing | Mittel (Secondary) | Gut | Mittel |
> | Double Hashing | Minimal | Mittel | Komplex |

> [!WARNING]
> **Ladefaktor bei Open Addressing**: Open-Addressing-Tabellen müssen rechtzeitig vergrößert werden (**Rehashing**). Ein Ladefaktor > 0.7 führt zu drastischem Performance-Verlust. Bei α → 1 (Tabelle fast voll) steigt die erwartete Suchzeit exponentiell.

### Operationen und Komplexitätsanalyse

Die Effizienz von Hash-Tabellen hängt stark von der Qualität der Hash-Funktion, der Kollisionsbehandlung und dem Ladefaktor ab.

#### Einfügen (Insert)

**Chaining**:
1. Berechne `index = h(key)`
2. Füge das Element zur Liste bei `table[index]` hinzu (Anfang oder Ende)

**Zeitkomplexität**: O(1) im Average Case, O(n) im Worst Case (alle Elemente in einer Liste)

**Open Addressing**:
1. Berechne `index = h(key)`
2. Sondiere, bis ein freier Platz gefunden wird
3. Füge das Element an der gefundenen Position ein

**Zeitkomplexität**: O(1/(1-α)) im Average Case, wobei α der Ladefaktor ist

#### Suchen (Search)

**Chaining**:
1. Berechne `index = h(key)`
2. Durchsuche die Liste bei `table[index]` linear

**Zeitkomplexität**: O(1 + α) im Average Case, O(n) im Worst Case

**Open Addressing**:
1. Berechne `index = h(key)`
2. Sondiere, bis der Schlüssel gefunden oder ein leerer Platz erreicht wird

**Zeitkomplexität**: O(1/(1-α)) im Average Case

#### Löschen (Delete)

**Chaining**:
1. Berechne `index = h(key)`
2. Finde und entferne das Element aus der Liste bei `table[index]`

**Zeitkomplexität**: O(1 + α) im Average Case, O(n) im Worst Case

**Open Addressing**:
1. Berechne `index = h(key)`
2. Sondiere, bis der Schlüssel gefunden wird
3. Markiere die Zelle als **gelöscht** (nicht leer), um die Sondierungssequenz nicht zu unterbrechen

**Problem**: Gelöschte Zellen können die Tabelle "verschmutzen". Lösung: Periodisches Rehashing.

**Zeitkomplexität**: O(1/(1-α)) im Average Case

> [!TIP]
> **Zusammenfassung Zeitkomplexitäten**:
> 
> | Operation | Chaining (Average) | Open Addressing (Average) | Worst Case (beide) |
> |-----------|-------------------|--------------------------|-------------------|
> | Insert | O(1) | O(1/(1-α)) | O(n) |
> | Search | O(1 + α) | O(1/(1-α)) | O(n) |
> | Delete | O(1 + α) | O(1/(1-α)) | O(n) |
> 
> **α = Ladefaktor** (n/m, Anzahl Elemente / Tabellengröße)

### Zusammenfassung Theorie

Die fortgeschrittenen Datenstrukturen dieser Vorlesung erweitern das Werkzeugrepertoire erheblich. **Binärbäume** und **Binäre Suchbäume** ermöglichen hierarchische Organisation und effiziente Suchoperationen in O(log n), sofern der Baum balanciert ist. Die **Traversierungsalgorithmen** (Inorder, Preorder, Postorder, Level-Order) bieten verschiedene Möglichkeiten, Bäume systematisch zu durchlaufen, wobei jede Methode spezifische Anwendungsfälle hat.

**Hash-Tabellen** bieten nahezu konstanten Zugriff (O(1) im Average Case) auf Elemente über Schlüssel, was sie zu einer der effizientesten Datenstrukturen für Lookup-Operationen macht. Die beiden Hauptstrategien zur Kollisionsbehandlung – **Chaining** und **Open Addressing** – haben unterschiedliche Vor- und Nachteile. Chaining ist robuster bei hoher Auslastung, während Open Addressing speichereffizienter und cache-freundlicher ist.

Die Wahl der richtigen Datenstruktur hängt vom konkreten Anwendungsfall ab: Benötigt man sortierte Daten? Wie häufig werden Einfüge-, Such- und Löschoperationen durchgeführt? Wie groß ist der Datensatz? Ein fundiertes Verständnis dieser Strukturen und ihrer Komplexitäten ist essentiell für die Entwicklung performanter Software.

---

## Teil 2: Python-Praxis - Try-Catch (Fehlerbehandlung)

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

Fehlerbehandlung ist ein fundamentaler Aspekt robuster Software-Entwicklung. In Python werden Laufzeitfehler als **Exceptions** (Ausnahmen) behandelt, die den normalen Programmablauf unterbrechen und eine strukturierte Fehlerbehandlung erfordern. Ohne geeignete Fehlerbehandlung stürzt ein Programm bei unerwarteten Eingaben oder Zuständen ab, was in produktiven Systemen inakzeptabel ist. Das `try-except`-Konstrukt ermöglicht es, potenzielle Fehlerquellen zu identifizieren, Fehler gezielt abzufangen und darauf angemessen zu reagieren – sei es durch alternative Programmlogik, Benutzerbenachrichtigung oder kontrolliertes Herunterfahren.

In dieser Vorlesung lernen wir, wie Python Exceptions strukturiert, wie wir sie abfangen und behandeln, und welche Best Practices für robuste und wartbare Fehlerbehandlung gelten.

### Was sind Exceptions?

Eine **Exception** ist ein Ereignis, das während der Programmausführung auftritt und den normalen Ablauf unterbricht. Exceptions werden **geworfen** (raised), wenn Python auf einen Fehler stößt, den es nicht automatisch beheben kann.

> [!NOTE]
> **Exception (Ausnahme)**: Ein Objekt, das einen Fehler oder eine außergewöhnliche Situation während der Programmausführung repräsentiert. Python hat eine Hierarchie vordefinierter Exception-Typen, die verschiedene Fehlerarten kategorisieren.

#### Häufige Exception-Typen

Python bietet eine umfangreiche Hierarchie von Exception-Typen. Die wichtigsten für Einsteiger sind:

**`ValueError`**: Wird geworfen, wenn eine Funktion ein Argument mit dem richtigen Typ, aber unangemessenem Wert erhält.

> [!TIP]
> ```python
> # ValueError-Beispiel:
> zahl = int("abc")  # ValueError: invalid literal for int()
> ```

**`TypeError`**: Wird geworfen, wenn eine Operation auf einen ungeeigneten Datentyp angewendet wird.

> [!TIP]
> ```python
> # TypeError-Beispiel:
> ergebnis = "5" + 10  # TypeError: can only concatenate str to str
> ```

**`IndexError`**: Wird geworfen, wenn versucht wird, auf einen Index zuzugreifen, der außerhalb des gültigen Bereichs einer Sequenz liegt.

> [!TIP]
> ```python
> # IndexError-Beispiel:
> liste = [1, 2, 3]
> element = liste[10]  # IndexError: list index out of range
> ```

**`KeyError`**: Wird geworfen, wenn versucht wird, auf einen nicht existierenden Dictionary-Schlüssel zuzugreifen.

> [!TIP]
> ```python
> # KeyError-Beispiel:
> daten = {"name": "Alice"}
> alter = daten["alter"]  # KeyError: 'alter'
> ```

**`FileNotFoundError`**: Wird geworfen, wenn versucht wird, eine nicht existierende Datei zu öffnen.

> [!TIP]
> ```python
> # FileNotFoundError-Beispiel:
> with open("nicht_vorhanden.txt") as datei:
>     inhalt = datei.read()
> # FileNotFoundError: [Errno 2] No such file or directory
> ```

**`ZeroDivisionError`**: Wird geworfen, wenn versucht wird, durch Null zu teilen.

> [!TIP]
> ```python
> # ZeroDivisionError-Beispiel:
> ergebnis = 10 / 0  # ZeroDivisionError: division by zero
> ```

**`AttributeError`**: Wird geworfen, wenn versucht wird, auf ein nicht existierendes Attribut eines Objekts zuzugreifen.

> [!TIP]
> ```python
> # AttributeError-Beispiel:
> text = "Hallo"
> text.append("!")  # AttributeError: 'str' object has no attribute 'append'
> ```

> [!NOTE]
> Alle Exception-Typen erben von der Basisklasse `BaseException`. Die meisten benutzerdefinierten Exceptions sollten von `Exception` erben, nicht direkt von `BaseException`.

### Das `try-except`-Konstrukt

Das `try-except`-Konstrukt ist das Herzstück der Fehlerbehandlung in Python. Code, der möglicherweise eine Exception werfen könnte, wird in einen `try`-Block eingeschlossen. Wenn eine Exception auftritt, wird der `try`-Block unterbrochen und der entsprechende `except`-Block ausgeführt.

> [!NOTE]
> **`try-except`-Block**: Ein Kontrollstrukt, das es ermöglicht, potenziell fehlerhafte Code-Abschnitte zu überwachen und auf Fehler zu reagieren, ohne dass das Programm abstürzt.
> 
> **Syntax**:
> ```python
> try:
>     # Code, der eine Exception werfen könnte
>     risikoreicher_code()
> except ExceptionType:
>     # Code, der ausgeführt wird, wenn ExceptionType auftritt
>     fehlerbehandlung()
> ```

#### Grundlegende Verwendung

Die einfachste Form fängt eine spezifische Exception ab:

> [!TIP]
> ```python
> try:
>     zahl = int(input("Gib eine Zahl ein: "))
>     ergebnis = 100 / zahl
>     print(f"Ergebnis: {ergebnis}")
> except ValueError:
>     print("Fehler: Keine gültige Zahl eingegeben!")
> except ZeroDivisionError:
>     print("Fehler: Division durch Null ist nicht erlaubt!")
> ```
> 
> **Erklärung**:
> - Der `try`-Block enthält Code, der bei ungültiger Eingabe oder Division durch Null fehlschlagen kann
> - Wenn `int()` keine Zahl konvertieren kann, wird `ValueError` abgefangen
> - Wenn der Benutzer 0 eingibt, wird `ZeroDivisionError` abgefangen
> - Andere Exceptions würden nicht abgefangen und das Programm würde abstürzen

> [!WARNING]
> **Vermeide blanket `except`**: Ein nacktes `except:` ohne Angabe eines Exception-Typs fängt **alle** Exceptions ab, einschließlich `KeyboardInterrupt` (Strg+C). Dies macht Debugging extrem schwierig und sollte vermieden werden. Nutze stattdessen spezifische Exception-Typen oder `except Exception:` für generische Fehlerbehandlung.

### Mehrere Exception-Typen abfangen

Ein `try`-Block kann mehrere `except`-Klauseln haben, um verschiedene Fehlertypen unterschiedlich zu behandeln.

> [!TIP]
> ```python
> def sicheres_liste_zugriff(liste, index):
>     """Greift sicher auf ein Listenelement zu."""
>     try:
>         return liste[index]
>     except IndexError:
>         print(f"Fehler: Index {index} existiert nicht.")
>         return None
>     except TypeError:
>         print("Fehler: Index muss eine Ganzzahl sein.")
>         return None
> 
> # Anwendung:
> zahlen = [10, 20, 30]
> print(sicheres_liste_zugriff(zahlen, 1))    # 20
> print(sicheres_liste_zugriff(zahlen, 10))   # Fehler: Index 10 existiert nicht. / None
> print(sicheres_liste_zugriff(zahlen, "a"))  # Fehler: Index muss eine Ganzzahl sein. / None
> ```

#### Mehrere Exceptions in einer Klausel

Wenn mehrere Exception-Typen identisch behandelt werden sollen, können sie als Tupel gruppiert werden:

> [!TIP]
> ```python
> try:
>     wert = int(input("Zahl: "))
>     ergebnis = 100 / wert
> except (ValueError, ZeroDivisionError):
>     print("Ungültige Eingabe oder Division durch Null!")
> ```
> 
> Dies ist eine kompaktere Alternative zu separaten `except`-Blöcken mit identischem Code.

### Zugriff auf das Exception-Objekt

Python ermöglicht es, das Exception-Objekt selbst zu erfassen, um detaillierte Fehlerinformationen zu extrahieren:

> [!NOTE]
> **Syntax**: `except ExceptionType as variable_name`
> 
> Das Exception-Objekt enthält Informationen wie die Fehlermeldung und kann für Logging oder detaillierte Benutzerbenachrichtigung verwendet werden.

> [!TIP]
> ```python
> try:
>     datei = open("config.txt")
>     inhalt = datei.read()
> except FileNotFoundError as e:
>     print(f"Datei konnte nicht geöffnet werden: {e}")
>     print(f"Dateipfad: {e.filename}")
> except PermissionError as e:
>     print(f"Keine Berechtigung zum Zugriff: {e}")
> ```
> 
> **Output-Beispiel**:
> ```
> Datei konnte nicht geöffnet werden: [Errno 2] No such file or directory: 'config.txt'
> Dateipfad: config.txt
> ```

### Die `else`-Klausel im `try-except`

Die `else`-Klausel wird ausgeführt, wenn der `try`-Block **keine Exception** geworfen hat. Dies ist nützlich, um Code zu platzieren, der nur bei Erfolg ausgeführt werden soll, aber selbst keine Exception-Behandlung benötigt.

> [!NOTE]
> **`else`-Klausel**: Ein optionaler Block nach allen `except`-Klauseln, der nur ausgeführt wird, wenn keine Exception aufgetreten ist.
> 
> **Syntax**:
> ```python
> try:
>     code()
> except ExceptionType:
>     fehlerbehandlung()
> else:
>     erfolgs_code()  # Nur wenn keine Exception auftrat
> ```

> [!TIP]
> ```python
> def datei_verarbeiten(dateiname):
>     """Verarbeitet eine Datei mit explizitem Erfolgs-Handling."""
>     try:
>         datei = open(dateiname, 'r')
>     except FileNotFoundError:
>         print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
>     else:
>         # Dieser Block wird nur ausgeführt, wenn open() erfolgreich war
>         inhalt = datei.read()
>         print(f"Datei erfolgreich gelesen: {len(inhalt)} Zeichen")
>         datei.close()
> 
> datei_verarbeiten("test.txt")
> ```
> 
> **Vorteil**: Der `else`-Block signalisiert klar, dass dieser Code nur im Erfolgsfall ausgeführt wird. Es trennt die "normale" Logik von der Fehlerbehandlung.

### Die `finally`-Klausel

Die `finally`-Klausel wird **immer** ausgeführt, unabhängig davon, ob eine Exception aufgetreten ist oder nicht. Sie ist ideal für Aufräumarbeiten wie das Schließen von Dateien, Netzwerkverbindungen oder das Freigeben von Ressourcen.

> [!NOTE]
> **`finally`-Klausel**: Ein optionaler Block, der **garantiert** ausgeführt wird, egal ob eine Exception auftrat oder nicht. Selbst wenn ein `return`-Statement im `try` oder `except` steht, wird `finally` vorher ausgeführt.
> 
> **Syntax**:
> ```python
> try:
>     code()
> except ExceptionType:
>     fehlerbehandlung()
> finally:
>     aufraeumen()  # Wird IMMER ausgeführt
> ```

> [!TIP]
> ```python
> def datei_sicher_lesen(dateiname):
>     """Liest eine Datei und stellt sicher, dass sie geschlossen wird."""
>     datei = None
>     try:
>         datei = open(dateiname, 'r')
>         inhalt = datei.read()
>         return inhalt
>     except FileNotFoundError:
>         print("Datei nicht gefunden.")
>         return None
>     finally:
>         # Wird immer ausgeführt, auch wenn return im try steht
>         if datei:
>             datei.close()
>             print("Datei wurde geschlossen.")
> 
> ergebnis = datei_sicher_lesen("daten.txt")
> ```
> 
> **Hinweis**: In modernem Python sollte man für Dateien das `with`-Statement verwenden, das automatisch aufräumt. `finally` ist aber universell für andere Ressourcen nützlich.

### Vollständige `try-except-else-finally`-Struktur

Die vollständige Struktur kombiniert alle Elemente:

> [!TIP]
> ```python
> def sichere_division(a, b):
>     """Führt eine Division mit vollständiger Fehlerbehandlung durch."""
>     print("Starte Division...")
>     try:
>         ergebnis = a / b
>     except ZeroDivisionError:
>         print("Fehler: Division durch Null!")
>         return None
>     except TypeError:
>         print("Fehler: Ungültige Datentypen!")
>         return None
>     else:
>         print(f"Division erfolgreich: {a} / {b} = {ergebnis}")
>         return ergebnis
>     finally:
>         print("Division-Operation beendet.")
> 
> # Tests:
> print(sichere_division(10, 2))
> # Output:
> # Starte Division...
> # Division erfolgreich: 10 / 2 = 5.0
> # Division-Operation beendet.
> # 5.0
> 
> print(sichere_division(10, 0))
> # Output:
> # Starte Division...
> # Fehler: Division durch Null!
> # Division-Operation beendet.
> # None
> ```

### Eigene Exceptions werfen mit `raise`

Python ermöglicht es, Exceptions explizit zu werfen, um Fehlerzustände im eigenen Code zu signalisieren.

> [!NOTE]
> **`raise`-Statement**: Wirft eine Exception, unterbricht den aktuellen Code-Fluss und löst die Fehlerbehandlung aus.
> 
> **Syntax**:
> ```python
> raise ExceptionType("Fehlermeldung")
> ```

> [!TIP]
> ```python
> def setze_alter(alter):
>     """Setzt das Alter, wirft ValueError bei ungültiger Eingabe."""
>     if not isinstance(alter, int):
>         raise TypeError("Alter muss eine Ganzzahl sein!")
>     if alter < 0:
>         raise ValueError("Alter kann nicht negativ sein!")
>     if alter > 150:
>         raise ValueError("Alter ist unrealistisch hoch!")
>     
>     print(f"Alter gesetzt: {alter}")
>     return alter
> 
> # Anwendung:
> try:
>     setze_alter(25)       # OK
>     setze_alter(-5)       # ValueError
> except ValueError as e:
>     print(f"Ungültiges Alter: {e}")
> ```
> 
> **Output**:
> ```
> Alter gesetzt: 25
> Ungültiges Alter: Alter kann nicht negativ sein!
> ```

#### Exception Re-Raise

Manchmal möchte man eine Exception abfangen, partiell behandeln und dann erneut werfen:

> [!TIP]
> ```python
> def verarbeite_daten(datei):
>     """Verarbeitet Daten, loggt Fehler, aber wirft sie erneut."""
>     try:
>         inhalt = open(datei).read()
>         return inhalt
>     except FileNotFoundError as e:
>         print(f"LOG: Datei {datei} nicht gefunden.")
>         raise  # Wirft die Exception erneut
> 
> try:
>     verarbeite_daten("nicht_vorhanden.txt")
> except FileNotFoundError:
>     print("Höhere Ebene behandelt den Fehler.")
> ```
> 
> **Output**:
> ```
> LOG: Datei nicht_vorhanden.txt nicht gefunden.
> Höhere Ebene behandelt den Fehler.
> ```

### Benutzerdefinierte Exceptions

Für komplexere Anwendungen ist es oft sinnvoll, eigene Exception-Typen zu definieren. Dies verbessert die Lesbarkeit und ermöglicht präzise Fehlerbehandlung.

> [!NOTE]
> **Benutzerdefinierte Exception**: Eine eigene Exception-Klasse, die von `Exception` oder einem anderen Exception-Typ erbt. Sie kann zusätzliche Attribute und Methoden enthalten.
> 
> **Syntax**:
> ```python
> class MeinFehler(Exception):
>     """Beschreibung des Fehlers."""
>     pass
> ```

> [!TIP]
> ```python
> class UngueltigeEmailError(Exception):
>     """Exception für ungültige E-Mail-Adressen."""
>     def __init__(self, email, nachricht="E-Mail-Format ungültig"):
>         self.email = email
>         self.nachricht = nachricht
>         super().__init__(f"{nachricht}: {email}")
> 
> def validiere_email(email):
>     """Validiert eine E-Mail-Adresse (vereinfacht)."""
>     if "@" not in email or "." not in email:
>         raise UngueltigeEmailError(email)
>     return True
> 
> # Anwendung:
> try:
>     validiere_email("benutzer@example.com")  # OK
>     validiere_email("ungueltig")             # UngueltigeEmailError
> except UngueltigeEmailError as e:
>     print(f"Fehler: {e}")
>     print(f"Problematische E-Mail: {e.email}")
> ```
> 
> **Output**:
> ```
> Fehler: E-Mail-Format ungültig: ungueltig
> Problematische E-Mail: ungueltig
> ```

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: Zu breite `except`-Klauseln**
> 
> **Problem**:
> ```python
> try:
>     code()
> except:
>     print("Ein Fehler ist aufgetreten.")
> ```
> 
> **Warum problematisch**: Fängt **alle** Exceptions ab, auch `KeyboardInterrupt` (Strg+C) und `SystemExit`. Verhindert kontrolliertes Beenden und erschwert Debugging.
> 
> **Lösung**: Verwende spezifische Exception-Typen oder mindestens `except Exception:`:
> ```python
> try:
>     code()
> except Exception as e:
>     print(f"Fehler: {e}")
> ```

> [!WARNING]
> **Fehler 2: Exceptions verschlucken**
> 
> **Problem**:
> ```python
> try:
>     kritischer_code()
> except ValueError:
>     pass  # Fehler wird ignoriert
> ```
> 
> **Warum problematisch**: Der Fehler wird komplett unterdrückt. Niemand erfährt, dass etwas schiefgelaufen ist.
> 
> **Lösung**: Mindestens loggen, oder den Benutzer informieren:
> ```python
> try:
>     kritischer_code()
> except ValueError as e:
>     print(f"Warnung: {e}")
>     # Oder: logging.error(f"Fehler: {e}")
> ```

> [!WARNING]
> **Fehler 3: Ausnahmen für Kontrollfluss missbrauchen**
> 
> **Problem**:
> ```python
> try:
>     wert = dictionary[key]
> except KeyError:
>     wert = default_wert
> ```
> 
> **Warum problematisch**: Exceptions sind für Ausnahmesituationen gedacht, nicht für normalen Kontrollfluss. Dies ist langsam und erschwert die Lesbarkeit.
> 
> **Lösung**: Nutze `.get()` bei Dictionaries:
> ```python
> wert = dictionary.get(key, default_wert)
> ```

### Zusammenfassung Python

Die Fehlerbehandlung in Python mit dem `try-except-else-finally`-Konstrukt ist ein mächtiges Werkzeug, um robuste und fehlertolerante Programme zu schreiben. Die wichtigsten Prinzipien sind:

1. **Spezifische Exceptions abfangen**: Verwende konkrete Exception-Typen, nicht blanket `except:`
2. **Fehler nicht verschlucken**: Informiere den Benutzer oder logge den Fehler
3. **`finally` für Aufräumarbeiten**: Garantiert Ausführung, ideal für Ressourcen-Freigabe
4. **`else` für Erfolgs-Logik**: Trennt normale Ausführung von Fehlerbehandlung
5. **Eigene Exceptions werfen**: Nutze `raise` für Validierung und Fehlersignalisierung
6. **Benutzerdefinierte Exceptions**: Verbessern Code-Klarheit bei komplexen Systemen

Mit diesen Werkzeugen können Programme elegant auf unerwartete Situationen reagieren, anstatt unkontrolliert abzustürzen.

### Neue Python-Funktionen/Methoden

In dieser Lektion wurden folgende Python-Konzepte **neu eingeführt**:

**Exception-Handling**:
- `try` – Markiert einen Block mit potenziell fehlerhaftem Code
- `except ExceptionType` – Fängt spezifische Exceptions ab
- `except ExceptionType as e` – Fängt Exception ab und bindet Objekt an Variable
- `except (Type1, Type2)` – Fängt mehrere Exception-Typen ab
- `else` (in try-except) – Wird ausgeführt, wenn keine Exception auftrat
- `finally` – Wird immer ausgeführt, auch bei Exceptions oder `return`
- `raise ExceptionType("message")` – Wirft eine Exception
- `raise` (ohne Argument) – Wirft die aktuell behandelte Exception erneut

**Vordefinierte Exception-Typen** (Auswahl):
- `ValueError` – Wert hat falschen Inhalt/Format
- `TypeError` – Operation auf falschen Datentyp angewendet
- `IndexError` – Index außerhalb des gültigen Bereichs
- `KeyError` – Dictionary-Schlüssel existiert nicht
- `FileNotFoundError` – Datei nicht gefunden
- `ZeroDivisionError` – Division durch Null
- `AttributeError` – Attribut existiert nicht
- `Exception` – Basisklasse für die meisten Exceptions

**Benutzerdefinierte Exceptions**:
- Eigene Exception-Klassen durch Vererbung von `Exception`

---

## Weiterführende Ressourcen

### Theorie

**Bücher und Tutorials**:
- "Introduction to Algorithms" (Cormen et al.) – Kapitel zu Bäumen und Hash-Tabellen
- "Data Structures and Algorithm Analysis" (Mark Allen Weiss) – Umfassende Darstellung von BST, Balancierung und Hashing
- [Visualgo](https://visualgo.net/) – Interaktive Visualisierung von Datenstrukturen und Algorithmen

**Wissenschaftliche Papers**:
- "A Method for the Construction of Minimum-Redundancy Codes" (Huffman, 1952) – Grundlage für Huffman-Bäume
- "Self-Adjusting Binary Search Trees" (Sleator & Tarjan, 1985) – Splay Trees

**Online-Ressourcen**:
- [GeeksforGeeks: Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
- [Brilliant.org: Hash Tables](https://brilliant.org/wiki/hash-tables/)

### Python

**Offizielle Dokumentation**:
- [Python Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

**Tutorials und Best Practices**:
- [Real Python: Python Exceptions](https://realpython.com/python-exceptions/)
- [PEP 8: Exception Handling](https://peps.python.org/pep-0008/#programming-recommendations)

**Video-Tutorials**:
- Corey Schafer: "Python Exception Handling - Try, Except, Else, Finally"
- [Python Official: Exception Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8)
