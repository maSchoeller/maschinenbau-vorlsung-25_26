# V15: Netzwerktechnik Grundlagen & Protokolle – Teil 1 – Aufgaben

## Teil A: Theorie-Aufgaben

### Aufgabe 1: OSI-Schichten zuordnen ⭐ (Leicht)

Ordne die folgenden Protokolle und Technologien der **korrekten OSI-Schicht** zu:

1. HTTP
2. Ethernet
3. TCP
4. IP
5. DNS
6. WLAN (IEEE 802.11)
7. TLS/SSL
8. MAC-Adresse
9. Glasfaserkabel
10. SMTP

**Schichten zur Auswahl:**
- Schicht 1: Bitübertragungsschicht (Physical Layer)
- Schicht 2: Sicherungsschicht (Data Link Layer)
- Schicht 3: Vermittlungsschicht (Network Layer)
- Schicht 4: Transportschicht (Transport Layer)
- Schicht 5: Sitzungsschicht (Session Layer)
- Schicht 6: Darstellungsschicht (Presentation Layer)
- Schicht 7: Anwendungsschicht (Application Layer)

**Zusatzfrage:** Erkläre für **zwei** der genannten Protokolle/Technologien, warum sie dieser Schicht zugeordnet sind (jeweils 2-3 Sätze).

---

### Aufgabe 2: IP-Adressen klassifizieren und umrechnen ⭐⭐ (Mittel)

**Teil 1: Klassifikation**

Bestimme für jede der folgenden IPv4-Adressen, ob sie **privat** oder **öffentlich** ist. Wenn privat: Gib den privaten Adressbereich an (z.B. `10.0.0.0/8`).

1. `192.168.50.10`
2. `8.8.8.8`
3. `172.20.15.100`
4. `10.255.255.255`
5. `172.32.0.1`
6. `127.0.0.1`

**Teil 2: Binäre Umrechnung**

Wandle die folgende IPv4-Adresse in ihre **binäre Darstellung** um:

```
IP-Adresse: 192.168.1.100
```

Notation:
```
Dezimal:  192      .  168      .  1        .  100
Binär:    ________ .  ________ .  ________ .  ________
```

**Teil 3: IPv6-Notation**

Kürze die folgende IPv6-Adresse **maximal** (nutze beide Vereinfachungsregeln):

```
Original: 2001:0db8:0000:0000:0000:ff00:0042:8329
Gekürzt:  _______________________________________
```

---

### Aufgabe 3: Subnetting für Produktionsanlagen ⭐⭐⭐ (Schwer)

Ein Maschinenbau-Unternehmen hat das Netzwerk **`172.16.100.0/24`** für seine Produktionshalle zugewiesen bekommen. Die IT-Abteilung soll dieses Netzwerk in **acht gleich große Subnetze** aufteilen, um verschiedene Produktionszellen zu isolieren:

- **Zelle 1**: CNC-Fräsmaschinen (15 Maschinen)
- **Zelle 2**: Drehmaschinen (12 Maschinen)
- **Zelle 3**: Roboterarme (20 Maschinen)
- **Zelle 4**: Qualitätsprüfung (8 Geräte)
- **Zelle 5**: Lagerverwaltung (10 Scanner)
- **Zelle 6**: Montage (18 Arbeitsplätze)
- **Zelle 7**: Wartung (5 Mobile Geräte)
- **Zelle 8**: Management/SCADA (10 Systeme)

**Aufgaben:**

**a) Berechnung der neuen Präfixlänge**
- Wie viele zusätzliche Bits werden für die Subnetz-ID benötigt?
- Wie lautet die neue Präfixlänge (CIDR-Notation)?
- Wie lautet die neue Subnetzmaske in Dezimalschreibweise?

**b) Hosts pro Subnetz**
- Wie viele Bits bleiben für die Host-ID?
- Wie viele **nutzbare** Adressen gibt es pro Subnetz (berücksichtige Netzwerk- und Broadcast-Adresse)?

