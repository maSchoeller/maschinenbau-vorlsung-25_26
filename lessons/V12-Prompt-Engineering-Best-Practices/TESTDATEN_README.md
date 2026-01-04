# Testdaten für V12 - Prompt Engineering Best Practices

Diese Datei dokumentiert die bereitgestellten Testdaten für die Aufgaben in Vorlesung V12.

---

## Datei: `produktionsdaten_test.csv`

**Verwendung**: Aufgabe P4 - Produktionsdaten-Verarbeitung mit relativen/absoluten Imports

**Beschreibung**: Diese CSV-Datei enthält realistische Produktionsdaten einer CNC-Fertigungszelle über einen kompletten Arbeitstag (08:00-17:00 Uhr). Die Daten wurden so gewählt, dass sie typische Produktionsszenarien widerspiegeln, einschließlich Schwankungen in der Stückzahl und variierender Ausschussraten.

**Format**: CSV (Comma-Separated Values) mit Header-Zeile

**Struktur**:
```
Zeit,Stueckzahl,Ausschuss
HH:MM,<int>,<int>
```

**Spalten**:
- **Zeit**: Zeitstempel im Format HH:MM (volle Stunden von 08:00 bis 17:00)
- **Stueckzahl**: Anzahl produzierter Bauteile in dieser Stunde (integer)
- **Ausschuss**: Anzahl fehlerhafter Bauteile in dieser Stunde (integer)

**Datensatz-Eigenschaften**:
- **Anzahl Zeilen**: 10 Datensätze (plus 1 Header)
- **Zeitraum**: 08:00-17:00 Uhr (9 Stunden Produktion + 1 Stunde Pause um 12:00)
- **Gesamtproduktion**: 2.511 Stück
- **Gesamtausschuss**: 105 Stück
- **Durchschnittliche Ausschussquote**: ~4,2%

**Typische Produktionsmerkmale**:
1. **Anlaufphase** (08:00-09:00): Niedrigere Stückzahlen zu Schichtbeginn
2. **Optimale Phase** (09:00-11:00, 13:00-15:00): Höchste Produktivität
3. **Mittagspause** (12:00): Reduzierte Produktion
4. **Schichtende** (16:00-17:00): Leicht sinkende Produktivität
5. **Ausschussschwankungen**: Realistisch zwischen 6-15 Stück/Stunde (2,5-5,8% Quote)

**Verwendung in der Aufgabe**:

Die Studierenden sollen:
1. Diese CSV-Datei mit `io/reader.py` einlesen
2. Ausschussquote pro Stunde mit `analyse/qualitaet.py` berechnen
3. OEE (Overall Equipment Effectiveness) mit `analyse/oee.py` berechnen
4. Einen Bericht mit `io/writer.py` generieren

**Beispiel-Berechnungen**:

```python
# Stunde 08:00
Stückzahl: 245
Ausschuss: 12
Ausschussquote: (12/245) × 100 = 4,90%
Qualitätsrate: 100% - 4,90% = 95,10%

# Gesamt (alle Stunden)
Gesamt-Stückzahl: 2.511
Gesamt-Ausschuss: 105
Gesamt-Ausschussquote: (105/2.511) × 100 = 4,18%
```

**Hinweise für Studierende**:

1. Die Datei liegt im gleichen Verzeichnis wie die Aufgabe
2. Der Dateipfad kann relativ angegeben werden: `"produktionsdaten_test.csv"`
3. Das CSV-Format ist einfach gehalten - keine Anführungszeichen, keine Leerzeichen
4. Jede Zeile (außer Header) kann mit `split(',')` verarbeitet werden
5. Werte müssen von String zu int konvertiert werden: `int(wert)`

**Erweiterungsmöglichkeiten**:

Falls Studierende eigene Testdaten erstellen möchten, sollten sie beachten:
- Stückzahlen realistisch halten (50-300 pro Stunde für CNC-Fertigung)
- Ausschussquote typischerweise 1-10% (höhere Werte deuten auf Probleme hin)
- Zeitangaben im Format HH:MM
- CSV-Format ohne zusätzliche Zeichen beibehalten

---

## Statistiken

| Datei | Größe | Zeilen | Format |
|-------|-------|--------|--------|
| produktionsdaten_test.csv | 152 Bytes | 11 (10 Daten + 1 Header) | CSV |

**Gesamt**: 1 Testdatei

---

## Nutzung

Stelle sicher, dass die Testdatei im gleichen Verzeichnis liegt wie dein Python-Code oder passe den Pfad entsprechend an:

```python
from produktionsdaten.io.reader import lese_produktionsdaten

# Relativer Pfad (wenn main.py im gleichen Verzeichnis wie CSV liegt)
daten = lese_produktionsdaten("produktionsdaten_test.csv")

# Oder absoluter Pfad
import os
pfad = os.path.join(os.path.dirname(__file__), "produktionsdaten_test.csv")
daten = lese_produktionsdaten(pfad)
```

---

**Erstellt für**: Vorlesung V12 - Prompt Engineering Best Practices  
**Zielgruppe**: Maschinenbau-Studierende (1.-2. Semester Informatik)  
**Letzte Aktualisierung**: 2026-01-04
