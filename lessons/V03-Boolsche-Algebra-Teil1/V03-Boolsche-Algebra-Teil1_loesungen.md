# V03: Lösungen - Boolsche Algebra & Variablen Management

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: Wahrheitstabellen für einfache Ausdrücke

**Lösung**:

**a) A ∧ B** (AND-Operator)

Anzahl Zeilen: $2^2 = 4$ (zwei Variablen)

| A | B | A ∧ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

**b) A ∨ B** (OR-Operator)

Anzahl Zeilen: $2^2 = 4$ (zwei Variablen)

| A | B | A ∨ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   1   |

**c) ¬A** (NOT-Operator)

Anzahl Zeilen: $2^1 = 2$ (eine Variable)

| A | ¬A |
|---|----|
| 0 | 1  |
| 1 | 0  |

**d) A ∧ ¬B** (AND mit negiertem B)

Anzahl Zeilen: $2^2 = 4$ (zwei Variablen)

| A | B | ¬B | A ∧ ¬B |
|---|---|----|--------|
| 0 | 0 | 1  |   0    |
| 0 | 1 | 0  |   0    |
| 1 | 0 | 1  |   1    |
| 1 | 1 | 0  |   0    |

**Erklärung**:

Bei Aufgabe d) muss man schrittweise vorgehen:
1. Zuerst die Eingangskombinationen für A und B aufschreiben (4 Zeilen)
2. Dann ¬B berechnen (Negation von B)
3. Schließlich A ∧ ¬B berechnen (AND-Verknüpfung von A mit ¬B)

Das Ergebnis ist nur in der dritten Zeile wahr (A=1, B=0), weil dann sowohl A wahr ist als auch ¬B wahr ist (da B falsch ist).

**Häufige Fehler**:
- **Vergessen der Zwischenspalte**: Bei zusammengesetzten Ausdrücken wie `A ∧ ¬B` hilft es, eine Zwischenspalte für `¬B` anzulegen.
- **Falsche Zeilenzahl**: Bei $n$ Variablen immer $2^n$ Zeilen erstellen, nicht mehr und nicht weniger.
- **Unsystematisches Auflisten**: Die Eingangskombinationen sollten systematisch aufgezählt werden (wie beim Binärzählen: 00, 01, 10, 11).

---

### Lösung T2: Zusammengesetzte logische Ausdrücke

**Lösung**:

**a) Wahrheitstabelle für (A ∧ B) ∨ (¬C)**

Anzahl Zeilen: $2^3 = 8$ (drei Variablen)

| A | B | C | A ∧ B | ¬C | (A ∧ B) ∨ (¬C) |
|---|---|---|-------|----| ---------------|
| 0 | 0 | 0 |   0   | 1  |       1        |
| 0 | 0 | 1 |   0   | 0  |       0        |
| 0 | 1 | 0 |   0   | 1  |       1        |
| 0 | 1 | 1 |   0   | 0  |       0        |
| 1 | 0 | 0 |   0   | 1  |       1        |
| 1 | 0 | 1 |   0   | 0  |       0        |
| 1 | 1 | 0 |   1   | 1  |       1        |
| 1 | 1 | 1 |   1   | 0  |       1        |

**b) Interpretation in natürlicher Sprache**

Der Ausdruck `(A ∧ B) ∨ (¬C)` ist wahr, wenn **mindestens eine** der folgenden Bedingungen erfüllt ist:
- Sowohl A **als auch** B sind wahr (erste Klammer: `A ∧ B`)
- C ist **nicht** wahr (zweite Klammer: `¬C`)

Anders formuliert: Der Ausdruck ist **nur dann falsch**, wenn:
- C wahr ist **UND**
- mindestens einer von A oder B falsch ist

**c) Schaltungsdiagramm**

```
    A ────┐
          │╲
          │ ╲──────┐
          │  ╱     │)
    B ────┘╱       │ )
                   │  )───── (A ∧ B) ∨ (¬C)
              ┌─○──┤ )
    C ────────┘    │)
                   
Legende:
- AND-Gatter (für A ∧ B)
- NOT-Gatter (für ¬C, symbolisiert durch Kreis ○)
- OR-Gatter (verbindet beide Zwischenergebnisse)
```

**Erklärung**:

**Lösungsweg Schritt für Schritt**:
1. **Eingänge identifizieren**: A, B und C sind die drei Eingangssignale
2. **Zwischenergebnis 1 berechnen**: `A ∧ B` wird durch ein AND-Gatter mit Eingängen A und B realisiert
3. **Zwischenergebnis 2 berechnen**: `¬C` wird durch ein NOT-Gatter (Inverter) mit Eingang C realisiert
4. **Endergebnis**: Beide Zwischenergebnisse werden mit einem OR-Gatter verknüpft

Die Wahrheitstabelle zeigt, dass der Ausdruck in 5 von 8 Fällen wahr ist (Zeilen 1, 3, 5, 7, 8). Das bedeutet, diese logische Funktion ist häufiger wahr als falsch.

**Häufige Fehler**:
- **Reihenfolge vertauschen**: `(A ∧ B) ∨ (¬C)` ist **nicht** dasselbe wie `(A ∨ B) ∧ (¬C)`. Klammern und Operatoren-Reihenfolge sind entscheidend!
- **NOT-Gatter vergessen**: ¬C benötigt ein eigenes NOT-Gatter vor dem OR-Gatter.
- **Zwischenschritte überspringen**: Berechne immer zuerst die Klammern (Zwischenergebnisse), bevor du die Hauptoperation durchführst.

---

### Lösung T3: Äquivalenz logischer Ausdrücke

**Lösung**:

**a) Logische Funktion formulieren**

Aus der Aufgabenstellung:
- **Not-Aus nicht gedrückt**: ¬N (Negation von N)
- **Entweder Schutztür geschlossen ODER Wartungsmodus**: T ∨ W
- **Startknopf gedrückt**: S

Alle drei Bedingungen müssen **gleichzeitig** erfüllt sein (UND-Verknüpfung):

**Logische Funktion**: 
$$M = (\neg N) \land (T \lor W) \land S$$

Oder in alternativer Schreibweise:
$$M = \overline{N} \cdot (T + W) \cdot S$$

**b) Vollständige Wahrheitstabelle**

Bei 4 Variablen (N, T, W, S): $2^4 = 16$ Zeilen

| N | T | W | S | ¬N | T ∨ W | (¬N) ∧ (T ∨ W) | M = (¬N) ∧ (T ∨ W) ∧ S |
|---|---|---|---|----| ------|----------------|------------------------|
| 0 | 0 | 0 | 0 | 1  |   0   |       0        |           0            |
| 0 | 0 | 0 | 1 | 1  |   0   |       0        |           0            |
| 0 | 0 | 1 | 0 | 1  |   1   |       1        |           0            |
| 0 | 0 | 1 | 1 | 1  |   1   |       1        |        **1**           |
| 0 | 1 | 0 | 0 | 1  |   1   |       1        |           0            |
| 0 | 1 | 0 | 1 | 1  |   1   |       1        |        **1**           |
| 0 | 1 | 1 | 0 | 1  |   1   |       1        |           0            |
| 0 | 1 | 1 | 1 | 1  |   1   |       1        |        **1**           |
| 1 | 0 | 0 | 0 | 0  |   0   |       0        |           0            |
| 1 | 0 | 0 | 1 | 0  |   0   |       0        |           0            |
| 1 | 0 | 1 | 0 | 0  |   1   |       0        |           0            |
| 1 | 0 | 1 | 1 | 0  |   1   |       0        |           0            |
| 1 | 1 | 0 | 0 | 0  |   1   |       0        |           0            |
| 1 | 1 | 0 | 1 | 0  |   1   |       0        |           0            |
| 1 | 1 | 1 | 0 | 0  |   1   |       0        |           0            |
| 1 | 1 | 1 | 1 | 0  |   1   |       0        |           0            |

