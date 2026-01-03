# V12: Lösungen - Prompt Engineering & Imports

> [!NOTE]
> Diese Lösungen dienen als Referenz. Deine Lösung kann abweichen und trotzdem korrekt sein.
> Wichtig ist, dass du die Konzepte verstanden hast.

---

## Teil A: Theorie-Lösungen

### Lösung T1: Prompt-Anatomie analysieren

**Analyse des Prompts**:

```
Du bist ein erfahrener Python-Entwickler. Erstelle eine Funktion zur 
Berechnung der Fakultät einer Zahl. Die Funktion soll Type Hints haben, 
einen Docstring im Google Style enthalten und rekursiv implementiert 
sein. Maximale Länge: 15 Zeilen.
```

**1. Kontext**:
Der Kontext ist: **"Du bist ein erfahrener Python-Entwickler."**

Dieser Kontext definiert die Rolle des Modells. Das Modell soll sich wie ein erfahrener Entwickler verhalten, was bedeutet, dass es Best Practices, idiomatischen Code und professionelle Standards anwenden soll.

**2. Aufgabe**:
Die konkrete Aufgabe ist: **"Erstelle eine Funktion zur Berechnung der Fakultät einer Zahl."**

Dies ist die zentrale Aktion, die ausgeführt werden soll. Die Aufgabe ist klar und spezifisch definiert.

**3. Format**:
Das geforderte Format umfasst mehrere Anforderungen:
- Type Hints verwenden
- Docstring im Google Style
- Rekursive Implementierung

Diese Formatvorgaben definieren die strukturellen und stilistischen Eigenschaften der Lösung.

**4. Constraints**:
Der definierte Constraint ist: **"Maximale Länge: 15 Zeilen."**

Diese Einschränkung setzt eine Obergrenze für den Umfang der Lösung und erzwingt Prägnanz.

> [!TIP]
> **Warum ist diese Analyse wichtig?**
> 
> Durch das Zerlegen eines Prompts in seine Komponenten erkennst du:
> - Welche Informationen dem Modell helfen, die Aufgabe zu verstehen (Kontext)
> - Was genau erreicht werden soll (Aufgabe)
> - Wie das Ergebnis strukturiert sein soll (Format)
> - Welche Grenzen gesetzt sind (Constraints)
> 
> Diese vier Komponenten sollten in jedem gut strukturierten Prompt enthalten sein.

**Häufige Fehler**:
- Kontext und Aufgabe verwechseln: Der Kontext beschreibt die Rolle, die Aufgabe die Aktion
- Format mit Constraints verwechseln: Format beschreibt Struktur, Constraints setzen Grenzen
- Implizite Anforderungen übersehen: Hier ist "rekursiv" eine Formatvorgabe, die die Implementierungsart festlegt

---

### Lösung T2: Prompt-Verbesserung

**Ursprünglicher Prompt** (vage):
```
Erkläre Sortieralgorithmen.
```

**Probleme des ursprünglichen Prompts**:
- Kein Kontext (Wer ist die Zielgruppe? Welches Vorwissen?)
- Aufgabe zu allgemein (Welche Sortieralgorithmen? Wie tief?)
- Kein Format (Text? Code? Tabelle? Visualisierung?)
- Keine Constraints (Länge? Komplexität?)

**Verbesserter Prompt**:

```
Du bist ein Informatik-Dozent an einer Hochschule und erklärst Erstsemstern 
im Bachelor Informatik die Grundlagen der Algorithmik. Die Studierenden haben 
bereits Programmierkenntnisse in Python, aber noch keine formale Ausbildung 
in Algorithmik.

Erstelle eine strukturierte Übersicht über die drei grundlegenden 
Sortieralgorithmen Bubble Sort, Insertion Sort und Quick Sort. 

Für jeden Algorithmus:
1. Erkläre die Funktionsweise in maximal 3 Sätzen
2. Gib die Zeit-Komplexität an (Best Case, Average Case, Worst Case)
3. Zeige ein minimales Python-Code-Beispiel (max. 10 Zeilen)
4. Nenne einen praktischen Anwendungsfall

Formatiere die Ausgabe als Markdown-Tabelle mit den Spalten: 
Algorithmus | Funktionsweise | Komplexität | Anwendungsfall

Beschränke die gesamte Ausgabe auf maximal 500 Wörter.
```

**Erklärung der Verbesserungen**:

**Kontext-Ergänzung**:
- Rolle definiert: Informatik-Dozent
- Zielgruppe spezifiziert: Erstsemester mit Python-Kenntnissen
- Vorwissen geklärt: Programmierung ja, Algorithmik nein

Diese Informationen helfen dem Modell, den richtigen Abstraktionslevel zu wählen.

**Aufgaben-Präzisierung**:
- Konkrete Algorithmen genannt (Bubble Sort, Insertion Sort, Quick Sort)
- Vier spezifische Anforderungen pro Algorithmus definiert
- Klare Struktur vorgegeben (1-4 durchnummeriert)

Die Aufgabe ist jetzt messbar und vollständig spezifiziert.

**Format-Definition**:
- Markdown-Tabelle als Ausgabeformat
- Spaltenstruktur vorgegeben
- Code-Beispiele mit Zeilenlimit

Das Format ist präzise und maschinell umsetzbar.

**Constraints gesetzt**:
- Funktionsweise: Max. 3 Sätze
- Code-Beispiele: Max. 10 Zeilen
- Gesamte Ausgabe: Max. 500 Wörter

Diese Einschränkungen verhindern ausufernde Antworten und erzwingen Prägnanz.

> [!TIP]
> **Prompt-Verbesserungs-Checkliste**:
> 
> ✅ Kontext:
> - Ist die Rolle des Modells klar?
> - Ist die Zielgruppe definiert?
> - Ist das Vorwissen spezifiziert?
> 
> ✅ Aufgabe:
> - Ist die Aufgabe konkret und messbar?
> - Sind alle erwarteten Ausgaben aufgelistet?
> - Gibt es eine klare Struktur?
> 
> ✅ Format:
> - Ist das Ausgabeformat definiert (Text, Code, Tabelle, etc.)?
> - Sind Stil und Ton spezifiziert?
> 
> ✅ Constraints:
> - Sind Längen-Limits gesetzt?
> - Sind Komplexitäts-Grenzen definiert?
> - Gibt es Ausschluss-Kriterien?

**Alternative Ansätze**:

Je nach Ziel könnte der Prompt auch anders verbessert werden:

**Für Anfänger mit visueller Präferenz**:
```
Erkläre die drei Sortieralgorithmen Bubble Sort, Insertion Sort und Quick Sort 
mit ASCII-Art-Visualisierungen der Sortierschritte. Zeige für jede Methode 
eine Beispiel-Sortierung des Arrays [64, 34, 25, 12, 22].
```

**Für fortgeschrittene Studierende**:
```
Vergleiche Bubble Sort, Insertion Sort und Quick Sort hinsichtlich ihrer 
Worst-Case-Laufzeit, Cache-Effizienz und Eignung für parallele Verarbeitung. 
Begründe deine Analyse formal mit Komplexitätstheorie.
```

Die Wahl der Verbesserung hängt vom tatsächlichen Bedarf ab.

---

### Lösung T3: Few-Shot Learning Design

**Vollständiger Few-Shot-Prompt**:

```
Du bist ein KI-Assistent für Kundenservice-Automatisierung. 
Deine Aufgabe ist es, aus Kunden-Reviews folgende Informationen zu extrahieren:

1. Sentiment: positiv | neutral | negativ
2. Hauptthema: Produkt | Lieferung | Service | Preis
3. Handlungsempfehlung: keine | Antworten | Eskalieren

Analysiere Reviews und gib die Extraktion im folgenden Format aus:
Sentiment: [Wert] | Thema: [Wert] | Empfehlung: [Wert]

Hier sind drei Beispiele:

---
Review: "Das Produkt ist qualitativ hochwertig und funktioniert einwandfrei. 
Der Preis ist zwar etwas hoch, aber das ist es wert. Bin sehr zufrieden!"

Sentiment: positiv | Thema: Produkt | Empfehlung: keine

---
Review: "Die Lieferung kam 2 Wochen zu spät, und die Verpackung war beschädigt. 
Das Produkt selbst ist okay, aber dieser Service ist inakzeptabel."

Sentiment: negativ | Thema: Lieferung | Empfehlung: Eskalieren

---
Review: "Ich habe eine Frage zur Garantie gestellt, aber noch keine Antwort 
erhalten. Das Produkt funktioniert soweit gut."

Sentiment: neutral | Thema: Service | Empfehlung: Antworten

---
Analysiere nun das folgende Review:
[BENUTZER-EINGABE]
```

**Erklärung der Beispiel-Wahl**:

**Beispiel 1 - Positives Sentiment**:
- Sentiment: Klar positiv ("sehr zufrieden", "hochwertig", "einwandfrei")
- Thema: Produkt (Fokus auf Produktqualität)
- Empfehlung: Keine (zufriedener Kunde, keine Aktion nötig)
- Besonderheit: Erwähnt Preis als Nebenaspekt, aber Hauptthema bleibt Produkt

