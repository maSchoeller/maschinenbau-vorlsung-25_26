# V16 - Testdaten für Pandas-Übungen

Dieser Ordner enthält Testdaten-Dateien für die Python-Pandas-Übungen in V16 (Netzwerktechnik Grundlagen & Protokolle – Teil 2).

---

## Übersicht der Testdaten-Dateien

| Datei | Format | Größe | Datensätze | Verwendung |
|-------|--------|-------|------------|------------|
| `sensoren_daten.csv` | CSV | ~1.3 KB | 15 | P1, P2 - Sensor-Datenanalyse |
| `wartungsauftraege.json` | JSON | ~4.3 KB | 10 | P3 - Wartungsmanagement-Analyse |
| `produktionsplanung.xml` | XML | ~3.9 KB | 6 | P5 - Produktionsplanung-Dashboard |
| `produkte_katalog.csv` | CSV | ~0.7 KB | 10 | P4 - Performance-Optimierung |

---

## 1. sensoren_daten.csv

**Beschreibung**: Industrielle Sensor-Messdaten von 15 Sensoren aus verschiedenen Produktionslinien.

**Struktur**:
```csv
Sensor_ID,Sensor_Name,Typ,Position,Temperatur_C,Vibration_mm_s,Druck_bar,Letztwartung,Status
S001,Temp-Sensor-01,Temperatur,Linie_A_Spindel,78.5,0.15,5.2,2024-11-15,Aktiv
...
```

**Spalten**:
- `Sensor_ID`: Eindeutige Sensor-ID (String)
- `Sensor_Name`: Bezeichnung des Sensors (String)
- `Typ`: Sensortyp (Temperatur/Vibration/Druck)
- `Position`: Einbauort in der Produktionslinie (String)
- `Temperatur_C`: Gemessene Temperatur in °C (float)
- `Vibration_mm_s`: Vibrationsamplitude in mm/s (float)
- `Druck_bar`: Druckmesswert in bar (float)
- `Letztwartung`: Datum der letzten Wartung (YYYY-MM-DD)
- `Status`: Betriebsstatus (Aktiv/Warnung/Kritisch)

**Statistiken**:
- Gesamt: 15 Sensoren
- Typen: 5 Temperatur, 5 Vibration, 5 Druck
- Status: 9 Aktiv, 3 Warnung, 3 Kritisch
- Temperaturen: 19.5°C - 105.2°C
- Vibrationen: 0.06 - 5.92 mm/s
- Druck: 4.7 - 165.8 bar

**Verwendung**:
```python
import pandas as pd
df = pd.read_csv('sensoren_daten.csv')
```

---

## 2. wartungsauftraege.json

**Beschreibung**: Wartungsaufträge für verschiedene Produktionsmaschinen mit Details zu Typ, Priorität, Kosten und Status.

**Struktur**:
```json
{
  "wartungsauftraege": [
    {
      "auftrag_id": "W2024-001",
      "maschine_id": "CNC-A-001",
      "maschine_name": "CNC Fräsmaschine DMC 80 U",
      "typ": "Präventiv",
      "prioritaet": "Mittel",
      "geplantes_datum": "2024-12-15",
      "dauer_stunden": 4.5,
      "techniker": "Schmidt, M.",
      "kosten_euro": 580.00,
      "komponenten": ["Spindellager", "Kühlsystem", "Schmierung"],
      "status": "Geplant"
    },
    ...
  ]
}
```

**Felder**:
- `auftrag_id`: Eindeutige Auftrags-ID (String)
- `maschine_id`: Maschinen-ID (String)
- `maschine_name`: Vollständiger Maschinenname (String)
- `typ`: Wartungstyp (Präventiv/Störung/Inspektion)
- `prioritaet`: Dringlichkeit (Niedrig/Mittel/Hoch/Kritisch)
- `geplantes_datum`: Geplantes Wartungsdatum (YYYY-MM-DD)
- `dauer_stunden`: Geschätzte Dauer in Stunden (float)
- `techniker`: Zuständiger Techniker (String)
- `kosten_euro`: Geschätzte Kosten in Euro (float)
- `komponenten`: Liste der zu wartenden Komponenten (Array)
- `status`: Aktueller Status (Geplant/In Bearbeitung/Abgeschlossen)

**Statistiken**:
- Gesamt: 10 Wartungsaufträge
- Typen: 4 Präventiv, 3 Störung, 3 Inspektion
- Prioritäten: 2 Niedrig, 4 Mittel, 2 Hoch, 2 Kritisch
- Status: 6 Geplant, 2 In Bearbeitung, 2 Abgeschlossen
- Durchschn. Dauer: 4.4 Stunden
- Durchschn. Kosten: 690 Euro
- Gesamtkosten: 6.905 Euro

**Verwendung**:
```python
import pandas as pd
import json

with open('wartungsauftraege.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
df = pd.DataFrame(data['wartungsauftraege'])
```

---

## 3. produktionsplanung.xml

