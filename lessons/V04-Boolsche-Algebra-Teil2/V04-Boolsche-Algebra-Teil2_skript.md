# V04: Boolsche Algebra & Logische Schaltungen – Teil 2

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Erweiterte logische Operatoren **XOR**, **NAND** und **NOR** verstehen und anwenden können
> - **De Morgan'sche Gesetze** zur Vereinfachung logischer Ausdrücke einsetzen
> - Komplexe logische Schaltungen wie **Halbaddierer** und **Volladdierer** analysieren und konstruieren
> - **Multiplexer** und **Demultiplexer** als fundamentale digitale Bausteine verstehen
> - Python-**Vergleichsoperatoren** (`==`, `!=`, `<`, `>`, `<=`, `>=`) sicher verwenden
> - Logische Operatoren in Python (`and`, `or`, `not`) zur Formulierung komplexer Bedingungen nutzen
> - **Kurzschlussauswertung** verstehen und gezielt einsetzen
> - Unterschied zwischen **Truthy** und **Falsy** Values in Python kennen

---

## Teil 1: Theorie - Boolsche Algebra & Logische Schaltungen – Teil 2

### Überblick

In der vorherigen Vorlesung haben wir die grundlegenden logischen Operatoren **AND**, **OR** und **NOT** kennengelernt. Diese Operatoren bilden das Fundament der digitalen Logik und ermöglichen es uns, einfache logische Entscheidungen zu treffen. In dieser Vorlesung erweitern wir unser Repertoire um leistungsfähigere Operatoren und lernen, wie diese in praktischen digitalen Schaltungen eingesetzt werden. Die **Boolsche Algebra** ist nicht nur theoretisches Fundament der Informatik, sondern bildet die Grundlage für jeden modernen Computer, jedes Smartphone und jede digitale Steuerung in Maschinen und Anlagen. Maschinenbau-Ingenieure begegnen digitaler Logik in Steuerungssystemen, Sensornetzwerken und der Automatisierungstechnik. Die in dieser Vorlesung gelernten Konzepte ermöglichen es, komplexe Steuerlogiken zu verstehen, zu analysieren und selbst zu entwerfen.

### Erweiterte Logische Operatoren

#### XOR – Exklusives ODER

Der **XOR-Operator** (gesprochen "Ex-Or", von "Exclusive OR") ist ein zweistelliger logischer Operator, der nur dann den Wert `1` (wahr) liefert, wenn genau einer der beiden Eingänge `1` ist, aber nicht beide gleichzeitig. Der XOR-Operator wird durch das Symbol ⊕ dargestellt und ist fundamental für viele digitale Schaltungen, insbesondere in der Arithmetik und Verschlüsselung.

> [!NOTE]
> **XOR (Exklusives ODER)**: Ein logischer Operator, der genau dann `1` liefert, wenn die Anzahl der Eingänge mit Wert `1` ungerade ist. Bei zwei Eingängen bedeutet dies: Genau einer ist `1`, der andere `0`.

Die **Wahrheitstabelle** für XOR (`A ⊕ B`) lautet:

| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 | 0     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

Eine wichtige Eigenschaft: XOR erkennt **Ungleichheit**. `A ⊕ B = 1` bedeutet `A ≠ B`.

> [!TIP]
> **Praktisches Beispiel – Lichtschalter-Schaltung**: Stellen Sie sich zwei Lichtschalter vor, die eine Lampe steuern (Wechselschaltung). Die Lampe soll leuchten, wenn genau ein Schalter gedrückt ist. Dies entspricht exakt einem XOR-Gatter: Schalter 1 = A, Schalter 2 = B, Lampe = A ⊕ B. Diese Schaltung findet sich in jedem Treppenhaus, wo man das Licht von oben oder unten an- und ausschalten kann.

**Mathematische Darstellung durch Grundoperatoren**: XOR lässt sich durch AND, OR und NOT ausdrücken:

$$
A \oplus B = (A \land \neg B) \lor (\neg A \land B)
$$

Dies bedeutet: XOR ist wahr, wenn (A ist wahr UND B ist falsch) ODER (A ist falsch UND B ist wahr).

**Wichtige XOR-Eigenschaften**:
- **Kommutativität**: $A \oplus B = B \oplus A$
- **Assoziativität**: $(A \oplus B) \oplus C = A \oplus (B \oplus C)$
- **Identitätselement**: $A \oplus 0 = A$ (XOR mit 0 lässt Wert unverändert)
- **Selbstinverse**: $A \oplus A = 0$ (XOR mit sich selbst ergibt 0)
- **Doppelte Negation**: $A \oplus B \oplus B = A$ (zweimal XOR mit B hebt sich auf)

Diese Eigenschaften machen XOR besonders nützlich für Verschlüsselung und Fehlerkorrektur.

#### NAND – Nicht-UND

Der **NAND-Operator** (von "NOT AND") ist die Negation des AND-Operators. NAND liefert nur dann `0`, wenn beide Eingänge `1` sind – in allen anderen Fällen liefert NAND den Wert `1`. NAND hat eine besondere Bedeutung in der digitalen Elektronik, da es **funktional vollständig** ist: Jede beliebige logische Funktion lässt sich ausschließlich durch NAND-Gatter realisieren.

> [!NOTE]
> **NAND (Nicht-UND)**: Ein logischer Operator, der die Negation von AND darstellt. Symbolisch: $A \uparrow B$ oder $\overline{A \land B}$. NAND ist funktional vollständig, das heißt, alle anderen logischen Operatoren (AND, OR, NOT, XOR) können ausschließlich durch NAND-Verknüpfungen konstruiert werden.

Die **Wahrheitstabelle** für NAND (`A ↑ B` oder `¬(A ∧ B)`):

| A | B | A ↑ B |
|---|---|-------|
| 0 | 0 | 1     |
| 0 | 1 | 1     |
| 1 | 0 | 1     |
| 1 | 1 | 0     |

> [!TIP]
> **Warum ist NAND so wichtig?** In der Halbleitertechnologie sind NAND-Gatter technisch einfacher und schneller zu realisieren als andere Gatter. Deshalb werden in der Praxis oft komplexe Schaltungen ausschließlich mit NAND-Gattern aufgebaut, auch wenn theoretisch andere Operatoren direkter wären. Dies reduziert die Produktionskosten und verbessert die Performance.

**Funktionale Vollständigkeit von NAND** – Konstruktion aller Grundoperatoren:

1. **NOT aus NAND**: $\neg A = A \uparrow A$ (beide Eingänge gleich)
2. **AND aus NAND**: $A \land B = \neg(A \uparrow B) = (A \uparrow B) \uparrow (A \uparrow B)$
3. **OR aus NAND**: $A \lor B = (\neg A) \uparrow (\neg B) = (A \uparrow A) \uparrow (B \uparrow B)$

Diese Eigenschaft macht NAND zum universellen Baustein digitaler Schaltungen.

#### NOR – Nicht-ODER

Der **NOR-Operator** (von "NOT OR") ist die Negation des OR-Operators. NOR liefert nur dann `1`, wenn beide Eingänge `0` sind – ansonsten liefert NOR den Wert `0`. NOR ist ebenso wie NAND **funktional vollständig**, das heißt, alle logischen Operationen lassen sich ausschließlich durch NOR-Gatter konstruieren.

> [!NOTE]
> **NOR (Nicht-ODER)**: Ein logischer Operator, der die Negation von OR darstellt. Symbolisch: $A \downarrow B$ oder $\overline{A \lor B}$. NOR ist funktional vollständig und wird oft in speziellen Schaltungsfamilien eingesetzt.

