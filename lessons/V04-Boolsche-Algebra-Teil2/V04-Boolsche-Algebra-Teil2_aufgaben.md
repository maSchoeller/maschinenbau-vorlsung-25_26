# V04: Übungsaufgaben - Boolsche Algebra & Logische Schaltungen – Teil 2

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V04.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: XOR und Grundoperatoren (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

XOR (Exklusives ODER) kann durch die Grundoperatoren AND, OR und NOT ausgedrückt werden. Gegeben ist die Formel:

$$
A \oplus B = (A \land \neg B) \lor (\neg A \land B)
$$

**Aufgabenstellung**:

Erstelle eine vollständige **Wahrheitstabelle** für die rechte Seite der Gleichung und zeige, dass sie mit der XOR-Wahrheitstabelle übereinstimmt.

**Hinweise**:
- Erstelle Spalten für alle Zwischenergebnisse: $\neg A$, $\neg B$, $A \land \neg B$, $\neg A \land B$
- Vergleiche das Endergebnis mit der XOR-Wahrheitstabelle aus der Vorlesung

---

### Aufgabe T2: De Morgan'sche Gesetze anwenden (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Vereinfache die folgenden logischen Ausdrücke mit Hilfe der **De Morgan'schen Gesetze** so weit wie möglich.

**Aufgabenstellung**:

Vereinfache die folgenden Ausdrücke und gib jeden Zwischenschritt an:

a) $\neg(A \land B \land C)$

b) $\neg((A \lor B) \land C)$

c) $\neg(A \land \neg B) \lor \neg(C \lor D)$

d) $\neg(\neg A \lor (B \land C))$

**Hinweise**:
- De Morgan'sche Gesetze:
  - $\neg(A \land B) = \neg A \lor \neg B$
  - $\neg(A \lor B) = \neg A \land \neg B$
- Doppelte Negation hebt sich auf: $\neg(\neg A) = A$
- Wende die Gesetze schrittweise von innen nach außen an

---

### Aufgabe T3: Volladdierer-Schaltung analysieren (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Ein **Volladdierer** hat die folgenden logischen Gleichungen:

$$
S = A \oplus B \oplus Cin
$$

$$
Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin)
$$

**Aufgabenstellung**:

a) Erstelle eine vollständige **Wahrheitstabelle** für den Volladdierer mit allen drei Eingängen (A, B, Cin) und beiden Ausgängen (S, Cout).

b) Zeige durch schrittweise Auswertung der Formeln, dass für die Eingangskombination **A=1, B=1, Cin=1** die Ausgänge **S=1** und **Cout=1** ergeben.

c) Berechne das Ergebnis der Addition von **1101** (binär, dezimal 13) und **1011** (binär, dezimal 11) mit Hilfe von vier kaskadierten Volladdierern. Zeige für jede Bitstelle:
   - Die Eingänge A, B, Cin
   - Die Ausgänge S, Cout
   - Den Übertrag zur nächsten Stelle

d) Vereinfache die Gleichung für **Cout** unter Verwendung von XOR zu:

$$
Cout = (A \land B) \lor ((A \oplus B) \land Cin)
$$

Beweise die Äquivalenz durch eine Wahrheitstabelle oder algebraische Umformung.

**Hinweise**:
- Bei (c): Beginne bei der niedrigsten Stelle (ganz rechts), Cin der ersten Stelle ist 0
- Der Cout jeder Stelle wird zum Cin der nächsten Stelle
- Prüfe dein Ergebnis: 13 + 11 = 24 dezimal = 11000 binär

---

## Teil B: Python-Aufgaben

### Aufgabe P1: CNC-Kühlmitteltemperatur-Monitor (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: Vergleichsoperatoren, logische Operatoren, verkettete Vergleiche

Schreibe ein Programm, das die Temperatur des Kühlmittels einer CNC-Maschine (z.B. DMG MORI NLX 2500) überwacht und den Betriebsstatus bewertet.

> [!NOTE]
> **Kühlmittel** (Emulsion aus Wasser und Öl) wird in der CNC-Bearbeitung verwendet, um die Werkzeuge zu kühlen, Späne abzutransportieren und die Oberflächenqualität zu verbessern. Die optimale Kühlmitteltemperatur ist entscheidend für Werkzeugstandzeit und Prozessstabilität.

