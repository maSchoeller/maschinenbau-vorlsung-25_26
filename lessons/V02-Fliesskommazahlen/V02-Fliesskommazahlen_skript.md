# V02: Fließkommazahlen

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Den IEEE 754 Standard für Fließkommazahlen verstehen und anwenden können
> - Die Darstellung von Fließkommazahlen im Binärsystem mit Vorzeichen, Exponent und Mantisse erklären können
> - Rundungsfehler und Genauigkeitsprobleme bei Fließkommaberechnungen erkennen und vermeiden
> - Spezielle Werte (NaN, Inf, -Inf) verstehen und korrekt handhaben
> - Best Practices beim Vergleichen von Fließkommazahlen anwenden können
> - Verschiedene Methoden der String-Formatierung in Python beherrschen (f-Strings, .format(), %-Operator)
> - Die erweiterten Parameter von `print()` nutzen können
> - Escape-Sequenzen und mehrzeilige Strings korrekt einsetzen
> - Daten in Dateien schreiben und aus Dateien lesen können

---

## Teil 1: Theorie - Fließkommazahlen

### Überblick

In der ersten Vorlesung haben wir uns mit ganzen Zahlen und dem binären Zahlensystem beschäftigt. Doch wie speichert ein Computer Zahlen mit Nachkommastellen wie 3.14159 oder 0.000001? Die naive Idee, einfach einen **Binärpunkt** zwischen zwei Binärzahlen zu setzen (analog zum Dezimalpunkt), funktioniert zwar theoretisch, ist aber in der Praxis ineffizient. Computer verwenden stattdessen **Fließkommazahlen** (englisch: floating-point numbers), bei denen die Position des Kommas variabel ist – daher der Name.

Die Darstellung von Fließkommazahlen folgt einem international standardisierten Format: dem **IEEE 754 Standard**. Dieser Standard definiert, wie reelle Zahlen im Binärsystem approximiert werden, welche Genauigkeit erreicht wird und wie spezielle Werte wie Unendlich oder "Not a Number" repräsentiert werden. Das Verständnis dieses Standards ist fundamental für jeden, der mit numerischen Berechnungen arbeitet – sei es in der Simulation, der Datenanalyse oder der Steuerungstechnik.

> [!NOTE]
> **Fließkommazahlen** sind eine Methode zur Darstellung reeller Zahlen in Computern, bei der die Position des Dezimalpunkts (bzw. Binärpunkts) variabel ist. Der Name "Fließkomma" (floating point) bezieht sich darauf, dass der Punkt in der Zahlendarstellung "schwimmt" und nicht an einer festen Position steht.

### Motivation: Warum nicht einfach ein festes Komma?

Stellen Sie sich vor, Sie möchten sowohl die Masse eines Elektrons (ca. 9.109 × 10⁻³¹ kg) als auch die Masse der Erde (ca. 5.972 × 10²⁴ kg) speichern. Mit einer **Festkommadarstellung**, bei der das Komma immer an derselben Stelle steht, müssten Sie entweder eine extrem hohe Anzahl von Bits verwenden oder auf Genauigkeit in einem der beiden Bereiche verzichten. Die Fließkommadarstellung löst dieses Problem elegant durch eine **wissenschaftliche Notation**, ähnlich der Exponentialschreibweise in der Mathematik.

### Wissenschaftliche Notation als Grundlage

Bevor wir zur Computerdarstellung kommen, betrachten wir die wissenschaftliche Notation im Dezimalsystem:

$$
\text{Zahl} = (-1)^s \times m \times 10^e
$$

Hierbei ist:
- $s$ das **Vorzeichen** (0 für positiv, 1 für negativ)
- $m$ die **Mantisse** (auch Signifikand genannt), eine Zahl zwischen 1.0 und 9.999...
- $e$ der **Exponent** (eine ganze Zahl)

Beispiel: Die Zahl -6500.0 wird dargestellt als $-6.5 \times 10^3$, also $s=1$, $m=6.5$, $e=3$.

> [!TIP]
> **Beispiele für wissenschaftliche Notation im Dezimalsystem**:
> - $123.45 = 1.2345 \times 10^2$
> - $0.00078 = 7.8 \times 10^{-4}$
> - $-5000000 = -5.0 \times 10^6$

### IEEE 754 Standard: Binäre Fließkommazahlen

Im Computer verwenden wir das **Binärsystem**, sodass die Formel lautet:

$$
\text{Zahl} = (-1)^s \times m \times 2^e
$$

Der **IEEE 754 Standard** definiert zwei gängige Formate:

#### Single Precision (32 Bit)

Die **Single Precision** (auch `float` genannt) verwendet 32 Bits:

- **1 Bit** für das Vorzeichen $s$
- **8 Bits** für den Exponenten $e$
- **23 Bits** für die Mantisse $m$

```
┌──┬──────────┬─────────────────────────┐
│ s│ Exponent │       Mantisse         │
│1 │    8     │          23            │
└──┴──────────┴─────────────────────────┘
```

#### Double Precision (64 Bit)

Die **Double Precision** (auch `double` genannt) verwendet 64 Bits und bietet höhere Genauigkeit:

- **1 Bit** für das Vorzeichen $s$
- **11 Bits** für den Exponenten $e$
- **52 Bits** für die Mantisse $m$

```
┌──┬─────────────┬───────────────────────────────┐
│ s│  Exponent   │         Mantisse             │
│1 │     11      │             52               │
└──┴─────────────┴───────────────────────────────┘
```

