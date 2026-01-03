# V02: Lösungen - Fließkommazahlen

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: IEEE 754 Single Precision Darstellung

**Lösung**:

```
Vorzeichen: 1
Exponent (binär): 10000001
Mantisse (binär): 01110000000000000000000
```

**Vollständige 32-Bit Darstellung**:
```
1 10000001 01110000000000000000000
```

**Erklärung**:

Die Zahl -5.75 wird in mehreren Schritten in die IEEE 754 Darstellung überführt.

**Schritt 1: Vorzeichen bestimmen**

Die Zahl ist negativ, daher ist das Vorzeichenbit $s = 1$.

**Schritt 2: Dezimalzahl in Binärform umwandeln**

Ganzzahlteil: $5_{10} = 101_2$

Nachkommateil: $0.75_{10} = 0.11_2$

Begründung: $0.75 = \frac{3}{4} = \frac{1}{2} + \frac{1}{4} = 2^{-1} + 2^{-2} = 0.11_2$

Zusammen: $5.75_{10} = 101.11_2$

**Schritt 3: Normalisierung**

Verschiebe den Binärpunkt so, dass genau eine 1 links davon steht:

$$
101.11_2 = 1.0111_2 \times 2^2
$$

Der Exponent ist also $e = 2$.

**Schritt 4: Exponent mit Bias berechnen**

Bei Single Precision ist der Bias 127:

$$
e_{\text{gespeichert}} = e_{\text{real}} + 127 = 2 + 127 = 129
$$

In Binärform: $129_{10} = 10000001_2$

**Schritt 5: Mantisse extrahieren**

Aus der normalisierten Form $1.0111_2$ wird nur der Teil nach dem Punkt gespeichert (die führende 1 ist implizit):

$$
\text{Mantisse} = 0111 \text{, aufgefüllt mit Nullen auf 23 Bits}
$$

$$
01110000000000000000000
$$

**Schritt 6: Zusammensetzen**

```
Vorzeichen: 1 (negativ)
Exponent: 10000001 (129 = 2 + 127)
Mantisse: 01110000000000000000000
```

**Häufige Fehler**:
- **Vergessen des Bias**: Der Exponent wird nicht direkt gespeichert, sondern mit Bias 127. Ein häufiger Fehler ist, einfach 2 binär zu speichern (`00000010`) statt 129 (`10000001`).
- **Führende 1 mitgezählt**: Die führende 1 in der normalisierten Mantisse ist implizit und wird **nicht** gespeichert. Aus `1.0111` wird nur `0111` gespeichert.
- **Nachkommaanteil falsch umgewandelt**: $0.75 = 0.11_2$ (nicht $0.75_2$, was keinen Sinn ergibt). Die Umwandlung erfolgt durch wiederholte Multiplikation mit 2.

---

### Lösung T2: Rundungsfehler analysieren

**Lösung**:

**1. Exaktes mathematisches Ergebnis**:

Dezimal: $a + b = 1.625 + 0.26875 = 1.89375_{10}$

Binär: $1.89375_{10} = 1.111001_2$ (genau darstellbar)

Nachweis: $1 + 2^{-1} + 2^{-2} + 2^{-3} + 2^{-6} = 1 + 0.5 + 0.25 + 0.125 + 0.015625 = 1.890625$ ❌

Korrektur: Rechnen wir genau:
- $1.625 = 1 + 0.625 = 1 + \frac{5}{8} = 1.101_2$
- $0.26875 = \frac{1}{4} + \frac{1}{32} = 0.01001_2$

Addition:
```
    1.10100  (1.625, Exponent angepasst)
  + 0.01001  (0.26875)
  ---------
    1.11101  
```

Ergebnis: $1.11101_2 = 1 + 0.5 + 0.25 + 0.125 + 0.03125 = 1.90625_{10}$

**Korrektur der Dezimalrechnung**: $1.625 + 0.26875 = 1.89375_{10}$

Lassen Sie mich die Binäraddition korrekt durchführen:

$1.625_{10} = 1.101_2$  
$0.26875_{10} = 0.010001_2$ (da $0.25 + 0.015625 + 0.003125 = 0.26875$)

Tatsächlich: $0.26875 = \frac{43}{160}$

Einfacher: Direkt konvertieren:
- $1.89375 \times 2 = 3.7875$ → 1
- $0.7875 \times 2 = 1.575$ → 1
- $0.575 \times 2 = 1.15$ → 1
- $0.15 \times 2 = 0.3$ → 0
- $0.3 \times 2 = 0.6$ → 0
- $0.6 \times 2 = 1.2$ → 1
- $0.2 \times 2 = 0.4$ → 0
- $0.4 \times 2 = 0.8$ → 0

$1.89375_{10} = 1.1110010_2$ (periodisch weitergehend)

**2. Normalisierte binäre Darstellung (vor der Rundung)**:

$$
1.89375_{10} = 1.1110010\ldots_2 \times 2^0
$$

Bei nur 4 Bits für die Mantisse (plus implizites Bit): $1.1110010_2$

**3. Gerundetes Ergebnis auf 4 Bits Mantisse**:

Zu speichernde Mantisse: Die ersten 4 Bits nach dem impliziten 1. sind `1110`

Nächstes Bit (für Rundung): `0`

Da das fünfte Bit eine `0` ist, wird **nicht** aufgerundet (Round to nearest, ties to even).

Gerundetes Ergebnis: $1.1110_2 \times 2^0 = 1.875_{10}$

Nachweis: $1 + 2^{-1} + 2^{-2} + 2^{-3} = 1 + 0.5 + 0.25 + 0.125 = 1.875$

**4. Absoluter Rundungsfehler**:

$$
\text{Fehler} = |1.89375 - 1.875| = 0.01875
$$

**Erklärung**:

Bei der Addition von Fließkommazahlen müssen zunächst die **Exponenten angeglichen** werden. In diesem Fall haben beide Zahlen unterschiedliche Exponenten:

- $a = 1.101_2 \times 2^0$
- $b = 1.011_2 \times 2^{-2}$

Um sie zu addieren, müssen wir einen gemeinsamen Exponenten wählen. Wir verwenden $2^0$:

$$
b = 1.011_2 \times 2^{-2} = 0.01011_2 \times 2^0
$$