**Aufgabenstellung**:

Erstelle ein Programm, das:
1. Die Kühlmitteltemperatur vom Benutzer einliest (als Float, in °C)
2. Prüft und ausgibt, in welchem Betriebsbereich die Temperatur liegt:
   - **❄️ Zu kalt**: unter 15°C (Kondensationsgefahr, schlechte Kühlleistung)
   - **🟡 Suboptimal kühl**: 15°C bis unter 20°C (funktionsfähig, aber nicht ideal)
   - **🟢 Optimal**: 20°C bis 28°C (einschließlich, beste Schmier- und Kühlwirkung)
   - **🟠 Suboptimal warm**: über 28°C bis 35°C (erhöhter Verschleiß)
   - **🔴 Zu heiß**: über 35°C (Ölanteil zersetzt sich, Maschine sollte gestoppt werden)
3. Zusätzlich prüft, ob die Temperatur im "Idealbereich" (22°C bis 26°C einschließlich) liegt

**Beispiel Ein-/Ausgabe**:
```
CNC-Kühlmittel-Temperatur (°C): 24.5
Betriebsbereich: 🟢 Optimal (20-28°C)
Idealbereich (22-26°C): ✅ Ja - Maximale Werkzeugstandzeit
Empfehlung: Betrieb freigegeben
```

```
CNC-Kühlmittel-Temperatur (°C): 37.2
Betriebsbereich: 🔴 Zu heiß (> 35°C)
Idealbereich (22-26°C): ❌ Nein
Empfehlung: ⚠️ MASCHINE STOPPEN! Kühlmittel prüfen/tauschen!
```

**Starter-Code** (optional):
```python
# Dein Code hier
temperatur = float(input("CNC-Kühlmittel-Temperatur (°C): "))

# Prüfe die Bereiche
# Tipp: Nutze verkettete Vergleiche wie: 20 <= temperatur <= 28
```

**Hintergrundinformationen**:
- **Emulsionskühlmittel** besteht typischerweise aus 5-10% Öl in Wasser
- Bei zu niedrigen Temperaturen: schlechte Fließeigenschaften, Biofilmbildung
- Bei zu hohen Temperaturen: Verdunstung, Ölzersetzung, Bakterienwachstum, schlechter Korrosionsschutz
- **Werkzeugstandzeit** (tool life) kann sich bei optimaler Kühlmitteltemperatur um 30-50% erhöhen
- Norm **VDI 3397** definiert Anforderungen an Kühlschmierstoffe

---

### Aufgabe P2: Hydraulikpress-Parameter-Validierung (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Vergleichsoperatoren, logische Operatoren, String-Methoden (aus V02/V03)

Schreibe ein Programm, das Betriebsparameter einer hydraulischen Presse validiert und prüft, ob sie verschiedene Sicherheits- und Qualitätskriterien erfüllt.

> [!NOTE]
> **Hydraulische Pressen** verwenden Flüssigkeitsdruck (typischerweise Hydrauliköl) zum Umformen von Metallen. Der Druck muss präzise kontrolliert werden, um Qualität zu sichern und Unfälle zu vermeiden (EN 693, Sicherheit von Maschinen - Hydraulische Pressen).

**Aufgabenstellung**:

Erstelle ein Programm, das die Betriebsparameter einer Presse vom Benutzer einliest und folgende Kriterien prüft:

**Eingaben**:
- Hydraulikdruck (bar, als Float)
- Pressengeschwindigkeit (mm/s, als Float)  
- Werkzeug-ID (String, z.B. "WZ-2024-A15")
- Öltemperatur (°C, als Float)

**Validierungskriterien**:

1. **Druckbereich**: 150 bar ≤ Druck ≤ 250 bar (Nenndruck der Presse)
2. **Geschwindigkeit**: 10 mm/s ≤ Geschwindigkeit ≤ 80 mm/s (Sicherheitsbereich)
3. **Werkzeug-ID-Format**: 
   - Mindestens 10 Zeichen
   - Enthält mindestens eine Ziffer
   - Enthält mindestens einen Bindestrich "-"