Die **Wahrheitstabelle** für NOR (`A ↓ B` oder `¬(A ∨ B)`):

| A | B | A ↓ B |
|---|---|-------|
| 0 | 0 | 1     |
| 0 | 1 | 0     |
| 1 | 0 | 0     |
| 1 | 1 | 0     |

**Funktionale Vollständigkeit von NOR** – Konstruktion aller Grundoperatoren:

1. **NOT aus NOR**: $\neg A = A \downarrow A$
2. **OR aus NOR**: $A \lor B = \neg(A \downarrow B) = (A \downarrow B) \downarrow (A \downarrow B)$
3. **AND aus NOR**: $A \land B = (\neg A) \downarrow (\neg B) = (A \downarrow A) \downarrow (B \downarrow B)$

> [!WARNING]
> **Verwechslungsgefahr**: Anfänger verwechseln oft NAND und NOR, weil beide "negierte" Operatoren sind. Merkhilfe: NAND ist das Gegenteil von AND (beide Eingänge müssen wahr sein für Falsch bei NAND), während NOR das Gegenteil von OR ist (mindestens ein Eingang muss wahr sein für Falsch bei NOR).

### De Morgan'sche Gesetze

Die **De Morgan'schen Gesetze** sind fundamentale Umformungsregeln der Boolschen Algebra, benannt nach dem britischen Mathematiker Augustus De Morgan (1806–1871). Diese Gesetze beschreiben, wie die Negation einer Konjunktion (UND) bzw. Disjunktion (ODER) in äquivalente Ausdrücke transformiert werden kann. Sie sind unverzichtbar für die Vereinfachung logischer Schaltungen und die Optimierung digitaler Designs.

> [!NOTE]
> **De Morgan'sche Gesetze**: Zwei fundamentale Äquivalenzregeln der Boolschen Algebra:
> 1. $\neg(A \land B) = \neg A \lor \neg B$ – Die Negation eines UND ist ein ODER der negierten Eingänge
> 2. $\neg(A \lor B) = \neg A \land \neg B$ – Die Negation eines ODER ist ein UND der negierten Eingänge

**Erstes De Morgan'sches Gesetz**:

$$
\neg(A \land B) = \neg A \lor \neg B
$$

Dies besagt: "Nicht (A und B)" ist äquivalent zu "(nicht A) oder (nicht B)". Anschaulich: Wenn nicht beide Bedingungen gleichzeitig erfüllt sind, dann ist mindestens eine Bedingung nicht erfüllt.

**Beweis durch Wahrheitstabelle**:

| A | B | A ∧ B | ¬(A ∧ B) | ¬A | ¬B | ¬A ∨ ¬B |
|---|---|-------|----------|----|----|---------|
| 0 | 0 | 0     | **1**    | 1  | 1  | **1**   |
| 0 | 1 | 0     | **1**    | 1  | 0  | **1**   |
| 1 | 0 | 0     | **1**    | 0  | 1  | **1**   |
| 1 | 1 | 1     | **0**    | 0  | 0  | **0**   |

Die Spalten für $\neg(A \land B)$ und $\neg A \lor \neg B$ sind identisch – die Ausdrücke sind äquivalent.

**Zweites De Morgan'sches Gesetz**:

$$
\neg(A \lor B) = \neg A \land \neg B
$$

Dies besagt: "Nicht (A oder B)" ist äquivalent zu "(nicht A) und (nicht B)". Anschaulich: Wenn keine der beiden Bedingungen erfüllt ist, dann sind beide Bedingungen nicht erfüllt.

**Beweis durch Wahrheitstabelle**:

| A | B | A ∨ B | ¬(A ∨ B) | ¬A | ¬B | ¬A ∧ ¬B |
|---|---|-------|----------|----|----|---------|
| 0 | 0 | 0     | **1**    | 1  | 1  | **1**   |
| 0 | 1 | 1     | **0**    | 1  | 0  | **0**   |
| 1 | 0 | 1     | **0**    | 0  | 1  | **0**   |
| 1 | 1 | 1     | **0**    | 0  | 0  | **0**   |

Auch hier sind die Spalten für $\neg(A \lor B)$ und $\neg A \land \neg B$ identisch.

> [!TIP]
> **Merkhilfe für De Morgan**: Beim Negieren einer Klammer werden aus UND-Verknüpfungen OR-Verknüpfungen (und umgekehrt), und jeder Operand wird einzeln negiert. Stellen Sie sich vor, Sie "verteilen" die Negation nach innen und "flippen" den Operator:
> - `¬(A AND B)` → `(¬A) OR (¬B)`
> - `¬(A OR B)` → `(¬A) AND (¬B)`

**Praktische Anwendung – Schaltungsvereinfachung**:

Die De Morgan'schen Gesetze erlauben es, komplexe logische Ausdrücke zu vereinfachen, was in der Praxis zu weniger Gattern und damit günstigeren, schnelleren und energieeffizienteren Schaltungen führt.

**Beispiel**: Vereinfache $\neg(A \land \neg B \land C)$

Anwendung des ersten De Morgan'schen Gesetzes:

$$
\neg(A \land \neg B \land C) = \neg A \lor \neg(\neg B) \lor \neg C = \neg A \lor B \lor \neg C
$$

Die ursprünglich komplexe dreifache UND-Verknüpfung mit Negation wird zu einer einfacheren ODER-Verknüpfung.

> [!WARNING]
> **Häufiger Fehler bei De Morgan**: Studierende vergessen oft, beim Anwenden von De Morgan auch die einzelnen Operanden zu negieren. Falsch wäre: $\neg(A \land B) = A \lor B$ (Negation fehlt auf A und B!). Richtig ist: $\neg(A \land B) = \neg A \lor \neg B$.

### Logische Schaltungen – Addierer

Digitale Computer arbeiten intern mit binären Zahlen, und die grundlegendste arithmetische Operation ist die Addition. **Addierer** sind logische Schaltungen, die binäre Zahlen addieren. Sie sind fundamentale Bausteine in der **Arithmetisch-Logischen Einheit (ALU)** eines jeden Prozessors. Wir betrachten zwei Arten von Addierern: den **Halbaddierer** (Half Adder) und den **Volladdierer** (Full Adder).

#### Halbaddierer (Half Adder)

Ein **Halbaddierer** addiert zwei einzelne Bits `A` und `B` und erzeugt zwei Ausgänge: die **Summe** `S` (engl. Sum) und den **Übertrag** `C` (engl. Carry). Der Halbaddierer berücksichtigt keinen Übertrag von einer vorherigen Addition, daher der Name "Halb"-Addierer.

> [!NOTE]
> **Halbaddierer (Half Adder)**: Eine digitale Schaltung, die zwei Bits addiert und eine Summe sowie einen Übertrag erzeugt. Der Halbaddierer hat zwei Eingänge (A, B) und zwei Ausgänge (Summe S, Übertrag C).

**Wahrheitstabelle des Halbaddierers**:

| A | B | **S** (Summe) | **C** (Übertrag) |
|---|---|---------------|------------------|
| 0 | 0 | 0             | 0                |
| 0 | 1 | 1             | 0                |
| 1 | 0 | 1             | 0                |
| 1 | 1 | 0             | 1                |

**Analyse der Ausgänge**:

- **Summe S**: Die Summe ist genau dann `1`, wenn genau ein Eingang `1` ist – dies entspricht der XOR-Funktion: $S = A \oplus B$
- **Übertrag C**: Ein Übertrag tritt nur auf, wenn beide Eingänge `1` sind – dies entspricht der AND-Funktion: $C = A \land B$