**c) Subnetz-Bereiche**

Fülle die folgende Tabelle für die **ersten drei** Subnetze aus:

| Subnetz | Produktionszelle | Netzwerkadresse | Erste nutzbare IP | Letzte nutzbare IP | Broadcast-Adresse |
|---------|------------------|-----------------|-------------------|--------------------|-------------------|
| 1 | CNC-Fräsmaschinen | | | | |
| 2 | Drehmaschinen | | | | |
| 3 | Roboterarme | | | | |

**d) Praktische Anwendung**

- Zelle 3 (Roboterarme) benötigt **20 Hosts**. Ist eines der acht Subnetze ausreichend? Begründe deine Antwort.
- Welche Produktionszellen passen **nicht** in ein einzelnes Subnetz und benötigen spezielle Lösungen?

**Bonus (+⭐):** Die SCADA-Systeme benötigen **60 Adressen** für zukünftige Erweiterungen. Kannst du zwei benachbarte Subnetze zu einem größeren zusammenfassen? Wenn ja, wie lautet die neue CIDR-Notation und der nutzbare IP-Bereich?

---

## Teil B: Python-Aufgaben

### Aufgabe P1: Netzwerk-Paket-Analyse ⭐⭐ (Mittel)

**Datei:** `netzwerk_pakete.csv`

In einer Produktionshalle wurden über 5 Minuten industrielle Netzwerkpakete aufgezeichnet. Die CSV-Datei enthält folgende Spalten:

```
Zeitstempel,Quell_IP,Ziel_IP,Protokoll,Port,Paketgroesse_Bytes,Maschine_ID
```

**Aufgabe:**

Schreibe ein Python-Programm, das die CSV-Datei analysiert und folgende Informationen ausgibt:

**a) Protokoll-Verteilung**
- Anzahl der Pakete pro Protokoll (TCP, UDP)
- Prozentuale Verteilung

**b) Port-Analyse**
- Identifiziere die Industrieprotokolle anhand der Ports:
  - Port 502: Modbus TCP
  - Port 1883: MQTT
  - Port 44818: OPC UA
- Zeige Anzahl Pakete pro Industrieprotokoll

**c) Netzwerk-Last**
- Gesamtes übertragenes Datenvolumen in KB
- Durchschnittliche Paketgröße

**d) Maschinen-Kommunikation**
- Top 3 aktivste Maschinen (nach Maschine_ID mit den meisten gesendeten Paketen)
- Liste aller Maschinen-IDs, die mit dem SCADA-Server (192.168.10.200) kommunizieren

**Anforderungen:**
- Nutze `csv.DictReader` für das Einlesen
- Behandle fehlerhafte oder unvollständige Zeilen mit try-except
- Formatiere Ausgaben übersichtlich mit Einheiten

**Erwartete Ausgabe (Beispiel):**
```
=== Netzwerk-Paket-Analyse ===

Protokoll-Verteilung:
  TCP: 70 Pakete (70.0%)
  UDP: 30 Pakete (30.0%)

Industrieprotokolle (nach Port):
  Modbus TCP (502): 50 Pakete
  MQTT (1883): 30 Pakete
  OPC UA (44818): 20 Pakete

Netzwerk-Last:
  Gesamt: 15.5 KB
  Ø Paketgröße: 155 Bytes

Top 3 aktivste Maschinen:
  1. CNC-01: 18 Pakete
  2. CNC-02: 15 Pakete
  3. Robot-01: 12 Pakete

Kommunikation mit SCADA (192.168.10.200):
  Maschinen: CNC-01, CNC-02, Robot-01, Press-01, Sensor-01
```

---

### Aufgabe P2: Maschinenkommunikations-Analyse mit JSON ⭐⭐ (Mittel)

**Datei:** `maschinenkommunikation.json`