4. **Öltemperatur**: 40°C ≤ Temperatur ≤ 60°C (optimaler Viskositätsbereich)
5. **Kritische Kombination**: Wenn Druck > 200 bar, dann muss Geschwindigkeit ≤ 50 mm/s sein (Sicherheitsregel)

Das Programm soll für jedes Kriterium ausgeben, ob es erfüllt ist, und am Ende eine Gesamtbewertung ("✅ Betrieb freigegeben" oder "❌ Betrieb gesperrt") ausgeben.

**Beispiel Ein-/Ausgabe**:
```
=== HYDRAULIKPRESS-PARAMETER-VALIDIERUNG ===
Hydraulikdruck (bar): 180.5
Pressengeschwindigkeit (mm/s): 45.0
Werkzeug-ID: WZ-2024-A15
Öltemperatur (°C): 52.3

--- Validierungsergebnisse ---
✅ Druckbereich erfüllt (150-250 bar): 180.5 bar
✅ Geschwindigkeit erfüllt (10-80 mm/s): 45.0 mm/s
✅ Werkzeug-ID-Format korrekt (≥10 Zeichen, Ziffer, Bindestrich): WZ-2024-A15
✅ Öltemperatur optimal (40-60°C): 52.3°C
✅ Sicherheitsregel erfüllt (Druck ≤200 bar ODER Geschwindigkeit ≤50 mm/s)

➡️ BETRIEB FREIGEGEBEN ✅
Alle Parameter im Sollbereich. Pressung kann gestartet werden.
```

```
=== HYDRAULIKPRESS-PARAMETER-VALIDIERUNG ===
Hydraulikdruck (bar): 230.0
Pressengeschwindigkeit (mm/s): 75.0
Werkzeug-ID: ABC123
Öltemperatur (°C): 68.5

--- Validierungsergebnisse ---
✅ Druckbereich erfüllt (150-250 bar): 230.0 bar
✅ Geschwindigkeit erfüllt (10-80 mm/s): 75.0 mm/s
❌ Werkzeug-ID-Format UNGÜLTIG (zu kurz: 6 Zeichen, min. 10 erforderlich)
❌ Öltemperatur außerhalb Sollbereich (40-60°C): 68.5°C - ÖL ZU HEISS!
❌ Sicherheitsregel VERLETZT (Druck >200 bar UND Geschwindigkeit >50 mm/s)

➡️ BETRIEB GESPERRT ❌
3 Kriterien nicht erfüllt. Presse darf NICHT gestartet werden!
```

**Hinweise**:
- Nutze String-Methoden: `.isdigit()`, `len()`, `in` (z.B. `"-" in werkzeug_id`)
- Um zu prüfen, ob *mindestens ein* Zeichen eine Bedingung erfüllt, nutze:
  ```python
  hat_ziffer = any(c.isdigit() for c in werkzeug_id)
  ```
- Die Sicherheitsregel ist eine **IMPLIKATION**: `Wenn Druck > 200, dann Geschwindigkeit ≤ 50`
  - Logisch äquivalent: `(druck <= 200) or (geschwindigkeit <= 50)`
- Zähle die Anzahl erfüllter Kriterien für die Gesamtbewertung

**Hintergrundinformationen**:
- **EN 693**: Europäische Norm für Sicherheit hydraulischer Pressen
- **Viskosität** des Hydrauliköls ist temperaturabhängig: zu kalt → zähflüssig, zu heiß → dünnflüssig
- Bei hohen Drücken und Geschwindigkeiten erhöht sich das Unfallrisiko (kinetische Energie $E_{kin} = \frac{1}{2}mv^2$)
- **Traceability**: Werkzeug-IDs ermöglichen Rückverfolgbarkeit bei Qualitätsproblemen (ISO 9001)

---

### Aufgabe P3: Sensor-Plausibilitätsprüfung mit Kurzschlussauswertung (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: Logische Operatoren, Kurzschlussauswertung, Funktionen

Schreibe ein Programm, das die Kurzschlussauswertung bei `and` und `or` demonstriert und für die Plausibilitätsprüfung von Sensordaten nutzt.

