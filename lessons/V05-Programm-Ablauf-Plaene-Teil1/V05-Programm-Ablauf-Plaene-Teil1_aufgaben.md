# V05: Übungsaufgaben - Programm-Ablauf-Pläne & Verzweigungen

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V05.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: PAP-Symbole identifizieren (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Ordne die folgenden PAP-Symbole ihrer korrekten Bedeutung zu:

1. Abgerundetes Rechteck (Oval)
2. Rechteck
3. Raute (Diamant)
4. Parallelogramm

**Mögliche Bedeutungen:**
- A) Ein-/Ausgabe-Operation
- B) Start oder Ende des Programms
- C) Entscheidung / Verzweigung
- D) Prozess / Anweisung

**Zusatzfrage:** Nach welchem Standard sind PAP-Symbole normiert? Nenne mindestens eine Norm.

**Hinweise**:
- Erinnere dich an die Form der Symbole aus dem Skript
- Die Standardisierung wurde in der Vorlesung ausführlich behandelt

---

### Aufgabe T2: PAP erstellen für einfachen Algorithmus (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Erstelle einen vollständigen Programm-Ablauf-Plan für den folgenden Algorithmus:

**Algorithmus: "Rabattberechnung"**

1. Starte das Programm
2. Lies den Einkaufswert ein (Variable: `betrag`)
3. Wenn der Betrag größer oder gleich 50 Euro ist:
   - Berechne 10% Rabatt: `rabatt = betrag * 0.10`
   - Berechne den Endbetrag: `endbetrag = betrag - rabatt`
4. Wenn der Betrag kleiner als 50 Euro ist:
   - Setze Rabatt auf 0: `rabatt = 0`
   - Setze Endbetrag gleich Betrag: `endbetrag = betrag`
5. Gib den Endbetrag aus
6. Beende das Programm

**Anforderungen:**
- Verwende die korrekten PAP-Symbole (Start/Ende, Prozess, Entscheidung, Ein-/Ausgabe)
- Beschrifte alle Pfeile bei Entscheidungen mit "Ja" / "Nein"
- Sorge für einen klaren, von oben nach unten fließenden Ablauf

**Hinweise**:
- Du kannst den PAP per Hand zeichnen oder ein Tool wie Draw.io, Lucidchart oder Mermaid verwenden
- Achte darauf, dass sich die Pfade nach der Verzweigung wieder zusammenführen

---

### Aufgabe T3: Grundstrukturen analysieren und optimieren (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Gegeben ist folgender PAP in beschreibender Form für einen **Login-Prozess**:

```
1. Start
2. Eingabe: Benutzername
3. Eingabe: Passwort
4. Entscheidung: Ist Benutzername korrekt?
   - Nein → Ausgabe: "Benutzername falsch" → Springe zu Schritt 10 (Ende)
   - Ja → weiter zu Schritt 5
5. Entscheidung: Ist Passwort korrekt?
   - Nein → Ausgabe: "Passwort falsch" → Springe zu Schritt 10
   - Ja → weiter zu Schritt 6
6. Ausgabe: "Login erfolgreich"
7. Entscheidung: Ist Benutzer Administrator?
   - Ja → Ausgabe: "Admin-Panel geladen"
   - Nein → Ausgabe: "Benutzer-Dashboard geladen"
8. (Beide Pfade führen hier zusammen)
9. Ausgabe: "Willkommen!"
10. Ende
```

**Aufgaben:**

a) **Identifiziere die drei Grundstrukturen**:
   - Wo findest du **Sequenzen** (einfache Folgen von Anweisungen)?
   - Wo findest du **Verzweigungen** (if-else Strukturen)?
   - Gibt es **Schleifen** (Wiederholungen)? Wenn nein, wo könnte man eine sinnvoll einbauen?

b) **Erstelle den vollständigen PAP**:
   - Zeichne den PAP mit allen Symbolen und Pfeilen
   - Achte auf klare Beschriftung bei Verzweigungen

c) **Optimierungsvorschlag**:
   - Der aktuelle Ablauf erlaubt nur **einen** Login-Versuch
   - Erweitere den PAP um eine **Schleife**, die dem Benutzer **3 Versuche** für die Eingabe gibt
   - Füge einen Zähler hinzu, der die Anzahl der Versuche speichert
   - Nach 3 fehlgeschlagenen Versuchen soll "Konto gesperrt" ausgegeben werden