**Die Maschine startet nur in 3 von 16 Fällen** (markiert mit **1**):
- Zeile 4: N=0, T=0, W=1, S=1 (Not-Aus nicht gedrückt, Wartungsmodus aktiv, Start gedrückt)
- Zeile 6: N=0, T=1, W=0, S=1 (Not-Aus nicht gedrückt, Schutztür geschlossen, Start gedrückt)
- Zeile 8: N=0, T=1, W=1, S=1 (Not-Aus nicht gedrückt, beides aktiv, Start gedrückt)

**c) Vereinfachung der Funktion**

Die Funktion $M = (\neg N) \land (T \lor W) \land S$ ist bereits in einer relativ einfachen Form (Produkt von Summen, POS-Form).

Mögliche Umformungen:
1. Ausmultiplizieren (Distributivgesetz):
   $$M = (\neg N) \land (T \lor W) \land S$$
   
2. Reihenfolge ändern (Kommutativgesetz):
   $$M = S \land (\neg N) \land (T \lor W)$$

Diese Form ist bereits minimal und kann nicht weiter vereinfacht werden, da:
- Alle drei Faktoren unabhängig voneinander sind
- Keine gemeinsamen Teilausdrücke existieren
- Die Funktion nur 3 von 16 möglichen Ausgängen auf 1 setzt

**Alternative Darstellung** (Disjunktive Normalform, DNF):
$$M = (\neg N \land \neg T \land W \land S) \lor (\neg N \land T \land \neg W \land S) \lor (\neg N \land T \land W \land S)$$

Diese Form ist **länger** als die ursprüngliche, zeigt aber explizit die drei Fälle, in denen M=1 ist.

**d) Situationen, in denen die Maschine trotz Startknopf nicht startet**

Wenn S=1 (Startknopf gedrückt), aber M=0 (Maschine startet nicht), dann sind folgende Fälle möglich:

**Fall 1: Not-Aus ist gedrückt (N=1)**
- Zeile 10: N=1, T=0, W=0, S=1
- Zeile 12: N=1, T=0, W=1, S=1
- Zeile 14: N=1, T=1, W=0, S=1
- Zeile 16: N=1, T=1, W=1, S=1

→ **Alle 4 Fälle mit N=1**: Der Not-Aus hat höchste Priorität und blockiert den Start immer!

**Fall 2: Not-Aus nicht gedrückt (N=0), aber weder Schutztür noch Wartungsmodus aktiv**
- Zeile 2: N=0, T=0, W=0, S=1

→ **1 Fall**: Weder Schutztür geschlossen noch Wartungsmodus aktiv.

**Insgesamt**: Von 8 Fällen mit S=1 startet die Maschine in **5 Fällen nicht** (und nur in 3 Fällen).

**Sicherheitsinterpretation**: Diese Schaltung ist sehr sicher, da:
1. Der Not-Aus absolute Priorität hat (selbst bei allen anderen korrekten Bedingungen)
2. Mindestens eine Schutzmaßnahme (Tür oder Wartungsmodus) aktiv sein muss
3. Der Start nur bei vollständiger Sicherheit erfolgt

**Häufige Fehler**:
- **Not-Aus-Logik verwechseln**: N=0 bedeutet "nicht gedrückt", daher muss ¬N verwendet werden!
- **OR vs. AND verwechseln**: "Entweder...oder" bedeutet OR (mindestens eine Bedingung), nicht XOR (genau eine).
- **Zwischenschritte überspringen**: Bei 16 Zeilen systematisch vorgehen und Zwischenergebnisse berechnen.
- **Vereinfachung erzwingen**: Nicht jede Funktion lässt sich dramatisch vereinfachen. Die POS-Form ist hier bereits optimal.

**Alternative Lösungsansätze**:

**Ansatz 1: Karnaugh-Diagramm** (fortgeschritten, kommt in V04)
- Visualisiert die Wahrheitstabelle in 2D
- Erlaubt einfaches Erkennen von Vereinfachungen
- Für diese Funktion: Keine weitere Vereinfachung möglich

**Ansatz 2: Quine-McCluskey-Algorithmus** (fortgeschritten)
- Systematischer Algorithmus zur Minimierung
- Liefert garantiert minimale Form
- Für diese Funktion: Bestätigt, dass POS-Form minimal ist

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: Sensor-Datentyp-Analyse für Industrie-4.0

**Vollständiger Code**:
```python
# Sensor-Datenanalyse für CAN-Bus / Industrie 4.0
# Demonstriert Type Checking und Type Casting für Sensordaten

print("=== Sensor-Datenanalyse CAN-Bus ===")

# Empfangene Sensornachricht (kommt als String über CAN-Bus)
sensor_wert = input("Empfangene Nachricht (Sensor ID 0x42): ")

# Ursprünglicher Wert und Typ
print(f"\nUrsprünglicher Wert: '{sensor_wert}', Typ: {type(sensor_wert)}")

# Konvertierung zu Integer (für Drehzahl)
wert_int = int(sensor_wert)
print(f"Als Integer: {wert_int}, Typ: {type(wert_int):20} → Drehzahl: {wert_int} U/min")

# Konvertierung zu Float (für Temperatur)
wert_float = float(sensor_wert)
print(f"Als Float: {wert_float}, Typ: {type(wert_float):20} → Temperatur: {wert_float} °C")

# Konvertierung zu Boolean (für Motor-Status)
wert_bool = bool(int(sensor_wert))  # int() zuerst, dann bool()
motor_status = "LÄUFT" if wert_bool else "STEHT"
print(f"Als Boolean: {wert_bool}, Typ: {type(wert_bool):20} → Motor: {motor_status} (Wert ≠ 0)")
```

**Beispiel-Ausgabe**:
```
=== Sensor-Datenanalyse CAN-Bus ===
Empfangene Nachricht (Sensor ID 0x42): 85

Ursprünglicher Wert: '85', Typ: <class 'str'>
Als Integer: 85, Typ: <class 'int'>        → Drehzahl: 85 U/min
Als Float: 85.0, Typ: <class 'float'>      → Temperatur: 85.0 °C
Als Boolean: True, Typ: <class 'bool'>     → Motor: LÄUFT (Wert ≠ 0)
```

**Maschinenbau-Kontext**:

**CAN-Bus** (Controller Area Network) ist der Standard für Maschinen-Kommunikation:
- Automobil: Motorsteuerung, ABS, Airbag
- Maschinenbau: CNC-Steuerung, Roboter, Förderbänder
- Protokoll: Nachrichten als Byte-Arrays → müssen dekodiert werden

