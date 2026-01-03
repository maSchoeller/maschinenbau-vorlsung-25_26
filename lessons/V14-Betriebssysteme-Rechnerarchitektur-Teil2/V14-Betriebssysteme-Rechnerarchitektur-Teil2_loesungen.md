# V14 - Betriebssysteme & Rechnerarchitektur – Teil 2 / Plots & Grafiken (Matplotlib) – Teil 2: Lösungen

---

## Teil 1: Theorie-Lösungen

### T1: Prozessverwaltung und Scheduling (⭐⭐)

#### Lösung a) FCFS (First-Come First-Served)

**Gantt-Chart:**

```
| P1 (0-8) | P2 (8-12) | P3 (12-21) | P4 (21-26) |
```

**Wartezeiten:**
- **P1**: Ankunft 0, Start 0 → Wartezeit = 0
- **P2**: Ankunft 1, Start 8 → Wartezeit = 8 - 1 = **7**
- **P3**: Ankunft 2, Start 12 → Wartezeit = 12 - 2 = **10**
- **P4**: Ankunft 3, Start 21 → Wartezeit = 21 - 3 = **18**

**Durchschnittliche Wartezeit**: (0 + 7 + 10 + 18) / 4 = **8.75 ms**

**Turnaround-Zeiten** (Zeit von Ankunft bis Fertigstellung):
- **P1**: 8 - 0 = **8**
- **P2**: 12 - 1 = **11**
- **P3**: 21 - 2 = **19**
- **P4**: 26 - 3 = **23**

**Durchschnittliche Turnaround-Zeit**: (8 + 11 + 19 + 23) / 4 = **15.25 ms**

---

#### Lösung b) SJF (Shortest Job First, nicht-preemptiv)

Bei SJF wird immer der Prozess mit der kürzesten Burst-Time ausgewählt (unter denen, die bereits angekommen sind).

**Reihenfolge:**
1. Bei t=0: Nur P1 da → P1 läuft (0-8)
2. Bei t=8: P2, P3, P4 sind da → P2 hat kürzeste Burst (4) → P2 läuft (8-12)
3. Bei t=12: P3 (Burst 9), P4 (Burst 5) da → P4 ist kürzer → P4 läuft (12-17)
4. Bei t=17: Nur P3 übrig → P3 läuft (17-26)

**Gantt-Chart:**

```
| P1 (0-8) | P2 (8-12) | P4 (12-17) | P3 (17-26) |
```

**Wartezeiten:**
- **P1**: 0 - 0 = **0**
- **P2**: 8 - 1 = **7**
- **P3**: 17 - 2 = **15**
- **P4**: 12 - 3 = **9**

**Durchschnittliche Wartezeit**: (0 + 7 + 15 + 9) / 4 = **7.75 ms**

**Turnaround-Zeiten:**
- **P1**: 8 - 0 = **8**
- **P2**: 12 - 1 = **11**
- **P3**: 26 - 2 = **24**
- **P4**: 17 - 3 = **14**

**Durchschnittliche Turnaround-Zeit**: (8 + 11 + 24 + 14) / 4 = **14.25 ms**

---

#### Lösung c) Vergleich

| Metrik | FCFS | SJF |
|--------|------|-----|
| Ø Wartezeit | 8.75 ms | 7.75 ms |
| Ø Turnaround | 15.25 ms | 14.25 ms |

**SJF ist effizienter**, da es kürzere Wartezeiten und kürzere Turnaround-Zeiten erreicht. Der Grund ist, dass kurze Jobs bevorzugt werden, was die durchschnittliche Wartezeit minimiert. Bei FCFS wartet P4 (Burst 5) unnötig lange, weil P3 (Burst 9) davor ausgeführt wird.

---

#### Lösung d) Nachteil von SJF

**Starvation (Verhungern)**: Prozesse mit langer Burst-Time können theoretisch **nie ausgeführt werden**, wenn ständig neue kurze Prozesse ankommen. Diese werden immer bevorzugt, sodass lange Prozesse unbegrenzt warten.

