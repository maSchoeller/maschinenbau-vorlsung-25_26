# V03: Übungsaufgaben - Boolsche Algebra & Variablen Management

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V03.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Wahrheitstabellen für einfache Ausdrücke (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Erstelle vollständige Wahrheitstabellen für die folgenden logischen Ausdrücke:

a) `A ∧ B`  
b) `A ∨ B`  
c) `¬A`  
d) `A ∧ ¬B`

Jede Wahrheitstabelle soll alle möglichen Eingangskombinationen und die zugehörigen Ausgangswerte enthalten. Gib auch die Anzahl der benötigten Zeilen an.

**Hinweise**:
- Bei zwei Variablen (A, B) gibt es $2^2 = 4$ mögliche Kombinationen
- Bei einer Variable (A) gibt es $2^1 = 2$ mögliche Kombinationen
- Bearbeite zuerst Klammern und Negationen, dann die Hauptoperation

---

### Aufgabe T2: Zusammengesetzte logische Ausdrücke (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 10-15 Minuten

Gegeben sind drei Eingänge A, B und C.

a) Erstelle eine Wahrheitstabelle für den Ausdruck: `(A ∧ B) ∨ (¬C)`

b) Interpretiere das Ergebnis: Wann ist der Ausdruck wahr? Formuliere eine Regel in natürlicher Sprache.

c) Zeichne die zugehörige Schaltung mit AND-, OR- und NOT-Gattern.

**Hinweise**:
- Berechne zunächst die Zwischenergebnisse `A ∧ B` und `¬C`
- Verknüpfe dann die Zwischenergebnisse mit OR
- Für die Schaltung: Jeder Operator entspricht einem Gatter

---

### Aufgabe T3: Äquivalenz logischer Ausdrücke (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 15-25 Minuten

Ein Ingenieur möchte eine Sicherheitsschaltung für eine Fertigungsmaschine entwerfen. Die Maschine soll nur starten, wenn folgende Bedingungen erfüllt sind:

- Der **Not-Aus-Schalter** ist **nicht** gedrückt (N = 0 bedeutet "nicht gedrückt")
- **Entweder** die Schutztür ist geschlossen (T = 1) **oder** der Wartungsmodus ist aktiv (W = 1)
- Der **Startknopf** ist gedrückt (S = 1)

a) Formuliere die logische Funktion für die Maschinensteuerung `M = f(N, T, W, S)` als Boolschen Ausdruck mit AND, OR und NOT.

b) Erstelle die vollständige Wahrheitstabelle für diese Funktion (16 Zeilen, da 4 Eingänge).

c) Vereinfache die Funktion so weit wie möglich und begründe deine Schritte.

d) In welchen Situationen startet die Maschine **nicht**, obwohl der Startknopf gedrückt ist? Liste alle Fälle auf.

