# Testdaten für V19 – Datenbanken Teil 1

Diese Testdaten dienen zur Bearbeitung der Python-Aufgaben P1-P5 im Rahmen der Vorlesung V19 (Datenbanken & SQL).

---

## 📂 Übersicht

### P1: Temperatur-Monitoring-System

**Datei: `temperaturmessungen.csv`**
- **Format**: CSV mit Header (Kuehlschrank_ID, Zeitstempel, Temperatur_Celsius)
- **Inhalt**: 48 Temperaturmessungen für 3 Kühlschränke (Kühlraum A1, Gefrierschrank B2, Kühlzelle C3)
- **Zeitraum**: 15.-16. März 2024, alle 15-30 Minuten
- **Besonderheiten**: 
  - Kühlraum A1: Überhitzung zwischen 10:00 und 11:30 Uhr (7.2°C bei Soll 4°C ±1.5°C)
  - Gefrierschrank B2: Zu warm um 09:30 Uhr (-13.5°C bei Soll -18°C ±3.0°C)
  - Kühlzelle C3: Überschreitung um 10:00 Uhr (4.5°C bei Soll 2°C ±1.0°C)
- **Verwendung**: Import der Messwerte und Berechnung des Alarm-Flags

---

### P2: Werkstoff-Prüfdatenbank

#### `werkstoffe.csv`
- **Format**: CSV mit Header (Werkstoff_ID, Bezeichnung, Werkstoffnummer, Dichte_g_cm3, E_Modul_GPa)
- **Inhalt**: 5 Werkstoffe (S235JR, C45, AlMg3, X5CrNi18-10, GGG-40)
- **Verwendung**: Basis-Tabelle für Material-Informationen

#### `proben.csv`
- **Format**: CSV mit Header (Proben_ID, Werkstoff_ID, Probendurchmesser_mm, Probenlaenge_mm, Herstellungsdatum)
- **Inhalt**: 20 Proben verschiedener Werkstoffe
- **Besonderheiten**: Alle Proben haben Standard-Abmessungen (Ø 10 mm, Länge 100 mm)
- **Verwendung**: Verknüpfung zwischen Werkstoffen und Zugversuchen

#### `zugversuche.csv`
- **Format**: CSV mit Header (Versuchs_ID, Proben_ID, Versuchsdatum, Streckgrenze_MPa, Zugfestigkeit_MPa, Bruchdehnung_Prozent, Pruefgeraet)
- **Inhalt**: 30 Zugversuche auf 2 Prüfgeräten (Zwick_Z100, Instron_5985)
- **Zeitraum**: Februar 2024
- **Besonderheiten**: 
  - Mehrere Messungen pro Probe (Reproduzierbarkeit)
  - Realistische Materialwerte:
    - S235JR: Streckgrenze ~245 MPa, Zugfestigkeit ~382 MPa
    - C45: Streckgrenze ~382 MPa, Zugfestigkeit ~625 MPa
    - AlMg3: Streckgrenze ~60 MPa, Zugfestigkeit ~127 MPa
    - Edelstahl X5CrNi18-10: Streckgrenze ~216 MPa, Zugfestigkeit ~522 MPa
    - GGG-40: Streckgrenze ~286 MPa, Zugfestigkeit ~403 MPa
- **Verwendung**: JOIN-Queries, Aggregationen, Ausreißer-Detektion

---

### P3: Fertigungsauftragsverwaltung

**Datei: `materialbestand.json`**
- **Format**: JSON-Array mit Material-Objekten
- **Inhalt**: 8 Materialien mit aktuellen Lagerbeständen und Mindestbeständen
- **Besonderheiten**: 
  - 3 Materialien unter Mindestbestand (PA6 Platten, Kupfer-Rohr, Carbon-Faser Gewebe)
  - Realistische Bestandsmengen in kg
- **Verwendung**: Initialdata für Materialbestand-Tabelle, Transaktionsszenario (Buchung/Rollback)

---

### P4: Sensor-Datenbank mit Zeitreihen-Analyse

#### `sensoren.csv`
- **Format**: CSV mit Header (Sensor_ID, Sensorname, Maschinen_ID, Sensor_Typ, Einheit)
- **Inhalt**: 10 Sensoren (3× Temperatur, 2× Drehzahl, 3× Vibration, 2× Druck)
- **Besonderheiten**: Sensoren sind verschiedenen Maschinen zugeordnet (ID 101-105)
- **Verwendung**: Metadaten für Sensormessungen

#### `sensormesswerte.csv`
- **Format**: CSV mit Header (Messwert_ID, Sensor_ID, Zeitstempel, Wert)
- **Inhalt**: 40 Messwerte (gekürzt für Demonstrationszwecke; reale Anwendung hätte 1000+ Zeilen)
- **Zeitraum**: 15. März 2024, 00:00-02:15 Uhr, alle 15 Minuten
- **Besonderheiten**:
  - TEMP_01: Temperaturanstieg von 68.5°C auf 80.2°C
  - DREHZAHL_01: Drehzahl mit Anomalien (1595.3 und 1380.5 U/min bei Ø 1485 U/min)
  - VIBRATION_01: Leichte Schwankungen zwischen 2.8 und 3.3 mm/s
  - DRUCK_01: Stabiler Druck um 6.0 bar
- **Verwendung**: pandas DataFrame-Export, Zeitreihen-Plot, gleitender Durchschnitt, Anomalie-Detektion

---

### P5: Produktionsplanungs-Tool