**Datentyp-Wahl**:
- **Integer**: Diskrete Werte (Drehzahl, Stückzahl, Impulse)
- **Float**: Kontinuierliche Messgrößen (Temperatur, Druck, Spannung)
- **Boolean**: Binärzustände (Motor AN/AUS, Ventil offen/geschlossen)

**Boolean-Konvertierung**: In Automatisierung gilt:
- `0` = FALSE = AUS/Inaktiv
- `≠ 0` = TRUE = AN/Aktiv

---

### Lösung P2: Maschinenlast-Monitor mit Warnungen

**Vollständiger Code**:
```python
# Maschinenlast-Monitor für CNC-Maschine
# Berechnet Auslastung und gibt Warnstufe aus

print("=== Maschinenlast-Monitor CNC DMG MORI ===")

# Eingaben einlesen
ist_leistung_str = input("Ist-Leistung (kW): ")
nenn_leistung_str = input("Nennleistung (kW): ")

# Konvertierung zu Float
ist_leistung = float(ist_leistung_str)
nenn_leistung = float(nenn_leistung_str)

# Auslastung berechnen (in Prozent)
auslastung = (ist_leistung / nenn_leistung) * 100

# Ausgabe mit 1 Dezimalstelle
print(f"\nAuslastung: {auslastung:.1f}%")

# Warnstufen-Kategorisierung
if auslastung < 50:
    status = "⚠️ UNTERLAST (ineffizient, Energieverschwendung)"
elif auslastung < 80:
    status = "✓ OPTIMAL (bester Wirkungsgrad)"
elif auslastung < 95:
    status = "⚡ HOHE LAST (erhöhter Verschleiß)"
else:  # >= 95%
    status = "🔴 KRITISCH (Überlastung, Notabschaltung empfohlen)"

print(f"Status: {status}")
```

**Maschinenbau-Kontext**:

**Nennleistung** (P_N): Maximale Dauerleistung laut Typenschild (kW)  
**Ist-Leistung** (P_ist): Aktuell verbrauchte Leistung (gemessen)

**Formel**: $\text{Auslastung [%]} = \frac{P_{\text{ist}}}{P_{\text{N}}} \times 100$

**Warnstufen-Begründung**:
- **< 50%**: Maschine im Teillastbereich → schlechter Wirkungsgrad, hohe spezifische Kosten
- **50-80%**: Optimaler Betriebspunkt → bester Wirkungsgrad, niedriger Verschleiß
- **80-95%**: Hohe Last → erhöhte Temperaturen, schnellerer Verschleiß an Lagern/Spindel
- **≥ 95%**: Überlast → Gefahr von Motorschäden, Sicherungen können auslösen

**Praktische Anwendung**: Maschinen sollten dauerhaft im Bereich 60-80% betrieben werden für maximale Lebensdauer und Effizienz.

**Beispiel-Ausgabe**:
```
Gib deine Größe in cm ein: 175
Gib dein Gewicht in kg ein: 70

Dein BMI beträgt: 22.86
Kategorie: Normalgewicht
```

**Erklärung**:

**Schritt-für-Schritt Durchlauf** (mit Beispielwerten: Größe 175 cm, Gewicht 70 kg):

1. **Eingabe**: `groesse_cm_str = "175"`, `gewicht_kg_str = "70"` (beide Strings!)
2. **Konvertierung**: `groesse_cm = 175.0`, `gewicht_kg = 70.0` (jetzt Floats)
3. **Umrechnung**: `groesse_m = 175.0 / 100 = 1.75` (Meter)
4. **BMI-Berechnung**: `bmi = 70.0 / (1.75 ** 2) = 70.0 / 3.0625 ≈ 22.857`
5. **Formatierung**: `f"{bmi:.2f}"` → `"22.86"` (2 Dezimalstellen)
6. **Kategorisierung**:
   - `bmi < 18.5`? Nein (22.86 ≮ 18.5)
   - `bmi < 25`? **Ja** (22.86 < 25) → `kategorie = "Normalgewicht"`

**Konzepte in dieser Lösung**:
- **Type Casting**: `input()` liefert String, Umwandlung mit `float()` nötig für Berechnungen
- **Arithmetik**: Division und Potenzierung (`**`)
- **f-String Formatierung**: `{bmi:.2f}` rundet auf 2 Dezimalstellen
- **Verzweigungen**: `if-elif-else` für Kategorisierung (V05 behandelt dies ausführlich)

**Warum float() statt int()?**

Wir verwenden `float()`, weil:
- Größe und Gewicht oft Dezimalstellen haben (z.B. 175.5 cm, 70.3 kg)
- `float()` kann auch ganzzahlige Strings konvertieren: `float("175")` → `175.0`
- Der BMI selbst ist fast immer eine Fließkommazahl

**Häufige Fehler**:
- **Vergessen der Umrechnung**: Direkt mit `groesse_cm` rechnen ohne Division durch 100 → BMI viel zu klein
- **int() statt float()**: `int("70.5")` würde einen `ValueError` werfen
- **Falsche Klammer-Setzung**: `gewicht_kg / groesse_m ** 2` ist **falsch** (Punktrechnung vor Strichrechnung!)
  - Richtig: `gewicht_kg / (groesse_m ** 2)` oder `gewicht_kg / groesse_m / groesse_m`

---

### Lösung P3: Sensor-Validierung für SPS-Eingänge

**Vollständiger Code**:
```python
# Sensor-Validierung für SPS (Speicherprogrammierbare Steuerung)
# Prüft Temperatursensor Pt100 auf Plausibilität

print("=== Sensor-Validierung SPS Eingang E0.0 ===")

# Sensor-Rohwert einlesen
temp_str = input("Temperatursensor Pt100 (°C): ")

# Typ der Eingabe anzeigen
print(f"\nTyp der Eingabe: {type(temp_str)}")

# Validierung: Prüfe, ob nur Ziffern (ggf. mit Minus)
if temp_str.lstrip('-').isdigit():
    print("✓ Eingabe ist gültig: Nur Ziffern")
    
    # Konvertierung zu Integer
    temp = int(temp_str)
    print(f"Konvertierter Wert: {temp}°C, Typ: {type(temp)}")
    
    # Plausibilitätsprüfung: -50 bis +150°C (typisch für Pt100/Pt1000)
    if -50 <= temp <= 150:
        # Temperatur-Kategorisierung
        if temp < 0:
            status = "❄️ GEFRIERBEREICH (Frostgefahr, Kühlmittelpumpen prüfen)"
        elif temp < 50:
            status = "🟢 NORMALBEREICH (Maschine im Standby oder Aufwärmphase)"
        elif temp < 80:
            status = "⚙️ BETRIEBSTEMPERATUR (Maschine arbeitet)"
        elif temp < 120:
            status = "⚠️ WARNUNG (erhöhte Temperatur, Kühlung prüfen)"
        else:  # 120-150°C
            status = "🔴 KRITISCH (Überhitzung, Notabschaltung)"
        
        print(f"\nStatus: {status}")
    else:
        print(f"\n✗ FEHLER: Temperatur {temp}°C außerhalb Sensor-Bereich (-50 bis +150°C)")
        print("→ Sensor defekt oder falsch kalibriert")
else:
    print("✗ FEHLER: Ungültige Zeichen!")
    print("→ Sensor defekt oder Kabelbruch")
```