**Hinweise**:
- "Entweder...oder" bedeutet in der Logik meist ein inklusives OR (mindestens eine Bedingung)
- Überlege dir zunächst die Grundstruktur: Was muss UND-verknüpft sein?
- Bei 4 Variablen: $2^4 = 16$ Zeilen in der Wahrheitstabelle
- Für die Vereinfachung: Suche nach gemeinsamen Teilausdrücken

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Sensor-Datentyp-Analyse für Industrie-4.0 (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `type()`, `int()`, `float()`, `str()`, `bool()`

In **Industrie 4.0** kommunizieren Maschinen über **CAN-Bus**, **Profibus** oder **OPC UA**. Sensordaten werden als Strings übertragen und müssen in die richtigen Datentypen konvertiert werden.

Schreibe ein Programm für eine **Sensor-Datenanalyse**, das:

1. Eine Sensor-Nachricht einliest (z.B. Temperatur "85" oder Drehzahl "1500")
2. Den ursprünglichen Wert und Datentyp anzeigt
3. Konvertierungen durchführt:
   - **Integer**: Für diskrete Werte (Stückzahl, Drehzahl in U/min)
   - **Float**: Für kontinuierliche Messgrößen (Temperatur, Druck)
   - **Boolean**: Für Binär-Zustände (Motor läuft: 1=True, 0=False)
4. Alle konvertierten Werte mit Typ-Information ausgibt

**Beispiel Ein-/Ausgabe**:
```
=== Sensor-Datenanalyse CAN-Bus ===
Empfangene Nachricht (Sensor ID 0x42): 85

Ursprünglicher Wert: '85', Typ: <class 'str'>
Als Integer: 85, Typ: <class 'int'>        → Drehzahl: 85 U/min
Als Float: 85.0, Typ: <class 'float'>      → Temperatur: 85.0 °C
Als Boolean: True, Typ: <class 'bool'>     → Motor: LÄUFT (Wert ≠ 0)
```

**Hinweise**:
- CAN-Bus (Controller Area Network): Standard in Automobil- und Maschinenbau
- Sensordaten werden oft als Hex oder String übertragen
- Boolean-Konvertierung: 0 = False, alle anderen Zahlen = True

---

### Aufgabe P2: Maschinenlast-Monitor mit Warnungen (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `input()`, `float()`, `print()`, Arithmetik, f-Strings

Erstelle einen **Maschinenlast-Monitor** für eine CNC-Maschine. Die **Auslastung** (Load Factor) zeigt, wie stark eine Maschine belastet ist und hilft, Überlast und vorzeitigen Verschleiß zu vermeiden.

**Formel**: $\text{Auslastung [%]} = \frac{\text{Ist-Leistung [kW]}}{\text{Nennleistung [kW]}} \times 100$

**Warnstufen**:
- < 50%: **Unterlast** (ineffizient, Energieverschwendung)
- 50-80%: **Optimal** (bester Wirkungsgrad)
- 80-95%: **Hohe Last** (erhöhter Verschleiß)
- ≥ 95%: **Kritisch** (Überlastung, Notabschaltung empfohlen)

Das Programm soll:
1. Ist-Leistung (aktuell verbrauchte Leistung in kW) einlesen
2. Nennleistung (maximale Leistung laut Typenschild in kW) einlesen
3. Eingaben in Float konvertieren
4. Auslastung in % berechnen (auf 1 Dezimalstelle)
5. Warnstufe mit Status-Symbol ausgeben

**Beispiel Ein-/Ausgabe**:
```
=== Maschinenlast-Monitor CNC DMG MORI ===
Ist-Leistung (kW): 18.5
Nennleistung (kW): 25.0

Auslastung: 74.0%
Status: ✓ OPTIMAL (bester Wirkungsgrad)
```

**Hinweise**:
- Nennleistung steht auf dem **Typenschild** der Maschine
- Bei Überlast (>95%): Risiko von Motorschäden, Sicherungen lösen aus
- Energieeffizienz: Maschinen sollten im optimalen Bereich (50-80%) betrieben werden
- Verwende `if-elif-else` für Kategorisierung

---

### Aufgabe P3: Sensor-Validierung für SPS-Eingänge (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-30 Minuten  
**Vorkenntnisse**: `isinstance()`, `type()`, `input()`, `str.isdigit()`, Type Casting

In der **Automatisierungstechnik** müssen SPS-Eingänge (Speicherprogrammierbare Steuerung) validiert werden, bevor sie verarbeitet werden. Fehlerhafte Sensordaten können zu Maschinenschäden oder Produktionsausfällen führen.

Schreibe ein **Sensor-Validierungs-Programm** für einen **Temperatursensor**:

1. Sensor-Rohwert einlesen (sollte eine Zahl sein)
2. Prüfen, ob der Wert nur aus Ziffern besteht (`.isdigit()` oder `.lstrip('-').isdigit()` für negative Werte)
3. In Integer konvertieren und Plausibilitätsprüfung:
   - **Bereich -50 bis +150°C** (typisch für Industriesensoren Pt100/Pt1000)
4. Temperatur kategorisieren:
   - **< 0°C**: Gefrierbereich (Frostgefahr, Kühlmittelpumpen prüfen)
   - **0-50°C**: Normalbereich (Maschine im Standby oder Aufwärmphase)
   - **50-80°C**: Betriebstemperatur (Maschine arbeitet)
   - **80-120°C**: Warnung (erhöhte Temperatur, Kühlung prüfen)
   - **> 120°C**: Kritisch (Überhitzung, Notabschaltung)
5. Bei ungültigen Werten: **Sensor-Fehler** melden

**Beispiel Ein-/Ausgabe (gültig)**:
```
=== Sensor-Validierung SPS Eingang E0.0 ===
Temperatursensor Pt100 (°C): 75

Typ der Eingabe: <class 'str'>
✓ Eingabe ist gültig: Nur Ziffern
Konvertierter Wert: 75°C, Typ: <class 'int'>

Status: ⚙️ BETRIEBSTEMPERATUR (Maschine arbeitet)
```

**Beispiel Ein-/Ausgabe (ungültig)**:
```
Temperatursensor Pt100 (°C): ERR

Typ der Eingabe: <class 'str'>
✗ FEHLER: Ungültige Zeichen!
→ Sensor defekt oder Kabelbruch
```

**Hinweise**:
- **Pt100/Pt1000**: Industrie-Standard-Temperatursensoren (Platin-Widerstandsthermometer)
- **SPS**: Siemens S7, Beckhoff, Allen-Bradley, etc.
- Negative Temperaturen mit `.lstrip('-').isdigit()` prüfen

---

### Aufgabe P4: Maschinenzustand-Tracking und Referenzen (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: `id()`, Datentypen, Unveränderlichkeit, Listen (Grundlagen)

In **Industrie 4.0** werden Maschinenzustände in Datenstrukturen gespeichert. Es ist kritisch zu verstehen, ob Änderungen neue Objekte erzeugen oder bestehende modifizieren → **Memory Leaks** und **Race Conditions** vermeiden.

Schreibe ein Programm zur **Analyse von Mutable vs. Immutable Datentypen** im Kontext von Maschinensteuerung:

**Teil 1: Immutable (Maschinen-ID als String)**
1. Erstelle eine Maschinen-ID: `maschine_id = "DMG-001"`
2. Zeige Speicheradresse: `id(maschine_id)`
3. Ändere die ID schrittweise:
   - `maschine_id = maschine_id + "-UPGRADED"`
   - `maschine_id = maschine_id.upper()`
   - `maschine_id = maschine_id.replace("DMG", "MORI")`
4. Dokumentiere: **Neue Speicheradresse bei jeder Änderung?**

**Teil 2: Mutable (Sensor-Messwerte als Liste)**
1. Erstelle Sensor-Array: `temperaturen = [20, 22, 21]`
2. Zeige Speicheradresse: `id(temperaturen)`
3. Modifiziere die Liste:
   - `temperaturen.append(23)` (neuer Messwert)
   - `temperaturen.remove(21)` (Ausreißer entfernen)
   - `temperaturen[0] = 19` (Korrektur)
4. Dokumentiere: **Gleiche Speicheradresse?**

**Teil 3: Referenz-Problem (Shallow Copy)**
1. Erstelle Original: `sensor_A = [50, 55, 60]` (Drucksensor A)
2. "Kopiere" für Sensor B: `sensor_B = sensor_A` (**FALSCH!**)
3. Ändere sensor_B: `sensor_B.append(65)`
4. Zeige beide: **Warum ändert sich auch sensor_A?**
5. Lösung: Echte Kopie mit `sensor_B = sensor_A.copy()`

**Ausgabeformat**:
```
=== Teil 1: Immutable (Maschinen-ID String) ===
Ursprünglich: 'DMG-001', id = 140234567890123
Nach Concat: 'DMG-001-UPGRADED', id = 140234567890456 → NEUES OBJEKT!
...

=== Teil 2: Mutable (Temperatursensor-Array) ===
Ursprünglich: [20, 22, 21], id = 140234567891000
Nach append: [20, 22, 21, 23], id = 140234567891000 → GLEICHES OBJEKT!
...

=== Teil 3: Referenz-Problem ===
VOR Änderung:
  sensor_A = [50, 55, 60]
  sensor_B = [50, 55, 60]

NACH sensor_B.append(65):
  sensor_A = [50, 55, 60, 65]  ← UNBEABSICHTIGT GEÄNDERT!
  sensor_B = [50, 55, 60, 65]

⚠️ Beide Variablen zeigen auf DASSELBE Speicher-Objekt!
```

**Hinweise**:
- **Immutable**: String, Int, Float, Tuple → Änderungen erzeugen neue Objekte
- **Mutable**: List, Dict, Set → Änderungen modifizieren das Objekt
- **Shallow Copy**: `sensor_B = sensor_A` kopiert nur die Referenz
- **Deep Copy**: `sensor_B = sensor_A.copy()` oder `sensor_B = sensor_A[:]`

---

### Aufgabe P5: Sicherheitsschaltungs-Validator (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Alle Konzepte aus V03, Boolsche Logik, Schleifen (Grundlagen), String-Methoden

In der **Maschinensicherheit** (ISO 13849, EN 60204) müssen **Sicherheitsschaltungen** prüfen, ob alle Bedingungen erfüllt sind, bevor eine Maschine startet. Fehlerhafte Logik kann zu Unfällen führen.

Erstelle einen **Sicherheitsschaltungs-Validator** für eine CNC-Fräsmaschine:

**Sicherheitsbedingungen (alle müssen TRUE sein)**:
1. **Not-Aus** nicht betätigt (Eingabe: 0 = nicht gedrückt, 1 = gedrückt)
2. **Schutztür** geschlossen (0 = offen, 1 = geschlossen)
3. **Lichtvorhang** frei (0 = unterbrochen, 1 = frei)
4. **Zwei-Hand-Bedienung** aktiv (beide Taster gleichzeitig: 0/1 für jeden)
5. **Hydraulikdruck** ausreichend (Eingabe in bar, min. 5.0 bar)
6. **Spindel** nicht blockiert (0 = blockiert, 1 = frei)

Das Programm soll:

1. **Alle 6 Sicherheits-Inputs einlesen** (als Strings)
2. **Automatisch klassifizieren**:
   - Ist es eine Binär-Eingabe (0 oder 1)?
   - Ist es eine Analog-Eingabe (Float-Wert wie Druck)?
3. **Jede Bedingung einzeln prüfen** und anzeigen
4. **Gesamtlogik**: Maschine darf NUR starten wenn ALLE Bedingungen erfüllt sind
5. **Sicherheitsprotokoll** ausgeben mit Zeitstempel

**Beispiel Ein-/Ausgabe 1 (alle OK)**:
```
=== Sicherheitsschaltungs-Validator CNC DMG MORI ===

Not-Aus Status (0=nicht gedrückt, 1=gedrückt): 0
Schutztür Status (0=offen, 1=geschlossen): 1
Lichtvorhang Status (0=unterbrochen, 1=frei): 1
Zwei-Hand Taster 1 (0/1): 1
Zwei-Hand Taster 2 (0/1): 1
Hydraulikdruck (bar): 6.5
Spindel Status (0=blockiert, 1=frei): 1

=== Sicherheitsprüfung ===
✓ Not-Aus: OK (nicht betätigt)
✓ Schutztür: OK (geschlossen)
✓ Lichtvorhang: OK (frei)
✓ Zwei-Hand-Bedienung: OK (beide Taster aktiv)
✓ Hydraulikdruck: OK (6.5 bar ≥ 5.0 bar)
✓ Spindel: OK (frei)

=== Gesamtergebnis ===
✓✓✓ MASCHINE FREIGEGEBEN ✓✓✓
Alle Sicherheitsbedingungen erfüllt.
```

**Beispiel Ein-/Ausgabe 2 (Fehler)**:
```
=== Sicherheitsschaltungs-Validator CNC DMG MORI ===

Not-Aus Status (0=nicht gedrückt, 1=gedrückt): 0
Schutztür Status (0=offen, 1=geschlossen): 0
Lichtvorhang Status (0=unterbrochen, 1=frei): 1
Zwei-Hand Taster 1 (0/1): 1
Zwei-Hand Taster 2 (0/1): 0
Hydraulikdruck (bar): 4.2
Spindel Status (0=blockiert, 1=frei): 1

=== Sicherheitsprüfung ===
✓ Not-Aus: OK (nicht betätigt)
✗ Schutztür: FEHLER (offen)
✓ Lichtvorhang: OK (frei)
✗ Zwei-Hand-Bedienung: FEHLER (nur ein Taster aktiv)
✗ Hydraulikdruck: FEHLER (4.2 bar < 5.0 bar)
✓ Spindel: OK (frei)

=== Gesamtergebnis ===
⚠️⚠️⚠️ MASCHINE GESPERRT ⚠️⚠️⚠️
3 Sicherheitsbedingungen NICHT erfüllt:
  - Schutztür offen
  - Zwei-Hand-Bedienung unvollständig
  - Hydraulikdruck zu niedrig
```

**Hinweise für die Implementierung**:
- **Binär-Prüfung**: `wert in ["0", "1"]`
- **Analog-Prüfung**: Prüfe, ob Float-Konvertierung möglich ist
- **Zwei-Hand-Logik**: Beide müssen "1" sein (AND-Verknüpfung)
- **Not-Aus-Logik**: Muss "0" sein (invertiert!)
- **Gesamtlogik**: `alle_ok = bedingung1 and bedingung2 and ... and bedingung6`
- Speichere Fehler in einer Liste für die Zusammenfassung

**Bonus-Challenge** (optional):
Erweitere das Programm um:
- **Zeitstempel** für jede Prüfung
- **Logfile** (wie in V02 P4) für alle Prüfungen
- **Wiederholungsschleife** für mehrere Prüfungen