> [!NOTE]
> **Plausibilitätsprüfung** (plausibility check) ist essentiell in der Automatisierung: Sensoren können ausfallen, falsche Werte liefern oder durch EMV-Störungen beeinflusst werden. Kurzschlussauswertung ermöglicht es, teure oder gefährliche Berechnungen erst dann durchzuführen, wenn Vorbedingungen erfüllt sind.

**Aufgabenstellung**:

Erstelle ein Programm mit Sensor-Simulationsfunktionen:

**Teil 1: Kurzschlussauswertung demonstrieren**

Implementiere zwei Funktionen:
1. `pruefe_sensor_a()`: Gibt "🟢 Sensor A: Drucksensor wird abgefragt..." aus und gibt `True` zurück (Sensor funktioniert)
2. `pruefe_sensor_b()`: Gibt "🔴 Sensor B: Temperatursensor wird abgefragt..." aus und gibt `False` zurück (Sensor defekt)

Teste dann folgende logische Ausdrücke und beobachte, welche Funktionen tatsächlich aufgerufen werden:

a) `result = pruefe_sensor_a() and pruefe_sensor_b()`  
b) `result = pruefe_sensor_b() and pruefe_sensor_a()`  
c) `result = pruefe_sensor_a() or pruefe_sensor_b()`  
d) `result = pruefe_sensor_b() or pruefe_sensor_a()`

Erkläre für jeden Fall, warum die Ausgabe so ist, wie sie ist.

**Teil 2: Sichere Druck-Berechnung**

In einer hydraulischen Anlage wird der Druck aus Kraft und Fläche berechnet:
$$
p = \frac{F}{A}
$$

Implementiere die Funktion:
- `berechne_druck(kraft_N, flaeche_m2)`: Gibt Druck in bar zurück ($1 \text{ bar} = 10^5 \text{ Pa} = 10^5 \text{ N/m}^2$)
- **Problem**: Wenn Fläche = 0 → Division durch Null → Programmabsturz!

**Lösung**: Nutze Kurzschlussauswertung, um die Division zu vermeiden, wenn `flaeche_m2 == 0` oder `flaeche_m2 < 0` (ungültige Eingabe):

```python
def berechne_druck(kraft_N, flaeche_m2):
    # Kurzschlussauswertung: Prüfe ERST Fläche, DANN Berechnung
    if flaeche_m2 > 0 and (ergebnis := kraft_N / flaeche_m2 / 100000) >= 0:
        return ergebnis
    else:
        print("⚠️ Fehler: Ungültige Fläche (muss > 0 sein)")
        return None
```

**Teil 3: Grenzwertüberwachung mit Kurzschluss**

Implementiere `pruefe_betriebsparameter(druck_bar, temperatur_C)`:
- Prüfe **ERST** ob Druck im zulässigen Bereich (100-300 bar)
- Prüfe **DANN** ob Temperatur im zulässigen Bereich (20-80°C)
- Nutze Kurzschlussauswertung, um unnötige Prüfungen zu vermeiden

**Beispiel Ausgabe**:
```
=== TEIL 1: Kurzschlussauswertung demonstrieren ===

Test 1: pruefe_sensor_a() and pruefe_sensor_b()
🟢 Sensor A: Drucksensor wird abgefragt...
🔴 Sensor B: Temperatursensor wird abgefragt...
➡️ Ergebnis: False (beide Sensoren geprüft)

Test 2: pruefe_sensor_b() and pruefe_sensor_a()
🔴 Sensor B: Temperatursensor wird abgefragt...
➡️ Ergebnis: False (Sensor A wurde NICHT geprüft, weil B bereits False ist!)

Test 3: pruefe_sensor_a() or pruefe_sensor_b()
🟢 Sensor A: Drucksensor wird abgefragt...
➡️ Ergebnis: True (Sensor B wurde NICHT geprüft, weil A bereits True ist!)

Test 4: pruefe_sensor_b() or pruefe_sensor_a()
🔴 Sensor B: Temperatursensor wird abgefragt...
🟢 Sensor A: Drucksensor wird abgefragt...
➡️ Ergebnis: True (beide geprüft)

=== TEIL 2: Sichere Druck-Berechnung ===

Berechne Druck: F=50000 N, A=0.01 m²
➡️ Druck: 50.0 bar

Berechne Druck: F=50000 N, A=0 m²
⚠️ Fehler: Ungültige Fläche (muss > 0 sein)
➡️ Druck: None (Division vermieden durch Kurzschluss)

=== TEIL 3: Grenzwertüberwachung ===

Prüfe Parameter: Druck=150 bar, Temperatur=55°C
✅ Druck im Sollbereich (100-300 bar)
✅ Temperatur im Sollbereich (20-80°C)
➡️ Betriebsparameter OK

Prüfe Parameter: Druck=350 bar, Temperatur=55°C
❌ Druck außerhalb Sollbereich (350 bar > 300 bar)
➡️ Temperaturprüfung übersprungen (Kurzschlussauswertung)
➡️ Betriebsparameter NICHT OK
```

