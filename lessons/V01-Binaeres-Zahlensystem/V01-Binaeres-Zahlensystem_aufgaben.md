# V01: Übungsaufgaben - Binäres Zahlensystem

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V01.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Zahlensystem-Umrechnung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Rechne die folgenden Zahlen in die jeweils angegebenen Zahlensysteme um:

a) **13₁₀** → Binär  
b) **1101₂** → Dezimal  
c) **2A₁₆** → Binär  
d) **11111111₂** → Hexadezimal  

**Hinweise**:
- Für Dezimal → Binär: Verwende das Divisionsverfahren (fortgesetzte Division durch 2)
- Für Binär → Dezimal: Berechne die Stellenwerte (Zweierpotenzen)
- Für Hexadezimal ↔ Binär: Denke daran, dass eine Hex-Ziffer genau 4 Binärziffern entspricht

---

### Aufgabe T2: Binäre Addition und Subtraktion (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Führe die folgenden binären Rechenoperationen durch. Gib jeweils den Rechenweg und das Ergebnis in binärer und dezimaler Form an.

a) **10110₂ + 1101₂**  
b) **11001₂ + 10111₂**  
c) **10110₂ - 1101₂**  
d) **100000₂ - 10101₂**  

**Hinweise**:
- Achte auf Überträge bei der Addition
- Bei der Subtraktion musst du eventuell von höherwertigen Stellen borgen
- Überprüfe deine Ergebnisse, indem du die dezimalen Werte ausrechnest

---

### Aufgabe T3: Zweierkomplement und negative Zahlen (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Gegeben seien 8-Bit Zahlen im Zweierkomplement.

a) Bilde das Zweierkomplement (negative Darstellung) der folgenden positiven Zahlen:
   - **42₁₀**
   - **127₁₀**

b) Welche Dezimalzahl wird durch die folgenden 8-Bit-Zweierkomplement-Zahlen dargestellt?
   - **10110110₂**
   - **11111111₂**
   - **10000000₂**

c) Führe die folgende Subtraktion durch Addition mit dem Zweierkomplement aus:
   - **50₁₀ - 30₁₀** (8-Bit)
   - Zeige den Rechenweg: Wandle beide Zahlen in binär um, bilde das Zweierkomplement von 30, addiere, ignoriere den Überlauf

d) Was ist der kleinste und größte darstellbare Wert bei 8-Bit im Zweierkomplement? Begründe deine Antwort.

**Hinweise**:
- Bei negativen Zweierkomplement-Zahlen ist das höchstwertige Bit (MSB) immer 1
- Um von Zweierkomplement zu Dezimal zu konvertieren: Wenn MSB = 1, bilde das Zweierkomplement und negiere das Ergebnis
- Bei Addition im Zweierkomplement wird ein Überlauf über das 8. Bit hinaus ignoriert

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Maschinendatenerfassung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `print()`, `input()`, Variablen  
**Maschinenbau-Kontext**: Erfassung und Protokollierung von Maschinenbetriebsdaten in der Werkstatt

Schreibe ein Python-Programm, das Basisdaten einer CNC-Maschine erfasst und ein Betriebsprotokoll erstellt.

**Anforderungen:**
- Frage nach der Maschinenbezeichnung (z.B. "CNC-Fräse-001")
- Frage nach den bisherigen Betriebsstunden
- Gib die eingegebenen Daten formatiert aus
- Berechne und zeige, wann die nächste Wartung fällig ist (nach weiteren 500 Betriebsstunden)

**Beispiel Ein-/Ausgabe**:
```
Maschinenbezeichnung: CNC-Fräse-001
Aktuelle Betriebsstunden: 2340
--- Betriebsprotokoll ---
Maschine: CNC-Fräse-001
Betriebsstunden: 2340 h
Nächste Wartung bei: 2840 h
```

**Starter-Code**:
```python
# Dein Code hier
```

---

### Aufgabe P2: Drehzahl-Umrechner (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `print()`, `input()`, Variablen, arithmetische Operatoren, Typkonvertierung  
**Maschinenbau-Kontext**: Umrechnung von Drehzahlen für Werkzeugmaschinen und Motoren

