# V14 - Betriebssysteme & Rechnerarchitektur – Teil 2 / Plots & Grafiken (Matplotlib) – Teil 2: Aufgaben

---

## Teil 1: Theorie-Aufgaben

### T1: Prozessverwaltung und Scheduling (⭐⭐)

Ein Betriebssystem muss folgende **vier Prozesse** schedulen. Gegeben sind die Ankunftszeit und die Burst-Time (benötigte CPU-Zeit):

| Prozess | Ankunft (ms) | Burst (ms) |
|---------|--------------|------------|
| P1      | 0            | 8          |
| P2      | 1            | 4          |
| P3      | 2            | 9          |
| P4      | 3            | 5          |

**Aufgaben:**

a) Erstellen Sie einen **Gantt-Chart** für **First-Come First-Served (FCFS)** Scheduling. Berechnen Sie die durchschnittliche **Wartezeit** und **Turnaround-Zeit**.

b) Erstellen Sie einen **Gantt-Chart** für **Shortest Job First (SJF)** (nicht-preemptiv). Berechnen Sie die durchschnittliche **Wartezeit** und **Turnaround-Zeit**.

c) Vergleichen Sie die Ergebnisse aus (a) und (b). Welcher Algorithmus ist effizienter und warum?

d) Nennen Sie **einen Nachteil** von SJF, der in der Praxis problematisch ist.

---

### T2: Virtueller Speicher und Paging (⭐⭐⭐)

Ein System verwendet **Paging** mit folgenden Eigenschaften:
- **Virtuelle Adressbreite**: 16 Bit
- **Page-Größe**: 1 KB (= 1024 Bytes)
- **Physischer Speicher**: 8 KB

**Page Table** für Prozess A:

| Virtuelle Page | Frame | Valid Bit |
|----------------|-------|-----------|
| 0              | 3     | 1         |
| 1              | 1     | 1         |
| 2              | -     | 0         |
| 3              | 5     | 1         |
| 4              | 2     | 1         |

**Aufgaben:**

a) Berechnen Sie die **Anzahl der virtuellen Pages** und die **Anzahl der physischen Frames** in diesem System.

b) Der Prozess greift auf die **virtuelle Adresse 0x0A50** (hexadezimal) zu. 
   - Berechnen Sie **Page Number** und **Offset**.
   - Bestimmen Sie die **physische Adresse** (hexadezimal).
   - Zeigen Sie die Umrechnung Schritt für Schritt.

c) Der Prozess greift auf die **virtuelle Adresse 0x0820** zu. Was passiert und warum? Welche Rolle spielt das Valid Bit?

d) Erklären Sie, warum **Paging** das **externe Fragmentierungsproblem** löst, aber **interne Fragmentierung** verursachen kann.

---

### T3: Dateisysteme und Journaling (⭐⭐)

**Situation**: Ein Linux-Server stürzt während eines Schreibvorgangs ab. Das Dateisystem ist **ext4** (mit Journaling).

**Aufgaben:**

a) Erklären Sie in **3-5 Sätzen**, wie **Journaling** funktioniert und welche Schritte das Dateisystem durchläuft, um Konsistenz zu gewährleisten.

b) **Vergleichen Sie** die drei Journaling-Modi von ext4:
   - **Journal**: Was wird geloggt?
   - **Ordered**: Was wird geloggt?
   - **Writeback**: Was wird geloggt?
   
   Ordnen Sie die Modi nach **Sicherheit** (höchste zuerst) und **Performance** (schnellste zuerst).

c) Nennen Sie **zwei moderne Dateisysteme** (außer ext4) und jeweils **eine Besonderheit**:
   - Beispiel: NTFS – verwendet Master File Table (MFT)

---

## Teil 2: Python-Aufgaben

### P1: Bar Chart - CPU-Auslastung visualisieren (⭐)

Ein Monitoring-System hat die durchschnittliche **CPU-Auslastung** verschiedener Prozesse über eine Stunde aufgezeichnet:

```python
prozesse = ['Python', 'Chrome', 'VS Code', 'Spotify', 'System']
cpu_prozent = [12.5, 28.3, 15.7, 8.2, 5.1]
```

**Aufgabe:**

Erstellen Sie einen **Bar Chart**, der:
- Die Prozesse auf der X-Achse zeigt
- Die CPU-Auslastung (%) auf der Y-Achse zeigt
- Balken in unterschiedlichen Farben darstellt (verwenden Sie eine Liste von Farben)
- Einen passenden **Titel** und **Achsenbeschriftungen** hat
- Ein **Gitter** auf der Y-Achse zeigt (`alpha=0.3`)
- Die Y-Achse von 0 bis 35 begrenzt

