# V02: Übungsaufgaben - Fließkommazahlen

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V02.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: IEEE 754 Single Precision Darstellung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten

Gegeben ist die Dezimalzahl **-5.75**.

Ermittle die IEEE 754 Single Precision (32 Bit) Darstellung dieser Zahl. Gib das Ergebnis in folgendem Format an:

```
Vorzeichen: [0 oder 1]
Exponent (binär): [8 Bits]
Mantisse (binär): [23 Bits]
```

**Hinweise**:
- Denke daran, dass Single Precision einen Bias von 127 verwendet
- Die Mantisse wird normalisiert dargestellt (führende 1 ist implizit)
- Beginne mit der Umwandlung der Dezimalzahl in Binärform

---

### Aufgabe T2: Rundungsfehler analysieren (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

Betrachte folgende Berechnung, die in einem fiktiven Fließkommasystem mit nur **4 Bits für die Mantisse** durchgeführt wird:

$$
a = 1.101_2 \times 2^0 = 1.625_{10}
$$
$$
b = 1.011_2 \times 2^{-2} = 0.26875_{10}
$$

Berechne $a + b$ und gib an:

1. Das exakte mathematische Ergebnis in Dezimal- und Binärform
2. Die normalisierte binäre Darstellung (vor der Rundung)
3. Das gerundete Ergebnis auf 4 Bits Mantisse (verwende "Round to nearest, ties to even")
4. Den absoluten Rundungsfehler in Dezimalform

**Hinweise**:
- Achte beim Addieren auf korrekte Ausrichtung der Exponenten
- Bei Rundung: Betrachte das erste wegfallende Bit

---

### Aufgabe T3: Spezielle Werte und Maschinenepsilon (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 20-30 Minuten

**Teil A**: Gegeben sind folgende IEEE 754 Single Precision Darstellungen (32 Bit). Identifiziere, welchen speziellen Wert oder welche Zahl sie repräsentieren:

1. `0 11111111 00000000000000000000000`
2. `1 11111111 00000000000000000000000`
3. `0 11111111 10000000000000000000000`
4. `0 00000000 00000000000000000000000`
5. `1 00000000 00000000000000000000000`

**Teil B**: Das **Maschinenepsilon** $\epsilon_{\text{machine}}$ ist die kleinste darstellbare Zahl, für die gilt: $1.0 + \epsilon_{\text{machine}} \neq 1.0$.

Berechne das Maschinenepsilon für IEEE 754 Single Precision. Berücksichtige dabei:
- Die Mantisse hat 23 Bits (plus ein implizites Bit)
- Die Normalisierung sorgt dafür, dass die kleinste Änderung im letzten Mantissen-Bit erfolgt

Gib das Ergebnis als Potenz von 2 und als Dezimalzahl an.