Schreibe ein Python-Programm, das Drehzahlen von U/min (Umdrehungen pro Minute) in rad/s (Radiant pro Sekunde) umrechnet.

**Anforderungen:**
- Frage den Benutzer nach einer Drehzahl in U/min
- Rechne die Drehzahl in rad/s um (Formel: rad/s = U/min × 2π / 60)
- Gib das Ergebnis mit sinnvollem Text aus
- **Bonus:** Rechne auch die Winkelgeschwindigkeit zurück nach U/min

**Beispiel Ein-/Ausgabe**:
```
=== Drehzahl-Umrechner für Werkzeugmaschinen ===
Drehzahl in U/min: 1500
1500.0 U/min entspricht 157.08 rad/s
Kontrolle: 157.08 rad/s = 1500.0 U/min
```

**Hinweise**:
- Verwende für Pi den Wert: `pi = 3.14159265359`
- Formel: 1 U/min = (2π / 60) rad/s ≈ 0.10472 rad/s
- Denke daran, `input()` in `float()` zu konvertieren

---

### Aufgabe P3: Materialspannungs-Rechner (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `print()`, `input()`, Variablen, arithmetische Operatoren, Typkonvertierung  
**Maschinenbau-Kontext**: Berechnung mechanischer Spannungen in Bauteilen

Schreibe ein Programm zur Berechnung von mechanischen Spannungen in einem Zugstab.

**Anforderungen:**
- Frage nach der wirkenden Kraft F in Newton (N)
- Frage nach der Querschnittsfläche A in mm²
- Berechne die Normalspannung σ (sigma) in N/mm² (MPa)
- Berechne die Normalspannung auch in Pa (Pascal) für SI-Einheit
- Gib alle Ergebnisse übersichtlich formatiert aus

**Formeln:**
- Normalspannung: σ = F / A (in N/mm²)
- Umrechnung: 1 N/mm² = 1 MPa = 1.000.000 Pa

**Beispiel Ein-/Ausgabe**:
```
=== Materialspannungs-Rechner ===
Kraft F (in N): 50000
Querschnittsfläche A (in mm²): 200

Berechnungsergebnisse:
Normalspannung σ = 250.0 N/mm² (MPa)
Normalspannung σ = 250000000.0 Pa
Normalspannung σ = 250.0 MPa
```

**Hinweise**:
- Verwende aussagekräftige Variablennamen (kraft, flaeche, spannung)
- 1 MPa = 1 N/mm² = 10⁶ Pa
- Achte auf übersichtliche Formatierung der Ausgabe

---

### Aufgabe P4: Binär-Sensor-Dekoder (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: `print()`, `input()`, Variablen, Berechnungen, String-Operationen  
**Maschinenbau-Kontext**: Auswertung binärer Sensordaten von Industriemaschinen (z.B. Status-Bits)

Schreibe ein Python-Programm, das einen 8-Bit-Statuscode einer Maschine (als binäre Zahl eingegeben) in eine Dezimalzahl umrechnet und interpretiert.

**Anforderungen:**
- Frage den Benutzer nach einem 8-Bit-Statuscode (z.B. "10110100")
- Berechne manuell den dezimalen Wert (ohne die eingebaute `int(x, 2)` Funktion!)
- Zeige das Ergebnis an
- Zeige zusätzlich die Berechnung Schritt für Schritt

**Teilaufgaben:**

**a) Grundversion**: Nimm an, dass die Eingabe genau 8 Bit lang ist.

**b) Erweiterung**: Zeige zusätzlich die Berechnung Schritt für Schritt an und interpretiere den Status.

**Statuscode-Bedeutung** (zur Information):
- Bit 0 (rechts): Motor läuft (1) / steht (0)
- Bit 1: Kühlmittel aktiv (1) / inaktiv (0)
- Bit 2: Notaus gedrückt (1) / normal (0)
- Bit 3: Tür offen (1) / geschlossen (0)
- Bits 4-7: Fehlercodes (Dezimalwert 0-15)

