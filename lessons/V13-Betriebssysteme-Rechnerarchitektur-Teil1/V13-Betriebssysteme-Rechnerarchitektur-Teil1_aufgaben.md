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

### Aufgabe P1: Erste Plots mit Matplotlib (Leicht)

**Schwierigkeit**: ⭐ Leicht  
**Zeitaufwand**: ca. 15-20 Minuten  
**Vorkenntnisse**: Matplotlib-Installation, `plt.plot()`, Achsenbeschriftungen

Erstelle ein Python-Programm, das folgende lineare Funktionen im Bereich x = 0 bis x = 10 (in 0.5er-Schritten) visualisiert:
- `y₁ = 2x + 1`
- `y₂ = -0.5x + 8`
- `y₃ = x`

**Anforderungen**:
1. Alle drei Funktionen sollen im selben Plot dargestellt werden
2. Verwende unterschiedliche Farben für jede Funktion (rot, blau, grün)
3. Füge eine Legende hinzu mit den Funktionsgleichungen
4. Beschrifte die X-Achse mit "x-Wert" und die Y-Achse mit "y-Wert"
5. Setze den Titel "Lineare Funktionen im Vergleich"
6. Aktiviere Gitterlinien

**Beispiel Ein-/Ausgabe**:
```
(Ein grafisches Fenster öffnet sich mit dem Plot)
```

**Starter-Code**:
```python
import matplotlib.pyplot as plt

# Erstelle x-Werte von 0 bis 10 in 0.5er-Schritten
x = [i * 0.5 for i in range(21)]  # 0, 0.5, 1.0, ..., 10.0

# Berechne y-Werte für die drei Funktionen
# Dein Code hier

# Erstelle den Plot
# Dein Code hier
```

**Hinweise**:
- Verwende `range(21)`, da 0 bis 10 in 0.5er-Schritten 21 Werte ergibt (0, 0.5, 1.0, ..., 10.0)
- List Comprehension ist nützlich für die Berechnung der y-Werte

---

### Aufgabe P2: Temperaturverlauf visualisieren (Leicht-Mittel)

**Schwierigkeit**: ⭐⭐ Leicht-Mittel  
**Zeitaufwand**: ca. 20-25 Minuten  
**Vorkenntnisse**: `plt.plot()`, Linienstile, Marker

Ein Temperatur-Sensor in einer Fertigungshalle misst die Temperatur stündlich über 24 Stunden. Gegeben sind folgende Messdaten:

```python
stunden = list(range(24))  # 0 bis 23 Uhr
temperaturen = [18, 18, 17, 17, 16, 16, 17, 19, 21, 23, 
                25, 27, 28, 29, 28, 27, 26, 24, 22, 21, 
                20, 19, 19, 18]  # °C
```

**Aufgaben**:

**Teil a)**: Erstelle einen Linienplot der Temperatur über die Zeit:
- X-Achse: "Uhrzeit (Stunde)"
- Y-Achse: "Temperatur (°C)"
- Titel: "Temperaturverlauf über 24 Stunden"
- Verwende eine durchgezogene Linie mit Marker-Punkten (`'o-'`)
- Farbe: Orange
- Gitterlinien aktiviert

**Teil b)**: Füge eine horizontale Linie bei 20°C hinzu, die die **Soll-Temperatur** markiert:
- Verwende `plt.axhline(y=20, color='red', linestyle='--', label='Soll-Temperatur')`
- Ergänze die Legende

**Teil c)**: Markiere alle Zeitpunkte, an denen die Temperatur über 25°C liegt, mit roten Scatter-Punkten:
- Filtere Stunden und Temperaturen, bei denen `temperatur > 25`
- Verwende `plt.scatter()` für diese Punkte mit Farbe Rot und größerem Marker (`s=100`)
- Label: "Überhitzung (>25°C)"

**Beispiel-Ausgabe**:
Ein Plot mit orangener Linie, roter gestrichelter Soll-Linie und roten Markierungen bei Überhitzungen.