**Logische Gleichungen**:

$$
S = A \oplus B
$$

$$
C = A \land B
$$

**Schaltplan des Halbaddierers**:

```
Eingänge: A, B

       A ──┬───────────────┐
           │               │
           │           ┌───▼────┐
           │           │  XOR   │──── S (Summe)
           │           └───▲────┘
           │               │
       B ──┼───────────────┘
           │
           │           ┌───▼────┐
           └───────────│  AND   │──── C (Übertrag)
                       └───▲────┘
                           │
                       ────┘
```

> [!TIP]
> **Binäre Addition verstehen**: Bei der Addition von `1 + 1` im Binärsystem erhalten wir `10` (dezimal 2). Die niedrigste Stelle ist `0` (Summe S), und wir haben einen Übertrag `1` zur nächsthöheren Stelle (Carry C). Der Halbaddierer modelliert genau diese Operation für einzelne Bits.

**Beispiel – Rechnung mit dem Halbaddierer**:

Addition von `A = 1` und `B = 1`:
- Summe: $S = 1 \oplus 1 = 0$
- Übertrag: $C = 1 \land 1 = 1$
- Ergebnis: `10` (binär) = 2 (dezimal) ✓

#### Volladdierer (Full Adder)

Ein **Volladdierer** erweitert den Halbaddierer, indem er einen zusätzlichen Eingang für einen **Übertrag von einer vorherigen Stelle** (`Cin`, Carry-In) berücksichtigt. Der Volladdierer ist die Grundlage für die Addition mehrstelliger binärer Zahlen, da er Überträge zwischen den Stellen propagieren kann.

> [!NOTE]
> **Volladdierer (Full Adder)**: Eine digitale Schaltung, die drei Bits addiert (A, B und ein Übertrag Cin) und eine Summe (S) sowie einen neuen Übertrag (Cout) erzeugt. Der Volladdierer hat drei Eingänge (A, B, Cin) und zwei Ausgänge (S, Cout).

**Wahrheitstabelle des Volladdierers**:

| A | B | Cin | **S** (Summe) | **Cout** (Übertrag) |
|---|---|-----|---------------|---------------------|
| 0 | 0 | 0   | 0             | 0                   |
| 0 | 0 | 1   | 1             | 0                   |
| 0 | 1 | 0   | 1             | 0                   |
| 0 | 1 | 1   | 0             | 1                   |
| 1 | 0 | 0   | 1             | 0                   |
| 1 | 0 | 1   | 0             | 1                   |
| 1 | 1 | 0   | 0             | 1                   |
| 1 | 1 | 1   | 1             | 1                   |

**Analyse der Ausgänge**:

- **Summe S**: Die Summe ist `1`, wenn eine ungerade Anzahl der drei Eingänge `1` ist. Dies entspricht einer dreifachen XOR-Verknüpfung: $S = A \oplus B \oplus Cin$
- **Übertrag Cout**: Ein Übertrag tritt auf, wenn mindestens zwei der drei Eingänge `1` sind. Dies lässt sich durch folgende Formel ausdrücken: $Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin)$

**Logische Gleichungen**:

$$
S = A \oplus B \oplus Cin
$$

$$
Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin)
$$

Alternative kompaktere Form für Cout (unter Verwendung der XOR-Eigenschaft):

$$
Cout = (A \land B) \lor ((A \oplus B) \land Cin)
$$

**Konstruktion aus zwei Halbaddierern**:

Ein Volladdierer lässt sich elegant aus zwei Halbaddierern und einem OR-Gatter konstruieren:

1. **Erster Halbaddierer** addiert `A` und `B`:
   - Zwischensumme: $S_1 = A \oplus B$
   - Zwischenübertrag: $C_1 = A \land B$

2. **Zweiter Halbaddierer** addiert $S_1$ und `Cin`:
   - Endgültige Summe: $S = S_1 \oplus Cin = A \oplus B \oplus Cin$
   - Zweiter Zwischenübertrag: $C_2 = S_1 \land Cin$

3. **OR-Gatter** verknüpft die beiden Überträge:
   - Endgültiger Übertrag: $Cout = C_1 \lor C_2$

**Schaltplan des Volladdierers (aus Halbaddierern)**:

```
          A ─────┐
                 │
          B ─────┼─── Halbaddierer 1 ───┬─── S1
                 │                       │
                 └───────────────────────┼─── C1 ─┐
                                         │        │
          Cin ───────────────────────────┘        │
                 │                                 │
                 └─── Halbaddierer 2 ─── S (Summe)│
                                                   │
                                          C2 ──────┼─── OR ─── Cout
                                                   │
                                          ─────────┘
```

> [!TIP]
> **Ripple-Carry-Addierer**: Um mehrstellige Binärzahlen zu addieren (z.B. zwei 8-Bit-Zahlen), kettet man Volladdierer hintereinander. Der Übertrag (Cout) jeder Stelle wird zum Carry-In (Cin) der nächsthöheren Stelle. Diese Architektur heißt **Ripple-Carry-Addierer**, da der Übertrag sich von der niedrigsten zur höchsten Stelle "durchrippt". Nachteil: Bei breiten Zahlen (z.B. 64 Bit) ist dies langsam, da jede Stelle auf den Übertrag der vorherigen warten muss. Schnellere Designs (Carry-Lookahead-Adder) existieren für High-Performance-Prozessoren.

**Beispiel – 4-Bit-Addition**:

Addiere `1011` (binär, dezimal 11) und `0110` (binär, dezimal 6):

```
  Position:    3  2  1  0
  A:           1  0  1  1
+ B:           0  1  1  0
  Cin:      0  0  1  1  0  (Überträge)
─────────────────────────
  Summe:    1  0  0  0  1  = 10001 (binär) = 17 (dezimal) ✓
```

Schritt-für-Schritt:
- Stelle 0: A=1, B=0, Cin=0 → S=1, Cout=0
- Stelle 1: A=1, B=1, Cin=0 → S=0, Cout=1
- Stelle 2: A=0, B=1, Cin=1 → S=0, Cout=1
- Stelle 3: A=1, B=0, Cin=1 → S=0, Cout=1
- Stelle 4: Cout=1 (finaler Übertrag)

### Multiplexer und Demultiplexer

**Multiplexer** (MUX) und **Demultiplexer** (DEMUX) sind fundamentale digitale Bausteine zur Datenweiterleitung. Sie werden in nahezu jedem digitalen System eingesetzt, von Prozessoren über Kommunikationssysteme bis hin zu Speicherarchitekturen.

#### Multiplexer (MUX)

Ein **Multiplexer** ist eine digitale Schaltung, die aus mehreren Eingangssignalen ein einzelnes Ausgangssignal auswählt. Die Auswahl erfolgt über ein oder mehrere **Steuer-** oder **Select-Leitungen** (S). Ein Multiplexer funktioniert wie ein steuerbarer digitaler Schalter.

> [!NOTE]
> **Multiplexer (MUX)**: Eine Kombinationsschaltung, die aus $2^n$ Dateneingängen einen auswählt und zum Ausgang durchschaltet. Die Auswahl erfolgt über $n$ Select-Leitungen. Ein 2:1-MUX hat 2 Dateneingänge und 1 Select-Leitung, ein 4:1-MUX hat 4 Dateneingänge und 2 Select-Leitungen, usw.

**Beispiel: 2:1-Multiplexer** (2 Eingänge, 1 Select-Leitung):

