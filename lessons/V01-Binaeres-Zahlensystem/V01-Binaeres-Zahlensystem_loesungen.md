# V01: Lösungen - Binäres Zahlensystem

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: Zahlensystem-Umrechnung

**Lösung**:

**a) 13₁₀ → Binär**

Divisionsverfahren:
```
13 : 2 = 6 Rest 1  ↑
 6 : 2 = 3 Rest 0  |
 3 : 2 = 1 Rest 1  |
 1 : 2 = 0 Rest 1  |
```

Reste von unten nach oben: **1101₂**

**b) 1101₂ → Dezimal**

$$1101_2 = 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$$
$$= 8 + 4 + 0 + 1 = 13_{10}$$

**Ergebnis**: **13₁₀**

**c) 2A₁₆ → Binär**

Ziffernweise Umwandlung:
- 2₁₆ = 0010₂
- A₁₆ = 1010₂

**Ergebnis**: **00101010₂** (oder kürzer: **101010₂**)

**d) 11111111₂ → Hexadezimal**

Gruppiere in 4er-Blöcke von rechts:
- 1111₂ = F₁₆
- 1111₂ = F₁₆

**Ergebnis**: **FF₁₆**

**Erklärung**:

Die Umrechnung zwischen verschiedenen Zahlensystemen basiert auf dem Stellenwertsystem-Prinzip. Bei der Umrechnung von Dezimal zu Binär nutzen wir wiederholte Division, weil jede Division durch 2 uns sagt, ob an der aktuellen Stelle eine 1 oder 0 steht (Rest 1 oder 0).

Die Umrechnung zwischen Hexadezimal und Binär ist besonders einfach, weil 16 = 2⁴. Jede Hexadezimalziffer entspricht exakt 4 Binärziffern. Diese Eigenschaft macht Hexadezimal sehr praktisch für die kompakte Darstellung von Binärdaten.

**Häufige Fehler**:
- **Reste in falscher Reihenfolge lesen**: Bei der Division-durch-2-Methode müssen die Reste von unten nach oben gelesen werden
- **Vergessen, führende Nullen bei Hex→Binär zu ergänzen**: Jede Hex-Ziffer muss zu genau 4 Bits werden (z.B. 2 = 0010, nicht 10)
- **Zweierpotenz falsch zuordnen**: Bei Binär→Dezimal immer von rechts mit 2⁰ beginnen

---

### Lösung T2: Binäre Addition und Subtraktion

**Lösung**:

**a) 10110₂ + 1101₂**

```
  Übertrag:  ¹ ¹
            1 0 1 1 0
          +   1 1 0 1
          -----------
          1 0 0 0 1 1
```

Schritt für Schritt von rechts:
- Position 0: 0 + 1 = 1
- Position 1: 1 + 0 = 1
- Position 2: 1 + 1 = 0, Übertrag 1
- Position 3: 0 + 1 + Übertrag 1 = 0, Übertrag 1
- Position 4: 1 + 0 + Übertrag 1 = 0, Übertrag 1
- Position 5: Übertrag 1

**Ergebnis**: **100011₂**

**Probe (dezimal)**: 22₁₀ + 13₁₀ = 35₁₀ = 100011₂ ✓

**b) 11001₂ + 10111₂**

```
  Übertrag: ¹¹¹¹¹
            1 1 0 0 1
          + 1 0 1 1 1
          -----------
          1 1 0 0 0 0
```

**Ergebnis**: **110000₂**

**Probe (dezimal)**: 25₁₀ + 23₁₀ = 48₁₀ = 110000₂ ✓

**c) 10110₂ - 1101₂**

```
  Borgen:     ¹ ¹
            1 0 1 1 0
          -   1 1 0 1
          -----------
              1 0 0 1
```

Schritt für Schritt von rechts:
- Position 0: 0 - 1 = braucht Borgen → 10₂ - 1 = 1
- Position 1: 1 (nach Borgen 0) - 0 = braucht erneut Borgen → 10₂ - 0 = 0
- Position 2: 1 (nach Borgen 0) - 1 = braucht Borgen → 10₂ - 1 = 1
- Position 3: 0 (nach Borgen entfällt)
- Position 4: 1 bleibt → 1

