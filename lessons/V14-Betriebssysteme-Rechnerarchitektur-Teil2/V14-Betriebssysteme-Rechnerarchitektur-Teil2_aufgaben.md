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

### P1: Bar Chart - CNC-Maschinenpräzision visualisieren (⭐)

Eine Qualitätskontrolle hat die **Positioniergenauigkeit** (Abweichung in μm) verschiedener CNC-Maschinen über einen Produktionstag gemessen:

```python
maschinen = ['CNC-01', 'CNC-02', 'CNC-03', 'CNC-04', 'CNC-05']
abweichung_um = [2.3, 8.7, 4.2, 1.8, 3.5]  # Mikrometer
```

**Aufgabe:**

Erstellen Sie einen **Bar Chart**, der:
- Die Maschinen auf der X-Achse zeigt
- Die Abweichung (μm) auf der Y-Achse zeigt
- Balken in unterschiedlichen Farben darstellt (verwenden Sie eine Liste von Farben)
- Einen passenden **Titel** und **Achsenbeschriftungen** hat
- Ein **Gitter** auf der Y-Achse zeigt (`alpha=0.3`)
- Die Y-Achse von 0 bis 12 begrenzt

**Zusatz**: Markieren Sie Balken mit Abweichung > 5 μm in Rot (außerhalb Toleranz), alle anderen in Grün (innerhalb Toleranz).

---

### P2: Histogramm - Hydraulikdruck-Schwankungen analysieren (⭐⭐)

Eine Hydraulikanlage hat **1000 Druckmessungen** während eines Produktionszyklus aufgezeichnet. Die Drücke (in bar) sind normalverteilt mit Mittelwert 180 bar und Standardabweichung 12 bar.

**Aufgabe:**

a) Generieren Sie die Daten mit NumPy:
```python
import numpy as np
np.random.seed(42)
druecke_bar = np.random.normal(180, 12, 1000)
```

b) Erstellen Sie ein **Histogramm** mit:
- 30 Bins
- Hellblauer Füllfarbe (`'lightblue'`)
- Schwarzen Rändern (`edgecolor='black'`)
- Titel: "Verteilung der Hydraulikdruck-Schwankungen"
- X-Achse: "Druck (bar)"
- Y-Achse: "Häufigkeit"
- Gitter auf der Y-Achse

c) Fügen Sie zwei **vertikale Linien** hinzu:
- Eine grüne gestrichelte Linie bei **Solldruck** (180 bar) mit Label "Solldruck"
- Eine rote gestrichelte Linie bei **Maximal zulässiger Druck** (204 bar = Mittelwert + 2×Standardabweichung) mit Label "Kritische Grenze"

d) Zeigen Sie eine **Legende** an.

---

### P3: Subplots - Materialprüfungs-Dashboard (⭐⭐⭐)

Erstellen Sie ein **Dashboard mit 4 Subplots** (2×2 Grid), das verschiedene Materialprüfungs-Metriken visualisiert.

**Daten generieren:**
```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
zeit_min = np.arange(0, 60, 1)  # 60 Minuten Zugversuch
zugspannung_mpa = 150 + 80 * np.sin(zeit_min / 10) + np.random.normal(0, 10, 60)
dehnung_prozent = 2.0 + 1.5 * np.sin(zeit_min / 15 + 1) + np.random.normal(0, 0.3, 60)
temperatur_c = np.random.exponential(25, 60) + 20  # Probentemperatur
kraftaufnahme_kn = np.random.exponential(15, 60) + 10
```

**Subplots:**

1. **Oben links**: Zugspannung über Zeit
   - Linienplot mit blauer Linie
   - Fülle Bereich unter der Linie (blau, `alpha=0.3`)
   - Titel: "Zugspannung (MPa)"

2. **Oben rechts**: Dehnung über Zeit
   - Linienplot mit grüner Linie
   - Horizontale rote Linie bei 5% (Bruchgrenze)
   - Titel: "Dehnung (%)"

3. **Unten links**: Temperatur vs. Kraftaufnahme (Scatter)
   - X-Achse: `temperatur_c`, Y-Achse: `kraftaufnahme_kn`
   - Rote Punkte, `alpha=0.5`
   - Titel: "Temperatur vs. Kraft Korrelation"

4. **Unten rechts**: Histogramm der Zugspannungswerte
   - 15 Bins, orange Farbe
   - Titel: "Zugspannungs-Verteilung"

**Anforderungen:**
- Verwenden Sie `plt.subplots(2, 2, figsize=(14, 10))`
- Nutzen Sie `tight_layout()`
- Haupttitel über allen Plots: "Materialprüfungs-Dashboard"