**Hinweise**:
- Verwende List Comprehension oder eine Schleife zum Filtern der Überhitzungs-Punkte
- `plt.axhline()` zeichnet eine horizontale Linie über die gesamte X-Achse

---

### Aufgabe P3: CPU-Frequenzen im Vergleich (Mittel)

**Schwierigkeit**: ⭐⭐ Mittel  
**Zeitaufwand**: ca. 25-30 Minuten  
**Vorkenntnisse**: Scatter Plots, Farben, Marker-Größen

Historische Daten über CPU-Taktfrequenzen verschiedener Prozessor-Generationen:

```python
jahre = [1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023]
intel_mhz = [16, 33, 150, 1400, 3800, 3600, 4000, 5300, 6000]
amd_mhz = [12, 40, 133, 1000, 2600, 3200, 4700, 4900, 5700]
kerne = [1, 1, 1, 1, 2, 4, 8, 16, 24]  # Anzahl CPU-Kerne
```

**Aufgaben**:

**Teil a)**: Erstelle einen Scatter Plot, der die Entwicklung von Intel und AMD CPU-Frequenzen über die Zeit zeigt:
- X-Achse: "Jahr"
- Y-Achse: "Taktfrequenz (MHz)"
- Titel: "CPU-Taktfrequenzen: Intel vs. AMD (1985-2023)"
- Intel: Blaue Kreise
- AMD: Rote Quadrate (`marker='s'`)
- Beide mit Label für Legende

**Teil b)**: Skaliere die **Marker-Größe** proportional zur Anzahl der CPU-Kerne:
- Verwende `s=kerne * 20` für die Marker-Größe bei beiden Scatter-Plots
- Füge eine Anmerkung hinzu: `plt.text(2018, 1000, "Größe ∝ Kerne", fontsize=10)`

**Teil c)**: Verbinde die Intel-Datenpunkte mit einer gestrichelten Linie und die AMD-Datenpunkte mit einer gepunkteten Linie:
- Verwende zusätzlich `plt.plot()` mit `linestyle='--'` (Intel) und `linestyle=':'` (AMD)
- Wichtig: Verwende dieselben Farben wie bei den Scatter-Punkten

**Teil d)**: Setze die Y-Achse auf logarithmische Skalierung:
- `plt.yscale('log')`
- Dies zeigt das exponentielle Wachstum deutlicher

**Hinweise**:
- Scatter-Plots und Linienplots können im selben Plot kombiniert werden
- Logarithmische Skala eignet sich für Daten mit großem Wertebereich
- `plt.text(x, y, text)` fügt Text an Position (x, y) ein

---

### Aufgabe P4: Messdaten-Analyse mit Fehlerbalken (Mittel-Schwer)

**Schwierigkeit**: ⭐⭐⭐ Mittel-Schwer  
**Zeitaufwand**: ca. 35-40 Minuten  
**Vorkenntnisse**: `plt.plot()`, `plt.scatter()`, `plt.fill_between()`, statistische Konzepte

Ein Ingenieur misst die Zugfestigkeit eines Materials bei verschiedenen Temperaturen. Jede Messung wurde 5-mal wiederholt, um die Streuung zu erfassen:

```python
temperaturen = [20, 40, 60, 80, 100, 120, 140, 160]  # °C
zugfestigkeit_mittel = [450, 445, 438, 428, 415, 398, 375, 348]  # MPa
zugfestigkeit_std = [12, 15, 18, 22, 25, 30, 35, 40]  # MPa (Standardabweichung)
```

**Aufgaben**:

**Teil a)**: Erstelle einen Plot mit Fehlerbalken:
- X-Achse: "Temperatur (°C)"
- Y-Achse: "Zugfestigkeit (MPa)"
- Titel: "Temperaturabhängigkeit der Zugfestigkeit"
- Verwende `plt.errorbar(x, y, yerr=std, fmt='o-', capsize=5, label='Messdaten ± Std')`
- Farbe: Dunkelblau
- Gitterlinien aktiviert

