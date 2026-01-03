# V16: Netzwerktechnik Grundlagen & Protokolle – Teil 2 - Übungsaufgaben

---

## Theorieaufgaben

### Aufgabe T1: TCP vs. UDP - Protokollauswahl (⭐)

**Kontext**: Ein Unternehmen plant verschiedene Netzwerkanwendungen und muss entscheiden, welches Transportprotokoll (TCP oder UDP) jeweils am besten geeignet ist.

**Aufgabenstellung**:

Analysiere die folgenden Anwendungsfälle und entscheide begründet, ob TCP oder UDP die bessere Wahl ist. Erkläre jeweils in 2-3 Sätzen, warum.

a) **Online-Banking-Anwendung**: Kunden können Überweisungen tätigen und ihren Kontostand abfragen.

b) **Video-Streaming-Plattform**: Benutzer schauen Live-Sportübertragungen.

c) **Firmendatenbank-Backup**: Nächtliche Sicherung von 500 GB Unternehmensdaten auf einen Remote-Server.

d) **VoIP-Telefonie**: Mitarbeiter führen Sprachtelefonate über das Netzwerk.

e) **IoT-Sensoren**: 1000 Temperatursensoren in einer Produktionshalle senden alle 5 Sekunden Messwerte an einen zentralen Server.

**Lernziele**: Verständnis der Unterschiede zwischen TCP und UDP; Fähigkeit, das passende Protokoll für konkrete Anwendungsfälle auszuwählen.

---

### Aufgabe T2: REST-API Design (⭐⭐)

**Kontext**: Du entwickelst eine REST-API für ein Bibliothekssystem. Die API soll die Verwaltung von Büchern, Autoren und Ausleihen ermöglichen.

**Aufgabenstellung**:

Entwirf RESTful API-Endpunkte für die folgenden Operationen. Gib jeweils die **HTTP-Methode**, die **URI** und den erwarteten **HTTP-Statuscode bei Erfolg** an.

a) Alle Bücher abrufen

b) Details eines spezifischen Buches mit ID 42 abrufen

c) Ein neues Buch hinzufügen

d) Die Informationen eines Buches mit ID 42 vollständig aktualisieren

e) Ein Buch mit ID 42 löschen

f) Alle Bücher eines bestimmten Autors (Autor-ID 7) abrufen

g) Ein Buch (ID 42) an einen Benutzer (ID 123) ausleihen (Erstellen einer neuen Ausleihe)

**Zusatzfrage**: Welche REST-Prinzipien (von den 6 Hauptprinzipien) werden durch dein API-Design besonders gut erfüllt? Nenne mindestens zwei und erkläre kurz.

**Lernziele**: Verständnis der REST-Prinzipien; Fähigkeit, RESTful API-Endpunkte zu entwerfen; Korrekte Verwendung von HTTP-Methoden und Statuscodes.

---

### Aufgabe T3: DNS-Auflösung verstehen (⭐⭐⭐)

**Kontext**: Ein Benutzer gibt `https://shop.example.com/products` in seinen Browser ein. Der lokale DNS-Cache ist leer. Der DNS-Resolver des ISP hat ebenfalls keinen Eintrag für diese Domain.

**Aufgabenstellung**:

a) **DNS-Auflösung nachvollziehen**: Beschreibe Schritt für Schritt, wie die DNS-Auflösung für `shop.example.com` abläuft. Erkläre, welche DNS-Server (Root, TLD, Authoritative) nacheinander kontaktiert werden und welche Informationen jeweils zurückgegeben werden.

b) **DNS-Record-Typen**: Angenommen, die DNS-Zone für `example.com` enthält folgende Records:

```
example.com.          IN  A      93.184.216.34
www.example.com.      IN  CNAME  example.com.
shop.example.com.     IN  A      203.0.113.50
mail.example.com.     IN  A      203.0.113.100
example.com.          IN  MX     10 mail.example.com.
example.com.          IN  NS     ns1.example.com.
example.com.          IN  NS     ns2.example.com.
```

Beantworte folgende Fragen:
- Welche IP-Adresse erhält der Browser für `shop.example.com`?
- Wenn ein Benutzer `www.example.com` anfragt, welche Antwort erhält er vom DNS-Server? Erkläre, wie CNAME-Records funktionieren.
- An welchen Server werden E-Mails für `admin@example.com` zugestellt?
- Was ist die Funktion der NS-Records?

c) **Caching und TTL**: Die A-Records haben eine TTL (Time To Live) von 300 Sekunden. Erkläre, was das bedeutet und welche Auswirkungen eine zu kurze oder zu lange TTL haben kann.

**Lernziele**: Tiefes Verständnis der DNS-Auflösung; Kenntnis verschiedener DNS-Record-Typen; Verständnis von DNS-Caching und TTL.

---

## Python-Aufgaben

