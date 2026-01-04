# Testdaten für V14 - Betriebssysteme & Rechnerarchitektur Teil 2

Dieses Verzeichnis enthält Testdaten für die Python-Aufgaben in V14 im **CSV-, JSON- und XML-Format**.

---

## Übersicht der Dateien

### 1. `cnc_praezision.csv` - CNC-Präzisionsmessungen

**Verwendung**: Aufgabe P1 (Bar Chart)

**Beschreibung**: Enthält Präzisionsmessungen von 15 CNC-Maschinen unterschiedlicher Typen mit Abweichungen in drei Achsen.

**Struktur**:
```csv
Maschine,Abweichung_X_um,Abweichung_Y_um,Abweichung_Z_um,Temperatur_C,Betriebsstunden
CNC-Fräse-01,2.3,1.8,2.1,22.5,1250
...
```

**Spalten**:
- `Maschine`: Maschinentyp und Identifikationsnummer
- `Abweichung_X_um`: Positionsabweichung X-Achse in Mikrometern
- `Abweichung_Y_um`: Positionsabweichung Y-Achse in Mikrometern
- `Abweichung_Z_um`: Positionsabweichung Z-Achse in Mikrometern
- `Temperatur_C`: Betriebstemperatur der Maschine in °C
- `Betriebsstunden`: Gesamtbetriebsstunden der Maschine

**Datensätze**: 15 Maschinen

**Verwendungsbeispiel**:
```python
import pandas as pd
import numpy as np

daten = pd.read_csv('cnc_praezision.csv')
# Berechne Gesamt-Abweichung
daten['gesamt_abweichung'] = np.sqrt(
    daten['Abweichung_X_um']**2 + 
    daten['Abweichung_Y_um']**2 + 
    daten['Abweichung_Z_um']**2
)
```

---

### 2. `werkstoff_pruefung.json` - Materialprüfungs-Daten

**Verwendung**: Aufgabe P3 (Box Plots)

**Beschreibung**: JSON-Datei mit Materialprüfungs-Ergebnissen für verschiedene Stahl- und Aluminium-Legierungen gemäß DIN EN ISO 6892-1.

**Struktur**:
```json
{
  "pruef_info": {
    "datum": "2024-03-15",
    "labor": "Materialtechnik Labor TU Berlin",
    "norm": "DIN EN ISO 6892-1",
    "pruefer": "Dr. Schmidt"
  },
  "proben": [
    {
      "proben_id": "S235-001",
      "werkstoff": "S235JR",
      "zugfestigkeit_mpa": 412,
      "streckgrenze_mpa": 285,
      "bruchdehnung_prozent": 28.5,
      "elastizitaetsmodul_gpa": 210,
      "haerte_hv": 145
    },
    ...
  ]
}
```

**Enthaltene Werkstoffe**:
- S235JR (Baustahl, 2 Proben)
- S355J2 (Baustahl, 1 Probe)
- C45E (Vergütungsstahl, 2 Proben)
- 42CrMo4 (Vergütungsstahl, 1 Probe)
- X5CrNi18-10 (Edelstahl, 1 Probe)
- AlMgSi1 (Aluminium, 1 Probe)

**Datensätze**: 8 Proben

**Verwendungsbeispiel**:
```python
import json

with open('werkstoff_pruefung.json', 'r', encoding='utf-8') as file:
    pruef_daten = json.load(file)

# Gruppiere nach Werkstoff
werkstoffe = {}
for probe in pruef_daten['proben']:
    werkstoff = probe['werkstoff']
    if werkstoff not in werkstoffe:
        werkstoffe[werkstoff] = []
    werkstoffe[werkstoff].append(probe['zugfestigkeit_mpa'])
```

---

### 3. `produktionslinien_vergleich.xml` - Produktionslinien-Analyse

**Verwendung**: Aufgabe P5 (Radar/Polar Chart)

**Beschreibung**: XML-Datei mit Performance-Daten von 5 Produktionslinien (Montage, Schweißen, Lackierung, Prüfung) eines Automotive-Zulieferers.

