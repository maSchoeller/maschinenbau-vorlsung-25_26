# V15 - Netzwerktechnik Grundlagen & Protokolle Teil 1: Testdaten

Dieses Verzeichnis enthält **Testdaten für die Python-Übungsaufgaben** in V15. Die Dateien simulieren realistische **industrielle Netzwerk- und Kommunikationsdaten** aus einer Produktionsumgebung.

---

## Übersicht der Testdaten

### 1. **netzwerk_pakete.csv** (CSV-Format)
**Verwendung:** Aufgabe P1 - Netzwerk-Paket-Analyse

**Beschreibung:**
- Netzwerk-Traffic-Log einer Produktionshalle über 5 Minuten
- Enthält 100 Netzwerkpakete von verschiedenen Industriemaschinen
- Kommunikation zwischen Maschinen und SCADA-Server

**Struktur:**
```csv
Zeitstempel,Quell_IP,Ziel_IP,Protokoll,Port,Paketgroesse_Bytes,Maschine_ID
2024-01-15_08:00:12,192.168.10.100,192.168.10.200,TCP,502,156,CNC-01
...
```

**Spalten:**
- `Zeitstempel`: Datum und Uhrzeit des Pakets (Format: YYYY-MM-DD_HH:MM:SS)
- `Quell_IP`: IP-Adresse der sendenden Maschine (192.168.10.x)
- `Ziel_IP`: IP-Adresse des SCADA-Servers (192.168.10.200)
- `Protokoll`: Netzwerkprotokoll (TCP oder UDP)
- `Port`: Zielport (502=Modbus TCP, 1883=MQTT, 44818=OPC UA)
- `Paketgroesse_Bytes`: Größe des Pakets in Bytes (95-234)
- `Maschine_ID`: Eindeutiger Bezeichner der Maschine (CNC-01, Robot-01, etc.)

**Statistiken:**
- Anzahl Datensätze: 100
- Zeitraum: 5 Minuten (08:00:00 - 08:05:00)
- Anzahl verschiedener Maschinen: 10
- Protokolle: Modbus TCP (Port 502), MQTT (Port 1883), OPC UA (Port 44818)
- Durchschnittliche Paketgröße: ~155 Bytes

**Maschinen im Netzwerk:**
- CNC-01, CNC-02: CNC-Drehmaschinen (Modbus TCP)
- Robot-01: Industrieroboter (MQTT, OPC UA)
- Press-01: Hydraulikpresse (Modbus TCP)
- Sensor-01: Vibrationssensor-Cluster (MQTT, OPC UA)
- SCADA-01: SCADA-Server (OPC UA, Modbus TCP)
- Lathe-01: Drehmaschine (Modbus TCP)
- HMI-01: HMI-Panel (OPC UA)
- Mill-01: Fräsmaschine (Modbus TCP)
- Grinder-01: Schleifmaschine (Modbus TCP)

---

### 2. **maschinenkommunikation.json** (JSON-Format)
**Verwendung:** Aufgabe P3 - JSON-basierte Maschinenkommunikations-Analyse

**Beschreibung:**
- Umfassende Konfigurationsdatei für 10 Produktionsmaschinen
- Enthält Maschinendaten, Netzwerkkonfiguration, Betriebsstatus und Kommunikationsmetriken
- Typisch für SCADA/MES-Systeme in der Industrie 4.0

**Struktur:**
```json
{
  "produktionshalle": { ... },
  "maschinen": [
    {
      "maschine_id": "CNC-01",
      "typ": "CNC-Drehmaschine",
      "hersteller": "DMG MORI",
      "ip_adresse": "192.168.10.100",
      "protokolle": ["Modbus TCP", "OPC UA"],
      "status": { ... },
      "kommunikation": { ... }
    },
    ...
  ],
  "netzwerk_statistik": { ... }
}
```

**Hauptelemente:**
- `produktionshalle`: Allgemeine Informationen (Name, Standort, Netzwerksegment)
- `maschinen`: Array mit 10 Maschineneinträgen, jeweils mit:
  - Identifikation (ID, Typ, Hersteller, Modell)
  - Netzwerk (IP, MAC, unterstützte Protokolle)
  - Status (Betriebsstatus, Laufzeit, Wartungsintervalle)
  - Kommunikation (Latenz, Paketrate, Fehlerrate)
- `netzwerk_statistik`: Aggregierte Statistiken über alle Maschinen

**Statistiken:**
- Anzahl Maschinen: 10
- Verschiedene Maschinentypen: 9 (CNC, Roboter, Pressen, Sensoren, etc.)
- Durchschnittliche Latenz: 13.6 ms
- Gesamte Paketrate: 508 Pakete/Sekunde
- Durchschnittliche Fehlerrate: 0.145%

**Protokolle:**
- Modbus TCP: Industriestandard für SPS-Kommunikation
- OPC UA: Plattformunabhängiger Industrie-4.0-Standard
- MQTT: Leichtgewichtiges Publish-Subscribe-Protokoll
- EtherNet/IP: Ethernet-basiertes Industrieprotokoll
- PROFINET: Siemens-Standard für Echtzeit-Ethernet