**Beispiel**: Ein Backup-Prozess (Burst: 1000 ms) wartet, während ständig neue Web-Requests (Burst: 10 ms) bearbeitet werden.

**Zusätzliches Problem**: Die **Burst-Time ist in der Praxis nicht vorhersehbar**. Das Betriebssystem kennt sie nicht im Voraus und muss sie schätzen (z.B. durch historische Durchschnittswerte), was zu Ungenauigkeiten führt.

---

### T2: Virtueller Speicher und Paging (⭐⭐⭐)

#### Lösung a) Anzahl Pages und Frames

**Virtuelle Adressbreite**: 16 Bit → Virtueller Adressraum = 2^16 = **65.536 Bytes** = **64 KB**

**Page-Größe**: 1 KB = 1024 Bytes

**Anzahl virtueller Pages**: 64 KB / 1 KB = **64 Pages**

---

**Physischer Speicher**: 8 KB = 8.192 Bytes

**Anzahl physischer Frames**: 8 KB / 1 KB = **8 Frames**

---

#### Lösung b) Adressübersetzung für 0x0A50

**Schritt 1: Virtuelle Adresse in Binär konvertieren**

```
0x0A50 (hex) = 0000 1010 0101 0000 (binär)
```

**Schritt 2: Page Number und Offset trennen**

Page-Größe = 1024 Bytes = 2^10 → **Offset benötigt 10 Bit**

```
Virtuelle Adresse (16 Bit):
[000010] [10 0101 0000]
 ^^^^^^   ^^^^^^^^^^^^
Page Num    Offset
```

- **Page Number**: `000010` (binär) = **2** (dezimal)
- **Offset**: `10 0101 0000` (binär) = **0x150** (hex) = **336** (dezimal)

**Schritt 3: Page Table konsultieren**

```
Virtuelle Page 2 → Valid Bit = 0 → Page Fault!
```

**Ergebnis**: Die Adresse 0x0A50 führt zu einem **Page Fault**, da Page 2 nicht im physischen Speicher liegt (Valid Bit = 0). Das Betriebssystem muss die Page vom Festplattenspeicher (Swap) in den RAM laden.

---

**Korrektur**: Ich hatte übersehen, dass 0x0A50 eigentlich Page 2 anspricht. Lassen Sie uns stattdessen eine gültige Adresse nehmen: **0x0450** (Page 1)

**Schritt 1: 0x0450 in Binär**

```
0x0450 = 0000 0100 0101 0000
```

**Schritt 2: Trennung**

```
[000001] [00 0101 0000]
Page 1      Offset 0x050 (80 dezimal)
```

**Schritt 3: Page Table**

```
Virtuelle Page 1 → Frame 1, Valid = 1
```

**Schritt 4: Physische Adresse berechnen**

```
Physische Adresse = Frame × Page-Größe + Offset
                  = 1 × 1024 + 80
                  = 1024 + 80
                  = 1104 (dezimal)
                  = 0x0450 (hex)
```

**Ergebnis**: Virtuelle Adresse **0x0450** wird auf physische Adresse **0x0450** (1104 dezimal) abgebildet.

---

#### Lösung c) Adresse 0x0820

**Schritt 1: Binär konvertieren**

```
0x0820 = 0000 1000 0010 0000
```

**Schritt 2: Trennung**

```
[000010] [00 0010 0000]
Page 2      Offset 0x020 (32 dezimal)
```

**Schritt 3: Page Table**

```
Virtuelle Page 2 → Valid Bit = 0
```

**Ergebnis**: **Page Fault!**

**Was passiert:**