**Maschinenbau-Kontext**:

**Pt100/Pt1000**: Platin-Widerstandsthermometer (RTD = Resistance Temperature Detector)
- **Pt100**: 100 Ω bei 0°C, Standard in Industrie
- **Messbereich**: Typisch -50°C bis +150°C (bis 600°C möglich)
- **Genauigkeit**: Klasse A: ±0.15°C bei 0°C

**SPS-Eingang**: Analog-Eingang (4-20 mA oder 0-10 V) wird digitalisiert
- **4 mA** = -50°C (Unterer Messbereich)
- **20 mA** = +150°C (Oberer Messbereich)

**`.lstrip('-').isdigit()`**: Entfernt führendes Minus, dann Ziffernprüfung → erlaubt negative Temperaturen wie "-25".
```

**Beispiel-Ausgaben**:

**Fall 1: Gültige Eingabe**
```
Gib dein Alter ein: 25
Typ der Eingabe: <class 'str'>
Eingabe ist gültig: Nur Ziffern
Konvertiertes Alter: 25, Typ: <class 'int'>
Du bist ein Erwachsener
```

**Fall 2: Ungültige Zeichen**
```
Gib dein Alter ein: abc
Typ der Eingabe: <class 'str'>
Fehler: Die Eingabe enthält ungültige Zeichen!
```

**Fall 3: Alter außerhalb des Bereichs**
```
Gib dein Alter ein: 150
Typ der Eingabe: <class 'str'>
Eingabe ist gültig: Nur Ziffern
Konvertiertes Alter: 150, Typ: <class 'int'>
Fehler: Alter muss zwischen 0 und 120 liegen!
```

**Erklärung**:

**Lösungsweg Schritt für Schritt**:

1. **Eingabe lesen**: `alter_str = input(...)` → String
2. **Typ anzeigen**: `type(alter_str)` → `<class 'str'>`
3. **Validierung**: `alter_str.isdigit()` prüft, ob **alle** Zeichen Ziffern sind
   - `"25".isdigit()` → `True`
   - `"abc".isdigit()` → `False`
   - `"-5".isdigit()` → `False` (Minus-Zeichen ist keine Ziffer)
   - `"2.5".isdigit()` → `False` (Punkt ist keine Ziffer)
4. **Konvertierung**: Nur bei gültiger Eingabe `int()` aufrufen
5. **Bereichsprüfung**: `0 <= alter <= 120` (Python erlaubt verkettete Vergleiche!)
6. **Kategorisierung**: Verschachtelte `if-elif-else`-Struktur

**Warum .isdigit() vor int()?**

Die Methode `.isdigit()` prüft **vor** der Konvertierung, ob der String nur Ziffern enthält. Dadurch vermeiden wir `ValueError`-Exceptions:

```python
# OHNE Validierung (kann crashen):
alter = int(input("Alter: "))  # ValueError bei "abc"

# MIT Validierung (sicher):
alter_str = input("Alter: ")
if alter_str.isdigit():
    alter = int(alter_str)  # Garantiert erfolgreich
```

**Konzepte in dieser Lösung**:
- **String-Methode `.isdigit()`**: Prüft, ob String nur Ziffern enthält
- **Verschachtelte Bedingungen**: `if` innerhalb eines `if`
- **Verkettete Vergleiche**: `0 <= alter <= 120` statt `alter >= 0 and alter <= 120`
- **Defensive Programmierung**: Validierung vor Konvertierung

**Häufige Fehler**:
- **Direkt int() ohne Prüfung**: Führt zu `ValueError` bei ungültigen Eingaben
- **Negative Zahlen akzeptieren**: `-5.isdigit()` ist `False`, aber logisch wäre negatives Alter auch ungültig
- **Bereichsprüfung vergessen**: Alter von 999 wäre ohne Bereichsprüfung "gültig"

---

### Lösung P4: Maschinenzustand-Tracking mit Mutable vs. Immutable

**Vollständiger Code**:
```python
# Maschinenzustand-Tracking: Unveränderliche vs. Veränderliche Typen
# Demonstriert Unterschied durch Speicheradressen (id()) in Industrie-4.0-Kontext

print("=== Teil 1: Unveränderliche Typen (Maschinen-ID als String) ===\n")

# Ursprüngliche Maschinen-ID
maschinen_id = "CNC-001"
print(f"Ursprung: maschinen_id = '{maschinen_id}', id = {id(maschinen_id)}")

# Operation 1: Produktionslinie hinzufügen (Konkatenation)
maschinen_id = maschinen_id + "-LINIE-A"
print(f"Nach Produktionslinie: maschinen_id = '{maschinen_id}', id = {id(maschinen_id)}")
print("→ Neue Speicheradresse! Neues Objekt wurde erstellt.\n")

# Operation 2: Großschreibung für SAP-Export
maschinen_id = maschinen_id.upper()
print(f"Nach .upper(): maschinen_id = '{maschinen_id}', id = {id(maschinen_id)}")
print("→ Wieder neue Speicheradresse! Neues Objekt.\n")

# Operation 3: Wartungskennung hinzufügen
maschinen_id = maschinen_id.replace("CNC", "CNC-WARTUNG")
print(f"Nach Wartungskennung: maschinen_id = '{maschinen_id}', id = {id(maschinen_id)}")
print("→ Erneut neue Speicheradresse! Neues Objekt.\n")

print("📌 Fazit Teil 1: Strings (Maschinen-IDs) sind unveränderlich (immutable).")
print("   Jede 'Änderung' erzeugt ein neues Objekt im Speicher.\n")
print("="*60)
print()

print("=== Teil 2: Veränderliche Typen (Sensor-Daten als Liste) ===\n")

# Ursprüngliche Sensor-Messwerte [Temperatur °C, Drehzahl U/min, Vibration mm/s]
sensor_daten = [45.2, 1200, 3.5]
print(f"Ursprung: sensor_daten = {sensor_daten}, id = {id(sensor_daten)}")

# Operation 1: Neue Messung hinzufügen (Leistung in kW)
sensor_daten.append(18.5)
print(f"Nach append(18.5): sensor_daten = {sensor_daten}, id = {id(sensor_daten)}")
print("→ GLEICHE Speicheradresse! Objekt wurde modifiziert.\n")

# Operation 2: Fehlerhafte Messung entfernen
sensor_daten.remove(3.5)  # Vibrationswert war Ausreißer
print(f"Nach remove(3.5): sensor_daten = {sensor_daten}, id = {id(sensor_daten)}")
print("→ Immer noch GLEICHE Speicheradresse!\n")

# Operation 3: Temperatur aktualisieren
sensor_daten[0] = 47.8  # Neue Temperaturmessung
print(f"Nach sensor_daten[0] = 47.8: sensor_daten = {sensor_daten}, id = {id(sensor_daten)}")
print("→ Immer noch GLEICHE Speicheradresse!\n")

print("📌 Fazit Teil 2: Listen (Sensor-Daten) sind veränderlich (mutable).")
print("   Modifikationen ändern das Objekt selbst, ohne neues zu erstellen.\n")
print("="*60)
print()

print("=== Teil 3: Seiteneffekte bei Maschinendaten-Logging ===\n")