---

### 3. **opc_ua_daten.xml** (XML-Format)
**Verwendung:** Aufgabe P5 - XML-basierte OPC-UA-Datenstruktur-Analyse

**Beschreibung:**
- XML-Dump einer OPC-UA-Server-Konfiguration
- Enthält Adressraum (Address Space) mit Knoten und Variablen
- Repräsentiert Echtzeit-Prozessdaten von 5 Produktionsmaschinen

**Struktur:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<opc_ua_server>
    <server_info>...</server_info>
    <nodes>
        <node id="ns=2;i=1001">
            <browse_name>CNC_Maschine_01</browse_name>
            <variables>
                <variable id="ns=2;i=1101">
                    <browse_name>Drehzahl</browse_name>
                    <value>2450.5</value>
                    <unit>U/min</unit>
                </variable>
                ...
            </variables>
        </node>
        ...
    </nodes>
    <metadata>...</metadata>
</opc_ua_server>
```

**Hauptelemente:**
- `server_info`: OPC-UA-Server-Metadaten (Name, Vendor, Endpoint)
- `nodes`: 5 Maschinenknoten mit jeweils 5-6 Variablen
- `metadata`: Statistiken (Knotenanzahl, Scan-Rate, letztes Update)

**Enthaltene Maschinen:**
1. **CNC_Maschine_01**: Drehmaschine
   - Variablen: Drehzahl, Vorschub, Spindelleistung, Werkzeugtemperatur, Betriebsstatus
2. **Fraesmaschine_01**: 5-Achs-Fräszentrum
   - Variablen: Spindeldrehzahl, Vorschubgeschwindigkeit, 3D-Achspositionen, Kühlmitteldurchfluss
3. **Roboter_01**: 6-Achs-Industrieroboter
   - Variablen: Achspositionen, Greiferstatus, Bewegungsgeschwindigkeit, Zykluszeit
4. **Hydraulikpresse_01**: 630-Tonnen-Presse
   - Variablen: Pressenkraft, Stößelposition, Hydraulikdruck, Öltemperatur, Hübe/min
5. **Sensor_Cluster_01**: Condition-Monitoring-Sensoren
   - Variablen: 3D-Vibration, Umgebungs-/Lagertemperatur, Alarmstatus

**Statistiken:**
- Anzahl Knoten: 5
- Anzahl Variablen: 27
- Datentypen: Double, String, Boolean
- Access Levels: Read, ReadWrite
- Scan-Rate: 100 ms

**OPC UA Besonderheiten:**
- NodeIDs folgen Standard-Format: `ns=2;i=xxxx`
- Browse Names sind maschinenlesbar
- Display Names sind benutzerfreundlich
- Jede Variable hat Datentyp, Wert, Einheit und Zugriffslevel

---

## Verwendung in den Aufgaben

### **P1: Netzwerk-Paket-Analyse** (CSV)
**Datei:** `netzwerk_pakete.csv`

**Lernziele:**
- CSV-Dateien mit `pandas` einlesen
- Daten nach Protokollen gruppieren
- Netzwerk-Traffic-Statistiken berechnen
- Paketverteilung visualisieren (Balkendiagramm)

**Beispiel-Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt

daten = pd.read_csv('netzwerk_pakete.csv')
protokoll_stats = daten.groupby('Protokoll')['Paketgroesse_Bytes'].agg(['count', 'mean'])
```

---

### **P3: Maschinenkommunikations-Analyse** (JSON)
**Datei:** `maschinenkommunikation.json`

**Lernziele:**
- JSON-Dateien mit `json`-Modul einlesen
- Verschachtelte Datenstrukturen navigieren
- Maschinenstatistiken berechnen
- Latenz-Verteilung visualisieren (Scatter Plot)

**Beispiel-Code:**
```python
import json

with open('maschinenkommunikation.json', 'r', encoding='utf-8') as f:
    daten = json.load(f)

maschinen = daten['maschinen']
latenzen = [m['kommunikation']['durchschnittliche_latenz_ms'] for m in maschinen]
```

---

### **P5: OPC-UA-Datenstruktur-Analyse** (XML)
**Datei:** `opc_ua_daten.xml`

**Lernziele:**
- XML-Dateien mit `xml.etree.ElementTree` parsen
- Hierarchische Datenstrukturen durchlaufen
- Variablenwerte extrahieren und aggregieren
- Maschinenparameter in Tabelle darstellen

**Beispiel-Code:**
```python
import xml.etree.ElementTree as ET

tree = ET.parse('opc_ua_daten.xml')
root = tree.getroot()

for node in root.findall('.//node'):
    maschine = node.find('browse_name').text
    for var in node.findall('.//variable'):
        name = var.find('browse_name').text
        wert = var.find('value').text
```

---

## Hinweise für Studierende

### **Dateiformat-Vergleich**