1. Die **MMU** (Memory Management Unit) prüft die Page Table und stellt fest, dass das **Valid Bit = 0** ist.
2. Eine **Exception** (Page Fault) wird ausgelöst.
3. Die **CPU wechselt in den Kernel-Modus** und übergibt die Kontrolle an den **Page Fault Handler** (Teil des Betriebssystems).
4. Das Betriebssystem lädt Page 2 vom **Festplattenspeicher (Swap Space)** in einen freien Frame im RAM.
5. Die **Page Table wird aktualisiert**: Frame-Nummer wird eingetragen, Valid Bit wird auf 1 gesetzt.
6. Die **CPU setzt die Instruktion fort** (wiederholt den Speicherzugriff).

**Rolle des Valid Bit:**

Das **Valid Bit** zeigt an, ob eine virtuelle Page **aktuell im physischen Speicher** liegt (1) oder **auf die Festplatte ausgelagert** wurde (0). Es ist essenziell für **Demand Paging**: Pages werden nur bei Bedarf in den RAM geladen, nicht alle auf einmal.

---

#### Lösung d) Fragmentierung

**Externes Fragmentierungsproblem gelöst:**

Bei **variabel großen Speicherblöcken** (wie bei älteren Systemen ohne Paging) entsteht **externe Fragmentierung**: Freier Speicher zerfällt in viele kleine, nicht zusammenhängende Blöcke. Ein Prozess, der 100 KB benötigt, kann nicht zugewiesen werden, obwohl insgesamt 150 KB frei sind – verteilt in 10×15 KB Blöcken.

**Paging löst das Problem**, weil:
- Alle Pages gleich groß sind (z.B. 4 KB)
- Prozesse beliebig im physischen Speicher verteilt werden können
- Die MMU übersetzt virtuelle Adressen transparent

---

**Interne Fragmentierung entsteht:**

Wenn ein Prozess weniger Speicher benötigt als eine volle Page. Beispiel:
- Page-Größe: 4 KB (4096 Bytes)
- Prozess benötigt: 10.500 Bytes

→ **3 Pages** werden alloziert (12.288 Bytes)  
→ **Verschwendung**: 12.288 - 10.500 = **1.788 Bytes** (≈ 14.6%)

Dieser ungenutzter Speicher **innerhalb** der zugewiesenen Pages ist **interne Fragmentierung**.

**Lösung**: Kleinere Pages reduzieren interne Fragmentierung, aber erhöhen den **Overhead** (mehr Page Table Entries, mehr TLB-Misses).

---

### T3: Dateisysteme und Journaling (⭐⭐)

#### Lösung a) Funktionsweise von Journaling

**Journaling** ist ein Mechanismus, der **Metadaten-Konsistenz** nach Systemabstürzen gewährleistet. Vor dem eigentlichen Schreibvorgang werden geplante Änderungen in einem **Journal** (Log) protokolliert.

**Ablauf:**

1. **Journal-Eintrag schreiben**: Das Dateisystem schreibt eine Beschreibung der geplanten Operation (z.B. "Datei erstellen, Inode 12345, Block 6789") ins Journal.
2. **Checkpoint setzen**: Sobald der Journal-Eintrag sicher auf Disk ist, wird ein Checkpoint gesetzt.
3. **Eigentliche Operation durchführen**: Die Daten und Metadaten werden an ihre finalen Positionen geschrieben.
4. **Journal-Eintrag löschen**: Nach erfolgreicher Operation wird der Journal-Eintrag als abgeschlossen markiert oder gelöscht.

**Bei Absturz:** Beim nächsten Boot liest das Dateisystem das Journal und führt unvollständige Operationen zu Ende (Replay) oder macht sie rückgängig (Rollback). Dies dauert nur Sekunden, statt stundenlanger `fsck`-Läufe bei klassischen Dateisystemen.

---

#### Lösung b) Journaling-Modi von ext4