Die JSON-Datei enthält Konfigurationsdaten von Produktionsmaschinen in einer Fertigungshalle. Die Struktur umfasst:

```json
{
  "produktionshalle": { "name": "...", "standort": "..." },
  "maschinen": [
    {
      "maschine_id": "CNC-01",
      "typ": "CNC-Drehmaschine",
      "ip_adresse": "192.168.10.100",
      "protokolle": ["Modbus TCP", "OPC UA"],
      "kommunikation": {
        "durchschnittliche_latenz_ms": 12,
        "pakete_pro_sekunde": 45,
        "fehlerrate_prozent": 0.1
      }
    },
    ...
  ]
}
```

**Aufgabe:**

Schreibe ein Python-Programm, das die JSON-Datei mit einem **Generator** verarbeitet und folgende Analysen durchführt:

**a) Generator-Funktion implementieren**

Erstelle eine Generator-Funktion `lies_maschinen(dateiname)`, die:
- Die JSON-Datei einliest
- Über die Liste `maschinen` iteriert
- Jede Maschine als Dictionary zurückgibt (mit `yield`)
- Bei Fehler eine aussagekräftige Fehlermeldung ausgibt

**b) Kommunikationsstatistik**

Berechne für jede Maschine:
- Maschinen-ID und Typ
- Durchschnittliche Latenz
- Paketrate (Pakete pro Sekunde)

**c) Protokoll-Analyse**

- Zähle, wie viele Maschinen welches Protokoll unterstützen
- Zeige die Protokolle mit Anzahl der Maschinen

**d) Performance-Bewertung**

- Identifiziere Maschinen mit Latenz > 15ms (als "langsam")
- Identifiziere Maschinen mit Fehlerrate > 0.15% (als "fehleranfällig")

**Anforderungen:**
- Nutze `json.load()` zum Einlesen
- Verwende `yield` für die Generator-Funktion
- Behandle FileNotFoundError und json.JSONDecodeError
- Formatiere Ausgaben übersichtlich

**Erwartete Ausgabe (Beispiel):**
```
=== Maschinenkommunikations-Analyse ===

Produktionshalle: Fertigungshalle A (Werk Stuttgart)

Maschinen-Übersicht:
  CNC-01 (CNC-Drehmaschine): Latenz 12ms, 45 Pakete/s
  CNC-02 (CNC-Fräsmaschine): Latenz 15ms, 42 Pakete/s
  Robot-01 (Industrieroboter): Latenz 10ms, 58 Pakete/s
  ...

Protokoll-Unterstützung:
  Modbus TCP: 7 Maschinen
  OPC UA: 6 Maschinen
  MQTT: 3 Maschinen
  EtherNet/IP: 2 Maschinen

Performance-Probleme:
  Langsame Maschinen (>15ms): Grinder-01 (22ms), Lathe-01 (20ms)
  Fehleranfällige Maschinen (>0.15%): Grinder-01 (0.30%), Lathe-01 (0.25%)
```

**c) Zeitbasierte Analyse**

Finde Zeiträume mit erhöhter Kommunikation:
- Gruppiere Nachrichten nach Stunden
- Zeige die Top 3 Stunden mit den meisten Nachrichten

**Anforderungen:**
- Nutze `yield` für speicher-effiziente Verarbeitung
- Verwende `json.load()` zum Einlesen
- Behandle FileNotFoundError und json.JSONDecodeError
- Formatiere Ausgaben übersichtlich

**Erwartete Ausgabe (Beispiel):**
```
=== Modbus-Kommunikationsanalyse ===

Slave-Statistiken:
  Slave 1: 45 Nachrichten, häufigster FC: 3, Ø Wert: 2340
  Slave 2: 32 Nachrichten, häufigster FC: 6, Ø Wert: 1850
  Slave 3: 28 Nachrichten, häufigster FC: 3, Ø Wert: 3120

Top 3 Kommunikationsstunden:
  1. 08:00-09:00: 35 Nachrichten
  2. 14:00-15:00: 28 Nachrichten
  3. 10:00-11:00: 22 Nachrichten
```

