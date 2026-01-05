# Testdaten für V18 - Kryptografie Teil 2 & HTTP-Requests

Dieser Ordner enthält Testdaten für die Python-Aufgaben der Vorlesung V18.

## Übersicht der Dateien

### P2: REST-API für Materialdatenbank
- **material_api_mock.json**: Mock-Daten für Material-API-Response
  - Enthält Werkstoffeigenschaften (S355, AlMg3, 42CrMo4, etc.)
  - Format: JSON mit properties (yield_strength, tensile_strength, youngs_modulus, density, etc.)

### P4: Cloud-API für Produktionsdaten
- **production_api_page1.json**: Erste Seite der Produktionsdaten
- **production_api_page2.json**: Zweite Seite der Produktionsdaten
- **production_api_page3.json**: Dritte Seite der Produktionsdaten
  - Enthält Maschinen-Daten (machine_id, runtime_hours, parts_produced, status)
  - Format: JSON mit pagination-Informationen

### P5: Firmware-Update-System
- **firmware_v2.3.0.bin**: Dummy-Firmware-Datei (500 KB)
- **firmware_v2.3.0_signature.json**: Digitale Signatur für Firmware
  - Enthält SHA-256-Hash, Signatur, CA-Informationen, Datum

## Verwendung

Die Dateien können in den Python-Aufgaben direkt eingelesen werden:

```python
# Beispiel: Material-API Mock laden
import json

with open("testdaten/material_api_mock.json", "r") as f:
    material_data = json.load(f)

print(material_data["S355"]["properties"]["tensile_strength_mpa"])
```

## Maschinenbau-Kontext

Alle Testdaten basieren auf realistischen Szenarien aus dem Maschinenbau:

- **Werkstoffdaten**: Echte Kennwerte aus DIN/ISO-Normen (S355, AlMg3, 42CrMo4)
- **Produktionsdaten**: Typische CNC-Maschinen und Roboter-Auslastung
- **Firmware**: Simuliert Update-System für Industrierobotter

## Dateigröße und Struktur

- Alle JSON-Dateien sind gut formatiert (indent=2) für Lesbarkeit
- Firmware-Datei ist 500 KB groß (realistisch für Embedded Systems)
- SHA-256-Hashes sind korrekt berechnet