Dieses Beispiel zeigt dem Modell, dass positive Reviews oft keine Aktion erfordern und wie man das Hauptthema identifiziert, auch wenn mehrere Aspekte erwähnt werden.

**Beispiel 2 - Negatives Sentiment**:
- Sentiment: Klar negativ ("inakzeptabel", "beschädigt", "zu spät")
- Thema: Lieferung (Lieferzeit und Verpackung im Fokus)
- Empfehlung: Eskalieren (schwerwiegendes Problem, Entschädigung/Management-Intervention nötig)
- Besonderheit: Gemischte Erwähnung (Produkt okay, aber Lieferung problematisch)

Dieses Beispiel demonstriert, dass negative Sentiments oft Eskalation erfordern und wie man das Hauptthema bei gemischten Reviews identifiziert.

**Beispiel 3 - Neutrales Sentiment**:
- Sentiment: Neutral (weder lobend noch kritisch, sachlich)
- Thema: Service (unbeantwortete Frage zum Kundenservice)
- Empfehlung: Antworten (aktive Kommunikation erforderlich)
- Besonderheit: Zeigt, dass neutrale Reviews trotzdem Aktion erfordern können

Dieses Beispiel zeigt dem Modell, dass neutrale Reviews oft offene Fragen enthalten, die beantwortet werden müssen, und dass Sentiment und Handlungsempfehlung nicht immer korrelieren.

**Warum diese Beispiele gut funktionieren**:

1. **Abdeckung aller Sentiments**: Positiv, neutral, negativ sind alle vertreten
2. **Vielfältige Themen**: Produkt, Lieferung, Service werden demonstriert
3. **Verschiedene Empfehlungen**: Alle drei Handlungsoptionen werden gezeigt
4. **Edge Cases**: Gemischte Reviews (positives Produkt + negative Lieferung) werden behandelt
5. **Konsistentes Format**: Alle Beispiele folgen exakt demselben Ausgabeformat
6. **Realitätsnähe**: Die Reviews klingen authentisch und repräsentieren echte Kundenszenarien

> [!WARNING]
> **Häufige Fehler bei Few-Shot-Prompts**:
> 
> ❌ **Zu ähnliche Beispiele**: Wenn alle Beispiele sehr ähnlich sind, lernt das Modell nicht zu generalisieren
> ```
> # Schlecht:
> "Das Produkt ist super!" → positiv
> "Das Produkt ist toll!" → positiv
> "Das Produkt ist großartig!" → positiv
> ```
> 
> ❌ **Inkonsistentes Format**: Wenn Beispiele unterschiedliche Formate haben, ist das Modell verwirrt
> ```
> # Schlecht:
> Beispiel 1: "Review: ... | Sentiment: positiv"
> Beispiel 2: "Text: ... Stimmung: gut"
> ```
> 
> ❌ **Keine Edge Cases**: Wenn nur einfache Fälle gezeigt werden, scheitert das Modell bei Komplexität
> ```
> # Schlecht: Nur klare Fälle, keine gemischten Reviews
> ```
> 
> ❌ **Zu viele Beispiele**: Bei Few-Shot sind 3-5 Beispiele optimal, mehr verwirrt oft
> 
> ✅ **Best Practice**: 3-5 diverse, konsistente, realistische Beispiele mit unterschiedlichen Edge Cases

**Alternative Lösungsansätze**:

**Zero-Shot-Ansatz** (ohne Beispiele, nur mit klarer Instruktion):
```
Extrahiere aus Kunden-Reviews: Sentiment (positiv/neutral/negativ), 
Hauptthema (Produkt/Lieferung/Service/Preis), Handlungsempfehlung (keine/Antworten/Eskalieren). 
Format: "Sentiment: X | Thema: Y | Empfehlung: Z"
```

**One-Shot-Ansatz** (ein sehr repräsentatives Beispiel):
```
Beispiel:
Review: "Gutes Produkt, aber Lieferung zu spät."
Sentiment: neutral | Thema: Lieferung | Empfehlung: Antworten

Analysiere nun: [EINGABE]
```

**Chain-of-Thought Few-Shot** (mit Begründung):
```
Review: "Das Produkt ist qualitativ hochwertig..."
Analyse:
- "qualitativ hochwertig", "sehr zufrieden" → Sentiment: positiv
- Fokus auf Produkteigenschaften → Thema: Produkt
- Keine Beschwerde oder offene Frage → Empfehlung: keine
Ergebnis: Sentiment: positiv | Thema: Produkt | Empfehlung: keine
```

Der Chain-of-Thought-Ansatz hilft bei komplexeren Fällen, benötigt aber mehr Tokens.

---

## Teil B: Python-Lösungen

### Lösung P1: Erstes eigenes Modul

**`greetings.py`**:

```python
"""
Modul für Begrüßungs- und Verabschiedungsnachrichten.

Dieses Modul bietet Funktionen für verschiedene Arten von Grußformeln,
sowohl informell als auch formell.
"""

def begruessung(name: str) -> str:
    """Gibt eine informelle Begrüßung zurück."""
    return f"Hallo, {name}!"

def verabschiedung(name: str) -> str:
    """Gibt eine informelle Verabschiedung zurück."""
    return f"Tschüss, {name}!"

def formelle_begruessung(titel: str, nachname: str) -> str:
    """Gibt eine formelle Begrüßung zurück."""
    return f"Guten Tag, {titel} {nachname}"
```

**`main.py`**:

```python
"""
Testprogramm für das greetings-Modul.
"""
import greetings

# Test der informellen Begrüßung
print(greetings.begruessung("Anna"))  # "Hallo, Anna!"

# Test der informellen Verabschiedung
print(greetings.verabschiedung("Max"))  # "Tschüss, Max!"

# Test der formellen Begrüßung
print(greetings.formelle_begruessung("Dr.", "Müller"))  # "Guten Tag, Dr. Müller"
print(greetings.formelle_begruessung("Prof.", "Schmidt"))  # "Guten Tag, Prof. Schmidt"
```

**Erklärung der Lösung**:

**Modul-Docstring**:
Der Modul-Docstring steht in der ersten Zeile der Datei (nach optionalen Shebang/Encoding-Zeilen) und beschreibt den Zweck des Moduls. Er wird angezeigt, wenn jemand `help(greetings)` aufruft.

**Type Hints**:
Jede Funktion hat Type Hints für alle Parameter und den Rückgabewert:
- `name: str` → Parameter ist vom Typ String
- `-> str` → Funktion gibt String zurück

Type Hints sind optional, aber verbessern die Code-Dokumentation und ermöglichen statische Typ-Prüfung mit Tools wie `mypy`.

**Docstrings**:
Jede Funktion hat einen einzeiligen Docstring, der die Funktionalität beschreibt. Bei einfachen Funktionen reicht oft ein Satz.

**f-Strings**:
Die Funktionen nutzen f-Strings für String-Formatierung (bereits in V02 eingeführt). f-Strings sind die moderne, empfohlene Methode für String-Interpolation in Python.

**Import-Stil**:
`import greetings` importiert das gesamte Modul. Der Zugriff erfolgt dann mit `greetings.funktionsname()`. Dies ist der expliziteste und klarste Import-Stil, da immer sichtbar ist, woher eine Funktion kommt.

> [!TIP]
> **Alternative Import-Stile**:
> 
> ```python
> # Variante 1: Gesamtes Modul (wie oben)
> import greetings
> print(greetings.begruessung("Anna"))
> 
> # Variante 2: Spezifische Funktionen
> from greetings import begruessung, verabschiedung
> print(begruessung("Anna"))  # Kürzerer Zugriff
> 
> # Variante 3: Alle Funktionen (nicht empfohlen!)
> from greetings import *
> print(begruessung("Anna"))  # Unklar, woher Funktion kommt
> 
> # Variante 4: Mit Alias
> import greetings as gr
> print(gr.begruessung("Anna"))
> ```
> 
> **Empfehlung**: Variante 1 oder 2, je nach Kontext. Variante 3 (`import *`) nur in interaktiven Sessions verwenden, nie in Production-Code.

**Häufige Fehler**:

❌ **Fehler 1: Modul-Docstring an falscher Stelle**
```python
# Falsch:
def begruessung(name: str) -> str:
    pass

"""Modul für Grußformeln."""  # Zu spät!
```

✅ **Richtig**: Modul-Docstring muss erste Zeile (nach Shebang/Encoding) sein.

❌ **Fehler 2: Type Hints vergessen**
```python
# Unvollständig:
def begruessung(name) -> str:  # Parameter-Typ fehlt
    return f"Hallo, {name}!"
```

✅ **Richtig**: Alle Parameter und Rückgabewerte typisieren.

❌ **Fehler 3: Funktionen im if __name__ Block definieren**
```python
# Falsch:
if __name__ == "__main__":
    def begruessung(name: str) -> str:  # Nicht importierbar!
        return f"Hallo, {name}!"
```

✅ **Richtig**: Funktionen auf Modul-Ebene definieren, nur Tests im `if __name__` Block.