---

### Aufgabe P3: Sensor-Datenanalyse mit CSV ⭐⭐ (Mittel)

**Datei:** `sensoren_daten.csv`

Eine Produktionsanlage hat mehrere Temperatursensoren installiert, die kontinuierlich Messwerte aufzeichnen. Die CSV-Datei hat folgende Struktur:

```csv
Sensor_ID,Zone,Temperatur_C,Timestamp,Status
S001,Presswerk,245.5,2024-01-15T08:00:00,OK
S002,Presswerk,248.2,2024-01-15T08:00:00,OK
S003,Schweissen,1850.3,2024-01-15T08:00:00,OK
S001,Presswerk,251.7,2024-01-15T08:01:00,Warnung
S004,Lackierung,65.2,2024-01-15T08:01:00,OK
```

**Schreibe ein Programm, das folgende Aufgaben löst:**

**a) Durchschnittstemperatur pro Zone**

Berechne die Durchschnittstemperatur für jede Produktionszone und gib das Ergebnis formatiert aus.

**Erwartete Ausgabe:**
```
Durchschnittstemperaturen nach Zone:
  Presswerk: 248.5°C
  Schweissen: 1850.3°C
  Lackierung: 65.2°C
```

**b) Kritische Messwerte**

Gib alle Sensoren aus, die eine **Warnung** haben oder deren Temperatur außerhalb des Normbereichs liegt (< 0°C oder > 300°C für Presswerk, > 2000°C für Schweißen). Sortiere nach Temperatur (höchste zuerst).

**Erwartete Ausgabe:**
```
Kritische Sensoren:
  1. S001 (Presswerk): 251.7°C - Status: Warnung
  2. S003 (Schweissen): 1850.3°C - Status: OK (Grenzwert)
```

**c) Neue CSV schreiben**

Erstelle eine neue CSV-Datei `presswerk_sensoren.csv`, die nur Sensoren aus dem Presswerk enthält. Füge eine zusätzliche Spalte "Bewertung" hinzu:
- Temperatur ≤ 240°C: "Normal"
- Temperatur ≤ 260°C: "Erhöht"
- Temperatur > 260°C: "Kritisch"

**Anforderungen:**
- Nutze `csv.DictReader` und `csv.DictWriter`
- Behandle fehlende Dateien und ungültige Datenformate
- Runde Durchschnittstemperaturen auf 1 Dezimalstelle
- Verwende `newline=''` beim Schreiben der CSV

---

### Aufgabe P4: OPC UA-Datenverarbeitung mit Iterator-Protokoll ⭐⭐ (Mittel)

**Teil 1: Analyse**

Analysiere den folgenden Code, der OPC UA-Datenpunkte aus einer industriellen Anlage verarbeitet:

```python
class OPCDataStream:
    def __init__(self, xml_file, max_items):
        self.xml_file = xml_file
        self.max_items = max_items
        self.current = 0
        self.data_points = []
        self._load_data()
    
    def _load_data(self):
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.xml_file)
        for node in tree.findall('.//DataPoint'):
            self.data_points.append({
                'node_id': node.get('id'),
                'value': float(node.find('Value').text),
                'quality': node.find('Quality').text
            })
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max_items or self.current >= len(self.data_points):
            raise StopIteration
        data = self.data_points[self.current]
        self.current += 1
        return data

# Verwendung:
opc_stream = OPCDataStream('opc_ua_daten.xml', 10)
```

**Fragen:**
1. Ist `OPCDataStream` ein **Iterable**, ein **Iterator**, oder beides? Begründe.
2. Was gibt `list(opc_stream)` zurück?
3. Was passiert, wenn du danach `list(opc_stream)` ein zweites Mal aufrufst? Warum?
4. Wie müsste die Klasse geändert werden, damit sie **mehrfach** iterierbar ist?
5. Welcher Nachteil besteht beim Laden aller Daten in `_load_data()`? Wie könnte man das mit Generatoren lösen?