**Starter-Code**:
```python
def pruefe_sensor_a():
    print("🟢 Sensor A: Drucksensor wird abgefragt...")
    return True

def pruefe_sensor_b():
    print("🔴 Sensor B: Temperatursensor wird abgefragt...")
    return False

# Teste die vier Fälle
print("=== TEIL 1: Kurzschlussauswertung demonstrieren ===\n")
print("Test 1: pruefe_sensor_a() and pruefe_sensor_b()")
# Dein Code hier

# ... weitere Tests und Teile 2+3
```

**Hinweise**:
- **Walrus-Operator** `:=` (ab Python 3.8) erlaubt Zuweisung innerhalb von Ausdrücken
- Alternative ohne Walrus: separate if-Bedingungen
- **Kurzschlussauswertung** ist **essenziell** bei zeitkritischen SPS-Programmen: keine unnötigen Sensorabfragen
- In der Praxis: Kombination mit Exception-Handling (`try-except`, wird in V09 behandelt)

---

### Aufgabe P4: Maschinenbedien-Berechtigungssystem (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: Vergleichs-/logische Operatoren, verkettete Vergleiche, String-Methoden

Schreibe ein Programm, das ein komplexes Berechtigungssystem für die Bedienung verschiedener Industriemaschinen simuliert.

> [!NOTE]
> **Maschinenberechtigung** ist gemäß **BetrSichV** (Betriebssicherheitsverordnung) und **DGUV Vorschrift 1** gesetzlich vorgeschrieben. Nur unterwiesene und qualifizierte Personen dürfen bestimmte Maschinen bedienen. Das System simuliert eine digitale Berechtigungsverwaltung wie sie in modernen Produktionshallen (Industrie 4.0, RFID-Zugang) zum Einsatz kommt.

**Aufgabenstellung**:

Erstelle ein Programm, das die Bedien-Berechtigung für verschiedene Maschinen prüft. Das System hat folgende Regeln:

**Eingaben**:
- **Qualifikation**: "Meister", "Fachkraft", "Angelernt" oder "Auszubildender"
- **Uhrzeit** (nur Stunde als Ganzzahl, 0-23)
- **Schicht**: "Frühschicht" (6-14 Uhr), "Spätschicht" (14-22 Uhr), "Nachtschicht" (22-6 Uhr)
- **Zusatzschulung absolviert**: "Ja" oder "Nein" (z.B. CNC-5-Achsen-Schulung, Kranschein)

**Maschinen und Berechtigungsregeln**:

1. **Handwerkzeuge / Montagearbeitsplatz**: Alle Qualifikationen haben Zugang (immer erlaubt)

2. **Konventionelle Drehmaschine**:
   - Meister: immer
   - Fachkraft: Früh- und Spätschicht (6-22 Uhr)
   - Angelernt: nur Frühschicht (6-14 Uhr), nur mit Zusatzschulung
   - Auszubildender: nur unter Aufsicht (nicht in Nachtschicht, nur mit Zusatzschulung)

3. **CNC-Bearbeitungszentrum (5-Achsen)**:
   - Nur Meister oder Fachkraft mit Zusatzschulung
   - Nicht in Nachtschicht (22-6 Uhr) - zu komplexe Maschine für Nachtbetrieb ohne erweiterte Überwachung

4. **Brückenkran (Tragkraft >10t)**:
   - Meister: immer
   - Fachkraft: nur mit Zusatzschulung (Kranschein)
   - Angelernt/Auszubildender: nie (gesetzliche Vorgabe DGUV 52)