**Ergebnis**: **1001₂**

**Probe (dezimal)**: 22₁₀ - 13₁₀ = 9₁₀ = 1001₂ ✓

**d) 100000₂ - 10101₂**

```
  Borgen:  ¹¹¹¹¹
           1 0 0 0 0 0
         -   1 0 1 0 1
         -------------
             0 1 0 1 1
```

**Ergebnis**: **01011₂** (oder kurz: **1011₂**)

**Probe (dezimal)**: 32₁₀ - 21₁₀ = 11₁₀ = 1011₂ ✓

**Erklärung**:

Die binäre Addition funktioniert genau wie die dezimale Addition: Wir addieren stellenweise von rechts nach links und erzeugen bei Summen ≥ 2 einen Übertrag. Die Regel "1 + 1 = 10₂" bedeutet: Ergebnis 0, Übertrag 1 zur nächsten Stelle.

Bei der Subtraktion müssen wir "borgen", wenn wir 1 von 0 subtrahieren müssen. Beim Borgen wird aus einer 0 eine 10₂ (dezimal 2), wovon wir dann subtrahieren können. Die Stelle, von der wir geborgt haben, verringert sich um 1.

**Lösungsweg Schritt für Schritt**:

1. Beginne bei der rechtesten Stelle
2. Addition: Addiere die Ziffern plus eventuelle Überträge; bei Summe ≥ 2 erzeuge Übertrag
3. Subtraktion: Wenn Minuend < Subtrahend, borge von der nächsten Stelle
4. Arbeite dich nach links durch
5. Überprüfe das Ergebnis durch Rückrechnung in Dezimal

**Häufige Fehler**:
- **Übertrag vergessen**: Bei 1 + 1 = 10₂ muss der Übertrag zur nächsten Stelle weitergegeben werden
- **Borgen-Kette nicht richtig verfolgt**: Wenn mehrere aufeinanderfolgende Nullen stehen, muss man mehrfach borgen
- **Führende Nullen vergessen**: Das Ergebnis sollte ohne führende Nullen angegeben werden (außer bei fester Bit-Breite)

---

### Lösung T3: Zweierkomplement und negative Zahlen

**Lösung**:

**a) Zweierkomplement bilden**

**42₁₀ → Zweierkomplement (negativ)**

1. Positive Darstellung: 42₁₀ = 00101010₂
2. Alle Bits invertieren: 11010101₂
3. 1 addieren: 11010101₂ + 1₂ = 11010110₂

**Ergebnis**: **11010110₂** repräsentiert **-42**

**127₁₀ → Zweierkomplement (negativ)**

1. Positive Darstellung: 127₁₀ = 01111111₂
2. Alle Bits invertieren: 10000000₂
3. 1 addieren: 10000000₂ + 1₂ = 10000001₂

**Ergebnis**: **10000001₂** repräsentiert **-127**

**b) Zweierkomplement → Dezimal**

**10110110₂**

MSB (höchstwertiges Bit) = 1 → negative Zahl

Zweierkomplement bilden um Betrag zu finden:
1. Invertieren: 01001001₂
2. Plus 1: 01001010₂ = 64 + 8 + 2 = 74₁₀

**Ergebnis**: **-74₁₀**

**11111111₂**

MSB = 1 → negative Zahl

Zweierkomplement bilden:
1. Invertieren: 00000000₂
2. Plus 1: 00000001₂ = 1₁₀

**Ergebnis**: **-1₁₀**

**10000000₂**

MSB = 1 → negative Zahl

Dies ist ein Spezialfall! Zweierkomplement bilden:
1. Invertieren: 01111111₂
2. Plus 1: 10000000₂ (wieder die Ausgangszahl!)

Das ist die kleinste darstellbare Zahl bei 8 Bit.

**Ergebnis**: **-128₁₀**