Eingänge: `I0`, `I1` (Dateneingänge), `S` (Select)  
Ausgang: `Y`

**Wahrheitstabelle**:

| S | **Y** |
|---|-------|
| 0 | I0    |
| 1 | I1    |

Bedeutung: Wenn `S = 0`, wird `I0` zum Ausgang durchgeschaltet; wenn `S = 1`, wird `I1` durchgeschaltet.

**Logische Gleichung**:

$$
Y = (\neg S \land I0) \lor (S \land I1)
$$

Anschaulich: Der Ausgang ist `I0` UND (`S` ist 0) ODER `I1` UND (`S` ist 1).

**Schaltplan 2:1-MUX**:

```
  I0 ────┬───────────────┐
         │               │
         │           ┌───▼────┐
         │           │  AND   │─────┐
         │           └───▲────┘     │
         │               │          │
     ┌───┴────┐          │      ┌───▼────┐
  S ─│  NOT   │──────────┘      │   OR   │──── Y
     └───┬────┘                  └───▲────┘
         │                           │
  I1 ────┼───────────────┐           │
         │               │           │
         │           ┌───▼────┐      │
         │           │  AND   │──────┘
         │           └───▲────┘
         │               │
         └───────────────┘
```

**Beispiel: 4:1-Multiplexer** (4 Eingänge, 2 Select-Leitungen):

Eingänge: `I0`, `I1`, `I2`, `I3`, `S1`, `S0` (zwei Select-Leitungen)  
Ausgang: `Y`

**Wahrheitstabelle**:

| S1 | S0 | **Y** |
|----|----|----|
| 0  | 0  | I0 |
| 0  | 1  | I1 |
| 1  | 0  | I2 |
| 1  | 1  | I3 |

Mit zwei Select-Leitungen kann man $2^2 = 4$ verschiedene Eingänge auswählen.

**Logische Gleichung**:

$$
Y = (\neg S1 \land \neg S0 \land I0) \lor (\neg S1 \land S0 \land I1) \lor (S1 \land \neg S0 \land I2) \lor (S1 \land S0 \land I3)
$$

> [!TIP]
> **Anwendung von Multiplexern – CPU-Datenbus**: In einem Prozessor werden Multiplexer verwendet, um verschiedene Datenquellen (Register, Speicher, ALU-Ergebnis) auf einen gemeinsamen Bus zu schalten. Die CPU-Steuerung wählt über Select-Leitungen, welche Datenquelle gerade aktiv ist. Dies spart Leitungen und reduziert die Komplexität.

#### Demultiplexer (DEMUX)

Ein **Demultiplexer** ist das Gegenstück zum Multiplexer: Er nimmt ein einziges Eingangssignal und leitet es zu einem von mehreren Ausgängen weiter. Die Auswahl des Ausgangs erfolgt ebenfalls über Select-Leitungen.

> [!NOTE]
> **Demultiplexer (DEMUX)**: Eine Kombinationsschaltung, die ein Eingangssignal auf einen von $2^n$ Ausgängen verteilt. Die Auswahl erfolgt über $n$ Select-Leitungen. Ein 1:2-DEMUX hat 1 Dateneingang und 2 Ausgänge, ein 1:4-DEMUX hat 1 Dateneingang und 4 Ausgänge.

**Beispiel: 1:2-Demultiplexer**:

Eingang: `I` (Dateneingang), `S` (Select)  
Ausgänge: `Y0`, `Y1`

**Wahrheitstabelle**:

| S | **Y0** | **Y1** |
|---|--------|--------|
| 0 | I      | 0      |
| 1 | 0      | I      |

Bedeutung: Wenn `S = 0`, wird `I` auf `Y0` geleitet (und `Y1 = 0`); wenn `S = 1`, wird `I` auf `Y1` geleitet (und `Y0 = 0`).

**Logische Gleichungen**:

$$
Y0 = \neg S \land I
$$

$$
Y1 = S \land I
$$

**Schaltplan 1:2-DEMUX**:

```
          ┌─── NOT ───┐
      S ──┤            │
          └────────────┼───┐
                       │   │
                   ┌───▼───▼───┐
      I ───────────│   AND     │──── Y0
                   └───────────┘
                   
                   ┌───▼───────┐
      I ───────────│   AND     │──── Y1
                   └───────────┘
                       │
      S ───────────────┘
```

> [!TIP]
> **Anwendung von Demultiplexern – Adressdekodierung**: In Speichersystemen werden Demultiplexer zur Adressdekodierung verwendet. Eine Adresse (Select-Leitungen) aktiviert genau eine Speicherzelle (Ausgang). Dies ermöglicht den gezielten Zugriff auf einzelne Speicherstellen in einem großen Speicherarray.

> [!WARNING]
> **Verwechslungsgefahr MUX vs. DEMUX**: Anfänger verwechseln oft die Richtung:
> - **Multiplexer**: Viele Eingänge → Ein Ausgang (mehrere Quellen zu einer Senke)
> - **Demultiplexer**: Ein Eingang → Viele Ausgänge (eine Quelle zu mehreren Senken)
> 
> Merkhilfe: "Multi" deutet auf viele Eingänge hin, "De-Multi" auf das "Aufteilen" (De-multiplizieren) auf viele Ausgänge.

### Zusammenfassung Theorie

Die zentralen Konzepte dieser Vorlesung zusammengefasst:

1. **Erweiterte Operatoren**: XOR, NAND und NOR sind leistungsfähige logische Operatoren. XOR erkennt Ungleichheit, NAND und NOR sind funktional vollständig und bilden die Grundlage für praktische Schaltungsdesigns.

2. **De Morgan'sche Gesetze**: Die Negation von AND wird zu OR (und umgekehrt), wobei alle Operanden negiert werden. Diese Gesetze sind essentiell für die Vereinfachung und Optimierung logischer Schaltungen.

3. **Addierer**: Der Halbaddierer addiert zwei Bits, der Volladdierer drei Bits (unter Berücksichtigung eines Übertrags). Durch Kaskadierung von Volladdierern können mehrstellige Binärzahlen addiert werden – dies ist das Fundament jeder CPU-Arithmetik.

4. **Multiplexer und Demultiplexer**: MUX wählt einen von mehreren Eingängen aus, DEMUX verteilt einen Eingang auf mehrere Ausgänge. Beide sind fundamentale Bausteine für Datenweiterleitung und -steuerung in digitalen Systemen.

5. **Praktische Relevanz**: Alle behandelten Konzepte sind nicht nur theoretische Konstrukte, sondern werden in realen Computern, Steuerungssystemen und digitalen Schaltungen täglich milliardenfach eingesetzt.

---

## Teil 2: Python-Praxis - Logische Ausdrücke (Boolsche Algebra)

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte! Die Grundlagen zu `bool`, `True`, `False` wurden bereits in V03 eingeführt. In dieser Vorlesung vertiefen wir die praktische Anwendung logischer Ausdrücke.

### Überblick

Nachdem wir in der Theorie erweiterte logische Operatoren und Schaltungen kennengelernt haben, wenden wir uns nun der praktischen Umsetzung logischer Ausdrücke in Python zu. Die **Vergleichsoperatoren** und **logischen Operatoren** in Python entsprechen direkt den Konzepten der Boolschen Algebra. Sie ermöglichen es uns, Bedingungen zu formulieren, Entscheidungen zu treffen und komplexe logische Zusammenhänge auszudrücken. Diese Konzepte bilden die Grundlage für Verzweigungen (die wir in V05 ausführlich behandeln) und sind essentiell für jedes nicht-triviale Python-Programm. Maschinenbau-Ingenieure nutzen diese Operatoren zur Formulierung von Steuerungsbedingungen, zur Validierung von Sensordaten und zur Implementierung von Sicherheitslogik in automatisierten Systemen.