> [!NOTE]
> Für alle Python-Aufgaben gilt: Verwende **Pandas** für die Datenverarbeitung. Achte auf **Vektorisierung** statt Schleifen, wo möglich, um gute Performance zu erreichen.

---

### Aufgabe P1: Pandas-Grundlagen - CSV einlesen und erkunden (⭐)

**Kontext**: Du hast eine CSV-Datei mit Mitarbeiterdaten eines Unternehmens erhalten. Deine Aufgabe ist es, die Daten einzulesen und einen ersten Überblick zu gewinnen.

**Datensatz** (`employees.csv`):
```csv
ID,Name,Abteilung,Gehalt,Eintritt,Alter
1,Alice Mueller,IT,65000,2020-03-15,32
2,Bob Schmidt,Vertrieb,55000,2019-07-22,28
3,Charlie Weber,IT,70000,2018-11-05,35
4,Diana Fischer,HR,52000,2021-01-10,29
5,Eva Wagner,Vertrieb,58000,2019-12-03,31
6,Frank Becker,IT,72000,2017-05-18,38
7,Gina Hoffmann,HR,54000,2020-09-25,27
8,Hans Schulz,Vertrieb,60000,2018-08-14,33
```

**Aufgabenstellung**:

a) Erstelle die CSV-Datei `employees.csv` mit dem obigen Inhalt.

b) Lies die CSV-Datei mit Pandas ein und speichere den DataFrame in der Variable `df`.

c) Zeige die **ersten 3 Zeilen** des DataFrames an.

d) Zeige **detaillierte Informationen** über den DataFrame an (Datentypen, fehlende Werte, Speicherverbrauch).

e) Berechne **deskriptive Statistiken** für numerische Spalten (Mittelwert, Standardabweichung, Min, Max, Quartile).

f) Wie viele **Zeilen und Spalten** hat der DataFrame?

g) Welche **Spaltennamen** existieren?

h) Konvertiere die Spalte `Eintritt` in den Datentyp **datetime**.

**Lernziele**: CSV-Dateien einlesen; DataFrame inspizieren; Basis-Methoden anwenden.

---

### Aufgabe P2: Filtern und Sortieren (⭐⭐)

**Kontext**: Verwende den DataFrame aus Aufgabe P1.

**Aufgabenstellung**:

a) **Filter 1**: Zeige alle Mitarbeiter, die in der Abteilung **"IT"** arbeiten.

b) **Filter 2**: Zeige alle Mitarbeiter, deren Gehalt **größer als 60000** ist.

c) **Filter 3**: Zeige alle Mitarbeiter, die **zwischen 30 und 35 Jahre alt** sind (inklusive).

d) **Kombinierter Filter**: Zeige alle Mitarbeiter aus der Abteilung **"Vertrieb"**, die ein Gehalt **größer als 55000** haben.

e) **Filter mit `.isin()`**: Zeige alle Mitarbeiter aus den Abteilungen **"IT"** oder **"HR"**.

f) **Sortierung 1**: Sortiere den DataFrame nach **Gehalt** (aufsteigend) und zeige das Ergebnis an.

g) **Sortierung 2**: Sortiere den DataFrame nach **Abteilung** (alphabetisch aufsteigend) und innerhalb jeder Abteilung nach **Gehalt** (absteigend).

**Lernziele**: Filtern mit Bedingungen; Kombinierte Bedingungen mit `&`, `|`; Sortieren nach einer oder mehreren Spalten.

---

### Aufgabe P3: Aggregation und Gruppierung (⭐⭐⭐)

**Kontext**: Verwende den DataFrame aus Aufgabe P1.

**Aufgabenstellung**:

a) Berechne das **durchschnittliche Gehalt** aller Mitarbeiter.

b) Berechne das **durchschnittliche Gehalt pro Abteilung**.

c) Finde das **höchste Gehalt pro Abteilung**.

d) Zähle, wie viele **Mitarbeiter pro Abteilung** arbeiten.

e) Erstelle eine **Übersichtstabelle** pro Abteilung, die folgende Informationen enthält:
   - Anzahl der Mitarbeiter
   - Durchschnittliches Gehalt
   - Minimales Gehalt
   - Maximales Gehalt
   - Gesamtsumme der Gehälter

f) Welche Abteilung hat die **höchste Gesamtsumme an Gehältern**?

g) **Bonus-Challenge**: Berechne das durchschnittliche Alter der Mitarbeiter pro Abteilung und zeige nur Abteilungen, deren Durchschnittsalter **über 30** liegt.

**Lernziele**: Aggregatfunktionen anwenden; `.groupby()` verwenden; Mehrfache Aggregationen mit `.agg()`.

---

### Aufgabe P4: Performance-Optimierung - Vektorisierung (⭐⭐⭐)

**Kontext**: Du hast einen großen Datensatz mit Verkaufsdaten und möchtest eine neue Spalte mit berechneten Werten hinzufügen.

**Aufgabenstellung**:

a) Erstelle einen DataFrame mit **100.000 Zeilen** und folgenden Spalten:
   - `Produkt_ID`: Fortlaufende IDs von 1 bis 100.000
   - `Preis`: Zufällige Preise zwischen 10 und 1000 (verwende `numpy.random.randint()` oder `random.randint()`)
   - `Anzahl`: Zufällige Anzahlen zwischen 1 und 10

b) **Methode 1 (LANGSAM)**: Berechne den **Gesamtpreis** (Preis × Anzahl) mit einer **for-Schleife** über alle Zeilen (`.iterrows()`). Messe die benötigte Zeit mit `time.time()`.

c) **Methode 2 (SCHNELL)**: Berechne den **Gesamtpreis** mit **Vektorisierung** (direkte Spaltenoperation). Messe die benötigte Zeit.

d) Vergleiche die Laufzeiten und berechne, um welchen **Faktor** die Vektorisierung schneller ist.

e) **Zusatzfrage**: Erkläre in 2-3 Sätzen, warum Vektorisierung so viel schneller ist als Schleifen.

**Lernziele**: Verstehen, warum Schleifen in Pandas langsam sind; Vektorisierung anwenden; Performance messen und vergleichen.

---

### Aufgabe P5: Reale Datenanalyse - E-Commerce-Dashboard (⭐⭐⭐⭐)

**Kontext**: Du arbeitest für einen Online-Shop und sollst ein einfaches Analyse-Dashboard mit Pandas erstellen.

**Datensatz** (`orders.csv`):
```csv
Bestellung_ID,Kunde_ID,Kunde_Name,Produkt,Kategorie,Preis,Anzahl,Datum,Status
1,101,Max Mustermann,Laptop,Elektronik,1200,1,2025-12-01,Abgeschlossen
2,102,Anna Schmidt,Maus,Elektronik,25,2,2025-12-01,Abgeschlossen
3,101,Max Mustermann,Tastatur,Elektronik,75,1,2025-12-02,Abgeschlossen
4,103,Tom Wagner,Monitor,Elektronik,300,1,2025-12-02,Storniert
5,102,Anna Schmidt,Laptop,Elektronik,1200,1,2025-12-03,Abgeschlossen
6,104,Lisa Mueller,Buch,Bücher,15,3,2025-12-03,Abgeschlossen
7,101,Max Mustermann,Monitor,Elektronik,300,2,2025-12-04,Abgeschlossen
8,105,Peter Schulz,Stuhl,Möbel,150,1,2025-12-04,Versandt
9,103,Tom Wagner,Tastatur,Elektronik,75,1,2025-12-05,Abgeschlossen
10,102,Anna Schmidt,Maus,Elektronik,25,3,2025-12-05,Abgeschlossen
11,106,Sarah Klein,Tisch,Möbel,400,1,2025-12-06,Versandt
12,104,Lisa Mueller,Lampe,Möbel,80,2,2025-12-06,Abgeschlossen
```

**Aufgabenstellung**:

a) Erstelle die CSV-Datei und lies sie mit Pandas ein. Konvertiere die Spalte `Datum` in datetime.

b) Füge eine neue Spalte **`Gesamtpreis`** hinzu, die den Gesamtpreis pro Bestellung berechnet (Preis × Anzahl).

c) **Analyse 1 - Umsatz**: Berechne den **Gesamtumsatz** (Summe aller abgeschlossenen Bestellungen). Ignoriere stornierte Bestellungen.

d) **Analyse 2 - Top-Kunden**: Welche 3 Kunden haben den **höchsten Gesamtumsatz**? Zeige Kunde_Name und Gesamtumsatz.

e) **Analyse 3 - Kategorien**: Welche **Produktkategorie** generiert den höchsten Umsatz? Zeige Kategorie und Gesamtumsatz pro Kategorie.

f) **Analyse 4 - Zeitreihe**: Berechne den **täglichen Umsatz** (nur abgeschlossene Bestellungen) und zeige das Ergebnis als Tabelle.

g) **Analyse 5 - Bestellstatus**: Wie viele Bestellungen haben welchen Status? Erstelle eine Zählung.

h) **Analyse 6 - Durchschnitt**: Was ist der **durchschnittliche Bestellwert** (Gesamtpreis pro Bestellung) für abgeschlossene Bestellungen?

i) **Bonus - Visualisierung**: Falls du Matplotlib kennst (aus V13/V14), erstelle ein **Balkendiagramm**, das den Umsatz pro Kategorie zeigt.

**Lernziele**: Komplette Datenanalyse-Pipeline durchführen; Daten filtern, gruppieren und aggregieren; Mehrere Analysen kombinieren; Praktisches Anwendungsbeispiel.

---

**Ende der Übungsaufgaben V16**

Die Lösungen zu diesen Aufgaben findest du in der Datei [V16-Netzwerktechnik-Grundlagen-Protokolle-Teil2_loesungen.md](V16-Netzwerktechnik-Grundlagen-Protokolle-Teil2_loesungen.md).