Jetzt können wir addieren:
```
    1.10100  (a, mit Nullen aufgefüllt)
  + 0.01011  (b, angepasst)
  ---------
    1.11111
```

Warten, korrigieren wir das genau:

$a = 1.625 = 1.101_2$  
$b = 0.26875 = ?$

$0.26875 \times 2 = 0.5375$ → 0  
$0.5375 \times 2 = 1.075$ → 1  
$0.075 \times 2 = 0.15$ → 0  
$0.15 \times 2 = 0.3$ → 0  
$0.3 \times 2 = 0.6$ → 0  
$0.6 \times 2 = 1.2$ → 1  
$0.2 \times 2 = 0.4$ → 0  
$0.4 \times 2 = 0.8$ → 0  
$0.8 \times 2 = 1.6$ → 1  

$0.26875 = 0.01000101_2$ (periodisch)

Normalisiert: $1.000101_2 \times 2^{-2}$

In Exponent $2^0$ umgerechnet: $0.01000101_2 \times 2^0$

Addition:
```
    1.10100000
  + 0.01000101
  -----------
    1.11100101
```

Mit 4 Bits Mantisse: `1110` (das fünfte Bit ist `0`, also abrunden)

Ergebnis: $1.1110_2 = 1.875_{10}$

Fehler: $|1.89375 - 1.875| = 0.01875_{10}$

**Lösungsweg Schritt für Schritt**:

1. Exponenten angleichen (kleineren Exponenten erhöhen durch Rechtsshift der Mantisse)
2. Mantissen addieren
3. Ergebnis normalisieren (falls nötig)
4. Auf gewünschte Mantissen-Länge runden
5. Rundungsfehler berechnen als Differenz zwischen exaktem und gerundetem Wert

**Häufige Fehler**:
- **Exponenten nicht angeglichen**: Direktes Addieren der Mantissen ohne Exponentenangleichung führt zu falschem Ergebnis
- **Falsche Rundungsregel**: "Round to nearest" bedeutet: Bei genau 0.5 wird zur nächsten **geraden** Zahl gerundet (Ties to even)
- **Normalisierung vergessen**: Nach der Addition muss das Ergebnis möglicherweise renormalisiert werden

---

### Lösung T3: Spezielle Werte und Maschinenepsilon

**Lösung Teil A**:

1. `0 11111111 00000000000000000000000` → **+∞ (Positive Unendlichkeit)**
   - Exponent: alle Bits 1
   - Mantisse: alle Bits 0
   - Vorzeichen: 0 (positiv)

2. `1 11111111 00000000000000000000000` → **-∞ (Negative Unendlichkeit)**
   - Exponent: alle Bits 1
   - Mantisse: alle Bits 0
   - Vorzeichen: 1 (negativ)

3. `0 11111111 10000000000000000000000` → **NaN (Not a Number)**
   - Exponent: alle Bits 1
   - Mantisse: mindestens ein Bit 1 (hier: erstes Bit)
   - Jede Kombination mit Exponent=255 und Mantisse≠0 ist NaN

4. `0 00000000 00000000000000000000000` → **+0 (Positive Null)**
   - Exponent: alle Bits 0
   - Mantisse: alle Bits 0
   - Vorzeichen: 0 (positiv)

5. `1 00000000 00000000000000000000000` → **-0 (Negative Null)**
   - Exponent: alle Bits 0
   - Mantisse: alle Bits 0
   - Vorzeichen: 1 (negativ)

**Lösung Teil B: Maschinenepsilon**

Das Maschinenepsilon für IEEE 754 Single Precision beträgt:

$$
\epsilon_{\text{machine}} = 2^{-23} \approx 1.19209 \times 10^{-7}
$$

**Erklärung**:

Das Maschinenepsilon ist die kleinste Zahl, die zu 1.0 addiert ein von 1.0 verschiedenes Ergebnis liefert.

**Schritt 1: Darstellung von 1.0**

Die Zahl 1.0 wird dargestellt als:
$$
1.0 = 1.0_2 \times 2^0
$$

In IEEE 754 Single Precision:
- Vorzeichen: 0
- Exponent: $0 + 127 = 127 = 01111111_2$
- Mantisse: $00000000000000000000000$ (alle Nullen nach der impliziten 1)

**Schritt 2: Nächstgrößere darstellbare Zahl**

Die nächstgrößere darstellbare Zahl hat dieselbe Vorzeichen- und Exponentenstruktur, aber die Mantisse ist um das kleinste Bit (Bit 23, LSB) erhöht:

Mantisse: $00000000000000000000001$

Dies repräsentiert:
$$
1.00000000000000000000001_2 \times 2^0
$$

Das zusätzliche Bit in Position 23 entspricht einem Gewicht von $2^{-23}$.

**Schritt 3: Differenz berechnen**

$$
\epsilon_{\text{machine}} = (1.0 + 2^{-23}) - 1.0 = 2^{-23}
$$

**Numerischer Wert**:

$$
2^{-23} = \frac{1}{8388608} \approx 1.1920928955078125 \times 10^{-7}
$$

**Interpretation**:

Jede Zahl in der Nähe von 1.0, die zwischen 1.0 und $1.0 + 2^{-23}$ liegt, wird entweder auf 1.0 oder auf $1.0 + 2^{-23}$ gerundet – es gibt keine Fließkommazahlen dazwischen. Dies ist die **Granularität** des Fließkommasystems bei diesem Exponenten.

**Wichtige Anmerkung**: Das relative Maschinenepsilon ist konstant (die relative Genauigkeit ist über den gesamten Wertebereich konstant), aber der **absolute Abstand** zwischen benachbarten Zahlen wächst mit dem Exponenten:

- Bei $1.0$: kleinster Abstand = $2^{-23}$
- Bei $1000.0 = 2^{9.97}$: kleinster Abstand ≈ $2^{-13}$
- Bei $1000000.0 = 2^{19.93}$: kleinster Abstand ≈ $2^{-3}$

**Lösungsweg Schritt für Schritt**:

1. Darstellung von 1.0 in IEEE 754 identifizieren
2. Mantisse hat 23 Bits (plus implizites Bit = 24 Bits Genauigkeit)
3. Kleinstes darstellbares Inkrement in der Mantisse ist das LSB (Bit 23)
4. Gewicht dieses Bits: $2^{-23}$
5. Maschinenepsilon = $2^{-23}$