**c) Subtraktion durch Addition mit Zweierkomplement: 50₁₀ - 30₁₀**

**Schritt 1**: Beide Zahlen binär darstellen
- 50₁₀ = 00110010₂
- 30₁₀ = 00011110₂

**Schritt 2**: Zweierkomplement von 30 bilden (um -30 zu erhalten)
- Invertieren: 11100001₂
- Plus 1: 11100010₂ (das ist -30)

**Schritt 3**: Addition durchführen
```
  Übertrag: ¹¹¹  ¹¹¹
            0 0 1 1 0 0 1 0  (50)
          + 1 1 1 0 0 0 1 0  (-30)
          -------------------
         (1)0 0 0 1 0 1 0 0  (20)
```

**Schritt 4**: Überlauf ignorieren
Der 9. Bit (Überlauf) wird bei 8-Bit-Arithmetik ignoriert.

**Ergebnis**: **00010100₂ = 20₁₀** ✓

**d) Wertebereich bei 8-Bit Zweierkomplement**

**Kleinster Wert**: **-128₁₀** (binär: 10000000₂)
**Größter Wert**: **+127₁₀** (binär: 01111111₂)

**Begründung**:

Mit n Bits können wir 2ⁿ verschiedene Werte darstellen. Bei 8 Bit sind das 2⁸ = 256 Werte.

Im Zweierkomplement:
- MSB = 0: positive Zahlen (und Null)
- MSB = 1: negative Zahlen

Mit 7 verbleibenden Bits für die positive Seite:
- Positive Zahlen: 0 bis 2⁷ - 1 = 0 bis 127 (128 Werte inkl. 0)

Mit 8 Bits für die negative Seite (MSB = 1):
- Negative Zahlen: -1 bis -2⁷ = -1 bis -128 (128 Werte)

Formel: Von **-2^(n-1)** bis **2^(n-1) - 1**

Bei 8 Bit: -2⁷ bis 2⁷ - 1 = **-128 bis +127**

**Erklärung**:

Das Zweierkomplement ist die Standard-Methode zur Darstellung negativer Zahlen in Computern, weil es die Subtraktion durch Addition ersetzt. Die Hardware muss nur einen Addierer implementieren, keinen separaten Subtrahierer. Das spart Transistoren und Energie.

Ein besonderer Aspekt: Der Wertebereich ist asymmetrisch. Es gibt eine negative Zahl mehr als positive Zahlen (-128 existiert, aber +128 nicht bei 8 Bit). Das liegt daran, dass die 0 bei den positiven Zahlen mitgezählt wird.

**Lösungsweg Schritt für Schritt**:

1. **Positive Zahl → Zweierkomplement**: Binär darstellen, invertieren, 1 addieren
2. **Zweierkomplement → Dezimal**: MSB prüfen; wenn 1: Zweierkomplement bilden, Betrag berechnen, negieren
3. **Subtraktion**: Subtrahenden negieren (Zweierkomplement), dann addieren
4. **Wertebereich**: Formel -2^(n-1) bis 2^(n-1) - 1 anwenden

**Alternative Lösungsansätze**:

**Für das Bilden des Zweierkomplements gibt es auch die "erste 1 von rechts beibehalten"-Methode**:
- Von rechts nach links kopieren bis einschließlich der ersten 1
- Alle weiteren Bits invertieren

Beispiel für 42 = 00101010₂:
- Von rechts: 0 kopieren → 0
- 1 kopieren (erste 1) → 10
- Rest invertieren: 00101 → 11010
- Ergebnis: 11010110₂ (identisch zur vorherigen Methode)

**Häufige Fehler**:
- **Vergessen, 1 zu addieren**: Nur invertieren reicht nicht, man muss auch 1 addieren
- **Bei Zweierkomplement → Dezimal falsch vorgehen**: Man muss das Zweierkomplement erneut bilden, um den Betrag zu bekommen
- **Überlauf nicht ignorieren**: Bei fester Bit-Breite wird der Überlauf abgeschnitten
- **Wertebereich verwechseln**: Bei n Bit ist der Bereich NICHT -2ⁿ bis +2ⁿ, sondern -2^(n-1) bis 2^(n-1) - 1

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: Maschinendatenerfassung