**Zusatz**: Markieren Sie Balken mit Auslastung > 20% in Rot, alle anderen in Blau.

---

### P2: Histogramm - Speicherzugriff-Latenz analysieren (⭐⭐)

Ein Benchmark hat **1000 Speicherzugriffe** gemessen. Die Latenzen (in Nanosekunden) sind normalverteilt mit Mittelwert 100 ns und Standardabweichung 15 ns.

**Aufgabe:**

a) Generieren Sie die Daten mit NumPy:
```python
import numpy as np
np.random.seed(42)
latenzen = np.random.normal(100, 15, 1000)
```

b) Erstellen Sie ein **Histogramm** mit:
- 30 Bins
- Hellblauer Füllfarbe (`'lightblue'`)
- Schwarzen Rändern (`edgecolor='black'`)
- Titel: "Verteilung der Speicherzugriff-Latenzen"
- X-Achse: "Latenz (ns)"
- Y-Achse: "Häufigkeit"
- Gitter auf der Y-Achse

c) Fügen Sie zwei **vertikale Linien** hinzu:
- Eine grüne gestrichelte Linie bei **Mittelwert** (100 ns) mit Label "Mittelwert"
- Eine rote gestrichelte Linie bei **Mittelwert + 2×Standardabweichung** (130 ns) mit Label "Ausreißer-Schwelle"

d) Zeigen Sie eine **Legende** an.

---

### P3: Subplots - Prozess-Monitor Dashboard (⭐⭐⭐)

Erstellen Sie ein **Dashboard mit 4 Subplots** (2×2 Grid), das verschiedene Systemmetriken visualisiert.

**Daten generieren:**
```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
zeit = np.arange(0, 60, 1)  # 60 Sekunden
cpu = 30 + 20 * np.sin(zeit / 10) + np.random.normal(0, 5, 60)
ram = 50 + 10 * np.sin(zeit / 15 + 1) + np.random.normal(0, 3, 60)
disk_read = np.random.exponential(10, 60)
disk_write = np.random.exponential(8, 60)
```

**Subplots:**

1. **Oben links**: CPU-Auslastung über Zeit
   - Linienplot mit blauer Linie
   - Fülle Bereich unter der Linie (blau, `alpha=0.3`)
   - Titel: "CPU-Auslastung (%)"

2. **Oben rechts**: RAM-Auslastung über Zeit
   - Linienplot mit grüner Linie
   - Horizontale rote Linie bei 70% (Warn-Schwelle)
   - Titel: "RAM-Auslastung (%)"

3. **Unten links**: Disk-Read vs. Disk-Write (Scatter)
   - X-Achse: `disk_read`, Y-Achse: `disk_write`
   - Rote Punkte, `alpha=0.5`
   - Titel: "Disk I/O Korrelation"

4. **Unten rechts**: Histogramm der CPU-Werte
   - 15 Bins, orange Farbe
   - Titel: "CPU-Verteilung"

**Anforderungen:**
- Verwenden Sie `plt.subplots(2, 2, figsize=(14, 10))`
- Nutzen Sie `tight_layout()`
- Haupttitel über allen Plots: "System-Monitor Dashboard"

---

### P4: Logarithmische Achsen - Speicher-Benchmark (⭐⭐⭐)

Ein Benchmark misst die **Speicherzugriffszeit** für verschiedene **Cache-Größen** (L1, L2, L3, RAM, SSD):

```python
import numpy as np
import matplotlib.pyplot as plt

groessen_kb = np.array([32, 256, 8192, 16384, 524288])  # KB
zugriffszeit_ns = np.array([0.5, 3, 15, 80, 100000])  # Nanosekunden
labels = ['L1 (32KB)', 'L2 (256KB)', 'L3 (8MB)', 'RAM (16MB)', 'SSD (512MB)']
```

**Aufgabe:**

a) Erstellen Sie einen **Plot mit logarithmischen Achsen** (log-log):
   - X-Achse: Speichergröße (KB) – logarithmisch
   - Y-Achse: Zugriffszeit (ns) – logarithmisch
   - Verwenden Sie rote Kreise als Marker (`'ro'`) mit `markersize=10`
   - Verbinden Sie Punkte mit gestrichelter Linie (`linestyle='--'`)