5. **Schweißroboter (Automatisiert)**:
   - Meister: immer
   - Fachkraft: Früh- und Spätschicht mit Zusatzschulung
   - Angelernt: nie (Programmierkennt­nisse erforderlich)
   - Auszubildender: nie

Das Programm soll für jede Maschine ausgeben, ob Bedienung erlaubt ist und warum (bzw. warum nicht).

**Beispiel Ein-/Ausgabe**:
```
=== MASCHINENBEDIEN-BERECHTIGUNGSSYSTEM ===
Qualifikation: Fachkraft
Uhrzeit (Stunde 0-23): 10
Schicht: Frühschicht
Zusatzschulung absolviert (Ja/Nein): Ja

--- Bedienberechtigungen ---
✅ Handwerkzeuge/Montage: Bedienung erlaubt (allgemeiner Zugang)
✅ Konventionelle Drehmaschine: Bedienung erlaubt (Fachkraft, Frühschicht 6-22 Uhr)
✅ CNC-Bearbeitungszentrum 5-Achsen: Bedienung erlaubt (Fachkraft mit Zusatzschulung, Tagschicht)
✅ Brückenkran >10t: Bedienung erlaubt (Fachkraft mit Kranschein)
✅ Schweißroboter: Bedienung erlaubt (Fachkraft, Frühschicht, Zusatzschulung vorhanden)

➡️ Alle Maschinen freigegeben für diese Person
```

```
=== MASCHINENBEDIEN-BERECHTIGUNGSSYSTEM ===
Qualifikation: Auszubildender
Uhrzeit (Stunde 0-23): 23
Schicht: Nachtschicht
Zusatzschulung absolviert (Ja/Nein): Nein

--- Bedienberechtigungen ---
✅ Handwerkzeuge/Montage: Bedienung erlaubt (allgemeiner Zugang)
❌ Konventionelle Drehmaschine: Bedienung NICHT erlaubt (Auszubildender ohne Zusatzschulung)
❌ CNC-Bearbeitungszentrum 5-Achsen: Bedienung NICHT erlaubt (nur Meister/Fachkraft mit Schulung)
❌ Brückenkran >10t: Bedienung NICHT erlaubt (DGUV 52: Kranführer müssen >18 Jahre, ausgebildet)
❌ Schweißroboter: Bedienung NICHT erlaubt (nur Meister/Fachkraft)

➡️ Beschränkung auf Montagearbeitsplatz und Handwerkzeuge
⚠️ Nachtschicht-Arbeit für Auszubildende unter 18 Jahren verboten (JArbSchG §14)!
```

**Hinweise**:
- Definiere Hilfsvariablen für häufige Bedingungen:
  ```python
  ist_meister = qualifikation == "Meister"
  ist_tagschicht = 6 <= uhrzeit < 22
  ist_frueh_oder_spaet = schicht in ["Frühschicht", "Spätschicht"]
  ```
- Nutze verkettete Vergleiche für Zeitbereiche: `6 <= uhrzeit < 14` für Frühschicht
- Strukturiere komplexe Bedingungen mit Klammern für Lesbarkeit
- Prüfe zuerst die einfacheren Fälle (Meister), dann die komplexeren
- **Wichtig**: Unterscheide zwischen "BetrSichV-Unterweisung" (Zusatzschulung Ja/Nein) und "Aufsichtsperson anwesend" (bei Auszubildenden)

**Hintergrundinformationen**:
- **BetrSichV §12**: Unterweisung und besondere Beauftragung von Beschäftigten
- **DGUV Vorschrift 52**: Krananlagen (Kranführer müssen schriftlich beauftragt sein)
- **JArbSchG §14**: Jugendliche dürfen nicht in Nachtschicht (20-6 Uhr) arbeiten
- **ISO 12100**: Risikobeurteilung für Maschinensicherheit
- In der Praxis: RFID-Karten speichern Qualifikation, System prüft automatisch vor Maschinenfreigabe

---

### Aufgabe P5: SPS-Logik-Simulator für Industriesteuerungen (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Alle logischen Operatoren, Funktionen, komplexe Bedingungen

