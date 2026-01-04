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
Zeitstempel,Quell_IP,Ziel_IP,Protokoll,Paketgroesse_Bytes,Latenz_ms
```

**Aufgabe:**

Schreibe ein Python-Programm, das die CSV-Datei analysiert und folgende Informationen ausgibt:

**a) Protokoll-Verteilung**
- Anzahl der Pakete pro Protokoll (Modbus TCP, MQTT, OPC UA)
- Prozentuale Verteilung

**b) Netzwerk-Last**
- Gesamtes übertragenes Datenvolumen in MB
- Durchschnittliche Paketgröße pro Protokoll

**c) Performance-Analyse**
- Durchschnittliche Latenz pro Protokoll
- Anzahl der Pakete mit Latenz > 100ms (kritisch für Echtzeitsteuerung)

**d) Maschinen-Kommunikation**
- Top 3 aktivste Maschinen (Quell-IPs mit den meisten gesendeten Paketen)
- Liste aller Maschinen, die mit dem SCADA-Server (192.168.1.100) kommunizieren

**Anforderungen:**
- Nutze `csv.DictReader` für das Einlesen
- Behandle fehlerhafte oder unvollständige Zeilen
- Formatiere Ausgaben übersichtlich mit Einheiten

**Erwartete Ausgabe (Beispiel):**
```
=== Netzwerk-Paket-Analyse ===

Protokoll-Verteilung:
  Modbus TCP: 42 Pakete (42.0%)
  MQTT: 35 Pakete (35.0%)
  OPC UA: 23 Pakete (23.0%)

Netzwerk-Last:
  Gesamt: 0.15 MB
  Ø Paketgröße Modbus TCP: 1024 Bytes
  Ø Paketgröße MQTT: 512 Bytes
  Ø Paketgröße OPC UA: 2048 Bytes

Performance:
  Ø Latenz Modbus TCP: 15.3 ms
  Ø Latenz MQTT: 8.7 ms
  Ø Latenz OPC UA: 42.1 ms
  Kritische Pakete (>100ms): 5

Top 3 aktivste Maschinen:
  1. 192.168.1.10: 18 Pakete
  2. 192.168.1.11: 15 Pakete
  3. 192.168.1.12: 12 Pakete

Kommunikation mit SCADA (192.168.1.100):
  - 192.168.1.10
  - 192.168.1.11
  - 192.168.1.13
```

---

###

 Aufgabe P2: Socket-Programmierung – Maschinen-Status-Monitor ⭐⭐ (Mittel)

Schreibe eine **Generator-Funktion** `filtere_zeilen(dateiname, mindestlaenge)`, die:
- Eine Textdatei Zeile für Zeile liest
- Nur Zeilen zurückgibt, die **mindestens `mindestlaenge` Zeichen** haben (nach `.strip()`)
- Leerzeilen ignoriert

**Anforderungen:**
- Nutze `yield` für speicher-effiziente Verarbeitung
- Verwende `with`-Statement für sicheres Datei-Handling
- Behandle FileNotFoundError mit aussagekräftiger Fehlermeldung

**Testdatei erstellen** (`test.txt`):
```
Kurz
Diese Zeile ist lang genug
x

Mittlere Länge hier
Superlange Zeile mit vielen Wörtern und Zeichen
```

**Beispiel-Nutzung:**
```python
for zeile in filtere_zeilen("test.txt", mindestlaenge=20):
    print(zeile)