**Alternative Lösungsansätze**:

**Ansatz 1: Über die Anzahl signifikanter Bits**
- 23 Bits Mantisse + 1 implizites Bit = 24 Bits Genauigkeit
- Relative Genauigkeit: $2^{-24}$ (halbes ULP, unit in last place)
- Maschinenepsilon (IEEE 754 Definition): $2^{-23}$

**Ansatz 2: Experimentell (in Python)**
```python
epsilon = 1.0
while 1.0 + epsilon / 2 != 1.0:
    epsilon = epsilon / 2
# epsilon ist nun das Maschinenepsilon
```

✅ Vorteile Ansatz 1: Direkt aus der Bit-Struktur ableitbar  
❌ Nachteile Ansatz 1: Erfordert genaues Verständnis der IEEE 754 Struktur

✅ Vorteile Ansatz 2: Intuitiv und praktisch nachprüfbar  
❌ Nachteile Ansatz 2: Keine theoretische Herleitung

**Häufige Fehler**:
- **Verwechslung von $2^{-23}$ und $2^{-24}$**: Das Maschinenepsilon nach IEEE 754 Definition ist $2^{-23}$ (nicht $2^{-24}$, was die halbe ULP wäre)
- **Vergessen des impliziten Bits**: Die Mantisse hat 23 gespeicherte Bits, aber 24 Bits effektive Genauigkeit durch das implizite führende Bit
- **Annahme konstanten absoluten Abstands**: Der absolute Abstand zwischen benachbarten Fließkommazahlen ist **nicht** konstant, sondern wächst mit dem Exponenten

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: Werkzeugmaschinen-Dashboard

**Vollständiger Code**:
```python
# CNC-Fräsmaschine - Betriebsparameter
spindel_drehzahl = 3456.789  # U/min
vorschubgeschwindigkeit = 0.0425  # m/s → mm/s
schnitttiefe = 2.5678  # mm
oberflaeche = 1.234e-6  # m² → μm
auslastung = 0.873  # 0-1 → %

# Umrechnungen
vorschub_mm = vorschubgeschwindigkeit * 1000  # m/s → mm/s
ra_wert_mikrometer = oberflaeche * 1e6  # m² → μm

# Formatierte Ausgabe
print("╔═══════════════════════════════════════╗")
print("║   CNC-FRÄSMASCHINE DMU 50 ecoline   ║")
print("╠═══════════════════════════════════════╣")
print(f"║ Spindeldrehzahl:      {spindel_drehzahl:7.2f} U/min ║")
print(f"║ Vorschub:               {vorschub_mm:5.2f} mm/s  ║")
print(f"║ Schnitttiefe:            {schnitttiefe:4.2f} mm    ║")
print(f"║ Oberflächengüte (Ra):    {ra_wert_mikrometer:4.2f} μm    ║")
print(f"║ Maschinenauslastung:    {auslastung:4.1%}      ║")
print("╚═══════════════════════════════════════╝")
```

**Maschinenbau-Kontext**:

**CNC-Maschinen** (Computerized Numerical Control) sind computergesteuerte Werkzeugmaschinen, die Werkstücke mit höchster Präzision bearbeiten. Diese Dashboard-Anzeige zeigt typische **Betriebsparameter**:

- **Spindeldrehzahl** (n): Rotationsgeschwindigkeit des Fräswerkzeugs in U/min (Umdrehungen pro Minute)
- **Vorschubgeschwindigkeit** (vf): Geschwindigkeit, mit der das Werkzeug durch Material bewegt wird (mm/s oder mm/min)
- **Schnitttiefe** (ap): Wie tief das Werkzeug in das Material eindringt
- **Oberflächengüte (Ra-Wert)**: Mittlere Rautiefe in Mikrometern (μm) – je kleiner, desto glatter
- **Maschinenauslastung**: Anteil der Produktiv-Zeit (Schnittzeit) an Gesamtzeit

**Formatierungs-Erklärung**:
- `{spindel_drehzahl:7.2f}`: 7 Zeichen breit, 2 Dezimalstellen → `3456.79`
- `{auslastung:4.1%}`: Prozentformat mit 4 Zeichen, 1 Dezimalstelle → `87.3%` (×100 automatisch!)
- μm = 10⁻⁶ m (Mikrometer)

---

### Lösung P2: Präzisionsmessungen und Fertigungstoleranzen

**Vollständiger Code**:
```python
# Qualitätskontrolle - Präzisionsmessungen mit Toleranzprüfung

print("=== Präzisionsmessung - Qualitätskontrolle ===\n")

# Test 1: Werkstück-Länge (3× Teilmessung)
print("Test 1: Werkstück-Länge (3× Teilmessung)")
messung1 = 3.33 + 3.33 + 3.34  # mm (drei Teilstrecken)
messung_soll1 = 10.0  # mm (Soll-Maß)

print(f"Gemessen:  {messung1:.20f} mm")
print(f"Soll-Maß:  {messung_soll1:.20f} mm")
print(f"Exakt gleich (==)?: {messung1 == messung_soll1}")

# IT7-Toleranz (ISO 286): ±0.1 mm für Standardteile
toleranz = 0.1  # mm
abweichung1 = abs(messung1 - messung_soll1)
bestanden1 = abweichung1 <= toleranz

status1 = "✓ BESTANDEN" if bestanden1 else "✗ DURCHGEFALLEN"
print(f"Innerhalb IT7-Toleranz (±{toleranz} mm)?: {status1} (Abweichung: {abweichung1:.2f} mm)")

print()

# Test 2: Bohrungsabstand (X + Y)
print("Test 2: Bohrungsabstand (X + Y)")
bohrung_x = 12.5  # mm (X-Richtung)
bohrung_y = 12.5  # mm (Y-Richtung)
messung2 = bohrung_x + bohrung_y
messung_soll2 = 25.0  # mm

print(f"Gemessen:  {messung2:.20f} mm")
print(f"Soll-Maß:  {messung_soll2:.20f} mm")
print(f"Exakt gleich (==)?: {messung2 == messung_soll2}")

abweichung2 = abs(messung2 - messung_soll2)
bestanden2 = abweichung2 <= toleranz
status2 = "✓ BESTANDEN" if bestanden2 else "✗ DURCHGEFALLEN"
print(f"Innerhalb IT7-Toleranz (±{toleranz} mm)?: {status2} (Abweichung: {abweichung2:.2f} mm)")
```