**Hinweise**:
- Für Teil A: Prüfe, ob Exponent und Mantisse Spezialwerte-Bedingungen erfüllen
- Für Teil B: Welche binäre Darstellung hat $1.0$? Was ist die nächstgrößere darstellbare Zahl?

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Werkzeugmaschinen-Dashboard (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 10-15 Minuten  
**Vorkenntnisse**: `print()`, f-Strings, Variablen

Schreibe ein Programm, das **Betriebsparameter einer CNC-Fräsmaschine** formatiert ausgibt. Eine Werkzeugmaschine liefert folgende Messwerte:

```python
spindel_drehzahl = 3456.789  # U/min
vorschubgeschwindigkeit = 0.0425  # m/s → in mm/s umrechnen
schnitttiefe = 2.5678  # mm
oberflaeche = 1.234e-6  # m² (Ra-Wert)
auslastung = 0.873  # 0-1 (87.3%)
```

Das Programm soll die Werte in folgender Form ausgeben:

```
╔═══════════════════════════════════════╗
║   CNC-FRÄSMASCHINE DMU 50 ecoline   ║
╠═══════════════════════════════════════╣
║ Spindeldrehzahl:      3456.79 U/min ║
║ Vorschub:               42.50 mm/s  ║
║ Schnitttiefe:            2.57 mm    ║
║ Oberflächengüte (Ra):    1.23 μm    ║
║ Maschinenauslastung:    87.3 %      ║
╚═══════════════════════════════════════╝
```

**Anforderungen**:
- Verwende f-Strings für die Formatierung
- Spindeldrehzahl auf 2 Dezimalstellen
- Vorschub in mm/s (Umrechnung: × 1000) mit 2 Dezimalstellen
- Schnitttiefe auf 2 Dezimalstellen
- Oberflächengüte in μm (Umrechnung: × 10⁶) mit 2 Dezimalstellen
- Auslastung als Prozent mit 1 Dezimalstelle
- Die Werte sollen rechtsbündig ausgerichtet sein

**Hinweise**:
- Verwende `{variable:.2f}` für Dezimalstellen
- Verwende `{variable:.1%}` für Prozentangaben
- Verwende `{variable:>10.2f}` für rechtsbündige Ausrichtung
- μm (Mikrometer) = 10⁻⁶ m
- mm/s = m/s × 1000

---

### Aufgabe P2: Präzisionsmessungen und Fertigungstoleranzen (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: `print()`, f-Strings, Variablen, arithmetische Operatoren

In der **Qualitätssicherung** werden Bauteile vermessen und mit Soll-Maßen verglichen. Aufgrund von Fließkomma-Rundungsfehlern darf man **niemals direkt mit `==` vergleichen**, sondern muss **Toleranzen** verwenden.

Schreibe ein Programm, das demonstriert, warum Toleranzprüfungen essentiell sind:

**Teil 1**: Drei Messschieber messen jeweils 10.0 mm an einem Werkstück:
```python
messung1 = 3.33 + 3.33 + 3.34  # mm (drei Teilstrecken)
messung2 = 10.0  # mm (Soll-Maß)
```

**Teil 2**: Drei Einzelmessungen einer Bohrung:
```python
bohrung_x = 12.5  # mm (X-Richtung)
bohrung_y = 12.5  # mm (Y-Richtung)
bohrung_summe = bohrung_x + bohrung_y
bohrung_soll = 25.0  # mm
```

Das Programm soll:
1. Die berechneten Werte mit **20 Dezimalstellen** ausgeben
2. Prüfen, ob sie exakt gleich (`==`) den Soll-Werten sind
3. Einen **Toleranz-Vergleich** mit IT-Grade-Toleranz `±0.1 mm` durchführen
4. Ausgeben, ob das Bauteil die Qualitätskontrolle besteht

**Beispiel-Ausgabe**:
```
=== Präzisionsmessung - Qualitätskontrolle ===

Test 1: Werkstück-Länge (3× Teilmessung)
Gemessen:  10.00000000000000000000 mm
Soll-Maß:  10.00000000000000000000 mm
Exakt gleich (==)?: True
Innerhalb IT7-Toleranz (±0.1 mm)?: ✓ BESTANDEN (Abweichung: 0.00 mm)

Test 2: Bohrungsabstand (X + Y)
Gemessen:  25.00000000000000000000 mm
Soll-Maß:  25.00000000000000000000 mm
Exakt gleich (==)?: True
Innerhalb IT7-Toleranz (±0.1 mm)?: ✓ BESTANDEN (Abweichung: 0.00 mm)
```

**Anforderungen**:
- Verwende `{zahl:.20f}` für 20 Dezimalstellen
- Toleranz-Vergleich: Prüfe ob `abs(gemessen - soll) <= toleranz`
- Gib Abweichung in mm mit 2 Dezimalstellen an
- Zeige ✓ BESTANDEN oder ✗ DURCHGEFALLEN

**Hinweise**:
- **IT7-Toleranz** (ISO 286) ist eine gängige Passungstoleranz in der Fertigung
- Für hochpräzise Teile (z.B. Getriebe): IT5 mit ±0.01 mm
- Für Standard-Teile: IT7 mit ±0.1 mm

---

### Aufgabe P3: Kühlmitteltemperatur-Tabelle für Bearbeitungsprozess (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: `print()`, f-Strings, `for`-Schleifen, arithmetische Operatoren

Bei **spanenden Fertigungsverfahren** (Drehen, Fräsen, Bohren) muss die **Kühlmitteltemperatur** überwacht werden. Zu hohe Temperaturen führen zu Werkzeugverschleiß, zu niedrige zu schlechter Oberflächengüte.

Schreibe ein Programm, das eine **Umrechnungstabelle** von Grad Celsius in Kelvin erstellt:

$$
K = C + 273.15
$$

Das Programm soll:
- Temperaturen von **10°C bis 60°C** in 5°C-Schritten umrechnen
- Die Werte in einer formatierten Tabelle ausgeben
- Die Spalten rechtsbündig ausrichten
- Werte mit 2 Dezimalstellen anzeigen
- **Warnungen** für kritische Temperaturen ausgeben:
  - < 15°C: ❄️ ZU KALT (schlechte Oberflächengüte)
  - > 50°C: 🔥 ZU HEISS (erhöhter Werkzeugverschleiß)

**Beispiel-Ausgabe**:
```
╔═══════════════════════════════════════════╗
║  Celsius │ Kelvin    │ Status           ║
╠═══════════════════════════════════════════╣
║    10.00 │  283.15   │ ❄️ ZU KALT       ║
║    15.00 │  288.15   │ ✓ OPTIMAL        ║
║    20.00 │  293.15   │ ✓ OPTIMAL        ║
║    25.00 │  298.15   │ ✓ OPTIMAL        ║
║    30.00 │  303.15   │ ✓ OPTIMAL        ║
║    35.00 │  308.15   │ ✓ OPTIMAL        ║
║    40.00 │  313.15   │ ✓ OPTIMAL        ║
║    45.00 │  318.15   │ ✓ OPTIMAL        ║
║    50.00 │  323.15   │ ✓ OPTIMAL        ║
║    55.00 │  328.15   │ 🔥 ZU HEISS      ║
║    60.00 │  333.15   │ 🔥 ZU HEISS      ║
╚═══════════════════════════════════════════╝

Optimaler Bereich: 15°C - 50°C (288.15 K - 323.15 K)
```

**Anforderungen**:
- Verwende eine `for`-Schleife mit `range(10, 61, 5)` für Schritte von 5°C
- Formatiere mit `{celsius:8.2f}` und `{kelvin:9.2f}` für Ausrichtung
- Verwende `if-elif-else` für Status-Ausgabe

**Hinweise**:
- **Kelvin**: Absolute Temperaturskala (0 K = -273.15°C = absoluter Nullpunkt)
- **Kühlmittel-Typen**: Emulsionen, Öle, Luft (je nach Verfahren)
- **Typische Betriebstemperatur**: 20-30°C bei wasserbasiertem Kühlmittel

---

### Aufgabe P4: Maschinenprotokoll mit Zeitstempel (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 30-40 Minuten  
**Vorkenntnisse**: `print()`, f-Strings, `input()`, Dateien (`open()`, `with`), Schleifen

Industriemaschinen protokollieren alle **Ereignisse** (Start, Stop, Fehler, Wartung) in Logfiles für **Nachverfolgbarkeit** und **Wartungsplanung**. Dies ist gesetzlich vorgeschrieben bei sicherheitskritischen Maschinen (Maschinenrichtlinie 2006/42/EG).

Schreibe ein Programm, das ein **Maschinenprotokoll-System** simuliert:

1. Benutzer wählt Ereignistyp: `START`, `STOP`, `WARTUNG`, `FEHLER`, `ALARM`
2. Benutzer gibt Nachricht ein (z.B. "Spindel erreicht Betriebstemperatur")
3. Simulierter **Zeitstempel** wird generiert (Format: `2026-01-15 08:23:45`)
4. Eintrag wird in Datei `maschine_dmg_001.log` gespeichert (anhängen!)
5. Eintrag wird auf Konsole ausgegeben
6. Nach Beenden: Gesamtes Logfile anzeigen

**Format eines Logeintrags**:
```
[2026-01-15 08:00:00] START: CNC-Maschine DMG MORI eingeschaltet
[2026-01-15 08:05:12] WARTUNG: Ölstand geprüft - OK
[2026-01-15 09:15:45] FEHLER: Spindelmotor überhitzt (85°C)
[2026-01-15 09:16:00] ALARM: Not-Aus betätigt
[2026-01-15 09:30:00] STOP: Maschine heruntergefahren
```

**Beispielablauf**:
```
=== Maschinenprotokoll-System DMG MORI ===

Ereignistyp (START/STOP/WARTUNG/FEHLER/ALARM): START
Nachricht: Maschine eingeschaltet, Referenzfahrt durchgeführt

✓ Eintrag gespeichert:
[2026-01-15 08:00:00] START: Maschine eingeschaltet, Referenzfahrt durchgeführt

Weiteren Eintrag hinzufügen? (j/n): j
Ereignistyp: FEHLER
Nachricht: Kühlmitteldruck zu niedrig (2.1 bar, Soll: 3.0 bar)

✓ Eintrag gespeichert:
[2026-01-15 08:15:00] FEHLER: Kühlmitteldruck zu niedrig

Weiteren Eintrag hinzufügen? (j/n): n

=== Gespeicherte Protokolleinträge ===
[2026-01-15 08:00:00] START: Maschine eingeschaltet
[2026-01-15 08:15:00] FEHLER: Kühlmitteldruck zu niedrig
```

**Anforderungen**:
- Verwende `with open("maschine_dmg_001.log", "a") as datei:` zum Anhängen
- Simuliere Zeitstempel: Start bei 08:00:00, erhöhe bei jedem Eintrag um 15 Minuten
- Format: `{stunde:02d}:{minute:02d}:{sekunde:02d}` für führende Nullen
- Farbige Ausgabe (optional): Rot für FEHLER/ALARM, Grün für START

**Hinweise**:
- **Traceability**: Rückverfolgbarkeit bei Produkthaftung
- **Predictive Maintenance**: Fehler-Muster erkennen durch Log-Analyse
- **Industrie 4.0**: Logs werden an Cloud-Systeme übertragen

---

### Aufgabe P5: Prüfprotokoll-Generator für Materialchargen (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 45-60 Minuten  
**Vorkenntnisse**: Alle bisherigen Python-Konzepte, mathematische Berechnungen, Dateien

In der **Qualitätssicherung** muss jede Materialcharge (Stahl, Aluminium, Kunststoff) geprüft und **zertifiziert** werden. Schreibe ein Programm, das ein **synthetisches Prüfprotokoll** für Zugversuche (DIN EN ISO 6892-1) generiert.

**Teil 1: Prüfdaten-Generierung**

Generiere 50 Prüfkörper (Normproben) mit folgenden Messwerten:
- **Proben-ID**: Fortlaufend P001 bis P050
- **Zugfestigkeit Rm**: Startwert 235 MPa (Stahl S235JR), Schwankung ±2% (simuliere mit Formel)
- **Streckgrenze Rp0.2**: Ca. 70% von Rm, Schwankung ±1%
- **Bruchdehnung A**: 25% Basiswert, Schwankung ±3%
- **Prüftemperatur**: 23°C (Normtemperatur) ±2°C

**Teil 2: CSV-Export**

Speichere die Daten in `pruefprotokoll_charge_2026_001.csv`:
```csv
Proben-ID,Zugfestigkeit(MPa),Streckgrenze(MPa),Bruchdehnung(%),Temperatur(C)
P001,238.45,166.92,25.34,22.8
P002,232.18,162.53,24.67,23.1
...
```

**Teil 3: Statistik und Abnahmeprüfung**

Berechne und prüfe:
- **Mittelwert, Minimum, Maximum** für alle Messgrößen
- **Prüfung nach DIN EN 10025**: Alle Proben müssen ≥ Mindestwerte erfüllen:
  - Rm ≥ 235 MPa
  - Rp0.2 ≥ 165 MPa
  - A ≥ 22%
- **Abnahmestatus**: BESTANDEN / NICHT BESTANDEN

**Beispiel Statistik-Ausgabe**:
```
╔═══════════════════════════════════════════════════╗
║  PRÜFPROTOKOLL - Materialcharge 2026-001        ║
║  Material: Stahl S235JR (DIN EN 10025)          ║
╠═══════════════════════════════════════════════════╣
║ Messgröße          │ Min    │ Ø      │ Max    ║
╠═══════════════════════════════════════════════════╣
║ Zugfestigkeit Rm   │ 230.12 │ 235.03 │ 239.87 ║
║ Streckgrenze Rp0.2 │ 161.08 │ 164.52 │ 167.91 ║
║ Bruchdehnung A     │  22.45 │  25.01 │  27.58 ║
╠═══════════════════════════════════════════════════╣
║ Abnahmeprüfung nach DIN EN 10025:           ║
║ • Zugfestigkeit:    ✓ Alle ≥ 235 MPa         ║
║ • Streckgrenze:     ✓ Alle ≥ 165 MPa         ║
║ • Bruchdehnung:     ✓ Alle ≥ 22%             ║
╠═══════════════════════════════════════════════════╣
║ STATUS: ✓ CHARGE FREIGEGEBEN                  ║
╚═══════════════════════════════════════════════════╝

✓ 50 Prüfkörper in 'pruefprotokoll_charge_2026_001.csv' gespeichert
```

**Anforderungen**:
- **Keine** externen Bibliotheken (kein `random`, kein `numpy`)
- Pseudo-Zufallszahlen durch Formel: `schwankung = ((probe_nr * 13) % 20 - 10) / 100` → Werte von -0.10 bis +0.10
- Eigene Funktionen für Min, Max, Durchschnitt (keine Built-ins)
- Alle Werte mit 2 Dezimalstellen formatieren

**Hinweise**:
- **S235JR**: Baustahl nach DIN EN 10025 (Häuser, Brücken, Maschinen)
- **3.1-Abnahmeprüfzeugnis**: Zertifikat nach DIN EN 10204
- **Zugversuch**: Normprobe wird bis zum Bruch gedehnt