**Vollständiger Code**:
```python
# Maschinendatenerfassung mit Wartungsplanung

# Maschinenbezeichnung einlesen
bezeichnung = input("Maschinenbezeichnung: ")

# Betriebsstunden einlesen
betriebsstunden_text = input("Aktuelle Betriebsstunden: ")
betriebsstunden = int(betriebsstunden_text)

# Nächste Wartung berechnen (alle 500 Betriebsstunden)
naechste_wartung = betriebsstunden + 500

# Protokoll ausgeben
print("--- Betriebsprotokoll ---")
print("Maschine:", bezeichnung)
print("Betriebsstunden:", betriebsstunden, "h")
print("Nächste Wartung bei:", naechste_wartung, "h")
```

**Kompaktere Version**:
```python
# Maschinendatenerfassung - kompakt

bezeichnung = input("Maschinenbezeichnung: ")
betriebsstunden = int(input("Aktuelle Betriebsstunden: "))

print("--- Betriebsprotokoll ---")
print("Maschine:", bezeichnung)
print("Betriebsstunden:", betriebsstunden, "h")
print("Nächste Wartung bei:", betriebsstunden + 500, "h")
```

**Erklärung**:

Das Programm demonstriert die typische Datenerfassung in der Industrie 4.0 – Maschinendaten werden digital protokolliert, um Wartungsintervalle zu planen und Ausfallzeiten zu minimieren.

**Zeile für Zeile**:
1. Wir lesen die Maschinenbezeichnung als String ein (z.B. "CNC-Fräse-001")
2. Wir lesen die Betriebsstunden ein und konvertieren sie mit `int()` in eine Ganzzahl
3. Wir berechnen, wann die nächste Wartung fällig ist (aktuell + 500h)
4. Wir geben ein strukturiertes Protokoll aus

**Maschinenbau-Kontext**:

In der Praxis würden solche Daten oft automatisch von Sensoren erfasst und in einer Datenbank gespeichert. Regelmäßige Wartung basierend auf Betriebsstunden ist entscheidend für:
- Vermeidung ungeplanter Ausfälle
- Optimierung der Anlagennutzung
- Einhaltung von Sicherheitsvorschriften
- Verlängerung der Maschinenlebensdauer

**Warum diese Lösung?**

Die kompaktere Version zeigt einen häufig verwendeten Python-Pattern: Die Konvertierung direkt im `input()`-Aufruf durchführen. Das spart eine Zeile Code und eine Variable.

**Häufige Fehler**:
- **Fehler**: Vergessen, `int()` zu verwenden
  - **Warum falsch**: `input()` gibt immer einen String zurück. "2340" + 500 führt zu einem TypeError
  - **Richtig**: `betriebsstunden = int(input("Betriebsstunden: "))`

- **Fehler**: Wartungsintervall falsch berechnet
  - **Warum falsch**: `naechste_wartung = 500` wäre ein fixer Wert, nicht relativ zu aktuellen Stunden
  - **Richtig**: `naechste_wartung = betriebsstunden + 500`

---

### Lösung P2: Drehzahl-Umrechner

**Vollständiger Code**:
```python
# Drehzahl-Umrechner: U/min ↔ rad/s

pi = 3.14159265359

print("=== Drehzahl-Umrechner für Werkzeugmaschinen ===")

# Drehzahl in U/min einlesen
drehzahl_upm = float(input("Drehzahl in U/min: "))

# Umrechnung U/min → rad/s
# Formel: rad/s = U/min × 2π / 60
winkelgeschwindigkeit = drehzahl_upm * 2 * pi / 60

# Ergebnisse ausgeben
print(drehzahl_upm, "U/min entspricht", round(winkelgeschwindigkeit, 2), "rad/s")

# Kontrolle: Rückrechnung rad/s → U/min
kontrolle = winkelgeschwindigkeit * 60 / (2 * pi)
print("Kontrolle:", round(winkelgeschwindigkeit, 2), "rad/s =", round(kontrolle, 2), "U/min")
```