**Ausgabe**:
```
=== Rundungsfehler-Demonstration ===

Test 1: 0.1 + 0.2 vs. 0.3
Berechnet:  0.30000000000000004441
Erwartet:   0.29999999999999998890
Gleich (==)?  False
Epsilon-Vergleich (Toleranz 1e-09): True

Test 2: 0.1 + 0.1 + 0.1 vs. 0.3
Berechnet:  0.30000000000000004441
Erwartet:   0.29999999999999998890
Gleich (==)?  False
Epsilon-Vergleich (Toleranz 1e-09): True
```

**Maschinenbau-Kontext**:

In der **Qualitätssicherung** werden Bauteile mit Messgeräten (Messschieber, Koordinatenmessmaschine) geprüft. Aufgrund von Fließkomma-Arithmetik in der Auswertungssoftware darf man **niemals mit `==` vergleichen**, sondern muss **Toleranzen** nach ISO 286 (IT-Grade) verwenden.

**Wichtige Toleranzklassen**:
- **IT5**: ±0.01 mm (Hochpräzisionsteile, z.B. Lager)
- **IT7**: ±0.1 mm (Standardteile, z.B. Wellen, Bohrungen)
- **IT12**: ±1 mm (Gussteile, grobe Bearbeitung)

**Schritt-für-Schritt Durchlauf**:

1. **Messwerte addieren**:
   ```python
   messung1 = 3.33 + 3.33 + 3.34  # = 10.00
   ```
   - Drei Teilmessungen an einem Werkstück
   - Fließkomma-Arithmetik kann kleine Rundungsfehler erzeugen

2. **Mit 20 Dezimalstellen ausgeben**:
   ```python
   print(f"{berechnet1:.20f}")
   ```
   - Zeigt den tatsächlich gespeicherten Wert
   - `0.30000000000000004441...` statt `0.3`

3. **Direkter Vergleich mit `==`**:
   ```python
   berechnet1 == erwartet1  # False!
   ```
   - Vergleicht Bit für Bit
   - Auch `0.3` wird gerundet gespeichert, aber anders als `0.1 + 0.2`
   - Daher nicht gleich

4. **Epsilon-Vergleich**:
   ```python
   abs(berechnet1 - erwartet1) < epsilon
   ```
   - Prüft, ob die Differenz kleiner als die Toleranzgrenze ist
   - Mit $\epsilon = 10^{-9}$ sind die Werte "praktisch gleich"
   - Dies ist die **richtige Methode** für Fließkomma-Vergleiche

**Konzepte in dieser Lösung**:

- **Formatierung mit vielen Dezimalstellen**: `:.20f` zeigt die internen Rundungsfehler
- **Absoluter Vergleich**: `abs(a - b) < epsilon` ist der Standard für Fließkomma-Vergleiche
- **Toleranz (Epsilon)**: $10^{-9}$ ist für Double Precision ein sinnvoller Wert

**Warum dieser Ansatz?**

Der Epsilon-Vergleich ist die einzig korrekte Methode zum Vergleichen von Fließkommazahlen. Der direkte Vergleich mit `==` ist fast immer falsch, da:
- Rundungsfehler unvermeidlich sind
- Verschiedene Berechnungswege zu minimal unterschiedlichen Ergebnissen führen
- Mathematisch äquivalente Ausdrücke unterschiedliche Binärdarstellungen haben können

**Häufige Fehler**:
- **Fehler**: Verwendung von `==` für Fließkomma-Vergleiche
  ```python
  if berechnet == erwartet:  # Fast immer falsch!
      print("Gleich")
  ```
  - **Warum falsch**: Ignoriert Rundungsfehler
  - **Richtig**: `if abs(berechnet - erwartet) < 1e-9:`

- **Fehler**: Zu kleine Toleranz
  ```python
  if abs(a - b) < 1e-20:  # Zu streng!
  ```
  - **Warum problematisch**: Bei Double Precision ist die Genauigkeit nur ~15-16 Dezimalstellen
  - **Richtig**: `1e-9` bis `1e-12` für normale Anwendungen

- **Fehler**: Fehlende `abs()`
  ```python
  if berechnet - erwartet < epsilon:  # Falsch!
  ```
  - **Warum falsch**: Funktioniert nicht, wenn `berechnet < erwartet`
  - **Richtig**: `abs(berechnet - erwartet) < epsilon`

---

### Lösung P3: Kühlmitteltemperatur-Tabelle für Bearbeitungsprozess

**Vollständiger Code**:
```python
# Kühlmitteltemperatur-Überwachung für CNC-Maschine

print("╔═══════════════════════════════════════════╗")
print("║  Celsius │ Kelvin    │ Status           ║")
print("╠═══════════════════════════════════════════╣")

for celsius in range(10, 61, 5):
    # Formel: K = C + 273.15
    kelvin = celsius + 273.15
    
    # Status bestimmen
    if celsius < 15:
        status = "❄️ ZU KALT"
    elif celsius > 50:
        status = "🔥 ZU HEISS"
    else:
        status = "✓ OPTIMAL"
    
    print(f"║ {celsius:8.2f} │ {kelvin:9.2f}   │ {status:16} ║")

print("╚═══════════════════════════════════════════╝")
print()
print("Optimaler Bereich: 15°C - 50°C (288.15 K - 323.15 K)")
```

**Ausgabe**:
```
╔═══════════════════════════╗
║  Celsius | Fahrenheit    ║
╠═══════════════════════════╣
║    -40.0 |       -40.0   ║
║    -30.0 |       -22.0   ║
║    -20.0 |        -4.0   ║
║    -10.0 |        14.0   ║
║      0.0 |        32.0   ║
║     10.0 |        50.0   ║
║     20.0 |        68.0   ║
║     30.0 |        86.0   ║
║     40.0 |       104.0   ║
║     50.0 |       122.0   ║
╚═══════════════════════════╝
```

**Maschinenbau-Kontext**:

Bei **spanenden Fertigungsverfahren** (Drehen, Fräsen, Bohren) wird **Kühlschmierstoff** (KSS) eingesetzt, um:
- Werkzeug und Werkstück zu kühlen
- Reibung zu verringern
- Späne abzutransportieren
- Oberflächenqualität zu verbessern

Die Temperatur muss im **optimalen Bereich 15-50°C** liegen:
- **< 15°C**: Zu kalt → schlechte Schmierwirkung, schlechte Oberflächengüte
- **> 50°C**: Zu heiß → Werkzeugverschleiß steigt, Emulsion kann brechen

**Kelvin-Skala**: Absolute Temperaturskala (0 K = -273.15°C = absoluter Nullpunkt). In der Thermodynamik und Materialkunde verwendet.

**Schritt-für-Schritt Durchlauf**:

1. **Schleife über Temperaturbereich**:
   ```python
   for celsius in range(10, 61, 5):
   ```
   - Startet bei 10°C, endet bei 60°C
   - Schrittweite: 5°C

2. **Umrechnung Celsius → Kelvin**:
   ```python
   kelvin = celsius + 273.15
   ```
   - Einfache Addition (keine Skalierung wie bei Fahrenheit)
   - Beispiel: 20°C = 293.15 K

3. **Status-Logik**:
   ```python
   if celsius < 15:
       status = "❄️ ZU KALT"
   elif celsius > 50:
       status = "🔥 ZU HEISS"
   else:
       status = "✓ OPTIMAL"
   ```
   - Warnsystem für Maschinenbediener

4. **Formatierte Ausgabe**:
   ```python
   print(f"║ {celsius:8.1f} | {fahrenheit:12.1f}   ║")
   ```
   - `{celsius:8.1f}`: Rechtsbündig, Breite 8, 1 Dezimalstelle
   - `{fahrenheit:12.1f}`: Rechtsbündig, Breite 12, 1 Dezimalstelle
   - Zusätzliche Leerzeichen für korrekte Rahmenausrichtung

5. **Tabellen-Footer**:
   ```python
   print("╚═══════════════════════════╝")
   ```

**Warum diese Lösung?**

Die Kombination aus `range()` für die Schleife und f-Strings für die Formatierung ist elegant und effizient. Die Formel wird direkt in einer Zeile berechnet, was den Code kompakt hält.

**Interessante Fakten**:
- Bei -40°C = -40°F sind beide Skalen identisch
- Der Nullpunkt der Celsius-Skala (0°C) entspricht 32°F (Gefrierpunkt von Wasser)
- Eine Änderung um 1°C entspricht einer Änderung um 1.8°F

**Häufige Fehler**:
- **Fehler**: Falsche Formel (häufig: Reihenfolge der Operationen)
  ```python
  fahrenheit = celsius * (9 / 5 + 32)  # Falsch!
  ```
  - **Warum falsch**: Punkt-vor-Strich nicht beachtet, Klammern falsch gesetzt
  - **Richtig**: `celsius * 9 / 5 + 32` oder `celsius * (9/5) + 32`

- **Fehler**: Ganzzahldivision vergessen
  ```python
  fahrenheit = celsius * 9 / 5 + 32  # In Python 3: korrekt
  ```
  - In Python 2 wäre `9 / 5` Ganzzahldivision → 1 statt 1.8
  - In Python 3: `/` ist immer Fließkommadivision → korrekt

- **Fehler**: Range-Endpunkt falsch
  ```python
  for celsius in range(-40, 50, 10):  # Fehlt: 50°C
  ```
  - **Warum falsch**: `range()` ist exklusiv beim Endpunkt
  - **Richtig**: `range(-40, 51, 10)` für -40 bis +50

---

### Lösung P4: Maschinenprotokoll mit Zeitstempel

**Vollständiger Code**:
```python
# Maschinenprotokoll-System für CNC-Maschine

print("=== Maschinenprotokoll-System DMG MORI ===")
print()

# Simulierte Zeit-Variablen (Start: 08:00:00)
stunde = 8
minute = 0
sekunde = 0

while True:
    # Eingabe
    ereignis = input("Ereignistyp (START/STOP/WARTUNG/FEHLER/ALARM): ").upper()
    nachricht = input("Nachricht: ")
    
    # Zeitstempel erstellen
    zeitstempel = f"2026-01-15 {stunde:02d}:{minute:02d}:{sekunde:02d}"
    
    # Logeintrag formatieren
    log_eintrag = f"[{zeitstempel}] {ereignis}: {nachricht}\n"
    
    # In Datei schreiben (anhängen)
    with open("maschine_dmg_001.log", "a") as datei:
        datei.write(log_eintrag)
    
    # Auf Konsole ausgeben
    print(f"\n✓ Eintrag gespeichert:")
    print(log_eintrag.strip())
    
    # Zeit um 15 Minuten erhöhen
    minute += 15
    if minute >= 60:
        minute = 0
        stunde += 1
        if stunde >= 24:
            stunde = 0
    
    # Weiteren Eintrag?
    weiter = input("\nWeiteren Eintrag hinzufügen? (j/n): ").lower()
    if weiter != "j":
        break

# Alle Logs anzeigen
print("\n=== Gespeicherte Protokolleinträge ===")
with open("maschine_dmg_001.log", "r") as datei:
    inhalt = datei.read()
    print(inhalt)
```

**Maschinenbau-Kontext**:

**Maschinenprotokolle** sind in der Industrie **gesetzlich vorgeschrieben** (Maschinenrichtlinie 2006/42/EG). Sie dienen:
- **Traceability**: Rückverfolgbarkeit bei Produkthaftung
- **Wartungsplanung**: Predictive Maintenance durch Fehler-Muster-Erkennung
- **Industrie 4.0**: Logs werden an Cloud-Systeme (MES, ERP) übertragen
- **Fehleranalyse**: Post-Mortem-Analyse bei Maschinenschäden

**Ereignistypen**:
- **START**: Maschine eingeschaltet, Referenzfahrt durchgeführt
- **STOP**: Reguläres Herunterfahren
- **WARTUNG**: Ölstand geprüft, Filter gewechselt, Kalibrierung
- **FEHLER**: Betriebsstörung (z.B. Kühlmitteldruck niedrig, Spindel überhitzt)
- **ALARM**: Sicherheitskritisch (Not-Aus betätigt, Schutztür offen)