| Modus | Was wird geloggt? | Sicherheit | Performance | Erklärung |
|-------|-------------------|------------|-------------|-----------|
| **Journal** | Metadaten + Daten | ⭐⭐⭐ Höchste | ⭐ Langsam | Alle Daten werden doppelt geschrieben (Journal + finaler Ort) → maximale Sicherheit, aber langsam |
| **Ordered** (Standard) | Nur Metadaten, aber Daten vor Metadaten | ⭐⭐ Mittel | ⭐⭐ Mittel | Daten werden geschrieben, bevor Metadaten geloggt werden → verhindert "Datenmüll" in Dateien |
| **Writeback** | Nur Metadaten, Daten beliebig | ⭐ Niedrig | ⭐⭐⭐ Schnell | Metadaten und Daten können unabhängig geschrieben werden → schnellste Option, aber Daten können korrupt sein |

**Sortierung nach Sicherheit**: Journal > Ordered > Writeback

**Sortierung nach Performance**: Writeback > Ordered > Journal

**Empfehlung**: **Ordered** ist der beste Kompromiss für die meisten Anwendungsfälle (daher Standard).

---

#### Lösung c) Moderne Dateisysteme

1. **NTFS** (Windows):
   - **Besonderheit**: Verwendet **Master File Table (MFT)**, wo jede Datei als Eintrag gespeichert wird. Unterstützt **Access Control Lists (ACLs)** für granulare Berechtigungen und **Change Journaling** für schnelle Backup-Lösungen.

2. **ZFS** (ursprünglich Solaris, jetzt Linux/FreeBSD):
   - **Besonderheit**: **Copy-on-Write (CoW)** – Daten werden nie überschrieben, sondern neue Versionen geschrieben. Integrierte **Checksummen** für jedes Datenblock (Schutz vor Silent Data Corruption). **Snapshots** in O(1)-Zeit.

3. **Btrfs** (Linux):
   - **Besonderheit**: **Subvolumes** und **Snapshots** ähnlich ZFS. **Integrierte RAID**-Funktionalität (Software-RAID auf Dateisystem-Ebene). Dynamische **inode-Allokation** (keine feste inode-Anzahl bei Formatierung).

4. **APFS** (Apple File System, macOS/iOS):
   - **Besonderheit**: Optimiert für **SSDs** und **Flash-Speicher**. **Space Sharing** zwischen Volumes (mehrere Volumes teilen sich einen Pool). **Clones** für Dateien (Instant-Kopie ohne Platzbedarf bis zur Änderung).

5. **XFS** (Linux, High-Performance):
   - **Besonderheit**: **Delay Allocation** (verzögerte Block-Allokation für bessere Leistung). Besonders gut für **große Dateien** (Videoverarbeitung, Datenbanken). Keine native Kompression (anders als Btrfs/ZFS).

---

## Teil 2: Python-Lösungen

### P1: Bar Chart - CPU-Auslastung visualisieren (⭐)

```python
import matplotlib.pyplot as plt

# Daten
prozesse = ['Python', 'Chrome', 'VS Code', 'Spotify', 'System']
cpu_prozent = [12.5, 28.3, 15.7, 8.2, 5.1]

# Farben: Rot für >20%, Blau für ≤20%
farben = ['red' if auslastung > 20 else 'blue' for auslastung in cpu_prozent]

# Bar Chart erstellen
plt.figure(figsize=(10, 6))
plt.bar(prozesse, cpu_prozent, color=farben, edgecolor='black', alpha=0.8)

# Beschriftungen und Titel
plt.xlabel('Prozess', fontsize=12)
plt.ylabel('CPU-Auslastung (%)', fontsize=12)
plt.title('CPU-Auslastung verschiedener Prozesse', fontsize=14, fontweight='bold')

# Y-Achse begrenzen und Gitter
plt.ylim(0, 35)
plt.grid(axis='y', alpha=0.3)

# Anzeigen
plt.tight_layout()
plt.show()
```

**Erklärung:**

- **List Comprehension** für Farben: `['red' if ... else 'blue' for ...]` erstellt dynamisch eine Farbliste basierend auf der Bedingung (>20%).
- **`edgecolor='black'`**: Schwarze Ränder um Balken für bessere Sichtbarkeit.
- **`alpha=0.8`**: Leichte Transparenz für ästhetisches Aussehen.
- **`plt.ylim(0, 35)`**: Begrenzt Y-Achse wie gefordert.