**Teil b)**: Füge einen **Unsicherheitsbereich** (Confidence Band) hinzu:
- Verwende `plt.fill_between()` um den Bereich Mittelwert ± Standardabweichung zu schattieren
- Berechne obere Grenze: `[mittel + std for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std)]`
- Berechne untere Grenze: `[mittel - std for mittel, std in zip(zugfestigkeit_mittel, zugfestigkeit_std)]`
- `plt.fill_between(temperaturen, untere_grenze, obere_grenze, alpha=0.2, color='blue', label='±1σ Bereich')`

**Teil c)**: Markiere kritische Bereiche:
- Wenn Zugfestigkeit < 380 MPa: Material gilt als **kritisch**
- Finde alle Temperaturen, bei denen Zugfestigkeit < 380 MPa
- Zeichne diese Bereiche mit roter Hintergrund-Schattierung: `plt.axvspan(temp_start, temp_end, color='red', alpha=0.15, label='Kritischer Bereich')`

**Teil d)**: Füge eine Trendlinie hinzu:
- Verwende `numpy.polyfit()` für eine lineare Regression: `koeffizienten = np.polyfit(temperaturen, zugfestigkeit_mittel, deg=1)`
- Berechne Trendlinie: `trendlinie = [koeffizienten[0] * t + koeffizienten[1] for t in temperaturen]`
- Zeichne Trendlinie mit gestrichelter schwarzer Linie: `plt.plot(temperaturen, trendlinie, 'k--', label='Trendlinie')`

**Beispiel-Ausgabe**:
Ein Plot mit blauen Datenpunkten mit Fehlerbalken, blauem Unsicherheitsbereich, roter kritischer Zone ab ca. 120°C, und schwarzer Trendlinie.

**Hinweise**:
- `plt.errorbar()` ist speziell für Messdaten mit Unsicherheiten
- `plt.fill_between()` schattiert den Bereich zwischen zwei Kurven
- `plt.axvspan(xmin, xmax, ...)` schattiert einen vertikalen Bereich
- NumPy wird hier verwendet (Installation: `pip install numpy`)
- `np.polyfit(x, y, deg)` berechnet Polynom-Koeffizienten (deg=1 für linear)

---

### Aufgabe P5: Cache-Performance-Simulation (Schwer/Komplex)

**Schwierigkeit**: ⭐⭐⭐⭐ Schwer/Komplex  
**Zeitaufwand**: ca. 50-60 Minuten  
**Vorkenntnisse**: Schleifen, Funktionen, `plt.plot()`, `plt.subplot()`, Performance-Analyse

In dieser Aufgabe simulierst du die Auswirkungen von Cache-Größen auf die Programm-Performance und visualisierst die Ergebnisse.

**Szenario**: Ein Programm durchläuft ein Array und greift sequenziell auf Elemente zu. Die Performance hängt davon ab, ob Daten im Cache liegen (Cache Hit) oder aus dem RAM geladen werden müssen (Cache Miss).

**Gegeben**:
- L1-Cache: 64 KB, Zugriffszeit: 4 Taktzyklen
- L2-Cache: 512 KB, Zugriffszeit: 12 Taktzyklen
- L3-Cache: 8 MB, Zugriffszeit: 40 Taktzyklen
- RAM: Zugriffszeit: 100 Taktzyklen
- Jedes Array-Element: 8 Bytes (Float)

**Aufgaben**:

**Teil a)**: Implementiere eine Funktion `berechne_zugriffszeit(array_groesse_kb, cache_groesse_kb, cache_zyklen)`, die die **durchschnittliche Zugriffszeit** berechnet:
- Wenn `array_groesse_kb <= cache_groesse_kb`: Alle Daten im Cache → Zugriffszeit = `cache_zyklen`
- Sonst: Cache Miss Rate = `1 - (cache_groesse_kb / array_groesse_kb)`
- Durchschnittliche Zeit = `(1 - miss_rate) * cache_zyklen + miss_rate * ram_zyklen`