| Format | Vorteile | Nachteile | Typische Verwendung |
|--------|----------|-----------|---------------------|
| **CSV** | Einfach, kompakt, tabellarisch | Keine Hierarchie, keine Metadaten | Messdaten, Logs, Export |
| **JSON** | Hierarchisch, flexibel, leicht lesbar | Größere Dateien, kein Schema | APIs, Konfiguration, Web |
| **XML** | Hierarchisch, validierbar (Schema), Metadaten | Verbose, komplexer zu parsen | OPC UA, SOAP, Legacy-Systeme |

### **Industrielle Protokolle (Übersicht)**

- **Modbus TCP** (Port 502): Einfaches Master-Slave-Protokoll, weit verbreitet in SPS
- **MQTT** (Port 1883): Publish-Subscribe für IoT, leichtgewichtig
- **OPC UA** (Port 4840/44818): Plattformunabhängig, sicher, Industrie 4.0-Standard
- **EtherNet/IP**: Allen-Bradley (Rockwell), Nord amerika-Standard
- **PROFINET**: Siemens, Europa-Standard, Echtzeit-Ethernet

### **Typische Netzwerkstruktur in der Produktion**

```
[SCADA-Server 192.168.10.200]
         |
    [Switch]
         |
    -------------------------
    |    |    |    |    |   |
  CNC  CNC Robot Press HMI Sensors
  .100 .101 .102  .103 .107  .104
```

---

## Erwartete Ausgaben (Beispiele)

### **P1: Protokoll-Verteilung**
```
Netzwerk-Traffic-Analyse:
  TCP (Modbus/OPC UA): 70 Pakete (Ø 158 Bytes)
  UDP (MQTT): 30 Pakete (Ø 107 Bytes)
  
Top 3 aktivste Maschinen:
  1. SCADA-01: 12 Pakete
  2. CNC-01: 10 Pakete
  3. HMI-01: 8 Pakete
```

### **P3: Latenz-Analyse**
```
Maschinen mit höchster Latenz (> 15 ms):
  - Grinder-01: 22.0 ms (Fehlerrate: 0.30%)
  - Lathe-01: 20.0 ms (Fehlerrate: 0.25%)
  - Press-01: 18.0 ms (Fehlerrate: 0.15%)

Durchschnittliche Netzwerk-Performance:
  Latenz: 13.6 ms
  Paketrate: 508 Pakete/s
  Fehlerrate: 0.145%
```

### **P5: OPC-UA-Variablen-Übersicht**
```
Maschine: CNC_Maschine_01
  Drehzahl: 2450.5 U/min
  Vorschub: 0.25 mm/Umdrehung
  Spindelleistung: 18.7 kW
  Werkzeugtemperatur: 85.2 °C
  Status: Aktiv

Maschine: Hydraulikpresse_01
  Pressenkraft: 450.8 Tonnen
  Hydraulikdruck: 185.5 bar
  ...
```

---

## Technische Hinweise

### **Encoding**
Alle Dateien sind in **UTF-8** encodiert. Beim Einlesen von CSV-Dateien mit Pandas:
```python
df = pd.read_csv('datei.csv', encoding='utf-8')
```

### **Zeitstempel-Parsing**
Das Zeitstempelformat `YYYY-MM-DD_HH:MM:SS` kann mit `pd.to_datetime()` geparst werden:
```python
df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'], format='%Y-%m-%d_%H:%M:%S')
```

### **XML-Namespace-Handling**
Die XML-Datei verwendet Default-Namespaces. Beim Parsen mit ElementTree werden diese automatisch behandelt.

---

## Quellen und Realitätsnähe

Die Testdaten basieren auf:
- **Industriestandards**: Modbus TCP, OPC UA, MQTT
- **Typische Maschinenparameter**: Drehzahlen, Vorschübe, Drücke aus realen CNC-/Roboter-Spezifikationen
- **Realistische Netzwerk-Latenzen**: 5-25 ms für industrielle Ethernet-Netzwerke
- **Übliche Paketgrößen**: 95-234 Bytes für Industrie protokoll-Overhead + Nutzdaten

**Referenzen:**
- OPC Foundation: https://opcfoundation.org/
- Modbus Organization: https://modbus.org/
- MQTT Specification: https://mqtt.org/
- Industrial Ethernet Standards (PROFINET, EtherNet/IP)

---

## Dateigröße und Performance

| Datei | Größe | Datensätze | Ladezeit (ca.) |
|-------|-------|------------|----------------|
| netzwerk_pakete.csv | ~7 KB | 100 | < 0.1 s |
| maschinenkommunikation.json | ~6 KB | 10 Maschinen | < 0.1 s |
| opc_ua_daten.xml | ~11 KB | 5 Knoten, 27 Variablen | < 0.2 s |

Alle Dateien sind klein genug für schnelles Laden und Prototyping.

---

## Lizenz und Nutzung

Diese Testdaten sind **ausschließlich für Bildungszwecke** im Rahmen der Vorlesung vorgesehen. Die Daten sind fiktiv, aber an realen Industrie-Szenarien orientiert.

**Erstellung:** 2024-01-15  
**Letzte Aktualisierung:** 2024-01-15  
**Version:** 1.0