# Original-Messdaten von Schicht 1
schicht1_daten = [150.0, 2400, 85.5]  # [Druck bar, Drehzahl, Temperatur]
print(f"schicht1_daten = {schicht1_daten}, id = {id(schicht1_daten)}")

# FEHLER: Schicht 2 "kopiert" Daten (aber es ist nur eine Referenz!)
schicht2_daten = schicht1_daten
print(f"schicht2_daten = schicht1_daten: schicht2_daten = {schicht2_daten}, id = {id(schicht2_daten)}")
print(f"→ Beide IDs sind GLEICH: {id(schicht1_daten)} == {id(schicht2_daten)}\n")

# Schicht 2 ändert "ihre" Daten
schicht2_daten.append(92.3)  # Neue Temperaturmessung
print(f"Nach schicht2_daten.append(92.3):")
print(f"  schicht1_daten = {schicht1_daten}  ⚠️ AUCH betroffen!")
print(f"  schicht2_daten = {schicht2_daten}")
print("→ BEIDE Listen sind betroffen! Datenverfälschung!\n")

print("📌 Fazit Teil 3: Bei veränderlichen Typen zeigt 'schicht2_daten = schicht1_daten'")
print("   auf dasselbe Objekt. Änderungen wirken sich auf beide aus!")
print("\n   ⚠️ Risiko in Produktion: Daten-Integrität gefährdet!")
print("\n   Für echte Kopie verwende: schicht2_daten = schicht1_daten.copy()")
print("   oder: schicht2_daten = schicht1_daten[:]\n")

# Demonstration echter Kopie
print("--- Demonstration echter Kopie (korrekte Schichtdaten-Trennung) ---")
schicht1_korrekt = [150.0, 2400, 85.5]
schicht2_korrekt = schicht1_korrekt.copy()  # Echte Kopie!
print(f"schicht1_korrekt = {schicht1_korrekt}, id = {id(schicht1_korrekt)}")
print(f"schicht2_korrekt = {schicht2_korrekt}, id = {id(schicht2_korrekt)}")
print(f"→ IDs sind VERSCHIEDEN: {id(schicht1_korrekt)} != {id(schicht2_korrekt)}\n")

schicht2_korrekt.append(92.3)
print(f"Nach schicht2_korrekt.append(92.3):")
print(f"  schicht1_korrekt = {schicht1_korrekt}  ✅ Unverändert!")
print(f"  schicht2_korrekt = {schicht2_korrekt}  ✅ Nur diese geändert!")
print("→ Daten-Integrität gewahrt!\n")
```

**Beispiel-Ausgabe** (Speicheradressen variieren):
```
=== Teil 1: Unveränderliche Typen (Strings) ===

Ursprung: text = 'Python', id = 140234567890123
Nach Konkatenation: text = 'Python ist toll', id = 140234567891456
→ Neue Speicheradresse! Neues Objekt wurde erstellt.

Nach .upper(): text = 'PYTHON IST TOLL', id = 140234567892789
→ Wieder neue Speicheradresse! Neues Objekt.

Nach .replace(): text = 'JAVA IST TOLL', id = 140234567893012
→ Erneut neue Speicheradresse! Neues Objekt.

📌 Fazit Teil 1: Strings sind unveränderlich (immutable).
   Jede 'Änderung' erzeugt ein neues Objekt im Speicher.

============================================================

=== Teil 2: Veränderliche Typen (Listen) ===

Ursprung: zahlen = [1, 2, 3], id = 140234567894000
Nach append(4): zahlen = [1, 2, 3, 4], id = 140234567894000
→ GLEICHE Speicheradresse! Objekt wurde modifiziert.

Nach remove(2): zahlen = [1, 3, 4], id = 140234567894000
→ Immer noch GLEICHE Speicheradresse!

Nach zahlen[0] = 10: zahlen = [10, 3, 4], id = 140234567894000
→ Immer noch GLEICHE Speicheradresse!

📌 Fazit Teil 2: Listen sind veränderlich (mutable).
   Modifikationen ändern das Objekt selbst, ohne neues zu erstellen.

============================================================

=== Teil 3: Seiteneffekte bei veränderlichen Typen ===

original = [1, 2, 3], id = 140234567895000
kopie = original: kopie = [1, 2, 3], id = 140234567895000
→ Beide IDs sind GLEICH: 140234567895000 == 140234567895000

Nach kopie.append(4):
  original = [1, 2, 3, 4]
  kopie = [1, 2, 3, 4]
→ BEIDE Listen sind betroffen!

📌 Fazit Teil 3: Bei veränderlichen Typen zeigt 'kopie = original'
   auf dasselbe Objekt. Änderungen wirken sich auf beide aus!

   Für echte Kopie verwende: kopie = original.copy()
   oder: kopie = original[:]

--- Demonstration echter Kopie ---
original2 = [1, 2, 3], id = 140234567896000
echte_kopie = [1, 2, 3], id = 140234567896200
→ IDs sind VERSCHIEDEN: 140234567896000 != 140234567896200

Nach echte_kopie.append(4):
  original2 = [1, 2, 3]  (unverändert)
  echte_kopie = [1, 2, 3, 4]  (geändert)