**Teil b)**: Simuliere verschiedene Array-Größen von 1 KB bis 16 MB (verwende logarithmische Schritte):
```python
array_groessen_kb = [2**i for i in range(0, 15)]  # 1, 2, 4, 8, ..., 16384 KB
```

Berechne für jede Array-Größe die durchschnittliche Zugriffszeit für:
- Nur L1-Cache (64 KB)
- L1 + L2-Cache (kombiniert: Erst L1, dann L2, dann RAM)
- L1 + L2 + L3-Cache (kombiniert: Erst L1, dann L2, dann L3, dann RAM)

**Teil c)**: Erstelle einen Plot mit **logarithmischer X-Achse**:
- X-Achse: "Array-Größe (KB)" (logarithmisch: `plt.xscale('log')`)
- Y-Achse: "Durchschnittliche Zugriffszeit (Taktzyklen)"
- Drei Linien für die drei Cache-Konfigurationen
- Titel: "Cache-Performance: Einfluss der Array-Größe"
- Legende mit Cache-Hierarchien
- Gitterlinien aktiviert

**Teil d)**: Erstelle einen zweiten Plot (verwende `plt.subplot(2, 1, 2)`), der die **Speedup** zeigt:
- Speedup = `Zugriffszeit_ohne_Cache / Zugriffszeit_mit_Cache`
- "Ohne Cache" bedeutet: Alle Zugriffe gehen direkt zum RAM (100 Taktzyklen)
- Y-Achse: "Speedup-Faktor"
- Zeige Speedup für L1, L1+L2, L1+L2+L3

**Bonus-Challenge** (optional):
Erweitere die Simulation um **Cache Line Effects**:
- Cache Lines sind typisch 64 Bytes (8 Float-Werte)
- Bei sequenziellem Zugriff wird eine ganze Cache Line geladen → Spatial Locality
- Modifiziere die Simulation, um diesen Effekt zu berücksichtigen

**Beispiel-Ausgabe**:
Zwei Plots:
1. Zugriffszeit vs. Array-Größe: Stufenförmige Kurven, die bei Cache-Größen "springen"
2. Speedup vs. Array-Größe: Zeigt, wie dramatisch Cache die Performance verbessert

**Starter-Code**:
```python
import matplotlib.pyplot as plt

# Konstanten
L1_KB = 64
L2_KB = 512
L3_KB = 8 * 1024  # 8 MB
RAM_ZYKLEN = 100
L1_ZYKLEN = 4
L2_ZYKLEN = 12
L3_ZYKLEN = 40

def berechne_zugriffszeit(array_groesse_kb, cache_groesse_kb, cache_zyklen, naechster_cache_zyklen):
    """
    Berechnet durchschnittliche Zugriffszeit basierend auf Cache-Größe.
    
    Args:
        array_groesse_kb: Größe des Arrays in KB
        cache_groesse_kb: Größe des Caches in KB
        cache_zyklen: Zugriffszeit bei Cache Hit
        naechster_cache_zyklen: Zugriffszeit bei Cache Miss (nächste Ebene)
    
    Returns:
        Durchschnittliche Zugriffszeit in Taktzyklen
    """
    # Dein Code hier
    pass

# Array-Größen von 1 KB bis 16 MB (logarithmisch)
array_groessen_kb = [2**i for i in range(0, 15)]

# Simuliere verschiedene Cache-Hierarchien
# Dein Code hier

# Plot 1: Zugriffszeiten
# Dein Code hier

# Plot 2: Speedup
# Dein Code hier
```

**Hinweise**:
- Verwende `plt.subplot(2, 1, 1)` und `plt.subplot(2, 1, 2)` für zwei übereinander angeordnete Plots
- Logarithmische X-Achse: `plt.xscale('log')`
- Bei Cache-Hierarchien: Erst L1 prüfen, dann L2, dann L3, dann RAM
- Die Kurven sollten "Stufen" zeigen: Bei kleinen Arrays ist alles schnell, bei größeren Arrays wird es stufenweise langsamer

---