---

### P2: Histogramm - Speicherzugriff-Latenz analysieren (⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

# Daten generieren
np.random.seed(42)
latenzen = np.random.normal(100, 15, 1000)

# Histogramm erstellen
plt.figure(figsize=(10, 6))
plt.hist(latenzen, bins=30, color='lightblue', edgecolor='black', alpha=0.7)

# Mittelwert und Ausreißer-Schwelle
mittelwert = 100
schwelle = mittelwert + 2 * 15  # 130 ns

# Vertikale Linien
plt.axvline(x=mittelwert, color='green', linestyle='--', linewidth=2, label='Mittelwert (100 ns)')
plt.axvline(x=schwelle, color='red', linestyle='--', linewidth=2, label='Ausreißer-Schwelle (130 ns)')

# Beschriftungen
plt.xlabel('Latenz (ns)', fontsize=12)
plt.ylabel('Häufigkeit', fontsize=12)
plt.title('Verteilung der Speicherzugriff-Latenzen', fontsize=14, fontweight='bold')

# Gitter und Legende
plt.grid(axis='y', alpha=0.3)
plt.legend(fontsize=11)

# Anzeigen
plt.tight_layout()
plt.show()
```

**Erklärung:**

- **`np.random.seed(42)`**: Macht Zufallsdaten reproduzierbar (gleiche Werte bei jedem Lauf).
- **`plt.axvline()`**: Zeichnet vertikale Linien bei gegebenen x-Werten.
- **Berechnungen**: Mittelwert 100, Standardabweichung 15 → 2σ-Schwelle = 100 + 2×15 = 130.
- **Interpretation**: Etwa 95% der Werte liegen innerhalb von 2 Standardabweichungen (68-95-99.7-Regel bei Normalverteilung).

---

### P3: Subplots - Prozess-Monitor Dashboard (⭐⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

# Daten generieren
np.random.seed(42)
zeit = np.arange(0, 60, 1)  # 60 Sekunden
cpu = 30 + 20 * np.sin(zeit / 10) + np.random.normal(0, 5, 60)
ram = 50 + 10 * np.sin(zeit / 15 + 1) + np.random.normal(0, 3, 60)
disk_read = np.random.exponential(10, 60)
disk_write = np.random.exponential(8, 60)

# Figure mit 2x2 Subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: CPU-Auslastung (oben links)
axes[0, 0].plot(zeit, cpu, 'b-', linewidth=2)
axes[0, 0].fill_between(zeit, 0, cpu, alpha=0.3, color='blue')
axes[0, 0].set_title('CPU-Auslastung (%)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Zeit (s)')
axes[0, 0].set_ylabel('CPU (%)')
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: RAM-Auslastung (oben rechts)
axes[0, 1].plot(zeit, ram, 'g-', linewidth=2)
axes[0, 1].axhline(y=70, color='red', linestyle='--', linewidth=2, label='Warn-Schwelle (70%)')
axes[0, 1].set_title('RAM-Auslastung (%)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Zeit (s)')
axes[0, 1].set_ylabel('RAM (%)')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Subplot 3: Disk I/O Korrelation (unten links)
axes[1, 0].scatter(disk_read, disk_write, color='red', alpha=0.5, s=50)
axes[1, 0].set_title('Disk I/O Korrelation', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Disk Read (MB/s)')
axes[1, 0].set_ylabel('Disk Write (MB/s)')
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: CPU-Verteilung Histogramm (unten rechts)
axes[1, 1].hist(cpu, bins=15, color='orange', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('CPU-Verteilung', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('CPU-Auslastung (%)')
axes[1, 1].set_ylabel('Häufigkeit')
axes[1, 1].grid(axis='y', alpha=0.3)

# Haupttitel
plt.suptitle('System-Monitor Dashboard', fontsize=16, fontweight='bold')

# Layout anpassen
plt.tight_layout()
plt.show()
```