**Erweiterte Version mit besserer Formatierung**:
```python
# Geschwindigkeits-Umrechner: km/h ↔ m/s (erweitert)

print("=== Geschwindigkeits-Umrechner ===")
print()

# Geschwindigkeit in km/h einlesen
geschwindigkeit_kmh = float(input("Geschwindigkeit in km/h: "))

# Umrechnung km/h → m/s (Formel: km/h / 3.6)
# Erklärung: 1 km/h = 1000m / 3600s = 1/3.6 m/s
geschwindigkeit_ms = geschwindigkeit_kmh / 3.6

# Ergebnisse ausgeben
print()
print("Ergebnisse:")
print("-----------")
print(geschwindigkeit_kmh, "km/h =", geschwindigkeit_ms, "m/s")

# Rückrechnung zur Kontrolle (Formel: m/s * 3.6)
print(geschwindigkeit_ms, "m/s =", geschwindigkeit_ms * 3.6, "km/h")
```

**Erklärung**:

Die Umrechnung von Drehzahl (U/min) zu Winkelgeschwindigkeit (rad/s) ist fundamental für die Maschinenauslegung. Die Formel ergibt sich aus:

$$\omega = \frac{2\pi n}{60} = \frac{2\pi \cdot \text{U/min}}{60 \text{ s/min}}$$

**Maschinenbau-Kontext**:

Winkelgeschwindigkeit in rad/s wird benötigt für:
- Berechnung von Umfangsgeschwindigkeiten: v = ω × r
- Dynamische Analysen (Beschleunigung, Kräfte)
- Motorsteuerung und Regelungstechnik
- Schwingungsanalysen

**Schritt-für-Schritt Durchlauf**:

Eingabe: `1500 U/min`

1. `drehzahl_upm` wird zu `1500.0` (float)
2. `winkelgeschwindigkeit = 1500 * 2 * 3.14159... / 60` ≈ `157.08 rad/s`
3. Ausgabe: "1500 U/min entspricht 157.08 rad/s"
4. Kontrolle: `157.08 * 60 / (2 * π)` ≈ `1500.0 U/min` ✓

**Häufige Fehler**:
- **Fehler**: Formel falsch anwenden (z.B. nur durch 60 teilen ohne 2π)
  - **Warum falsch**: Eine vollständige Umdrehung = 2π Radiant, nicht nur π
  - **Richtig**: `omega = n * 2 * pi / 60`

- **Fehler**: Pi-Wert zu ungenau (z.B. nur 3.14 verwenden)
  - **Warum falsch**: Bei hohen Drehzahlen führt dies zu merklichen Abweichungen
  - **Richtig**: Mindestens 6 Nachkommastellen: `pi = 3.14159265359`

- **Fehler**: Einheiten verwechseln (rad/s vs. °/s)
  - **Warum falsch**: 1 rad/s ≠ 1 °/s (1 rad ≈ 57.3°)
  - **Richtig**: Immer rad/s für Winkelgeschwindigkeit in technischen Berechnungen verwenden

---

### Lösung P3: Materialspannungs-Rechner

**Vollständiger Code**:
```python
# Materialspannungs-Rechner für Zugstab

print("=== Materialspannungs-Rechner ===")

# Kraft und Querschnittsfläche einlesen
kraft = float(input("Kraft F (in N): "))
flaeche = float(input("Querschnittsfläche A (in mm²): "))

# Normalspannung berechnen (in N/mm²  = MPa)
spannung_mpa = kraft / flaeche

# Umrechnung in Pascal (1 N/mm² = 1.000.000 Pa)
spannung_pa = spannung_mpa * 1000000

# Ergebnisse ausgeben
print()
print("Berechnungsergebnisse:")
print("Normalspannung σ =", spannung_mpa, "N/mm² (MPa)")
print("Normalspannung σ =", spannung_pa, "Pa")
print("Normalspannung σ =", spannung_mpa, "MPa")
```