Erstelle einen Simulator für **SPS-Logikschaltungen** (Speicherprogrammierbare Steuerung), der verschiedene Gatter (AND, OR, NOT, XOR, NAND, NOR) simuliert und industrietypische Steuerungsaufgaben auswertet.

> [!NOTE]
> **SPS** (Programmable Logic Controller, PLC) sind die "Gehirne" moderner Industrieanlagen. Sie verwenden **digitale Logik** (Boolesche Algebra) zur Steuerung von Maschinen, Förderbändern, Robotern und Sicherheitsschaltungen. Die Programmiersprache **Ladder Diagram (LD)** nach **IEC 61131-3** basiert auf den gleichen Grundgattern wie dieses Programm.

**Aufgabenstellung**:

Schreibe ein Programm mit folgenden Funktionen:

**1. Grundgatter-Funktionen (IEC 61131-3 Basiselemente)**:
   - `gate_and(a, b)` → AND-Gatter (Reihenschaltung in Ladder Logic)
   - `gate_or(a, b)` → OR-Gatter (Parallelschaltung in Ladder Logic)
   - `gate_not(a)` → NOT-Gatter (Öffner-Kontakt)
   - `gate_xor(a, b)` → XOR-Gatter (Exklusiv-ODER, für Wechselschaltungen)
   - `gate_nand(a, b)` → NAND-Gatter (universelles Gatter)
   - `gate_nor(a, b)` → NOR-Gatter (universelles Gatter)

**2. Industrietypische Schaltungen**:
   - `sicherheitsschaltung_2kanalig(kanal_a, kanal_b)` → 2-Kanal-Sicherheitslogik (gibt Tupel zurück: (Freigabe, Fehler))
     - Freigabe nur wenn BEIDE Kanäle HIGH (redundante Sicherheit nach ISO 13849)
     - Fehler wenn genau EIN Kanal HIGH (Kanalfehler erkannt)
   
   - `foerderband_steuerung(not_aus, start, bewegungsmelder, endschalter)` → Förderbandlogik
     - Startet nur wenn: Not-Aus NICHT gedrückt UND Start gedrückt UND KEIN Hindernis (Bewegungsmelder frei)
     - Stoppt wenn: Endschalter erreicht ODER Not-Aus gedrückt
   
   - `ampelsteuerung(sensor_auto, taster_fussgaenger, timer_abgelaufen)` → Ampelkreuzung-Logik
     - Fußgänger-Grün nur wenn: Taster gedrückt UND kein Auto UND Timer abgelaufen

**3. Binär-Addierer (für Zähler in SPS)**:
   - `half_adder(a, b)` → Halbaddierer (gibt Tupel zurück: (Summe, Carry))
   - `full_adder(a, b, cin)` → Volladdierer (gibt Tupel zurück: (Summe, Cout))

**4. Wahrheitstabellen-Generator**:
   - `print_truth_table(func, num_inputs, input_names, output_names)` 
   - Generiert und druckt die Wahrheitstabelle für eine beliebige SPS-Funktion

**5. Hauptprogramm - Interaktives SPS-Testpanel**:
   - Menü mit Optionen:
     1. Einzelne Gatter testen
     2. Sicherheitsschaltung (2-Kanal) testen
     3. Förderbandsteuerung testen
     4. Ampelsteuerung testen
     5. Volladdierer testen (für SPS-Zähler)
     6. Wahrheitstabelle anzeigen
     7. Beenden