**Teil 2: Implementierung**

Schreibe eine **Generator-Funktion** `opc_data_generator(xml_file, max_items, quality_filter="Good")`, die:
- Die XML-Datei `opc_ua_daten.xml` speicher-effizient liest
- Nur Datenpunkte mit der angegebenen Qualität zurückgibt
- Maximal `max_items` Einträge liefert
- Bei ungültigen XML-Strukturen eine Warnung ausgibt und weitermacht

**Anforderungen:**
- Nutze `yield` statt `return`
- Nutze `xml.etree.ElementTree` zum Parsen
- Teste mit verschiedenen `quality_filter` Werten ("Good", "Bad", "Uncertain")

**Erwartete Ausgabe:**
```python
for data in opc_data_generator('opc_ua_daten.xml', max_items=5, quality_filter="Good"):
    print(f"Node {data['node_id']}: {data['value']}")

# Ausgabe:
# Node ns=2;i=1001: 245.8
# Node ns=2;i=1003: 89.2
# Node ns=2;i=1005: 1023.5
# Node ns=2;i=1008: 512.0
# Node ns=2;i=1012: 78.9
```

---

### Aufgabe P5: SCADA-Log-Analyse mit Generator-Pipeline ⭐⭐⭐ (Schwer)

Du erhältst eine große Log-Datei `scada_system.log` von einem SCADA-System (Supervisory Control and Data Acquisition) einer Produktionsanlage:

```
2024-01-15T08:00:15.234 | PLC-001 | INFO | Register 1000 read: 2450 | Response: 12ms
2024-01-15T08:00:16.145 | PLC-002 | INFO | Register 2000 read: 3500 | Response: 8ms
2024-01-15T08:00:17.876 | PLC-001 | WARNING | Register 1000 read: 2650 | Response: 125ms
2024-01-15T08:00:18.234 | PLC-003 | ERROR | Connection timeout | Response: 5000ms
2024-01-15T08:00:19.456 | PLC-002 | INFO | Register 2000 write: 3600 | Response: 15ms
```

**Erstelle ein Programm mit Generator-Pipeline, das folgende Analysen durchführt:**

**a) Generator-Funktionen**

Implementiere die folgenden drei Generator-Funktionen:

1. **`lies_log_zeilen(dateiname)`**: 
   - Liest Log-Datei Zeile für Zeile
   - Gibt jede Zeile als String zurück

2. **`parse_log_zeile(zeilen)`**:
   - Nimmt Generator von Zeilen entgegen
   - Parst jede Zeile und gibt Dictionary zurück mit:
     - `timestamp`: Zeitstempel als String
     - `plc_id`: PLC-Identifier (z.B. "PLC-001")
     - `level`: Log-Level (INFO, WARNING, ERROR)
     - `message`: Nachricht (z.B. "Register 1000 read: 2450")
     - `response_time`: Response-Zeit in ms als Integer
   - Ignoriere ungültige Zeilen (fehlerhafte Struktur)

3. **`filtere_level(log_entries, level)`**:
   - Nimmt Generator von Dictionaries entgegen
   - Gibt nur Einträge mit spezifischem Log-Level zurück

**b) Analyse-Funktionen**

Implementiere folgende Analyse-Funktionen, die die Pipeline nutzen:

1. **`zaehle_log_levels(dateiname)`**:
   - Gibt Dictionary mit Anzahl pro Log-Level zurück
   - Format: `{"INFO": 152, "WARNING": 23, "ERROR": 5}`

2. **`finde_langsame_responses(dateiname, schwellwert_ms=100)`**:
   - Gibt Liste aller Log-Einträge mit Response-Zeit über Schwellwert zurück
   - Sortiert nach Response-Zeit (langsamste zuerst)