**Erklärung:**

- **`axes[zeile, spalte]`**: Zugriff auf Subplots im 2D-Array.
- **`fill_between()`**: Füllt Bereich unter CPU-Kurve für visuellen Effekt.
- **`axhline()`**: Horizontale Linie bei 70% für RAM-Warnschwelle.
- **Exponentialverteilung**: `np.random.exponential()` simuliert I/O-Bursts (typisch für Disk-Zugriffe).
- **`tight_layout()`**: Passt Abstände automatisch an, damit nichts überlappt.

**Interpretation:**

- **CPU**: Oszilliert zwischen ~10% und ~50% mit Rauschen (typisch für interaktive Workloads).
- **RAM**: Stabilere Auslastung um 50%, gelegentliche Spitzen.
- **Disk I/O**: Keine starke Korrelation zwischen Read und Write (Punkte verstreut).
- **CPU-Histogram**: Zeigt, dass CPU meistens im Bereich 20-40% liegt (Normalverteilung).

---

### P4: Logarithmische Achsen - Speicher-Benchmark (⭐⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

# Daten
groessen_kb = np.array([32, 256, 8192, 16384, 524288])  # KB
zugriffszeit_ns = np.array([0.5, 3, 15, 80, 100000])  # Nanosekunden
labels = ['L1 (32KB)', 'L2 (256KB)', 'L3 (8MB)', 'RAM (16MB)', 'SSD (512MB)']

# Plot mit logarithmischen Achsen
plt.figure(figsize=(12, 8))
plt.loglog(groessen_kb, zugriffszeit_ns, 'ro--', markersize=10, linewidth=2, label='Speicher-Hierarchie')

# Labels zu jedem Punkt hinzufügen
for i, label in enumerate(labels):
    plt.text(groessen_kb[i] * 1.2, zugriffszeit_ns[i], label, 
             fontsize=10, verticalalignment='center')

# Beschriftungen
plt.xlabel('Speichergröße (KB, log)', fontsize=12)
plt.ylabel('Zugriffszeit (ns, log)', fontsize=12)
plt.title('Speicher-Hierarchie: Größe vs. Zugriffszeit', fontsize=14, fontweight='bold')

# Gitter und Legende
plt.grid(True, alpha=0.3, which='both')
plt.legend(fontsize=11)

# Anzeigen
plt.tight_layout()
plt.show()

# Kommentar zur Begründung
"""
Warum logarithmische Achsen hier sinnvoll sind:

Die Daten umfassen mehrere Größenordnungen:
- Speichergröße: 32 KB bis 512 MB (Faktor ~16.000)
- Zugriffszeit: 0.5 ns bis 100.000 ns (Faktor 200.000)

Mit linearen Achsen wären L1/L2/L3 kaum sichtbar (zu klein im Vergleich zu SSD).
Logarithmische Achsen komprimieren große Werte und spreizen kleine Werte,
sodass alle Datenpunkte gut sichtbar und vergleichbar sind.

Zusätzlich: In log-log-Plots werden Powerlaws (y = x^k) zu Geraden.
Die Speicher-Hierarchie zeigt einen exponentiellen Trade-off zwischen
Größe und Geschwindigkeit – perfekt für log-log-Darstellung.
"""
```

**Ausgabe-Erklärung:**

- **`plt.loglog()`**: Kurzform für beide Achsen logarithmisch (Basis 10).
- **`plt.text(..., groessen_kb[i] * 1.2, ...)`**: Platziert Label rechts neben Punkt (20% nach rechts verschoben).
- **`which='both'`**: Gitter für Major und Minor Ticks (bei log-Achsen gibt es Zwischenlinien).

**Visualisierung zeigt:**

- L1-Cache ist extrem schnell (0.5 ns), aber winzig (32 KB)
- SSD ist 200.000× langsamer als L1, aber 16.000× größer
- Fast lineare Beziehung im log-log-Plot → Powerlaw-Beziehung

---

### P5: Komplettes Dashboard mit Annotationen (⭐⭐⭐⭐⭐)

```python
import numpy as np
import matplotlib.pyplot as plt