**Struktur**:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<produktionsvergleich>
  <meta>
    <unternehmen>AutoTeile GmbH</unternehmen>
    <standort>München</standort>
    <analysedatum>2024-03-20</analysedatum>
  </meta>
  <linien>
    <linie>
      <name>Linie-A</name>
      <typ>Montage</typ>
      <kapazitaet_stueck_h>120</kapazitaet_stueck_h>
      <tatsaechliche_output_stueck_h>108</tatsaechliche_output_stueck_h>
      <ausschussquote_prozent>2.1</ausschussquote_prozent>
      <ruestzeit_min_pro_umstellung>45</ruestzeit_min_pro_umstellung>
      <anzahl_mitarbeiter>12</anzahl_mitarbeiter>
      <energieverbrauch_kwh_h>68.5</energieverbrauch_kwh_h>
      <wartungskosten_euro_monat>3200</wartungskosten_euro_monat>
    </linie>
    ...
  </linien>
</produktionsvergleich>
```

**Enthaltene Linien**:
- Linie-A: Montage
- Linie-B: Schweißen
- Linie-C: Lackierung
- Linie-D: Montage
- Linie-E: Prüfung

**Datensätze**: 5 Produktionslinien

**Verwendungsbeispiel**:
```python
import xml.etree.ElementTree as ET

tree = ET.parse('produktionslinien_vergleich.xml')
root = tree.getroot()

linien_daten = []
for linie in root.findall('.//linie'):
    name = linie.find('name').text
    kapazitaet = float(linie.find('kapazitaet_stueck_h').text)
    output = float(linie.find('tatsaechliche_output_stueck_h').text)
    auslastung = (output / kapazitaet) * 100
    
    linien_daten.append({
        'name': name,
        'auslastung': auslastung
    })
```

---

## Hinweise

### CSV-Dateien
- Verwenden Sie `pandas.read_csv()` zum Einlesen
- Encoding: UTF-8
- Trennzeichen: Komma (`,`)

### JSON-Dateien
- Verwenden Sie `json.load()` zum Einlesen
- Encoding: UTF-8
- Verschachteltes Format mit Metadaten und Daten-Arrays

### XML-Dateien
- Verwenden Sie `xml.etree.ElementTree` zum Parsen
- Encoding: UTF-8
- Hierarchische Struktur mit Meta-Informationen

---

## Aufgabenverteilung

| Aufgabe | Datei | Format | Fokus |
|---------|-------|--------|-------|
| P1 | `cnc_praezision.csv` | CSV | Pandas, NumPy, Bar Charts, Farbcodierung |
| P2 | - | - | NumPy Random, Histogramme (keine externe Datei) |
| P3 | `werkstoff_pruefung.json` | JSON | JSON-Parsing, Box Plots, Gruppierung |
| P4 | - | - | NumPy Arrays, Log-Log Plots (keine externe Datei) |
| P5 | `produktionslinien_vergleich.xml` | XML | XML-Parsing, Radar Charts, Multi-dimensionale Analyse |

---

## Statistische Zusammenfassung

### CNC-Präzision (`cnc_praezision.csv`)
- Durchschnittliche X-Abweichung: ~5.2 μm
- Durchschnittliche Y-Abweichung: ~5.3 μm
- Durchschnittliche Z-Abweichung: ~5.1 μm
- Beste Maschine: CNC-Bearbeitungszentrum-01 (1.2 μm)
- Schlechteste Maschine: CNC-Drehmaschine-02 (12.1 μm)

### Werkstoff-Prüfung (`werkstoff_pruefung.json`)
- Höchste Zugfestigkeit: 42CrMo4 (1100 MPa)
- Niedrigste Zugfestigkeit: AlMgSi1 (310 MPa)
- Höchste Bruchdehnung: X5CrNi18-10 (45.3%)
- Anzahl Stahl-Proben: 7
- Anzahl Aluminium-Proben: 1

### Produktionslinien (`produktionslinien_vergleich.xml`)
- Höchste Auslastung: Linie-C Lackierung (94.7%)
- Niedrigste Ausschussquote: Linie-C Lackierung (1.8%)
- Kürzeste Rüstzeit: Linie-E Prüfung (25 min)
- Höchster Energieverbrauch: Linie-B Schweißen (125.3 kWh/h)
- Geringste Wartungskosten: Linie-E Prüfung (2100 €/Monat)

---

## Python-Module-Referenzen

Die folgenden neuen Python-Module werden in V14 eingeführt:

- `xml.etree.ElementTree` (Aufgabe P5) - XML-Parsing und Datenextraktion
- `pandas` (Aufgabe P1) - CSV-Datenanalyse
- `json` (Aufgabe P3) - JSON-Datenverarbeitung

**Hinweis**: Alle neuen Module sind in `python_topics.md` dokumentiert.

---

Letzte Aktualisierung: 2024-03-20