**Schritt-für-Schritt Durchlauf**:

1. **Zeitvariablen initialisieren**:
   ```python
   stunde = 8  # Schichtbeginn: 08:00:00
   minute = 0
   ```

2. **Zeitstempel formatieren** (ISO 8601):
   ```python
   zeitstempel = f"2026-01-15 {stunde:02d}:{minute:02d}:{sekunde:02d}"
   ```
   - `{stunde:02d}`: Führende Null (09 statt 9)

3. **Append-Modus** (wichtig!):
   ```python
   with open("maschine_dmg_001.log", "a") as datei:
   ```
   - `"a"` = Anhängen, **nicht** überschreiben
   - Bei "w" würden alte Logs gelöscht → Datenverlust!

4. **Zeit inkrementieren** (15 Minuten):
   ```python
   minute += 15
   if minute >= 60:
       minute = 0
       stunde += 1
   ```
   - Überlauf-Behandlung essentiell
   ```
   - Liest die gesamte Datei ein
   - Zeigt alle bisher gespeicherten Logs

**Konzepte in dieser Lösung**:

- **Datei-Persistenz**: Daten bleiben nach Programmende erhalten
- **Append-Modus**: Wichtig, um bestehende Logs nicht zu überschreiben
- **Zeitberechnung**: Manuelle Zeitarithmetik mit Überlauf-Behandlung
- **String-Manipulation**: `.upper()`, `.strip()`, `.lower()` für Eingabe-Normalisierung
- **Context Manager**: `with`-Statement für sichere Datei-Operationen

**Design-Entscheidungen**:

- **Warum manuelle Zeitberechnung statt Bibliothek?**  
  In V02 haben wir noch keine Zeitbibliotheken eingeführt. Die manuelle Berechnung demonstriert grundlegende Programmierkonzepte (Bedingungen, Überlauf-Logik).

- **Warum `.upper()` bei Ereignistyp?**  
  Sorgt für konsistente Log-Einträge unabhängig von der Benutzereingabe.

- **Warum Append-Modus?**  
  Logs sollten akkumuliert werden, nicht überschrieben. Append ist Standard für Log-Dateien.

**Häufige Fehler**:

- **Fehler**: Verwendung von Write-Modus statt Append
  ```python
  with open("system.log", "w") as datei:  # Falsch!
  ```
  - **Warum falsch**: `"w"` löscht bei jedem Aufruf alle bisherigen Logs
  - **Richtig**: `"a"` für Append (Anhängen)

- **Fehler**: Fehlende Zeilenumbrüche
  ```python
  datei.write(log_eintrag)  # Ohne \n
  ```
  - **Problem**: Alle Einträge stehen in einer Zeile
  - **Lösung**: `log_eintrag` muss `\n` am Ende enthalten

- **Fehler**: Zeit-Überlauf nicht behandelt
  ```python
  sekunde += 15  # Was passiert bei sekunde=59?
  ```
  - **Problem**: Ohne Überlauf-Logik entstehen ungültige Werte wie 74 Sekunden
  - **Lösung**: `if sekunde >= 60: sekunde = 0; minute += 1`

- **Fehler**: Vergessenes `.strip()` bei Ausgabe
  ```python
  print(log_eintrag)  # Druckt mit \n → doppelter Zeilenumbruch
  ```
  - **Problem**: `print()` fügt eigenes `\n` hinzu, log_eintrag hat auch `\n` → Leerzeile
  - **Lösung**: `print(log_eintrag.strip())` entfernt Whitespace

---

### Lösung P5: Prüfprotokoll-Generator für Materialchargen

**Vollständiger Code**:
```python
# Prüfprotokoll-Generator für Zugversuche (DIN EN ISO 6892-1)
# Material: Stahl S235JR (DIN EN 10025)

print("Generiere Prüfdaten für Charge 2026-001...\n")

# Teil 1: Datengenerierung für 50 Prüfkörper
daten = []  # Liste: [(id, rm, rp02, a, temp), ...]

for i in range(1, 51):  # P001 bis P050
    proben_id = f"P{i:03d}"  # P001, P002, ..., P050
    
    # Pseudo-Zufallsschwankungen (ohne random-Modul)
    schwankung_rm = ((i * 13) % 20 - 10) / 500.0  # ±2% von 235 MPa
    schwankung_rp = ((i * 17) % 20 - 10) / 1000.0  # ±1%
    schwankung_a = ((i * 23) % 20 - 10) / 400.0  # ±3% von 25%
    schwankung_temp = ((i * 7) % 40 - 20) / 10.0  # ±2°C
    
    # Zugfestigkeit Rm (Startwert 235 MPa für S235JR)
    rm = 235.0 + schwankung_rm * 235.0
    
    # Streckgrenze Rp0.2 (ca. 70% von Rm)
    rp02 = rm * 0.70 + schwankung_rp * rm
    
    # Bruchdehnung A (Basiswert 25%)
    a = 25.0 + schwankung_a * 25.0
    
    # Prüftemperatur (Norm: 23°C)
    temp = 23.0 + schwankung_temp
    
    daten.append((proben_id, rm, rp02, a, temp))

# Teil 2: CSV-Export
with open("pruefprotokoll_charge_2026_001.csv", "w") as datei:
    # Header
    datei.write("Proben-ID,Zugfestigkeit(MPa),Streckgrenze(MPa),Bruchdehnung(%),Temperatur(C)\n")
    
    # Daten
    for proben_id, rm, rp02, a, temp in daten:
        datei.write(f"{proben_id},{rm:.2f},{rp02:.2f},{a:.2f},{temp:.1f}\n")

# Teil 3: Statistik-Berechnung (ohne built-in min/max)

# Zugfestigkeit Rm
rm_min = daten[0][1]
rm_max = daten[0][1]
rm_summe = 0.0

for probe in daten:
    rm_wert = probe[1]
    if rm_wert < rm_min:
        rm_min = rm_wert
    if rm_wert > rm_max:
        rm_max = rm_wert
    rm_summe += rm_wert

rm_durchschnitt = rm_summe / len(daten)

