# Testdaten für V20: Datenbanken – Teil 2

Dieser Ordner enthält alle Testdaten für die Python-Aufgaben P1-P5.

---

## 📊 Datenbankstruktur: `produktionsdb.db`

Die SQLite-Datenbank `produktionsdb.db` enthält Tabellen für ein Produktionsmanagement-System in der Maschinenbau-Branche.

### Tabellen-Schema

#### 1. `Maschinen`
Speichert Informationen über Produktionsmaschinen.

```sql
CREATE TABLE Maschinen (
    Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE,
    Typ TEXT NOT NULL,  -- 'Fräse', 'Drehbank', 'Roboter', 'Presse'
    Baujahr INTEGER NOT NULL CHECK(Baujahr >= 1980 AND Baujahr <= 2024),
    Betriebsstunden INTEGER DEFAULT 0,
    Status TEXT CHECK(Status IN ('Bereit', 'Produktion', 'Wartung', 'Defekt')) DEFAULT 'Bereit',
    Aktiv INTEGER DEFAULT 1  -- 1 = aktiv, 0 = stillgelegt
);
```

**Beispieldaten**: 15 Maschinen (5 Fräsen, 5 Drehbänke, 3 Roboter, 2 Pressen)

---

#### 2. `Wartungen`
Protokolliert Wartungsarbeiten an Maschinen.

```sql
CREATE TABLE Wartungen (
    Wartung_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Wartungstyp TEXT NOT NULL,  -- 'Inspektion', 'Reparatur', 'Ölwechsel', 'Kalibrierung'
    Datum TEXT NOT NULL,  -- Format: YYYY-MM-DD
    Kosten REAL NOT NULL CHECK(Kosten >= 0),
    Techniker TEXT,
    Beschreibung TEXT,
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID) ON DELETE CASCADE
);
```

**Beispieldaten**: 80 Wartungen über 2023-2024, verschiedene Typen und Kosten (50€ - 5000€)

---

#### 3. `Materialbestand`
Verwaltet Lagerbestände von Rohmaterialien.

```sql
CREATE TABLE Materialbestand (
    Material_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Materialname TEXT NOT NULL UNIQUE,
    Menge_Lager REAL NOT NULL CHECK(Menge_Lager >= 0),
    Einheit TEXT NOT NULL,  -- 'kg', 'Stück', 'm', 'Liter'
    Mindestbestand REAL NOT NULL,
    Preis_Pro_Einheit REAL NOT NULL
);
```

**Beispieldaten**: 10 Materialien (Stahl, Aluminium, Schrauben, Öl, etc.)

---

#### 4. `Produktionslaeufe`
Dokumentiert Fertigungsaufträge.

```sql
CREATE TABLE Produktionslaeufe (
    Lauf_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Artikel TEXT NOT NULL,  -- 'Zahnrad Z42', 'Welle W15', 'Gehäuse G08'
    Menge_Geplant INTEGER NOT NULL CHECK(Menge_Geplant > 0),
    Menge_Produziert INTEGER DEFAULT 0,
    Start_Zeit TEXT NOT NULL,  -- Format: YYYY-MM-DD HH:MM:SS
    End_Zeit TEXT,
    Dauer_Minuten INTEGER,
    Status TEXT CHECK(Status IN ('Geplant', 'Laufend', 'Abgeschlossen', 'Abgebrochen')) DEFAULT 'Geplant',
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
);
```

**Beispieldaten**: 50 Produktionsläufe, verschiedene Artikel, Status-Verteilung: 60% Abgeschlossen, 20% Laufend, 20% Geplant

---

#### 5. `Pruefprotokolle`
**Wichtig für Aufgabe P1**: Enthält Qualitätsprüfungen. Diese Tabelle wird in P1 für SQL-Injection-Tests verwendet.

