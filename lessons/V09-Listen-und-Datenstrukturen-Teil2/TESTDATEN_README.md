# Testdaten für V09 - Listen und Datenstrukturen Teil 2

Diese Dateien enthalten Testdaten für die Python-Aufgaben in V09.

## Verfügbare Testdaten

### 1. `maschine_01.log`
**Verwendet in**: Aufgabe P2 - Maschinen-Logfile-Analyse mit Fehlerbehandlung

**Beschreibung**: Realistisches CNC-Maschinen-Logfile mit verschiedenen Event-Typen (INFO, WARNING, ALARM, ERROR). Das Logfile dokumentiert eine typische Produktionsschicht einer CNC-Drehmaschine.

**Statistiken**:
- Gesamtzeilen: 54
- ALARM-Einträge: 4
- ERROR-Einträge: 2
- Zeitraum: 08:00 - 09:00 Uhr (1 Stunde Betrieb)

**Verwendung**:
```python
stats = analyse_maschinenlog("maschine_01.log")
print(stats)
# Output: {'zeilen': 54, 'alarme': 4, 'errors': 2}
```

### 2. `fertigungszelle_01.json`
**Verwendet in**: Aufgabe P5 - Robustes Maschinen-Konfigurationssystem

**Beschreibung**: JSON-Konfigurationsdatei für eine Fertigungszelle mit CNC-Drehmaschine. Enthält umfassende Maschinenkonfiguration mit Parametern für Maschine, Qualitätssicherung, Prozess, Netzwerk, Wartung und Produktion.

**Struktur**:
- `maschine`: Maschinenspezifikationen (Typ, ID, Achsen, Werkzeugmagazin)
- `qualitaet`: QS-Parameter (Toleranzen, Prüfintervalle, Messmittel)
- `prozess`: Prozessparameter (Kühlmittel, Spindel, Vorschub)
- `netzwerk`: Netzwerkkonfiguration (IP, Ports, Protokolle)
- `wartung`: Wartungsinformationen (Intervalle, Kontakte)
- `produktion`: Produktionsparameter (Schichtzeiten, Taktzeit)

**Verwendung**:
```python
config = FertigungszellenKonfiguration(
    "fertigungszelle_01.json",
    erforderliche_felder=["maschine", "qualitaet"]
)
config.laden()
print(config.get("maschine")["typ"])
# Output: CNC-Drehmaschine
```

## Hinweise für Studierende

- Die Testdaten sind so gestaltet, dass sie realistische Maschinenbau-Szenarien abbilden
- Die Dateien können für Tests der eigenen Implementierungen verwendet werden
- Bei Bedarf können die Dateien angepasst oder erweitert werden
- Achten Sie auf die korrekte Pfadangabe beim Öffnen der Dateien (relativer oder absoluter Pfad)

## Technische Details

### maschine_01.log
- **Format**: Text (UTF-8)
- **Größe**: ~3.4 KB
- **Struktur**: `YYYY-MM-DD HH:MM:SS | LEVEL | Nachricht`
- **Event-Level**: INFO, WARNING, ALARM, ERROR

### fertigungszelle_01.json
- **Format**: JSON (UTF-8)
- **Größe**: ~1.7 KB
- **Verschachtelung**: Bis zu 3 Ebenen
- **Validierung**: Gültiges JSON-Format nach RFC 8259

## Fehlersimulation

Für erweiterte Tests können folgende Szenarien simuliert werden:

1. **Datei nicht gefunden**: Verwende nicht-existierenden Dateinamen
2. **Ungültiges JSON**: Erstelle eine Kopie von `fertigungszelle_01.json` und füge Syntaxfehler ein
3. **Keine Leseberechtigung**: Ändere die Dateiberechtigungen (nur Unix/Linux)

## Erstellung eigener Testdaten

Studierende können eigene Testdaten erstellen, um verschiedene Szenarien zu testen:

**Beispiel für minimales Logfile**:
```
2026-01-04 10:00:00 | INFO | Start
2026-01-04 10:05:00 | ALARM | Überhitzung
2026-01-04 10:10:00 | INFO | Ende
```

**Beispiel für minimale JSON-Konfiguration**:
```json
{
  "maschine": {
    "id": "TEST-01",
    "typ": "Testmaschine"
  },
  "qualitaet": {
    "toleranz": 0.05
  }
}
```