# Erwartete Ausgabe:
# Diese Zeile ist lang genug
# Superlange Zeile mit vielen Wörtern und Zeichen
```

---

### Aufgabe 5: CSV-Analyse – Studenten-Datenbank ⭐⭐ (Mittel)

Gegeben ist eine CSV-Datei `studenten.csv` mit folgendem Inhalt:

```csv
Matrikelnummer,Name,Studiengang,Semester,Note
12345,Alice,Informatik,3,1.3
23456,Bob,Maschinenbau,5,2.1
34567,Charlie,Informatik,2,1.7
45678,Diana,Elektrotechnik,4,1.9
56789,Eve,Informatik,6,2.3
67890,Frank,Maschinenbau,1,3.0
78901,Grace,Informatik,4,1.5
```

**Schreibe ein Programm, das folgende Aufgaben löst:**

**a) Durchschnittsnote pro Studiengang**

Berechne die Durchschnittsnote für jeden Studiengang und gib das Ergebnis formatiert aus.

**Erwartete Ausgabe:**
```
Durchschnittsnoten nach Studiengang:
  Informatik: 1.70
  Maschinenbau: 2.55
  Elektrotechnik: 1.90
```

**b) Beste Studenten**

Gib alle Studenten aus, die eine Note **besser als 1.8** haben. Sortiere nach Note (beste zuerst).

**Erwartete Ausgabe:**
```
Studenten mit Note < 1.8:
  1. Alice (Informatik, Semester 3): 1.3
  2. Grace (Informatik, Semester 4): 1.5
  3. Charlie (Informatik, Semester 2): 1.7
```

**c) Neue CSV schreiben**

Erstelle eine neue CSV-Datei `informatik_studenten.csv`, die nur Informatik-Studenten enthält. Füge eine zusätzliche Spalte "Bewertung" hinzu:
- Note ≤ 1.5: "Sehr gut"
- Note ≤ 2.0: "Gut"
- Note > 2.0: "Befriedigend"

**Anforderungen:**
- Nutze `csv.DictReader` und `csv.DictWriter`
- Behandle fehlende Dateien und ungültige Datenformate
- Runde Durchschnittsnoten auf 2 Dezimalstellen

---

### Aufgabe 6: Iterator vs. Iterable verstehen ⭐⭐ (Mittel)

**Teil 1: Analyse**

Analysiere den folgenden Code und beantworte die Fragen:

```python
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

