"""
Initialisiert die Datenbank produktionsdb.db mit allen Tabellen und Beispieldaten.
Verwendung: python testdaten/init_produktionsdb.py
"""

import sqlite3
import random
from datetime import datetime, timedelta

# Datenbankverbindung
conn = sqlite3.connect('testdaten/produktionsdb.db')
cursor = conn.cursor()

# Foreign Keys aktivieren
cursor.execute('PRAGMA foreign_keys = ON;')

print("🗄️  Erstelle Tabellen...")

# Tabelle: Maschinen
cursor.execute('''
CREATE TABLE IF NOT EXISTS Maschinen (
    Maschinen_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE,
    Typ TEXT NOT NULL,
    Baujahr INTEGER NOT NULL CHECK(Baujahr >= 1980 AND Baujahr <= 2024),
    Betriebsstunden INTEGER DEFAULT 0,
    Status TEXT CHECK(Status IN ('Bereit', 'Produktion', 'Wartung', 'Defekt')) DEFAULT 'Bereit',
    Aktiv INTEGER DEFAULT 1
);
''')

# Tabelle: Wartungen
cursor.execute('''
CREATE TABLE IF NOT EXISTS Wartungen (
    Wartung_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Wartungstyp TEXT NOT NULL,
    Datum TEXT NOT NULL,
    Kosten REAL NOT NULL CHECK(Kosten >= 0),
    Techniker TEXT,
    Beschreibung TEXT,
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID) ON DELETE CASCADE
);
''')

# Tabelle: Materialbestand
cursor.execute('''
CREATE TABLE IF NOT EXISTS Materialbestand (
    Material_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Materialname TEXT NOT NULL UNIQUE,
    Menge_Lager REAL NOT NULL CHECK(Menge_Lager >= 0),
    Einheit TEXT NOT NULL,
    Mindestbestand REAL NOT NULL,
    Preis_Pro_Einheit REAL NOT NULL
);
''')

# Tabelle: Produktionslaeufe
cursor.execute('''
CREATE TABLE IF NOT EXISTS Produktionslaeufe (
    Lauf_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Maschinen_ID INTEGER NOT NULL,
    Artikel TEXT NOT NULL,
    Menge_Geplant INTEGER NOT NULL CHECK(Menge_Geplant > 0),
    Menge_Produziert INTEGER DEFAULT 0,
    Start_Zeit TEXT NOT NULL,
    End_Zeit TEXT,
    Dauer_Minuten INTEGER,
    Status TEXT CHECK(Status IN ('Geplant', 'Laufend', 'Abgeschlossen', 'Abgebrochen')) DEFAULT 'Geplant',
    FOREIGN KEY (Maschinen_ID) REFERENCES Maschinen(Maschinen_ID)
);
''')

