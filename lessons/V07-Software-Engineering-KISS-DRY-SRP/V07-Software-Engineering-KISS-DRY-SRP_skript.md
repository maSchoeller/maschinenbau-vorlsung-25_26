# V07: Software Engineering (KISS, DRY, SRP)

> [!NOTE]
> **Lernziele dieser Vorlesung**:
> - Die drei grundlegenden Software-Engineering-Prinzipien KISS, DRY und SRP verstehen und anwenden können
> - Code-Qualität anhand objektiver Kriterien bewerten können
> - Typische Code-Smells erkennen und durch Refactoring beseitigen
> - `break` und `continue` zur präzisen Schleifensteuerung einsetzen
> - Verschachtelte Schleifen korrekt implementieren und deren Komplexität verstehen
> - Die `else`-Klausel bei Schleifen für elegante Suchalgorithmen nutzen
> - List Comprehensions als kompakte Alternative zu expliziten Schleifen schreiben

---

## Teil 1: Theorie - Software Engineering Prinzipien

### Überblick

Software Engineering beschäftigt sich mit der systematischen Entwicklung, Wartung und Verwaltung von Softwaresystemen. Während in den bisherigen Vorlesungen die korrekte Funktionsweise von Code im Vordergrund stand, geht es nun um die Qualität des Codes selbst. Guter Code ist nicht nur Code, der funktioniert, sondern Code, der lesbar, wartbar, erweiterbar und robust ist. Die drei Prinzipien KISS, DRY und SRP bilden das Fundament für qualitativ hochwertigen Code und sind in der professionellen Softwareentwicklung unverzichtbar.

Diese Prinzipien sind sprachunabhängig und gelten für alle Programmierparadigmen. Sie helfen dabei, technische Schulden zu vermeiden und die Langlebigkeit von Software sicherzustellen. Technische Schulden entstehen, wenn kurzfristige Lösungen die langfristige Wartbarkeit beeinträchtigen. Je früher diese Prinzipien verinnerlicht werden, desto natürlicher werden sie in der täglichen Programmierpraxis angewendet.

### Das KISS-Prinzip: Keep It Simple, Stupid

> [!NOTE]
> **KISS (Keep It Simple, Stupid)**: Ein Software-Design-Prinzip, das besagt, dass Systeme am besten funktionieren, wenn sie einfach gehalten werden, anstatt unnötig komplex zu sein.

Das KISS-Prinzip wurde in den 1960er Jahren von der US-Navy entwickelt und ist heute eines der fundamentalsten Prinzipien im Software Engineering. Die zentrale Aussage lautet: Einfachheit sollte ein primäres Designziel sein, und unnötige Komplexität sollte aktiv vermieden werden. Dies bedeutet nicht, dass Software simpel oder primitiv sein soll, sondern dass jede Komplexität gerechtfertigt sein muss.

Komplexität in Software entsteht auf verschiedenen Ebenen. Die **algorithmische Komplexität** beschreibt, wie aufwändig ein Algorithmus ist. Die **strukturelle Komplexität** bezieht sich auf die Architektur und Organisation des Codes. Die **kognitive Komplexität** misst, wie schwierig es ist, den Code zu verstehen. KISS zielt primär darauf ab, die kognitive Komplexität zu minimieren, da diese die Wartbarkeit am stärksten beeinflusst.

#### Warum Einfachheit wichtig ist

Einfacher Code bietet zahlreiche Vorteile, die sich über den gesamten Softwarelebenszyklus bemerkbar machen. Die **Verständlichkeit** verbessert sich dramatisch, da neue Teammitglieder den Code schneller erfassen können und die Einarbeitungszeit sinkt. Die **Wartbarkeit** profitiert davon, dass Bugs leichter zu finden und zu beheben sind. Die **Erweiterbarkeit** wird erleichtert, weil neue Features ohne große Umbauten integriert werden können. Schließlich führt Einfachheit zu weniger Bugs, da weniger Komplexität weniger potenzielle Fehlerquellen bedeutet.

Komplexer Code hingegen birgt erhebliche Risiken. Versteckte Bugs treten häufiger auf, da sie in verschachtelten Strukturen schwerer zu entdecken sind. Die Entwicklungsgeschwindigkeit sinkt, weil Änderungen mehr Zeit und Aufwand erfordern. Refactoring wird schwieriger, da die Auswirkungen von Änderungen schwer abzuschätzen sind. Zudem führt komplexer Code zu Frustration im Team, was die Motivation und Produktivität beeinträchtigt.

#### KISS in der Praxis

Die Anwendung des KISS-Prinzips erfordert bewusste Entscheidungen auf allen Ebenen der Softwareentwicklung. Bei der **Namenswahl** sollten Variablen, Funktionen und Klassen selbsterklärende Namen erhalten, die ihre Funktion klar beschreiben. Vermeide kryptische Abkürzungen, die nur dem ursprünglichen Autor verständlich sind. Statt `calc_res_for_usr_inp` ist `calculate_result_for_user_input` oder noch besser `process_user_calculation` viel klarer.

Bei **Funktionen und Methoden** gilt die Regel: Eine Funktion sollte eine klar definierte Aufgabe erfüllen. Funktionen, die mehrere nicht zusammenhängende Dinge tun, sollten aufgeteilt werden. Eine Funktion mit 200 Zeilen Code ist fast immer ein Zeichen dafür, dass sie gegen KISS verstößt. Als Faustregel gilt: Wenn eine Funktion nicht auf einen Bildschirm passt, ist sie wahrscheinlich zu komplex.

Die **Verschachtelungstiefe** sollte begrenzt werden. Mehr als drei Ebenen von verschachtelten `if`-Statements oder Schleifen machen Code schwer lesbar. In solchen Fällen sollte der Code durch frühe Returns, Hilfsfunktionen oder Guard Clauses umstrukturiert werden.

Bei **Algorithmen** bedeutet KISS nicht, ineffiziente Lösungen zu wählen. Vielmehr geht es darum, den einfachsten Algorithmus zu wählen, der die Anforderungen erfüllt. Vorzeitige Optimierung ist oft die Wurzel unnötiger Komplexität. Erst wenn ein Performanzproblem tatsächlich gemessen wurde, sollte optimiert werden.

> [!TIP]
> ```python
> # Schlecht: Unnötig komplex
> def check_status(x):
>     if x > 0:
>         if x < 100:
>             if x % 2 == 0:
>                 return "even_valid"
>             else:
>                 return "odd_valid"
>         else:
>             return "too_large"
>     else:
>         return "invalid"
> 
> # Gut: Einfach und klar
> def check_status(x):
>     if x <= 0:
>         return "invalid"
>     if x >= 100:
>         return "too_large"
>     return "even_valid" if x % 2 == 0 else "odd_valid"
> ```

> [!WARNING]
> **Häufiger Fehler**: KISS bedeutet nicht, auf Abstraktionen oder Design Patterns zu verzichten, wenn sie angemessen sind. Es bedeutet, keine unnötigen Abstraktionen einzuführen. Die Kunst liegt darin, die richtige Balance zu finden.

#### Wann ist Code zu einfach?

Es gibt Situationen, in denen übermäßige Vereinfachung problematisch sein kann. Wenn ein einfacher Algorithmus signifikante Performance-Probleme verursacht, die durch eine etwas komplexere Lösung behoben werden können, ist die Komplexität gerechtfertigt. Wenn Domänen-Logik inhärent komplex ist (z.B. in Finanzsystemen oder wissenschaftlichen Berechnungen), sollte diese Komplexität nicht künstlich verschleiert werden. Wenn wichtige Fehlerbehandlung oder Validierung weggelassen wird, um den Code "einfach" zu halten, ist dies ein Fehler. KISS bedeutet nicht, auf notwendige Robustheit zu verzichten.

### Das DRY-Prinzip: Don't Repeat Yourself