**Erklärung**:

Das Programm berechnet die mechanische Normalspannung σ (Sigma) in einem belasteten Bauteil. Dies ist eine fundamentale Berechnung im Maschinenbau zur Festigkeitsbewertung.

**Maschinenbau-Kontext**:

Die Normalspannung beschreibt die Belastung eines Materials unter Zugkraft:
- **Formel**: σ = F / A (Kraft pro Fläche)
- **Einheiten**: 1 N/mm² = 1 MPa = 10⁶ Pa
- **Anwendung**: Dimensionierung von Bauteilen, Festigkeitsnachweise, Materialauswahl

Typische Werte:
- Baustahl S235: Streckgrenze ≈ 235 MPa
- Aluminium AlMg3: Zugfestigkeit ≈ 250 MPa
- Beton: Druckfestigkeit ≈ 30-50 MPa

**Konzepte in dieser Lösung**:
- **Float-Arithmetik**: Division von Gleitkommazahlen
- **Einheitenumrechnung**: Skalierung von MPa zu Pa
- **Formatierte Ausgabe**: Strukturierte Ergebnisdarstellung

**Häufige Fehler**:
- **Fehler**: Einheiten verwechseln (N und kN, mm² und m²)
  - **Warum falsch**: 1 kN = 1000 N, 1 m² = 1.000.000 mm²
  - **Richtig**: Immer konsistente Einheiten verwenden oder explizit umrechnen

- **Fehler**: Division durch 0 bei Flächeneingabe
  - **Warum falsch**: Führt zu `ZeroDivisionError`
  - **Richtig**: Validierung der Eingabe (wird in V09 mit try-except behandelt)

---

### Lösung P4: Binär-Sensor-Dekoder

**Vollständiger Code mit Maschinenstatus-Interpretation**:
```python
# Binär-Sensor-Dekoder für Maschinen-Statuscode

print("=== Binär-Sensor-Dekoder ===")
binaer = input("Gib den 8-Bit-Statuscode ein: ")

# Dezimalwert berechnen
laenge = len(binaer)
dezimal = 0

print()
print("Berechnung:")

position = 0
while position < laenge:
    ziffer = int(binaer[position])
    potenz = laenge - position - 1
    zweierpotenz = 2 ** potenz
    beitrag = ziffer * zweierpotenz
    
    print(f"Bit {potenz}: {ziffer} * {zweierpotenz} = {beitrag}")
    
    dezimal += beitrag
    position += 1

print()
print(f"Summe: {dezimal}")
print(f"Der Statuscode {binaer} entspricht dem Dezimalwert {dezimal}")

# Status-Interpretation (Bits von rechts)
print()
print("Status-Interpretation:")
bit0 = int(binaer[7])  # Motor
bit1 = int(binaer[6])  # Kühlmittel
bit2 = int(binaer[5])  # Notaus
bit3 = int(binaer[4])  # Tür

print("- Motor:", "LÄUFT" if bit0 == 1 else "STEHT")
print("- Kühlmittel:", "AKTIV" if bit1 == 1 else "INAKTIV")
print("- Notaus:", "AKTIV (!)" if bit2 == 1 else "NORMAL")
print("- Tür:", "OFFEN" if bit3 == 1 else "GESCHLOSSEN")

# Fehlercode aus Bits 4-7 extrahieren
fehlercode = int(binaer[0:4], 2)
print(f"- Fehlercode: {fehlercode} (Binär: {binaer[0:4]})")
```

**Maschinenbau-Kontext**:

In der Automatisierungstechnik werden Maschinenzustände oft als Bit-Felder (Status-Bytes) übertragen:
- **Kompakt**: 8 Zustände in 1 Byte
- **Schnell**: Bitweise Verarbeitung durch Mikrocontroller
- **Standard**: Modbus, Profibus, CANopen nutzen Statusregister