3. **`top_plcs(dateiname, n=5)`**:
   - Gibt die Top-N PLCs mit den meisten Log-Einträgen zurück
   - Format: Liste von Tupeln `[(plc_id, anzahl), ...]`

**Anforderungen:**
- **Speicher-Effizienz**: Nutze Generator-Pipeline, nicht `readlines()`
- **Fehlerbehandlung**: Ignoriere ungültige Zeilen, zähle sie aber
- **Performance**: Datei wird nur einmal gelesen pro Analyse
- **Ausgabe**: Formatiere Ergebnisse übersichtlich

**Beispiel-Ausgabe:**
```python
# Log-Level-Verteilung:
level_counts = zaehle_log_levels("scada_system.log")
print("Log-Level-Verteilung:")
for level, count in sorted(level_counts.items()):
    print(f"  {level}: {count}")

# Output:
# Log-Level-Verteilung:
#   INFO: 152
#   WARNING: 23
#   ERROR: 5

# Langsame Responses:
slow_responses = finde_langsame_responses("scada_system.log", schwellwert_ms=100)
print(f"\n{len(slow_responses)} langsame Responses gefunden")

# Top-5 PLCs:
top = top_plcs("scada_system.log", n=5)
print("\nTop-5 aktivste PLCs:")
for i, (plc, count) in enumerate(top, 1):
    print(f"  {i}. {plc}: {count} Log-Einträge")
```

**Bonus (+⭐):** Erweitere die Pipeline um eine Funktion `error_burst_detection(dateiname, zeitfenster_sekunden=60, min_errors=3)`, die Zeiträume mit gehäuften ERROR-Meldungen findet (z.B. 3+ Errors innerhalb von 60 Sekunden).

---

### Aufgabe P6: Produktionsdaten-ETL mit Generator-Pipeline ⭐⭐⭐⭐ (Sehr Schwer)

Du arbeitest für ein Maschinenbau-Unternehmen und erhältst täglich eine große CSV-Datei `produktion_maschinen.csv` mit Produktionsdaten:

```csv
Maschine_ID,Schicht,Produkt_ID,Menge,Ausschuss,Zykluszeit_s,Timestamp,Status
M001,Frueh,P100,250,5,12.5,2024-01-15T06:00:00,completed
M002,Frueh,P101,180,3,18.2,2024-01-15T06:00:00,completed
M001,Frueh,P100,245,8,12.8,2024-01-15T07:00:00,warning
M003,Frueh,P102,320,1,9.5,2024-01-15T07:00:00,completed
M002,Spaet,P101,0,0,0,2024-01-15T14:00:00,malfunction
M001,Spaet,P100,260,4,12.3,2024-01-15T14:00:00,completed
```

**Aufgabe: Erstelle eine speicher-effiziente ETL-Pipeline (Extract, Transform, Load)**

**Teil 1: Extrahieren und Validieren**

Implementiere einen Generator `validiere_produktionsdaten(dateiname)`, der:
- CSV-Datei mit `csv.DictReader` liest
- Jede Produktionszeile validiert:
  - `Maschine_ID`, `Produkt_ID`, `Schicht` müssen vorhanden sein
  - `Menge`, `Ausschuss` müssen nicht-negative Ganzzahlen sein
  - `Zykluszeit_s` muss positive Dezimalzahl sein
  - `Timestamp` muss gültiges Datum sein (Format: ISO 8601)
  - `Status` muss einer der Werte sein: `completed`, `warning`, `malfunction`
- Nur **valide** Produktionsdaten als Dictionary zurückgibt
- **Fehlerhafte** Zeilen in separate Datei `validation_errors.log` schreibt (mit Fehlerbeschreibung)

**Teil 2: Transformieren**