> [!NOTE]
> **Single Precision** bietet etwa 7 Dezimalstellen Genauigkeit und einen Wertebereich von ca. $10^{-38}$ bis $10^{38}$.  
> **Double Precision** bietet etwa 15-16 Dezimalstellen Genauigkeit und einen Wertebereich von ca. $10^{-308}$ bis $10^{308}$.

In Python entspricht der Datentyp `float` standardmäßig der **Double Precision** (64 Bit).

### Aufbau und Interpretation

#### Das Vorzeichenbit

Das **Vorzeichenbit** ist das einfachste Element:
- `0` bedeutet: Die Zahl ist positiv oder +0
- `1` bedeutet: Die Zahl ist negativ oder -0

> [!WARNING]
> Es gibt tatsächlich zwei verschiedene Null-Werte: `+0` und `-0`. Diese werden in den meisten Berechnungen gleich behandelt, können aber in Grenzfällen (z.B. bei Division) zu unterschiedlichen Ergebnissen führen.

#### Der Exponent (Bias-Darstellung)

Der Exponent wird **nicht** im Zweierkomplement gespeichert, sondern verwendet eine **Bias-Darstellung**. Dabei wird zu jedem Exponenten ein fester Wert (der Bias) addiert, um negative Exponenten darzustellen:

- **Single Precision**: Bias = 127
- **Double Precision**: Bias = 1023

Der tatsächliche Exponent berechnet sich als: $e_{\text{real}} = e_{\text{gespeichert}} - \text{Bias}$

**Beispiel (Single Precision)**:
- Gespeicherter Wert `10000010` (binär) = 130 (dezimal)
- Tatsächlicher Exponent = 130 - 127 = 3
- Die Zahl wird mit $2^3 = 8$ multipliziert

> [!TIP]
> **Warum Bias-Darstellung?**
> 
> Die Bias-Darstellung hat den Vorteil, dass sich Fließkommazahlen als Ganzzahlen interpretiert in derselben Reihenfolge befinden. Dies vereinfacht Vergleichsoperationen in Hardware erheblich.

#### Die Mantisse (Normalisierung)

Die Mantisse repräsentiert die signifikanten Stellen der Zahl. Um maximale Genauigkeit zu erreichen, wird die **normalisierte Darstellung** verwendet:

$$
m = 1.b_1b_2b_3\ldots b_{23}
$$

Das führende `1.` wird **nicht gespeichert** (implizites Bit), da es bei normalisierten Zahlen immer vorhanden ist. Dies gewinnt ein zusätzliches Bit an Genauigkeit!

**Beispiel**: Die Mantisse `11001000000000000000000` repräsentiert eigentlich:
$$
1.11001000000000000000000_2 = 1 + 2^{-1} + 2^{-2} + 2^{-5} = 1.78125
$$

### Vollständiges Beispiel: Darstellung von 12.375

Konvertieren wir die Dezimalzahl **12.375** in die IEEE 754 Single Precision Darstellung:

#### Schritt 1: Vorzeichen bestimmen
12.375 ist positiv → $s = 0$

#### Schritt 2: Binärdarstellung
Ganzzahlteil: $12_{10} = 1100_2$  
Nachkommateil: $0.375_{10} = 0.011_2$ (da $0.375 = \frac{3}{8} = \frac{1}{4} + \frac{1}{8} = 2^{-2} + 2^{-3}$)  
Zusammen: $12.375_{10} = 1100.011_2$

#### Schritt 3: Normalisierung
Verschiebe den Binärpunkt so, dass genau eine 1 links davon steht:
$$
1100.011_2 = 1.100011_2 \times 2^3
$$

Hier ist der **Exponent** $e = 3$.

#### Schritt 4: Exponent mit Bias
Gespeicherter Exponent = $3 + 127 = 130 = 10000010_2$

#### Schritt 5: Mantisse (ohne führende 1)
Aus $1.100011$ wird nur $100011$ gespeichert, aufgefüllt mit Nullen:
$$
10001100000000000000000
$$

#### Ergebnis
```
Vorzeichen: 0
Exponent:   10000010
Mantisse:   10001100000000000000000

Komplette Darstellung (32 Bit):
0 10000010 10001100000000000000000
```

> [!TIP]
> **Interaktive Online-Tools**:
> 
> Um die IEEE 754 Darstellung zu visualisieren und zu experimentieren, gibt es hilfreiche Online-Konverter:
> - https://www.h-schmidt.net/FloatConverter/IEEE754.html
> - https://baseconvert.com/ieee-754-floating-point

### Rundungsfehler und Genauigkeitsprobleme

Ein fundamentales Problem von Fließkommazahlen ist, dass nicht alle Dezimalzahlen exakt darstellbar sind. Dies führt zu **Rundungsfehlern**.

#### Warum 0.1 + 0.2 ≠ 0.3

Das klassische Beispiel zeigt das Problem eindrucksvoll: Im Dezimalsystem ist $\frac{1}{3} = 0.333\ldots$ eine unendliche Dezimalzahl. Im Binärsystem haben viele dezimal "einfache" Brüche unendliche Binärdarstellungen:

$$
0.1_{10} = 0.0001100110011001100110011\ldots_2 \text{ (periodisch)}
$$

Da Computer nur endlich viele Bits speichern können, wird gerundet. Die Folge:

```
0.1 (gerundet) + 0.2 (gerundet) = 0.30000000000000004
```

> [!WARNING]
> **Niemals Fließkommazahlen mit `==` vergleichen!**
> 
> Aufgrund von Rundungsfehlern führt direkter Vergleich mit `==` oft zu unerwartetem Verhalten. Stattdessen sollte man prüfen, ob der Unterschied kleiner als eine Toleranzgrenze (Epsilon) ist.

