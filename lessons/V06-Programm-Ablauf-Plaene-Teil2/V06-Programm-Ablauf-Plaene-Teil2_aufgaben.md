# V06: Übungsaufgaben - Programm-Ablauf-Pläne Teil 2 & Schleifen

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V06.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Pseudocode zu PAP (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten

Gegeben ist folgender Pseudocode für einen Algorithmus, der prüft, ob eine Zahl eine Primzahl ist:

```
BEGIN IstPrimzahl
    EINGABE(n)
    IF n < 2 THEN
        AUSGABE("Keine Primzahl")
    ELSE
        ist_prim ← WAHR
        i ← 2
        WHILE i * i ≤ n DO
            IF n MOD i = 0 THEN
                ist_prim ← FALSCH
            ENDIF
            i ← i + 1
        ENDWHILE
        IF ist_prim THEN
            AUSGABE("Primzahl")
        ELSE
            AUSGABE("Keine Primzahl")
        ENDIF
    ENDIF
END IstPrimzahl
```

**Aufgabe**:
1. Erstelle einen vollständigen PAP (Programmablaufplan) für diesen Algorithmus
2. Verwende die korrekten Symbole nach DIN 66001/ISO 5807
3. Beschrifte alle Pfeile und Bedingungen klar

**Hinweise**:
- Du kannst Mermaid-Syntax verwenden oder den PAP auf Papier zeichnen
- Achte auf die korrekte Darstellung der Schleife (Rückwärtspfeil)
- Jede Bedingung (Raute) muss zwei ausgehende Pfeile haben (Ja/Nein)

---

### Aufgabe T2: Analyse verschachtelter Schleifen (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Betrachte folgenden PAP für einen Algorithmus mit verschachtelten Schleifen:

```mermaid
flowchart TD
    Start([START]) --> InitN[n ← 5]
    InitN --> InitI[i ← 1]
    InitI --> CheckI{i ≤ n?}
    CheckI -->|Nein| Ende([ENDE])
    CheckI -->|Ja| InitJ[j ← 1]
    InitJ --> CheckJ{j ≤ i?}
    CheckJ -->|Nein| IncrI[i ← i + 1]
    IncrI --> CheckI
    CheckJ -->|Ja| Output[/AUSGABE: '*'/]
    Output --> IncrJ[j ← j + 1]
    IncrJ --> CheckJ
```

**Aufgaben**:
1. Schreibe den zugehörigen Pseudocode zu diesem PAP
2. Führe den Algorithmus manuell für n = 3 aus und notiere alle Ausgaben
3. Was gibt der Algorithmus für beliebiges n aus? (Beschreibe das Muster)
4. Berechne die Gesamtzahl der Sternchen-Ausgaben für n = 5
5. Gib die Zeitkomplexität des Algorithmus in Big-O-Notation an

**Hinweise**:
- Achte auf die Verschachtelung der Schleifen
- Die innere Schleife läuft bis `j ≤ i`, nicht bis `j ≤ n`
- Zeichne eine Tabelle mit den Werten von i und j für jeden Durchlauf

---

### Aufgabe T3: Entwurf eines komplexen Algorithmus (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 25-30 Minuten

Entwerfe einen Algorithmus für das **Euklidische Algorithmus** zur Berechnung des größten gemeinsamen Teilers (ggT) zweier Zahlen. Der Algorithmus funktioniert wie folgt:

**Beschreibung**:
- Gegeben: Zwei positive Ganzzahlen a und b (a ≥ b)
- Solange b ≠ 0:
  - Berechne den Rest r von a geteilt durch b
  - Setze a ← b
  - Setze b ← r
- Wenn b = 0, ist a der ggT

**Aufgaben**:
1. Erstelle einen vollständigen PAP für den Euklidischen Algorithmus
2. Schreibe den zugehörigen Pseudocode
3. Führe den Algorithmus manuell für a = 48 und b = 18 aus (Trace-Tabelle)
4. Identifiziere potenzielle Probleme: Was passiert, wenn a < b? Was wenn b = 0 zu Beginn?
5. Erweitere den Algorithmus um Eingabevalidierung (beide Zahlen müssen positiv sein, falls a < b → tauschen)

**Hinweise**:
- Der Modulo-Operator (MOD) berechnet den Rest
- Verwende eine Trace-Tabelle mit Spalten: Durchlauf, a, b, r
- Die Schleife ist kopfgesteuert (while-Typ)
- Achte auf die Initialisierung und alle Randfälle

---

## Teil B: Python-Aufgaben

### Aufgabe P1: CNC-Drehzahl-Sequenz ausgeben (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `for`-Schleifen, `range()`  
**Maschinenbau-Kontext**: Analyse von CNC-Spindeldrehzahl-Stufen und Bearbeitungsparametern

Schreibe ein Python-Programm zur Ausgabe von **CNC-Spindeldrehzahl-Sequenzen** für verschiedene Bearbeitungsszenarien.

> [!NOTE]
> **CNC-Drehzahl**: Die Umdrehungen pro Minute (U/min oder RPM) der Werkzeugspindel. Die Drehzahl ist entscheidend für Schnittgeschwindigkeit, Oberflächenqualität und Werkzeugverschleiß. Typische Bereiche:
> - Drehen (Stahl): 200-2000 U/min
> - Fräsen (Aluminium): 3000-10000 U/min
> - Bohren (Kunststoff): 1000-5000 U/min

**Teilaufgaben**:
1. **Drehen-Sequenz**: Alle Drehzahlen von 200 bis 2000 U/min in Schritten von 200 U/min
2. **Fräsen-Sequenz**: Alle Drehzahlen von 3000 bis 10000 U/min in Schritten von 1000 U/min
3. **Bohren-Sequenz**: Alle Drehzahlen von 1000 bis 5000 U/min in Schritten von 500 U/min
4. **Hochlauf-Test**: Drehzahl-Rampe von 0 bis 1000 U/min in Schritten von 100 U/min
5. **Notfall-Abbremsen**: Countdown von 3000 U/min auf 0 in Schritten von 500 U/min

**Beispiel-Ausgabe für Teilaufgabe 1**:
```
Drehen-Sequenz (U/min): 200 400 600 800 1000 1200 1400 1600 1800 2000
```

**Beispiel-Ausgabe für Teilaufgabe 5**:
```
Notfall-Abbremsen (U/min): 3000 2500 2000 1500 1000 500 0
```

**Hinweise**:
- Verwende `range()` mit verschiedenen Parametern (Start, Stopp, Schrittweite)
- Für Countdown: `range(3000, -1, -500)` (negative Schrittweite!)
- Verwende `end=' '` in `print()`, um Zahlen in einer Zeile auszugeben
- Achte darauf, dass die Endwerte inkludiert werden (z.B. für 200-2000: `range(200, 2001, 200)`)

---

### Aufgabe P2: Zahnrad-Übersetzung berechnen (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `for`-Schleifen, `range()`, Akkumulation  
**Maschinenbau-Kontext**: Berechnung von Drehzahl-Übersetzungen in mehrstufigen Getrieben

Erstelle ein Programm zur Berechnung der **Gesamt-Übersetzung** in einem mehrstufigen Zahnradgetriebe.

> [!NOTE]
> **Getriebe-Übersetzung**: Das Verhältnis zwischen Eingangs- und Ausgangsdrehzahl. Bei mehrstufigen Getrieben multiplizieren sich die einzelnen Übersetzungen:
> $$i_{gesamt} = i_1 \times i_2 \times i_3 \times ... \times i_n$$
> - Übersetzung $ i < 1 $: Drehzahlerhöhung (z.B. 0.5 → Verdopplung)
> - Übersetzung $ i > 1 $: Drehzahlreduzierung (z.B. 2.0 → Halbierung)
> - Übersetzung $ i = 1 $: Keine Änderung

**Aufgabe**:
Schreibe ein Python-Programm für ein **3-stufiges Getriebe**, das:
1. Nach der **Anzahl der Stufen** (n) fragt
2. Für jede Stufe die **Übersetzung** $ i $ abfragt (z.B. 2.5, 1.8, 3.0)
3. Die **Gesamt-Übersetzung** berechnet (Produkt aller Einzelübersetzungen)
4. Die **Ausgangsdrehzahl** berechnet, wenn die Eingangsdrehzahl 1500 U/min beträgt

**Beispiel Ein-/Ausgabe**:
```
Anzahl der Getriebestufen: 3
Übersetzung Stufe 1: 2.5
Übersetzung Stufe 2: 1.8
Übersetzung Stufe 3: 3.0
───────────────────────────────
Gesamt-Übersetzung: 13.50
Eingangsdrehzahl: 1500 U/min
Ausgangsdrehzahl: 111.11 U/min
```

**Berechnung**:
- Gesamt-Übersetzung: $i_{gesamt} = 2.5 \times 1.8 \times 3.0 = 13.5$
- Ausgangsdrehzahl: $n_{aus} = \frac{n_{ein}}{i_{gesamt}} = \frac{1500}{13.5} = 111.11$ U/min

**Zusatzaufgabe** (optional):
Berechne auch das **Drehmoment** an der Ausgangswelle, wenn das Eingangsdrehmoment 50 Nm beträgt. 
Formel: $M_{aus} = M_{ein} \times i_{gesamt} \times \eta $ (mit Wirkungsgrad $ \eta = 0.95$ für jede Stufe).

**Hinweise**:
- Initialisiere eine Variable `i_gesamt = 1.0` (nicht 0!)
- Verwende eine `for`-Schleife mit `range(1, n+1)` für die Stufenabfrage
- Multipliziere in jedem Durchlauf: `i_gesamt *= i_stufe`
- Ausgangsdrehzahl: `n_aus = n_ein / i_gesamt`
- Formatiere Ergebnisse auf 2 Dezimalstellen: `f"{wert:.2f}"`

---

### Aufgabe P3: G-Code Programm analysieren (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: `for`-Schleifen, String-Iteration, Zählen  
**Maschinenbau-Kontext**: Analyse von CNC-G-Code Programmen zur Fehlerdiagnose und Statistik

Schreibe ein Python-Programm zur Analyse eines **G-Code-Programms** für CNC-Maschinen.

> [!NOTE]
> **G-Code**: Die standardisierte Programmiersprache für CNC-Maschinen (DIN 66025 / ISO 6983). Wichtige Befehle:
> - **G-Befehle** (G00, G01, G02, G03...): Steuern die Bewegung (Eilgang, Linear, Kreisbogen)
> - **M-Befehle** (M03, M05, M06...): Maschinenfunktionen (Spindel ein/aus, Werkzeugwechsel)
> - **Koordinaten** (X, Y, Z): Position in mm
> - **F-Wert**: Vorschub in mm/min
> - **S-Wert**: Spindeldrehzahl in U/min

**Aufgabe**:
Analysiere einen G-Code-String (vom Benutzer eingegeben oder vorgegeben) und zähle:

1. **Anzahl der Zeilen** (Gesamtlänge nach Zeilenumbruch-Split)
2. **Anzahl der G-Befehle** (Zeichen "G" gefolgt von Ziffern)
3. **Anzahl der M-Befehle** (Zeichen "M" gefolgt von Ziffern)
4. **Anzahl der X-Koordinaten** (Zeichen "X")
5. **Anzahl der Y-Koordinaten** (Zeichen "Y")
6. **Anzahl der Z-Koordinaten** (Zeichen "Z")
7. **Anzahl der Kommentare** (Zeilen mit ";")

**Beispiel G-Code**:
```gcode
; CNC-Programm für Rechteck-Tasche
G21 G90 G94
G00 X0 Y0 Z5
M03 S2000
G01 Z-5 F100
G01 X50 Y0 F500
G01 X50 Y30
G01 X0 Y30
G01 X0 Y0
G00 Z5
M05
M30
```

**Beispiel Ein-/Ausgabe**:
```
Bitte G-Code eingeben (mehrere Zeilen, mit ENTER beenden, leere Zeile zum Abschluss):
> G21 G90 G94
> G00 X0 Y0 Z5
> ...
> M30
>
═══════════════════════════════════
G-Code Analyse-Ergebnis:
═══════════════════════════════════
- Zeilen gesamt: 10
- G-Befehle: 8
- M-Befehle: 3
- X-Koordinaten: 6
- Y-Koordinaten: 6
- Z-Koordinaten: 3
- Kommentare: 1
═══════════════════════════════════
```

**Hinweise**:
- Lies den G-Code zeilenweise ein (mit `input()` in Schleife oder als Multiline-String)
- Verwende `.split('\n')` um Zeilen zu trennen
- Zähle mit `zeile.count('G')`, `zeile.count('M')`, etc.
- Für Kommentare: `if ';' in zeile:`
- Verwende separate Zähler-Variablen für jede Kategorie
- **Hinweis**: Eine genauere Analyse würde Reguläre Ausdrücke verwenden (später im Kurs)

---

### Aufgabe P4: Material-Zugversuch mit Eingabevalidierung (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 25-35 Minuten  
**Vorkenntnisse**: `while`-Schleifen, `input()`, Validierung, Verzweigungen  
**Maschinenbau-Kontext**: Simulation eines materialwissenschaftlichen Zugversuchs mit Eingabevalidierung

Schreibe ein Programm zur Simulation eines **Zugversuchs** nach DIN EN ISO 6892-1.

> [!NOTE]
> **Zugversuch**: Standardprüfverfahren zur Ermittlung mechanischer Kennwerte von Werkstoffen:
> - **Zugfestigkeit** $ R_m $ [MPa]: Maximale Spannung vor Bruch
> - **Streckgrenze** $ R_e $ [MPa]: Spannung bei plastischer Verformung
> - **Bruchdehnung** $ A $ [%]: Verlängerung bei Bruch
> - Typische Werte für Baustahl S235: $ R_e $ = 235 MPa, $ R_m $ = 360-510 MPa

**Aufgabe**:
Erstelle ein Programm, das:
1. Zufällig einen **Werkstoff** aus einer Liste wählt: Baustahl S235, Aluminium 6061, Edelstahl 1.4301, Kunststoff POM
2. Den Benutzer die **Zugfestigkeit** $ R_m $ in MPa erraten lässt
3. Nach jedem Versuch einen Hinweis gibt: "Zu niedrig", "Zu hoch" oder "Richtig!"
4. Maximal **5 Versuche** erlaubt
5. Ungültige Eingaben (keine Zahl, negative Werte) **nicht** als Versuch zählt
6. Am Ende die tatsächliche Zugfestigkeit und die Anzahl der Versuche anzeigt

**Werkstoff-Datenbank** (verwende diese Werte):
```python
werkstoffe = {
    "Baustahl S235": 360,
    "Aluminium 6061": 310,
    "Edelstahl 1.4301": 520,
    "Kunststoff POM": 65
}
```

**Beispiel-Ablauf**:
```
═══════════════════════════════════
  Zugversuch-Simulator
═══════════════════════════════════
Zu testender Werkstoff: Aluminium 6061
Schätze die Zugfestigkeit Rm (MPa)!
Du hast 5 Versuche.

Versuch 1/5 - Deine Schätzung (MPa): 200
❌ Zu niedrig!

Versuch 2/5 - Deine Schätzung (MPa): 400
❌ Zu hoch!

Versuch 3/5 - Deine Schätzung (MPa): abc
⚠️  Ungültige Eingabe! Bitte eine positive Zahl eingeben.

Versuch 3/5 - Deine Schätzung (MPa): 310
✅ Richtig! Du hast die Zugfestigkeit in 3 Versuchen erraten.

Ergebnis:
- Werkstoff: Aluminium 6061
- Zugfestigkeit Rm: 310 MPa
- Benötigte Versuche: 3
```

**Beispiel bei Misserfolg**:
```
Versuch 5/5 - Deine Schätzung (MPa): 280
❌ Zu niedrig!

Leider verloren! Du hast die Zugfestigkeit nicht erraten.
Die korrekte Zugfestigkeit von Aluminium 6061 ist 310 MPa.
```

**Anforderungen**:
- Verwende `import random` und `random.choice(list(werkstoffe.keys()))` für die Werkstoffwahl
- Nutze eine `while`-Schleife für die Wiederholung
- Validiere die Eingabe (nur positive Zahlen akzeptieren)
- Zähle nur gültige Versuche
- Brich ab nach 5 Versuchen oder wenn die Zahl erraten wurde

**Hinweise**:
- Struktur: `while versuch <= 5 and not erraten:`
- Verwende `try-except` für Eingabevalidierung: `float(input())`
- Nach korrekter Eingabe: `versuch += 1`
- Bei ungültiger Eingabe: **kein** Versuchs-Inkrement
- Toleranz einbauen (optional): ±5 MPa als "nah genug" akzeptieren

---

### Aufgabe P5: Fertigungslinie-Simulation mit verschachtelten Schleifen (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 40-50 Minuten  
**Vorkenntnisse**: Verschachtelte Schleifen, String-Konkatenation, Logik  
**Maschinenbau-Kontext**: Visualisierung von Fertigungslinien-Layouts und Produktionsmatrizen

Schreibe ein Python-Programm zur **Visualisierung verschiedener Fertigungslinen-Layouts** für eine Produktionshalle.

> [!NOTE]
> **Fertigungslinie**: Anordnung von Maschinen und Arbeitsplätzen in der Produktion. Verschiedene Layouts:
> - **Linien-Layout**: Maschinen in einer Reihe (für Fließfertigung)
> - **U-förmiges Layout**: Materialfluss in U-Form (platzsparend)
> - **Insel-Layout**: Maschinen gruppiert nach Funktion
> - **Matrix-Layout**: Flexible Anordnung für variierende Produkte

**Aufgabe**:
Erstelle ein Programm, das verschiedene **Produktionshallen-Layouts** mit ASCII-Zeichen visualisiert.

**Teilaufgabe 1: Linien-Layout (Fließfertigung)**
Zeige n Maschinen in einer Reihe mit Förderbändern dazwischen:
```
[M1] → [M2] → [M3] → [M4] → [M5]
```

**Teilaufgabe 2: U-förmiges Layout**
Zeige n Maschinen in U-Form (obere Reihe → untere Reihe rückwärts):
```
[M1] → [M2] → [M3]
                ↓
[M6] ← [M5] ← [M4]
```

**Teilaufgabe 3: Matrix-Layout (Raster)**
Zeige n×m Maschinen in Rasterform:
```
[M01] [M02] [M03] [M04]
[M05] [M06] [M07] [M08]
[M09] [M10] [M11] [M12]
```

**Teilaufgabe 4: Auslastungs-Heatmap**
Zeige eine Matrix mit Auslastungssymbolen (█ = 100%, ▓ = 75%, ▒ = 50%, ░ = 25%, · = 0%):
```
Maschinen-Auslastung (Schicht 1):
█ ▓ ▒ ░ ·
█ █ ▓ ▓ ▒
▓ ▒ ░ · ·
```

**Anforderungen**:
1. Der Benutzer gibt die **Anzahl der Maschinen** n ein (z.B. n = 6)
2. Das Programm zeigt ein **Menü** mit den vier Layouts
3. Der Benutzer wählt ein Layout aus
4. Das Programm zeichnet das gewählte Layout mit der angegebenen Anzahl

**Beispiel Ein-/Ausgabe**:
```
═══════════════════════════════════
  Fertigungslinen-Visualisierung
═══════════════════════════════════
Anzahl der Maschinen: 6

Wähle ein Layout:
1. Linien-Layout (Fließfertigung)
2. U-förmiges Layout
3. Matrix-Layout (Raster)
4. Auslastungs-Heatmap
Deine Wahl: 2

U-förmiges Layout (6 Maschinen):
[M1] → [M2] → [M3]
                ↓
[M6] ← [M5] ← [M4]
```

**Hinweise für Teilaufgabe 2 (U-Form)**:
- Verwende verschachtelte `for`-Schleifen
- Obere Reihe: Maschinen 1 bis n//2
- Leerzeilen für seitliche Verbindung
- Untere Reihe: Maschinen n bis (n//2 + 1) in umgekehrter Reihenfolge
- Berechne Leerzeichen für die Ausrichtung

**Hinweise für Teilaufgabe 3 (Matrix)**:
- Frage nach Zeilen und Spalten
- Verwende zweistellige Nummerierung: `f"M{i:02d}"`
- Verschachtelte Schleifen: äußere für Zeilen, innere für Spalten

**Hinweise für Teilaufgabe 4 (Heatmap)**:
- Verwende `import random` für Zufalls-Auslastungen
- Auslastung in Prozent: `random.randint(0, 100)`
- Mapping: 0-20% → `·`, 21-40% → `░`, 41-60% → `▒`, 61-80% → `▓`, 81-100% → `█`

**Bonus-Challenge** (optional):
- Erweitere das Matrix-Layout um **Gänge** (leere Spalten alle 3 Maschinen)
- Füge ein fünftes Layout hinzu: **Roboter-Zelle** (kreisförmig um zentralen Roboter)
- Speichere das Layout in einer Textdatei `layout.txt`