### Vergleichsoperatoren

Python bietet sechs fundamentale **Vergleichsoperatoren**, die zwei Werte miteinander vergleichen und einen Boolean-Wert (`True` oder `False`) zurückgeben. Diese Operatoren funktionieren nicht nur mit Zahlen, sondern auch mit Strings, Listen und anderen Datentypen.

> [!NOTE]
> **Vergleichsoperatoren**: Operatoren, die zwei Werte miteinander vergleichen und einen Boolean-Wert zurückgeben. Python bietet sechs Vergleichsoperatoren: `==` (gleich), `!=` (ungleich), `<` (kleiner), `>` (größer), `<=` (kleiner-gleich), `>=` (größer-gleich).

#### Gleichheit und Ungleichheit

- **`==` (Gleichheit)**: Prüft, ob zwei Werte **gleich** sind
- **`!=` (Ungleichheit)**: Prüft, ob zwei Werte **unterschiedlich** sind

> [!TIP]
> ```python
> # Gleichheit testen
> x = 5
> y = 5
> z = 10
> 
> print(x == y)  # True – beide haben denselben Wert
> print(x == z)  # False – unterschiedliche Werte
> print(x != z)  # True – sie sind ungleich
> 
> # Funktioniert auch mit Strings
> name1 = "Python"
> name2 = "Python"
> name3 = "python"  # Kleinschreibung!
> 
> print(name1 == name2)  # True – identische Strings
> print(name1 == name3)  # False – Groß-/Kleinschreibung zählt!
> print(name1 != name3)  # True – sie sind unterschiedlich
> ```

> [!WARNING]
> **Häufiger Fehler: `==` vs. `=`**
> 
> Anfänger verwechseln oft den Zuweisungsoperator `=` mit dem Vergleichsoperator `==`:
> - `x = 5` → **Zuweisung**: Variable `x` bekommt den Wert 5
> - `x == 5` → **Vergleich**: Prüft, ob `x` den Wert 5 hat
> 
> ```python
> # Falsch (führt zu SyntaxError in Bedingungen):
> if x = 5:  # SyntaxError: invalid syntax
>     pass
> 
> # Richtig:
> if x == 5:
>     pass
> ```

#### Größer, Kleiner und ihre Varianten

- **`<` (Kleiner als)**: Prüft, ob linker Wert **kleiner** als rechter ist
- **`>` (Größer als)**: Prüft, ob linker Wert **größer** als rechter ist
- **`<=` (Kleiner oder gleich)**: Prüft, ob linker Wert **kleiner oder gleich** rechter ist
- **`>=` (Größer oder gleich)**: Prüft, ob linker Wert **größer oder gleich** rechter ist

> [!TIP]
> ```python
> # Zahlenvergleiche
> alter = 25
> 
> print(alter < 30)   # True
> print(alter > 20)   # True
> print(alter <= 25)  # True (gleich ist inkludiert!)
> print(alter >= 26)  # False
> 
> # String-Vergleiche (lexikographisch)
> print("Apple" < "Banana")  # True – A kommt vor B im Alphabet
> print("abc" < "abd")       # True – c kommt vor d
> print("Python" < "python") # True – Großbuchstaben vor Kleinbuchstaben (ASCII)
> 
> # Float-Vergleiche
> temperatur = 20.5
> print(temperatur >= 20.0)  # True
> print(temperatur < 21.0)   # True
> ```

> [!WARNING]
> **Float-Vergleiche mit Vorsicht!**
> 
> Aufgrund von Rundungsfehlern bei Fließkommazahlen (siehe V02) sollte man Floats nicht direkt mit `==` vergleichen:
> 
> ```python
> # Problematisch:
> result = 0.1 + 0.2
> print(result == 0.3)  # False! (wegen Rundungsfehlern)
> print(result)         # 0.30000000000000004
> 
> # Richtig mit Toleranz (bereits in V03 eingeführt: abs()):
> tolerance = 1e-10
> print(abs(result - 0.3) < tolerance)  # True
> ```

### Logische Operatoren

Python bietet drei fundamentale **logische Operatoren**, die Boolean-Werte verknüpfen: `and`, `or` und `not`. Diese entsprechen den logischen Operatoren AND, OR und NOT aus der Boolschen Algebra.

> [!NOTE]
> **Logische Operatoren in Python**: Operatoren zur Verknüpfung von Boolean-Ausdrücken:
> - `and` – Logisches UND (beide müssen wahr sein)
> - `or` – Logisches ODER (mindestens einer muss wahr sein)
> - `not` – Logische Negation (kehrt Wahrheitswert um)

#### AND-Operator

Der **`and`-Operator** gibt `True` zurück, wenn **beide** Operanden `True` sind. Ansonsten gibt er `False` zurück.

> [!TIP]
> ```python
> # AND-Verknüpfungen
> a = True
> b = True
> c = False
> 
> print(a and b)  # True – beide sind wahr
> print(a and c)  # False – c ist falsch
> print(c and c)  # False – beide sind falsch
> 
> # Praktisches Beispiel – Bereichsprüfung
> alter = 25
> hat_fuehrerschein = True
> 
> # Darf Auto mieten? (18+ UND Führerschein)
> kann_auto_mieten = alter >= 18 and hat_fuehrerschein
> print(kann_auto_mieten)  # True
> 
> # Mehrfache Verknüpfung
> temperatur = 22
> luftfeuchtigkeit = 45
> 
> # Komfortzone: 20-25°C UND 40-60% Luftfeuchtigkeit
> ist_komfortabel = (20 <= temperatur <= 25) and (40 <= luftfeuchtigkeit <= 60)
> print(ist_komfortabel)  # True
> ```

#### OR-Operator

Der **`or`-Operator** gibt `True` zurück, wenn **mindestens einer** der Operanden `True` ist. Er gibt nur dann `False` zurück, wenn **alle** Operanden `False` sind.

> [!TIP]
> ```python
> # OR-Verknüpfungen
> a = True
> b = False
> c = False
> 
> print(a or b)  # True – a ist wahr
> print(b or c)  # False – beide sind falsch
> print(a or c)  # True – a ist wahr
> 
> # Praktisches Beispiel – Zutrittsberechtigung
> ist_admin = False
> ist_mitarbeiter = True
> ist_gast = False
> 
> # Hat Zugang? (Admin ODER Mitarbeiter ODER Gast)
> hat_zugang = ist_admin or ist_mitarbeiter or ist_gast
> print(hat_zugang)  # True
> 
> # Wochenende prüfen
> tag = "Samstag"
> ist_wochenende = (tag == "Samstag") or (tag == "Sonntag")
> print(ist_wochenende)  # True
> ```

#### NOT-Operator

Der **`not`-Operator** kehrt den Boolean-Wert um: `True` wird zu `False` und umgekehrt.

> [!TIP]
> ```python
> # NOT-Negation
> a = True
> b = False
> 
> print(not a)  # False – kehrt True um
> print(not b)  # True – kehrt False um
> 
> # Praktisches Beispiel – Fehlererkennung
> fehler_gefunden = False
> 
> if not fehler_gefunden:
>     print("Programm läuft fehlerfrei")
> # Ausgabe: Programm läuft fehlerfrei
> 
> # Doppelte Negation (hebt sich auf)
> x = True
> print(not not x)  # True – doppelte Negation
> 
> # Kombination mit anderen Operatoren
> ist_fertig = False
> ist_abgebrochen = False
> 
> noch_aktiv = not ist_fertig and not ist_abgebrochen
> print(noch_aktiv)  # True
> ```