**Hinweise**:
- Beginne mit Teil (a) und (b), bevor du die Optimierung angehst
- Für die Schleife benötigst du eine Zählvariable (z.B. `versuche`) und eine Entscheidung mit Rücksprung
- Überlege dir, wann die Schleife abgebrochen werden soll (erfolgreicher Login ODER 3 Versuche)

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Einfache if-Anweisung - CNC-Drehzahl-Warnung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `input()`, `int()`, `if`, Vergleichsoperatoren

Schreibe ein Python-Programm für eine **CNC-Maschine**, das die aktuelle **Spindeldrehzahl** (in U/min) überprüft. Wenn die Drehzahl **3000 U/min oder höher** ist, soll die Warnung **"⚠️ WARNUNG: Hohe Drehzahl! Werkzeugverschleiß prüfen."** ausgegeben werden. Wenn die Drehzahl unter 3000 U/min ist, soll **keine Ausgabe** erfolgen (nur die einfache if-Anweisung ohne else).

> [!NOTE]
> **CNC-Spindeldrehzahl**: Die Umdrehungsgeschwindigkeit des Werkzeugs/Werkstücks. Hohe Drehzahlen (>3000 U/min) erhöhen den Verschleiß und erfordern regelmäßige Wartung.

**Beispiel Ein-/Ausgabe**:
```
Eingabe: Aktuelle Spindeldrehzahl (U/min): 3500
Ausgabe: ⚠️ WARNUNG: Hohe Drehzahl! Werkzeugverschleiß prüfen.
```

```
Eingabe: Aktuelle Spindeldrehzahl (U/min): 2500
Ausgabe: (keine Ausgabe, Programm endet einfach)
```

**Starter-Code**:
```python
# Dein Code hier
drehzahl = int(input("Aktuelle Spindeldrehzahl (U/min): "))

# Implementiere die if-Anweisung
```

**Hinweise**:
- Verwende `int()` um die Eingabe in eine Ganzzahl zu konvertieren
- Die Bedingung soll prüfen, ob `drehzahl >= 3000`
- Typische CNC-Drehzahlen: Bohren 1000-3000 U/min, Fräsen 2000-8000 U/min, Drehen 500-2000 U/min

---

### Aufgabe P2: if-else für binäre Entscheidung - Hydraulikdruck-Monitor (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `input()`, `float()`, `if-else`, Vergleichsoperatoren, f-Strings

Schreibe ein Programm zur **Hydraulikdruck-Überwachung** einer Presse. Das Programm soll den aktuellen **Systemdruck in bar** abfragen.

- Wenn der Druck **unter 50 bar** liegt, gib aus: **"❌ FEHLER: Druck zu niedrig ({druck} bar). Pumpe prüfen!"**
- Ansonsten gib aus: **"✅ Druck OK ({druck} bar). System betriebsbereit."**

> [!NOTE]
> **Hydraulikdruck**: Der Arbeitsdruck in hydraulischen Systemen. Typische Bereiche:
> - Mobil hydraulik (Bagger, Krane): 150-350 bar
> - Industriehydraulik (Pressen): 50-250 bar
> - Niederdruck-Systeme: < 50 bar (oft Fehler oder Leckage)

**Beispiel Ein-/Ausgabe**:
```
Eingabe: Systemdruck (bar): 35.5
Ausgabe: ❌ FEHLER: Druck zu niedrig (35.5 bar). Pumpe prüfen!
```

```
Eingabe: Systemdruck (bar): 180.0
Ausgabe: ✅ Druck OK (180.0 bar). System betriebsbereit.
```

**Zusatzaufgabe (optional):**
Erweitere das Programm so, dass es auch den **Druck in PSI** (Pound per Square Inch) ausgibt. Die Formel lautet: `psi = bar * 14.5038`

**Beispiel mit PSI**:
```
Eingabe: Systemdruck (bar): 200
Ausgabe: ✅ Druck OK (200.0 bar / 2900.76 PSI). System betriebsbereit.
```

**Hinweise**:
- Verwende `float()` für die Eingabe, da Druckwerte Dezimalstellen haben können
- Nutze f-Strings für die formatierte Ausgabe: `f"{druck} bar"`
- Für PSI-Konvertierung: `psi = druck * 14.5038` und Format mit 2 Dezimalstellen: `f"{psi:.2f}"`

---

### Aufgabe P3: if-elif-else für mehrfache Verzweigung - Materialspannungs-Klassifikation (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `input()`, `float()`, `if-elif-else`, Vergleichsoperatoren

Erstelle einen **Spannungs-Klassifikator** für Materialtests. Die **mechanische Spannung** $ \sigma $ (Sigma) wird berechnet als:

$$\sigma = \frac{F}{A}$$