→ Nur echte_kopie ist betroffen!
```

**Erklärung**:

**Architektur-Überblick**:

Das Programm ist in drei Teile gegliedert, die jeweils einen Aspekt der Mutability demonstrieren:

1. **Teil 1**: Zeigt, dass String-Operationen immer neue Objekte erzeugen
2. **Teil 2**: Zeigt, dass Listen-Operationen das existierende Objekt modifizieren
3. **Teil 3**: Demonstriert Seiteneffekte durch gemeinsame Referenzen und wie man sie vermeidet

**Schritt-für-Schritt Erklärung**:

**Teil 1 – Strings (Immutable)**:
- Bei jeder String-Operation (Konkatenation, `.upper()`, `.replace()`) ändert sich die Speicheradresse (`id()`)
- Das bedeutet: Python erzeugt ein **neues String-Objekt** und weist es der Variable zu
- Das alte String-Objekt wird vom Garbage Collector entfernt (wenn keine anderen Referenzen existieren)

**Teil 2 – Listen (Mutable)**:
- Bei Listen-Operationen (`.append()`, `.remove()`, Indexzuweisung) bleibt die Speicheradresse **gleich**
- Das bedeutet: Python modifiziert das **existierende Listen-Objekt**
- Keine neuen Objekte werden erstellt (effizienter für große Datenstrukturen)

**Teil 3 – Seiteneffekte**:
- `kopie = original` erstellt **keine Kopie**, sondern eine zweite Referenz auf dasselbe Objekt
- Beide Variablen zeigen auf die **gleiche Speicheradresse**
- Änderungen über eine Variable wirken sich auf beide aus (unerwartetes Verhalten!)
- **Lösung**: `.copy()` oder Slice `[:]` für echte Kopien

**Design-Entscheidungen**:
- **`id()` verwenden**: Macht die Speicheradresse sichtbar und beweist, ob neue Objekte erstellt werden
- **Klare Struktur**: Drei separate Teile mit jeweils eigenem Fazit
- **Visuelle Trennung**: `print("="*60)` für bessere Lesbarkeit
- **Demonstration echter Kopie**: Zeigt die Lösung für das Problem aus Teil 3

**Komplexitätsanalyse**:
- **Zeitkomplexität**: O(1) für alle Operationen außer String-Konkatenation (O(n) für neue String-Erzeugung)
- **Speicherkomplexität**: Strings erzeugen viele temporäre Objekte (O(n) pro Operation), Listen modifizieren in-place (O(1))

**Alternative Lösungsansätze**:

**Ansatz 1: Visualisierung mit Diagrammen**
```python
# ASCII-Art zur Visualisierung der Referenzen
print("kopie ─────┐")
print("           ↓")
print("        [1,2,3] ← original")
```
- ✅ Vorteile: Sehr anschaulich, gut für didaktische Zwecke
- ❌ Nachteile: Aufwändiger zu erstellen, nicht maschinell auswertbar

**Ansatz 2: Assertions für automatische Tests**
```python
original = [1, 2, 3]
kopie = original
assert id(original) == id(kopie), "IDs sollten gleich sein"
kopie.append(4)
assert original == [1, 2, 3, 4], "Original sollte auch geändert sein"
```
- ✅ Vorteile: Automatisch testbar, findet Fehler
- ❌ Nachteile: Weniger lehrreich für Anfänger

**Häufige Fehler**:
- **Annahme, dass `=` kopiert**: `kopie = original` erstellt **keine** Kopie bei mutable Typen!
- **Verwechslung von is und ==**: `is` prüft Identität (gleiche Speicheradresse), `==` prüft Wertgleichheit
- **Immutability falsch einschätzen**: Tupel sind immutable, aber können mutable Elemente enthalten: `([1, 2], 3)` – die Liste kann verändert werden!

---

### Lösung P5: Sicherheitsschaltungs-Validator mit Boolean-Logik

**Vollständiger Code**:
```python
# Sicherheitsschaltungs-Validator für Industriemaschinen
# Prüft alle Sicherheitsbedingungen gemäß ISO 13849 und EN 60204-1
# Alle 6 Bedingungen müssen erfüllt sein für sicheren Maschinenbetrieb

def eingabe_boolean(beschreibung):
    """
    Liest Boolean-Eingabe von Benutzer.
    Akzeptiert: "1", "True", "true", "TRUE", "ja", "j", "yes", "y"
    """
    eingabe = input(f"{beschreibung} (1/True/ja für aktiv): ").strip().lower()
    return eingabe in ["1", "true", "ja", "j", "yes", "y"]

# === EINGABE: Sensor-Zustände abfragen ===
print("="*70)
print("SICHERHEITSSCHALTUNGS-VALIDATOR")
print("Maschinenbetrieb nur bei erfüllten Sicherheitsbedingungen!")
print("="*70)
print()

# Sicherheitsbedingungen abfragen
not_aus_ok = eingabe_boolean("1️⃣  Not-Aus-Schalter NICHT gedrückt")
schutztuer_ok = eingabe_boolean("2️⃣  Schutztür geschlossen")
lichtvorhang_ok = eingabe_boolean("3️⃣  Lichtvorhang frei")
zweihand_ok = eingabe_boolean("4️⃣  Zwei-Hand-Bedienung aktiv")
hydraulik_ok = eingabe_boolean("5️⃣  Hydraulikdruck im Sollbereich (150-200 bar)")
spindel_ok = eingabe_boolean("6️⃣  Spindeldrehzahl < Grenzwert (< 6000 U/min)")

print()
print("="*70)
print("VALIDIERUNG DER SICHERHEITSBEDINGUNGEN")
print("="*70)
print()

# === EINZELPRÜFUNG ===
print("--- Einzelprüfung ---")
print(f"{'✅' if not_aus_ok else '❌'} Not-Aus: {'OK' if not_aus_ok else 'FEHLER - Not-Aus gedrückt!'}")
print(f"{'✅' if schutztuer_ok else '❌'} Schutztür: {'OK' if schutztuer_ok else 'FEHLER - Schutztür offen!'}")
print(f"{'✅' if lichtvorhang_ok else '❌'} Lichtvorhang: {'OK' if lichtvorhang_ok else 'FEHLER - Lichtvorhang unterbrochen!'}")
print(f"{'✅' if zweihand_ok else '❌'} Zwei-Hand-Bedienung: {'OK' if zweihand_ok else 'FEHLER - Nicht beide Taster gedrückt!'}")
print(f"{'✅' if hydraulik_ok else '❌'} Hydraulikdruck: {'OK' if hydraulik_ok else 'FEHLER - Druck außerhalb Sollbereich!'}")
print(f"{'✅' if spindel_ok else '❌'} Spindeldrehzahl: {'OK' if spindel_ok else 'FEHLER - Drehzahl zu hoch!'}")

print()

# === GESAMTVALIDIERUNG ===
# Alle Bedingungen müssen erfüllt sein (AND-Verknüpfung)
alle_bedingungen_erfuellt = (
    not_aus_ok and 
    schutztuer_ok and 
    lichtvorhang_ok and 
    zweihand_ok and 
    hydraulik_ok and 
    spindel_ok
)

print("--- Gesamtergebnis ---")
if alle_bedingungen_erfuellt:
    print("✅ ✅ ✅  ALLE SICHERHEITSBEDINGUNGEN ERFÜLLT  ✅ ✅ ✅")
    print("➡️  Maschinenbetrieb FREIGEGEBEN")
    print("➡️  SPS-Ausgang: ENABLE = HIGH")
else:
    print("❌ ❌ ❌  SICHERHEITSBEDINGUNGEN NICHT ERFÜLLT  ❌ ❌ ❌")
    print("➡️  Maschinenbetrieb GESPERRT")
    print("➡️  SPS-Ausgang: ENABLE = LOW")

print()

# === FEHLERANALYSE ===
if not alle_bedingungen_erfuellt:
    print("--- Fehleranalyse (fehlgeschlagene Bedingungen) ---")
    fehler_count = 0
    
    if not not_aus_ok:
        fehler_count += 1
        print(f"  {fehler_count}. Not-Aus-Schalter ist gedrückt → Freigabe sofort aufheben!")
    
    if not schutztuer_ok:
        fehler_count += 1
        print(f"  {fehler_count}. Schutztür ist offen → Zugang zur Gefahrenzone!")
    
    if not lichtvorhang_ok:
        fehler_count += 1
        print(f"  {fehler_count}. Lichtvorhang unterbrochen → Person im Gefahrenbereich!")
    
    if not zweihand_ok:
        fehler_count += 1
        print(f"  {fehler_count}. Zwei-Hand-Bedienung nicht aktiv → Hände nicht geschützt!")
    
    if not hydraulik_ok:
        fehler_count += 1
        print(f"  {fehler_count}. Hydraulikdruck außerhalb 150-200 bar → Prozessunsicherheit!")
    
    if not spindel_ok:
        fehler_count += 1
        print(f"  {fehler_count}. Spindeldrehzahl ≥ 6000 U/min → Überdrehzahl-Risiko!")
    
    print()
    print(f"➡️  Anzahl fehlgeschlagener Bedingungen: {fehler_count} von 6")

print()
print("="*70)