### Verkettete Vergleiche (Chained Comparisons)

Python erlaubt als besonderes Feature **verkettete Vergleiche**, die mehrere Vergleichsoperatoren elegant kombinieren. Dies entspricht der mathematischen Notation und ist deutlich lesbarer als mehrfache `and`-Verknüpfungen.

> [!NOTE]
> **Verkettete Vergleiche (Chained Comparisons)**: Ein Python-spezifisches Feature, das mehrere Vergleiche ohne explizite `and`-Verknüpfung erlaubt. Syntax: `a < b < c` statt `a < b and b < c`. Python garantiert, dass der Mittelwert nur einmal ausgewertet wird.

> [!TIP]
> ```python
> # Klassische Bereichsprüfung mit and
> alter = 25
> if alter >= 18 and alter < 65:
>     print("Erwachsen, nicht Senior")
> 
> # Eleganter mit verketteten Vergleichen
> if 18 <= alter < 65:
>     print("Erwachsen, nicht Senior")
> # Ausgabe: Erwachsen, nicht Senior
> 
> # Weitere Beispiele
> x = 15
> 
> # Prüft: 0 < x <= 100
> if 0 < x <= 100:
>     print(f"{x} liegt im Bereich (0, 100]")
> # Ausgabe: 15 liegt im Bereich (0, 100]
> 
> # Prüft Gleichheit aller drei Variablen
> a = 5
> b = 5
> c = 5
> if a == b == c:
>     print("Alle drei sind gleich")
> # Ausgabe: Alle drei sind gleich
> 
> # Komplexere Kette
> temperatur = 22.5
> if 15 < temperatur < 25:
>     print("Angenehme Temperatur")
> # Ausgabe: Angenehme Temperatur
> ```

> [!WARNING]
> **Vorsicht bei ungewöhnlichen Ketten**
> 
> Verkettete Vergleiche funktionieren bei allen Vergleichsoperatoren, aber nicht alle Kombinationen ergeben semantisch Sinn:
> 
> ```python
> # Sinnvoll:
> x = 10
> if 5 < x < 15:  # x liegt zwischen 5 und 15
>     pass
> 
> # Syntaktisch korrekt, aber semantisch seltsam:
> if 5 < x > 3:  # x ist größer als 5 UND größer als 3 (redundant)
>     pass
> 
> # Mathematisch korrekt, aber unüblich in Code:
> if x < 15 > 10:  # x < 15 AND 15 > 10 (15 > 10 ist immer wahr!)
>     pass  # Entspricht einfach x < 15
> ```
> 
> Nutze verkettete Vergleiche für Bereichsprüfungen (`a < b < c`) und Gleichheitsprüfungen (`a == b == c`).

### Kurzschlussauswertung (Short-Circuit Evaluation)

Python nutzt **Kurzschlussauswertung** (auch Lazy Evaluation genannt) bei logischen Operatoren. Das bedeutet: Python wertet Ausdrücke von links nach rechts aus und stoppt, sobald das Endergebnis feststeht. Dies spart Performance und kann zur Fehlervermeidung genutzt werden.

> [!NOTE]
> **Kurzschlussauswertung (Short-Circuit Evaluation)**: Python wertet logische Ausdrücke von links nach rechts aus und stoppt, sobald das Gesamtergebnis feststeht:
> - Bei `and`: Wenn der linke Operand `False` ist, wird der rechte **nicht** ausgewertet
> - Bei `or`: Wenn der linke Operand `True` ist, wird der rechte **nicht** ausgewertet

#### Kurzschluss bei AND

Bei `a and b`: Wenn `a` bereits `False` ist, kann das Gesamtergebnis nur `False` sein – `b` wird nicht ausgewertet.

> [!TIP]
> ```python
> # Demonstration der Kurzschlussauswertung
> def teuer_check():
>     print("Teure Berechnung wird ausgeführt!")
>     return True
> 
> x = False
> 
> # Der rechte Teil wird NICHT ausgeführt
> result = x and teuer_check()
> print(result)  # False
> # Keine Ausgabe von "Teure Berechnung..."!
> 
> # Praktisches Beispiel – Division-durch-Null vermeiden
> x = 0
> y = 10
> 
> # Sicher: Prüft erst, ob x != 0, bevor dividiert wird
> if x != 0 and y / x > 5:
>     print("y/x ist größer als 5")
> else:
>     print("Division nicht möglich oder Bedingung nicht erfüllt")
> # Ausgabe: Division nicht möglich oder Bedingung nicht erfüllt
> # Kein ZeroDivisionError, weil y/x nicht ausgewertet wird!
> 
> # Ohne Kurzschlussauswertung würde das crashen:
> # if y / x > 5 and x != 0:  # ZeroDivisionError!
> ```

#### Kurzschluss bei OR

Bei `a or b`: Wenn `a` bereits `True` ist, kann das Gesamtergebnis nur `True` sein – `b` wird nicht ausgewertet.

> [!TIP]
> ```python
> # Demonstration der Kurzschlussauswertung bei OR
> def teuer_check():
>     print("Teure Berechnung wird ausgeführt!")
>     return False
> 
> x = True
> 
> # Der rechte Teil wird NICHT ausgeführt
> result = x or teuer_check()
> print(result)  # True
> # Keine Ausgabe von "Teure Berechnung..."!
> 
> # Praktisches Beispiel – Default-Werte
> benutzername = ""  # Leerer String
> 
> # Wenn benutzername leer, verwende "Gast"
> anzeigename = benutzername or "Gast"
> print(anzeigename)  # Gast
> 
> benutzername = "Alice"
> anzeigename = benutzername or "Gast"
> print(anzeigename)  # Alice
> ```

> [!WARNING]
> **Performance-Tipp: Reihenfolge bei AND**
> 
> Setze "billige" Checks vor "teure" Checks bei `and`:
> 
> ```python
> # Gut: Einfacher Check zuerst
> if benutzer_eingeloggt and komplexe_berechtigung_pruefen():
>     pass
> # Wenn benutzer_eingeloggt False ist, wird die teure Funktion nicht aufgerufen!
> 
> # Schlecht: Teure Operation zuerst
> if komplexe_berechtigung_pruefen() and benutzer_eingeloggt:
>     pass
> # Teure Funktion wird immer aufgerufen, auch wenn benutzer_eingeloggt False ist
> ```

### Operator-Präzedenz (Vorrangregeln)

Python wertet logische und Vergleichsoperatoren in einer festgelegten Reihenfolge aus. Die **Operator-Präzedenz** bestimmt, welche Operationen zuerst ausgeführt werden.

> [!NOTE]
> **Operator-Präzedenz**: Die Reihenfolge, in der Operatoren ausgewertet werden (von höchster zu niedrigster Priorität):
> 1. **Vergleichsoperatoren** (`==`, `!=`, `<`, `>`, `<=`, `>=`)
> 2. **`not`** (Negation)
> 3. **`and`** (Konjunktion)
> 4. **`or`** (Disjunktion)