wobei:
- $ F $ = aufgebrachte Kraft in Newton [N]
- $ A $ = Querschnittsfläche in Quadratmillimetern [mm²]
- $ \sigma $ = mechanische Spannung in Megapascal [MPa] (da 1 MPa = 1 N/mm²)

Das Programm soll:
1. Nach **Kraft F in Newton** fragen
2. Nach **Querschnittsfläche A in mm²** fragen
3. Die Spannung $ \sigma $ berechnen
4. Eine Materialklasse ausgeben basierend auf dieser Tabelle (für Baustahl S235):

| Spannung $ \sigma $ [MPa] | Klassifikation | Beschreibung |
|-------------------------|----------------|--------------|
| $ \sigma < 100 $ | Niedrigspannung | Sicher, weit unter Streckgrenze |
| $ 100 \leq \sigma < 235 $ | Betriebsspannung | Normal, im zulässigen Bereich |
| $ 235 \leq \sigma < 360 $ | Grenzspannung | Achtung! Nahe/über Streckgrenze |
| $ \sigma \geq 360 $ | Bruchspannung | GEFAHR! Material versagt! |

> [!NOTE]
> **Mechanische Spannung**: Die innere Kraft pro Flächeneinheit in einem belasteten Bauteil. Wichtige Kennwerte für Baustahl S235:
> - **Streckgrenze** $ R_e $ = 235 MPa (Material beginnt plastisch zu verformen)
> - **Zugfestigkeit** $ R_m $ = 360-510 MPa (Material bricht)
> - **E-Modul** $ E $ = 210.000 MPa (Steifigkeit)

**Beispiel Ein-/Ausgabe**:
```
Eingabe: Kraft F (N): 50000
Eingabe: Querschnittsfläche A (mm²): 250
Ausgabe: Spannung σ: 200.00 MPa
Ausgabe: Klassifikation: Betriebsspannung (Normal, im zulässigen Bereich)
```

```
Eingabe: Kraft F (N): 100000
Eingabe: Querschnittsfläche A (mm²): 250
Ausgabe: Spannung σ: 400.00 MPa
Ausgabe: Klassifikation: Bruchspannung (GEFAHR! Material versagt!)
```

**Hinweise**:
- Verwende `float()` für beide Eingaben
- Berechne die Spannung mit: `sigma = kraft / flaeche` (Ergebnis automatisch in MPa, da N/mm²)
- Formatiere die Spannung auf 2 Dezimalstellen: `f"{sigma:.2f}"`
- Verwende if-elif-else um die Klassifikationen zu unterscheiden
- **Achtung**: Prüfe auf Division durch Null! Wenn Fläche = 0, gib Fehlermeldung aus

---

### Aufgabe P4: Verschachtelte Bedingungen - CNC-Bearbeitungskosten-Rechner (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: `input()`, `float()`, verschachtelte if-Anweisungen, logische Operatoren (`and`, `or`)

Erstelle einen **Bearbeitungskosten-Rechner** für eine CNC-Werkstatt mit folgenden Regeln:

**Preisstruktur:**
- **Grundkosten** (Maschinenstundensatz): 80 EUR/Stunde
- **Materialaufschläge:**
  - Aluminium (Material-Code 1): + 15 EUR/kg
  - Stahl (Material-Code 2): + 10 EUR/kg
  - Edelstahl (Material-Code 3): + 25 EUR/kg
- **Bearbeitungskomplexität (Zusatzkosten pro Stunde):**
  - Einfach (2D-Fräsen, Bohren): + 0 EUR
  - Mittel (3D-Fräsen, Gewinde): + 20 EUR/Stunde
  - Komplex (5-Achs-Bearbeitung): + 50 EUR/Stunde
- **Mengenrabatt:**
  - Ab 10 Stück: 10% Rabatt auf Gesamtkosten
  - Ab 50 Stück: 20% Rabatt auf Gesamtkosten
  - Ab 100 Stück: 30% Rabatt auf Gesamtkosten
- **Express-Zuschlag:**
  - Wenn Express-Bearbeitung gewünscht: + 50% auf Gesamtkosten (wird NACH Mengenrabatt berechnet)

> [!NOTE]
> **CNC-Kostenkalkulation**: Maschinenstundensätze umfassen Abschreibung, Energie, Werkzeugverschleiß und Personal. Materialkosten werden nach Gewicht berechnet. Komplexität bestimmt den Zeitaufwand und Programmieraufwand.