# Streckgrenze Rp0.2
rp_min = daten[0][2]
rp_max = daten[0][2]
rp_summe = 0.0

for probe in daten:
    rp_wert = probe[2]
    if rp_wert < rp_min:
        rp_min = rp_wert
    if rp_wert > rp_max:
        rp_max = rp_wert
    rp_summe += rp_wert

rp_durchschnitt = rp_summe / len(daten)

# Bruchdehnung A
a_min = daten[0][3]
a_max = daten[0][3]
a_summe = 0.0

for probe in daten:
    a_wert = probe[3]
    if a_wert < a_min:
        a_min = a_wert
    if a_wert > a_max:
        a_max = a_wert
    a_summe += a_wert

a_durchschnitt = a_summe / len(daten)

# Teil 4: Abnahmeprüfung nach DIN EN 10025 (Mindestwerte für S235JR)
rm_bestanden = all(probe[1] >= 235.0 for probe in daten)
rp_bestanden = all(probe[2] >= 165.0 for probe in daten)
a_bestanden = all(probe[3] >= 22.0 for probe in daten)

gesamtstatus = "✓ CHARGE FREIGEGEBEN" if (rm_bestanden and rp_bestanden and a_bestanden) else "✗ CHARGE GESPERRT"

# Statistik-Ausgabe
print("╔═══════════════════════════════════════════════════╗")
print("║  PRÜFPROTOKOLL - Materialcharge 2026-001        ║")
print("║  Material: Stahl S235JR (DIN EN 10025)          ║")
print("╠═══════════════════════════════════════════════════╣")
print("║ Messgröße          │ Min    │ Ø      │ Max    ║")
print("╠═══════════════════════════════════════════════════╣")
print(f"║ Zugfestigkeit Rm   │ {rm_min:6.2f} │ {rm_durchschnitt:6.2f} │ {rm_max:6.2f} ║")
print(f"║ Streckgrenze Rp0.2 │ {rp_min:6.2f} │ {rp_durchschnitt:6.2f} │ {rp_max:6.2f} ║")
print(f"║ Bruchdehnung A     │ {a_min:6.2f} │ {a_durchschnitt:6.2f} │ {a_max:6.2f} ║")
print("╠═══════════════════════════════════════════════════╣")
print("║ Abnahmeprüfung nach DIN EN 10025:           ║")
print(f"║ • Zugfestigkeit:    {'✓ Alle ≥ 235 MPa' if rm_bestanden else '✗ NICHT BESTANDEN'}         ║")
print(f"║ • Streckgrenze:     {'✓ Alle ≥ 165 MPa' if rp_bestanden else '✗ NICHT BESTANDEN'}         ║")
print(f"║ • Bruchdehnung:     {'✓ Alle ≥ 22%' if a_bestanden else '✗ NICHT BESTANDEN'}             ║")
print("╠═══════════════════════════════════════════════════╣")
print(f"║ STATUS: {gesamtstatus:36} ║")
print("╚═══════════════════════════════════════════════════╝")
print(f"\n✓ {len(daten)} Prüfkörper in 'pruefprotokoll_charge_2026_001.csv' gespeichert")
```

**Maschinenbau-Kontext**:

Dieses Programm simuliert ein **Prüfprotokoll nach DIN EN ISO 6892-1** (Zugversuch). In der Qualitätssicherung werden Materialchargen (Coils, Bleche) durch **Zugversuche** geprüft, bevor sie in die Produktion gehen.

**Material S235JR** (Baustahl):
- Rm ≥ 235 MPa (Zugfestigkeit)
- Rp0.2 ≥ 165 MPa (Streckgrenze bei 0.2% plastischer Dehnung)
- A ≥ 22% (Bruchdehnung)
- Verwendung: Stahlbau, Maschinenbau, Fahrzeugbau

**Schritt-für-Schritt Durchlauf**:

1. **Proben-ID generieren**:
   ```python
   proben_id = f"P{i:03d}"  # P001, P002, ..., P050
   ```
   - Eindeutige Kennzeichnung jeder Probe

2. **Pseudo-Zufallsschwankungen** (ohne `random`):
   ```python
   schwankung_rm = ((i * 13) % 20 - 10) / 500.0
   ```
   - Modulo-Arithmetik erzeugt deterministische "Zufälligkeit"
   - ±2% Schwankung von 235 MPa

3. **Zugfestigkeit Rm berechnen**:
   ```python
   rm = 235.0 + schwankung_rm * 235.0
   ```
   - Basiswert 235 MPa (Mindestwert nach DIN EN 10025)

4. **Streckgrenze Rp0.2** (ca. 70% von Rm):
   ```python
   rp02 = rm * 0.70 + schwankung_rp * rm
   ```
   - Typisches Verhältnis bei Baustahl

5. **Statistik ohne Built-ins**:
   - Min/Max durch manuellen Vergleich
   - Durchschnitt durch Summe / Anzahl

6. **Abnahmeprüfung**:
   ```python
   rm_bestanden = all(probe[1] >= 235.0 for probe in daten)
   ```
   - `all()` prüft, ob **alle** Proben die Mindestwerte erfüllen
   - Bei einer Abweichung → Charge GESPERRT

**3.1-Abnahmeprüfzeugnis** (DIN EN 10204): Zertifikat, das dem Kunden die Einhaltung der Normen bestätigt.

---

## ✅ V02 vollständig abgeschlossen!
- Bei 1011 hPa: Höhe ≈ +20 m
- Bei 1015 hPa: Höhe ≈ -15 m

**Phase 2: CSV-Export**

```python
with open("sensor_data.csv", "w") as datei:
    datei.write("Zeit(s),Temperatur(C),Druck(hPa),Hoehe(m)\n")
```
- CSV-Standard: Komma-getrennte Werte
- Erste Zeile: Header mit Spaltennamen und Einheiten
- `\n` für Zeilenumbruch (wichtig!)

**Datenzeilen schreiben**:
```python
for zeit, temp, druck, hoehe in daten:
    datei.write(f"{zeit},{temp:.2f},{druck:.2f},{hoehe:.2f}\n")