> [!TIP]
> ```python
> # Beispiel 1: not hat höhere Priorität als and
> x = True
> y = False
> 
> result = not x and y
> # Wird interpretiert als: (not x) and y
> # = False and False
> # = False
> print(result)  # False
> 
> # Beispiel 2: and hat höhere Priorität als or
> a = True
> b = False
> c = True
> 
> result = a or b and c
> # Wird interpretiert als: a or (b and c)
> # = True or (False and True)
> # = True or False
> # = True
> print(result)  # True
> 
> # Beispiel 3: Vergleiche vor logischen Operatoren
> x = 5
> result = x > 3 and x < 10
> # Wird interpretiert als: (x > 3) and (x < 10)
> # = True and True
> # = True
> print(result)  # True
> ```

> [!WARNING]
> **Best Practice: Klammern für Lesbarkeit!**
> 
> Auch wenn Python klare Präzedenzregeln hat, verbessern Klammern die Lesbarkeit erheblich:
> 
> ```python
> # Funktioniert, aber schwer lesbar:
> result = x > 0 and y > 0 or z > 0
> 
> # Besser mit Klammern (auch für Code-Reviews):
> result = (x > 0 and y > 0) or (z > 0)
> ```

### Truthy und Falsy Values (Truth Value Testing)

Eine Besonderheit von Python: **Jeder Wert** kann in einem Boolean-Kontext als `True` oder `False` interpretiert werden. Man spricht von **truthy** (wird als `True` interpretiert) und **falsy** (wird als `False` interpretiert) Values.

> [!NOTE]
> **Truthy und Falsy Values**: In Python kann jedes Objekt in einem Boolean-Kontext ausgewertet werden:
> - **Falsy Values** (werden als `False` interpretiert): `False`, `None`, `0`, `0.0`, `""` (leerer String), `[]` (leere Liste), `()` (leeres Tupel), `{}` (leeres Dictionary), `set()` (leeres Set)
> - **Truthy Values** (werden als `True` interpretiert): Alle anderen Werte!

> [!TIP]
> ```python
> # Zahlen
> print(bool(0))      # False – Null ist falsy
> print(bool(0.0))    # False – Auch Fließkomma-Null
> print(bool(42))     # True – Alle anderen Zahlen sind truthy
> print(bool(-5))     # True – Auch negative Zahlen!
> 
> # Strings
> print(bool(""))     # False – Leerer String ist falsy
> print(bool("0"))    # True – String "0" ist truthy (nicht leer!)
> print(bool("Hallo")) # True – Nicht-leere Strings sind truthy
> 
> # None
> print(bool(None))   # False – None ist falsy
> 
> # Collections (werden in V08 behandelt, hier zur Demonstration)
> print(bool([]))     # False – Leere Liste ist falsy
> print(bool([1, 2])) # True – Nicht-leere Liste ist truthy
> print(bool({}))     # False – Leeres Dictionary ist falsy
> ```

**Praktische Anwendung – Kompakte Existenzprüfungen**:

> [!TIP]
> ```python
> # Liste auf Leerheit prüfen
> zahlen = []
> 
> # Unpythonisch (funktioniert, aber umständlich):
> if len(zahlen) > 0:
>     print("Liste enthält Elemente")
> else:
>     print("Liste ist leer")
> 
> # Pythonisch (idiomatisch):
> if zahlen:
>     print("Liste enthält Elemente")
> else:
>     print("Liste ist leer")
> # Ausgabe: Liste ist leer
> 
> # String auf Leerheit prüfen
> name = ""
> if not name:
>     print("Kein Name angegeben")
> # Ausgabe: Kein Name angegeben
> 
> # Default-Werte mit or
> eingabe = ""
> wert = eingabe or "Standard"
> print(wert)  # Standard (weil eingabe falsy ist)
> 
> eingabe = "Benutzer"
> wert = eingabe or "Standard"
> print(wert)  # Benutzer
> ```

> [!WARNING]
> **Vorsicht: `if x:` vs. `if x is not None:`**
> 
> Diese beiden Checks sind **nicht** identisch!
> 
> ```python
> # Fall 1: x ist 0
> x = 0
> 
> if x:  # False, weil 0 falsy ist
>     print("x hat einen Wert")
> else:
>     print("x ist falsy")
> # Ausgabe: x ist falsy
> 
> if x is not None:  # True, weil 0 != None
>     print("x ist nicht None")
> # Ausgabe: x ist nicht None
> 
> # Fall 2: x ist None
> x = None
> 
> if x:  # False
>     print("x hat einen Wert")
> 
> if x is not None:  # False
>     print("x ist nicht None")
> 
> # Fall 3: x ist leerer String
> x = ""
> 
> if x:  # False, weil "" falsy ist
>     print("x hat einen Wert")
> 
> if x is not None:  # True, weil "" != None
>     print("x ist nicht None")
> # Ausgabe: x ist nicht None
> ```
> 
> **Regel**: Nutze `if x:` für Leer-/Existenzprüfungen. Nutze `if x is not None:` wenn du explizit auf `None` testen willst.

### Komplexe Logische Ausdrücke

In der Praxis kombiniert man oft mehrere Vergleichs- und logische Operatoren zu komplexen Bedingungen. Hier sind Best Practices für lesbare und wartbare Ausdrücke.

> [!TIP]
> ```python
> # Beispiel 1: Passwortvalidierung
> passwort = "Sicher123!"
> 
> # Anforderungen prüfen
> hat_mindestlaenge = len(passwort) >= 8
> hat_ziffer = any(c.isdigit() for c in passwort)  # Vorschau auf V08, any() wurde in V04 erwähnt
> hat_grossbuchstaben = any(c.isupper() for c in passwort)
> 
> ist_gueltig = hat_mindestlaenge and hat_ziffer and hat_grossbuchstaben
> print(f"Passwort gültig: {ist_gueltig}")  # True
> 
> # Beispiel 2: Zugriffskontrolle mit mehreren Bedingungen
> ist_admin = False
> ist_moderator = True
> ist_autor = False
> beitrag_alter_tage = 3
> 
> # Darf bearbeiten, wenn: Admin ODER (Moderator UND Beitrag < 7 Tage) ODER (Autor UND Beitrag < 1 Tag)
> darf_bearbeiten = (
>     ist_admin or
>     (ist_moderator and beitrag_alter_tage < 7) or
>     (ist_autor and beitrag_alter_tage < 1)
> )
> print(f"Bearbeitungsrecht: {darf_bearbeiten}")  # True
> 
> # Beispiel 3: Sensorvalidierung
> temperatur = 85.0
> druck = 1.5
> vibration = 0.8
> 
> # Warnung, wenn Temperatur zu hoch ODER Druck zu niedrig ODER Vibration zu hoch
> temperatur_kritisch = temperatur > 80
> druck_kritisch = druck < 1.0
> vibration_kritisch = vibration > 1.0
> 
> warnung_ausgeben = temperatur_kritisch or druck_kritisch or vibration_kritisch
> 
> if warnung_ausgeben:
>     print("⚠️ Warnung: Kritische Betriebsbedingungen!")
>     if temperatur_kritisch:
>         print(f"  - Temperatur zu hoch: {temperatur}°C")
>     if druck_kritisch:
>         print(f"  - Druck zu niedrig: {druck} bar")
>     if vibration_kritisch:
>         print(f"  - Vibration zu hoch: {vibration} mm/s")
> # Ausgabe: ⚠️ Warnung: Kritische Betriebsbedingungen!
> #          - Temperatur zu hoch: 85.0°C
> ```