**Beispiel Ein-/Ausgabe**:
```
=== Binär-Sensor-Dekoder ===
Gib den 8-Bit-Statuscode ein: 10110100

Berechnung:
Bit 7: 1 * 128 = 128
Bit 6: 0 * 64 = 0
Bit 5: 1 * 32 = 32
Bit 4: 1 * 16 = 16
Bit 3: 0 * 8 = 0
Bit 2: 1 * 4 = 4
Bit 1: 0 * 2 = 0
Bit 0: 0 * 1 = 0

Summe: 128 + 0 + 32 + 16 + 0 + 4 + 0 + 0 = 180
Der Statuscode 10110100 entspricht dem Dezimalwert 180

Status-Interpretation:
- Motor: STEHT
- Kühlmittel: INAKTIV
- Notaus: AKTIV (!)
- Tür: GESCHLOSSEN
- Fehlercode: 11 (Binär: 1011)
```

**Hinweise**:
- Du kannst auf einzelne Zeichen eines Strings mit Indizes zugreifen: `code[0]` gibt das erste Zeichen
- Die Länge eines Strings bekommst du mit `len(code)`
- Du musst die Zweierpotenzen selbst berechnen (z.B. mit `**`-Operator)
- Strings müssen in Zahlen konvertiert werden: `int("1")` ergibt `1`

---

### Aufgabe P5: Getriebe-Berechnungs-Programm (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: `print()`, `input()`, Variablen, Berechnungen, Formatierung  
**Maschinenbau-Kontext**: Berechnung von Getriebeparametern für Übersetzungsverhältnisse

Schreibe ein umfassendes Programm zur Berechnung verschiedener Getriebepa rameter bei einfachen Stirnradgetrieben.

**Anforderungen:**

Das Programm soll dem Benutzer ein Menü anbieten:
1. Berechnung bei gegebenem Übersetzungsverhältnis i
2. Berechnung bei gegebenen Zähnezahlen (z₁ und z₂)
3. Berechnung bei gegebenen Drehzahlen (n₁ und n₂)
4. Berechnung bei gegebenem Abtriebsmoment und Wirkungsgrad

Abhängig von der Auswahl soll das Programm die entsprechenden Eingaben einfordern und dann **alle** anderen relevanten Werte berechnen und ausgeben.

**Formeln:**
- Übersetzungsverhältnis: $i = \frac{n_1}{n_2} = \frac{z_2}{z_1}$
- Drehzahl Abtrieb: $n_2 = \frac{n_1}{i}$
- Drehmoment Abtrieb: $M_2 = M_1 \times i \times \eta$ (η = Wirkungsgrad)

**Beispiel Ein-/Ausgabe**:
```
=== Getriebe-Berechnungs-Programm ===

Wähle eine Option:
1. Übersetzungsverhältnis gegeben
2. Zähnezahlen gegeben
3. Drehzahlen gegeben
4. Antriebswerte gegeben (n₁, M₁, i, η)

Deine Wahl: 1
Gib das Übersetzungsverhältnis i ein: 3.5
Gib die Antriebsdrehzahl n₁ ein (U/min): 1500
Gib das Antriebsmoment M₁ ein (Nm): 50
Gib den Wirkungsgrad η ein (0-1): 0.95

Ergebnisse für ein Getriebe mit i = 3.5:
- Abtriebsdrehzahl n₂: 428.57 U/min
- Abtriebsmoment M₂: 166.25 Nm
- Leistungsverlust: 5.0 %
```

**Hinweise**:
- Verwende aussagekräftige Variablennamen
- Strukturiere dein Programm logisch mit Kommentaren
- Der Wirkungsgrad η (eta) liegt typischerweise zwischen 0.90 und 0.98
- Bei der Drehmomentberechnung gilt: Hohe Übersetzung → hohes Abtriebsmoment, aber niedrige Drehzahl

**Bonus-Challenge**:
Erweitere das Programm so, dass es auch prüft, ob das berechnete Abtriebsmoment innerhalb der zulässigen Grenzen für ein gegebenes Getriebe liegt (z.B. M₂ max = 200 Nm). Gib eine entsprechende Warnung aus, falls der Wert überschritten wird.

(Hinweis: Verzweigungen mit if-elif-else werden erst in V05 behandelt, aber du kannst versuchen, die Grundversion ohne Fallunterscheidung zu implementieren)