---

### P4: Logarithmische Achsen - Werkzeugstandzeit-Analyse (⭐⭐⭐)

Eine Verschleißanalyse misst die **Werkzeugstandzeit** für verschiedene **Schnittgeschwindigkeiten** bei unterschiedlichen Werkzeugen:

```python
import numpy as np
import matplotlib.pyplot as plt

schnittgeschw_m_min = np.array([50, 100, 200, 400, 800])  # m/min
standzeit_min = np.array([720, 180, 45, 11, 3])  # Minuten (Taylor-Gleichung)
labels = ['HSS niedrig', 'HSS hoch', 'HM niedrig', 'HM hoch', 'Keramik']
```

**Aufgabe:**

a) Erstellen Sie einen **Plot mit logarithmischen Achsen** (log-log):
   - X-Achse: Schnittgeschwindigkeit (m/min) – logarithmisch
   - Y-Achse: Werkzeugstandzeit (min) – logarithmisch
   - Verwenden Sie rote Kreise als Marker (`'ro'`) mit `markersize=10`
   - Verbinden Sie Punkte mit gestrichelter Linie (`linestyle='--'`)

b) Beschriften Sie jeden Punkt mit dem entsprechenden Label aus der `labels`-Liste:
   - Verwenden Sie `plt.text()` oder `plt.annotate()`
   - Position: rechts neben jedem Punkt
   - Schriftgröße: 10

c) Fügen Sie hinzu:
   - Titel: "Werkzeugverschleiß: Schnittgeschwindigkeit vs. Standzeit (Taylor-Gleichung)"
   - X-Achse: "Schnittgeschwindigkeit (m/min, log)"
   - Y-Achse: "Werkzeugstandzeit (min, log)"
   - Gitter mit `alpha=0.3`

d) Erklären Sie in einem **Kommentar**, warum logarithmische Achsen hier sinnvoll sind (Hinweis: Taylor-Gleichung vc × T^n = konstant).

---

### P5: Komplettes Dashboard mit Annotationen (⭐⭐⭐⭐⭐)

Erstellen Sie eine **umfassende Visualisierung** eines Fertigungsverfahrens-Vergleichs.

**Daten:**
```python
import numpy as np
import matplotlib.pyplot as plt

verfahren = ['Drehen', 'Fräsen', 'Bohren', 'Schleifen']
durchlaufzeit_min = [12.5, 18.3, 8.7, 22.1]  # Minuten pro Werkstück
ruestzeit_min = [25.3, 35.6, 15.4, 45.2]  # Rüstzeit in Minuten
werkzeugwechsel = [0, 3, 1, 5]  # Anzahl Werkzeugwechsel pro Werkstück
```

**Aufgabe:**

Erstellen Sie eine Figure mit **3 Subplots** (vertikal angeordnet):

**Subplot 1: Gruppiertes Bar Chart**
- X-Achse: Verfahren
- Y-Achse: Zeit (min)
- Zwei Balken pro Verfahren: Durchlaufzeit (blau) und Rüstzeit (orange)
- Legende mit Label "Durchlaufzeit" und "Rüstzeit"
- Titel: "Fertigungsverfahren: Durchlauf- vs. Rüstzeit"

**Subplot 2: Horizontales Bar Chart**
- Y-Achse: Verfahren
- X-Achse: Anzahl Werkzeugwechsel
- Balkenfarbe: Grün
- Fügen Sie **Text-Labels** am Ende jeder Leiste hinzu (Wert)
- Titel: "Werkzeugwechsel pro Verfahren"

**Subplot 3: Scatter Plot mit Annotationen**
- X-Achse: Durchlaufzeit
- Y-Achse: Rüstzeit
- Jedes Verfahren als Punkt
- **Annotieren** Sie jeden Punkt mit dem Verfahrensnamen
- Verwenden Sie `arrowprops` für Pfeile von Annotationen zu Punkten
- Titel: "Durchlaufzeit vs. Rüstzeit Korrelation"

**Zusätzliche Anforderungen:**
- Gesamtgröße: `figsize=(12, 14)`
- Verwenden Sie `tight_layout()`
- Haupt-Titel über allen Plots: "Fertigungsverfahren: Detaillierter Vergleich"
- Speichern Sie das Ergebnis als `fertigungsverfahren_vergleich.png` mit **300 DPI**

**Bonus (+)**: Heben Sie in Subplot 1 das Verfahren mit der kürzesten Durchlaufzeit farblich hervor.

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