b) Beschriften Sie jeden Punkt mit dem entsprechenden Label aus der `labels`-Liste:
   - Verwenden Sie `plt.text()` oder `plt.annotate()`
   - Position: rechts neben jedem Punkt
   - Schriftgröße: 10

c) Fügen Sie hinzu:
   - Titel: "Speicher-Hierarchie: Größe vs. Zugriffszeit"
   - X-Achse: "Speichergröße (KB, log)"
   - Y-Achse: "Zugriffszeit (ns, log)"
   - Gitter mit `alpha=0.3`

d) Erklären Sie in einem **Kommentar**, warum logarithmische Achsen hier sinnvoll sind.

---

### P5: Komplettes Dashboard mit Annotationen (⭐⭐⭐⭐⭐)

Erstellen Sie eine **umfassende Visualisierung** eines Scheduling-Algorithmus-Vergleichs.

**Daten:**
```python
import numpy as np
import matplotlib.pyplot as plt

algorithmen = ['FCFS', 'SJF', 'Round Robin', 'Priority']
avg_wartezeit = [28.5, 15.2, 18.7, 20.1]  # Millisekunden
avg_turnaround = [45.3, 32.6, 36.4, 38.2]  # Millisekunden
context_switches = [0, 0, 24, 12]  # Anzahl
```

**Aufgabe:**

Erstellen Sie eine Figure mit **3 Subplots** (vertikal angeordnet):

**Subplot 1: Gruppiertes Bar Chart**
- X-Achse: Algorithmen
- Y-Achse: Zeit (ms)
- Zwei Balken pro Algorithmus: Wartezeit (blau) und Turnaround-Zeit (orange)
- Legende mit Label "Wartezeit" und "Turnaround"
- Titel: "Performance-Vergleich: Wartezeit vs. Turnaround"

**Subplot 2: Horizontales Bar Chart**
- Y-Achse: Algorithmen
- X-Achse: Anzahl Context Switches
- Balkenfarbe: Grün
- Fügen Sie **Text-Labels** am Ende jeder Leiste hinzu (Wert)
- Titel: "Context Switches pro Algorithmus"

**Subplot 3: Scatter Plot mit Annotationen**
- X-Achse: Wartezeit
- Y-Achse: Turnaround-Zeit
- Jeder Algorithmus als Punkt
- **Annotieren** Sie jeden Punkt mit dem Algorithmus-Namen
- Verwenden Sie `arrowprops` für Pfeile von Annotationen zu Punkten
- Titel: "Wartezeit vs. Turnaround-Zeit Korrelation"

**Zusätzliche Anforderungen:**
- Gesamtgröße: `figsize=(12, 14)`
- Verwenden Sie `tight_layout()`
- Haupt-Titel über allen Plots: "Scheduling-Algorithmen: Detaillierter Vergleich"
- Speichern Sie das Ergebnis als `scheduling_vergleich.png` mit **300 DPI**

**Bonus (+)**: Heben Sie in Subplot 1 den besten Algorithmus (kürzeste Wartezeit) farblich hervor.

---

## Hinweise

### Allgemeine Hinweise

- Verwenden Sie `import matplotlib.pyplot as plt` für alle Matplotlib-Aufgaben
- Verwenden Sie `import numpy as np` für numerische Operationen
- Testen Sie Ihren Code in einer Python-Umgebung (IDLE, Jupyter, VS Code)
- Achten Sie auf **konsistente Formatierung**: Titel, Labels, Legenden wo sinnvoll

### Matplotlib Best Practices

- Verwenden Sie **aussagekräftige Titel** und **Achsenbeschriftungen**
- Setzen Sie **Gitter** mit `alpha=0.3` für bessere Lesbarkeit
- Nutzen Sie `tight_layout()` bei Subplots
- Verwenden Sie `figsize` für angemessene Plot-Größen
- Speichern Sie Plots mit **mind. 300 DPI** für Publikationen

### Debugging-Tipps

- **Plot wird nicht angezeigt**: Fehlt `plt.show()` am Ende?
- **Subplots überlappen**: Haben Sie `tight_layout()` vergessen?
- **Logarithmische Achse leer**: Enthält Ihr Datensatz Null oder negative Werte?
- **Gruppierte Bar Charts falsch positioniert**: Prüfen Sie die `x`-Positionen mit `np.arange()` und die `width`-Anpassung

---

**Viel Erfolg bei den Aufgaben!** 🚀
