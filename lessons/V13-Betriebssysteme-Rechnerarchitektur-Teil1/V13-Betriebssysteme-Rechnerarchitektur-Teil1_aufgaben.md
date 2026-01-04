# V13: Übungsaufgaben - Betriebssysteme & Rechnerarchitektur – Teil 1

> [!NOTE]
> Diese Übungsaufgaben vertiefen das Verständnis der Vorlesung V13.
> Bearbeite die Aufgaben in der angegebenen Reihenfolge.

---

## Teil A: Theorie-Aufgaben

### Aufgabe T1: Von-Neumann-Architektur (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 5-10 Minuten

Die Von-Neumann-Architektur ist das fundamentale Konzept moderner Computer. Beantworte folgende Fragen:

**Teilaufgabe a)**: Benenne die vier Hauptkomponenten der Von-Neumann-Architektur und beschreibe in jeweils einem Satz deren Aufgabe.

**Teilaufgabe b)**: Was ist der **Von-Neumann-Flaschenhals** und warum ist er ein Performance-Problem? Erkläre in 2-3 Sätzen.

**Teilaufgabe c)**: Der System-Bus besteht aus drei Teilbussen. Benenne diese und erkläre, welche Informationen jeweils übertragen werden.

**Hinweise**:
- Denke an die Diagramme aus der Vorlesung
- Der Von-Neumann-Flaschenhals entsteht durch eine Eigenschaft der Architektur, die Befehle und Daten betrifft

---

### Aufgabe T2: CPU-Aufbau und Fetch-Decode-Execute-Zyklus (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 15-20 Minuten

**Teilaufgabe a)**: Die CPU besteht aus drei Hauptkomponenten: ALU, Steuerwerk und Register. Erkläre für jede Komponente:
- Was ist ihre primäre Aufgabe?
- Welche konkreten Operationen führt sie aus?
- Wie interagiert sie mit den anderen Komponenten?

**Teilaufgabe b)**: Beschreibe den **Fetch-Decode-Execute-Zyklus** im Detail. Gehe dabei auf folgende Punkte ein:
- Was passiert in jeder der drei Phasen (Fetch, Decode, Execute)?
- Welche Register sind beteiligt (Program Counter, Instruction Register)?
- Wie wird sichergestellt, dass der nächste Befehl nach der Ausführung geholt wird?

**Teilaufgabe c)**: Gegeben sei folgender Maschinenbefehl: `ADD R1, R2` (Addiere den Inhalt von Register R2 zu Register R1, Ergebnis in R1 speichern).

Angenommen, vor der Ausführung gilt:
- `R1 = 10`
- `R2 = 25`
- `Program Counter (PC) = 0x2000`
- Der Befehl steht an Adresse `0x2000`

Beschreibe Schritt für Schritt, was in jeder Phase des Fetch-Decode-Execute-Zyklus passiert. Gib auch an, welche Werte sich in welchen Registern ändern.

**Hinweise**:
- Die Fetch-Phase betrifft hauptsächlich den Program Counter und das Instruction Register
- Die Decode-Phase analysiert den Befehl und identifiziert ALU-Operation und Operanden
- Die Execute-Phase führt die eigentliche Addition durch

---

### Aufgabe T3: Cache-Hierarchie und Performance (Schwer)

**Schwierigkeit**: ⭐⭐⭐ Schwer  
**Zeitaufwand**: ca. 20-30 Minuten

**Teilaufgabe a)**: Erkläre das **Lokalitätsprinzip** (Principle of Locality) und dessen zwei Ausprägungen:
- **Temporal Locality** (zeitliche Lokalität)
- **Spatial Locality** (räumliche Lokalität)

Gib für jede Ausprägung ein konkretes Programmierbeispiel, bei dem diese Lokalität auftritt.

**Teilaufgabe b)**: Die Cache-Hierarchie besteht aus L1, L2 und L3. Fülle die folgende Tabelle aus:

| Cache | Typische Größe | Zugriffszeit (Taktzyklen) | Zugriffszeit (ns) | Pro Kern oder geteilt? |
|-------|----------------|---------------------------|-------------------|------------------------|
| L1    | ?              | ?                         | ?                 | ?                      |
| L2    | ?              | ?                         | ?                 | ?                      |
| L3    | ?              | ?                         | ?                 | ?                      |
| RAM   | ?              | ?                         | ?                 | -                      |