```sql
CREATE TABLE Pruefprotokolle (
    Pruef_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artikelname TEXT NOT NULL,
    Pruef_Datum TEXT NOT NULL,
    Pruef_Wert REAL NOT NULL,
    Soll_Wert REAL NOT NULL,
    Status TEXT CHECK(Status IN ('Bestanden', 'Fehlgeschlagen')) NOT NULL
);
```

**Beispieldaten**: 30 Prüfprotokolle für "Zahnrad Z42", "Welle W15", "Gehäuse G08"

---

#### Indizes

Folgende Indizes sind bereits erstellt:

```sql
CREATE INDEX idx_wartungen_maschinen ON Wartungen(Maschinen_ID);
CREATE INDEX idx_wartungen_datum ON Wartungen(Datum);
CREATE INDEX idx_laeufe_maschinen ON Produktionslaeufe(Maschinen_ID);
CREATE INDEX idx_laeufe_status ON Produktionslaeufe(Status);
```

---

## 📁 Zusätzliche Dateien

### `wartungen_2023_2024.csv`
CSV-Export aller Wartungen aus 2023-2024 zur Verwendung in pandas (Aufgabe P4).

**Spalten**:
- `Wartung_ID`: Integer
- `Maschinen_ID`: Integer
- `Maschinenname`: Text (JOIN mit Maschinen)
- `Typ`: Text (Maschinentyp)
- `Wartungstyp`: Text
- `Datum`: Text (YYYY-MM-DD)
- `Kosten`: Float
- `Techniker`: Text
- `Quartal`: Text (z.B. "2023-Q1")

**Größe**: 80 Zeilen + Header

---

### `materialbewegungen.json`
JSON-Datei mit historischen Material-Buchungen (Einlagerungen/Entnahmen) für Aufgabe P3.

**Struktur**:
```json
{
  "bewegungen": [
    {
      "id": 1,
      "material_id": 101,
      "materialname": "Stahl C45",
      "menge_aenderung": -150.5,
      "zeitstempel": "2024-01-15 10:30:00",
      "grund": "Produktionslauf 1045",
      "lager_nach_buchung": 1849.5
    },
    ...
  ]
}
```

**Größe**: 100 Bewegungen

---

## 🛠️ Datenbank initialisieren

Um die Datenbank neu zu erstellen (z.B. nach versehentlichem DROP), führe das Skript `init_produktionsdb.py` aus:

```bash
python testdaten/init_produktionsdb.py
```

Dies erstellt `produktionsdb.db` mit allen Tabellen, Indizes und Beispieldaten.

---

## 📈 Verwendung in Aufgaben

- **P1 (SQL-Injection)**: Nutzt Tabelle `Pruefprotokolle`
- **P2 (UPDATE/DELETE)**: Nutzt `Maschinen` und `Wartungen`
- **P3 (Transaktionen)**: Nutzt `Materialbestand`, `Maschinen`, `Produktionslaeufe`
- **P4 (Aggregationen + Visualisierung)**: Nutzt `wartungen_2023_2024.csv` oder direkten DB-Zugriff
- **P5 (Projekt)**: Erweitert DB um `Pruefprotokolle` (vollständiges Schema) und `Fehlerarten`

---

## ⚠️ Wichtige Hinweise

- **Foreign Keys**: Müssen in SQLite explizit aktiviert werden: `PRAGMA foreign_keys = ON;`
- **Transaktionen**: SQLite verwendet standardmäßig autocommit. Für explizite Transaktionen `BEGIN TRANSACTION` verwenden oder `isolation_level=None` bei `sqlite3.connect()` setzen.
- **Datum-Format**: Alle Datumsangaben als TEXT in ISO 8601 Format (`YYYY-MM-DD` oder `YYYY-MM-DD HH:MM:SS`)
- **Backup**: Die Original-Datei wird nicht überschrieben. Teste Queries zuerst mit `.backup` oder Kopie.

---

**Erstellt**: 2026-01-04  
**Version**: 1.0  
**Autor**: Informatik-Dozent KI-Assistent