Implementiere einen Generator `transformiere_produktionsdaten(daten)`, der:
- `Timestamp` von String zu `datetime`-Objekt konvertiert
- Neues Feld `Ausschussrate` berechnet: `(Ausschuss / Menge) * 100` in Prozent
- Neues Feld `OEE_Faktor` berechnet: Simplified OEE = `((Menge - Ausschuss) / Menge) * 100`
- Neues Feld `Stunde`, `Datum` aus `Timestamp` extrahiert
- Neues Feld `IstProblematisch` hinzufügt: `True` wenn `Status != "completed"` oder `Ausschussrate > 3%`

**Teil 3: Aggregieren**

Implementiere folgende Analyse-Funktionen:

1. **`produktion_pro_schicht(daten)`**:
   - Berechnet Gesamtproduktion (gute Stücke = Menge - Ausschuss) pro Schicht
   - Gibt Dictionary zurück: `{"Frueh": int, "Spaet": int, "Nacht": int}`

2. **`top_maschinen(daten, n=5)`**:
   - Findet die Top-N produktivsten Maschinen (höchste Gutmenge)
   - Gibt Liste von Tupeln: `[(Maschine_ID, Gutmenge, Durchschnitt_OEE), ...]`

3. **`problem_analyse(daten)`**:
   - Berechnet pro Maschine: Anzahl problematischer Zyklen, durchschnittliche Ausschussrate
   - Gibt Dictionary: `{Maschine_ID: {'probleme': int, 'avg_ausschuss': float}}`

**Teil 4: Laden (Exportieren)**

Implementiere `exportiere_produktionsbericht(input_datei, output_prefix)`, das:
- Die gesamte Pipeline durchläuft
- Drei neue CSV-Dateien erstellt:
  - `{output_prefix}_schicht_uebersicht.csv`: Produktionen pro Schicht
  - `{output_prefix}_top_maschinen.csv`: Beste Maschinen
  - `{output_prefix}_problem_bericht.csv`: Problemanalyse
- Alle Dateien mit `csv.DictWriter` schreibt (mit `newline=''`)

**Anforderungen:**
- **Speicher-Effizienz**: Datei wird nur **einmal** durchgelesen für alle Analysen (nutze `itertools.tee()` falls nötig)
- **Fehlertoleranz**: Einzelne fehlerhafte Zeilen stoppen nicht die gesamte Verarbeitung
- **Genauigkeit**: Nutze `decimal.Decimal` für Prozentsätze und OEE-Berechnungen
- **Performance**: Bei 100.000 Zeilen < 30 Sekunden
- **Logging**: Schreibe Statistiken (Anzahl verarbeitete/fehlerhafte Zeilen, Laufzeit)

**Beispiel-Nutzung:**
```python
exportiere_produktionsbericht("produktion_maschinen.csv", "bericht_2024_01_15")

# Erstellt:
# - bericht_2024_01_15_schicht_uebersicht.csv
# - bericht_2024_01_15_top_maschinen.csv
# - bericht_2024_01_15_problem_bericht.csv
# - validation_errors.log

# Konsolen-Ausgabe:
# Verarbeitung gestartet...
# ✓ 1.543 Produktionszyklen validiert
# ✗ 12 fehlerhafte Zeilen (siehe validation_errors.log)
# ✓ Export abgeschlossen
# Laufzeit: 0.85 Sekunden
# Durchschnittliche OEE: 96.5%
```

**Bonus (+⭐):** Implementiere eine Funktion `echtzeit_monitoring(dateiname, update_intervall_s=5)`, die:
- Die Produktionsdatei kontinuierlich überwacht
- Bei neuen Zeilen automatisch Warnungen ausgibt, wenn:
  - Ausschussrate > 5%
  - Zykluszeit > 20% über Durchschnitt
  - Status = "malfunction"

**Tipp:** Nutze `collections.defaultdict`, `itertools.tee()` und `decimal.Decimal` aus der Standard-Library.