> [!NOTE]
> **DRY (Don't Repeat Yourself)**: Ein Software-Entwicklungsprinzip, das besagt, dass jede Information in einem System eine einzige, eindeutige und autoritative Repräsentation haben sollte.

Das DRY-Prinzip wurde von Andrew Hunt und David Thomas in ihrem Buch "The Pragmatic Programmer" (1999) formuliert und ist heute ein zentrales Konzept moderner Softwareentwicklung. Die Kernidee ist, dass Code-Duplikation aktiv vermieden werden sollte, weil sie zu Inkonsistenzen, erhöhtem Wartungsaufwand und Fehleranfälligkeit führt.

Wichtig ist zu verstehen, dass DRY sich nicht nur auf identischen Code bezieht. Auch konzeptionelle Duplikation, bei der dasselbe Konzept an mehreren Stellen auf unterschiedliche Weise implementiert wird, verstößt gegen DRY. Ebenso fällt die Duplikation von Wissen oder Business-Logik unter dieses Prinzip.

#### Warum Code-Duplikation problematisch ist

Code-Duplikation führt zu zahlreichen Problemen im Softwarelebenszyklus. Bei der **Wartung** entsteht das Problem, dass bei Änderungen alle duplizierten Stellen gefunden und konsistent aktualisiert werden müssen. Übersieht man eine Stelle, entstehen Inkonsistenzen. Bugs müssen an mehreren Stellen gefixt werden, was zeitaufwändig und fehleranfällig ist.

Die **Konsistenz** leidet, weil verschiedene Versionen desselben Codes sich im Laufe der Zeit auseinanderentwickeln können. Dies führt zu unerwartetem Verhalten und macht das System unvorhersehbar. Die **Codegröße** wächst unnötig, was die Übersichtlichkeit reduziert und die Build-Zeit erhöht. Bei der **Fehlersuche** wird es schwieriger, die Ursache von Bugs zu lokalisieren, wenn derselbe fehlerhafte Code an mehreren Stellen existiert.

#### Arten von Code-Duplikation

Es gibt verschiedene Formen von Duplikation, die erkannt werden sollten. Die **exakte Duplikation** liegt vor, wenn identischer oder nahezu identischer Code mehrfach vorkommt. Dies ist die offensichtlichste Form und am leichtesten zu beheben.

Die **strukturelle Duplikation** tritt auf, wenn derselbe Algorithmus oder dieselbe Logik mit leicht unterschiedlichen Variablen oder Parametern mehrfach implementiert wird. Diese Form ist subtiler und erfordert Abstraktion durch Funktionen oder Klassen.

Die **konzeptionelle Duplikation** entsteht, wenn dasselbe Problem auf verschiedene Weisen gelöst wird. Beispielsweise könnte Datums-Formatierung an einer Stelle mit `strftime()` und an anderer Stelle manuell mit String-Operationen erfolgen. Beide implementieren dasselbe Konzept, aber nicht konsistent.

Die **Datenduplikation** bezieht sich auf redundante Datenhaltung, bei der dieselbe Information an mehreren Stellen gespeichert wird, ohne dass eine Single Source of Truth existiert.

#### DRY in der Praxis

Die Anwendung des DRY-Prinzips erfolgt durch verschiedene Techniken. **Funktionen und Methoden** sind das primäre Werkzeug zur Vermeidung von Code-Duplikation. Wiederholter Code sollte in Funktionen extrahiert werden. Diese Funktionen sollten mit klaren, aussagekräftigen Namen versehen werden, die ihre Aufgabe beschreiben.

**Konstanten und Konfigurationen** helfen dabei, Magic Numbers und wiederholte Werte zu vermeiden. Statt die Zahl `3.14159` an mehreren Stellen zu verwenden, sollte eine Konstante `PI = 3.14159` definiert werden. Dies gilt auch für Schwellwerte, Limits und Konfigurationswerte.

**Schleifen und Datenstrukturen** können oft genutzt werden, um repetitiven Code zu eliminieren. Anstatt denselben Code für verschiedene Eingaben zu kopieren, sollte eine Schleife über eine Datenstruktur verwendet werden.

**Abstraktionen und Design Patterns** ermöglichen es, wiederkehrende Lösungsmuster elegant zu implementieren. Template Method, Strategy oder Factory Patterns sind Beispiele für Abstraktionen, die Duplikation auf höherer Ebene vermeiden.

> [!TIP]
> ```python
> # Schlecht: Code-Duplikation
> temperatur_celsius_1 = (temperatur_fahrenheit_1 - 32) * 5/9
> temperatur_celsius_2 = (temperatur_fahrenheit_2 - 32) * 5/9
> temperatur_celsius_3 = (temperatur_fahrenheit_3 - 32) * 5/9
> 
> # Gut: Funktion zur Wiederverwendung
> def fahrenheit_zu_celsius(fahrenheit):
>     """Konvertiert Fahrenheit in Celsius."""
>     return (fahrenheit - 32) * 5 / 9
> 
> temperatur_celsius_1 = fahrenheit_zu_celsius(temperatur_fahrenheit_1)
> temperatur_celsius_2 = fahrenheit_zu_celsius(temperatur_fahrenheit_2)
> temperatur_celsius_3 = fahrenheit_zu_celsius(temperatur_fahrenheit_3)
> 
> # Noch besser: Mit Schleife
> temperaturen_fahrenheit = [temperatur_fahrenheit_1, temperatur_fahrenheit_2, temperatur_fahrenheit_3]
> temperaturen_celsius = [fahrenheit_zu_celsius(temp) for temp in temperaturen_fahrenheit]
> ```

> [!WARNING]
> **Häufiger Fehler**: Zwei Code-Stücke, die zufällig momentan identisch sind, aber unterschiedliche Konzepte repräsentieren, sollten nicht "getrocknet" werden. Die Ähnlichkeit könnte zufällig sein, und eine gemeinsame Abstraktion würde künstliche Kopplung erzeugen. Die "Rule of Three" besagt: Erst beim dritten Vorkommen refaktorieren, nicht beim zweiten.

#### Wann ist DRY zu weit getrieben?

Es gibt Situationen, in denen strikte Anwendung von DRY kontraproduktiv sein kann. Wenn die Abstraktion komplexer ist als die ursprüngliche Duplikation, ist DRY übertrieben. Eine einfache Wiederholung von zwei Zeilen kann klarer sein als eine generische Funktion mit vielen Parametern.

Wenn zwei Code-Stücke nur zufällig ähnlich sind, aber unterschiedliche Verantwortlichkeiten haben, sollten sie nicht zusammengefasst werden. Dies würde unerwünschte Kopplung erzeugen. Wenn eine Änderung an der gemeinsamen Abstraktion eine der Verwendungsstellen betrifft, aber nicht die andere, ist die Abstraktion falsch gewählt.

In Performance-kritischen Situationen kann manchmal bewusste Duplikation akzeptabel sein, wenn die Abstraktion zu einem messbaren Performance-Verlust führt. Dies sollte aber die Ausnahme sein und durch Profiling belegt werden.

### Das SRP: Single Responsibility Principle

> [!NOTE]
> **SRP (Single Responsibility Principle)**: Ein Prinzip aus der objektorientierten Programmierung, das besagt, dass jede Klasse, Funktion oder Modul genau eine Verantwortlichkeit haben sollte und nur einen Grund zur Änderung haben sollte.

Das Single Responsibility Principle wurde von Robert C. Martin ("Uncle Bob") als Teil der SOLID-Prinzipien formuliert und ist fundamental für modulare, wartbare Software. Die zentrale Idee ist, dass jede Softwareeinheit eine klar definierte Aufgabe haben sollte. Dies reduziert Komplexität, verbessert die Testbarkeit und erleichtert Änderungen.

Robert C. Martin definiert eine "Verantwortlichkeit" als "einen Grund zur Änderung". Wenn eine Klasse oder Funktion aus mehreren unterschiedlichen Gründen geändert werden muss, verletzt sie das SRP. Beispielsweise sollte eine Funktion, die sowohl Daten aus einer Datei liest als auch Berechnungen durchführt, aufgeteilt werden, da Änderungen am Dateiformat und Änderungen an der Berechnungslogik unterschiedliche Verantwortlichkeiten darstellen.

#### Warum SRP wichtig ist

Das Single Responsibility Principle bietet zahlreiche Vorteile für die Softwarequalität. Die **Wartbarkeit** verbessert sich, weil Änderungen lokal bleiben und sich nicht über das gesamte System ausbreiten. Wenn eine Funktion nur eine Aufgabe hat, sind die Auswirkungen von Änderungen leicht vorhersehbar.

Die **Testbarkeit** profitiert enorm von SRP. Kleine, fokussierte Funktionen sind einfach zu testen. Unit Tests können präzise geschrieben werden, und Edge Cases sind leichter zu identifizieren. Testdaten sind weniger komplex, wenn Funktionen nur eine Sache tun.

Die **Wiederverwendbarkeit** steigt, da spezialisierte Funktionen in verschiedenen Kontexten eingesetzt werden können. Eine Funktion, die nur eine Aufgabe erfüllt, ist wahrscheinlicher an anderer Stelle nützlich als eine Funktion, die mehrere Dinge tut.

Die **Verständlichkeit** wird deutlich besser. Code, der SRP befolgt, liest sich wie gut strukturierte Prosa. Jede Funktion hat einen klaren Namen, der ihre Aufgabe beschreibt, und der Code innerhalb der Funktion fokussiert sich auf diese eine Aufgabe.

#### SRP in der Praxis

Die Anwendung des SRP erfordert sorgfältige Planung und kontinuierliches Refactoring. Bei **Funktionen** bedeutet SRP, dass jede Funktion genau eine klar definierte Aufgabe erfüllen sollte. Eine Funktion namens `berechne_und_speichere_ergebnis()` verletzt vermutlich SRP, da sie zwei Dinge tut: berechnen und speichern. Besser wäre es, dies in `berechne_ergebnis()` und `speichere_ergebnis()` zu trennen.

Bei **Klassen** (die in späteren Vorlesungen behandelt werden) sollte jede Klasse eine kohärente Menge von Funktionen bereitstellen, die alle derselben übergeordneten Verantwortlichkeit dienen. Eine Klasse `BenutzerManager`, die gleichzeitig Benutzer authentifiziert, E-Mails versendet und Datenbank-Backups erstellt, verletzt SRP massiv.

Bei **Modulen und Dateien** sollte die Dateistruktur die Verantwortlichkeiten widerspiegeln. Eine Python-Datei sollte zusammenhängende Funktionalität enthalten. Eine Datei `utils.py`, die zufällige Hilfsfunktionen sammelt, verletzt oft SRP, weil sie keine klare Verantwortlichkeit hat.

#### Wie man Verantwortlichkeiten identifiziert

Die Identifikation von Verantwortlichkeiten erfordert Übung und Erfahrung. Ein praktischer Ansatz ist die **"Reason to Change"-Methode**. Stelle dir die Frage: "Aus welchen unterschiedlichen Gründen könnte dieser Code geändert werden müssen?" Wenn du mehr als einen Grund findest, liegt wahrscheinlich eine SRP-Verletzung vor.

Die **Beschreibungsmethode** hilft ebenfalls. Versuche, die Aufgabe einer Funktion in einem Satz zu beschreiben, ohne "und" zu verwenden. Wenn du "und" brauchst, macht die Funktion wahrscheinlich mehrere Dinge.

Die **Kohäsionsanalyse** betrachtet, wie stark die verschiedenen Teile einer Funktion oder Klasse zusammenhängen. Wenn Variablen und Operationen logisch zusammengehören und aufeinander aufbauen, ist die Kohäsion hoch. Wenn verschiedene Teile unabhängig voneinander sind, ist die Kohäsion niedrig und SRP wird wahrscheinlich verletzt.

> [!TIP]
> ```python
> # Schlecht: Mehrere Verantwortlichkeiten
> def verarbeite_bestellung(bestellung_id):
>     # Daten aus Datenbank laden
>     bestellung = lade_aus_db(bestellung_id)
>     
>     # Validierung
>     if bestellung.betrag < 0:
>         raise ValueError("Negativer Betrag")
>     
>     # Berechnung
>     steuern = bestellung.betrag * 0.19
>     gesamt = bestellung.betrag + steuern
>     
>     # In Datenbank speichern
>     speichere_in_db(bestellung_id, gesamt)
>     
>     # E-Mail senden
>     sende_email(bestellung.kunde_email, f"Rechnung: {gesamt}€")
>     
>     # Logging
>     schreibe_log(f"Bestellung {bestellung_id} verarbeitet")
> 
> # Gut: Aufgeteilt nach Verantwortlichkeiten
> def lade_bestellung(bestellung_id):
>     """Lädt Bestellung aus Datenbank."""
>     return lade_aus_db(bestellung_id)
> 
> def validiere_bestellung(bestellung):
>     """Validiert Bestellungsdaten."""
>     if bestellung.betrag < 0:
>         raise ValueError("Negativer Betrag")
> 
> def berechne_gesamtbetrag(betrag, steuersatz=0.19):
>     """Berechnet Gesamtbetrag inkl. Steuern."""
>     steuern = betrag * steuersatz
>     return betrag + steuern
> 
> def speichere_bestellung(bestellung_id, betrag):
>     """Speichert Bestellung in Datenbank."""
>     speichere_in_db(bestellung_id, betrag)
> 
> def benachrichtige_kunde(kunde_email, betrag):
>     """Sendet Bestätigungsmail an Kunden."""
>     sende_email(kunde_email, f"Rechnung: {betrag}€")
> 
> def protokolliere_verarbeitung(bestellung_id):
>     """Protokolliert Verarbeitung."""
>     schreibe_log(f"Bestellung {bestellung_id} verarbeitet")
> 
> # Koordinierende Funktion (orchestriert die Schritte)
> def verarbeite_bestellung(bestellung_id):
>     """Koordiniert die Verarbeitung einer Bestellung."""
>     bestellung = lade_bestellung(bestellung_id)
>     validiere_bestellung(bestellung)
>     gesamt = berechne_gesamtbetrag(bestellung.betrag)
>     speichere_bestellung(bestellung_id, gesamt)
>     benachrichtige_kunde(bestellung.kunde_email, gesamt)
>     protokolliere_verarbeitung(bestellung_id)
> ```

> [!WARNING]
> **Häufiger Fehler**: Über-Engineering durch zu starke Aufteilung. Nicht jede Zeile Code muss in eine eigene Funktion. Die Aufteilung sollte logische Verantwortlichkeiten widerspiegeln, nicht willkürlich erfolgen. Eine Funktion mit 5-10 Zeilen, die eine kohärente Aufgabe erfüllt, ist oft besser als fünf Einzeilen-Funktionen.

#### Wann ist SRP zu strikt?

Es gibt Situationen, in denen eine strikte Anwendung von SRP kontraproduktiv sein kann. Bei sehr kleinen Funktionen (3-5 Zeilen), die eine offensichtlich zusammenhängende Aufgabe erfüllen, ist weitere Aufteilung oft übertrieben. Wenn die Abstraktion die Lesbarkeit verschlechtert, weil man ständig zwischen Funktionen hin- und herspringen muss, ist SRP zu weit getrieben.

In Performance-kritischen Abschnitten kann es sinnvoll sein, verwandte Operationen zusammenzufassen, um Funktionsaufruf-Overhead zu vermeiden. Dies sollte aber durch Profiling belegt sein und dokumentiert werden.

Bei prototypischer Entwicklung oder Proof-of-Concepts ist es oft pragmatischer, zunächst funktionierenden Code zu schreiben und erst später zu refaktorieren. Verfrühte Abstraktion kann die Entwicklung verlangsamen, ohne echten Nutzen zu bringen.

### Code-Qualität und Wartbarkeit

Die drei Prinzipien KISS, DRY und SRP bilden zusammen ein starkes Fundament für qualitativ hochwertigen Code. Sie ergänzen sich gegenseitig und überlappen in vielen Bereichen. KISS sorgt dafür, dass Code verständlich bleibt. DRY verhindert Redundanz und Inkonsistenz. SRP stellt sicher, dass Code modular und änderbar ist.

Code-Qualität ist nicht nur eine ästhetische Frage, sondern hat direkte Auswirkungen auf den Projekterfolg. Schlechte Code-Qualität führt zu erhöhten Wartungskosten, längeren Entwicklungszeiten und höherer Fehlerrate. Gute Code-Qualität ermöglicht es Teams, nachhaltig produktiv zu bleiben und flexibel auf Änderungen zu reagieren.

#### Code-Smells und Refactoring

**Code-Smells** sind Symptome im Code, die auf tieferliegende Probleme hindeuten. Sie sind keine Bugs, aber Warnsignale, dass der Code verbessert werden sollte. Typische Code-Smells umfassen lange Funktionen (mehr als 20-30 Zeilen), viele Parameter (mehr als 3-4), tief verschachtelte Strukturen (mehr als 3 Ebenen), duplizierter Code, magische Zahlen ohne Erklärung, unklare Namensgebung und Funktionen mit Seiteneffekten.

**Refactoring** ist der Prozess, Code zu verbessern, ohne sein externes Verhalten zu ändern. Refactoring sollte in kleinen, sicheren Schritten erfolgen. Jeder Schritt sollte getestet werden, bevor der nächste erfolgt. Idealerweise existieren automatisierte Tests, die sicherstellen, dass Refactoring keine Funktionalität bricht.

Typische Refactoring-Operationen umfassen das Extrahieren von Funktionen (Extract Method), das Umbenennen von Variablen (Rename), das Zusammenfassen von duplizierten Code (Extract Method oder Superclass), das Aufteilen von langen Funktionen (Extract Method), das Einführen von Konstanten für Magic Numbers und das Vereinfachen von Bedingungen.

#### Code Reviews und Best Practices

Code Reviews sind ein essentieller Bestandteil professioneller Softwareentwicklung. Sie dienen dazu, Fehler frühzeitig zu finden, Wissen im Team zu teilen, Code-Qualität zu sichern und Best Practices zu etablieren. Bei einem Code Review prüft ein anderer Entwickler den Code, bevor er ins Hauptrepository integriert wird.

Effektive Code Reviews konzentrieren sich auf die Lesbarkeit des Codes, die Einhaltung von Coding Standards, die Anwendung von KISS, DRY und SRP, potenzielle Bugs und Edge Cases, die Korrektheit von Tests und die Dokumentation.

Best Practices für Code Reviews umfassen konstruktives Feedback mit konkreten Verbesserungsvorschlägen, die Fokussierung auf den Code statt auf die Person, das Anbieten von Alternativen statt bloßer Kritik, die zeitnahe Durchführung von Reviews und die Begrenzung der Review-Größe auf überschaubare Mengen (typischerweise 200-400 Zeilen Code).

### Zusammenfassung Theorie

Die drei Software-Engineering-Prinzipien KISS, DRY und SRP bilden das Fundament für qualitativ hochwertigen, wartbaren Code. Das **KISS-Prinzip** fordert, Komplexität nur dort einzuführen, wo sie notwendig ist, und Einfachheit als primäres Designziel zu verfolgen. Das **DRY-Prinzip** eliminiert Code-Duplikation und stellt sicher, dass jede Information im System eine einzige, autoritative Repräsentation hat. Das **SRP** garantiert, dass jede Code-Einheit eine klar definierte Verantwortlichkeit hat und nur aus einem Grund geändert werden muss.

Diese Prinzipien sind nicht dogmatisch zu verstehen, sondern als Leitlinien, die mit Erfahrung und Kontext angewendet werden sollten. Die Balance zwischen Einfachheit und Funktionalität, zwischen DRY und Pragmatismus, zwischen SRP und Lesbarkeit ist eine Kunst, die mit der Zeit entwickelt wird. Code-Qualität ist ein kontinuierlicher Prozess, kein einmaliges Ziel. Durch regelmäßiges Refactoring, Code Reviews und bewusste Anwendung dieser Prinzipien entsteht langfristig wartbare Software, die den Anforderungen moderner Entwicklung gerecht wird.

---

## Teil 2: Python-Praxis - Schleifen (for, while) – Teil 2

> [!WARNING]
> **Python-Konsistenz beachten**: Die Grundlagen von `for` und `while` wurden in V06 eingeführt. Hier erweitern wir das Wissen um fortgeschrittene Schleifensteuerung.

### Überblick

In V06 wurden die Grundlagen von Schleifen behandelt: `for`-Schleifen zum Iterieren über Sequenzen und `while`-Schleifen für bedingte Wiederholungen. Diese Vorlesung erweitert das Schleifen-Repertoire um drei mächtige Konzepte: Die präzise Steuerung mit `break` und `continue`, die elegante `else`-Klausel für Schleifen und die kompakte List Comprehension-Syntax. Diese Werkzeuge ermöglichen es, komplexe Iterationslogik elegant und pythonisch zu formulieren.

Schleifen sind fundamentale Kontrollstrukturen, und ihre Beherrschung ist essentiell für effektive Programmierung. Die hier vorgestellten Konzepte sind typisch für Python und heben sich von vielen anderen Programmiersprachen ab. Die `else`-Klausel bei Schleifen ist beispielsweise ein Python-spezifisches Feature, das in Sprachen wie Java oder C++ nicht existiert.

### Schleifensteuerung mit `break` und `continue`

Python bietet zwei Keywords zur feingranularen Steuerung von Schleifen: `break` und `continue`. Beide beeinflussen den Kontrollfluss innerhalb von Schleifen, erfüllen aber unterschiedliche Zwecke.

#### Das `break`-Statement

> [!NOTE]
> **`break`**: Ein Python-Keyword, das die Ausführung der umgebenden Schleife sofort beendet und die Kontrolle an die nächste Anweisung nach der Schleife übergibt.

Das `break`-Statement wird verwendet, wenn eine Schleife vorzeitig beendet werden soll, weil eine bestimmte Bedingung erfüllt ist. Nach der Ausführung von `break` wird die Schleife verlassen, und das Programm fährt mit der ersten Anweisung nach der Schleife fort. `break` funktioniert sowohl in `for`-Schleifen als auch in `while`-Schleifen.

Typische Anwendungsfälle für `break` umfassen die Suche in Listen oder Strings, bei der die Schleife beendet werden soll, sobald das gesuchte Element gefunden wurde. Eingabevalidierung nutzt `break`, um aus einer Eingabeschleife auszubrechen, wenn gültige Daten eingegeben wurden. Bei der Verarbeitung von Dateien oder Datenströmen wird `break` verwendet, wenn ein Abbruchkriterium (z.B. ein Sentinel-Wert) erkannt wird. In Spielprogrammierung dient `break` dazu, Spiel-Loops bei Game Over oder Pause zu beenden.

> [!TIP]
> ```python
> # Beispiel: Suche nach einem Element
> zahlen = [3, 7, 2, 9, 4, 11, 5]
> gesucht = 9
> 
> for i, zahl in enumerate(zahlen):
>     if zahl == gesucht:
>         print(f"Gefunden an Index {i}")
>         break  # Schleife beenden, da gefunden
> else:
>     print("Nicht gefunden")  # Wird nur ausgeführt, wenn break NICHT aufgerufen wurde
> 
> # Beispiel: Eingabevalidierung mit while
> while True:
>     eingabe = input("Gib eine positive Zahl ein: ")
>     if eingabe.isdigit():
>         zahl = int(eingabe)
>         if zahl > 0:
>             print(f"Danke! Du hast {zahl} eingegeben.")
>             break  # Gültige Eingabe, Schleife beenden
>         else:
>             print("Die Zahl muss positiv sein!")
>     else:
>         print("Das ist keine gültige Zahl!")
> ```

Das `break`-Statement beeinflusst nur die innerste umgebende Schleife. Bei verschachtelten Schleifen beendet `break` nur die Schleife, in der es steht, nicht die äußeren Schleifen.

> [!TIP]
> ```python
> # break in verschachtelten Schleifen
> for i in range(3):
>     print(f"Äußere Schleife: i = {i}")
>     for j in range(5):
>         if j == 3:
>             print(f"  Break bei j = {j}")
>             break  # Beendet nur die innere Schleife
>         print(f"  Innere Schleife: j = {j}")
>     print("Innere Schleife beendet")
> 
> # Ausgabe:
> # Äußere Schleife: i = 0
> #   Innere Schleife: j = 0
> #   Innere Schleife: j = 1
> #   Innere Schleife: j = 2
> #   Break bei j = 3
> # Innere Schleife beendet
> # Äußere Schleife: i = 1
> # ...
> ```

#### Das `continue`-Statement

> [!NOTE]
> **`continue`**: Ein Python-Keyword, das den aktuellen Schleifendurchlauf sofort beendet und mit dem nächsten Durchlauf fortsetzt, ohne die Schleife zu verlassen.

Das `continue`-Statement überspringt den Rest des aktuellen Schleifendurchlaufs und springt direkt zur nächsten Iteration. Bei `for`-Schleifen wird die Schleifenvariable auf den nächsten Wert gesetzt. Bei `while`-Schleifen wird die Bedingung erneut geprüft. `continue` wird verwendet, wenn bestimmte Elemente übersprungen werden sollen, ohne die gesamte Schleife zu beenden.

Typische Anwendungsfälle für `continue` umfassen das Filtern von Elementen während der Verarbeitung, das Überspringen ungültiger oder fehlerhafter Daten, das Ignorieren von Sonderfällen und das Vermeiden tief verschachtelter if-Statements durch frühe Fortsetzung.

> [!TIP]
> ```python
> # Beispiel: Nur gerade Zahlen verarbeiten
> zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
> 
> for zahl in zahlen:
>     if zahl % 2 != 0:
>         continue  # Ungerade Zahlen überspringen
>     print(f"{zahl} ist gerade")
> 
> # Ausgabe:
> # 2 ist gerade
> # 4 ist gerade
> # 6 ist gerade
> # 8 ist gerade
> # 10 ist gerade
> 
> # Beispiel: Eingaben verarbeiten und ungültige überspringen
> eingaben = ["12", "abc", "45", "", "78", "xyz"]
> 
> for eingabe in eingaben:
>     if not eingabe.isdigit():
>         print(f"Überspringe ungültige Eingabe: '{eingabe}'")
>         continue
>     
>     # Nur gültige Zahlen werden hier verarbeitet
>     zahl = int(eingabe)
>     quadrat = zahl ** 2
>     print(f"{zahl}² = {quadrat}")
> ```

#### Vergleich: `break` vs. `continue`

Die Unterschiede zwischen `break` und `continue` sind fundamental für ihr Verständnis. `break` beendet die gesamte Schleife sofort, während `continue` nur den aktuellen Durchlauf beendet. Nach `break` wird die Schleife nicht mehr fortgesetzt, nach `continue` geht es mit dem nächsten Element weiter. `break` wird für vorzeitigen Abbruch bei erfüllter Bedingung verwendet, `continue` zum Überspringen einzelner Iterationen. Bei Schleifen mit `else`-Klausel verhindert `break` die Ausführung der `else`-Klausel, `continue` nicht.

> [!TIP]
> ```python
> # Demonstration des Unterschieds
> print("Mit break:")
> for i in range(10):
>     if i == 5:
>         break
>     print(i, end=" ")
> print("\nSchleife beendet")
> # Ausgabe: 0 1 2 3 4
> # Schleife beendet
> 
> print("\nMit continue:")
> for i in range(10):
>     if i == 5:
>         continue
>     print(i, end=" ")
> print("\nSchleife beendet")
> # Ausgabe: 0 1 2 3 4 6 7 8 9
> # Schleife beendet
> ```

> [!WARNING]
> **Häufige Fehler mit `break` und `continue`**:
> 
> **Fehler 1**: `continue` in Kombination mit Inkrement-Operationen bei `while`-Schleifen vergessen
> ```python
> # Problematisch: Endlos-Schleife
> i = 0
> while i < 10:
>     if i % 2 == 0:
>         continue  # i wird nie inkrementiert!
>     print(i)
>     i += 1
> 
> # Richtig: Inkrement vor continue
> i = 0
> while i < 10:
>     i += 1
>     if i % 2 == 0:
>         continue
>     print(i)
> ```
> 
> **Fehler 2**: `break` verwenden, wenn `continue` gemeint war (oder umgekehrt)
> ```python
> # Falsch: Beendet Schleife beim ersten ungeraden Element
> for zahl in [2, 4, 5, 6, 8]:
>     if zahl % 2 != 0:
>         break  # Sollte continue sein
>     print(zahl)
> # Gibt nur "2 4" aus, statt alle geraden
> ```

#### Best Practices für `break` und `continue`

Die effektive Nutzung von `break` und `continue` erfordert Sorgfalt. Vermeide übermäßigen Einsatz, der die Lesbarkeit beeinträchtigt. Zu viele `break` oder `continue` in einer Schleife machen den Kontrollfluss schwer nachvollziehbar. Überlege, ob die Logik nicht klarer mit besseren Bedingungen formuliert werden kann.

Bevorzuge klare Schleifenbedingungen über `break`, wenn möglich. Eine `while`-Schleife mit aussagekräftiger Bedingung ist oft verständlicher als `while True` mit `break`. Nutze `continue` zur Reduzierung von Verschachtelung. Statt tief verschachtelter `if`-Statements kann `continue` verwendet werden, um frühe Exits zu implementieren (Guard Clauses).

Dokumentiere komplexe Verwendungen von `break` und `continue` mit Kommentaren, damit andere Entwickler (oder dein zukünftiges Ich) die Intention verstehen. In verschachtelten Schleifen verwende aussagekräftige Variablennamen und strukturiere den Code so, dass klar ist, welche Schleife von `break` oder `continue` betroffen ist.

### Die `else`-Klausel bei Schleifen

Python bietet eine einzigartige Ergänzung zu Schleifen: die `else`-Klausel. Dieses Feature existiert in den meisten anderen Programmiersprachen nicht und ist eine der eleganten Besonderheiten von Python.

#### Funktionsweise der Schleifen-`else`-Klausel

> [!NOTE]
> **Schleifen-`else`-Klausel**: Ein Python-Feature, bei dem ein `else`-Block nach einer Schleife ausgeführt wird, wenn die Schleife vollständig durchlaufen wurde, ohne dass `break` aufgerufen wurde.

Die `else`-Klausel kann sowohl an `for`-Schleifen als auch an `while`-Schleifen angehängt werden. Der Code im `else`-Block wird nur ausgeführt, wenn die Schleife normal beendet wurde, das heißt ohne Unterbrechung durch `break`. Wenn `break` aufgerufen wird, wird der `else`-Block übersprungen.

Diese Semantik mag zunächst kontraintuitiv erscheinen, da `else` typischerweise "sonst" bedeutet. In diesem Kontext ist es besser als "dann" oder "abschließend, falls nicht abgebrochen" zu interpretieren. Eine alternative Benennung wäre `nobreak` gewesen, aber Python verwendet `else` für Konsistenz.

> [!TIP]
> ```python
> # Beispiel: Primzahl-Test mit else
> def ist_primzahl(n):
>     """Prüft, ob n eine Primzahl ist."""
>     if n < 2:
>         return False
>     
>     for teiler in range(2, int(n ** 0.5) + 1):
>         if n % teiler == 0:
>             print(f"{n} ist durch {teiler} teilbar")
>             break  # Teiler gefunden, keine Primzahl
>     else:
>         # Wird nur ausgeführt, wenn break NICHT aufgerufen wurde
>         print(f"{n} ist eine Primzahl")
>         return True
>     
>     return False
> 
> ist_primzahl(17)  # 17 ist eine Primzahl
> ist_primzahl(18)  # 18 ist durch 2 teilbar
> ```

#### Praktische Anwendungsfälle

Die `else`-Klausel bei Schleifen ist besonders nützlich für Suchalgorithmen. Wenn nach einem Element gesucht wird und es nicht gefunden wurde, wird der `else`-Block ausgeführt. Dies vermeidet die Notwendigkeit zusätzlicher Boolean-Flags.

Bei der Validierung von Daten kann die `else`-Klausel verwendet werden, um anzuzeigen, dass alle Elemente eine Bedingung erfüllen. Wenn ein Element die Bedingung nicht erfüllt, wird `break` aufgerufen und `else` wird übersprungen.

Für Benutzer-Dialoge mit Abbruchmöglichkeit zeigt die `else`-Klausel an, dass der Benutzer die Interaktion nicht vorzeitig abgebrochen hat. In Algorithmen, die nach der ersten Lösung suchen, signalisiert `else`, dass keine Lösung gefunden wurde.

> [!TIP]
> ```python
> # Beispiel: Suche in einer Liste
> namen = ["Alice", "Bob", "Charlie", "David"]
> gesucht = "Eve"
> 
> for name in namen:
>     if name == gesucht:
>         print(f"Gefunden: {name}")
>         break
> else:
>     print(f"{gesucht} wurde nicht gefunden")
> 
> # Beispiel: Validierung aller Elemente
> zahlen = [2, 4, 6, 8, 10]
> 
> for zahl in zahlen:
>     if zahl % 2 != 0:
>         print(f"{zahl} ist ungerade - Validierung fehlgeschlagen")
>         break
> else:
>     print("Alle Zahlen sind gerade - Validierung erfolgreich")
> 
> # Beispiel: while mit else
> versuche = 0
> max_versuche = 3
> 
> while versuche < max_versuche:
>     passwort = input("Passwort: ")
>     versuche += 1
>     
>     if passwort == "geheim123":
>         print("Zugriff gewährt!")
>         break
> else:
>     # Wird nur ausgeführt, wenn alle Versuche aufgebraucht sind
>     print("Maximale Anzahl an Versuchen erreicht. Zugriff verweigert.")
> ```

#### Alternative ohne `else`-Klausel

Bevor die `else`-Klausel bei Schleifen eingeführt wurde (und in Sprachen, die sie nicht haben), wurde typischerweise ein Boolean-Flag verwendet. Dieser Ansatz funktioniert, ist aber weniger elegant und erfordert zusätzlichen Code.

> [!TIP]
> ```python
> # Ohne else-Klausel: Flag-basierter Ansatz
> namen = ["Alice", "Bob", "Charlie", "David"]
> gesucht = "Eve"
> gefunden = False
> 
> for name in namen:
>     if name == gesucht:
>         print(f"Gefunden: {name}")
>         gefunden = True
>         break
> 
> if not gefunden:
>     print(f"{gesucht} wurde nicht gefunden")
> 
> # Mit else-Klausel: Eleganter
> for name in namen:
>     if name == gesucht:
>         print(f"Gefunden: {name}")
>         break
> else:
>     print(f"{gesucht} wurde nicht gefunden")
> ```

> [!WARNING]
> **Häufiger Fehler**: Die `else`-Klausel wird nicht als "falls Schleife nicht durchlaufen" interpretiert (was falsch ist), sondern als "falls break nicht aufgerufen wurde" (was richtig ist). Die Schleife kann vollständig durchlaufen werden, und `else` wird trotzdem ausgeführt – solange kein `break` vorkam.
> 
> ```python
> # Missverständnis: else wird ausgeführt!
> for i in range(5):
>     print(i)
> else:
>     print("Schleife vollständig durchlaufen")  # Wird ausgeführt
> ```

### Verschachtelte Schleifen

Verschachtelte Schleifen sind Schleifen innerhalb von Schleifen. Sie werden verwendet, wenn mehrdimensionale Strukturen verarbeitet werden müssen, wie Matrizen, Koordinatensysteme oder verschachtelte Listen.

#### Grundlagen verschachtelter Schleifen

Bei verschachtelten Schleifen wird für jede Iteration der äußeren Schleife die innere Schleife vollständig durchlaufen. Dies führt zu einer multiplikativen Anzahl von Durchläufen. Wenn die äußere Schleife n-mal läuft und die innere m-mal, werden insgesamt n × m Durchläufe ausgeführt.

> [!TIP]
> ```python
> # Einfaches Beispiel: Multiplikationstabelle
> for i in range(1, 6):
>     for j in range(1, 6):
>         produkt = i * j
>         print(f"{i} × {j} = {produkt:2d}", end="  ")
>     print()  # Zeilenumbruch nach jeder Zeile
> 
> # Ausgabe:
> # 1 × 1 =  1  1 × 2 =  2  1 × 3 =  3  1 × 4 =  4  1 × 5 =  5  
> # 2 × 1 =  2  2 × 2 =  4  2 × 3 =  6  2 × 4 =  8  2 × 5 = 10  
> # ...
> ```

#### Zeitkomplexität verschachtelter Schleifen

Die Zeitkomplexität verschachtelter Schleifen ist ein wichtiges Konzept, das in V10 (Laufzeitanalyse) ausführlich behandelt wird. Zwei ineinander verschachtelte Schleifen, die jeweils n-mal laufen, haben eine Zeitkomplexität von O(n²). Drei verschachtelte Schleifen führen zu O(n³), und so weiter.

Diese exponentielle Steigerung macht verschachtelte Schleifen potenziell teuer. Bei großen Datenmengen kann die Laufzeit schnell problematisch werden. Daher sollte die Notwendigkeit verschachtelter Schleifen kritisch hinterfragt und nach effizienteren Alternativen gesucht werden.

> [!TIP]
> ```python
> # Demonstration der Laufzeit-Explosion
> import time
> 
> n = 100
> 
> # Einfache Schleife: O(n)
> start = time.time()
> for i in range(n):
>     pass
> print(f"Einfache Schleife: {time.time() - start:.6f}s")
> 
> # Doppelt verschachtelt: O(n²)
> start = time.time()
> for i in range(n):
>     for j in range(n):
>         pass
> print(f"Doppelt verschachtelt: {time.time() - start:.6f}s")
> 
> # Dreifach verschachtelt: O(n³)
> start = time.time()
> for i in range(n):
>     for j in range(n):
>         for k in range(n):
>             pass
> print(f"Dreifach verschachtelt: {time.time() - start:.6f}s")
> ```

#### Praktische Beispiele

Verschachtelte Schleifen finden Anwendung in vielen realen Szenarien. Bei der Matrixverarbeitung wird die äußere Schleife für Zeilen und die innere für Spalten verwendet. Koordinatensysteme nutzen verschachtelte Schleifen für x- und y-Koordinaten. Mustergenererierung erstellt 2D-Muster oder ASCII-Art. Kombinatorik erzeugt alle Paare, Tripel oder Permutationen. Algorithmen wie Bubble Sort, Selection Sort und Matrix-Multiplikation verwenden verschachtelte Schleifen.

> [!TIP]
> ```python
> # Beispiel: Rechteck aus Sternen zeichnen
> hoehe = 5
> breite = 8
> 
> for zeile in range(hoehe):
>     for spalte in range(breite):
>         print("*", end="")
>     print()
> 
> # Ausgabe:
> # ********
> # ********
> # ********
> # ********
> # ********
> 
> # Beispiel: Dreieck aus Zahlen
> hoehe = 5
> 
> for zeile in range(1, hoehe + 1):
>     for zahl in range(1, zeile + 1):
>         print(zahl, end="")
>     print()
> 
> # Ausgabe:
> # 1
> # 12
> # 123
> # 1234
> # 12345
> 
> # Beispiel: Alle Paare aus zwei Listen
> farben = ["Rot", "Grün", "Blau"]
> groessen = ["S", "M", "L"]
> 
> for farbe in farben:
>     for groesse in groessen:
>         print(f"{farbe}-{groesse}")
> 
> # Ausgabe:
> # Rot-S
> # Rot-M
> # Rot-L
> # Grün-S
> # ...
> ```

> [!WARNING]
> **Performance-Fallstrick**: Verschachtelte Schleifen können bei großen Datenmengen sehr langsam werden. Wenn möglich, verwende effizientere Algorithmen oder Datenstrukturen. In vielen Fällen können verschachtelte Schleifen durch Hash-Tabellen (Dictionaries) oder Set-Operationen ersetzt werden, was die Komplexität von O(n²) auf O(n) reduziert.

#### `break` und `continue` in verschachtelten Schleifen

In verschachtelten Schleifen beeinflussen `break` und `continue` nur die innerste Schleife, in der sie stehen. Um die äußere Schleife zu beeinflussen, sind zusätzliche Mechanismen nötig.

> [!TIP]
> ```python
> # break bricht nur innere Schleife ab
> for i in range(3):
>     print(f"Äußere: {i}")
>     for j in range(5):
>         if j == 2:
>             break
>         print(f"  Innere: {j}")
> # Äußere Schleife läuft weiter
> 
> # Um beide Schleifen abzubrechen: Flag verwenden
> abbruch = False
> for i in range(3):
>     if abbruch:
>         break
>     for j in range(5):
>         if i == 1 and j == 2:
>             abbruch = True
>             break
>         print(f"({i}, {j})")
> 
> # Alternative: Exception (nicht empfohlen für Kontrollfluss)
> class LoopBreak(Exception):
>     pass
> 
> try:
>     for i in range(3):
>         for j in range(5):
>             if i == 1 and j == 2:
>                 raise LoopBreak
>             print(f"({i}, {j})")
> except LoopBreak:
>     pass
> 
> # Beste Lösung: In Funktion auslagern und return verwenden
> def verarbeite_matrix():
>     for i in range(3):
>         for j in range(5):
>             if i == 1 and j == 2:
>                 return  # Beendet beide Schleifen
>             print(f"({i}, {j})")
> 
> verarbeite_matrix()
> ```

### List Comprehensions

List Comprehensions sind eine kompakte und pythonische Methode, um Listen zu erstellen. Sie kombinieren die Funktionalität von Schleifen, Bedingungen und Listenerstellung in einem einzigen, lesbaren Ausdruck.

#### Grundsyntax der List Comprehension

> [!NOTE]
> **List Comprehension**: Eine syntaktische Konstruktion in Python, die es ermöglicht, Listen durch eine kompakte Notation zu erzeugen, die eine Iteration und optional eine Bedingung enthält.

Die grundlegende Syntax einer List Comprehension ist: `[ausdruck for element in iterable]`. Dies ist äquivalent zu einer `for`-Schleife, die eine Liste aufbaut:

```python
# Mit Schleife
ergebnis = []
for element in iterable:
    ergebnis.append(ausdruck)

# Mit List Comprehension
ergebnis = [ausdruck for element in iterable]
```

List Comprehensions sind nicht nur kürzer, sondern in den meisten Fällen auch schneller als äquivalente Schleifen, da sie intern optimiert sind.

> [!TIP]
> ```python
> # Beispiel: Quadratzahlen erstellen
> zahlen = [1, 2, 3, 4, 5]
> 
> # Mit Schleife
> quadrate = []
> for zahl in zahlen:
>     quadrate.append(zahl ** 2)
> print(quadrate)  # [1, 4, 9, 16, 25]
> 
> # Mit List Comprehension
> quadrate = [zahl ** 2 for zahl in zahlen]
> print(quadrate)  # [1, 4, 9, 16, 25]
> 
> # Direkt mit range()
> quadrate = [x ** 2 for x in range(1, 6)]
> print(quadrate)  # [1, 4, 9, 16, 25]
> ```

#### List Comprehensions mit Bedingungen

List Comprehensions können eine optionale `if`-Bedingung enthalten, um Elemente zu filtern. Die Syntax ist: `[ausdruck for element in iterable if bedingung]`. Nur Elemente, für die die Bedingung `True` ist, werden in die resultierende Liste aufgenommen.

> [!TIP]
> ```python
> # Beispiel: Nur gerade Zahlen
> zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
> 
> # Mit Schleife
> gerade = []
> for zahl in zahlen:
>     if zahl % 2 == 0:
>         gerade.append(zahl)
> print(gerade)  # [2, 4, 6, 8, 10]
> 
> # Mit List Comprehension
> gerade = [zahl for zahl in zahlen if zahl % 2 == 0]
> print(gerade)  # [2, 4, 6, 8, 10]
> 
> # Beispiel: Quadrate gerader Zahlen
> quadrate_gerade = [zahl ** 2 for zahl in zahlen if zahl % 2 == 0]
> print(quadrate_gerade)  # [4, 16, 36, 64, 100]
> 
> # Beispiel: Wörter mit mehr als 3 Buchstaben
> woerter = ["hi", "Hallo", "Welt", "zu", "Python"]
> lange_woerter = [wort for wort in woerter if len(wort) > 3]
> print(lange_woerter)  # ['Hallo', 'Welt', 'Python']
> ```

#### Verschachtelte List Comprehensions

List Comprehensions können verschachtelt werden, ähnlich wie verschachtelte Schleifen. Die Syntax wird von links nach rechts gelesen, ähnlich wie verschachtelte Schleifen von außen nach innen.

`[ausdruck for outer in outer_iterable for inner in inner_iterable]` entspricht:

```python
for outer in outer_iterable:
    for inner in inner_iterable:
        ausdruck
```

> [!TIP]
> ```python
> # Beispiel: Alle Kombinationen
> buchstaben = ['A', 'B', 'C']
> zahlen = [1, 2, 3]
> 
> # Mit Schleifen
> kombinationen = []
> for buchstabe in buchstaben:
>     for zahl in zahlen:
>         kombinationen.append(f"{buchstabe}{zahl}")
> print(kombinationen)
> # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
> 
> # Mit List Comprehension
> kombinationen = [f"{buchstabe}{zahl}" for buchstabe in buchstaben for zahl in zahlen]
> print(kombinationen)
> # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
> 
> # Beispiel: Matrix transponieren
> matrix = [
>     [1, 2, 3],
>     [4, 5, 6],
>     [7, 8, 9]
> ]
> 
> # Transponierte Matrix (Zeilen und Spalten tauschen)
> transponiert = [[zeile[i] for zeile in matrix] for i in range(len(matrix[0]))]
> print(transponiert)
> # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
> ```

> [!WARNING]
> **Lesbarkeit beachten**: Verschachtelte List Comprehensions können schnell unlesbar werden. Als Faustregel gilt: Wenn eine List Comprehension mehr als zwei Ebenen der Verschachtelung hat oder nicht auf eine Zeile passt, ist eine explizite Schleife wahrscheinlich lesbarer.
> 
> ```python
> # Zu komplex: Schwer lesbar
> ergebnis = [[x * y for x in range(3) if x > 0] for y in range(5) if y % 2 == 0]
> 
> # Besser: Explizite Schleifen
> ergebnis = []
> for y in range(5):
>     if y % 2 == 0:
>         zeile = []
>         for x in range(3):
>             if x > 0:
>                 zeile.append(x * y)
>         ergebnis.append(zeile)
> ```

#### Bedingte Ausdrücke in List Comprehensions

List Comprehensions können auch den ternären Operator enthalten, um verschiedene Werte basierend auf einer Bedingung zu erzeugen. Die Syntax ist: `[ausdruck_wenn_wahr if bedingung else ausdruck_wenn_falsch for element in iterable]`.

> [!TIP]
> ```python
> # Beispiel: Gerade/Ungerade kennzeichnen
> zahlen = [1, 2, 3, 4, 5, 6]
> 
> kennzeichnung = ["gerade" if zahl % 2 == 0 else "ungerade" for zahl in zahlen]
> print(kennzeichnung)
> # ['ungerade', 'gerade', 'ungerade', 'gerade', 'ungerade', 'gerade']
> 
> # Beispiel: Werte begrenzen (Clipping)
> werte = [-5, 10, 3, 25, -2, 15]
> maximum = 20
> minimum = 0
> 
> begrenzt = [max(minimum, min(wert, maximum)) for wert in werte]
> print(begrenzt)
> # [0, 10, 3, 20, 0, 15]
> 
> # Mit ternärem Operator für klarere Logik
> begrenzt = [wert if 0 <= wert <= 20 else (0 if wert < 0 else 20) for wert in werte]
> print(begrenzt)
> # [0, 10, 3, 20, 0, 15]
> ```

#### Wann List Comprehensions verwenden

List Comprehensions sind ideal für einfache Transformationen und Filterungen von Listen. Sie sollten verwendet werden, wenn die Logik in eine Zeile passt und leicht verständlich ist, wenn keine komplexe Fehlerbehandlung erforderlich ist, wenn die resultierende Liste tatsächlich benötigt wird (nicht nur Iteration) und wenn die Performance eine Rolle spielt (List Comprehensions sind oft schneller).

List Comprehensions sollten vermieden werden, wenn die Logik komplex ist und mehrere Verschachtelungen erfordert, wenn Seiteneffekte gewünscht sind (z.B. Ausgaben, Datei-Operationen), wenn die Lesbarkeit durch die kompakte Form leidet oder wenn die Fehlerbehandlung wichtig ist (try-except ist in List Comprehensions nicht möglich).

> [!WARNING]
> **Häufiger Fehler**: List Comprehensions für Seiteneffekte verwenden
> 
> ```python
> # Schlecht: List Comprehension nur für Seiteneffekt
> zahlen = [1, 2, 3, 4, 5]
> [print(zahl) for zahl in zahlen]  # Erstellt nutzlose Liste von None-Werten
> 
> # Gut: Normale Schleife für Seiteneffekte
> for zahl in zahlen:
>     print(zahl)
> ```

#### Set und Dictionary Comprehensions

Neben List Comprehensions gibt es auch Set Comprehensions und Dictionary Comprehensions, die nach demselben Prinzip funktionieren. Diese werden in V08 ausführlicher behandelt, wenn Sets und Dictionaries eingeführt werden.

> [!TIP]
> ```python
> # Set Comprehension (erzeugt Set statt Liste)
> zahlen = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
> eindeutige_quadrate = {zahl ** 2 for zahl in zahlen}
> print(eindeutige_quadrate)  # {1, 4, 9, 16} (automatisch eindeutig)
> 
> # Dictionary Comprehension (erzeugt Dictionary)
> woerter = ["Hallo", "Welt", "Python"]
> laengen = {wort: len(wort) for wort in woerter}
> print(laengen)  # {'Hallo': 5, 'Welt': 4, 'Python': 6}
> ```

### Häufige Fehler und Lösungen

> [!WARNING]
> **Fehler 1**: Schleifenvariable in List Comprehension außerhalb verwenden
> 
> ```python
> # Problem: Schleifenvariable "leakt" nach List Comprehension
> quadrate = [x ** 2 for x in range(5)]
> print(x)  # Überraschung: x existiert und hat Wert 4 (letzter Wert)
> # In Python 3 ist dies behoben für List Comprehensions
> 
> # Bei normalen Schleifen existiert die Variable weiterhin
> for i in range(5):
>     pass
> print(i)  # 4 (existiert weiterhin)
> ```
> 
> **Lösung**: Verlasse dich nicht darauf, dass Schleifenvariablen nach der Schleife einen bestimmten Wert haben. Verwende explizite Variablen, wenn der Wert benötigt wird.

> [!WARNING]
> **Fehler 2**: Modifikation der iterierten Liste während der Iteration
> 
> ```python
> # Gefährlich: Liste während Iteration ändern
> zahlen = [1, 2, 3, 4, 5]
> for zahl in zahlen:
>     if zahl % 2 == 0:
>         zahlen.remove(zahl)  # Ändert Liste während Iteration!
> print(zahlen)  # Unvorhersehbares Ergebnis: [1, 3, 5] oder [1, 2, 3, 5]?
> ```
> 
> **Lösung**: Iteriere über eine Kopie oder erstelle eine neue Liste mit den gewünschten Elementen.
> 
> ```python
> # Richtig: Über Kopie iterieren
> zahlen = [1, 2, 3, 4, 5]
> for zahl in zahlen[:]:  # [:] erstellt flache Kopie
>     if zahl % 2 == 0:
>         zahlen.remove(zahl)
> print(zahlen)  # [1, 3, 5]
> 
> # Oder: Neue Liste mit List Comprehension
> zahlen = [1, 2, 3, 4, 5]
> zahlen = [zahl for zahl in zahlen if zahl % 2 != 0]
> print(zahlen)  # [1, 3, 5]
> ```

> [!WARNING]
> **Fehler 3**: Unendliche Schleifen mit `while True` ohne `break`
> 
> ```python
> # Gefährlich: Keine Abbruchbedingung
> while True:
>     print("Das läuft ewig...")
>     # Kein break!
> ```
> 
> **Lösung**: Stelle immer sicher, dass eine Abbruchbedingung existiert.
> 
> ```python
> # Richtig: break bei Bedingung
> zaehler = 0
> while True:
>     print(f"Durchlauf {zaehler}")
>     zaehler += 1
>     if zaehler >= 10:
>         break
> 
> # Oder: Explizite Bedingung
> zaehler = 0
> while zaehler < 10:
>     print(f"Durchlauf {zaehler}")
>     zaehler += 1
> ```

### Zusammenfassung Python

Die erweiterten Schleifenkonzepte aus V07 vervollständigen das Werkzeugset für Iterationen in Python. Das **`break`-Statement** ermöglicht den vorzeitigen Abbruch von Schleifen, wenn eine Bedingung erfüllt ist, und ist besonders nützlich für Such-Algorithmen. Das **`continue`-Statement** überspringt den aktuellen Durchlauf und setzt die Schleife mit dem nächsten Element fort, was zur Filterung und Reduzierung von Verschachtelungen dient.

Die **`else`-Klausel bei Schleifen** ist ein Python-spezifisches Feature, das ausgeführt wird, wenn die Schleife vollständig durchlaufen wurde, ohne dass `break` aufgerufen wurde. Dies eliminiert die Notwendigkeit für Boolean-Flags in vielen Such- und Validierungs-Szenarien.

**Verschachtelte Schleifen** ermöglichen die Verarbeitung mehrdimensionaler Datenstrukturen, bringen aber eine Zeitkomplexität von O(n²) oder höher mit sich. Die Performance sollte bei großen Datenmengen berücksichtigt werden, und Alternativen wie Hash-Tabellen sollten in Betracht gezogen werden.

**List Comprehensions** bieten eine kompakte, pythonische Syntax zur Erstellung von Listen durch Iteration und optionale Filterung. Sie sind lesbarer und oft performanter als äquivalente Schleifen, sollten aber bei komplexer Logik zugunsten expliziter Schleifen vermieden werden.

Die Verbindung zwischen den Software-Engineering-Prinzipien aus Teil 1 und den Python-Konzepten aus Teil 2 ist klar erkennbar. KISS fordert, Schleifen einfach zu halten und keine unnötig verschachtelten Strukturen zu erstellen. DRY wird durch Funktionen und List Comprehensions unterstützt, die redundanten Code eliminieren. SRP gilt auch für Schleifenkörper: Jede Schleife sollte eine klare Aufgabe haben.

### Neue Python-Funktionen/Methoden

In dieser Vorlesung wurden folgende neue Python-Konzepte eingeführt:

- **`break`** (Python Keyword, Python 1.0+): Beendet die umgebende Schleife sofort und übergibt die Kontrolle an die nächste Anweisung nach der Schleife.
- **`continue`** (Python Keyword, Python 1.0+): Beendet den aktuellen Schleifendurchlauf sofort und springt zur nächsten Iteration.
- **Schleifen-`else`-Klausel** (Python 1.0+): Ein `else`-Block nach einer Schleife wird ausgeführt, wenn die Schleife normal beendet wurde (ohne `break`).
- **List Comprehensions** (Python 2.0+, PEP 202): Kompakte Syntax zur Erstellung von Listen: `[ausdruck for element in iterable if bedingung]`.
- **Verschachtelte List Comprehensions** (Python 2.0+): List Comprehensions mit mehreren `for`-Klauseln für mehrdimensionale Iterationen.
- **Set Comprehensions** (Python 2.7+, PEP 274, Vorschau): `{ausdruck for element in iterable}` - ausführliche Behandlung in V08.
- **Dictionary Comprehensions** (Python 2.7+, PEP 274, Vorschau): `{key: value for element in iterable}` - ausführliche Behandlung in V08.

---

## Weiterführende Ressourcen

### Theorie

- **"The Pragmatic Programmer" von Andrew Hunt und David Thomas**: Klassisches Werk über Software-Qualität und DRY-Prinzip
- **"Clean Code" von Robert C. Martin**: Umfassendes Buch über Code-Qualität, KISS, SRP und SOLID-Prinzipien
- **"Code Complete" von Steve McConnell**: Detailliertes Werk über Code-Konstruktion und Best Practices
- **"Refactoring" von Martin Fowler**: Standardwerk über Code-Verbesserung und Refactoring-Patterns
- **PEP 8 - Style Guide for Python Code**: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
- **"The Zen of Python" (PEP 20)**: [https://www.python.org/dev/peps/pep-0020/](https://www.python.org/dev/peps/pep-0020/)

### Python

- **Python Dokumentation - Control Flow**: [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
- **PEP 202 - List Comprehensions**: [https://www.python.org/dev/peps/pep-0202/](https://www.python.org/dev/peps/pep-0202/)
- **PEP 274 - Dict Comprehensions**: [https://www.python.org/dev/peps/pep-0274/](https://www.python.org/dev/peps/pep-0274/)
- **Real Python - Python "for" Loops**: [https://realpython.com/python-for-loop/](https://realpython.com/python-for-loop/)
- **Real Python - Python "while" Loops**: [https://realpython.com/python-while-loop/](https://realpython.com/python-while-loop/)
- **Real Python - List Comprehensions**: [https://realpython.com/list-comprehension-python/](https://realpython.com/list-comprehension-python/)