# === ZUSATZINFORMATIONEN ===
print("--- Statistik ---")
bedingungen_erfuellt = sum([not_aus_ok, schutztuer_ok, lichtvorhang_ok, 
                             zweihand_ok, hydraulik_ok, spindel_ok])
bedingungen_gesamt = 6
prozent = (bedingungen_erfuellt / bedingungen_gesamt) * 100

print(f"Erfüllte Bedingungen: {bedingungen_erfuellt} / {bedingungen_gesamt} ({prozent:.1f}%)")
print(f"Sicherheitslevel: {'SICHER' if alle_bedingungen_erfuellt else 'UNSICHER'}")
print()

# === BOOLEAN-LOGIK ANALYSE ===
print("--- Boolean-Logik (für SPS-Programmierung) ---")
print(f"not_aus_ok AND schutztuer_ok AND lichtvorhang_ok AND zweihand_ok AND hydraulik_ok AND spindel_ok")
print(f"= {not_aus_ok} AND {schutztuer_ok} AND {lichtvorhang_ok} AND {zweihand_ok} AND {hydraulik_ok} AND {spindel_ok}")
print(f"= {alle_bedingungen_erfuellt}")
print()
print("In SPS-Logik (Ladder Diagram):")
print("|--[ ]--[ ]--[ ]--[ ]--[ ]--[ ]--(ENABLE)--|")
print("   NOT  TÜR  LICHT 2HAND HYD  SPIN")
print("="*70)
```

**Beispiel-Ausgaben**:

**Szenario 1: Alle Sicherheitsbedingungen erfüllt**
```
======================================================================
SICHERHEITSSCHALTUNGS-VALIDATOR
Maschinenbetrieb nur bei erfüllten Sicherheitsbedingungen!
======================================================================

1️⃣  Not-Aus-Schalter NICHT gedrückt (1/True/ja für aktiv): 1
2️⃣  Schutztür geschlossen (1/True/ja für aktiv): true
3️⃣  Lichtvorhang frei (1/True/ja für aktiv): ja
4️⃣  Zwei-Hand-Bedienung aktiv (1/True/ja für aktiv): 1
5️⃣  Hydraulikdruck im Sollbereich (150-200 bar) (1/True/ja für aktiv): yes
6️⃣  Spindeldrehzahl < Grenzwert (< 6000 U/min) (1/True/ja für aktiv): y

======================================================================
VALIDIERUNG DER SICHERHEITSBEDINGUNGEN
======================================================================

--- Einzelprüfung ---
✅ Not-Aus: OK
✅ Schutztür: OK
✅ Lichtvorhang: OK
✅ Zwei-Hand-Bedienung: OK
✅ Hydraulikdruck: OK
✅ Spindeldrehzahl: OK

--- Gesamtergebnis ---
✅ ✅ ✅  ALLE SICHERHEITSBEDINGUNGEN ERFÜLLT  ✅ ✅ ✅
➡️  Maschinenbetrieb FREIGEGEBEN
➡️  SPS-Ausgang: ENABLE = HIGH

--- Statistik ---
Erfüllte Bedingungen: 6 / 6 (100.0%)
Sicherheitslevel: SICHER

--- Boolean-Logik (für SPS-Programmierung) ---
not_aus_ok AND schutztuer_ok AND lichtvorhang_ok AND zweihand_ok AND hydraulik_ok AND spindel_ok
= True AND True AND True AND True AND True AND True
= True

In SPS-Logik (Ladder Diagram):
|--[ ]--[ ]--[ ]--[ ]--[ ]--[ ]--(ENABLE)--|
   NOT  TÜR  LICHT 2HAND HYD  SPIN
======================================================================
```

**Szenario 2: Mehrere Sicherheitsbedingungen verletzt**
```
======================================================================
SICHERHEITSSCHALTUNGS-VALIDATOR
Maschinenbetrieb nur bei erfüllten Sicherheitsbedingungen!
======================================================================

1️⃣  Not-Aus-Schalter NICHT gedrückt (1/True/ja für aktiv): 1
2️⃣  Schutztür geschlossen (1/True/ja für aktiv): 0
3️⃣  Lichtvorhang frei (1/True/ja für aktiv): False
4️⃣  Zwei-Hand-Bedienung aktiv (1/True/ja für aktiv): true
5️⃣  Hydraulikdruck im Sollbereich (150-200 bar) (1/True/ja für aktiv): 1
6️⃣  Spindeldrehzahl < Grenzwert (< 6000 U/min) (1/True/ja für aktiv): no

======================================================================
VALIDIERUNG DER SICHERHEITSBEDINGUNGEN
======================================================================

--- Einzelprüfung ---
✅ Not-Aus: OK
❌ Schutztür: FEHLER - Schutztür offen!
❌ Lichtvorhang: FEHLER - Lichtvorhang unterbrochen!
✅ Zwei-Hand-Bedienung: OK
✅ Hydraulikdruck: OK
❌ Spindeldrehzahl: FEHLER - Drehzahl zu hoch!

--- Gesamtergebnis ---
❌ ❌ ❌  SICHERHEITSBEDINGUNGEN NICHT ERFÜLLT  ❌ ❌ ❌
➡️  Maschinenbetrieb GESPERRT
➡️  SPS-Ausgang: ENABLE = LOW

--- Fehleranalyse (fehlgeschlagene Bedingungen) ---
  1. Schutztür ist offen → Zugang zur Gefahrenzone!
  2. Lichtvorhang unterbrochen → Person im Gefahrenbereich!
  3. Spindeldrehzahl ≥ 6000 U/min → Überdrehzahl-Risiko!

➡️  Anzahl fehlgeschlagener Bedingungen: 3 von 6

--- Statistik ---
Erfüllte Bedingungen: 3 / 6 (50.0%)
Sicherheitslevel: UNSICHER

--- Boolean-Logik (für SPS-Programmierung) ---
not_aus_ok AND schutztuer_ok AND lichtvorhang_ok AND zweihand_ok AND hydraulik_ok AND spindel_ok
= True AND False AND False AND True AND True AND False
= False

In SPS-Logik (Ladder Diagram):
|--[ ]--[ ]--[ ]--[ ]--[ ]--[ ]--(ENABLE)--|
   NOT  TÜR  LICHT 2HAND HYD  SPIN