#### Akkumulation von Rundungsfehlern

Bei wiederholten Berechnungen können sich Rundungsfehler aufaddieren:

```
Summe = 0
Für i = 1 bis 1.000.000:
    Summe = Summe + 0.1
    
Erwartetes Ergebnis: 100.000
Tatsächliches Ergebnis: ~99.999.999... oder ähnlich
```

> [!TIP]
> **Best Practices gegen Rundungsfehler**:
> - Wenn möglich, mit ganzen Zahlen rechnen und erst am Ende dividieren
> - Bei Geldbeträgen: Rechnen in Cent (Ganzzahlen) statt Euro (Fließkomma)
> - Verwenden Sie spezielle Bibliotheken wie `decimal` für höhere Genauigkeit bei kritischen Anwendungen

### Spezielle Werte

Der IEEE 754 Standard definiert mehrere spezielle Werte für außergewöhnliche Situationen:

#### Positive und negative Unendlichkeit (±Inf)

**Infinity** tritt auf bei:
- Division durch Null: $\frac{5.0}{0.0} = +\infty$
- Überlauf bei Berechnungen: $10^{400} = +\infty$ (außerhalb des Wertebereichs)

Darstellung:
- Exponent: alle Bits auf 1
- Mantisse: alle Bits auf 0
- Vorzeichen bestimmt $+\infty$ oder $-\infty$

```
+Inf: 0 11111111 00000000000000000000000  (Single Precision)
-Inf: 1 11111111 00000000000000000000000
```

> [!NOTE]
> **Unendlichkeit (Infinity, Inf)** ist ein spezieller Fließkommawert, der Zahlen repräsentiert, die den maximalen darstellbaren Wertebereich überschreiten. Es gibt positive und negative Unendlichkeit.

#### Not a Number (NaN)

**NaN** (Not a Number) signalisiert ein ungültiges oder undefiniertes Ergebnis:
- $\frac{0}{0}$
- $\infty - \infty$
- $\sqrt{-1}$ (ohne komplexe Zahlen)

Darstellung:
- Exponent: alle Bits auf 1
- Mantisse: **mindestens ein Bit** auf 1 (beliebige Kombination)

```
NaN: 0 11111111 10000000000000000000000  (ein mögliches NaN)
```

> [!NOTE]
> **NaN (Not a Number)** ist ein spezieller Fließkommawert, der signalisiert, dass das Ergebnis einer Operation mathematisch undefiniert oder nicht darstellbar ist.

> [!WARNING]
> **NaN ist nie gleich zu irgendetwas – auch nicht zu sich selbst!**
> 
> `NaN == NaN` ergibt `False`! Um auf NaN zu testen, muss eine spezielle Funktion verwendet werden (z.B. `math.isnan()` in Python).

#### Null

Es gibt **zwei verschiedene Nullen**: `+0` und `-0`. Beide verhalten sich in den meisten Operationen identisch, können aber unterschiedliche Vorzeichen für das Ergebnis produzieren:

```
1.0 / (+0) = +Inf
1.0 / (-0) = -Inf
```

### Best Practices beim Vergleichen von Fließkommazahlen

Aufgrund von Rundungsfehlern sollten Fließkommazahlen niemals direkt mit `==` verglichen werden. Stattdessen wird geprüft, ob der **absolute Unterschied** kleiner als eine **Toleranzgrenze** (Epsilon, $\varepsilon$) ist:

$$
|a - b| < \varepsilon
$$

Typische Werte für $\varepsilon$:
- `1e-9` (0.000000001) für Double Precision bei "normalen" Zahlen
- `1e-6` (0.000001) für weniger kritische Anwendungen

> [!TIP]
> **Fließkomma-Vergleich in Pseudocode**:
> ```
> FUNKTION fast_gleich(a, b, epsilon=1e-9):
>     RÜCKGABE abs(a - b) < epsilon
> ```

Für sehr große oder sehr kleine Zahlen sollte zusätzlich ein **relativer Vergleich** durchgeführt werden:

$$
\frac{|a - b|}{\max(|a|, |b|)} < \varepsilon
$$

Dies stellt sicher, dass der Vergleich sowohl für kleine Zahlen ($10^{-10}$) als auch für große Zahlen ($10^{10}$) funktioniert.

### Zusammenfassung Theorie

Die wichtigsten Erkenntnisse über Fließkommazahlen:

1. **IEEE 754** ist der Industriestandard für die binäre Darstellung von Fließkommazahlen mit Vorzeichen, Exponent (Bias-Darstellung) und Mantisse (normalisiert mit implizitem führenden Bit).

2. **Rundungsfehler** sind unvermeidlich, da nicht alle Dezimalzahlen im Binärsystem exakt darstellbar sind. Dies gilt besonders für dezimal "einfache" Brüche wie 0.1, 0.2, 0.3.

3. **Spezielle Werte** wie $\pm\infty$ und NaN ermöglichen die Repräsentation von Überlauf, Unterlauf und undefinierten Operationen ohne Programmabsturz.

4. **Vergleiche** zwischen Fließkommazahlen sollten nie mit `==` durchgeführt werden, sondern immer mit einer Toleranzgrenze (Epsilon-Vergleich).

5. **Single Precision** (32 Bit) bietet ca. 7 Dezimalstellen, **Double Precision** (64 Bit) ca. 15-16 Dezimalstellen Genauigkeit. Für die meisten Anwendungen ist Double Precision ausreichend und der Standard in Python.

---

## Teil 2: Python-Praxis - Eingaben/Ausgaben & Formatierung