Das Programm soll fragen:
1. **Bearbeitungszeit** in Stunden
2. **Material-Code** (1=Aluminium, 2=Stahl, 3=Edelstahl)
3. **Materialgewicht** in kg
4. **Komplexität** (1=Einfach, 2=Mittel, 3=Komplex)
5. **Stückzahl**
6. **Express-Bearbeitung?** (j/n)

Dann sollen die finalen Gesamtkosten berechnet und ausgegeben werden.

**Berechnungslogik:**
1. **Maschinenkosten** = (Grundkosten + Komplexitätszuschlag) × Bearbeitungszeit
2. **Materialkosten** = Materialpreis pro kg × Materialgewicht
3. **Stückkosten** = Maschinenkosten + Materialkosten
4. **Gesamtkosten (vor Rabatt)** = Stückkosten × Stückzahl
5. **Gesamtkosten (nach Mengenrabatt)** = Gesamtkosten × (1 - Rabatt)
6. **Endkosten** = Gesamtkosten × (1.5 falls Express, sonst 1.0)

**Beispiel Ein-/Ausgabe**:
```
Eingabe: Bearbeitungszeit (h): 2.5
Eingabe: Material-Code (1=Alu, 2=Stahl, 3=Edelstahl): 2
Eingabe: Materialgewicht (kg): 5
Eingabe: Komplexität (1=Einfach, 2=Mittel, 3=Komplex): 1
Eingabe: Stückzahl: 1
Eingabe: Express-Bearbeitung? (j/n): n

Ausgabe: 
=== CNC-Bearbeitungskosten ===
Maschinenkosten: 200.00 EUR (80 EUR/h × 2.5 h)
Materialkosten: 50.00 EUR (10 EUR/kg × 5 kg Stahl)
Stückkosten: 250.00 EUR
Gesamtkosten: 250.00 EUR (1 Stück)
Mengenrabatt: 0%
Express-Zuschlag: Nein
────────────────────────────
ENDKOSTEN: 250.00 EUR
```

```
Eingabe: Bearbeitungszeit (h): 3
Eingabe: Material-Code (1=Alu, 2=Stahl, 3=Edelstahl): 3
Eingabe: Materialgewicht (kg): 2
Eingabe: Komplexität (1=Einfach, 2=Mittel, 3=Komplex): 3
Eingabe: Stückzahl: 15
Eingabe: Express-Bearbeitung? (j/n): j

Ausgabe:
=== CNC-Bearbeitungskosten ===
Maschinenkosten: 390.00 EUR ((80+50) EUR/h × 3 h)
Materialkosten: 50.00 EUR (25 EUR/kg × 2 kg Edelstahl)
Stückkosten: 440.00 EUR
Gesamtkosten: 6600.00 EUR (15 Stück)
Mengenrabatt: 10% → 5940.00 EUR
Express-Zuschlag: +50% → 8910.00 EUR
────────────────────────────
ENDKOSTEN: 8910.00 EUR
```

**Hinweise**:
- Verwende verschachtelte if-elif-else für Material-Code und Komplexität
- Berechne schrittweise: Maschinenkosten → Materialkosten → Stückkosten → Gesamtkosten → Rabatt → Express
- Formatiere alle Preise mit 2 Dezimalstellen: `f"{preis:.2f}"`
- Nutze aussagekräftige Variablennamen: `maschinenkosten`, `materialkosten`, `stueckkosten`, etc.

---

### Aufgabe P5: PAP zu Python-Code übersetzen - Werkstoffprüfung-Validator (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Alle bisherigen Konzepte + String-Methoden

Gegeben ist folgender **Programm-Ablauf-Plan** in textueller Beschreibung für einen **Werkstoffprüfungs-Validator**, der Zugversuchs-Protokolle auf Vollständigkeit und Normkonformität prüft:

> [!NOTE]
> **Zugversuch**: Standardisierter Materialtest nach DIN EN ISO 6892-1. Eine Probe wird bis zum Bruch gedehnt, dabei werden Kennwerte wie Zugfestigkeit $ R_m $, Streckgrenze $ R_e $ und Bruchdehnung $ A $ ermittelt. Normkonforme Protokolle müssen alle Pflichtangaben enthalten.