#### `produkte.csv`
- **Format**: CSV mit Header (Produkt_ID, Produktname, Produktionszeit_Minuten, Material_pro_Stueck_kg)
- **Inhalt**: 6 Produkte mit unterschiedlichen Produktionszeiten (8-45 Minuten) und Materialbedarfen
- **Verwendung**: Basis-Tabelle für Produktionsinformationen

#### `produktionsauftraege.json`
- **Format**: JSON-Array mit Auftrags-Objekten
- **Inhalt**: 15 Produktionsaufträge in verschiedenen Status
  - 5× IN_ARBEIT
  - 8× GEPLANT
  - 2× ABGESCHLOSSEN
- **Besonderheiten**: 
  - Verschiedene Prioritäten (1-8, niedrigste Zahl = höchste Priorität)
  - Zieltermine März-April 2024
  - Realistische Stückzahlen (80-5000 Stück)
- **Verwendung**: Produktionsplan-Report, Materialbedarfsrechnung

#### `maschinenbelegung.xml`
- **Format**: XML mit Wurzelelement `<maschinenbelegungen>` und Kind-Elementen `<belegung>`
- **Inhalt**: 25 Maschinenbelegungen für verschiedene Aufträge
- **Besonderheiten**: 
  - Mehrere Maschinen pro Auftrag (z.B. Auftrag 101 auf Maschinen 5, 7)
  - Realistische Schichtzeiten (08:00-18:30 Uhr)
  - Tatsächliche Stückzahlen (teilweise 0 für laufende Belegungen)
  - Verschiedene Maschinen (ID 1-9)
- **Verwendung**: JOIN mit Produktionsaufträgen, Auslastungs-Analyse, Fortschrittsberechnung

---

## 🔧 Technische Hinweise

### CSV-Dateien
- **Encoding**: UTF-8
- **Separator**: Komma (`,`)
- **Header**: Erste Zeile enthält Spaltennamen
- **Import**: `import csv` → `csv.reader()` oder `csv.DictReader()`

### JSON-Dateien
- **Encoding**: UTF-8
- **Format**: JSON-Array mit Objekten
- **Import**: `import json` → `json.load(datei)`
- **Besonderheit**: Keine Trailing-Commas

### XML-Dateien
- **Encoding**: UTF-8
- **Root-Element**: Unterschiedlich je nach Datei (`<maschinenbelegungen>`)
- **Import**: `import xml.etree.ElementTree as ET` → `ET.parse(datei)`
- **Besonderheit**: Numerische Werte als Text gespeichert (muss mit `int()` / `float()` konvertiert werden)

### Zeitstempel
- **Format**: ISO 8601 (`YYYY-MM-DDTHH:MM:SS`)
- **Zeitzone**: Keine Angabe (implizit lokale Zeit)
- **Python-Konvertierung**: `datetime.datetime.fromisoformat(zeitstempel)`

---

## 📊 Datenqualität

Alle Testdaten sind:
- **Realistisch**: Basieren auf tatsächlichen Materialwerten, Betriebszeiten, Produktionsabläufen
- **Konsistent**: Fremdschlüssel-Beziehungen sind korrekt (kein Orphan)
- **Variabel**: Enthalten normale Werte und Anomalien für interessante Analysen
- **Maschinenbau-fokussiert**: Temperaturüberwachung, Werkstoffprüfung, Produktionsplanung

---

## 🛠 Verwendungsbeispiele

### CSV mit `csv.DictReader()`
```python
import csv

with open('testdaten/werkstoffe.csv', 'r', encoding='utf-8') as datei:
    reader = csv.DictReader(datei)
    for zeile in reader:
        print(zeile['Bezeichnung'], zeile['Werkstoffnummer'])
```

### JSON laden
```python
import json

with open('testdaten/materialbestand.json', 'r', encoding='utf-8') as datei:
    materialien = json.load(datei)
    for material in materialien:
        print(material['Bezeichnung'], material['Lagerbestand_kg'])
```

### XML parsen
```python
import xml.etree.ElementTree as ET

tree = ET.parse('testdaten/maschinenbelegung.xml')
root = tree.getroot()

for belegung in root.findall('belegung'):
    auftrag_id = belegung.find('Auftrag_ID').text
    maschine_id = belegung.find('Maschinen_ID').text
    stueckzahl = int(belegung.find('Tatsaechliche_Stueckzahl').text)
    print(f"Auftrag {auftrag_id} auf Maschine {maschine_id}: {stueckzahl} Stk")
```

---

## ⚠️ Hinweise zur Verwendung

1. **Pfade**: Alle Python-Skripte sollten im Ordner `V19-Datenbanken-Teil1/` liegen. Testdaten befinden sich in `testdaten/` (relativer Pfad: `testdaten/dateiname.csv`).

2. **Encoding**: Beim Öffnen von Dateien **immer** `encoding='utf-8'` angeben (insbesondere unter Windows):
   ```python
   with open('testdaten/werkstoffe.csv', 'r', encoding='utf-8') as datei:
       ...
   ```

3. **CSV newline-Parameter**: Beim Schreiben von CSV-Dateien unter Windows `newline=''` verwenden:
   ```python
   with open('output.csv', 'w', newline='', encoding='utf-8') as datei:
       writer = csv.writer(datei)
       ...
   ```

4. **Datei-Existenz prüfen**: Vor Import prüfen, ob Datei existiert:
   ```python
   import os
   if not os.path.exists('testdaten/werkstoffe.csv'):
       print("Fehler: Datei nicht gefunden!")
   ```

5. **SQLite Transaktionen**: Bei Fehlern immer `conn.rollback()` aufrufen:
   ```python
   try:
       cursor.execute("INSERT INTO ...")
       conn.commit()
   except Exception as e:
       conn.rollback()
       print(f"Fehler: {e}")
   ```