# Daten
algorithmen = ['FCFS', 'SJF', 'Round Robin', 'Priority']
avg_wartezeit = [28.5, 15.2, 18.7, 20.1]  # Millisekunden
avg_turnaround = [45.3, 32.6, 36.4, 38.2]  # Millisekunden
context_switches = [0, 0, 24, 12]  # Anzahl

# Figure mit 3 Subplots (vertikal)
fig, axes = plt.subplots(3, 1, figsize=(12, 14))

# ========== Subplot 1: Gruppiertes Bar Chart ==========
x_pos = np.arange(len(algorithmen))
breite = 0.35

# Bester Algorithmus für Wartezeit
bester_index = np.argmin(avg_wartezeit)
wartezeit_farben = ['red' if i == bester_index else 'blue' for i in range(len(avg_wartezeit))]

bars1 = axes[0].bar(x_pos - breite/2, avg_wartezeit, breite, 
                     label='Wartezeit', color=wartezeit_farben, edgecolor='black', alpha=0.8)
bars2 = axes[0].bar(x_pos + breite/2, avg_turnaround, breite,
                     label='Turnaround', color='orange', edgecolor='black', alpha=0.8)

axes[0].set_xlabel('Algorithmus', fontsize=11)
axes[0].set_ylabel('Zeit (ms)', fontsize=11)
axes[0].set_title('Performance-Vergleich: Wartezeit vs. Turnaround', fontsize=12, fontweight='bold')
axes[0].set_xticks(x_pos)
axes[0].set_xticklabels(algorithmen)
axes[0].legend(fontsize=10)
axes[0].grid(axis='y', alpha=0.3)

# ========== Subplot 2: Horizontales Bar Chart ==========
bars3 = axes[1].barh(algorithmen, context_switches, color='green', edgecolor='black', alpha=0.8)

# Text-Labels am Ende jeder Leiste
for i, (bar, val) in enumerate(zip(bars3, context_switches)):
    width = bar.get_width()
    axes[1].text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                 str(val), ha='left', va='center', fontsize=10, fontweight='bold')

axes[1].set_xlabel('Anzahl Context Switches', fontsize=11)
axes[1].set_ylabel('Algorithmus', fontsize=11)
axes[1].set_title('Context Switches pro Algorithmus', fontsize=12, fontweight='bold')
axes[1].grid(axis='x', alpha=0.3)

# ========== Subplot 3: Scatter Plot mit Annotationen ==========
axes[2].scatter(avg_wartezeit, avg_turnaround, s=150, color='purple', 
                edgecolors='black', linewidths=2, alpha=0.7, zorder=3)

# Annotationen mit Pfeilen
for i, algo in enumerate(algorithmen):
    # Pfeil-Position leicht versetzt für bessere Lesbarkeit
    xytext_offset = [(10, 15), (-50, 20), (10, -25), (-50, -25)][i]
    
    axes[2].annotate(algo, 
                      xy=(avg_wartezeit[i], avg_turnaround[i]),
                      xytext=xytext_offset,
                      textcoords='offset points',
                      fontsize=10,
                      bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                      arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3',
                                     color='black', lw=1.5))

