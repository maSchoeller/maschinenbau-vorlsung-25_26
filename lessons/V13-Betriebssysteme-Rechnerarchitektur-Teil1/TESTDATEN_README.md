# Testdaten für V13 - Betriebssysteme & Rechnerarchitektur Teil 1

Diese Datei beschreibt die Testdaten, die für die Python-Aufgaben in Vorlesung 13 benötigt werden.

---

## Datei: lager_vibrationsdaten.csv

**Verwendung**: Aufgabe P5 - Lager-Vibrations-Datenanalyse

**Beschreibung**: Diese CSV-Datei enthält realistische Vibrationsmessdaten von Wälzlagern in vier verschiedenen Zuständen über einen weiten Drehzahlbereich.

### Datei-Statistik

- **Anzahl Datensätze**: 120 Messpunkte
- **Datensätze pro Zustand**: 30 Messpunkte
- **Drehzahlbereich**: 100 - 10.000 U/min
- **Dateigröße**: ~3,7 KB

### Spalten-Struktur

Die CSV-Datei hat folgende Spalten (mit Header):

```
Drehzahl_UPM,Zustand,Amplitude_mm_s,Temperatur_C,Betriebsstunden
```

| Spaltenname | Typ | Einheit | Beschreibung |
|-------------|-----|---------|--------------|
| **Drehzahl_UPM** | Integer | U/min | Drehzahl des Lagers in Umdrehungen pro Minute |
| **Zustand** | String | - | Lagerzustand: `Neu`, `Leicht_verschlissen`, `Stark_verschlissen`, `Beschaedigt` |
| **Amplitude_mm_s** | Float | mm/s | Gemessene Vibrationsamplitude in Millimeter pro Sekunde |
| **Temperatur_C** | Float | °C | Lagertemperatur in Grad Celsius |
| **Betriebsstunden** | Integer | h | Kumulative Betriebsstunden des Lagers |

### Beispiel-Zeilen

```csv
Drehzahl_UPM,Zustand,Amplitude_mm_s,Temperatur_C,Betriebsstunden
100,Neu,0.18,45,10
1000,Neu,0.58,54,10
10000,Neu,1.52,73,10
100,Leicht_verschlissen,0.32,47,2500
1000,Leicht_verschlissen,1.04,60,2500
10000,Leicht_verschlissen,2.74,89,2500
100,Stark_verschlissen,0.63,52,5000
1000,Stark_verschlissen,2.03,73,5000
10000,Stark_verschlissen,5.33,112,5000
100,Beschaedigt,1.44,58,7500
1000,Beschaedigt,4.64,87,7500
10000,Beschaedigt,12.16,134,7500
```

### Lagerzustände

**1. Neu** (30 Messpunkte)
- Betriebsstunden: 10-100 h
- Vibrationsamplitude: 0.18 - 1.53 mm/s
- Temperatur: 45 - 74°C
- Verhalten: Niedrige, stabile Vibrationen

**2. Leicht verschlissen** (30 Messpunkte)
- Betriebsstunden: 2.500-3.500 h
- Vibrationsamplitude: 0.32 - 2.76 mm/s
- Temperatur: 47 - 90°C
- Verhalten: Moderat erhöhte Vibrationen (Faktor ~1.8)

**3. Stark verschlissen** (30 Messpunkte)
- Betriebsstunden: 5.000-6.000 h
- Vibrationsamplitude: 0.63 - 5.35 mm/s
- Temperatur: 52 - 113°C
- Verhalten: Deutlich erhöhte Vibrationen (Faktor ~3.5)

**4. Beschädigt** (30 Messpunkte)
- Betriebsstunden: 7.500-8.500 h
- Vibrationsamplitude: 1.44 - 12.18 mm/s
- Temperatur: 58 - 135°C
- Verhalten: Kritisch hohe Vibrationen (Faktor ~8)

### Verwendung in Python

**Einlesen der Datei**:

```python
# Methode 1: Mit open() und manueller Parsing
datei = 'lager_vibrationsdaten.csv'
daten = {'Neu': {'drehzahl': [], 'amplitude': [], 'temperatur': []},
         'Leicht_verschlissen': {'drehzahl': [], 'amplitude': [], 'temperatur': []},
         'Stark_verschlissen': {'drehzahl': [], 'amplitude': [], 'temperatur': []},
         'Beschaedigt': {'drehzahl': [], 'amplitude': [], 'temperatur': []}}

with open(datei, 'r') as f:
    next(f)  # Header überspringen
    for line in f:
        teile = line.strip().split(',')
        drehzahl = int(teile[0])
        zustand = teile[1]
        amplitude = float(teile[2])
        temperatur = float(teile[3])
        betriebsstunden = int(teile[4])
        
        daten[zustand]['drehzahl'].append(drehzahl)
        daten[zustand]['amplitude'].append(amplitude)
        daten[zustand]['temperatur'].append(temperatur)
```

**Daten sortieren**:

```python
# Sortiere Daten nach Drehzahl für saubere Plots
for zustand in daten:
    kombiniert = sorted(zip(daten[zustand]['drehzahl'], 
                           daten[zustand]['amplitude'], 
                           daten[zustand]['temperatur']))
    daten[zustand]['drehzahl'] = [k[0] for k in kombiniert]
    daten[zustand]['amplitude'] = [k[1] for k in kombiniert]
    daten[zustand]['temperatur'] = [k[2] for k in kombiniert]
```

**Visualisierung**:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
for zustand in daten:
    plt.plot(daten[zustand]['drehzahl'], 
             daten[zustand]['amplitude'], 
             label=zustand.replace('_', ' '), 
             marker='o')

plt.xscale('log')
plt.xlabel('Drehzahl (U/min)')
plt.ylabel('Vibrationsamplitude (mm/s)')
plt.title('Lager-Vibrations-Analyse')
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.show()
```

### Physikalische Interpretation

Die Daten zeigen realistische Verhaltensmuster von Wälzlagern:

1. **Drehzahl-Abhängigkeit**: Vibrationsamplitude steigt mit Drehzahl (nicht-linear, ~n^0.7)
2. **Verschleiß-Progression**: Jeder Zustand zeigt charakteristische Erhöhung
3. **Temperatur-Korrelation**: Höhere Vibrationen → höhere Temperaturen (Reibung)
4. **Kritische Schwelle**: Bei Schadensfaktor > 5 ist sofortiger Lagerwechsel erforderlich

### Erwartete Ergebnisse

**Schadensfaktor-Berechnung**:

Für Drehzahl 1000 U/min:
- Neu: 0.58 mm/s (Basis)
- Leicht verschlissen: 1.04 mm/s → Faktor: 1.04/0.58 ≈ 1.79
- Stark verschlissen: 2.03 mm/s → Faktor: 2.03/0.58 ≈ 3.50
- Beschädigt: 4.64 mm/s → Faktor: 4.64/0.58 ≈ 8.00

**Statistische Auswertung** (gerundet):
```
Max. Amplitude Neu: 1.53 mm/s
Max. Amplitude Leicht verschlissen: 2.76 mm/s
Max. Amplitude Stark verschlissen: 5.35 mm/s
Max. Amplitude Beschädigt: 12.18 mm/s

Durchschn. Temp. Neu: 58.3°C
Durchschn. Temp. Leicht verschlissen: 68.5°C
Durchschn. Temp. Stark verschlissen: 84.7°C
Durchschn. Temp. Beschädigt: 99.8°C
```

### Hinweise für Studierende

- Die CSV-Datei muss im selben Verzeichnis wie das Python-Skript liegen
- Achte auf korrekte Spaltennamen beim Einlesen (inkl. Unterstriche)
- Sortierung der Daten ist wichtig für saubere Linienplots
- Bei logarithmischen Plots: `plt.xscale('log')` verwenden
- Schadensfaktor-Berechnung erfordert Zuordnung gleicher Drehzahlen

### Erweiterungsmöglichkeiten

1. **Korrelationsanalyse**: Zusammenhang Amplitude ↔ Temperatur
2. **Regression**: Formel für Amplitude(Drehzahl, Zustand) ermitteln
3. **Prognose**: Wann erreicht "Leicht verschlissen" kritischen Zustand?
4. **3D-Plot**: Drehzahl × Zustand × Amplitude visualisieren
5. **Histogramme**: Verteilung der Amplituden pro Zustand

---

**Erstellt**: 2026-01-04  
**Vorlesung**: V13 - Betriebssysteme & Rechnerarchitektur Teil 1  
**Datengröße**: 120 Messpunkte über 4 Lagerzustände