**Warum diese Lösung gut ist**:
- Klare Trennung von Modul-Definition (greetings.py) und Nutzung (main.py)
- Vollständige Dokumentation (Modul-Docstring + Funktions-Docstrings)
- Type Hints für bessere IDE-Unterstützung und Dokumentation
- Einfache, verständliche Funktionen, die eine Aufgabe erfüllen (Single Responsibility Principle)

---

### Lösung P2: `if __name__ == "__main__":` anwenden

**`calculator.py`**:

```python
"""
Einfaches Rechner-Modul mit grundlegenden arithmetischen Operationen.

Dieses Modul kann sowohl als Bibliothek importiert als auch als
eigenständiges Kommandozeilen-Programm ausgeführt werden.
"""

def addiere(a: float, b: float) -> float:
    """
    Addiert zwei Zahlen.
    
    Args:
        a: Erste Zahl
        b: Zweite Zahl
    
    Returns:
        Summe von a und b
    """
    return a + b

def subtrahiere(a: float, b: float) -> float:
    """
    Subtrahiert zwei Zahlen.
    
    Args:
        a: Minuend (Zahl, von der subtrahiert wird)
        b: Subtrahend (Zahl, die subtrahiert wird)
    
    Returns:
        Differenz von a und b
    """
    return a - b

def multipliziere(a: float, b: float) -> float:
    """
    Multipliziert zwei Zahlen.
    
    Args:
        a: Erster Faktor
        b: Zweiter Faktor
    
    Returns:
        Produkt von a und b
    """
    return a * b

def dividiere(a: float, b: float) -> float:
    """
    Dividiert zwei Zahlen.
    
    Args:
        a: Dividend (Zahl, die geteilt wird)
        b: Divisor (Zahl, durch die geteilt wird)
    
    Returns:
        Quotient von a und b
    
    Raises:
        ZeroDivisionError: Wenn b gleich 0 ist
    """
    if b == 0:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt")
    return a / b

# Dieser Block wird nur ausgeführt, wenn das Modul direkt gestartet wird,
# nicht wenn es importiert wird
if __name__ == "__main__":
    print("=== Einfacher Rechner ===")
    print("Gib zwei Zahlen und eine Operation ein.\n")
    
    try:
        # Benutzereingaben einlesen
        erste_zahl = float(input("Erste Zahl: "))
        zweite_zahl = float(input("Zweite Zahl: "))
        operation = input("Operation (+, -, *, /): ")
        
        # Operation ausführen
        if operation == "+":
            ergebnis = addiere(erste_zahl, zweite_zahl)
        elif operation == "-":
            ergebnis = subtrahiere(erste_zahl, zweite_zahl)
        elif operation == "*":
            ergebnis = multipliziere(erste_zahl, zweite_zahl)
        elif operation == "/":
            ergebnis = dividiere(erste_zahl, zweite_zahl)
        else:
            print(f"Ungültige Operation: {operation}")
            exit(1)
        
        # Ergebnis ausgeben
        print(f"Ergebnis: {ergebnis}")
    
    except ValueError:
        print("Fehler: Bitte gib gültige Zahlen ein.")
    except ZeroDivisionError as e:
        print(f"Fehler: {e}")
    except KeyboardInterrupt:
        print("\nProgramm abgebrochen.")
```

**Nutzung als Skript**:

```bash
$ python calculator.py
=== Einfacher Rechner ===
Gib zwei Zahlen und eine Operation ein.

Erste Zahl: 10
Zweite Zahl: 5
Operation (+, -, *, /): *
Ergebnis: 50.0
```

**Nutzung als Modul (import_test.py)**:

```python
"""
Test-Programm, das calculator als Bibliothek nutzt.
"""
from calculator import multipliziere, dividiere

# Verwende calculator-Funktionen in eigenem Code
preis = 19.99
menge = 3
gesamt = multipliziere(preis, menge)
print(f"Gesamtpreis: {gesamt:.2f} EUR")  # Gesamtpreis: 59.97 EUR

# Division mit Error Handling
try:
    result = dividiere(100, 0)
except ZeroDivisionError as e:
    print(f"Fehler bei Division: {e}")
```

**Erklärung der Lösung**:

**`if __name__ == "__main__":`-Pattern**:
Dieses Pattern ist der Schlüssel zur Doppelnutzung als Skript und Bibliothek.

**Wie funktioniert es?**
- Wenn Python eine Datei direkt ausführt: `__name__ = "__main__"`
- Wenn Python eine Datei importiert: `__name__ = "calculator"` (Modulname)

Der `if __name__ == "__main__":` Block wird also nur ausgeführt, wenn das Modul direkt gestartet wird, nicht bei Import.

**Detaillierte Analyse**:

```python
if __name__ == "__main__":
    # Dieser Code läuft nur bei:
    # $ python calculator.py
    
    # Aber NICHT bei:
    # from calculator import addiere
```

**Warum ist das nützlich?**
1. **Wiederverwendbarkeit**: Funktionen können in anderen Programmen importiert werden
2. **Testbarkeit**: Interaktive Tests können direkt im Modul-Skript stehen
3. **Dokumentation durch Beispiele**: Der `if __name__` Block zeigt Beispiel-Nutzung
4. **Keine Seiteneffekte bei Import**: Code läuft nicht versehentlich beim Import

**Error Handling in `dividiere()`**:
Die Funktion wirft explizit einen `ZeroDivisionError`, falls durch Null geteilt wird. Dies ist Best Practice:
- Fehler werden früh erkannt (Fail Fast)
- Die Fehlermeldung ist klar und hilfreich
- Der Aufrufer kann den Fehler mit `try-except` behandeln

**Error Handling im `if __name__` Block**:
Drei verschiedene Exceptions werden abgefangen:
1. `ValueError`: Bei ungültigen Zahlen-Eingaben (z.B. "abc")
2. `ZeroDivisionError`: Bei Division durch Null
3. `KeyboardInterrupt`: Bei Strg+C (sauberer Abbruch)

Dies zeigt professionelles Error Handling: Unterschiedliche Fehlertypen werden unterschiedlich behandelt.

> [!WARNING]
> **Häufige Fehler mit `if __name__ == "__main__":`**:
> 
> ❌ **Fehler 1: Falsche String-Schreibweise**
> ```python
> if __name__ == '__main__':  # Funktioniert, aber...
>     pass
> # Besser: Doppelte Anführungszeichen für Konsistenz
> if __name__ == "__main__":
>     pass
> ```
> 
> ❌ **Fehler 2: Funktionen im if-Block definieren**
> ```python
> if __name__ == "__main__":
>     def addiere(a, b):  # FALSCH! Nicht importierbar!
>         return a + b
> ```
> ✅ **Richtig**: Funktionen außerhalb definieren, nur Ausführungs-Code im Block
> 
> ❌ **Fehler 3: if-Block vergessen**
> ```python
> # Datei ohne if __name__:
> print("Rechner gestartet")  # Wird IMMER ausgeführt, auch bei Import!
> ```
> ✅ **Richtig**: Test-/Interaktions-Code immer in `if __name__` Block

**Warum diese Lösung gut ist**:
- Vollständige Docstrings im Google Style mit Args, Returns, Raises
- Sauberes Error Handling mit aussagekräftigen Fehlermeldungen
- Korrekte Verwendung des `if __name__ == "__main__":` Patterns
- Das Modul ist sowohl als Bibliothek als auch als eigenständiges Programm nutzbar
- Alle Funktionen sind einfach testbar

---

### Lösung P3: Package-Struktur aufbauen

**Verzeichnisstruktur**:
```
text_tools/
├── __init__.py
├── formatters.py
└── validators.py
main.py
```

**`text_tools/__init__.py`**:

```python
"""
text_tools Package - Werkzeuge für Textverarbeitung und -validierung.

Dieses Package bietet Funktionen zum Formatieren und Validieren von Text.
"""

# Importiere alle Funktionen aus den Submodulen
from .formatters import upper_first, snake_case
from .validators import ist_email_gueltig, ist_passwort_sicher

# Definiere, welche Namen bei `from text_tools import *` verfügbar sind
__all__ = [
    'upper_first',
    'snake_case',
    'ist_email_gueltig',
    'ist_passwort_sicher'
]
```

**`text_tools/formatters.py`**:

```python
"""
Formatierungs-Funktionen für Text.
"""

def upper_first(text: str) -> str:
    """
    Macht den ersten Buchstaben des Textes groß.
    
    Args:
        text: Eingabetext
    
    Returns:
        Text mit großem ersten Buchstaben
    
    Examples:
        >>> upper_first("hallo")
        'Hallo'
        >>> upper_first("WELT")
        'WELT'
    """
    if not text:
        return text
    return text[0].upper() + text[1:]

def snake_case(text: str) -> str:
    """
    Konvertiert Text zu snake_case.
    
    Ersetzt Leerzeichen durch Unterstriche und konvertiert zu Kleinbuchstaben.
    
    Args:
        text: Eingabetext
    
    Returns:
        Text in snake_case Format
    
    Examples:
        >>> snake_case("Hello World")
        'hello_world'
        >>> snake_case("Python Programming")
        'python_programming'
    """
    return text.replace(" ", "_").lower()
```