======================================================================
```

**Erklärung**:

**Architektur-Überblick**:

Das Programm simuliert die Sicherheitslogik einer **Speicherprogrammierbaren Steuerung (SPS)** für eine Industriemaschine nach den Normen **ISO 13849** (Sicherheit von Maschinen) und **EN 60204-1** (Elektrische Ausrüstung von Maschinen). Die Architektur besteht aus drei Hauptkomponenten:

1. **Eingabe-Modul** (`eingabe_boolean()`): Liest und normalisiert Sensor-Zustände
2. **Validierungs-Modul**: Prüft jede Sicherheitsbedingung einzeln und in Kombination
3. **Ausgabe- und Analyse-Modul**: Visualisiert Ergebnisse und gibt SPS-Freigabesignal

**Schritt-für-Schritt Erklärung**:

**1. Hilfsfunktion `eingabe_boolean()`**:
Die Funktion akzeptiert verschiedene Eingaben für "wahr" (1, True, ja, j, yes, y) und normalisiert sie auf einen Boolean-Wert. Dies simuliert die Flexibilität von SPS-Eingängen, die über verschiedene Sensoren (digital HIGH/LOW, Spannungspegel, Schalter) angesteuert werden können.

**2. Sensorabfrage**:
Sechs kritische Sicherheitssensoren werden abgefragt:
- **Not-Aus**: Zentrale Notabschaltung (ISO 13849 Category 0)
- **Schutztür**: Verhindert Zugang zur Gefahrenzone während Betrieb
- **Lichtvorhang**: Optoelektronische Schutzeinrichtung (ESPE, EN 61496)
- **Zwei-Hand-Bedienung**: Verhindert, dass Hände in Gefahrenzone geraten (EN 574)
- **Hydraulikdruck**: Prozessparameter für sichere Funktionsausführung
- **Spindeldrehzahl**: Überdrehzahlschutz (kritisch bei CNC-Maschinen)

**3. AND-Verknüpfung (Serienschaltung)**:
Die zentrale Sicherheitslogik ist eine **AND-Verknüpfung** aller sechs Bedingungen:
```python
alle_bedingungen_erfuellt = (not_aus_ok AND schutztuer_ok AND lichtvorhang_ok AND 
                              zweihand_ok AND hydraulik_ok AND spindel_ok)
```

Das entspricht einer **Reihenschaltung** in der SPS-Ladder-Logik: Jeder Sensor ist ein „Öffner"-Kontakt (normally closed, NC), der bei Fehler öffnet und die gesamte Kette unterbricht.

**4. Fehleranalyse**:
Wenn die Gesamtbedingung `False` ist, werden alle fehlgeschlagenen Bedingungen mit spezifischen Fehlermeldungen aufgelistet. Dies entspricht der **Diagnosefunktion** moderner SPS-Systeme (z.B. Siemens TIA Portal, Beckhoff TwinCAT).

**5. SPS-Ausgang**:
- **ENABLE = HIGH**: Freigabe für Maschinenbetrieb (alle Bedingungen erfüllt)
- **ENABLE = LOW**: Sperre (mindestens eine Bedingung verletzt)

**Design-Entscheidungen**:

- **Klare Trennung von Eingabe und Logik**: Die `eingabe_boolean()`-Funktion kapselt die Eingabevalidierung und macht den Hauptcode übersichtlicher.

- **Visuelle Feedback-Symbole**: Emojis (✅/❌) verbessern die Lesbarkeit erheblich und simulieren moderne HMI-Displays (Human-Machine Interface) wie die von Siemens oder Allen-Bradley.

- **Ausführliche Fehleranalyse**: In der Praxis muss ein Maschinenbediener **sofort erkennen**, warum die Maschine gesperrt ist. Die detaillierte Fehlerausgabe simuliert ein industrielles HMI-Panel.

- **Ladder-Logik-Visualisierung**: Die ASCII-Darstellung zeigt die **SPS-Programmierlogik** (Ladder Diagram, LD gemäß IEC 61131-3). Dies ist die Standardsprache für SPS-Programmierung.

- **Statistik**: Die prozentuale Erfüllung ist hilfreich für **Wartungsprotokolle** und **Maschinenverfügbarkeit** (MTBF, MTTR-Analyse).

**Sicherheitsnormen-Kontext**:

- **ISO 13849-1**: Definiert Performance Level (PL) von PLa (niedrig) bis PLe (hoch). Eine Maschine mit 6 Sicherheitssensoren in AND-Verknüpfung erreicht typischerweise PL d oder e.

- **EN 60204-1**: Fordert, dass Sicherheitsfunktionen **fail-safe** sind: Bei Sensorfehler (z.B. Kabelbruch) muss die Maschine in einen sicheren Zustand übergehen (Stopp).

- **EN 574 (Zwei-Hand-Bedienung)**: Taster müssen gleichzeitig gedrückt werden (zeitliche Synchronität < 0,5 s), um zu verhindern, dass eine Hand in die Gefahrenzone gerät.

**Komplexitätsanalyse**:

- **Zeitkomplexität**: O(1) für alle Operationen (feste Anzahl von Bedingungen)
- **Speicherkomplexität**: O(1), nur sechs Boolean-Variablen

**Alternative Lösungsansätze**:

**Ansatz 1: Liste von Bedingungen (flexibler)**
```python
bedingungen = [
    (not_aus_ok, "Not-Aus-Schalter gedrückt"),
    (schutztuer_ok, "Schutztür offen"),
    # ...
]
alle_ok = all(bedingung for bedingung, _ in bedingungen)
```
- ✅ Vorteile: Leicht erweiterbar, iterierbar
- ❌ Nachteile: Weniger explizit, schwerer zu debuggen

**Ansatz 2: Dictionary für Sensorwerte (skalierbar)**
```python
sensoren = {
    "not_aus": True,
    "schutztuer": False,
    # ...
}
alle_ok = all(sensoren.values())
```
- ✅ Vorteile: Gut für viele Sensoren, benennbare Keys
- ❌ Nachteile: Verliert Reihenfolge (vor Python 3.7), weniger typsicher

**Erweiterungsmöglichkeiten**:

1. **Zeitverzögerung**: Not-Aus sollte sofort wirken, aber Zwei-Hand-Bedienung kann 0,5 s tolerieren
2. **Prioritäten**: Not-Aus ist kritischer als Hydraulikdruck
3. **Logging**: Jede Sicherheitsverletzung sollte mit Timestamp gespeichert werden
4. **Redundanz**: Kritische Sensoren (Not-Aus, Schutztür) sollten doppelt vorhanden sein (2-Kanal-Architektur)

**Häufige Fehler**:

- **OR statt AND verwenden**: `not_aus_ok OR schutztuer_ok` würde bedeuten, dass **eine** Bedingung reicht → hochgefährlich!
- **Boolean-Eingabe nicht normalisieren**: `input()` gibt immer String zurück, auch "0" ist truthy!
- **Fail-Safe vergessen**: Bei Sensorfehler (None, Timeout) sollte Default `False` sein, nicht `True`
- **Zwei-Hand-Bedienung mit OR**: `taster1 OR taster2` statt `taster1 AND taster2` → nur ein Taster würde reichen!

**Praxisrelevanz**:

Dieses Programm ist eine **vereinfachte, aber realistische Simulation** echter SPS-Sicherheitslogik. In der Industrie würde diese Logik in einer **zertifizierten Sicherheits-SPS** (z.B. Siemens S7-1500F, Pilz PSS 4000) laufen, die nach ISO 13849 PLe und SIL 3 (IEC 62061) zertifiziert ist. Die Boolean-Logik ist identisch, aber die Hardware muss redundant, selbsttestend und fehlersicher sein.

---

**🎓 Pädagogischer Hinweis**:

Diese Aufgabe zeigt, dass **Boolean-Algebra nicht nur Mathematik** ist, sondern **Leben rettet**. Ein einziger logischer Fehler (`OR` statt `AND`, `not` vergessen) kann in der Industrie zu schweren Unfällen führen. Die explizite Schreibweise (`and` statt `&`, klare Variablennamen) ist hier nicht nur guter Stil, sondern **sicherheitskritisch** und Teil der Norm EN 62304 (Software für medizinische Geräte) und DO-178C (Software für Luftfahrt).