**Erklärung**: Dieses Programm zeigt die Dekodierung von Maschinensensordaten – ein reales Szenario in SPS-Programmierung und Industrie 4.0.

---

### Lösung P5: Kreisberechnungs-Programm

**Vollständiger Code**:
```python
# Umfassendes Kreisberechnungs-Programm

# Konstante Pi definieren
pi = 3.14159265359

print("=== Kreisberechnungs-Programm ===")
print()
print("Wähle eine Option:")
print("1. Radius gegeben")
print("2. Durchmesser gegeben")
print("3. Umfang gegeben")
print("4. Fläche gegeben")
print()

# Benutzerauswahl einlesen
wahl = input("Deine Wahl: ")

# Je nach Wahl unterschiedlich verarbeiten
# Wir müssen alle vier Fälle einzeln behandeln

if wahl == "1":
    # Fall 1: Radius gegeben
    radius = float(input("Gib den Radius ein (in cm): "))
    
    # Alle anderen Werte berechnen
    durchmesser = 2 * radius
    umfang = 2 * pi * radius
    flaeche = pi * radius * radius
    
    # Ergebnisse ausgeben
    print()
    print("Ergebnisse für einen Kreis mit Radius", radius, "cm:")
    print("- Durchmesser:", durchmesser, "cm")
    print("- Umfang:", umfang, "cm")
    print("- Fläche:", flaeche, "cm²")

elif wahl == "2":
    # Fall 2: Durchmesser gegeben
    durchmesser = float(input("Gib den Durchmesser ein (in cm): "))
    
    # Radius berechnen, dann alles andere
    radius = durchmesser / 2
    umfang = pi * durchmesser  # Alternative: 2 * pi * radius
    flaeche = pi * radius * radius
    
    # Ergebnisse ausgeben
    print()
    print("Ergebnisse für einen Kreis mit Durchmesser", durchmesser, "cm:")
    print("- Radius:", radius, "cm")
    print("- Umfang:", umfang, "cm")
    print("- Fläche:", flaeche, "cm²")

elif wahl == "3":
    # Fall 3: Umfang gegeben
    umfang = float(input("Gib den Umfang ein (in cm): "))
    
    # Aus Umfang = 2*pi*r folgt: r = Umfang / (2*pi)
    radius = umfang / (2 * pi)
    durchmesser = 2 * radius
    flaeche = pi * radius * radius
    
    # Ergebnisse ausgeben
    print()
    print("Ergebnisse für einen Kreis mit Umfang", umfang, "cm:")
    print("- Radius:", radius, "cm")
    print("- Durchmesser:", durchmesser, "cm")
    print("- Fläche:", flaeche, "cm²")

elif wahl == "4":
    # Fall 4: Fläche gegeben
    flaeche = float(input("Gib die Fläche ein (in cm²): "))
    
    # Aus Fläche = pi*r² folgt: r = sqrt(Fläche / pi)
    # sqrt müssen wir manuell berechnen (oder ** 0.5 verwenden)
    # r² = Fläche / pi
    # r = (Fläche / pi) ** 0.5
    radius = (flaeche / pi) ** 0.5
    durchmesser = 2 * radius
    umfang = 2 * pi * radius
    
    # Ergebnisse ausgeben
    print()
    print("Ergebnisse für einen Kreis mit Fläche", flaeche, "cm²:")
    print("- Radius:", radius, "cm")
    print("- Durchmesser:", durchmesser, "cm")
    print("- Umfang:", umfang, "cm")

else:
    # Ungültige Eingabe
    print("Ungültige Wahl! Bitte 1, 2, 3 oder 4 eingeben.")
```

**Hinweis**: Dieses Programm verwendet `if-elif-else`, was offiziell erst in V05 behandelt wird. Für motivierte Studierende ist dies eine gute Herausforderung zum Vorauslernen.