**Teilaufgabe c)**: Betrachte folgenden Python-Code, der eine 1000×1000 Matrix durchläuft:

**Variante 1** (Zeilenweise):
```python
for zeile in range(1000):
    for spalte in range(1000):
        matrix[zeile][spalte] += 1
```

**Variante 2** (Spaltenweise):
```python
for spalte in range(1000):
    for zeile in range(1000):
        matrix[zeile][spalte] += 1
```

**Fragen**:
1. Welche Variante ist cache-effizienter und warum?
2. Erkläre, wie die Cache Line (typisch 64 Bytes) bei jeder Variante genutzt wird.
3. Schätze grob ab, wie viele Cache Misses bei Variante 1 vs. Variante 2 auftreten (Annahme: Cache Line = 64 Bytes, ein Float = 8 Bytes, d.h. 8 Float-Werte pro Cache Line).

**Teilaufgabe d)**: Eine CPU läuft mit 3 GHz (3 Milliarden Taktzyklen pro Sekunde). Berechne:
- Wie lange dauert ein einzelner Taktzyklus in Nanosekunden?
- Wenn L1-Cache 4 Taktzyklen Zugriffszeit hat, wie lange dauert ein L1-Zugriff in Nanosekunden?
- Wenn RAM 100 ns Zugriffszeit hat, wie viele Taktzyklen entspricht das?
- Wie viel schneller ist L1-Cache gegenüber RAM (Faktor)?

**Hinweise**:
- 1 GHz = 10⁹ Hz = 10⁹ Taktzyklen pro Sekunde
- 1 Sekunde = 10⁹ Nanosekunden
- Arrays werden in Python (und den meisten Sprachen) zeilenweise im Speicher abgelegt (**Row-Major Order**)
- Cache Lines werden immer vollständig geladen, auch wenn nur ein Byte benötigt wird

---

## Teil B: Python-Aufgaben

### Aufgabe P1: CNC-Werkzeugverschleiß Visualisierung (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Matplotlib-Installation, `plt.plot()`, Achsenbeschriftungen

Erstelle ein Python-Programm, das den Werkzeugverschleiß verschiedener Fräswerkzeuge über die Betriebszeit visualisiert. In der Zerspanung nimmt der Werkzeugverschleiß mit der Standzeit zu.

Gegeben sind drei Werkzeugtypen mit ihren Verschleißmodellen (Verschleiß in mm nach t Minuten):
- **Hartmetall-Fräser**: `verschleiß = 0.002 * t + 0.05` (langsamer Verschleiß)
- **HSS-Fräser**: `verschleiß = 0.008 * t + 0.10` (mittlerer Verschleiß)
- **Schnellstahl**: `verschleiß = 0.015 * t + 0.15` (schneller Verschleiß)

**Anforderungen**:
1. Visualisiere den Verschleiß für Betriebszeiten von 0 bis 100 Minuten (in 5-Minuten-Schritten)
2. Verwende unterschiedliche Farben: Hartmetall (blau), HSS (grün), Schnellstahl (rot)
3. Füge eine Legende hinzu mit den Werkzeugbezeichnungen
4. Beschrifte die X-Achse mit "Betriebszeit (Minuten)" und die Y-Achse mit "Verschleiß (mm)"
5. Setze den Titel "Werkzeugverschleiß bei Fräsoperationen"
6. Aktiviere Gitterlinien
7. Markiere die kritische Verschleißgrenze von 1.0 mm mit einer horizontalen roten gestrichelten Linie

**Beispiel Ein-/Ausgabe**:
```
(Ein grafisches Fenster öffnet sich mit dem Plot)
```

**Starter-Code**:
```python
import matplotlib.pyplot as plt

# Erstelle Betriebszeit-Werte von 0 bis 100 Minuten in 5-Minuten-Schritten
betriebszeit = [i * 5 for i in range(21)]  # 0, 5, 10, ..., 100

# Berechne Verschleiß-Werte für die drei Werkzeugtypen
# Dein Code hier

# Erstelle den Plot
# Dein Code hier

# Markiere kritische Verschleißgrenze
# Dein Code hier
```

**Hinweise**:
- Verwende `range(21)`, da 0 bis 100 in 5er-Schritten 21 Werte ergibt
- List Comprehension ist nützlich für die Berechnung der Verschleißwerte
- `plt.axhline(y=1.0, ...)` zeichnet eine horizontale Linie