**`text_tools/validators.py`**:

```python
"""
Validierungs-Funktionen für Text und Eingaben.
"""

def ist_email_gueltig(email: str) -> bool:
    """
    Prüft, ob eine E-Mail-Adresse gültig ist (einfache Validierung).
    
    Diese Funktion führt eine grundlegende Validierung durch:
    - Enthält genau ein @-Zeichen
    - Hat Text vor und nach dem @
    - Hat mindestens einen Punkt nach dem @
    
    Args:
        email: Zu prüfende E-Mail-Adresse
    
    Returns:
        True wenn gültig, False sonst
    
    Examples:
        >>> ist_email_gueltig("test@example.com")
        True
        >>> ist_email_gueltig("invalid.email")
        False
        >>> ist_email_gueltig("@example.com")
        False
    """
    # Prüfe, ob genau ein @ vorhanden ist
    if email.count("@") != 1:
        return False
    
    # Teile an @ auf
    local, domain = email.split("@")
    
    # Prüfe, ob beide Teile nicht leer sind
    if not local or not domain:
        return False
    
    # Prüfe, ob Domain mindestens einen Punkt hat
    if "." not in domain:
        return False
    
    return True

def ist_passwort_sicher(passwort: str) -> bool:
    """
    Prüft, ob ein Passwort grundlegende Sicherheitskriterien erfüllt.
    
    Kriterien:
    - Mindestens 8 Zeichen lang
    - Mindestens ein Großbuchstabe
    - Mindestens eine Ziffer
    
    Args:
        passwort: Zu prüfendes Passwort
    
    Returns:
        True wenn sicher, False sonst
    
    Examples:
        >>> ist_passwort_sicher("Passwort1")
        True
        >>> ist_passwort_sicher("kurz")
        False
        >>> ist_passwort_sicher("langohnenummer")
        False
    """
    # Prüfe Länge
    if len(passwort) < 8:
        return False
    
    # Prüfe, ob mindestens ein Großbuchstabe vorhanden ist
    hat_grossbuchstaben = any(c.isupper() for c in passwort)
    if not hat_grossbuchstaben:
        return False
    
    # Prüfe, ob mindestens eine Ziffer vorhanden ist
    hat_ziffer = any(c.isdigit() for c in passwort)
    if not hat_ziffer:
        return False
    
    return True
```

**`main.py`**:

```python
"""
Test-Programm für das text_tools Package.
"""
from text_tools import upper_first, snake_case, ist_email_gueltig, ist_passwort_sicher

print("=== Formatierungs-Tests ===")

# Test upper_first
print(upper_first("hallo"))  # "Hallo"
print(upper_first("python"))  # "Python"
print(upper_first(""))  # ""

# Test snake_case
print(snake_case("Hello World"))  # "hello_world"
print(snake_case("Python Programming Language"))  # "python_programming_language"

print("\n=== Validierungs-Tests ===")

# Test ist_email_gueltig
print(ist_email_gueltig("test@example.com"))  # True
print(ist_email_gueltig("invalid.email"))  # False
print(ist_email_gueltig("@example.com"))  # False
print(ist_email_gueltig("test@@example.com"))  # False

# Test ist_passwort_sicher
print(ist_passwort_sicher("Passwort1"))  # True
print(ist_passwort_sicher("kurz"))  # False
print(ist_passwort_sicher("langeohnegrossbuchstaben1"))  # False
print(ist_passwort_sicher("LangOhneZiffer"))  # False
```

**Ausgabe von `main.py`**:
```
=== Formatierungs-Tests ===
Hallo
Python

hello_world
python_programming_language

=== Validierungs-Tests ===
True
False
False
False
True
False
False
False
```

**Erklärung der Lösung**:

**Package-Struktur**:
Ein Python-Package ist ein Verzeichnis mit einer `__init__.py` Datei. Diese Datei macht das Verzeichnis zu einem Package und definiert, was beim Import verfügbar ist.

**`__init__.py` - Die zentrale Rolle**:

```python
from .formatters import upper_first, snake_case
```

Der Punkt `.` vor `formatters` bedeutet "relatives Import aus dem aktuellen Package". Dies ist wichtig, damit die Imports auch funktionieren, wenn das Package in ein größeres Projekt eingebunden wird.

```python
__all__ = ['upper_first', 'snake_case', ...]
```

`__all__` definiert, welche Namen bei `from text_tools import *` verfügbar sind. Dies ist Best Practice zur Kontrolle der Package-API.

**Warum funktioniert `from text_tools import upper_first`?**

Durch die Imports in `__init__.py` sind die Funktionen direkt im Package-Namespace verfügbar:

```python
# Funktioniert wegen __init__.py:
from text_tools import upper_first

# Wäre sonst nötig:
from text_tools.formatters import upper_first
```

Die erste Variante ist nutzerfreundlicher und versteckt die interne Struktur.

**Implementierungs-Details**:

**`upper_first()` - Edge Case Handling**:
```python
if not text:
    return text
```
Diese Prüfung verhindert einen `IndexError` bei leerem String.

**`ist_email_gueltig()` - Schritt-für-Schritt-Validierung**:
Die Funktion prüft schrittweise:
1. Genau ein @ vorhanden
2. Aufsplitten in Local- und Domain-Teil
3. Beide Teile nicht leer
4. Domain hat mindestens einen Punkt

Diese schrittweise Validierung ist klarer als ein komplexer Regex und ausreichend für grundlegende Prüfungen.

**`ist_passwort_sicher()` - Verwendung von `any()`**:
```python
hat_grossbuchstaben = any(c.isupper() for c in passwort)
```
`any()` mit Generator Expression ist idiomatisches Python für "mindestens ein Element erfüllt Bedingung".

> [!TIP]
> **Package-Design Best Practices**:
> 
> 1. **Flache vs. tiefe Hierarchie**:
>    ```
>    # Gut für kleine Packages:
>    text_tools/
>    ├── __init__.py
>    ├── formatters.py
>    └── validators.py
>    
>    # Gut für große Packages:
>    text_tools/
>    ├── __init__.py
>    ├── formatters/
>    │   ├── __init__.py
>    │   ├── case.py
>    │   └── whitespace.py
>    └── validators/
>        ├── __init__.py
>        ├── email.py
>        └── password.py
>    ```
> 
> 2. **__all__ pflegen**: Definiere explizit, was öffentlich ist
> 
> 3. **Relative Imports in Packages**: Nutze `.` für Imports innerhalb des Packages
> 
> 4. **Dokumentation**: Package-Docstring in `__init__.py` beschreibt das gesamte Package

**Häufige Fehler**:

❌ **Fehler 1: __init__.py vergessen**
```
text_tools/  # Kein __init__.py → kein Package!
├── formatters.py
└── validators.py
```
→ `ImportError: No module named 'text_tools'`

❌ **Fehler 2: Absolute Imports in Package**
```python
# In __init__.py:
from formatters import upper_first  # Falsch!
```
→ `ImportError: No module named 'formatters'`

✅ **Richtig**: Relative Imports mit Punkt
```python
from .formatters import upper_first
```

❌ **Fehler 3: Zirkuläre Imports**
```python
# formatters.py:
from .validators import ist_email_gueltig

# validators.py:
from .formatters import snake_case  # Fehler!
```

✅ **Lösung**: Gemeinsame Funktionen in separates Modul auslagern oder Imports in Funktionen verschieben

**Warum diese Lösung gut ist**:
- Klare Package-Struktur mit logischer Aufteilung (Formatierung vs. Validierung)
- Vollständige Dokumentation mit Examples in Docstrings
- Nutzerfreundliche API durch `__init__.py` (Funktionen direkt aus Package importierbar)
- Robustes Error Handling (Edge Cases wie leere Strings werden behandelt)
- Idiomatisches Python (`any()`, Generator Expressions)

---

### Lösung P4: Relative und absolute Imports

**Verzeichnisstruktur**:
```
data_processing/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── reader.py
│   └── writer.py
└── utils/
    ├── __init__.py
    ├── validators.py
    └── transformers.py
main.py
test.txt  (Test-Datei)
```

**`data_processing/__init__.py`**:

```python
"""
data_processing Package - Werkzeuge für Datenverarbeitung.

Dieses Package bietet Funktionalitäten zum Lesen, Schreiben,
Validieren und Transformieren von Textdaten.
"""

# Package-Version
__version__ = '1.0.0'

# Importiere wichtigste Funktionen für direkten Zugriff
from .core.reader import lese_zeilen
from .core.writer import schreibe_zeilen
from .utils.transformers import filtere_leere_zeilen, zu_grossbuchstaben

__all__ = [
    'lese_zeilen',
    'schreibe_zeilen',
    'filtere_leere_zeilen',
    'zu_grossbuchstaben'
]
```

**`data_processing/core/__init__.py`**:

```python
"""
Core-Modul für grundlegende I/O-Operationen.
"""

from .reader import lese_zeilen
from .writer import schreibe_zeilen

__all__ = ['lese_zeilen', 'schreibe_zeilen']
```