# Tabelle: Pruefprotokolle (für P1 - SQL-Injection)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pruefprotokolle (
    Pruef_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Artikelname TEXT NOT NULL,
    Pruef_Datum TEXT NOT NULL,
    Pruef_Wert REAL NOT NULL,
    Soll_Wert REAL NOT NULL,
    Status TEXT CHECK(Status IN ('Bestanden', 'Fehlgeschlagen')) NOT NULL
);
''')

print("✅ Tabellen erstellt.")
print("📊 Füge Beispieldaten ein...")

# Maschinen einfügen
maschinen_daten = [
    ('CNC-Fräse 01', 'Fräse', 2018, 12500, 'Bereit', 1),
    ('CNC-Fräse 02', 'Fräse', 2020, 8300, 'Produktion', 1),
    ('CNC-Fräse 03', 'Fräse', 2015, 18000, 'Wartung', 1),
    ('CNC-Fräse 04', 'Fräse', 2022, 3200, 'Bereit', 1),
    ('CNC-Fräse 05', 'Fräse', 2019, 10500, 'Bereit', 1),
    ('Drehmaschine 01', 'Drehbank', 2016, 15000, 'Produktion', 1),
    ('Drehmaschine 02', 'Drehbank', 2021, 5500, 'Bereit', 1),
    ('Drehmaschine 03', 'Drehbank', 2017, 13800, 'Bereit', 1),
    ('Drehmaschine 04', 'Drehbank', 2023, 1200, 'Bereit', 1),
    ('Drehmaschine 05', 'Drehbank', 2014, 22000, 'Defekt', 0),
    ('Roboter-Arm R1', 'Roboter', 2020, 7800, 'Produktion', 1),
    ('Roboter-Arm R2', 'Roboter', 2022, 3400, 'Bereit', 1),
    ('Roboter-Arm R3', 'Roboter', 2019, 9200, 'Bereit', 1),
    ('Hydraulikpresse HP-01', 'Presse', 2015, 16500, 'Bereit', 1),
    ('Hydraulikpresse HP-02', 'Presse', 2018, 11000, 'Wartung', 1),
]

cursor.executemany('INSERT INTO Maschinen (Name, Typ, Baujahr, Betriebsstunden, Status, Aktiv) VALUES (?, ?, ?, ?, ?, ?)', maschinen_daten)

# Wartungen einfügen (80 Einträge über 2023-2024)
wartungen_daten = []
wartungstypen = ['Inspektion', 'Reparatur', 'Ölwechsel', 'Kalibrierung', 'Reinigung']
techniker = ['Müller T.', 'Schmidt A.', 'Weber K.', 'Fischer M.', 'Meyer S.']

start_datum = datetime(2023, 1, 1)
for i in range(80):
    maschinen_id = random.randint(1, 15)
    wartungstyp = random.choice(wartungstypen)
    datum = (start_datum + timedelta(days=random.randint(0, 729))).strftime('%Y-%m-%d')  # 2 Jahre
    kosten = round(random.uniform(50, 5000), 2)
    tech = random.choice(techniker)
    beschreibung = f"{wartungstyp} durchgeführt"
    
    wartungen_daten.append((maschinen_id, wartungstyp, datum, kosten, tech, beschreibung))

cursor.executemany('INSERT INTO Wartungen (Maschinen_ID, Wartungstyp, Datum, Kosten, Techniker, Beschreibung) VALUES (?, ?, ?, ?, ?, ?)', wartungen_daten)

# Materialbestand einfügen
material_daten = [
    ('Stahl C45', 2000.0, 'kg', 500.0, 4.50),
    ('Aluminium AlMgSi1', 1500.0, 'kg', 300.0, 8.20),
    ('Schrauben M8x30', 5000.0, 'Stück', 1000.0, 0.15),
    ('Schrauben M10x40', 3500.0, 'Stück', 800.0, 0.22),
    ('Hydrauliköl HLP 68', 800.0, 'Liter', 200.0, 12.50),
    ('Kühlschmierstoff', 1200.0, 'Liter', 300.0, 8.00),
    ('Dichtungen NBR', 500.0, 'Stück', 100.0, 2.80),
    ('Kugellager 6203', 150.0, 'Stück', 30.0, 18.50),
    ('Kupferrohr 15mm', 300.0, 'm', 50.0, 6.40),
    ('Schleifpapier K120', 100.0, 'Bogen', 20.0, 1.20),
]

cursor.executemany('INSERT INTO Materialbestand (Materialname, Menge_Lager, Einheit, Mindestbestand, Preis_Pro_Einheit) VALUES (?, ?, ?, ?, ?)', material_daten)

# Produktionsläufe einfügen (50 Einträge)
produktions_daten = []
artikel = ['Zahnrad Z42', 'Welle W15', 'Gehäuse G08', 'Flansch F12', 'Lager LG05']
status_liste = ['Abgeschlossen', 'Abgeschlossen', 'Abgeschlossen', 'Laufend', 'Geplant']

for i in range(50):
    maschinen_id = random.randint(1, 15)
    artikel_name = random.choice(artikel)
    menge_geplant = random.randint(10, 200)
    status = random.choice(status_liste)
    
    start_zeit = (datetime(2023, 6, 1) + timedelta(days=random.randint(0, 549))).strftime('%Y-%m-%d %H:%M:%S')
    
    if status == 'Abgeschlossen':
        menge_produziert = menge_geplant
        dauer_minuten = random.randint(30, 480)
        end_zeit = (datetime.strptime(start_zeit, '%Y-%m-%d %H:%M:%S') + timedelta(minutes=dauer_minuten)).strftime('%Y-%m-%d %H:%M:%S')
    elif status == 'Laufend':
        menge_produziert = int(menge_geplant * random.uniform(0.3, 0.8))
        dauer_minuten = None
        end_zeit = None
    else:  # Geplant
        menge_produziert = 0
        dauer_minuten = None
        end_zeit = None
    
    produktions_daten.append((maschinen_id, artikel_name, menge_geplant, menge_produziert, start_zeit, end_zeit, dauer_minuten, status))

cursor.executemany('INSERT INTO Produktionslaeufe (Maschinen_ID, Artikel, Menge_Geplant, Menge_Produziert, Start_Zeit, End_Zeit, Dauer_Minuten, Status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', produktions_daten)

# Prüfprotokolle einfügen (30 Einträge für P1)
pruef_daten = []
pruef_artikel = ['Zahnrad Z42', 'Welle W15', 'Gehäuse G08']

for i in range(30):
    artikel_name = random.choice(pruef_artikel)
    pruef_datum = (datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
    
    if artikel_name == 'Zahnrad Z42':
        soll_wert = 50.00
        toleranz = 0.05
    elif artikel_name == 'Welle W15':
        soll_wert = 100.00
        toleranz = 0.10
    else:  # Gehäuse G08
        soll_wert = 75.00
        toleranz = 0.08
    
    pruef_wert = soll_wert + random.uniform(-toleranz * 2, toleranz * 2)
    status = 'Bestanden' if abs(pruef_wert - soll_wert) <= toleranz else 'Fehlgeschlagen'
    
    pruef_daten.append((artikel_name, pruef_datum, pruef_wert, soll_wert, status))

cursor.executemany('INSERT INTO Pruefprotokolle (Artikelname, Pruef_Datum, Pruef_Wert, Soll_Wert, Status) VALUES (?, ?, ?, ?, ?)', pruef_daten)

print("✅ Beispieldaten eingefügt.")
print("🔧 Erstelle Indizes...")

# Indizes erstellen
cursor.execute('CREATE INDEX IF NOT EXISTS idx_wartungen_maschinen ON Wartungen(Maschinen_ID);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_wartungen_datum ON Wartungen(Datum);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_laeufe_maschinen ON Produktionslaeufe(Maschinen_ID);')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_laeufe_status ON Produktionslaeufe(Status);')

print("✅ Indizes erstellt.")

# Transaktion committen
conn.commit()

# Statistiken ausgeben
cursor.execute('SELECT COUNT(*) FROM Maschinen')
print(f"📊 Statistik:")
print(f"   Maschinen: {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT(*) FROM Wartungen')
print(f"   Wartungen: {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT(*) FROM Materialbestand')
print(f"   Materialien: {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT(*) FROM Produktionslaeufe')
print(f"   Produktionsläufe: {cursor.fetchone()[0]}")

cursor.execute('SELECT COUNT(*) FROM Pruefprotokolle')
print(f"   Prüfprotokolle: {cursor.fetchone()[0]}")

conn.close()
print("✅ Datenbank 'produktionsdb.db' erfolgreich erstellt!")