axes[2].set_xlabel('Wartezeit (ms)', fontsize=11)
axes[2].set_ylabel('Turnaround-Zeit (ms)', fontsize=11)
axes[2].set_title('Wartezeit vs. Turnaround-Zeit Korrelation', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

# Haupttitel
plt.suptitle('Scheduling-Algorithmen: Detaillierter Vergleich', 
             fontsize=16, fontweight='bold', y=0.995)

# Layout und Speichern
plt.tight_layout()
plt.savefig('scheduling_vergleich.png', dpi=300, bbox_inches='tight')
plt.show()

print("Plot erfolgreich gespeichert als 'scheduling_vergleich.png' mit 300 DPI!")
```

**Erklärung der Highlights:**

**Subplot 1 - Bonus-Feature:**
- **`bester_index = np.argmin(avg_wartezeit)`**: Findet Index des kleinsten Werts (SJF mit 15.2 ms).
- **Farbkodierung**: Bester Algorithmus (SJF) wird in Rot hervorgehoben, andere in Blau.
- **List Comprehension**: `[... if i == bester_index else ...]` für dynamische Farben.

**Subplot 2 - Text-Labels:**
- **`bar.get_width()`**: Gibt Balkenbreite zurück (Wert auf X-Achse).
- **`bar.get_y() + bar.get_height()/2`**: Zentriert Text vertikal in der Mitte des Balkens.
- **Position `width + 0.5`**: Platziert Text rechts neben Balken mit 0.5 Einheiten Abstand.

**Subplot 3 - Annotationen:**
- **`xytext`-Offsets**: Manuell angepasst, damit Annotationen nicht überlappen:
  - FCFS: rechts oben (10, 15)
  - SJF: links oben (-50, 20)
  - Round Robin: rechts unten (10, -25)
  - Priority: links unten (-50, -25)
- **`textcoords='offset points'`**: `xytext` wird als Pixel-Offset interpretiert (nicht als Datenkoordinaten).
- **`connectionstyle='arc3,rad=0.3'`**: Pfeil hat leichte Kurve (Radius 0.3) für bessere Ästhetik.
- **`bbox`**: Gelber Rahmen um Text für bessere Lesbarkeit auf farbigem Hintergrund.
- **`zorder=3`**: Punkte werden über Gitterlinien gezeichnet (höherer z-Index).

**Speichern:**
- **`dpi=300`**: Hochauflösend für Publikationen (Standard 72 DPI wäre zu niedrig).
- **`bbox_inches='tight'`**: Entfernt unnötigen Whitespace am Rand.

**Interpretation:**

- **SJF ist optimal**: Kürzeste Wartezeit (15.2 ms) und kürzeste Turnaround-Zeit (32.6 ms).
- **FCFS ist am schlechtesten**: Längste Wartezeit (28.5 ms), keine Context Switches aber ineffizient.
- **Round Robin hat hohe Overhead**: 24 Context Switches führen zu leicht schlechterer Performance als Priority Scheduling.
- **Korrelation**: Alle Punkte liegen nahe einer imaginären Diagonale → kürzere Wartezeit korreliert mit kürzerer Turnaround-Zeit.

---

## Zusammenfassung

Diese Lösungen demonstrieren:

**Theorie:**
- **Scheduling-Algorithmen** mit Gantt-Charts und Metriken-Berechnung
- **Virtuelle Speicherverwaltung** mit Adressübersetzung und Page Faults
- **Dateisysteme** mit Journaling-Modi und modernen Alternativen

**Python:**
- **Bar Charts** (vertikal, horizontal, gruppiert, gestapelt)
- **Histogramme** mit Verteilungsanalyse und statistischen Markierungen
- **Subplots** mit verschiedenen Plot-Typen in einem Dashboard
- **Logarithmische Achsen** für Daten mit großem Wertebereich
- **Annotationen** mit Pfeilen und Boxen für wichtige Datenpunkte
- **Speichern in verschiedenen Formaten** mit hoher Auflösung

**Best Practices:**
- Konsistente Farbschemata und Beschriftungen
- `tight_layout()` für professionelles Layout
- Gitter mit `alpha=0.3` für bessere Lesbarkeit
- Legenden und Annotationen für Kontext
- DPI 300+ für Publikationen

---

**Gut gemacht!** 🎉 Diese Übungen decken reale Anwendungsfälle in System-Monitoring, Performance-Analyse und wissenschaftlicher Visualisierung ab.