**`data_processing/core/reader.py`**:

```python
"""
Funktionen zum Lesen von Dateien.
"""

def lese_zeilen(dateiname: str) -> list[str]:
    """
    Liest eine Datei zeilenweise ein.
    
    Args:
        dateiname: Pfad zur Datei
    
    Returns:
        Liste aller Zeilen (mit Zeilenumbrüchen)
    
    Raises:
        FileNotFoundError: Wenn Datei nicht existiert
        PermissionError: Wenn keine Leseberechtigung
    
    Examples:
        >>> zeilen = lese_zeilen("test.txt")
        >>> len(zeilen)
        5
    """
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            return datei.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Datei '{dateiname}' wurde nicht gefunden")
    except PermissionError:
        raise PermissionError(f"Keine Leseberechtigung für '{dateiname}'")
```

**`data_processing/core/writer.py`**:

```python
"""
Funktionen zum Schreiben von Dateien.
"""

def schreibe_zeilen(dateiname: str, zeilen: list[str]) -> None:
    """
    Schreibt Zeilen in eine Datei.
    
    Args:
        dateiname: Pfad zur Zieldatei
        zeilen: Liste von Zeilen zum Schreiben
    
    Raises:
        PermissionError: Wenn keine Schreibberechtigung
        OSError: Bei anderen I/O-Fehlern
    
    Examples:
        >>> schreibe_zeilen("output.txt", ["Zeile 1\n", "Zeile 2\n"])
    """
    try:
        with open(dateiname, 'w', encoding='utf-8') as datei:
            datei.writelines(zeilen)
    except PermissionError:
        raise PermissionError(f"Keine Schreibberechtigung für '{dateiname}'")
    except OSError as e:
        raise OSError(f"Fehler beim Schreiben in '{dateiname}': {e}")
```

**`data_processing/utils/__init__.py`**:

```python
"""
Utilities-Modul für Validierung und Transformation.
"""

from .validators import ist_nicht_leer
from .transformers import filtere_leere_zeilen, zu_grossbuchstaben

__all__ = ['ist_nicht_leer', 'filtere_leere_zeilen', 'zu_grossbuchstaben']
```

**`data_processing/utils/validators.py`**:

```python
"""
Validierungs-Funktionen für Textdaten.
"""

def ist_nicht_leer(zeile: str) -> bool:
    """
    Prüft, ob eine Zeile nicht leer ist.
    
    Eine Zeile gilt als nicht leer, wenn sie nach Entfernen von
    Whitespace-Zeichen (Leerzeichen, Tabs, Newlines) noch Zeichen enthält.
    
    Args:
        zeile: Zu prüfende Zeile
    
    Returns:
        True wenn Zeile nicht leer, False sonst
    
    Examples:
        >>> ist_nicht_leer("Hallo")
        True
        >>> ist_nicht_leer("   ")
        False
        >>> ist_nicht_leer("\n")
        False
    """
    return bool(zeile.strip())
```

**`data_processing/utils/transformers.py`**:

```python
"""
Transformations-Funktionen für Textdaten.

Dieses Modul nutzt RELATIVE IMPORTS für Package-interne Dependencies.
"""

# RELATIVER IMPORT: Importiert aus dem selben Package (utils)
from .validators import ist_nicht_leer

def filtere_leere_zeilen(zeilen: list[str]) -> list[str]:
    """
    Filtert leere Zeilen aus einer Liste.
    
    Args:
        zeilen: Liste von Zeilen
    
    Returns:
        Liste ohne leere Zeilen
    
    Examples:
        >>> filtere_leere_zeilen(["Hallo\n", "  \n", "Welt\n"])
        ['Hallo\n', 'Welt\n']
    """
    # Nutzt ist_nicht_leer aus validators.py (via relativen Import)
    return [zeile for zeile in zeilen if ist_nicht_leer(zeile)]

def zu_grossbuchstaben(zeilen: list[str]) -> list[str]:
    """
    Konvertiert alle Zeilen zu Großbuchstaben.
    
    Args:
        zeilen: Liste von Zeilen
    
    Returns:
        Liste mit Zeilen in Großbuchstaben
    
    Examples:
        >>> zu_grossbuchstaben(["hallo\n", "welt\n"])
        ['HALLO\n', 'WELT\n']
    """
    return [zeile.upper() for zeile in zeilen]
```

**`main.py`** (Hauptprogramm mit ABSOLUTEN IMPORTS):

```python
"""
Hauptprogramm zur Demonstration von absoluten Imports.

Dieses Programm nutzt ABSOLUTE IMPORTS aus dem data_processing Package.
"""

# ABSOLUTE IMPORTS: Vollständiger Pfad vom Package-Root
from data_processing.core.reader import lese_zeilen
from data_processing.core.writer import schreibe_zeilen
from data_processing.utils.transformers import filtere_leere_zeilen, zu_grossbuchstaben

def main():
    """Hauptfunktion zur Datenverarbeitung."""
    eingabe_datei = "test.txt"
    ausgabe_datei = "output.txt"
    
    try:
        # Schritt 1: Datei einlesen
        print(f"Lese Datei: {eingabe_datei}")
        zeilen = lese_zeilen(eingabe_datei)
        print(f"  → {len(zeilen)} Zeilen gelesen")
        
        # Schritt 2: Leere Zeilen filtern
        print("Filtere leere Zeilen...")
        gefiltert = filtere_leere_zeilen(zeilen)
        print(f"  → {len(gefiltert)} Zeilen nach Filterung")
        
        # Schritt 3: Zu Großbuchstaben konvertieren
        print("Konvertiere zu Großbuchstaben...")
        gross = zu_grossbuchstaben(gefiltert)
        
        # Schritt 4: In neue Datei schreiben
        print(f"Schreibe in Datei: {ausgabe_datei}")
        schreibe_zeilen(ausgabe_datei, gross)
        print("✅ Verarbeitung abgeschlossen!")
        
    except FileNotFoundError as e:
        print(f"❌ Fehler: {e}")
        print("Erstelle Test-Datei...")
        test_zeilen = [
            "Hallo Welt\n",
            "\n",
            "Python Programmierung\n",
            "   \n",
            "Imports und Module\n"
        ]
        schreibe_zeilen(eingabe_datei, test_zeilen)
        print(f"✅ Test-Datei '{eingabe_datei}' erstellt. Führe Programm erneut aus.")
    
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    main()
```

**Test-Datei erstellen (test.txt)**:
```
Hallo Welt

Python Programmierung
   
Imports und Module
Datenverarbeitung
```

**Ausführung**:
```bash
$ python main.py
Lese Datei: test.txt
  → 6 Zeilen gelesen
Filtere leere Zeilen...
  → 4 Zeilen nach Filterung
Konvertiere zu Großbuchstaben...
Schreibe in Datei: output.txt
✅ Verarbeitung abgeschlossen!
```

**Ergebnis (output.txt)**:
```
HALLO WELT
PYTHON PROGRAMMIERUNG
IMPORTS UND MODULE
DATENVERARBEITUNG
```

**Erklärung der Lösung**:

**Relative vs. Absolute Imports**:

**Relativer Import in `transformers.py`**:
```python
from .validators import ist_nicht_leer
```
- Der Punkt `.` bedeutet "aktuelles Package" (hier: `utils`)
- Funktioniert nur innerhalb des Packages
- Vorteil: Package kann umbenannt werden, Imports bleiben gültig
- Nachteil: Nur in Packages nutzbar, nicht in Standalone-Skripten

**Absoluter Import in `main.py`**:
```python
from data_processing.core.reader import lese_zeilen
```
- Vollständiger Pfad vom Package-Root
- Funktioniert überall (innerhalb und außerhalb des Packages)
- Vorteil: Klar und eindeutig, keine Mehrdeutigkeit
- Nachteil: Bei Package-Umbenennung müssen alle Imports angepasst werden

**Faustregel**:
- **Innerhalb eines Packages**: Relative Imports (`.`, `..`)
- **Von außen/Main-Skript**: Absolute Imports
- **Bei Unsicherheit**: Absolute Imports (expliziter)

**Import-Syntax Übersicht**:

```python
# Relative Imports (nur innerhalb von Packages)
from .module import func          # Gleiches Package
from ..other import func          # Parent-Package
from ..sibling.module import func # Geschwister-Package

# Absolute Imports (überall)
from package.module import func
import package.module
```

**Package-Hierarchie visualisiert**:

```
data_processing/           ← Package-Root
├── __init__.py            ← "data_processing" Package
├── core/                  ← Sub-Package
│   ├── __init__.py        ← "data_processing.core" Package
│   ├── reader.py          ← Modul "data_processing.core.reader"
│   └── writer.py          ← Modul "data_processing.core.writer"
└── utils/                 ← Sub-Package
    ├── __init__.py        ← "data_processing.utils" Package
    ├── validators.py      ← Modul "data_processing.utils.validators"
    └── transformers.py    ← Modul "data_processing.utils.transformers"
```

**Warum `__init__.py` in jedem Verzeichnis?**
- Macht Verzeichnis zu einem Python-Package
- Erlaubt Imports aus dem Verzeichnis
- Kann öffentliche API des Packages definieren
- Kann Initialisierungscode enthalten