> [!WARNING]
> **Python-Konsistenz beachten**: Prüfe [../../python_topics.md](../../python_topics.md) für bereits eingeführte Konzepte!

### Überblick

In der ersten Vorlesung haben wir die grundlegende Verwendung von `print()` und `input()` kennengelernt. In dieser Lektion vertiefen wir die Möglichkeiten der **Ein- und Ausgabe** erheblich. Wir lernen verschiedene Methoden zur **String-Formatierung**, die es ermöglichen, Zahlen, Variablen und Text elegant und präzise zu formatieren. Dies ist besonders wichtig beim Arbeiten mit Fließkommazahlen, da wir oft die Anzahl der Dezimalstellen kontrollieren oder Zahlen in wissenschaftlicher Notation darstellen möchten.

Zusätzlich erkunden wir die erweiterten Parameter von `print()`, die Verwendung von **Escape-Sequenzen** für Spezialzeichen und die grundlegende **Datei-Ein- und Ausgabe**, um Programme zu erstellen, die persistente Daten speichern und lesen können.

### String-Formatierung: Drei Methoden im Vergleich

Python bietet mehrere Methoden zur String-Formatierung. Wir behandeln die drei wichtigsten: **f-Strings** (modern und empfohlen), die **`.format()`-Methode** (flexibel und weit verbreitet) und den **%-Operator** (legacy, aber noch in altem Code zu finden).

#### f-Strings (Formatted String Literals) – Empfohlen!

**f-Strings** sind seit Python 3.6 verfügbar und die modernste, lesbarste Form der String-Formatierung. Sie werden durch ein `f` vor dem öffnenden Anführungszeichen gekennzeichnet und erlauben es, Variablen und Ausdrücke direkt in geschweiften Klammern `{}` einzubetten.

> [!NOTE]
> **f-Strings** (Formatted String Literals) sind eine moderne Methode zur String-Formatierung in Python, bei der Ausdrücke in geschweiften Klammern innerhalb eines Strings mit dem Präfix `f` direkt ausgewertet werden.

> [!TIP]
> **Grundlegende f-String Verwendung**:
> ```python
> name = "Ada"
> alter = 25
> print(f"Hallo, ich bin {name} und {alter} Jahre alt.")
> # Ausgabe: Hallo, ich bin Ada und 25 Jahre alt.
> ```

**Ausdrücke in f-Strings**: Innerhalb der geschweiften Klammern können beliebige Python-Ausdrücke stehen:

```python
x = 10
y = 20
print(f"Die Summe von {x} und {y} ist {x + y}.")
# Ausgabe: Die Summe von 10 und 20 ist 30.
```

**Zahlenformatierung in f-Strings**: Die eigentliche Stärke von f-Strings zeigt sich bei der Kontrolle über die Ausgabeformatierung. Nach der Variable bzw. dem Ausdruck folgt ein Doppelpunkt `:` und dann die **Formatspezifikation**.

##### Dezimalstellen bei Fließkommazahlen

```python
pi = 3.14159265359

# Auf 2 Dezimalstellen runden
print(f"Pi gerundet: {pi:.2f}")
# Ausgabe: Pi gerundet: 3.14

# Auf 4 Dezimalstellen
print(f"Pi präziser: {pi:.4f}")
# Ausgabe: Pi präziser: 3.1416
```

Die Syntax `:.2f` bedeutet:
- `:` leitet die Formatspezifikation ein
- `.2` gibt die Anzahl der Dezimalstellen an
- `f` steht für "fixed-point notation" (Festkommadarstellung)

> [!NOTE]
> **Formatspezifikation** ist der Teil nach dem Doppelpunkt in f-Strings oder `.format()`, der definiert, wie ein Wert dargestellt werden soll (z.B. Anzahl der Dezimalstellen, Breite, Ausrichtung).

##### Wissenschaftliche Notation

Für sehr große oder sehr kleine Zahlen ist die **wissenschaftliche Notation** (Exponentialschreibweise) praktisch:

```python
grosse_zahl = 123456789.123456
kleine_zahl = 0.000000123456

print(f"Große Zahl: {grosse_zahl:.3e}")
# Ausgabe: Große Zahl: 1.235e+08

print(f"Kleine Zahl: {kleine_zahl:.3e}")
# Ausgabe: Kleine Zahl: 1.235e-07
```

Die Syntax `:.3e` bedeutet:
- `.3` gibt die Anzahl der Dezimalstellen in der Mantisse an
- `e` steht für "exponential notation"

##### Breite und Ausrichtung

Oft möchte man Ausgaben in Spalten formatieren. Die Breite eines Feldes wird vor dem Dezimalpunkt angegeben:

```python
zahlen = [1.5, 12.75, 123.456, 0.001]

print("Rechtsbündig (Breite 10):")
for z in zahlen:
    print(f"{z:10.2f}")
# Ausgabe:
#       1.50
#      12.75
#     123.46
#       0.00

print("\nLinksbündig (Breite 10):")
for z in zahlen:
    print(f"{z:<10.2f}")
# Ausgabe:
# 1.50      
# 12.75     
# 123.46    
# 0.00      

print("\nZentriert (Breite 10):")
for z in zahlen:
    print(f"{z:^10.2f}")
# Ausgabe:
#   1.50    
#   12.75   
#  123.46   
#   0.00    
```

Die Syntax:
- `{z:10.2f}` – rechtsbündig (Standard für Zahlen), Breite 10
- `{z:<10.2f}` – linksbündig
- `{z:^10.2f}` – zentriert

##### Tausender-Trennzeichen

Für bessere Lesbarkeit großer Zahlen:

```python
million = 1000000
milliarde = 1000000000

print(f"Eine Million: {million:,}")
# Ausgabe: Eine Million: 1,000,000

print(f"Eine Milliarde: {milliarde:_}")
# Ausgabe: Eine Milliarde: 1_000_000_000
```

- `,` verwendet Komma als Tausender-Trennzeichen (US-amerikanisch)
- `_` verwendet Unterstrich als Tausender-Trennzeichen (Python-Style)

##### Prozentangaben

```python
anteil = 0.8642

print(f"Anteil: {anteil:.1%}")
# Ausgabe: Anteil: 86.4%

print(f"Anteil: {anteil:.2%}")
# Ausgabe: Anteil: 86.42%
```

Die Syntax `:.1%` multipliziert den Wert mit 100 und fügt ein Prozentzeichen hinzu, mit 1 Dezimalstelle.

> [!TIP]
> **f-String Formatierungs-Spickzettel**:
> 
> | Format | Bedeutung | Beispiel | Ausgabe |
> |--------|-----------|----------|---------|
> | `{x:.2f}` | 2 Dezimalstellen | `x = 3.14159` | `3.14` |
> | `{x:.3e}` | Exponentialnotation | `x = 1234.5` | `1.235e+03` |
> | `{x:10.2f}` | Breite 10, rechtsbündig | `x = 42.1` | `     42.10` |
> | `{x:<10.2f}` | Breite 10, linksbündig | `x = 42.1` | `42.10     ` |
> | `{x:^10.2f}` | Breite 10, zentriert | `x = 42.1` | `  42.10   ` |
> | `{x:,}` | Tausender-Trennung (Komma) | `x = 1000000` | `1,000,000` |
> | `{x:_}` | Tausender-Trennung (Unterstrich) | `x = 1000000` | `1_000_000` |
> | `{x:.1%}` | Prozent | `x = 0.8642` | `86.4%` |
> | `{x:+.2f}` | Mit Vorzeichen | `x = 42.1` | `+42.10` |
> | `{x:08.2f}` | Mit Nullen auffüllen | `x = 42.1` | `00042.10` |

#### Die `.format()`-Methode

Die **`.format()`-Methode** ist die Vorgänger-Technologie zu f-Strings, aber immer noch weit verbreitet und in manchen Situationen nützlich (z.B. wenn der Format-String wiederverwendet wird).

> [!NOTE]
> **Die `.format()`-Methode** ist eine String-Methode, die Platzhalter in geschweiften Klammern durch die als Argumente übergebenen Werte ersetzt.

**Grundlegende Verwendung**:

```python
name = "Ada"
alter = 25
nachricht = "Hallo, ich bin {} und {} Jahre alt.".format(name, alter)
print(nachricht)
# Ausgabe: Hallo, ich bin Ada und 25 Jahre alt.
```

**Mit Positionsangabe**:

```python
nachricht = "Hallo, ich bin {0} und {1} Jahre alt. {0} ist mein Name.".format("Ada", 25)
print(nachricht)
# Ausgabe: Hallo, ich bin Ada und 25 Jahre alt. Ada ist mein Name.
```

**Mit benannten Platzhaltern**:

```python
nachricht = "Hallo, ich bin {name} und {alter} Jahre alt.".format(name="Ada", alter=25)
print(nachricht)
# Ausgabe: Hallo, ich bin Ada und 25 Jahre alt.
```

**Formatierung wie bei f-Strings**:

```python
pi = 3.14159265359
print("Pi gerundet: {:.2f}".format(pi))
# Ausgabe: Pi gerundet: 3.14

print("Pi präziser: {:.4f}".format(pi))
# Ausgabe: Pi präziser: 3.1416
```

> [!WARNING]
> **f-Strings vs. `.format()`**:
> 
> f-Strings sind in den meisten Fällen vorzuziehen, da sie lesbarer und schneller sind. Verwenden Sie `.format()` nur, wenn Sie den Format-String mehrfach mit unterschiedlichen Werten verwenden möchten.

#### Der %-Operator (Legacy)

Der **%-Operator** ist die älteste Methode zur String-Formatierung in Python und stammt aus der C-Programmiersprache. Er wird heute nicht mehr empfohlen, ist aber in älterem Code häufig zu finden.

> [!NOTE]
> **Der %-Operator** ist eine veraltete Methode zur String-Formatierung, die Platzhalter wie `%s`, `%d`, `%f` verwendet und Werte aus einem Tupel einsetzt.

```python
name = "Ada"
alter = 25
print("Hallo, ich bin %s und %d Jahre alt." % (name, alter))
# Ausgabe: Hallo, ich bin Ada und 25 Jahre alt.
```

Wichtige Platzhalter:
- `%s` – String
- `%d` – Integer (decimal)
- `%f` – Float
- `%.2f` – Float mit 2 Dezimalstellen

```python
pi = 3.14159265359
print("Pi: %.2f" % pi)
# Ausgabe: Pi: 3.14
```

> [!WARNING]
> **Legacy-Methode – nicht empfohlen!**
> 
> Verwenden Sie den %-Operator nur, wenn Sie alten Code warten. Für neuen Code sind f-Strings die deutlich bessere Wahl.

### Erweiterte `print()`-Parameter

Die `print()`-Funktion akzeptiert mehrere optionale Parameter, die wir in V01 noch nicht behandelt haben.

#### Der `sep`-Parameter

Standardmäßig trennt `print()` mehrere Argumente durch ein Leerzeichen. Mit `sep` kann dies angepasst werden:

```python
print("A", "B", "C")
# Ausgabe: A B C

print("A", "B", "C", sep="-")
# Ausgabe: A-B-C

print("A", "B", "C", sep="")
# Ausgabe: ABC

print(2026, 1, 1, sep="/")
# Ausgabe: 2026/1/1
```

#### Der `end`-Parameter

Standardmäßig fügt `print()` am Ende einen Zeilenumbruch `\n` hinzu. Mit `end` kann dies geändert werden:

```python
print("Zeile 1")
print("Zeile 2")
# Ausgabe:
# Zeile 1
# Zeile 2

print("Zeile 1", end=" ")
print("Zeile 2")
# Ausgabe: Zeile 1 Zeile 2

print("Lade", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Fertig!")
# Ausgabe: Lade... Fertig!
```

Praktisches Beispiel – Fortschrittsbalken:

```python
import time

for i in range(10):
    print("#", end="", flush=True)
    time.sleep(0.2)
print(" Komplett!")
# Ausgabe (nach und nach): ########## Komplett!
```

#### Der `flush`-Parameter

Normalerweise werden Ausgaben **gepuffert** (buffered), d.h. sie werden erst geschrieben, wenn der Puffer voll ist oder ein Zeilenumbruch kommt. Mit `flush=True` wird die Ausgabe sofort geschrieben:

```python
print("Warte 5 Sekunden", end="", flush=True)
time.sleep(5)
print(" Fertig!")
```

Ohne `flush=True` würde "Warte 5 Sekunden" erst nach den 5 Sekunden erscheinen.

> [!TIP]
> **`print()`-Parameter kombinieren**:
> ```python
> print("Status", "OK", "2026", sep=" | ", end=" [DONE]\n")
> # Ausgabe: Status | OK | 2026 [DONE]
> ```

### Escape-Sequenzen und Spezialzeichen

**Escape-Sequenzen** beginnen mit einem Backslash `\` und repräsentieren Spezialzeichen, die nicht direkt getippt werden können oder besondere Bedeutung haben.

> [!NOTE]
> **Escape-Sequenzen** sind spezielle Zeichenkombinationen, die mit einem Backslash `\` beginnen und Spezialzeichen oder Steuerzeichen in Strings repräsentieren.

#### Die wichtigsten Escape-Sequenzen

| Escape-Sequenz | Bedeutung | Beispiel |
|----------------|-----------|----------|
| `\n` | Zeilenumbruch (Newline) | `"Zeile 1\nZeile 2"` |
| `\t` | Tabulator (Tab) | `"Name:\tAda"` |
| `\\` | Backslash selbst | `"Pfad: C:\\Users"` |
| `\'` | Einfaches Anführungszeichen | `'It\'s okay'` |
| `\"` | Doppeltes Anführungszeichen | `"Er sagte \"Hallo\""` |
| `\r` | Carriage Return (Wagenrücklauf) | `"Überschreibe\rText"` |
| `\b` | Backspace (Rückschritt) | `"abc\bd"` → `"abd"` |

> [!TIP]
> **Escape-Sequenzen in Aktion**:
> ```python
> print("Name:\tAlter:\tStadt:")
> print("Ada\t25\tBerlin")
> print("Bob\t30\tMünchen")
> # Ausgabe:
> # Name:	Alter:	Stadt:
> # Ada	25	Berlin
> # Bob	30	München
> 
> print("Zeile 1\nZeile 2\nZeile 3")
> # Ausgabe:
> # Zeile 1
> # Zeile 2
> # Zeile 3
> 
> print("Pfad: C:\\Users\\Ada\\Documents")
> # Ausgabe: Pfad: C:\Users\Ada\Documents
> ```

#### Raw Strings (r-Strings)

Wenn Sie viele Backslashes in einem String haben (z.B. bei Windows-Pfaden oder regulären Ausdrücken), können Sie **Raw Strings** verwenden, die durch ein `r` vor dem Anführungszeichen gekennzeichnet sind. In Raw Strings werden Escape-Sequenzen **nicht** interpretiert:

```python
# Ohne Raw String (umständlich)
pfad = "C:\\Users\\Ada\\Documents\\file.txt"
print(pfad)
# Ausgabe: C:\Users\Ada\Documents\file.txt

# Mit Raw String (einfacher)
pfad = r"C:\Users\Ada\Documents\file.txt"
print(pfad)
# Ausgabe: C:\Users\Ada\Documents\file.txt
```

> [!NOTE]
> **Raw Strings** sind Strings mit dem Präfix `r`, in denen Backslashes nicht als Escape-Zeichen interpretiert werden, sondern als literale Backslashes.

### Mehrzeilige Strings

Für längere Texte über mehrere Zeilen können **triple quotes** (dreifache Anführungszeichen) verwendet werden:

```python
text = """Dies ist ein
mehrzeiliger String.
Er kann über mehrere
Zeilen gehen."""

print(text)
# Ausgabe:
# Dies ist ein
# mehrzeiliger String.
# Er kann über mehrere
# Zeilen gehen.
```

Mehrzeilige Strings respektieren alle Zeilenumbrüche und Einrückungen:

```python
gedicht = """Rosen sind rot,
Veilchen sind blau,
Python ist toll,
und das weißt du genau!"""