**Vereinfachte Version ohne if-elif (nur Radius-Eingabe)**:
```python
# Kreisberechnungs-Programm (vereinfacht: nur Radius-Eingabe)

pi = 3.14159265359

print("=== Kreisberechnungs-Programm ===")
print()

# Radius vom Benutzer einlesen
radius = float(input("Gib den Radius ein (in cm): "))

# Eingaben einlesen
uebersetzung = float(input("Gib das Übersetzungsverhältnis i ein: "))
n1 = float(input("Gib die Antriebsdrehzahl n₁ ein (U/min): "))
m1 = float(input("Gib das Antriebsmoment M₁ ein (Nm): "))
eta = float(input("Gib den Wirkungsgrad η ein (0-1): "))

# Berechnungen
n2 = n1 / uebersetzung  # Abtriebsdrehzahl
m2 = m1 * uebersetzung * eta  # Abtriebsmoment
leistungsverlust = (1 - eta) * 100  # in Prozent

# Ergebnisse ausgeben
print()
print(f"Ergebnisse für ein Getriebe mit i = {uebersetzung}:")
print(f"- Abtriebsdrehzahl n₂: {round(n2, 2)} U/min")
print(f"- Abtriebsmoment M₂: {round(m2, 2)} Nm")
print(f"- Leistungsverlust: {leistungsverlust} %")

# Bonus: Warnung bei hohem Moment
m2_max = 200  # Maximales zulässiges Moment in Nm
if m2 > m2_max:
    print(f"⚠️ WARNUNG: Abtriebsmoment ({round(m2, 2)} Nm) überschreitet zulässiges Maximum ({m2_max} Nm)!")
```

**Maschinenbau-Kontext**:

Getriebe sind zentrale **Maschinenelemente** zur Drehmoment- und Drehzahlwandlung. Diese Berechnungen sind fundamental für jeden Maschinenbau-Ingenieur:

**Übersetzungsverhältnis**:
- **i < 1**: Übersetzung ins Schnelle (Drehzahl ↑, Moment ↓)
- **i > 1**: Übersetzung ins Langsame (Drehzahl ↓, Moment ↑)
- **i = 1**: Durchlaufgetriebe (keine Wandlung)

**Wichtige Formeln**:
- Übersetzungsverhältnis: i = n₁/n₂ = z₂/z₁ (Zähnezahlen)
- Abtriebsdrehzahl: n₂ = n₁/i
- Abtriebsmoment: M₂ = M₁ × i × η
- Leistung bleibt (theoretisch) gleich: P₁ = P₂ (mit Verlusten: P₂ = P₁ × η)

**Wirkungsgrad**:
- Gut geschmierte Stirnradgetriebe: η ≈ 0.95-0.98
- Schneckengetriebe: η ≈ 0.5-0.9 (höhere Reibung)
- Planetengetriebe: η ≈ 0.97-0.99 (sehr effizient)

**Praktische Anwendung**:

Elektromotoren liefern typischerweise hohe Drehzahl (z.B. 1500 oder 3000 U/min) aber relativ niedriges Moment. Für Förderbänder, Kräne oder Werkzeugmaschinen benötigt man jedoch oft niedrige Drehzahl und hohes Moment → Getriebe wandelt optimal um.

**Bonus-Funktionalität**: Die Warnung prüft, ob das berechnete Abtriebsmoment die zulässige Grenze überschreitet (Überlastschutz). Dies ist kritisch für Betriebssicherheit, da Überlastung zu Zahnbruch, Lagerschäden oder frühzeitigem Verschleiß führen kann.
**Bonus-Funktionalität**: Die Warnung prüft, ob das berechnete Abtriebsmoment die zulässige Grenze überschreitet (Überlastschutz). Dies ist kritisch für Betriebssicherheit, da Überlastung zu Zahnbruch, Lagerschäden oder frühzeitigem Verschleiß führen kann.

---

## ✅ V01 abgeschlossen!

**Zusammenfassung**:
- Alle Python-Aufgaben (P1-P5) haben Maschinenbau-Kontext
- Lösungen mit technischen Erklärungen und Formeln
- Keine externen Testdaten erforderlich (interaktive Programme)