**Design-Entscheidungen erklärt**:

**1. Separation of Concerns**:
- `core/`: Grundlegende I/O-Operationen (Lesen/Schreiben)
- `utils/`: Höherstufige Operationen (Validierung/Transformation)

Diese Trennung erlaubt:
- Einfaches Testen jedes Moduls separat
- Wiederverwendung in anderen Projekten
- Klare Verantwortlichkeiten

**2. Error Handling in reader.py/writer.py**:
Spezifische Exceptions mit hilfreichen Meldungen:
```python
except FileNotFoundError:
    raise FileNotFoundError(f"Datei '{dateiname}' wurde nicht gefunden")
```
Dies gibt besseren Kontext als die Original-Exception.

**3. Encoding-Parameter**:
```python
with open(dateiname, 'r', encoding='utf-8') as datei:
```
UTF-8 explizit setzen verhindert Encoding-Probleme auf verschiedenen Systemen.

**4. List Comprehensions in transformers.py**:
```python
[zeile for zeile in zeilen if ist_nicht_leer(zeile)]
```
Pythonic und effizienter als explizite for-Schleife mit append.

> [!TIP]
> **Best Practices für Package-Struktur**:
> 
> **Do's:**
> ✅ Verwende relative Imports innerhalb des Packages
> ✅ Definiere `__all__` in `__init__.py` für klare Public API
> ✅ Dokumentiere Package-Hierarchie in Docstrings
> ✅ Halte Module klein und fokussiert (Single Responsibility)
> ✅ Nutze aussagekräftige Namen (core, utils, helpers, etc.)
> 
> **Don'ts:**
> ❌ Vermeide zirkuläre Imports (A importiert B, B importiert A)
> ❌ Keine `import *` in Production-Code
> ❌ Keine zu tiefe Verschachtelung (max. 2-3 Ebenen)
> ❌ Keine gemischten relativen/absoluten Imports im selben Modul

**Häufige Fehler**:

❌ **Fehler 1: Relativer Import im Main-Skript**
```python
# main.py (Top-Level-Skript)
from .reader import lese_zeilen  # ImportError!
```
→ Relative Imports funktionieren nur in Packages, nicht in Top-Level-Skripten

❌ **Fehler 2: Falscher relativer Import**
```python
# In transformers.py (utils/transformers.py)
from ..validators import ist_nicht_leer  # Falsch! validators ist im selben Verzeichnis
```
✅ **Richtig**: `from .validators import ...` (ein Punkt)

❌ **Fehler 3: __init__.py fehlt**
```
data_processing/
├── core/
│   ├── reader.py      # Kein __init__.py!
│   └── writer.py
```
→ `ImportError: No module named 'data_processing.core'`

❌ **Fehler 4: Package-Name kollidiert mit Standard-Library**
```python
# Schlechter Package-Name:
email/           # Kollidiert mit Python's email-Modul!
├── __init__.py
└── sender.py
```

**Warum diese Lösung gut ist**:
- Klare Trennung zwischen Core-Funktionalität und Utilities
- Korrekte Verwendung von relativen Imports innerhalb des Packages
- Korrekte Verwendung von absoluten Imports im Main-Skript
- Robustes Error Handling mit hilfreichen Fehlermeldungen
- Gut strukturierte `__init__.py` Dateien für klare Public API
- Vollständige Dokumentation mit Examples
- Praktisches Beispiel zeigt realen Anwendungsfall (Datenverarbeitung)

---

### Lösung P5: Modul mit venv und Dependencies

**Projekt-Struktur**:
```
weather_cli/
├── venv/                    # Virtuelle Umgebung (git-ignored)
├── weather_cli/             # Package-Verzeichnis
│   ├── __init__.py
│   ├── api.py               # Mock-API für Wetterdaten
│   ├── formatter.py         # Formatierung der Ausgabe
│   └── cli.py               # Command-Line Interface
├── tests/                   # Test-Verzeichnis
│   ├── __init__.py
│   └── test_formatter.py    # Unit-Tests (Bonus)
├── .gitignore               # Git-Ignore-Datei
├── requirements.txt         # Dependencies
├── README.md                # Projektdokumentation
└── main.py                  # Einstiegspunkt
```

**Setup-Schritte** (vor der Implementierung):

```bash
# 1. Virtuelle Umgebung erstellen
python -m venv venv

# 2. Virtuelle Umgebung aktivieren
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Dependencies installieren (nach Erstellung von requirements.txt)
pip install -r requirements.txt

# 4. Programm ausführen
python main.py --stadt Berlin
```

**`.gitignore`**:

```gitignore
# Virtuelle Umgebung
venv/
env/
ENV/

# Python Cache
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Tests
.pytest_cache/
.coverage
htmlcov/

# Build
build/
dist/
*.egg-info/
```

**`requirements.txt`**:

```txt
requests==2.31.0
```

**Für Bonus (Tests)**:
```txt
requests==2.31.0
pytest==7.4.3
```

**`weather_cli/__init__.py`**:

```python
"""
Weather CLI - Ein einfaches Kommandozeilen-Tool für Wetterinformationen.

Dieses Package demonstriert:
- Verwendung externer Dependencies (requests)
- Package-Struktur
- Virtuelle Umgebungen
- Command-Line Interfaces mit argparse
"""

__version__ = '1.0.0'
__author__ = 'Dein Name'

from .api import hole_wetter
from .formatter import formatiere_wetter
from .cli import main

__all__ = ['hole_wetter', 'formatiere_wetter', 'main']
```

**`weather_cli/api.py`**:

```python
"""
API-Modul für Wetterdaten.

In einer realen Anwendung würde dieses Modul eine echte Wetter-API aufrufen.
Für diese Übung verwenden wir Mock-Daten.
"""

import requests
from typing import Dict, Optional

def hole_wetter(stadt: str) -> Dict[str, any]:
    """
    Ruft Wetterdaten für eine Stadt ab.
    
    HINWEIS: Dies ist eine Mock-Implementation für Übungszwecke.
    In einer realen Anwendung würde hier ein API-Call zu einem
    Wetterdienst wie OpenWeatherMap erfolgen.
    
    Args:
        stadt: Name der Stadt
    
    Returns:
        Dictionary mit Wetterdaten:
        - stadt (str): Stadtname
        - temperatur (int): Temperatur in °C
        - bedingungen (str): Wetterbedingungen
        - luftfeuchtigkeit (int): Luftfeuchtigkeit in %
        - wind (int): Windgeschwindigkeit in km/h
    
    Raises:
        ValueError: Wenn Stadt leer ist
    
    Examples:
        >>> wetter = hole_wetter("Berlin")
        >>> wetter['stadt']
        'Berlin'
        >>> wetter['temperatur']
        20
    """
    if not stadt or not stadt.strip():
        raise ValueError("Stadt darf nicht leer sein")
    
    # Mock-Daten basierend auf Stadt (simuliert verschiedene Wetterbedingungen)
    stadt = stadt.strip().capitalize()
    
    # Einfache Hash-Funktion für konsistente, aber variierende Mock-Daten
    stadt_hash = sum(ord(c) for c in stadt) % 5
    
    bedingungen_optionen = ["Sonnig", "Bewölkt", "Regnerisch", "Neblig", "Windig"]
    temperatur_basis = [22, 15, 12, 18, 25]
    luftfeuchtigkeit_basis = [45, 70, 85, 90, 40]
    wind_basis = [10, 15, 20, 5, 30]
    
    # Simuliere API-Call (requests würde hier verwendet werden)
    # Beispiel für echten API-Call (auskommentiert):
    # API_KEY = "dein_api_key"
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={API_KEY}&units=metric&lang=de"
    # try:
    #     response = requests.get(url, timeout=10)
    #     response.raise_for_status()
    #     data = response.json()
    #     return {
    #         "stadt": data["name"],
    #         "temperatur": round(data["main"]["temp"]),
    #         "bedingungen": data["weather"][0]["description"],
    #         "luftfeuchtigkeit": data["main"]["humidity"],
    #         "wind": round(data["wind"]["speed"] * 3.6)
    #     }
    # except requests.RequestException as e:
    #     raise ConnectionError(f"Fehler beim Abrufen der Wetterdaten: {e}")
    
    # Mock-Daten zurückgeben
    return {
        "stadt": stadt,
        "temperatur": temperatur_basis[stadt_hash],
        "bedingungen": bedingungen_optionen[stadt_hash],
        "luftfeuchtigkeit": luftfeuchtigkeit_basis[stadt_hash],
        "wind": wind_basis[stadt_hash]
    }

def check_api_verfuegbar() -> bool:
    """
    Prüft, ob die requests-Library verfügbar ist.
    
    Returns:
        True wenn requests importiert werden kann, False sonst
    """
    try:
        import requests
        return True
    except ImportError:
        return False
```

**`weather_cli/formatter.py`**:

```python
"""
Formatierungs-Modul für Wetterausgaben.
"""

from typing import Dict

def formatiere_wetter(wetter: Dict[str, any]) -> str:
    """
    Formatiert Wetterdaten als lesbaren Text.
    
    Args:
        wetter: Dictionary mit Wetterdaten (von hole_wetter())
    
    Returns:
        Formatierter String mit Wetterinformationen
    
    Raises:
        KeyError: Wenn erforderliche Schlüssel fehlen
        TypeError: Wenn wetter nicht vom Typ dict ist
    
    Examples:
        >>> wetter = {"stadt": "Berlin", "temperatur": 20, "bedingungen": "Sonnig", 
        ...           "luftfeuchtigkeit": 45, "wind": 10}
        >>> print(formatiere_wetter(wetter))
        ╔════════════════════════════════════════╗
        ║  Wetter in Berlin                      ║
        ╠════════════════════════════════════════╣
        ║  🌡️  Temperatur:     20°C              ║
        ║  ☁️  Bedingungen:    Sonnig            ║
        ║  💧  Luftfeuchtigkeit: 45%             ║
        ║  💨  Wind:           10 km/h           ║
        ╚════════════════════════════════════════╝
    """
    if not isinstance(wetter, dict):
        raise TypeError("Wetter muss ein Dictionary sein")
    
    # Prüfe erforderliche Schlüssel
    erforderliche_keys = ["stadt", "temperatur", "bedingungen", "luftfeuchtigkeit", "wind"]
    for key in erforderliche_keys:
        if key not in wetter:
            raise KeyError(f"Erforderlicher Schlüssel '{key}' fehlt in Wetterdaten")
    
    # Wähle Emoji basierend auf Bedingungen
    bedingung = wetter["bedingungen"].lower()
    wetter_emoji = "☀️" if "sonn" in bedingung else \
                   "🌧️" if "regen" in bedingung else \
                   "🌫️" if "nebel" in bedingung else \
                   "💨" if "wind" in bedingung else "☁️"
    
    # Formatierung mit Box-Drawing-Characters
    breite = 40
    output = []
    output.append("╔" + "═" * (breite - 2) + "╗")
    output.append(f"║ {wetter_emoji} Wetter in {wetter['stadt']:<{breite - 12}}║")
    output.append("╠" + "═" * (breite - 2) + "╣")
    output.append(f"║  🌡️  Temperatur:     {wetter['temperatur']}°C{' ' * (breite - 22 - len(str(wetter['temperatur'])))}║")
    output.append(f"║  ☁️  Bedingungen:    {wetter['bedingungen']:<{breite - 22}}║")
    output.append(f"║  💧  Luftfeuchtigkeit: {wetter['luftfeuchtigkeit']}%{' ' * (breite - 25 - len(str(wetter['luftfeuchtigkeit'])))}║")
    output.append(f"║  💨  Wind:           {wetter['wind']} km/h{' ' * (breite - 21 - len(str(wetter['wind'])))}║")
    output.append("╚" + "═" * (breite - 2) + "╝")
    
    return "\n".join(output)

def formatiere_wetter_einfach(wetter: Dict[str, any]) -> str:
    """
    Einfache Formatierung ohne Box (für ältere Terminals).
    
    Args:
        wetter: Dictionary mit Wetterdaten
    
    Returns:
        Einfach formatierter String
    """
    return f"""Wetter in {wetter['stadt']}:
Temperatur: {wetter['temperatur']}°C
Bedingungen: {wetter['bedingungen']}
Luftfeuchtigkeit: {wetter['luftfeuchtigkeit']}%
Wind: {wetter['wind']} km/h"""
```

**`weather_cli/cli.py`**:

```python
"""
Command-Line Interface für das Weather CLI Tool.
"""

import argparse
import sys
from typing import Optional

from .api import hole_wetter, check_api_verfuegbar
from .formatter import formatiere_wetter, formatiere_wetter_einfach

def parse_arguments(args: Optional[list[str]] = None) -> argparse.Namespace:
    """
    Parst Kommandozeilen-Argumente.
    
    Args:
        args: Optionale Liste von Argumenten (für Tests)
    
    Returns:
        Namespace-Objekt mit geparsten Argumenten
    """
    parser = argparse.ArgumentParser(
        prog='weather-cli',
        description='Ruft Wetterinformationen für eine Stadt ab.',
        epilog='Beispiel: python main.py --stadt Berlin'
    )
    
    parser.add_argument(
        '--stadt',
        type=str,
        required=True,
        help='Name der Stadt, für die Wetterinformationen abgerufen werden sollen'
    )
    
    parser.add_argument(
        '--einfach',
        action='store_true',
        help='Verwendet einfache Formatierung ohne Box-Drawing'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )
    
    return parser.parse_args(args)

def main(args: Optional[list[str]] = None) -> int:
    """
    Hauptfunktion des CLI-Tools.
    
    Args:
        args: Optionale Kommandozeilen-Argumente (für Tests)
    
    Returns:
        Exit-Code (0 = Erfolg, 1 = Fehler)
    """
    # Prüfe, ob requests verfügbar ist
    if not check_api_verfuegbar():
        print("❌ Fehler: requests-Library nicht gefunden.")
        print("Installiere mit: pip install requests")
        return 1
    
    try:
        # Parse Argumente
        parsed_args = parse_arguments(args)
        
        # Wetterdaten abrufen
        print(f"📡 Rufe Wetterdaten für {parsed_args.stadt} ab...")
        wetter = hole_wetter(parsed_args.stadt)
        
        # Formatieren und ausgeben
        print()
        if parsed_args.einfach:
            print(formatiere_wetter_einfach(wetter))
        else:
            print(formatiere_wetter(wetter))
        
        return 0
    
    except ValueError as e:
        print(f"❌ Eingabefehler: {e}")
        return 1
    
    except KeyError as e:
        print(f"❌ Datenfehler: {e}")
        return 1
    
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

**`main.py`** (Einstiegspunkt):

```python
"""
Einstiegspunkt für das Weather CLI Tool.

Verwendung:
    python main.py --stadt Berlin
    python main.py --stadt München --einfach
"""

import sys
from weather_cli.cli import main

if __name__ == "__main__":
    sys.exit(main())
```

**`README.md`**:

```markdown
# Weather CLI Tool

Ein einfaches Kommandozeilen-Tool zum Abrufen von Wetterinformationen.

## Features

- Abrufen von Wetterinformationen für beliebige Städte
- Übersichtliche, formatierte Ausgabe
- Einfacher Modus für ältere Terminals
- Mock-API für Übungszwecke (kein API-Key erforderlich)

## Installation

### 1. Repository klonen oder herunterladen

```bash
cd weather_cli
```

### 2. Virtuelle Umgebung erstellen

```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### 3. Virtuelle Umgebung aktivieren

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Nach Aktivierung sollte `(venv)` vor deiner Kommandozeile erscheinen.

### 4. Dependencies installieren

```bash
pip install -r requirements.txt
```

## Verwendung

### Grundlegende Verwendung

```bash
python main.py --stadt Berlin
```

Ausgabe:
```
📡 Rufe Wetterdaten für Berlin ab...

╔════════════════════════════════════════╗
║ ☀️ Wetter in Berlin                    ║
╠════════════════════════════════════════╣
║  🌡️  Temperatur:     22°C              ║
║  ☁️  Bedingungen:    Sonnig            ║
║  💧  Luftfeuchtigkeit: 45%             ║
║  💨  Wind:           10 km/h           ║
╚════════════════════════════════════════╝
```

### Einfacher Modus

Für Terminals, die Box-Drawing-Characters nicht unterstützen:

```bash
python main.py --stadt München --einfach
```

### Hilfe anzeigen

```bash
python main.py --help
```

### Version anzeigen

```bash
python main.py --version
```

## Projekt-Struktur

```
weather_cli/
├── venv/                    # Virtuelle Umgebung (git-ignored)
├── weather_cli/             # Haupt-Package
│   ├── __init__.py          # Package-Initialisierung
│   ├── api.py               # Mock-API für Wetterdaten
│   ├── formatter.py         # Formatierungs-Funktionen
│   └── cli.py               # Command-Line Interface
├── tests/                   # Unit-Tests (optional)
│   ├── __init__.py
│   └── test_formatter.py
├── .gitignore               # Git-Ignore-Konfiguration
├── requirements.txt         # Python-Dependencies
├── README.md                # Diese Datei
└── main.py                  # Einstiegspunkt
```

## Virtuelle Umgebung deaktivieren

Wenn du fertig bist:

```bash
deactivate
```

## Hinweise für Entwickler

### Requirements exportieren

Nach Installation neuer Packages:

```bash
pip freeze > requirements.txt
```

### Tests ausführen (Bonus)

```bash
pip install pytest
pytest tests/
```

### Mock-Daten

Dieses Tool verwendet Mock-Daten für Übungszwecke. Für eine reale Anwendung:
1. Registriere dich bei einem Wetterdienst (z.B. OpenWeatherMap)
2. Erhalte einen API-Key
3. Passe `api.py` an, um echte API-Calls zu machen

## Häufige Probleme

### `ModuleNotFoundError: No module named 'requests'`

→ Stelle sicher, dass die virtuelle Umgebung aktiviert ist und installiere Dependencies:
```bash
pip install -r requirements.txt
```

### `requests` ist installiert, aber Fehler tritt trotzdem auf

→ Prüfe, ob die virtuelle Umgebung aktiviert ist:
```bash
# Windows
where python
# Sollte auf venv\Scripts\python.exe zeigen