# Verwendung:
fib = Fibonacci(5)
```

**Fragen:**
1. Ist `Fibonacci` ein **Iterable**, ein **Iterator**, oder beides? Begründe.
2. Was gibt `list(fib)` zurück?
3. Was passiert, wenn du danach `list(fib)` ein zweites Mal aufrufst? Warum?
4. Wie müsste die Klasse geändert werden, damit sie **mehrfach** iterierbar ist?

**Teil 2: Implementierung**

Schreibe eine **Generator-Funktion** `fibonacci_generator(n)`, die dieselbe Funktionalität wie die obige Klasse bietet, aber als Generator implementiert ist.

**Anforderungen:**
- Nutze `yield` statt `return`
- Funktion soll Fibonacci-Zahlen von 0 bis zur n-ten Zahl erzeugen
- Teste mit `n=10`

**Erwartete Ausgabe:**
```python
print(list(fibonacci_generator(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

### Aufgabe 7: Log-Datei-Analyse mit Generator-Pipeline ⭐⭐⭐ (Schwer)

Du erhältst eine große Log-Datei `access.log` im Apache Combined Log Format:

```
192.168.1.100 - - [10/Jan/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
192.168.1.101 - - [10/Jan/2024:13:55:37 +0000] "GET /about.html HTTP/1.1" 200 1523
192.168.1.102 - - [10/Jan/2024:13:55:38 +0000] "POST /api/login HTTP/1.1" 401 512
192.168.1.100 - - [10/Jan/2024:13:55:39 +0000] "GET /admin HTTP/1.1" 403 234
192.168.1.103 - - [10/Jan/2024:13:55:40 +0000] "GET /data.json HTTP/1.1" 500 1024
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
     - `ip`: IP-Adresse
     - `timestamp`: Zeitstempel (String)
     - `method`: HTTP-Methode (GET, POST, etc.)
     - `path`: Pfad (z.B. `/index.html`)
     - `status`: HTTP-Statuscode als Integer
     - `bytes`: Übertragene Bytes als Integer
   - Ignoriere ungültige Zeilen (fehlerhafte Struktur)

3. **`filtere_status(log_entries, status_code)`**:
   - Nimmt Generator von Dictionaries entgegen
   - Gibt nur Einträge mit spezifischem Statuscode zurück

**b) Analyse-Funktionen**

Implementiere folgende Analyse-Funktionen, die die Pipeline nutzen:

1. **`zaehle_status_codes(dateiname)`**:
   - Gibt Dictionary mit Anzahl pro Statuscode zurück
   - Format: `{200: 152, 404: 23, 500: 5, ...}`

2. **`finde_fehlerhafte_requests(dateiname)`**:
   - Gibt Liste aller Requests mit Statuscode 4xx oder 5xx zurück
   - Sortiert nach Statuscode (höchste zuerst)

3. **`top_ips(dateiname, n=5)`**:
   - Gibt die Top-N IP-Adressen mit den meisten Requests zurück
   - Format: Liste von Tupeln `[(ip, anzahl), ...]`

**Anforderungen:**
- **Speicher-Effizienz**: Nutze Generator-Pipeline, nicht `readlines()`
- **Fehlerbehandlung**: Ignoriere ungültige Zeilen, zähle sie aber
- **Performance**: Datei wird nur einmal gelesen pro Analyse
- **Ausgabe**: Formatiere Ergebnisse übersichtlich

**Beispiel-Ausgabe:**
```python
# Status-Code-Verteilung:
status_counts = zaehle_status_codes("access.log")
print("Status-Code-Verteilung:")
for code, count in sorted(status_counts.items()):
    print(f"  {code}: {count}")

# Output:
# Status-Code-Verteilung:
#   200: 152
#   401: 12
#   403: 8
#   404: 23
#   500: 5

# Fehlerhafte Requests:
errors = finde_fehlerhafte_requests("access.log")
print(f"\n{len(errors)} fehlerhafte Requests gefunden")

# Top-5 IPs:
top = top_ips("access.log", n=5)
print("\nTop-5 aktivste IP-Adressen:")
for i, (ip, count) in enumerate(top, 1):
    print(f"  {i}. {ip}: {count} Requests")
```

**Bonus (+⭐):** Erweitere die Pipeline um eine Funktion `zeitfenster_analyse(dateiname, start_stunde, end_stunde)`, die nur Requests innerhalb eines bestimmten Stunden-Fensters analysiert (z.B. zwischen 13:00 und 15:00 Uhr).

---

### Aufgabe 8: CSV-Daten-Transformation mit Generatoren ⭐⭐⭐⭐ (Sehr Schwer)

Du arbeitest für ein E-Commerce-Unternehmen und erhältst täglich eine große CSV-Datei `orders.csv` mit Bestellungen:

```csv
OrderID,CustomerID,ProductID,Quantity,Price,OrderDate,Status
1001,C001,P100,2,19.99,2024-01-10,completed
1002,C002,P101,1,49.99,2024-01-10,completed
1003,C001,P102,3,9.99,2024-01-10,pending
1004,C003,P100,1,19.99,2024-01-11,completed
1005,C002,P103,5,5.99,2024-01-11,cancelled
1006,C004,P100,2,19.99,2024-01-11,completed
```

**Aufgabe: Erstelle eine speicher-effiziente ETL-Pipeline (Extract, Transform, Load)**

**Teil 1: Extrahieren und Validieren**

Implementiere einen Generator `validiere_bestellungen(dateiname)`, der:
- CSV-Datei mit `csv.DictReader` liest
- Jede Bestellung validiert:
  - `OrderID`, `CustomerID`, `ProductID` müssen vorhanden sein
  - `Quantity` muss positive Ganzzahl sein
  - `Price` muss positive Dezimalzahl sein
  - `OrderDate` muss gültiges Datum sein (Format: YYYY-MM-DD)
  - `Status` muss einer der Werte sein: `completed`, `pending`, `cancelled`
- Nur **valide** Bestellungen als Dictionary zurückgibt
- **Fehlerhafte** Zeilen in separate Datei `errors.log` schreibt (mit Fehlerbeschreibung)

**Teil 2: Transformieren**

Implementiere einen Generator `transformiere_bestellungen(bestellungen)`, der:
- `OrderDate` von String zu `datetime`-Objekt konvertiert
- Neues Feld `TotalPrice` berechnet: `Quantity * Price`
- Neues Feld `Year`, `Month`, `Day` aus `OrderDate` extrahiert
- Neues Feld `IsHighValue` hinzufügt: `True` wenn `TotalPrice > 50`, sonst `False`

**Teil 3: Aggregieren**

Implementiere folgende Analyse-Funktionen:

1. **`umsatz_pro_tag(bestellungen)`**:
   - Berechnet Gesamtumsatz pro Tag (nur `completed` Orders)
   - Gibt Dictionary zurück: `{datetime.date(...): Decimal('...')}`

2. **`top_produkte(bestellungen, n=5)`**:
   - Findet die Top-N meist-bestellten Produkte
   - Gibt Liste von Tupeln: `[(ProductID, Anzahl_Bestellungen, Gesamtumsatz), ...]`

3. **`kunden_statistik(bestellungen)`**:
   - Berechnet pro Kunde: Anzahl Bestellungen, Gesamtumsatz, durchschnittlicher Warenkorb
   - Gibt Dictionary: `{CustomerID: {'orders': int, 'total': Decimal, 'avg': Decimal}}`

**Teil 4: Laden (Exportieren)**

Implementiere `exportiere_aggregierte_daten(input_datei, output_prefix)`, das:
- Die gesamte Pipeline durchläuft
- Drei neue CSV-Dateien erstellt:
  - `{output_prefix}_daily_revenue.csv`: Tagesumsätze
  - `{output_prefix}_top_products.csv`: Top-Produkte
  - `{output_prefix}_customer_stats.csv`: Kunden-Statistik
- Alle Dateien mit `csv.DictWriter` schreibt

**Anforderungen:**
- **Speicher-Effizienz**: Datei wird nur **einmal** durchgelesen für alle Analysen (nutze `itertools.tee()` falls nötig)
- **Fehlertoleranz**: Einzelne fehlerhafte Zeilen stoppen nicht die gesamte Verarbeitung
- **Genauigkeit**: Nutze `decimal.Decimal` für Geldbeträge (keine Float-Rundungsfehler!)
- **Performance**: Bei 1 Million Zeilen < 30 Sekunden
- **Logging**: Schreibe Statistiken (Anzahl verarbeitete/fehlerhafte Zeilen, Laufzeit)

**Beispiel-Nutzung:**
```python
exportiere_aggregierte_daten("orders.csv", "report_2024_01")

# Erstellt:
# - report_2024_01_daily_revenue.csv
# - report_2024_01_top_products.csv
# - report_2024_01_customer_stats.csv
# - errors.log

# Konsolen-Ausgabe:
# Verarbeitung gestartet...
# ✓ 12.543 Bestellungen validiert
# ✗ 87 fehlerhafte Zeilen (siehe errors.log)
# ✓ Export abgeschlossen
# Laufzeit: 2.34 Sekunden
```

**Bonus (+⭐):** Implementiere eine Funktion `inkrementeller_export(input_datei, state_datei, output_prefix)`, die:
- Merkt sich, welche Bestellungen bereits verarbeitet wurden (via `state_datei`)
- Bei erneutem Aufruf nur **neue** Bestellungen verarbeitet (inkrementelles Update)
- Ideal für tägliche Batch-Jobs

**Tipp:** Nutze `collections.defaultdict`, `itertools.tee()` und `decimal.Decimal` aus der Standard-Library.