print(gedicht)
```

> [!TIP]
> **Mehrzeilige f-Strings**:
> 
> f-Strings können auch mehrzeilig sein:
> ```python
> name = "Ada"
> alter = 25
> 
> info = f"""Name: {name}
> Alter: {alter}
> Status: Aktiv"""
> 
> print(info)
> # Ausgabe:
> # Name: Ada
> # Alter: 25
> # Status: Aktiv
> ```

### Dateien lesen und schreiben

Bisher haben wir nur mit der Konsole interagiert. Für persistente Datenspeicherung müssen wir **Dateien** verwenden.

#### Dateien schreiben

Mit der `open()`-Funktion öffnen wir eine Datei, schreiben mit der `.write()`-Methode und schließen mit `.close()`:

```python
# Datei im Schreibmodus öffnen
datei = open("beispiel.txt", "w")

# Text in Datei schreiben
datei.write("Hallo, dies ist die erste Zeile.\n")
datei.write("Und dies ist die zweite Zeile.\n")

# Datei schließen (wichtig!)
datei.close()
```

> [!NOTE]
> **`open(filename, mode)`** öffnet eine Datei. Der `mode` bestimmt, ob gelesen, geschrieben oder angehängt wird:
> - `"r"` – Read (Lesen, Standard)
> - `"w"` – Write (Schreiben, überschreibt existierende Datei)
> - `"a"` – Append (Anhängen, fügt am Ende hinzu)
> - `"r+"` – Read/Write (Lesen und Schreiben)

> [!WARNING]
> **Mode "w" überschreibt existierende Dateien!**
> 
> Wenn Sie `open("datei.txt", "w")` aufrufen und die Datei bereits existiert, wird ihr Inhalt **komplett gelöscht**. Verwenden Sie `"a"` (append), um am Ende anzuhängen.

#### Dateien lesen

```python
# Datei im Lesemodus öffnen
datei = open("beispiel.txt", "r")

# Gesamten Inhalt lesen
inhalt = datei.read()
print(inhalt)

# Datei schließen
datei.close()
```

**Zeile für Zeile lesen**:

```python
datei = open("beispiel.txt", "r")

for zeile in datei:
    print(zeile, end="")  # end="" vermeidet doppelte Zeilenumbrüche

datei.close()
```

**Alle Zeilen als Liste lesen**:

```python
datei = open("beispiel.txt", "r")

zeilen = datei.readlines()  # Gibt Liste von Strings zurück
print(zeilen)
# ['Hallo, dies ist die erste Zeile.\n', 'Und dies ist die zweite Zeile.\n']

datei.close()
```

#### Context Manager: `with`-Statement

Das manuelle Öffnen und Schließen von Dateien ist fehleranfällig (was passiert bei einem Fehler vor `.close()`?). Python bietet das **`with`-Statement**, das sicherstellt, dass die Datei automatisch geschlossen wird:

```python
# Schreiben mit context manager
with open("beispiel.txt", "w") as datei:
    datei.write("Diese Datei wird automatisch geschlossen.\n")
    datei.write("Auch bei Fehlern!\n")
# Datei ist hier automatisch geschlossen