---

### Aufgabe P2: Hydrauliksystem-Überwachung (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: `plt.plot()`, Linienstile, Marker

Ein Drucksensor überwacht den Hydraulikdruck einer Pressmaschine während eines 24-Stunden-Produktionszyklus (stündliche Messung). Gegeben sind folgende Messdaten:

```python
stunden = list(range(24))  # 0 bis 23 Uhr
druck_bar = [145, 148, 152, 158, 165, 170, 178, 185, 192, 198, 
             205, 210, 215, 218, 215, 210, 205, 198, 190, 182, 
             170, 160, 152, 148]  # bar
```

**Aufgaben**:

**Teil a)**: Erstelle einen Linienplot des Hydraulikdrucks über die Zeit:
- X-Achse: "Uhrzeit (Stunde)"
- Y-Achse: "Hydraulikdruck (bar)"
- Titel: "Hydraulikdruck-Überwachung über 24 Stunden"
- Verwende eine durchgezogene Linie mit Marker-Punkten (`'o-'`)
- Farbe: Dunkelblau (`'darkblue'`)
- Gitterlinien aktiviert

**Teil b)**: Füge zwei horizontale Linien hinzu für die zulässigen Druckgrenzen:
- Minimaler Betriebsdruck: 150 bar (grüne gestrichelte Linie)
- Maximaler Betriebsdruck: 200 bar (rote gestrichelte Linie)
- Verwende `plt.axhline()` mit entsprechenden Labels
- Ergänze die Legende

**Teil c)**: Markiere alle Zeitpunkte, an denen der Druck **außerhalb** des zulässigen Bereichs liegt (< 150 bar ODER > 200 bar):
- Filtere die kritischen Stunden
- Verwende `plt.scatter()` für diese Punkte mit oranger Farbe und größerem Marker (`s=120`)
- Label: "Kritischer Druck"

**Beispiel-Ausgabe**:
Ein Plot mit blauer Druckkurve, grünen und roten Grenzlinien, und orangen Markierungen bei kritischen Druckwerten.

**Hinweise**:
- Verwende `or`-Operator zum Filtern: `druck < 150 or druck > 200`
- `plt.axhline()` zeichnet eine horizontale Linie über die gesamte X-Achse
- `zorder=5` stellt sicher, dass Scatter-Punkte über der Linie liegen

---

### Aufgabe P3: Produktionsqualität im Vergleich (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-30 Minuten  
**Vorkenntnisse**: Scatter Plots, Farben, Marker-Größen

Historische Daten zur Produktionsqualität verschiedener Fertigungslinien über 9 Quartale:

```python
quartale = [1, 2, 3, 4, 5, 6, 7, 8, 9]
linie_a_ausschuss_prozent = [8.5, 7.2, 6.1, 5.5, 4.8, 4.2, 3.5, 2.9, 2.1]
linie_b_ausschuss_prozent = [9.2, 8.5, 7.8, 7.0, 6.5, 6.0, 5.2, 4.5, 3.8]
produktionsvolumen_tsd = [10, 12, 15, 18, 22, 25, 30, 35, 42]  # in Tausend Stück
```

**Aufgaben**:

**Teil a)**: Erstelle einen Scatter Plot für beide Fertigungslinien:
- X-Achse: "Quartal"
- Y-Achse: "Ausschussquote (%)"
- Titel: "Qualitätsentwicklung: Linie A vs. Linie B"
- Linie A: Blaue Kreise
- Linie B: Rote Quadrate (`marker='s'`)
- Beide mit Label für Legende

**Teil b)**: Skaliere die **Marker-Größe** proportional zum Produktionsvolumen:
- Verwende `s=produktionsvolumen_tsd` für beide Scatter-Plots
- Füge eine Anmerkung hinzu: `plt.text(7, 8, "Größe ∝ Produktionsvolumen", fontsize=10)`

**Teil c)**: Verbinde die Datenpunkte mit Linien:
- Linie A: Gestrichelte blaue Linie (`linestyle='--'`)
- Linie B: Gepunktete rote Linie (`linestyle=':'`)
- Verwende dieselben Farben wie bei den Scatter-Punkten