```
- **Tupel-Unpacking**: `(zeit, temp, druck, hoehe)` wird aus jedem Listen-Element extrahiert
- Formatierung: Alle Fließkommazahlen mit 2 Dezimalstellen
- Keine Leerzeichen nach Kommas (CSV-Standard)

**Phase 3: Statistik-Berechnung**

**Eigene Min-Funktion**:
```python
temp_min = daten[0][1]  # Initialisierung
for zeit, temp, druck, hoehe in daten:
    if temp < temp_min:
        temp_min = temp
```
- Initialisierung mit erstem Wert (sicherer als mit 0 oder ∞)
- Iteration über alle Werte
- Vergleich und Aktualisierung bei kleinerem Wert

**Eigene Durchschnitts-Funktion**:
```python
temp_summe = 0.0
for zeit, temp, druck, hoehe in daten:
    temp_summe += temp
temp_durchschnitt = temp_summe / len(daten)
```
- Akkumulator-Muster: Summe initialisieren, dann addieren
- Durchschnitt = Summe / Anzahl (arithmetisches Mittel)
- `len(daten)` gibt Anzahl der Datenpunkte

**Komplexitätsanalyse**:

- **Zeitkomplexität (Gesamt)**: O(n)
  - Datengenerierung: O(n) – eine Schleife über n=100 Elemente
  - CSV-Export: O(n) – eine Schleife
  - Statistik: O(3n) – drei Schleifen über n Elemente
  - Gesamt: O(n) (konstante Faktoren werden ignoriert)

- **Speicherkomplexität**: O(n)
  - Liste `daten` speichert n Tupel mit jeweils 4 Float-Werten
  - CSV-Datei: ebenfalls O(n)

**Alternative Lösungsansätze**:

**Ansatz 1: Einzelne Listen statt Liste von Tupeln**
```python
zeiten = []
temperaturen = []
druecke = []
hoehen = []
# Dann getrennte Listen füllen
```
✅ Vorteile: Direkter Zugriff auf einzelne Messgrößen  
❌ Nachteile: Mehr Variablen, Synchronisation erforderlich

**Ansatz 2: Dictionary pro Datenpunkt**
```python
daten = []
for t in range(100):
    punkt = {
        "zeit": t,
        "temperatur": temp,
        "druck": druck,
        "hoehe": hoehe
    }
    daten.append(punkt)
```
✅ Vorteile: Selbstdokumentierend, Zugriff per Key  
❌ Nachteile: Mehr Speicher, langsamer

**Ansatz 3: Statistiken direkt während Generierung**
```python
temp_min = float('inf')
temp_max = float('-inf')
temp_summe = 0
for t in range(100):
    # ... temp berechnen ...
    temp_min = temp if temp < temp_min else temp_min
    temp_max = temp if temp > temp_max else temp_max
    temp_summe += temp
```
✅ Vorteile: Nur ein Durchlauf, O(n) statt O(4n)  
❌ Nachteile: Code unübersichtlicher, Daten nicht gespeichert für spätere Verwendung

**Die gewählte Lösung (Liste von Tupeln + separate Statistik-Schleifen)** ist ein guter Kompromiss:
- Klare Trennung der Verantwortlichkeiten
- Daten bleiben für weitere Verwendung (z.B. Bonus-Challenge) verfügbar
- Code bleibt lesbar und wartbar

**Bonus-Challenge Lösung**:

```python
# CSV einlesen und Statistiken neu berechnen
print("\n=== Bonus-Challenge: CSV einlesen ===")

daten_aus_csv = []

with open("sensor_data.csv", "r") as datei:
    # Header-Zeile überspringen
    header = datei.readline()
    
    # Datenzeilen einlesen
    for zeile in datei:
        # Zeile in Teile splitten (an Kommas)
        teile = zeile.strip().split(",")
        
        # Strings in Zahlen konvertieren
        zeit = int(teile[0])
        temp = float(teile[1])
        druck = float(teile[2])
        hoehe = float(teile[3])
        
        daten_aus_csv.append((zeit, temp, druck, hoehe))

# Statistiken neu berechnen (gleicher Code wie oben)
# ... (hier würde der gleiche Statistik-Code folgen) ...

print(f"✓ {len(daten_aus_csv)} Datenpunkte aus CSV gelesen")
print("✓ Statistiken erfolgreich neu berechnet")
```

**Erklärung Bonus-Challenge**:

- **`.readline()`**: Liest eine Zeile (hier: Header) und überspringt sie
- **`.strip()`**: Entfernt Whitespace und `\n` am Ende der Zeile
- **`.split(",")`**: Teilt String an Kommas in eine Liste von Strings
- **Typ-Konvertierung**: `int()` und `float()` konvertieren String-Teile zu Zahlen
- **Rekonstruktion**: Tupel werden identisch zu Original-Datenstruktur aufgebaut

**Häufige Fehler**:

- **Fehler**: Verwendung von Built-in-Funktionen
  ```python
  temp_min = min(temperaturen)  # Nicht erlaubt laut Aufgabe
  ```
  - **Lösung**: Eigene Implementierung mit Schleife

- **Fehler**: Vergessener Header in CSV
  ```python
  with open("sensor_data.csv", "w") as datei:
      for ...:
          datei.write(f"{zeit},{temp:.2f}...\n")  # Kein Header!
  ```
  - **Problem**: CSV ohne Header schwer zu interpretieren
  - **Lösung**: Erste Zeile mit Spaltennamen

- **Fehler**: Leerzeichen in CSV
  ```python
  datei.write(f"{zeit}, {temp:.2f}, {druck:.2f}\n")  # Leerzeichen!
  ```
  - **Problem**: Manche CSV-Parser interpretieren Leerzeichen als Teil des Werts
  - **Lösung**: Keine Leerzeichen nach Kommas

- **Fehler**: Division durch Null bei leerem Datensatz
  ```python
  durchschnitt = summe / len(daten)  # Was wenn len(daten) == 0?
  ```
  - **Lösung**: Prüfung `if len(daten) > 0:` vor Division

- **Fehler**: Initialisierung von Min mit 0
  ```python
  temp_min = 0  # Falsch, wenn alle Temperaturen > 0
  ```
  - **Problem**: Wenn alle echten Werte größer als 0 sind, bleibt temp_min bei 0
  - **Lösung**: Initialisierung mit erstem Wert: `temp_min = daten[0][1]`