**Beispiel Ausgabe** (Auszug):
```
=== SPS-LOGIK-SIMULATOR (IEC 61131-3) ===

1. Grundgatter testen
2. Sicherheitsschaltung (2-Kanal) testen
3. Förderbandsteuerung testen
4. Ampelsteuerung testen
5. Volladdierer testen (SPS-Zähler)
6. Wahrheitstabelle anzeigen
7. Beenden

Wähle eine Option: 2

--- Sicherheitsschaltung (2-Kanal-System, ISO 13849) ---
Kanal A (0=LOW/1=HIGH): 1
Kanal B (0=LOW/1=HIGH): 1

Ergebnisse:
  Freigabe (Q):       1 ✅ (Maschine FREIGEGEBEN)
  Fehler (F):         0 ✅ (Kein Kanalfehler)

Erklärung: Beide Sicherheitskanäle HIGH → redundante Bestätigung → Betrieb sicher

--- Test mit Kanalfehler ---
Kanal A: 1, Kanal B: 0
Ergebnisse:
  Freigabe (Q):       0 ❌ (Maschine GESPERRT)
  Fehler (F):         1 ⚠️ (KANALFEHLER ERKANNT! Sensor/Verkabelung prüfen!)

Wähle eine Option: 3

--- Förderbandsteuerung ---
Not-Aus gedrückt? (0=Nein/1=Ja): 0
Start-Taster gedrückt? (0=Nein/1=Ja): 1
Bewegungsmelder (Hindernis)? (0=Frei/1=Blockiert): 0
Endschalter erreicht? (0=Nein/1=Ja): 0

Ergebnis:
  Motor-Ausgang (Q): 1 ✅
➡️ Förderband läuft

Simulation Endschalter erreicht:
  Motor-Ausgang (Q): 0 🛑
➡️ Förderband gestoppt (Endposition erreicht)

Wähle eine Option: 6

--- Wahrheitstabelle ---
Wähle Schaltung:
1. XOR
2. 2-Kanal-Sicherheit
3. Förderbandsteuerung (vereinfacht: NOT_AUS AND START)

Wähle: 2

Wahrheitstabelle - 2-Kanal-Sicherheitsschaltung:
| A | B | Freigabe | Fehler |
|---|---|----------|--------|
| 0 | 0 |    0     |   0    | (Beide OFF: Normal AUS)
| 0 | 1 |    0     |   1    | (Kanalfehler!)
| 1 | 0 |    0     |   1    | (Kanalfehler!)
| 1 | 1 |    1     |   0    | (Beide ON: FREIGABE)

Logik:
  Freigabe = A AND B
  Fehler = A XOR B  (nur EIN Kanal aktiv = Fehler)
```

**Bonus-Challenge**:
Erweitere den Simulator um einen **8-Bit-Produktionszähler**, der Werkstücke zählt (BCD-Addition mit zwei 4-Bit-Addierern). Simuliere:
```python
zaehle_werkstuecke(aktueller_zaehlerstand=[0,0,0,0,0,0,1,0], impulse=5)
# Aktuell: 00000010 (binär) = 2 (dezimal)
# Nach 5 Impulsen: 00000111 (binär) = 7 (dezimal)
```

**Hinweise**:
- **2-Kanal-Logik**:
  ```python
  freigabe = gate_and(kanal_a, kanal_b)  # Beide müssen HIGH sein
  fehler = gate_xor(kanal_a, kanal_b)    # Nur einer HIGH = Fehler
  ```
- **Förderbandlogik** (vereinfacht):
  ```python
  motor = gate_and(gate_not(not_aus), gate_and(start, gate_not(bewegungsmelder)))
  # Motor läuft wenn: NOT(Not-Aus) AND Start AND NOT(Hindernis)
  ```
- XOR in Python: `a != b` (für Booleans) oder `gate_xor = lambda a, b: (a or b) and not (a and b)`
- NAND ist `not (a and b)`, NOR ist `not (a or b)`
- Für Wahrheitstabellen: `itertools.product([0, 1], repeat=num_inputs)` generiert alle Kombinationen
- Strukturiere Code nach **IEC 61131-3**: Jede Funktion = ein Funktionsbaustein (FB)

**Hintergrundinformationen**:
- **IEC 61131-3**: Internationale Norm für SPS-Programmierung (5 Sprachen: LD, FBD, ST, IL, SFC)
- **Ladder Diagram (LD)**: Grafische Programmiersprache, die Relaisschaltpläne nachbildet
- **2-Kanal-Sicherheit**: Nach ISO 13849 müssen sicherheitskritische Signale redundant erfasst werden
- **Siemens TIA Portal**, **Beckhoff TwinCAT**, **Rockwell Studio 5000**: Professionelle SPS-Software nutzt gleiche Logikgatter
- In der Praxis: SPS-Zykluszeit typisch 1-10 ms, alle Eingänge werden gelesen → Logik ausgewertet → Ausgänge gesetzt

---