**Teil d)**: Markiere die Zielausschussquote von 3% mit einer horizontalen grünen Linie:
- `plt.axhline(y=3, color='green', linestyle='-.', label='Ziel-Ausschussquote (3%)')`

**Hinweise**:
- Scatter-Plots und Linienplots können kombiniert werden
- Kleinere Marker-Größen am Anfang zeigen geringeres Produktionsvolumen

---

### Aufgabe P4: FEM-Spannungsanalyse mit Fehlerbalken (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 35-40 Minuten  
**Vorkenntnisse**: `plt.plot()`, `plt.scatter()`, `plt.errorbar()`, `plt.fill_between()`

Ein Konstrukteur führt FEM-Simulationen (Finite-Elemente-Methode) durch, um die Zugspannung in einem Bauteil bei verschiedenen Lasten zu analysieren. Jede Simulation wurde 5-mal mit leicht variierten Parametern wiederholt:

```python
lasten_kn = [5, 10, 15, 20, 25, 30, 35, 40]  # kN
spannung_mittel_mpa = [48, 95, 142, 189, 235, 282, 328, 375]  # MPa
spannung_std_mpa = [3, 5, 7, 9, 12, 15, 18, 22]  # MPa (Standardabweichung)
```

**Aufgaben**:

**Teil a)**: Erstelle einen Plot mit Fehlerbalken:
- X-Achse: "Last (kN)"
- Y-Achse: "Spannung (MPa)"
- Titel: "FEM-Spannungsanalyse mit Messunsicherheit"
- Verwende `plt.errorbar(x, y, yerr=std, fmt='o-', capsize=5, label='Simulation ± σ')`
- Farbe: Dunkelblau
- Gitterlinien aktiviert

**Teil b)**: Füge einen **Unsicherheitsbereich** (Confidence Band) hinzu:
- Verwende `plt.fill_between()` um den Bereich Mittelwert ± Standardabweichung zu schattieren
- Berechne obere Grenze: `[mittel + std for mittel, std in zip(spannung_mittel_mpa, spannung_std_mpa)]`
- Berechne untere Grenze: `[mittel - std for mittel, std in zip(spannung_mittel_mpa, spannung_std_mpa)]`
- `plt.fill_between(lasten_kn, untere_grenze, obere_grenze, alpha=0.2, color='blue', label='±1σ Bereich')`

**Teil c)**: Markiere die **Streckgrenze** des Materials (σ_y = 300 MPa):
- Zeichne eine horizontale rote gestrichelte Linie: `plt.axhline(y=300, color='red', linestyle='--', linewidth=2, label='Streckgrenze (300 MPa)')`
- Markiere den Bereich ab dem die Streckgrenze überschritten wird mit roter Schattierung: `plt.axvspan(x_min, x_max, color='red', alpha=0.1, label='Plastische Verformung')`

**Teil d)**: Füge eine Trendlinie hinzu:
- Verwende `numpy.polyfit()` für eine lineare Regression
- Berechne: `koeffizienten = np.polyfit(lasten_kn, spannung_mittel_mpa, deg=1)`
- Zeichne Trendlinie: `plt.plot(lasten_kn, trendlinie, 'k--', label='Trendlinie')`

**Beispiel-Ausgabe**:
Ein Plot mit blauen Fehlerbalken, blauem Unsicherheitsbereich, roter Streckgrenze und schwarzer Trendlinie.

**Hinweise**:
- Die Streckgrenze wird zwischen 25-30 kN überschritten
- Lineare Regression zeigt perfekten Zusammenhang (Hookesche Gesetz: σ = E·ε)
- `np.polyfit()` benötigt `import numpy as np`

---

### Aufgabe P5: Lager-Vibrations-Performance-Analyse (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 50-60 Minuten  
**Vorkenntnisse**: Schleifen, Funktionen, `plt.plot()`, `plt.subplot()`, Performance-Analyse

In dieser Aufgabe simulierst du die Vibrationseffekte bei Wälzlagern unter verschiedenen Betriebsbedingungen und visualisierst die Ergebnisse.

**Szenario**: Wälzlager erzeugen bei hohen Drehzahlen Vibrationsamplituden, die von der Drehzahl und dem Lagerzustand abhängen. Die Amplitude steigt mit der Drehzahl, aber gesunde Lager zeigen deutlich niedrigere Amplituden als beschädigte.