# macOS/Linux
which python
# Sollte auf venv/bin/python zeigen
```

## Lizenz

MIT License - Frei verwendbar für Bildungszwecke.
```

**`tests/__init__.py`** (leer):

```python
"""Test-Package für weather_cli."""
```

**`tests/test_formatter.py`** (Bonus):

```python
"""
Unit-Tests für das formatter-Modul.

Verwendung:
    pip install pytest
    pytest tests/
"""

import pytest
from weather_cli.formatter import formatiere_wetter, formatiere_wetter_einfach

def test_formatiere_wetter_vollstaendig():
    """Testet Formatierung mit vollständigen Daten."""
    wetter = {
        "stadt": "Berlin",
        "temperatur": 20,
        "bedingungen": "Sonnig",
        "luftfeuchtigkeit": 45,
        "wind": 10
    }
    
    ergebnis = formatiere_wetter(wetter)
    
    # Prüfe, ob wichtige Elemente enthalten sind
    assert "Berlin" in ergebnis
    assert "20°C" in ergebnis
    assert "Sonnig" in ergebnis
    assert "45%" in ergebnis
    assert "10 km/h" in ergebnis
    assert "╔" in ergebnis  # Box-Character

def test_formatiere_wetter_einfach():
    """Testet einfache Formatierung."""
    wetter = {
        "stadt": "München",
        "temperatur": 15,
        "bedingungen": "Bewölkt",
        "luftfeuchtigkeit": 70,
        "wind": 15
    }
    
    ergebnis = formatiere_wetter_einfach(wetter)
    
    assert "München" in ergebnis
    assert "15°C" in ergebnis
    assert "Bewölkt" in ergebnis

def test_formatiere_wetter_fehlende_keys():
    """Testet Fehlerbehandlung bei fehlenden Schlüsseln."""
    wetter_unvollstaendig = {
        "stadt": "Hamburg",
        "temperatur": 12
        # bedingungen, luftfeuchtigkeit, wind fehlen
    }
    
    with pytest.raises(KeyError):
        formatiere_wetter(wetter_unvollstaendig)

def test_formatiere_wetter_falscher_typ():
    """Testet Fehlerbehandlung bei falschem Typ."""
    with pytest.raises(TypeError):
        formatiere_wetter("nicht ein dict")

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

**Ausführung des Programms**:

```bash
# 1. Setup (einmalig)
$ python -m venv venv
$ venv\Scripts\activate  # Windows
$ pip install -r requirements.txt

# 2. Programm ausführen
$ python main.py --stadt Berlin
📡 Rufe Wetterdaten für Berlin ab...

╔════════════════════════════════════════╗
║ ☀️ Wetter in Berlin                    ║
╠════════════════════════════════════════╣
║  🌡️  Temperatur:     22°C              ║
║  ☁️  Bedingungen:    Sonnig            ║
║  💧  Luftfeuchtigkeit: 45%             ║
║  💨  Wind:           10 km/h           ║
╚════════════════════════════════════════╝

# 3. Einfacher Modus
$ python main.py --stadt München --einfach
📡 Rufe Wetterdaten für München ab...

Wetter in München:
Temperatur: 15°C
Bedingungen: Bewölkt
Luftfeuchtigkeit: 70%
Wind: 15 km/h

# 4. Tests ausführen (Bonus)
$ pip install pytest
$ pytest tests/ -v
```

**Erklärung der Lösung**:

**Virtuelle Umgebung (venv)**:

Eine virtuelle Umgebung isoliert Python-Packages pro Projekt. Vorteile:
- Keine Konflikte zwischen Projekt-Dependencies
- Reproduzierbare Umgebungen
- Sauberes System-Python

**Warum `python -m venv venv`?**
- `python -m venv`: Ruft das venv-Modul der Standard-Library auf
- Zweites `venv`: Name des Verzeichnisses für die virtuelle Umgebung

**Aktivierung**:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

Nach Aktivierung:
- `(venv)` erscheint vor der Eingabeaufforderung
- `python` zeigt auf venv-Python, nicht System-Python
- `pip install` installiert nur in venv

**requirements.txt**:

Definiert alle Projekt-Dependencies mit Versionen:
```txt
requests==2.31.0
```

**Best Practice**: Versions-Pinning für Reproduzierbarkeit
- `==`: Exakte Version (empfohlen für Production)
- `>=`: Mindestversion
- `~=`: Kompatible Version

**Erstellen**: `pip freeze > requirements.txt`  
**Installieren**: `pip install -r requirements.txt`

**argparse - Command-Line Interface**:

`argparse` ist Teil der Standard-Library und ermöglicht professionelle CLIs:

```python
parser = argparse.ArgumentParser(description='...')
parser.add_argument('--stadt', required=True, help='...')
```

Features:
- Automatische `--help` Generation
- Type Checking
- Required vs. optional Arguments
- Default Values
- Custom Actions

**Design-Entscheidungen**:

**1. Package-Struktur (weather_cli/)**:
- Trennung von Concerns: API, Formatierung, CLI
- Jedes Modul hat eine klare Verantwortung
- Testbar und wiederverwendbar

**2. Mock-API statt echter API**:
- Keine API-Key-Registrierung nötig (Übungszweck)
- Konsistente Ergebnisse für Demonstration
- Kommentar zeigt, wie echter API-Call aussehen würde

**3. Zwei Formatierungs-Modi**:
- Standard: Box-Drawing für moderne Terminals
- Einfach: Fallback für ältere Terminals
- User-Experience-Optimierung

**4. Error Handling auf mehreren Ebenen**:
- API-Modul: Validierung der Eingabe
- Formatter: Type und Key Checks
- CLI: Catch-All für unerwartete Fehler

**5. Exit Codes**:
```python
sys.exit(0)  # Erfolg
sys.exit(1)  # Fehler
```
Ermöglicht Shell-Scripting und Automatisierung.

> [!WARNING]
> **Häufige Fehler mit venv**:
> 
> ❌ **Fehler 1: venv nicht aktiviert**
> ```bash
> # Falsch:
> $ python -m venv venv
> $ pip install requests  # Installiert in System-Python!
> ```
> ✅ **Richtig**: Immer aktivieren vor pip install
> 
> ❌ **Fehler 2: venv in Git committen**
> ```bash
> # venv/ sollte in .gitignore!
> git add venv/  # NICHT tun!
> ```
> ✅ **Richtig**: Nur requirements.txt committen
> 
> ❌ **Fehler 3: requirements.txt nicht aktualisieren**
> ```bash
> $ pip install neue-library
> # requirements.txt vergessen zu aktualisieren!
> ```
> ✅ **Richtig**: `pip freeze > requirements.txt` nach jeder Installation
> 
> ❌ **Fehler 4: Falsche Python-Version**
> ```bash
> # System hat Python 3.8, aber Projekt braucht 3.11
> $ python -m venv venv  # Nutzt System-Python!
> ```
> ✅ **Richtig**: Spezifische Version nutzen:
> ```bash
> $ python3.11 -m venv venv
> ```

**Warum diese Lösung gut ist**:
- Vollständige Demonstration von venv-Workflow
- Professionelle CLI mit argparse
- Saubere Package-Struktur mit Separation of Concerns
- Umfassendes README mit Setup-Anweisungen
- .gitignore für saubere Versionskontrolle
- Error Handling und Exit Codes
- Bonus: Unit-Tests mit pytest
- Gut dokumentierter Code mit Docstrings
- Mock-API ermöglicht Übung ohne externe Abhängigkeiten
- Zwei Formatierungs-Modi für bessere UX

---

## Zusammenfassung

Diese Übungsaufgaben haben folgende Konzepte vertieft:

**Theorie - Prompt Engineering**:
- Anatomie guter Prompts (Kontext, Aufgabe, Format, Constraints)
- Prompt-Verbesserung durch SMART-Kriterien
- Few-Shot Learning mit repräsentativen Beispielen
- Iteratives Prompt-Design

**Python - Imports & Modularisierung**:
- **P1**: Einfache Module erstellen mit Docstrings und Type Hints
- **P2**: `if __name__ == "__main__"` Pattern für Dual-Use-Module
- **P3**: Packages mit `__init__.py` und `__all__`
- **P4**: Relative vs. absolute Imports in Package-Hierarchien
- **P5**: Virtuelle Umgebungen, requirements.txt, professionelle CLI-Tools

**Neue Python-Konzepte**:
- `import`, `from ... import`, `as`
- `if __name__ == "__main__"`
- `__init__.py`, `__all__`
- Relative Imports (`.`, `..`)
- `python -m venv`
- `pip freeze > requirements.txt`
- `argparse` für CLIs
- Package-Strukturen und Hierarchien

Diese Lösungen zeigen Best Practices für strukturierten, wartbaren Python-Code.