> [!WARNING]
> **Häufige Fehler bei komplexen Bedingungen**
> 
> **Fehler 1**: Mehrfachvergleich falsch formuliert
> ```python
> x = 5
> 
> # FALSCH (funktioniert nicht wie erwartet):
> if x == 3 or 4 or 5:
>     print("x ist 3, 4 oder 5")
> # Wird interpretiert als: if (x == 3) or (4) or (5)
> # (4) und (5) sind truthy, daher immer True!
> 
> # RICHTIG:
> if x == 3 or x == 4 or x == 5:
>     print("x ist 3, 4 oder 5")
> 
> # ALTERNATIV (eleganter, wird in V08 behandelt):
> if x in [3, 4, 5]:
>     print("x ist 3, 4 oder 5")
> ```
> 
> **Fehler 2**: De Morgan nicht korrekt angewendet
> ```python
> ist_wochenende = True
> ist_urlaub = False
> 
> # FALSCH (De Morgan falsch angewendet):
> muss_arbeiten = not (ist_wochenende or ist_urlaub)
> # Richtig negiert
> 
> # Wenn man manuell umformt:
> # not (A or B) = (not A) and (not B)
> muss_arbeiten = (not ist_wochenende) and (not ist_urlaub)
> 
> # ABER NICHT:
> # muss_arbeiten = not ist_wochenende or not ist_urlaub  # FALSCH!
> ```

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: `==` vs. `=` verwechseln**
> 
> **Problem**: Zuweisungsoperator statt Vergleichsoperator verwendet
> 
> ```python
> # Falsch:
> x = 5
> if x = 10:  # SyntaxError: invalid syntax
>     print("x ist 10")
> 
> # Richtig:
> if x == 10:
>     print("x ist 10")
> ```

> [!WARNING]
> **Fehler 2: Float-Vergleiche ohne Toleranz**
> 
> **Problem**: Direkter Vergleich von Floats schlägt wegen Rundungsfehlern fehl
> 
> ```python
> # Problematisch:
> result = 0.1 + 0.2
> if result == 0.3:  # False!
>     print("Gleich")
> 
> # Richtig mit Toleranz:
> if abs(result - 0.3) < 1e-10:
>     print("Gleich")
> ```

> [!WARNING]
> **Fehler 3: Truthy/Falsy missverstehen**
> 
> **Problem**: String "0" wird als truthy interpretiert (weil nicht leer!)
> 
> ```python
> eingabe = "0"
> 
> # Falsch (denkt, "0" ist falsy):
> if eingabe:
>     print("Eingabe vorhanden")  # Wird ausgeführt!
> # Ausgabe: Eingabe vorhanden (nicht wie erwartet!)
> 
> # Richtig (expliziter Check):
> if eingabe and eingabe != "0":
>     print("Gültige Eingabe")
> 
> # Oder für Zahlen:
> if int(eingabe) != 0:
>     print("Nicht Null")
> ```

> [!WARNING]
> **Fehler 4: Mehrfachvergleich mit `or` falsch**
> 
> **Problem**: `x == 1 or 2` funktioniert nicht wie erwartet
> 
> ```python
> x = 5
> 
> # Falsch:
> if x == 1 or 2:  # Immer True!
>     print("x ist 1 oder 2")
> # Wird interpretiert als: if (x == 1) or (2)
> # (2) ist truthy, also immer True!
> 
> # Richtig:
> if x == 1 or x == 2:
>     print("x ist 1 oder 2")
> ```

### Zusammenfassung Python

Die wichtigsten Python-Konzepte dieser Vorlesung:

1. **Vergleichsoperatoren** (`==`, `!=`, `<`, `>`, `<=`, `>=`) vergleichen Werte und liefern Boolean-Ergebnisse. Sie funktionieren mit Zahlen, Strings und vielen anderen Datentypen.

2. **Logische Operatoren** (`and`, `or`, `not`) verknüpfen Boolean-Ausdrücke nach den Regeln der Boolschen Algebra.

3. **Verkettete Vergleiche** sind ein Python-Feature, das elegante Bereichsprüfungen ermöglicht: `a < b < c`.

4. **Kurzschlussauswertung** spart Performance und verhindert Fehler, indem Ausdrücke nur so weit ausgewertet werden, wie nötig.

5. **Truthy/Falsy Values**: Jeder Python-Wert hat einen impliziten Boolean-Wert. Leere Collections, Null und `None` sind falsy, alles andere ist truthy.

6. **Operator-Präzedenz**: Vergleiche vor `not` vor `and` vor `or`. Klammern nutzen für Klarheit!

7. **Best Practices**: Floats mit Toleranz vergleichen, `isinstance()` für Typ-Checks, explizite Klammern für komplexe Ausdrücke.

### Neue Python-Funktionen/Methoden in dieser Vorlesung

Folgende Python-Konzepte wurden in V04 **neu eingeführt**:

#### Operatoren
- **Vergleichsoperatoren**: `==`, `!=`, `<`, `>`, `<=`, `>=` – Vergleichen Werte, liefern Boolean
- **Logische Operatoren**: `and`, `or`, `not` – Verknüpfen Boolean-Ausdrücke
- **Bitweiser XOR-Operator**: `^` – Für Integer (nur erwähnt als Theorie-Bezug)

#### Konzepte
- **Verkettete Vergleiche (Chained Comparisons)**: `a < b < c` (Python-spezifisch)
- **Kurzschlussauswertung (Short-Circuit Evaluation)**: Bei `and` und `or`
- **Operator-Präzedenz**: Reihenfolge der Auswertung von Operatoren
- **Truthy und Falsy Values**: Implizite Boolean-Interpretation aller Werte

#### Built-in Funktionen (erwähnt/vorschau)
- **`abs(x)`** (Built-in, bereits in V03 kurz erwähnt): Absolutbetrag für Float-Toleranzprüfungen
- **`any(iterable)`** (Built-in, Vorschau): Gibt `True` zurück, wenn mindestens ein Element truthy ist (wird in V08 ausführlich behandelt)

> [!NOTE]
> Die detaillierte Dokumentation aller neu eingeführten Konzepte findet sich in [../../python_topics.md](../../python_topics.md) unter der Sektion V04.

---

## Weiterführende Ressourcen

### Theorie
- **Wikipedia: Boolsche Algebra** – Umfassende Übersicht über Grundlagen und erweiterte Konzepte  
  [https://de.wikipedia.org/wiki/Boolesche_Algebra](https://de.wikipedia.org/wiki/Boolesche_Algebra)

- **Wikipedia: Addierer** – Detaillierte Erklärung von Halb- und Volladdierern  
  [https://de.wikipedia.org/wiki/Addierer](https://de.wikipedia.org/wiki/Addierer)

- **Nand2Tetris** – Kostenloses Projekt: Bau eines Computers von NAND-Gattern aufwärts  
  [https://www.nand2tetris.org/](https://www.nand2tetris.org/)

- **Digital Logic Design Tutorial** – Interaktive Tutorials zu logischen Schaltungen  
  [https://www.electronics-tutorials.ws/logic/](https://www.electronics-tutorials.ws/logic/)

### Python
- **Python Official Documentation: Comparisons** – Offizielle Dokumentation zu Vergleichsoperatoren  
  [https://docs.python.org/3/reference/expressions.html#comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)

- **Python Official Documentation: Boolean Operations** – Offizielle Dokumentation zu logischen Operatoren  
  [https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

- **Python Official Documentation: Truth Value Testing** – Truthy/Falsy Values  
  [https://docs.python.org/3/library/stdtypes.html#truth-value-testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

- **Real Python: Operators and Expressions in Python** – Tutorial zu allen Python-Operatoren  
  [https://realpython.com/python-operators-expressions/](https://realpython.com/python-operators-expressions/)

- **PEP 8: Style Guide for Python Code** – Empfehlungen für lesbare Python-Bedingungen  
  [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