**Gegeben**:
- Lagerzustände: Neu (Faktor 1.0), Leicht verschlissen (Faktor 1.8), Stark verschlissen (Faktor 3.5), Beschädigt (Faktor 8.0)
- Drehzahlbereich: 100 bis 10.000 U/min
- Basisvibration bei 1000 U/min: 0.5 mm/s

**Aufgaben**:

**Teil a)**: Implementiere eine Funktion `berechne_vibrationsamplitude(drehzahl_upm, zustandsfaktor)`:
- Formel: `amplitude = basisvibration * (drehzahl / 1000)**0.7 * zustandsfaktor`
- Der Exponent 0.7 modelliert das nicht-lineare Verhalten bei steigender Drehzahl
- Rückgabe: Vibrationsamplitude in mm/s

**Teil b)**: Simuliere verschiedene Drehzahlen von 100 bis 10.000 U/min (in logarithmischen Schritten):
```python
drehzahlen = [100, 200, 500, 1000, 2000, 3000, 5000, 7000, 10000]  # U/min
```

Berechne für jede Drehzahl die Vibrationsamplituden für alle vier Lagerzustände.

**Teil c)**: Erstelle einen Plot mit **logarithmischer X-Achse**:
- X-Achse: "Drehzahl (U/min)" (logarithmisch: `plt.xscale('log')`)
- Y-Achse: "Vibrationsamplitude (mm/s)"
- Vier Linien für die vier Lagerzustände (verschiedene Farben und Linienstile)
- Titel: "Lager-Vibrations-Analyse: Einfluss von Drehzahl und Lagerzustand"
- Legende mit Lagerzuständen
- Gitterlinien aktiviert (`which='both'` für logarithmische Achse)

**Teil d)**: Erstelle einen zweiten Plot (verwende `plt.subplot(2, 1, 2)`), der den **Schadensfaktor** zeigt:
- Schadensfaktor = `Amplitude_Zustand / Amplitude_Neu` 
- Y-Achse: "Schadensfaktor (relativ zu Neu-Lager)"
- Zeige Schadensfaktoren für leicht verschlissen, stark verschlissen und beschädigt
- Markiere kritische Schwelle: `plt.axhline(y=5, color='red', linestyle='--', label='Kritische Schwelle')`

**Bonus-Challenge** (optional):
Erweitere die Simulation um **Resonanzeffekte**:
- Bei bestimmten Drehzahlen (z.B. 3000, 6000 U/min) treten Resonanzen auf
- Modifiziere die Formel um Resonanzpeaks zu berücksichtigen

**Beispiel-Ausgabe**:
Zwei Plots:
1. Vibrationsamplitude vs. Drehzahl: Zeigt steigendes Vibrationsniveau, deutliche Unterschiede zwischen Lagerzuständen
2. Schadensfaktor vs. Drehzahl: Zeigt, wie stark beschädigte Lager von gesunden abweichen

**Starter-Code**:
```python
import matplotlib.pyplot as plt

# Konstanten
BASISVIBRATION = 0.5  # mm/s bei 1000 U/min
REFERENZ_DREHZAHL = 1000
ZUSTANDSFAKTOREN = {
    'Neu': 1.0,
    'Leicht verschlissen': 1.8,
    'Stark verschlissen': 3.5,
    'Beschädigt': 8.0
}

def berechne_vibrationsamplitude(drehzahl_upm, zustandsfaktor):
    """
    Berechnet Vibrationsamplitude basierend auf Drehzahl und Lagerzustand.
    """
    # Dein Code hier
    pass

# Drehzahlen (logarithmisch verteilt)
drehzahlen = [100, 200, 500, 1000, 2000, 3000, 5000, 7000, 10000]

# Simuliere verschiedene Lagerzustände
# Dein Code hier

# Plot 1: Vibrationsamplituden
# Dein Code hier

# Plot 2: Schadensfaktoren
# Dein Code hier
```

**Hinweise**:
- Verwende `plt.subplot(2, 1, 1)` und `plt.subplot(2, 1, 2)` für zwei übereinander angeordnete Plots
- Logarithmische X-Achse: `plt.xscale('log')`
- Bei logarithmischen Achsen: `plt.grid(True, which='both', alpha=0.3)`
- Dictionary-Iteration: `for zustand, faktor in ZUSTANDSFAKTOREN.items()`

---