**Beschreibung**: Produktionsplanungsdaten für eine Woche (KW 50/2024) mit Aufträgen auf 3 Produktionslinien.

**Struktur**:
```xml
<produktionsplanung>
  <woche datum="2024-12-09_bis_2024-12-15">
    <produktionslinie id="Linie_A" name="CNC-Fertigung Linie A">
      <auftrag auftrag_id="A-2024-1201">
        <bezeichnung>Gehäusefertigung Serie X1</bezeichnung>
        <stueckzahl_geplant>150</stueckzahl_geplant>
        <stueckzahl_produziert>148</stueckzahl_produziert>
        <ausschuss>2</ausschuss>
        <zykluszeit_minuten>12.5</zykluszeit_minuten>
        ...
      </auftrag>
    </produktionslinie>
  </woche>
</produktionsplanung>
```

**Felder (pro Auftrag)**:
- `auftrag_id`: Eindeutige Auftrags-ID
- `bezeichnung`: Produktbezeichnung
- `stueckzahl_geplant`: Geplante Stückzahl
- `stueckzahl_produziert`: Tatsächlich produzierte Stückzahl
- `ausschuss`: Ausschussteile
- `zykluszeit_minuten`: Durchschnittliche Zykluszeit
- `prioritaet`: Auftragspriorität (Niedrig/Mittel/Hoch/Kritisch)
- `material`: Verwendetes Material
- `werkzeugkosten_euro`: Werkzeugkosten
- `start_datum` / `end_datum`: Zeitraum
- `status`: Auftragsstatus

**Statistiken**:
- 3 Produktionslinien
- 6 Produktionsaufträge
- Geplante Produktion: 1.350 Stück
- Produziert: 1.197 Stück (88.7%)
- Ausschuss: 29 Stück (2.4%)
- Status: 3 Abgeschlossen, 2 In Bearbeitung, 1 Geplant
- Gesamtwerkzeugkosten: 2.434,15 Euro

**Verwendung**:
```python
import pandas as pd
import xml.etree.ElementTree as ET

tree = ET.parse('produktionsplanung.xml')
root = tree.getroot()
```

---

## 4. produkte_katalog.csv

**Beschreibung**: Katalog von 10 mechanischen Komponenten mit Preisen, Bestellmengen und Lieferzeiten.

**Struktur**:
```csv
Produkt_ID,Bezeichnung,Kategorie,Preis_Euro,Bestellmenge,Lieferzeit_Tage,Gewicht_kg,Qualitaetsstufe
1,Linearführung LM20,Führungssysteme,125.50,50,7,2.8,A
...
```

**Spalten**:
- `Produkt_ID`: Eindeutige Produkt-ID (int)
- `Bezeichnung`: Produktname (String)
- `Kategorie`: Produktkategorie (String)
- `Preis_Euro`: Stückpreis in Euro (float)
- `Bestellmenge`: Verfügbare Menge (int)
- `Lieferzeit_Tage`: Lieferzeit in Tagen (int)
- `Gewicht_kg`: Gewicht in kg (float)
- `Qualitaetsstufe`: Qualitätsstufe (A/B)

**Verwendung** (für P4 Performance-Optimierung):
```python
import pandas as pd
df = pd.read_csv('produkte_katalog.csv')
```

---

## Hinweise für Studierende

1. **Dateipfade**: Stelle sicher, dass die CSV/JSON/XML-Dateien im gleichen Verzeichnis wie dein Python-Script liegen.

2. **Encoding**: Alle Dateien sind in UTF-8 kodiert. Bei Umlauten (ä, ö, ü) verwende:
   ```python
   df = pd.read_csv('datei.csv', encoding='utf-8')
   ```

3. **Datum-Konvertierung**: Konvertiere Datumsspalten zu datetime:
   ```python
   df['Letztwartung'] = pd.to_datetime(df['Letztwartung'])
   ```

4. **JSON-Import**: Für verschachtelte JSON-Strukturen:
   ```python
   import json
   with open('datei.json', 'r', encoding='utf-8') as f:
       data = json.load(f)
   df = pd.DataFrame(data['key'])
   ```

5. **XML-Parsing**: Für XML-Daten verwende xml.etree.ElementTree:
   ```python
   import xml.etree.ElementTree as ET
   tree = ET.parse('datei.xml')
   root = tree.getroot()
   ```

---

## Erweiterungsmöglichkeiten

- **Mehr Sensoren**: Füge zusätzliche Sensoren mit verschiedenen Status hinzu
- **Zeitreihen**: Erweitere sensoren_daten.csv mit mehreren Zeitstempeln pro Sensor
- **Weitere Maschinen**: Ergänze wartungsauftraege.json mit mehr Maschinentypen
- **Mehrzeilige Auswertung**: Kombiniere Daten aus mehreren Dateien für Cross-Analysen

---

**Letzte Aktualisierung**: 2024-12-04  
**Kontakt**: Bei Fragen zu den Testdaten wende dich an die Übungsleitung.