```
1. Start
2. Eingabe: Protokoll-ID (String, z.B. "ZV-2024-0123")
3. Initialisiere Qualität-Punkte = 0
4. Entscheidung: Enthält Protokoll mindestens 8 Zeichen?
   - Ja: Qualität += 1
   - Nein: (nichts)
5. Entscheidung: Beginnt Protokoll mit "ZV-" (Zugversuch)?
   - Ja: Qualität += 1
   - Nein: (nichts)
6. Entscheidung: Enthält Protokoll mindestens eine Ziffer?
   - Ja: Qualität += 1
   - Nein: (nichts)
7. Entscheidung: Enthält Protokoll mindestens einen Großbuchstaben?
   - Ja: Qualität += 1
   - Nein: (nichts)
8. Entscheidung: Enthält Protokoll mindestens einen Bindestrich "-"?
   - Ja: Qualität += 1
   - Nein: (nichts)
9. Bewerte die Qualität:
   - Qualität == 5: "Vollständig normkonform (DIN EN ISO 6892-1)"
   - Qualität == 4: "Weitgehend konform (1 Kriterium fehlt)"
   - Qualität == 3: "Teilweise konform (2 Kriterien fehlen)"
   - Qualität <= 2: "Nicht normkonform (Protokoll ungültig)"
10. Ausgabe: Protokoll-Qualität und Bewertung
11. Ende
```

**Aufgabe:**

Implementiere diesen PAP in Python. Das Programm soll:
1. Eine Protokoll-ID vom Benutzer einlesen
2. Alle 5 Qualitätskriterien prüfen
3. Die Qualitäts-Punktzahl berechnen
4. Eine Bewertung ausgeben

**Die 5 Prüfkriterien:**
1. **Länge** ≥ 8 Zeichen
2. **Format-Check**: Beginnt mit "ZV-" (Zugversuch)
3. **Ziffer vorhanden**: Mindestens eine Ziffer für Jahr/Nummer
4. **Großbuchstaben vorhanden**: Mindestens ein Großbuchstabe (Z, V)
5. **Bindestrich vorhanden**: Mindestens ein "-" (Trennzeichen)

**Beispiel Ein-/Ausgabe**:
```
Eingabe: Protokoll-ID: ZV-2024-0123
Ausgabe: 
Protokoll-Analyse: ZV-2024-0123
✅ Länge: Ausreichend (13 Zeichen)
✅ Format: Korrekt (beginnt mit "ZV-")
✅ Ziffern: Vorhanden
✅ Großbuchstaben: Vorhanden
✅ Bindestriche: Vorhanden
────────────────────────────
Qualität: 5/5 Punkte
Bewertung: Vollständig normkonform (DIN EN ISO 6892-1)
```

```
Eingabe: Protokoll-ID: test123
Ausgabe:
Protokoll-Analyse: test123
✅ Länge: Ausreichend (7 Zeichen... Moment, zu kurz!)
❌ Format: Fehlerhaft (beginnt nicht mit "ZV-")
✅ Ziffern: Vorhanden
❌ Großbuchstaben: Fehlen
❌ Bindestriche: Fehlen
────────────────────────────
Qualität: 2/5 Punkte
Bewertung: Nicht normkonform (Protokoll ungültig)
```

**Hilfe für die Implementierung:**

- **Längencheck**: `len(protokoll) >= 8`
- **Format-Check (beginnt mit "ZV-")**: `protokoll.startswith("ZV-")`
- **Ziffer-Check**: `any(zeichen.isdigit() for zeichen in protokoll)`
- **Großbuchstaben-Check**: `any(zeichen.isupper() for zeichen in protokoll)`
- **Bindestrich-Check**: `"-" in protokoll`

**Bonus-Challenge** (optional):
Erweitere das Programm so, dass es dem Benutzer **konkrete Korrekturvorschläge** gibt, welche Kriterien fehlen. Beispiel:
```
Ausgabe: Bewertung: Nicht normkonform (Protokoll ungültig)
Ausgabe: 
Korrekturvorschläge:
- ❌ Protokoll-ID muss mit "ZV-" beginnen (für Zugversuch)
- ❌ Mindestens ein Großbuchstabe erforderlich
- ❌ Mindestens ein Bindestrich "-" erforderlich
```

**Erweiterte Challenge** (für Fortgeschrittene):
Implementiere eine **vollständige Format-Validierung** mit regulären Ausdrücken (Modul `re`):
```python
import re
pattern = r"^ZV-\d{4}-\d{4}$"  # ZV-JJJJ-NNNN
if re.match(pattern, protokoll):
    print("✅ Format exakt korrekt: ZV-JJJJ-NNNN")
```

**Hinweise**:
- Verwende String-Methoden wie `.isdigit()`, `.isupper()`, `.startswith()`
- Die `any()`-Funktion prüft, ob mindestens ein Element in einem Iterable `True` ist
- Strukturiere deinen Code mit klaren Variablennamen: `laenge_ok`, `format_ok`, `ziffer_ok`, etc.
- Verwende Emojis (✅/❌) für bessere Lesbarkeit der Ausgabe