# Lesen mit context manager
with open("beispiel.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)
# Datei ist hier automatisch geschlossen
```

> [!NOTE]
> **Das `with`-Statement** ist ein Kontext-Manager, der sicherstellt, dass Ressourcen (wie Dateien) korrekt freigegeben werden, auch wenn ein Fehler auftritt. Die Datei wird automatisch geschlossen, wenn der `with`-Block verlassen wird.

> [!TIP]
> **Best Practice: Immer `with` verwenden!**
> 
> Das `with`-Statement ist die empfohlene Methode zum Arbeiten mit Dateien:
> ```python
> # ✅ Gut: mit context manager
> with open("daten.txt", "r") as f:
>     daten = f.read()
> 
> # ❌ Schlecht: manuelles Öffnen/Schließen
> f = open("daten.txt", "r")
> daten = f.read()
> f.close()  # Wird bei Fehler möglicherweise nicht erreicht!
> ```

#### Praktisches Beispiel: Messdaten speichern

```python
# Messdaten generieren und in Datei speichern
with open("messdaten.txt", "w") as datei:
    datei.write("Zeit (s)\tTemperatur (°C)\n")
    datei.write("-" * 30 + "\n")
    
    for t in range(0, 11):
        temp = 20 + t * 0.5  # Simulierte Temperatur
        datei.write(f"{t}\t\t{temp:.1f}\n")

print("Messdaten gespeichert!")

# Messdaten wieder einlesen
with open("messdaten.txt", "r") as datei:
    print("\nInhalt der Datei:")
    print(datei.read())
```

> [!WARNING]
> **Dateipfade unter Windows**:
> 
> Unter Windows verwenden Pfade Backslashes `\`, die in Python Escape-Zeichen sind. Verwenden Sie entweder:
> - Raw Strings: `r"C:\Users\Ada\file.txt"`
> - Forward Slashes: `"C:/Users/Ada/file.txt"` (funktioniert auch unter Windows!)
> - Doppelte Backslashes: `"C:\\Users\\Ada\\file.txt"`

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1: Datei nicht geschlossen**
> 
> Problem: Datei wird mit `open()` geöffnet, aber nie mit `.close()` geschlossen. Dies kann zu Datenverlust führen.
> 
> **Lösung**: Verwenden Sie **immer** das `with`-Statement für automatisches Schließen.

> [!WARNING]
> **Fehler 2: Dezimalstellen bei `print()` statt in Format-String**
> 
> Problem:
> ```python
> pi = 3.14159
> print("Pi:", pi)  # Gibt alle Dezimalstellen aus
> ```
> 
> **Lösung**: Verwenden Sie f-Strings zur Kontrolle:
> ```python
> print(f"Pi: {pi:.2f}")  # Gibt 3.14 aus
> ```

> [!WARNING]
> **Fehler 3: Fehlende `\n` bei `.write()`**
> 
> Problem: `.write()` fügt **keine** automatischen Zeilenumbrüche hinzu (im Gegensatz zu `print()`).
> ```python
> datei.write("Zeile 1")
> datei.write("Zeile 2")
> # Ergebnis in Datei: "Zeile 1Zeile 2" (ohne Umbruch!)
> ```
> 
> **Lösung**: Manuell `\n` hinzufügen:
> ```python
> datei.write("Zeile 1\n")
> datei.write("Zeile 2\n")
> ```

> [!WARNING]
> **Fehler 4: Vergessener Mode-Parameter beim Anhängen**
> 
> Problem: Wollen an Datei anhängen, verwenden aber `"w"` statt `"a"` und löschen versehentlich alle Daten.
> 
> **Lösung**:
> ```python
> # Anhängen ohne Überschreiben
> with open("logfile.txt", "a") as datei:
>     datei.write("Neuer Eintrag\n")
> ```

### Zusammenfassung Python

Die wichtigsten Python-Konzepte dieser Lektion:

1. **f-Strings** sind die modernste und empfohlene Methode zur String-Formatierung. Sie ermöglichen direkte Einbettung von Variablen mit `f"{variable}"` und mächtige Formatierungsoptionen wie `{x:.2f}` für Dezimalstellen oder `{x:10.2f}` für Breite und Ausrichtung.

2. Die **`.format()`-Methode** ist eine flexible Alternative, die besonders nützlich ist, wenn der Format-String wiederverwendet wird. Der **%-Operator** ist veraltet und sollte in neuem Code vermieden werden.

3. **`print()`** akzeptiert die Parameter `sep` (Trennzeichen zwischen Argumenten), `end` (was am Ende ausgegeben wird) und `flush` (sofortiges Schreiben ohne Pufferung).

4. **Escape-Sequenzen** wie `\n` (Zeilenumbruch), `\t` (Tab) und `\\` (Backslash) ermöglichen die Darstellung von Spezialzeichen. **Raw Strings** mit `r"..."` deaktivieren Escape-Sequenzen.

5. **Dateien** werden mit `open(filename, mode)` geöffnet. Der Mode bestimmt, ob gelesen (`"r"`), geschrieben (`"w"`) oder angehängt (`"a"`) wird. Das **`with`-Statement** ist die empfohlene Methode, da es automatisches Schließen garantiert.

### Neue Python-Funktionen/Methoden

In dieser Lektion wurden folgende Python-Funktionen und -Konzepte **neu eingeführt**:

#### String-Formatierung
- **f-Strings** (Python 3.6+): `f"Text {variable}"` mit Formatspezifikationen wie `{x:.2f}`, `{x:10.2f}`, `{x:.3e}`, `{x:,}`, `{x:.1%}`
- **`.format()`-Methode**: `"Text {}".format(value)` mit Positions- und benannten Argumenten
- **%-Operator** (legacy): `"Text %s" % (value,)` mit Platzhaltern wie `%s`, `%d`, `%f`

#### Erweiterte `print()`-Parameter
- **`sep`-Parameter**: `print(a, b, sep="-")` – Trennzeichen zwischen Argumenten
- **`end`-Parameter**: `print(text, end="")` – was am Ende ausgegeben wird
- **`flush`-Parameter**: `print(text, flush=True)` – sofortiges Schreiben ohne Pufferung

#### Escape-Sequenzen und Strings
- **Escape-Sequenzen**: `\n` (newline), `\t` (tab), `\\` (backslash), `\'`, `\"`
- **Raw Strings**: `r"C:\Users"` – Backslashes werden nicht als Escape interpretiert
- **Mehrzeilige Strings**: `"""Text über\nmehrere Zeilen"""`

#### Datei-Ein-/Ausgabe
- **`open(filename, mode)`** (Built-in): Öffnet eine Datei
  - Modi: `"r"` (read), `"w"` (write), `"a"` (append)
- **`.write(string)`**: Schreibt String in Datei (ohne automatischen Zeilenumbruch)
- **`.read()`**: Liest gesamten Dateiinhalt als String
- **`.readlines()`**: Liest alle Zeilen als Liste von Strings
- **`with`-Statement**: Context Manager für automatisches Schließen von Ressourcen

---

## Weiterführende Ressourcen

### Theorie

- **IEEE 754 Standard (offizielles Dokument)**: https://standards.ieee.org/standard/754-2019.html – Der vollständige Standard (sehr technisch)
- **What Every Computer Scientist Should Know About Floating-Point Arithmetic** von David Goldberg: https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html – Klassischer Artikel zum Thema
- **Floating Point Visually Explained**: https://fabiensanglard.net/floating_point_visually_explained/ – Interaktive Visualisierung des IEEE 754 Formats
- **Online IEEE 754 Converter**: https://www.h-schmidt.net/FloatConverter/IEEE754.html – Tool zum Experimentieren mit Fließkommazahlen

### Python

- **Python String Formatting (offizielle Dokumentation)**: https://docs.python.org/3/library/string.html#formatstrings – Vollständige Referenz aller Formatierungsoptionen
- **Python f-Strings Guide**: https://realpython.com/python-f-strings/ – Umfassender Artikel zu f-Strings
- **Python File I/O Tutorial**: https://realpython.com/read-write-files-python/ – Ausführliche Anleitung zum Arbeiten mit Dateien
- **Python Format Specification Mini-Language**: https://docs.python.org/3/library/string.html#format-specification-mini-language – Details zur Formatspezifikation
- **PEP 498 – Literal String Interpolation**: https://www.python.org/dev/peps/pep-0498/ – Die offizielle Spezifikation für f-Strings
