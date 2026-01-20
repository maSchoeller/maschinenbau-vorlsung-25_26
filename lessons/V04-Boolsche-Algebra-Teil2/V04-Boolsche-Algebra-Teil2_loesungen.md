# V04: Lösungen - Boolsche Algebra & Logische Schaltungen – Teil 2

> [!WARNING]
> Versuche die Aufgaben zuerst selbstständig zu lösen, bevor du die Lösungen ansiehst!

---

## Teil A: Theorie-Aufgaben - Lösungen

### Lösung T1: XOR und Grundoperatoren

**Lösung**:

Vollständige Wahrheitstabelle für $A \oplus B = (A \land \neg B) \lor (\neg A \land B)$:

| A | B | ¬A | ¬B | A ∧ ¬B | ¬A ∧ B | (A ∧ ¬B) ∨ (¬A ∧ B) | **A ⊕ B** |
|---|---|----|----|--------|--------|---------------------|-----------|
| 0 | 0 | 1  | 1  | 0      | 0      | **0**               | **0**     |
| 0 | 1 | 1  | 0  | 0      | 1      | **1**               | **1**     |
| 1 | 0 | 0  | 1  | 1      | 0      | **1**               | **1**     |
| 1 | 1 | 0  | 0  | 0      | 0      | **0**               | **0**     |

**Erklärung**:

Die Wahrheitstabelle zeigt, dass die Formel $(A \land \neg B) \lor (\neg A \land B)$ für alle Eingangskombinationen exakt das gleiche Ergebnis liefert wie die XOR-Operation $A \oplus B$. Beide Spalten (fettgedruckt) sind identisch, was die Äquivalenz beweist.

**Schritt-für-Schritt-Analyse**:

- **Zeile 1** (A=0, B=0): 
  - $A \land \neg B = 0 \land 1 = 0$
  - $\neg A \land B = 1 \land 0 = 0$
  - $0 \lor 0 = 0$ ✓ (entspricht XOR)

- **Zeile 2** (A=0, B=1):
  - $A \land \neg B = 0 \land 0 = 0$
  - $\neg A \land B = 1 \land 1 = 1$
  - $0 \lor 1 = 1$ ✓ (entspricht XOR)

- **Zeile 3** (A=1, B=0):
  - $A \land \neg B = 1 \land 1 = 1$
  - $\neg A \land B = 0 \land 0 = 0$
  - $1 \lor 0 = 1$ ✓ (entspricht XOR)

- **Zeile 4** (A=1, B=1):
  - $A \land \neg B = 1 \land 0 = 0$
  - $\neg A \land B = 0 \land 1 = 0$
  - $0 \lor 0 = 0$ ✓ (entspricht XOR)

**Häufige Fehler**:
- **Fehler**: Negation vergessen – z.B. $\neg B$ wird als $B$ interpretiert
- **Fehler**: OR und AND verwechselt – die Formel verwendet sowohl AND als auch OR
- **Fehler**: Klammerung missachtet – $(A \land \neg B)$ muss vollständig ausgewertet werden, bevor das OR kommt

---

### Lösung T2: De Morgan'sche Gesetze anwenden

**Lösung**:

**a) Vereinfache** $\neg(A \land B \land C)$

Schritt 1: Wende De Morgan auf die gesamte UND-Verknüpfung an:

$$
\neg(A \land B \land C) = \neg A \lor \neg B \lor \neg C
$$

**Endergebnis**: $\neg A \lor \neg B \lor \neg C$

---

**b) Vereinfache** $\neg((A \lor B) \land C)$

Schritt 1: Wende De Morgan auf die äußere Verknüpfung an (UND wird zu ODER):

$$
\neg((A \lor B) \land C) = \neg(A \lor B) \lor \neg C
$$

Schritt 2: Wende De Morgan auf $\neg(A \lor B)$ an (ODER wird zu UND):

$$
\neg(A \lor B) \lor \neg C = (\neg A \land \neg B) \lor \neg C
$$

**Endergebnis**: $(\neg A \land \neg B) \lor \neg C$

---

**c) Vereinfache** $\neg(A \land \neg B) \lor \neg(C \lor D)$

Schritt 1: Wende De Morgan auf $\neg(A \land \neg B)$ an:

$$
\neg(A \land \neg B) = \neg A \lor \neg(\neg B) = \neg A \lor B
$$

Schritt 2: Wende De Morgan auf $\neg(C \lor D)$ an:

$$
\neg(C \lor D) = \neg C \land \neg D
$$

Schritt 3: Setze zusammen:

$$
(\neg A \lor B) \lor (\neg C \land \neg D)
$$

**Endergebnis**: $(\neg A \lor B) \lor (\neg C \land \neg D)$ oder $\neg A \lor B \lor (\neg C \land \neg D)$

---

**d) Vereinfache** $\neg(\neg A \lor (B \land C))$

Schritt 1: Wende De Morgan auf die äußere Verknüpfung an:

$$
\neg(\neg A \lor (B \land C)) = \neg(\neg A) \land \neg(B \land C)
$$

Schritt 2: Vereinfache die doppelte Negation:

$$
\neg(\neg A) = A
$$

Schritt 3: Wende De Morgan auf $\neg(B \land C)$ an:

$$
\neg(B \land C) = \neg B \lor \neg C
$$

Schritt 4: Setze zusammen:

$$
A \land (\neg B \lor \neg C)
$$

**Endergebnis**: $A \land (\neg B \lor \neg C)$

---

**Erklärung**:

De Morgan'sche Gesetze erlauben es, Negationen in logischen Ausdrücken "nach innen zu schieben". Dabei werden UND-Verknüpfungen zu ODER-Verknüpfungen (und umgekehrt), und jeder Operand wird einzeln negiert. Diese Umformungen sind essentiell für die Vereinfachung komplexer Schaltungen, da sie oft zu weniger Gattern oder effizienteren Implementierungen führen.

**Häufige Fehler**:
- **Fehler**: Operator nicht "flippen" – beim Anwenden von De Morgan muss AND zu OR werden (und umgekehrt)
- **Fehler**: Einzelne Negationen vergessen – jeder Operand innerhalb der Klammer muss negiert werden
- **Fehler**: Doppelte Negation nicht vereinfachen – $\neg(\neg A)$ sollte zu $A$ vereinfacht werden
- **Fehler**: Falsche Klammerung – bei geschachtelten Ausdrücken von außen nach innen arbeiten

---

### Lösung T3: Volladdierer-Schaltung analysieren

**Lösung**:

**a) Vollständige Wahrheitstabelle des Volladdierers**

| A | B | Cin | **S** (Summe) | **Cout** (Übertrag) |
|---|---|-----|---------------|---------------------|
| 0 | 0 | 0   | 0             | 0                   |
| 0 | 0 | 1   | 1             | 0                   |
| 0 | 1 | 0   | 1             | 0                   |
| 0 | 1 | 1   | 0             | 1                   |
| 1 | 0 | 0   | 1             | 0                   |
| 1 | 0 | 1   | 0             | 1                   |
| 1 | 1 | 0   | 0             | 1                   |
| 1 | 1 | 1   | 1             | 1                   |

**Erklärung der Logik**:
- **Summe S**: Ist `1`, wenn eine ungerade Anzahl der drei Eingänge `1` ist (XOR-Logik)
- **Übertrag Cout**: Ist `1`, wenn mindestens zwei der drei Eingänge `1` sind (Mehrheitslogik)

---

**b) Schrittweise Auswertung für A=1, B=1, Cin=1**

Gegeben: $A = 1$, $B = 1$, $Cin = 1$

**Berechnung der Summe** $S = A \oplus B \oplus Cin$:

Schritt 1: $A \oplus B = 1 \oplus 1 = 0$ (beide gleich → XOR ist 0)

Schritt 2: $(A \oplus B) \oplus Cin = 0 \oplus 1 = 1$ (unterschiedlich → XOR ist 1)

**Ergebnis S**: $S = 1$ ✓

**Berechnung des Übertrags** $Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin)$:

Schritt 1: $A \land B = 1 \land 1 = 1$

Schritt 2: $A \land Cin = 1 \land 1 = 1$

Schritt 3: $B \land Cin = 1 \land 1 = 1$

Schritt 4: $1 \lor 1 \lor 1 = 1$ (mindestens eines ist 1 → OR ist 1)

**Ergebnis Cout**: $Cout = 1$ ✓

**Interpretation**: Die Addition von $1 + 1 + 1 = 11$ (binär) = $3$ (dezimal). Die niedrigste Stelle ist $1$ (Summe S), und wir haben einen Übertrag von $1$ (Cout) zur nächsten Stelle.

---

**c) Addition von 1101 + 1011 mit kaskadierten Volladdierern**

Gegeben:
- $A = 1101_2$ (dezimal 13)
- $B = 1011_2$ (dezimal 11)

Wir addieren Stelle für Stelle von rechts nach links:

**Stelle 0** (niedrigste Stelle):
- Eingänge: $A_0 = 1$, $B_0 = 1$, $Cin_0 = 0$ (kein Übertrag von vorheriger Stelle)
- Summe: $S_0 = 1 \oplus 1 \oplus 0 = 0 \oplus 0 = 0$
- Übertrag: $Cout_0 = (1 \land 1) \lor (1 \land 0) \lor (1 \land 0) = 1 \lor 0 \lor 0 = 1$
- **Ergebnis**: $S_0 = 0$, $Cout_0 = 1$

**Stelle 1**:
- Eingänge: $A_1 = 0$, $B_1 = 1$, $Cin_1 = 1$ (Übertrag von Stelle 0)
- Summe: $S_1 = 0 \oplus 1 \oplus 1 = 1 \oplus 1 = 0$
- Übertrag: $Cout_1 = (0 \land 1) \lor (0 \land 1) \lor (1 \land 1) = 0 \lor 0 \lor 1 = 1$
- **Ergebnis**: $S_1 = 0$, $Cout_1 = 1$

**Stelle 2**:
- Eingänge: $A_2 = 1$, $B_2 = 0$, $Cin_2 = 1$
- Summe: $S_2 = 1 \oplus 0 \oplus 1 = 1 \oplus 1 = 0$
- Übertrag: $Cout_2 = (1 \land 0) \lor (1 \land 1) \lor (0 \land 1) = 0 \lor 1 \lor 0 = 1$
- **Ergebnis**: $S_2 = 0$, $Cout_2 = 1$

**Stelle 3** (höchste Stelle):
- Eingänge: $A_3 = 1$, $B_3 = 1$, $Cin_3 = 1$
- Summe: $S_3 = 1 \oplus 1 \oplus 1 = 0 \oplus 1 = 1$
- Übertrag: $Cout_3 = (1 \land 1) \lor (1 \land 1) \lor (1 \land 1) = 1 \lor 1 \lor 1 = 1$
- **Ergebnis**: $S_3 = 1$, $Cout_3 = 1$

**Finales Ergebnis**: 
- Summen-Bits: $S_3 S_2 S_1 S_0 = 1000_2$
- Finaler Übertrag: $Cout_3 = 1$
- Gesamtergebnis: $1 1000_2 = 11000_2 = 24_{10}$ ✓

**Verifikation**: $13 + 11 = 24$ (dezimal) = $11000$ (binär) ✓

**Übersichtstabelle**:

| Stelle | A | B | Cin | S | Cout |
|--------|---|---|-----|---|------|
| 0      | 1 | 1 | 0   | 0 | 1    |
| 1      | 0 | 1 | 1   | 0 | 1    |
| 2      | 1 | 0 | 1   | 0 | 1    |
| 3      | 1 | 1 | 1   | 1 | 1    |

Ergebnis: **11000** (binär) = **24** (dezimal)

---

**d) Vereinfachung der Cout-Gleichung**

Zu zeigen: 

$$
Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin) = (A \land B) \lor ((A \oplus B) \land Cin)
$$

**Beweis durch Wahrheitstabelle**:

| A | B | Cin | A∧B | A∧Cin | B∧Cin | **(A∧B)∨(A∧Cin)∨(B∧Cin)** | A⊕B | (A⊕B)∧Cin | **(A∧B)∨((A⊕B)∧Cin)** |
|---|---|-----|-----|-------|-------|---------------------------|-----|-----------|-----------------------|
| 0 | 0 | 0   | 0   | 0     | 0     | **0**                     | 0   | 0         | **0**                 |
| 0 | 0 | 1   | 0   | 0     | 0     | **0**                     | 0   | 0         | **0**                 |
| 0 | 1 | 0   | 0   | 0     | 0     | **0**                     | 1   | 0         | **0**                 |
| 0 | 1 | 1   | 0   | 0     | 1     | **1**                     | 1   | 1         | **1**                 |
| 1 | 0 | 0   | 0   | 0     | 0     | **0**                     | 1   | 0         | **0**                 |
| 1 | 0 | 1   | 0   | 1     | 0     | **1**                     | 1   | 1         | **1**                 |
| 1 | 1 | 0   | 1   | 0     | 0     | **1**                     | 0   | 0         | **1**                 |
| 1 | 1 | 1   | 1   | 1     | 1     | **1**                     | 0   | 0         | **1**                 |

Die beiden fettgedruckten Spalten sind identisch, was die Äquivalenz beweist.

**Algebraischer Beweis** (alternativ):

Ausgangspunkt:

$$
Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin)
$$

Schritt 1: Faktorisiere $(A \land Cin) \lor (B \land Cin)$ aus:

$$
(A \land Cin) \lor (B \land Cin) = (A \lor B) \land Cin
$$

(Distributivgesetz rückwärts angewendet)

Aber das ist nicht ganz richtig. Versuchen wir einen anderen Ansatz.

Schritt 1: Erweitere $(A \land B)$ geschickt:

$$
Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin)
$$

Schritt 2: Füge $(A \land B \land Cin)$ zweimal hinzu (ändert nichts: $X \lor X = X$):

$$
Cout = (A \land B) \lor (A \land Cin) \lor (B \land Cin) \lor (A \land B \land Cin) \lor (A \land B \land Cin)
$$

Schritt 3: Gruppiere:

$$
Cout = (A \land B) \lor (A \land B \land Cin) \lor (A \land Cin \land \neg (A \land B)) \lor (B \land Cin \land \neg(A \land B))
$$

Das wird zu kompliziert. Nutzen wir die Wahrheitstabelle als Beweis (siehe oben).

**Intuitive Erklärung der vereinfachten Formel**:

Die Formel $(A \land B) \lor ((A \oplus B) \land Cin)$ sagt:
- Ein Übertrag entsteht, wenn **beide A und B wahr** sind (erster Term)
- ODER wenn **genau einer von A und B wahr** ist UND ein **Eingangsübertrag** vorliegt (zweiter Term)

Dies entspricht der Logik des Volladdierers: Wenn beide Bits gesetzt sind, haben wir sowieso einen Übertrag. Wenn nur eines gesetzt ist, hängt der Übertrag vom Eingangsübertrag ab.

**Häufige Fehler**:
- **Fehler bei (c)**: Überträge nicht korrekt weitergeben – der Cout jeder Stelle muss zum Cin der nächsten werden
- **Fehler bei (c)**: Reihenfolge vertauschen – immer von rechts (niederwertigste Stelle) nach links (höchstwertigste) rechnen
- **Fehler bei (d)**: XOR-Eigenschaft nicht erkennen – $(A \oplus B)$ ist genau dann 1, wenn nur einer der beiden Eingänge 1 ist

---

## Teil B: Python-Aufgaben - Lösungen

### Lösung P1: CNC-Kühlmitteltemperatur-Monitor

**Vollständiger Code**:
```python
# Kühlmitteltemperatur einlesen
temperatur = float(input("CNC-Kühlmittel-Temperatur (°C): "))

# Betriebsbereich bestimmen (mit verketteten Vergleichen)
if temperatur < 15:
    bereich = "❄️ Zu kalt"
    emoji = "❄️"
    beschreibung = "unter 15°C"
    empfehlung = "⚠️ Kühlmittel auf Betriebstemperatur bringen!"
elif 15 <= temperatur < 20:
    bereich = "🟡 Suboptimal kühl"
    emoji = "🟡"
    beschreibung = "15-19°C"
    empfehlung = "Betrieb möglich, aber nicht ideal"
elif 20 <= temperatur <= 28:
    bereich = "🟢 Optimal"
    emoji = "🟢"
    beschreibung = "20-28°C"
    empfehlung = "Betrieb freigegeben"
elif 28 < temperatur <= 35:
    bereich = "🟠 Suboptimal warm"
    emoji = "🟠"
    beschreibung = "28-35°C"
    empfehlung = "Erhöhter Verschleiß, Kühlmittelkühler prüfen"
else:  # temperatur > 35
    bereich = "🔴 Zu heiß"
    emoji = "🔴"
    beschreibung = "über 35°C"
    empfehlung = "⚠️ MASCHINE STOPPEN! Kühlmittel prüfen/tauschen!"

# Idealbereich prüfen (verketteter Vergleich)
im_idealbereich = 22 <= temperatur <= 26

# Ausgabe
print(f"Betriebsbereich: {bereich} ({beschreibung})")
print(f"Idealbereich (22-26°C): {'✅ Ja - Maximale Werkzeugstandzeit' if im_idealbereich else '❌ Nein'}")
print(f"Empfehlung: {empfehlung}")
```

**Beispiel-Ausgaben**:
```
CNC-Kühlmittel-Temperatur (°C): 24.5
Betriebsbereich: 🟢 Optimal (20-28°C)
Idealbereich (22-26°C): ✅ Ja - Maximale Werkzeugstandzeit
Empfehlung: Betrieb freigegeben
```

```
CNC-Kühlmittel-Temperatur (°C): 37.2
Betriebsbereich: 🔴 Zu heiß (über 35°C)
Idealbereich (22-26°C): ❌ Nein
Empfehlung: ⚠️ MASCHINE STOPPEN! Kühlmittel prüfen/tauschen!
```

**Erklärung**:

Zeile für Zeile Durchgang:

1. **Eingabe einlesen**: `float(input(...))` liest die Kühlmitteltemperatur als Fließkommazahl ein

2. **Bereichsprüfung mit elif-Kette**: Wir prüfen die Bereiche von niedrig zu hoch
   - `temperatur < 15`: Zu kalt für CNC-Betrieb (Kondensationsgefahr, schlechte Schmierwirkung)
   - `15 <= temperatur < 20`: Funktionsfähig, aber suboptimal (zähflüssig)
   - `20 <= temperatur <= 28`: **Optimaler Bereich** für beste Kühl- und Schmierwirkung
   - `28 < temperatur <= 35`: Zu warm, erhöhter Verschleiß, Ölanteil beginnt sich zu zersetzen
   - `else`: Kritisch heiß (> 35°C), Maschine muss gestoppt werden

3. **Idealbereich**: Ein verketteter Vergleich `22 <= temperatur <= 26` für die absolut beste Temperatur (VDI 3397 Empfehlung)

4. **Ausgabe**: f-Strings mit Emojis für bessere Visualisierung (wie auf modernen CNC-Bildschirmen)

**Warum diese Lösung?**

Die Verwendung von **verketteten Vergleichen** (`20 <= temperatur <= 28`) macht den Code deutlich lesbarer als verschachtelte `and`-Verknüpfungen. Die `elif`-Struktur stellt sicher, dass nur ein Bereich zutrifft (Bedingungen schließen sich gegenseitig aus). 

**Praxisbezug**:
- In echten CNC-Steuerungen (z.B. **Siemens SINUMERIK**, **Fanuc**) werden solche Temperaturüberwachungen permanent durchgeführt
- Bei Grenzwertüberschreitung: Automatischer **NOT-STOP** (EN 60204-1, Kategorie 0)
- **Kühlmittelkühler** (Chiller) regeln die Temperatur automatisch, aber Überwachung ist essentiell
- **VDI 3397**: Richtlinie für Kühlschmierstoffe in der Metallbearbeitung

**Häufige Fehler**:
- **Fehler**: Überlappende Bereiche – z.B. `temperatur >= 20` und dann `temperatur >= 28` würde für 30°C beide Bedingungen erfüllen
  - **Richtig**: Exklusive Bereiche mit `<` und `<=` kombinieren
- **Fehler**: Grenzwerte falsch – z.B. 28°C ist die obere Grenze des Optimalbereichs (inklusiv!)
  - **Richtig**: Aufgabenstellung genau lesen: "20°C bis 28°C **einschließlich**"
- **Fehler**: Verkettete Vergleiche falsch verstehen – `20 <= temperatur <= 28` ist NICHT das gleiche wie `20 <= temperatur or temperatur <= 28`
  - **Richtig**: Verkettete Vergleiche entsprechen `(20 <= temperatur) and (temperatur <= 28)`
- **Fehler**: Physikalische Plausibilität ignorieren – negative Temperaturen bei Kühlmittel sind möglich (Frostschutzmittel), aber unter -10°C unrealistisch für Betrieb

---

### Lösung P2: Hydraulikpress-Parameter-Validierung

**Vollständiger Code**:
```python
# Eingaben einlesen
print("=== HYDRAULIKPRESS-PARAMETER-VALIDIERUNG ===")
druck = float(input("Hydraulikdruck (bar): "))
geschwindigkeit = float(input("Pressengeschwindigkeit (mm/s): "))
werkzeug_id = input("Werkzeug-ID: ")
oel_temperatur = float(input("Öltemperatur (°C): "))

print("\n--- Validierungsergebnisse ---")

# Kriterium 1: Druckbereich prüfen (150-250 bar)
druck_ok = 150 <= druck <= 250
print(f"{'✅' if druck_ok else '❌'} Druckbereich {'erfüllt' if druck_ok else 'NICHT erfüllt'} (150-250 bar): {druck} bar")

# Kriterium 2: Geschwindigkeit prüfen (10-80 mm/s)
geschwindigkeit_ok = 10 <= geschwindigkeit <= 80
print(f"{'✅' if geschwindigkeit_ok else '❌'} Geschwindigkeit {'erfüllt' if geschwindigkeit_ok else 'NICHT erfüllt'} (10-80 mm/s): {geschwindigkeit} mm/s")

# Kriterium 3: Werkzeug-ID-Format prüfen
# - Mindestens 10 Zeichen
# - Enthält mindestens eine Ziffer
# - Enthält mindestens einen Bindestrich
werkzeug_laenge_ok = len(werkzeug_id) >= 10
werkzeug_hat_ziffer = any(c.isdigit() for c in werkzeug_id)
werkzeug_hat_bindestrich = "-" in werkzeug_id
werkzeug_id_ok = werkzeug_laenge_ok and werkzeug_hat_ziffer and werkzeug_hat_bindestrich

if werkzeug_id_ok:
    print(f"✅ Werkzeug-ID-Format korrekt (≥10 Zeichen, Ziffer, Bindestrich): {werkzeug_id}")
else:
    fehler = []
    if not werkzeug_laenge_ok:
        fehler.append(f"zu kurz: {len(werkzeug_id)} Zeichen")
    if not werkzeug_hat_ziffer:
        fehler.append("keine Ziffer")
    if not werkzeug_hat_bindestrich:
        fehler.append("kein Bindestrich")
    print(f"❌ Werkzeug-ID-Format UNGÜLTIG ({', '.join(fehler)})")

# Kriterium 4: Öltemperatur prüfen (40-60°C)
oel_temperatur_ok = 40 <= oel_temperatur <= 60
if oel_temperatur_ok:
    print(f"✅ Öltemperatur optimal (40-60°C): {oel_temperatur}°C")
else:
    if oel_temperatur < 40:
        print(f"❌ Öltemperatur außerhalb Sollbereich (40-60°C): {oel_temperatur}°C - ÖL ZU KALT!")
    else:
        print(f"❌ Öltemperatur außerhalb Sollbereich (40-60°C): {oel_temperatur}°C - ÖL ZU HEISS!")

# Kriterium 5: Sicherheitsregel prüfen
# Wenn Druck > 200 bar, dann muss Geschwindigkeit ≤ 50 mm/s sein
# Logisch äquivalent: (druck <= 200) OR (geschwindigkeit <= 50)
sicherheitsregel_ok = (druck <= 200) or (geschwindigkeit <= 50)
if sicherheitsregel_ok:
    print(f"✅ Sicherheitsregel erfüllt (Druck ≤200 bar ODER Geschwindigkeit ≤50 mm/s)")
else:
    print(f"❌ Sicherheitsregel VERLETZT (Druck >200 bar UND Geschwindigkeit >50 mm/s)")
    print(f"   ⚠️ GEFAHR: Hoher Druck ({druck} bar) + Hohe Geschwindigkeit ({geschwindigkeit} mm/s)")

# Gesamtbewertung
alle_kriterien_erfuellt = (druck_ok and geschwindigkeit_ok and werkzeug_id_ok and 
                           oel_temperatur_ok and sicherheitsregel_ok)

# Anzahl erfüllter Kriterien zählen
kriterien_erfuellt = sum([druck_ok, geschwindigkeit_ok, werkzeug_id_ok, 
                          oel_temperatur_ok, sicherheitsregel_ok])
kriterien_gesamt = 5

print()
if alle_kriterien_erfuellt:
    print("➡️ BETRIEB FREIGEGEBEN ✅")
    print("Alle Parameter im Sollbereich. Pressung kann gestartet werden.")
else:
    print(f"➡️ BETRIEB GESPERRT ❌")
    print(f"{kriterien_gesamt - kriterien_erfuellt} Kriterien nicht erfüllt. Presse darf NICHT gestartet werden!")
```

**Beispiel-Ausgaben**:

**Szenario 1: Alle Kriterien erfüllt**
```
=== HYDRAULIKPRESS-PARAMETER-VALIDIERUNG ===
Hydraulikdruck (bar): 180.5
Pressengeschwindigkeit (mm/s): 45.0
Werkzeug-ID: WZ-2024-A15
Öltemperatur (°C): 52.3

--- Validierungsergebnisse ---
✅ Druckbereich erfüllt (150-250 bar): 180.5 bar
✅ Geschwindigkeit erfüllt (10-80 mm/s): 45.0 mm/s
✅ Werkzeug-ID-Format korrekt (≥10 Zeichen, Ziffer, Bindestrich): WZ-2024-A15
✅ Öltemperatur optimal (40-60°C): 52.3°C
✅ Sicherheitsregel erfüllt (Druck ≤200 bar ODER Geschwindigkeit ≤50 mm/s)

➡️ BETRIEB FREIGEGEBEN ✅
Alle Parameter im Sollbereich. Pressung kann gestartet werden.
```

**Szenario 2: Mehrere Kriterien verletzt**
```
=== HYDRAULIKPRESS-PARAMETER-VALIDIERUNG ===
Hydraulikdruck (bar): 230.0
Pressengeschwindigkeit (mm/s): 75.0
Werkzeug-ID: ABC123
Öltemperatur (°C): 68.5

--- Validierungsergebnisse ---
✅ Druckbereich erfüllt (150-250 bar): 230.0 bar
✅ Geschwindigkeit erfüllt (10-80 mm/s): 75.0 mm/s
❌ Werkzeug-ID-Format UNGÜLTIG (zu kurz: 6 Zeichen, kein Bindestrich)
❌ Öltemperatur außerhalb Sollbereich (40-60°C): 68.5°C - ÖL ZU HEISS!
❌ Sicherheitsregel VERLETZT (Druck >200 bar UND Geschwindigkeit >50 mm/s)
   ⚠️ GEFAHR: Hoher Druck (230.0 bar) + Hohe Geschwindigkeit (75.0 mm/s)

➡️ BETRIEB GESPERRT ❌
3 Kriterien nicht erfüllt. Presse darf NICHT gestartet werden!
```

**Erklärung**:

**Kriterien-Prüfung**:

1. **Druckbereich**: Verketteter Vergleich `150 <= druck <= 250` prüft, ob Druck im Nenndruck-Bereich der Presse liegt (EN 693)

2. **Geschwindigkeit**: `10 <= geschwindigkeit <= 80` stellt sicher, dass die Presse nicht zu langsam (Produktivitätsverlust) oder zu schnell (Sicherheitsrisiko) fährt

3. **Werkzeug-ID-Format**: Drei Bedingungen mit AND verknüpft:
   - `len(werkzeug_id) >= 10`: Mindestlänge für aussagekräftige IDs
   - `any(c.isdigit() for c in werkzeug_id)`: Muss Ziffern enthalten (Jahreszahl, Laufnummer)
   - `"-" in werkzeug_id`: Bindestriche für strukturierte IDs (z.B. WZ-2024-A15)

4. **Öltemperatur**: Optimaler Viskositätsbereich 40-60°C
   - Zu kalt (< 40°C): Öl zu zähflüssig, schlechte Druckübertragung
   - Zu heiß (> 60°C): Öl zu dünnflüssig, Leckagen, thermische Belastung

5. **Sicherheitsregel (IMPLIKATION)**: 
   - Regel: "**Wenn** Druck > 200 bar, **dann** Geschwindigkeit ≤ 50 mm/s"
   - Logisch äquivalent: `(druck <= 200) OR (geschwindigkeit <= 50)`
   - Verhindert gefährliche Kombination aus hohem Druck und hoher Geschwindigkeit (hohe kinetische Energie)

**Schritt-für-Schritt Durchlauf** (Beispiel: Druck=230 bar, Geschwindigkeit=75 mm/s):

1. `druck_ok = 150 <= 230 <= 250` → `True` (im Bereich)
2. `geschwindigkeit_ok = 10 <= 75 <= 80` → `True` (im Bereich)
3. Werkzeug-ID "ABC123":
   - `len("ABC123") = 6` → `False` (zu kurz)
   - `any(c.isdigit() for c in "ABC123")` → `True` ('1','2','3' sind Ziffern)
   - `"-" in "ABC123"` → `False` (kein Bindestrich)
   - `werkzeug_id_ok = False and True and False` → `False`
4. `oel_temperatur_ok = 40 <= 68.5 <= 60` → `False` (zu heiß)
5. **Sicherheitsregel**:
   - `(230 <= 200) or (75 <= 50)`
   - `False or False` → `False` ❌
   - Beide Bedingungen verletzt: Druck UND Geschwindigkeit zu hoch!
6. `alle_kriterien_erfuellt = True and True and False and False and False` → `False`

**Praxisbezug**:
- **EN 693**: Europäische Norm für Sicherheit hydraulischer Pressen
- **Traceability**: Werkzeug-IDs ermöglichen Rückverfolgung bei Qualitätsproblemen (ISO 9001)
- **Risikobeurteilung**: Kombination aus hohem Druck und Geschwindigkeit erhöht Unfallrisiko exponentiell
- **Hydrauliköl**: Temperaturabhängige Viskosität ist kritisch für präzise Druckregelung

**Häufige Fehler**:
- **Fehler**: Implikation falsch umsetzen – `(druck > 200) and (geschwindigkeit <= 50)` ist NICHT korrekt!
  - **Richtig**: `(druck <= 200) or (geschwindigkeit <= 50)` (Kontraposition der Implikation)
- **Fehler**: `any()` Funktion nicht verstehen – `c.isdigit()` prüft jedes Zeichen einzeln
- **Fehler**: `"-" in werkzeug_id` mit `.isdigit()` verwechseln – `in` prüft Substring-Vorkommen
- **Fehler**: Fehlerausgabe nicht ausführlich genug – Bediener muss genau wissen, WAS falsch ist
- **Fehler**: `sum()` auf Boolean-Liste – funktioniert, weil `True = 1`, `False = 0` in Python

---

### Lösung P3: Sensor-Plausibilitätsprüfung mit Kurzschlussauswertung

**Vollständiger Code**:
```python
# Teil 1: Kurzschlussauswertung demonstrieren
def pruefe_sensor_a():
    print("🟢 Sensor A: Drucksensor wird abgefragt...")
    return True  # Sensor funktioniert

def pruefe_sensor_b():
    print("🔴 Sensor B: Temperatursensor wird abgefragt...")
    return False  # Sensor defekt

print("=== TEIL 1: Kurzschlussauswertung demonstrieren ===\n")

# Test 1: pruefe_sensor_a() and pruefe_sensor_b()
print("Test 1: pruefe_sensor_a() and pruefe_sensor_b()")
result = pruefe_sensor_a() and pruefe_sensor_b()
print(f"➡️ Ergebnis: {result} (beide Sensoren geprüft)\n")

# Test 2: pruefe_sensor_b() and pruefe_sensor_a()
print("Test 2: pruefe_sensor_b() and pruefe_sensor_a()")
result = pruefe_sensor_b() and pruefe_sensor_a()
print(f"➡️ Ergebnis: {result} (Sensor A wurde NICHT geprüft, weil B bereits False ist!)\n")

# Test 3: pruefe_sensor_a() or pruefe_sensor_b()
print("Test 3: pruefe_sensor_a() or pruefe_sensor_b()")
result = pruefe_sensor_a() or pruefe_sensor_b()
print(f"➡️ Ergebnis: {result} (Sensor B wurde NICHT geprüft, weil A bereits True ist!)\n")

# Test 4: pruefe_sensor_b() or pruefe_sensor_a()
print("Test 4: pruefe_sensor_b() or pruefe_sensor_a()")
result = pruefe_sensor_b() or pruefe_sensor_a()
print(f"➡️ Ergebnis: {result} (beide geprüft)\n")

# Teil 2: Sichere Druck-Berechnung
print("=" * 70)
print("=== TEIL 2: Sichere Druck-Berechnung ===")
print("=" * 70)

def berechne_druck(kraft_N, flaeche_m2):
    """
    Berechnet Druck in bar aus Kraft (N) und Fläche (m²).
    Formel: p = F/A, mit 1 bar = 10^5 Pa = 10^5 N/m²
    
    Nutzt Kurzschlussauswertung zur Vermeidung von Division durch Null.
    """
    if flaeche_m2 > 0:
        # Umrechnung: Pa → bar (dividiere durch 100000)
        druck_bar = (kraft_N / flaeche_m2) / 100000
        return druck_bar
    else:
        print("⚠️ Fehler: Ungültige Fläche (muss > 0 sein)")
        return None

# Tests
print("\nBerechne Druck: F=50000 N, A=0.01 m²")
druck1 = berechne_druck(50000, 0.01)
print(f"➡️ Druck: {druck1} bar\n")

print("Berechne Druck: F=50000 N, A=0 m²")
druck2 = berechne_druck(50000, 0)
print(f"➡️ Druck: {druck2} (Division vermieden durch Kurzschluss)\n")

print("Berechne Druck: F=150000 N, A=0.005 m²")
druck3 = berechne_druck(150000, 0.005)
print(f"➡️ Druck: {druck3} bar\n")

# Teil 3: Grenzwertüberwachung mit Kurzschluss
print("=" * 70)
print("=== TEIL 3: Grenzwertüberwachung ===")
print("=" * 70)

def pruefe_betriebsparameter(druck_bar, temperatur_C):
    """
    Prüft Betriebsparameter einer Hydraulikanlage.
    - Druck: 100-300 bar
    - Temperatur: 20-80°C
    
    Nutzt Kurzschlussauswertung: Wenn Druck außerhalb, keine Temperaturprüfung.
    """
    print(f"\nPrüfe Parameter: Druck={druck_bar} bar, Temperatur={temperatur_C}°C")
    
    druck_ok = 100 <= druck_bar <= 300
    
    if druck_ok:
        print(f"✅ Druck im Sollbereich (100-300 bar)")
        
        temperatur_ok = 20 <= temperatur_C <= 80
        if temperatur_ok:
            print(f"✅ Temperatur im Sollbereich (20-80°C)")
            print("➡️ Betriebsparameter OK")
            return True
        else:
            print(f"❌ Temperatur außerhalb Sollbereich ({temperatur_C}°C nicht in 20-80°C)")
            print("➡️ Betriebsparameter NICHT OK")
            return False
    else:
        if druck_bar < 100:
            print(f"❌ Druck zu niedrig ({druck_bar} bar < 100 bar)")
        else:
            print(f"❌ Druck zu hoch ({druck_bar} bar > 300 bar)")
        print("➡️ Temperaturprüfung übersprungen (Kurzschlussauswertung)")
        print("➡️ Betriebsparameter NICHT OK")
        return False

# Tests
pruefe_betriebsparameter(150, 55)
pruefe_betriebsparameter(350, 55)  # Druck zu hoch, Temp wird nicht geprüft
pruefe_betriebsparameter(200, 95)  # Druck OK, aber Temp zu hoch
pruefe_betriebsparameter(80, 50)   # Druck zu niedrig, Temp wird nicht geprüft
```

**Erklärung**:

**Teil 1 – Kurzschlussauswertung bei AND/OR**:

- **Test 1** (`pruefe_sensor_a() and pruefe_sensor_b()`):
  - Beide Funktionen werden aufgerufen, da `True and ?` noch unbestimmt ist
  - Ergebnis: `True and False = False`

- **Test 2** (`pruefe_sensor_b() and pruefe_sensor_a()`):
  - Nur `pruefe_sensor_b()` wird aufgerufen → `False`
  - `pruefe_sensor_a()` wird **NICHT** aufgerufen (Kurzschluss!)
  - Grund: `False and ...` ist immer `False`, rechte Seite ist irrelevant
  - **Praxisvorteil**: Keine unnötige Sensorabfrage (spart Zeit, reduziert Bus-Last)

- **Test 3** (`pruefe_sensor_a() or pruefe_sensor_b()`):
  - Nur `pruefe_sensor_a()` wird aufgerufen → `True`
  - `pruefe_sensor_b()` wird **NICHT** aufgerufen (Kurzschluss!)
  - Grund: `True or ...` ist immer `True`, rechte Seite ist irrelevant
  - **Praxisvorteil**: Reduzierter I/O-Zugriff, schnellere Auswertung

- **Test 4** (`pruefe_sensor_b() or pruefe_sensor_a()`):
  - Beide Funktionen werden aufgerufen
  - `False or True = True`

**Teil 2 – Sichere Druck-Berechnung**:

Die Funktion `berechne_druck()` nutzt eine if-Bedingung zur sicheren Division:

```python
if flaeche_m2 > 0:
    druck_bar = (kraft_N / flaeche_m2) / 100000
    return druck_bar
else:
    return None
```

**Warum ist das wichtig?**
- Ohne Prüfung: `kraft_N / 0` → `ZeroDivisionError` → Programmabsturz
- Mit Prüfung: Division wird nur ausgeführt, wenn `flaeche_m2 > 0`
- In SPS-Programmierung: Division-by-Zero kann gesamte Steuerung stoppen!

**Formel-Herleitung**:
$$p = \frac{F}{A}$$

- $F$ in Newton [N]
- $A$ in Quadratmeter [m²]
- $p$ in Pascal [Pa] = N/m²

Umrechnung zu bar:
$$1 \text{ bar} = 10^5 \text{ Pa} = 100000 \text{ N/m}^2$$

Beispiel: F = 50000 N, A = 0.01 m²
$$p = \frac{50000}{0.01} = 5000000 \text{ Pa} = 50 \text{ bar}$$

**Teil 3 – Grenzwertüberwachung**:

Die Funktion prüft **ERST** den Druck, **DANN** (nur bei OK) die Temperatur:

```python
druck_ok = 100 <= druck_bar <= 300

if druck_ok:
    # Temperatur wird NUR geprüft, wenn Druck OK ist
    temperatur_ok = 20 <= temperatur_C <= 80
```

**Praxisrelevanz**:
- In echten SPS-Programmen: Priorität der Prüfungen
- Kritische Parameter (Druck) zuerst prüfen
- Weniger kritische Parameter (Temperatur) nur bei Bedarf
- **Performance-Optimierung**: Keine unnötigen Berechnungen

**Konzepte in dieser Lösung**:
- **Kurzschlussauswertung**: Python wertet logische Operatoren lazy aus (nur so weit wie nötig)
- **Defensive Programmierung**: Division-by-Zero abfangen
- **Priorisierte Validierung**: Wichtige Checks zuerst
- **Return Early**: Bei Fehler sofort zurückkehren, nicht weitermachen

**Häufige Fehler**:
- **Fehler**: Denken, dass beide Operanden von `and`/`or` immer ausgewertet werden
  - **Falsch**: Python stoppt sobald Ergebnis feststeht
- **Fehler**: Reihenfolge bei `if flaeche_m2 > 0` vergessen
  - **Folge**: Division wird trotzdem ausgeführt → Absturz
- **Fehler**: Ternären Operator falsch herum: `a/b if b != 0 else None` crasht bei b=0
  - **Richtig**: `None if b == 0 else a/b` (Bedingung wird ZUERST geprüft)
- **Fehler**: In SPS-Logik: Alle Sensoren immer abfragen (unnötiger Overhead)
  - **Richtig**: Kurzschluss nutzen für performante Steuerungsprogramme

**Praxisbezug Maschinenbau**:
- **CAN-Bus**: Sensoren liefern Daten zyklisch, aber nicht alle Daten sind immer relevant
- **SPS-Zykluszeit**: Typisch 1-10 ms, jede unnötige Operation kostet Zeit
- **Profibus/Profinet**: Kurzschluss reduziert Bus-Last
- **Safety PLCs**: Kritische Sensoren (Not-Aus) haben Vorrang vor nicht-kritischen (Temperatur)

---
    # Kurzschlussauswertung: Wenn b == 0, wird a/b NICHT ausgewertet
    return None if b == 0 else a / b

# Tests
print(f"sichere_division(10, 2) = {sichere_division(10, 2)}")    # 5.0
print(f"sichere_division(10, 0) = {sichere_division(10, 0)}")    # None
print(f"sichere_division(7, 3) = {sichere_division(7, 3)}")      # 2.333...
print(f"sichere_division(0, 5) = {sichere_division(0, 5)}")      # 0.0
print(f"sichere_division(0, 0) = {sichere_division(0, 0)}")      # None

# Alternative mit if-else statt ternärem Operator
def sichere_division_v2(a, b):
    """Alternative Implementierung mit expliziter if-Abfrage."""
    if b == 0:
        return None
    else:
        return a / b

print(f"\nsichere_division_v2(10, 0) = {sichere_division_v2(10, 0)}")  # None
```

**Erklärung**:

**Tests 1-4 demonstrieren Kurzschlussauswertung**:

- **Test 1** (`check_a() and check_b()`):
  - `check_a()` wird aufgerufen → gibt `True` zurück
  - Da `True and ...` noch nicht feststeht, wird `check_b()` auch aufgerufen → gibt `False` zurück
  - Ergebnis: `True and False` = `False`
  - **Beide Funktionen wurden aufgerufen**

- **Test 2** (`check_b() and check_a()`):
  - `check_b()` wird aufgerufen → gibt `False` zurück
  - Da `False and ...` **immer** `False` ist, wird `check_a()` **NICHT** aufgerufen
  - Ergebnis: `False` (Kurzschluss!)
  - **Nur check_b wurde aufgerufen**

- **Test 3** (`check_a() or check_b()`):
  - `check_a()` wird aufgerufen → gibt `True` zurück
  - Da `True or ...` **immer** `True` ist, wird `check_b()` **NICHT** aufgerufen
  - Ergebnis: `True` (Kurzschluss!)
  - **Nur check_a wurde aufgerufen**

- **Test 4** (`check_b() or check_a()`):
  - `check_b()` wird aufgerufen → gibt `False` zurück
  - Da `False or ...` noch nicht feststeht, wird `check_a()` auch aufgerufen → gibt `True` zurück
  - Ergebnis: `False or True` = `True`
  - **Beide Funktionen wurden aufgerufen**

**Zusatzaufgabe – Sichere Division**:

```python
return None if b == 0 else a / b
```

Diese Zeile nutzt Kurzschlussauswertung im ternären Operator:
1. Zuerst wird `b == 0` geprüft
2. **Falls wahr**: Rückgabe `None` – die Division `a / b` wird **nie ausgeführt**
3. **Falls falsch**: Rückgabe `a / b` – Division wird durchgeführt

**Warum ist das wichtig?**

Ohne Kurzschlussauswertung würde folgender Code crashen:
```python
# FALSCH (crasht bei b=0):
result = a / b if b != 0 else None
# Python würde a/b ZUERST auswerten, DANN die Bedingung prüfen → ZeroDivisionError!
```

**Richtige Reihenfolge** bei ternärem Operator:
```python
wert_wenn_wahr if bedingung else wert_wenn_falsch
```

**Alternative mit klassischer if-else**:
```python
if b == 0:
    return None
else:
    return a / b
```

Dies ist expliziter und für Anfänger oft leichter lesbar. Der ternäre Operator ist kompakter für einfache Fälle.

**Konzepte in dieser Lösung**:
- **Kurzschlussauswertung**: Python wertet `and`/`or` nur so weit aus, wie nötig
- **Funktionen als Demonstrationswerkzeug**: Seiteneffekte (print) machen Auswertungsreihenfolge sichtbar
- **Ternärer Operator**: Kompakte Schreibweise für einfache if-else-Konstrukte
- **Defensive Programmierung**: Fehlerhafte Eingaben abfangen, bevor sie Probleme verursachen

**Häufige Fehler**:
- **Fehler**: Denken, dass `check_a() and check_b()` beide Funktionen immer aufruft
  - **Warum falsch**: Bei `False and ...` wird der rechte Teil nicht mehr ausgewertet
- **Fehler**: Ternären Operator falsch herum schreiben
  - **Falsch**: `if b == 0: None else a / b` (falsche Syntax)
  - **Richtig**: `None if b == 0 else a / b`
- **Fehler**: Reihenfolge bei sicherer Division vertauschen
  - **Falsch**: `a / b if b != 0 else None` würde bei b=0 crashen (Division wird zuerst ausgewertet!)
  - **Richtig**: `None if b == 0 else a / b`

---

### Lösung P4: Maschinenbedien-Berechtigungssystem

**Vollständiger Code**:
```python
# Eingaben einlesen
print("=== MASCHINENBEDIEN-BERECHTIGUNGSSYSTEM ===")
qualifikation = input("Qualifikation: ")  # Meister, Fachkraft, Angelernt, Auszubildender
uhrzeit = int(input("Uhrzeit (Stunde 0-23): "))
schicht = input("Schicht: ")  # Frühschicht, Spätschicht, Nachtschicht
zusatzschulung = input("Zusatzschulung absolviert (Ja/Nein): ")

# Normalisierung
qualifikation = qualifikation.capitalize()
schicht = schicht.capitalize()
zusatzschulung_absolviert = zusatzschulung.lower() in ["ja", "j", "yes", "y", "1"]

# Hilfsvariablen
ist_meister = qualifikation == "Meister"
ist_fachkraft = qualifikation == "Fachkraft"
ist_angelernt = qualifikation == "Angelernt"
ist_auszubildender = qualifikation == "Auszubildender"

ist_fruehschicht = 6 <= uhrzeit < 14
ist_spaetschicht = 14 <= uhrzeit < 22
ist_nachtschicht = uhrzeit >= 22 or uhrzeit < 6
ist_tagschicht = 6 <= uhrzeit < 22

print("\n--- Bedienberechtigungen ---\n")

# 1. Handwerkzeuge/Montage: Alle Qualifikationen
handwerkzeug_berechtigt = True
print(f"✅ Handwerkzeuge/Montage: Bedienung erlaubt (allgemeiner Zugang)")

# 2. Konventionelle Drehmaschine
if ist_meister:
    drehmaschine_berechtigt = True
    grund = "Meister hat volle Berechtigung"
elif ist_fachkraft and ist_tagschicht:
    drehmaschine_berechtigt = True
    grund = "Fachkraft, Tagschicht (6-22 Uhr)"
elif ist_angelernt and ist_fruehschicht and zusatzschulung_absolviert:
    drehmaschine_berechtigt = True
    grund = "Angelernt, Frühschicht, Zusatzschulung vorhanden"
elif ist_auszubildender and zusatzschulung_absolviert and not ist_nachtschicht:
    drehmaschine_berechtigt = True
    grund = "Auszubildender mit Zusatzschulung, nicht Nachtschicht (Aufsicht erforderlich)"
else:
    drehmaschine_berechtigt = False
    if ist_angelernt and not zusatzschulung_absolviert:
        grund = "Zusatzschulung erforderlich"
    elif ist_auszubildender and not zusatzschulung_absolviert:
        grund = "Zusatzschulung und Aufsicht erforderlich"
    elif ist_nachtschicht:
        grund = "Nachtschicht nicht erlaubt für diese Qualifikation"
    else:
        grund = "Qualifikation nicht ausreichend"

print(f"{'✅' if drehmaschine_berechtigt else '❌'} Konventionelle Drehmaschine: Bedienung {'erlaubt' if drehmaschine_berechtigt else 'NICHT erlaubt'} ({grund})")

# 3. CNC-Bearbeitungszentrum (5-Achsen)
cnc_berechtigt = (ist_meister or (ist_fachkraft and zusatzschulung_absolviert)) and not ist_nachtschicht

if cnc_berechtigt:
    if ist_meister:
        grund = "Meister, Tagschicht"
    else:
        grund = "Fachkraft mit 5-Achsen-Schulung, Tagschicht"
else:
    if ist_nachtschicht:
        grund = "CNC 5-Achsen nicht in Nachtschicht (zu komplex ohne erweiterte Überwachung)"
    elif ist_fachkraft and not zusatzschulung_absolviert:
        grund = "5-Achsen-Zusatzschulung erforderlich"
    else:
        grund = "Nur Meister/Fachkraft mit Zusatzschulung"

print(f"{'✅' if cnc_berechtigt else '❌'} CNC-Bearbeitungszentrum 5-Achsen: Bedienung {'erlaubt' if cnc_berechtigt else 'NICHT erlaubt'} ({grund})")

# 4. Brückenkran (>10t)
if ist_meister:
    kran_berechtigt = True
    grund = "Meister hat Kranschein"
elif ist_fachkraft and zusatzschulung_absolviert:
    kran_berechtigt = True
    grund = "Fachkraft mit Kranschein (DGUV 52)"
else:
    kran_berechtigt = False
    if ist_angelernt or ist_auszubildender:
        grund = "DGUV 52: Kranführer müssen ≥18 Jahre, ausgebildet und beauftragt sein"
    else:
        grund = "Kranschein (Zusatzschulung) erforderlich"

print(f"{'✅' if kran_berechtigt else '❌'} Brückenkran >10t: Bedienung {'erlaubt' if kran_berechtigt else 'NICHT erlaubt'} ({grund})")

# 5. Schweißroboter
if ist_meister:
    roboter_berechtigt = True
    grund = "Meister hat volle Roboter-Programmierung"
elif ist_fachkraft and (ist_fruehschicht or ist_spaetschicht) and zusatzschulung_absolviert:
    roboter_berechtigt = True
    grund = "Fachkraft, Tagschicht, Roboter-Schulung vorhanden"
else:
    roboter_berechtigt = False
    if ist_angelernt or ist_auszubildender:
        grund = "Roboter-Programmierung nur für Meister/Fachkraft"
    elif ist_nachtschicht:
        grund = "Roboter-Bedienung nicht in Nachtschicht"
    else:
        grund = "Roboter-Schulung erforderlich"

print(f"{'✅' if roboter_berechtigt else '❌'} Schweißroboter: Bedienung {'erlaubt' if roboter_berechtigt else 'NICHT erlaubt'} ({grund})")

# Zusammenfassung
print("\n" + "=" * 70)
berechtigte_maschinen = sum([handwerkzeug_berechtigt, drehmaschine_berechtigt, 
                             cnc_berechtigt, kran_berechtigt, roboter_berechtigt])
print(f"➡️ Zugriff auf {berechtigte_maschinen} von 5 Maschinen")

if berechtigte_maschinen == 5:
    print("✅ Alle Maschinen freigegeben für diese Person")
elif berechtigte_maschinen == 1:
    print("⚠️ Beschränkung auf Montagearbeitsplatz und Handwerkzeuge")

# Zusätzliche Warnungen
if ist_auszubildender and ist_nachtschicht:
    print("⚠️ WARNUNG: Nachtschicht-Arbeit für Auszubildende unter 18 Jahren verboten (JArbSchG §14)!")
```

**Beispiel-Ausgaben**:

**Szenario 1: Fachkraft, Frühschicht, mit Zusatzschulung**
```
=== MASCHINENBEDIEN-BERECHTIGUNGSSYSTEM ===
Qualifikation: Fachkraft
Uhrzeit (Stunde 0-23): 10
Schicht: Frühschicht
Zusatzschulung absolviert (Ja/Nein): Ja

--- Bedienberechtigungen ---

✅ Handwerkzeuge/Montage: Bedienung erlaubt (allgemeiner Zugang)
✅ Konventionelle Drehmaschine: Bedienung erlaubt (Fachkraft, Tagschicht (6-22 Uhr))
✅ CNC-Bearbeitungszentrum 5-Achsen: Bedienung erlaubt (Fachkraft mit 5-Achsen-Schulung, Tagschicht)
✅ Brückenkran >10t: Bedienung erlaubt (Fachkraft mit Kranschein (DGUV 52))
✅ Schweißroboter: Bedienung erlaubt (Fachkraft, Tagschicht, Roboter-Schulung vorhanden)

======================================================================
➡️ Zugriff auf 5 von 5 Maschinen
✅ Alle Maschinen freigegeben für diese Person
```

**Szenario 2: Auszubildender, Nachtschicht, keine Zusatzschulung**
```
=== MASCHINENBEDIEN-BERECHTIGUNGSSYSTEM ===
Qualifikation: Auszubildender
Uhrzeit (Stunde 0-23): 23
Schicht: Nachtschicht
Zusatzschulung absolviert (Ja/Nein): Nein

--- Bedienberechtigungen ---

✅ Handwerkzeuge/Montage: Bedienung erlaubt (allgemeiner Zugang)
❌ Konventionelle Drehmaschine: Bedienung NICHT erlaubt (Zusatzschulung und Aufsicht erforderlich)
❌ CNC-Bearbeitungszentrum 5-Achsen: Bedienung NICHT erlaubt (CNC 5-Achsen nicht in Nachtschicht)
❌ Brückenkran >10t: Bedienung NICHT erlaubt (DGUV 52: Kranführer müssen ≥18 Jahre, ausgebildet)
❌ Schweißroboter: Bedienung NICHT erlaubt (Roboter-Programmierung nur für Meister/Fachkraft)

======================================================================
➡️ Zugriff auf 1 von 5 Maschinen
⚠️ Beschränkung auf Montagearbeitsplatz und Handwerkzeuge
⚠️ WARNUNG: Nachtschicht-Arbeit für Auszubildende unter 18 Jahren verboten (JArbSchG §14)!
```

**Erklärung**:

**Struktur der Lösung**:

1. **Normalisierung**: Eingaben werden für robuste Vergleiche normalisiert
2. **Hilfsvariablen**: Rollen und Schichtzeiten werden in Boolean-Variablen übersetzt
3. **Maschinenkategorien**: Jede Maschine hat eigene Berechtigungslogik mit `if-elif-else`
4. **Begründungen**: Für jede Entscheidung wird ein `grund` gespeichert (wichtig für Transparenz)

**Logik-Analyse am Beispiel CNC 5-Achsen**:

```python
cnc_berechtigt = (ist_meister or (ist_fachkraft and zusatzschulung_absolviert)) and not ist_nachtschicht
```

Analyse:
- **Erste Klammer**: `ist_meister or (ist_fachkraft and zusatzschulung_absolviert)`
  - Meister sind immer berechtigt ODER
  - Fachkraft mit Zusatzschulung ist berechtigt
- **AND Verknüpfung**: `... and not ist_nachtschicht`
  - Aber NICHT in Nachtschicht (zu komplex ohne Aufsicht)

**Wahrheitstabelle (vereinfacht)**:

| Meister | Fachkraft+Schulung | Nachtschicht | Berechtigt |
|---------|-------------------|--------------|------------|
| True    | -                 | False        | True       |
| True    | -                 | True         | False      |
| False   | True              | False        | True       |
| False   | True              | True         | False      |
| False   | False             | False        | False      |

**Praxisbezug**:
- **BetrSichV §12**: Unterweisung und Beauftragung von Beschäftigten
- **DGUV Vorschrift 52**: Krane - Kranführer müssen schriftlich beauftragt sein
- **JArbSchG §14**: Jugendliche dürfen nicht in Nachtschicht (20-6 Uhr) arbeiten
- **ISO 12100**: Risikobeurteilung - höhere Qualifikation bei komplexen/gefährlichen Maschinen

**Häufige Fehler**:
- **Fehler**: Schichtzeiten überschneiden sich – z.B. 14 Uhr sowohl Früh- als auch Spätschicht
  - **Richtig**: Exklusive Grenzen mit `<` und `>=` setzen
- **Fehler**: `ist_fachkraft and zusatzschulung_absolviert or ist_meister` ohne Klammern
  - **Falsch interpretiert**: `(ist_fachkraft and zusatzschulung_absolviert) or ist_meister` (korrekt)
  - **Könnte sein**: `ist_fachkraft and (zusatzschulung_absolviert or ist_meister)` (falsch!)
  - **Lösung**: Immer Klammern setzen für Klarheit!
- **Fehler**: Zusatzwarnung für Auszubildende vergessen (JArbSchG)

---


- **Lesbarkeit**: Durch Hilfsvariablen ist sofort klar, was geprüft wird
- **Wartbarkeit**: Zeitfenster können zentral geändert werden
- **Erweiterbarkeit**: Neue Rollen oder Bereiche lassen sich leicht hinzufügen
- **Debugging**: Jeder Bereich ist isoliert – Fehler lassen sich leicht lokalisieren

**Schritt-für-Schritt Durchlauf** (Beispiel: Praktikant, 15 Uhr, Mittwoch):

1. Eingaben: `rolle="Praktikant"`, `uhrzeit=15`, `wochentag="Mittwoch"`, `sondererlaubnis=False`
2. Hilfsvariablen:
   - `ist_werktag = True` (Mittwoch ist Werktag)
   - `ist_geschaeftszeit = True` (15 liegt in [8, 18])
   - `ist_erweiterte_oeffnungszeit = True` (15 liegt in [6, 20])
   - `ist_garage_offen = True` (15 liegt in [6, 22])
   - `ist_praktikant = True`
3. Empfang: `True` (alle haben Zugang)
4. Bürobereich:
   - `ist_admin`? Nein
   - `ist_mitarbeiter and ...`? Nein (ist Praktikant)
   - `ist_praktikant and ist_werktag and ist_geschaeftszeit`? **Ja** → `buero_zugang = True`
5. Serverraum:
   - `ist_admin or (ist_mitarbeiter and sondererlaubnis)`? Nein → `serverraum_zugang = False`
6. Tiefgarage:
   - `ist_admin`? Nein
   - `(ist_mitarbeiter or ist_praktikant) and ist_werktag and ist_garage_offen`? **Ja** → `garage_zugang = True`

**Design-Entscheidungen**:

1. **Warum `in [...]` statt mehrfache OR?**
   ```python
   # Lesbar und kompakt:
   ist_werktag = wochentag in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
   
   # Alternative (umständlich):
   ist_werktag = wochentag == "Montag" or wochentag == "Dienstag" or ...
   ```

2. **Warum separate Grund-Variable?**
   - Ermöglicht detailliertes Feedback für den Benutzer
   - Erleichtert Debugging (man sieht, welche Bedingung fehlschlug)

3. **Warum Hierarchie bei Bürobereich?**
   - Admin-Check zuerst (häufigster Sonderfall)
   - Dann spezifischere Rollen
   - `else` fängt alle anderen Fälle ab

**Alternative Lösungsansätze**:

**Ansatz 1: Dictionary-basierte Regeln** (fortgeschrittener):
```python
regeln = {
    "Empfang": lambda: True,
    "Bürobereich": lambda: ist_admin or 
                           (ist_mitarbeiter and ist_werktag and ist_erweiterte_oeffnungszeit) or
                           (ist_praktikant and ist_werktag and ist_geschaeftszeit) or
                           (ist_gast and sondererlaubnis),
    # ...
}
```
✅ Vorteile: Kompakter, leicht erweiterbar  
❌ Nachteile: Schwerer zu debuggen, keine spezifischen Fehlermeldungen

**Ansatz 2: Klassen-basiert** (objektorientiert, V10+):
```python
class Benutzer:
    def __init__(self, rolle, uhrzeit, wochentag, sondererlaubnis):
        # ...
    
    def hat_zugang_buerobereich(self):
        # ...
```
✅ Vorteile: Sehr sauber strukturiert, testbar  
❌ Nachteile: Overkill für diese Aufgabe, benötigt OOP-Kenntnisse

**Häufige Fehler**:
- **Fehler**: Logik-Reihenfolge falsch – z.B. Gast vor Admin prüfen
  - **Warum problematisch**: Wenn Admin-Rechte später geprüft werden, greift vorher schon die restriktivere Regel
  - **Richtig**: Von großzügigsten (Admin) zu restriktivsten Regeln
- **Fehler**: Zeitbereiche mit `and` statt verketteten Vergleichen
  - **Unpythonisch**: `uhrzeit >= 8 and uhrzeit <= 18`
  - **Pythonisch**: `8 <= uhrzeit <= 18`
- **Fehler**: Case-Sensitivity nicht behandeln
  - Eingabe "praktikant" würde nicht erkannt, wenn Code "Praktikant" erwartet
  - **Lösung**: `.capitalize()` oder `.lower()` verwenden
- **Fehler**: Sondererlaubnis als String vergleichen
  - `if sondererlaubnis == "Ja":` funktioniert, aber nicht bei "ja", "JA", " Ja "
  - **Robuster**: `sondererlaubnis.lower().strip() == "ja"` oder zu Boolean konvertieren

---

### Lösung P5: SPS-Logik-Simulator für Industriesteuerungen

**Vollständiger Code**:
```python
# ==================================
# 1. Grundgatter-Funktionen (IEC 61131-3)
# ==================================

def gate_and(a, b):
    """AND-Gatter: Reihenschaltung in Ladder Logic."""
    return a and b

def gate_or(a, b):
    """OR-Gatter: Parallelschaltung in Ladder Logic."""
    return a or b

def gate_not(a):
    """NOT-Gatter: Öffner-Kontakt."""
    return not a

def gate_xor(a, b):
    """XOR-Gatter: Exklusiv-ODER für Wechselschaltungen."""
    return a != b

def gate_nand(a, b):
    """NAND-Gatter: NOT(AND) - universelles Gatter."""
    return not (a and b)

def gate_nor(a, b):
    """NOR-Gatter: NOT(OR) - universelles Gatter."""
    return not (a or b)

# ==================================
# 2. Industrietypische Schaltungen
# ==================================

def sicherheitsschaltung_2kanalig(kanal_a, kanal_b):
    """
    2-Kanal-Sicherheitsschaltung nach ISO 13849.
    
    Returns:
        (freigabe, fehler): Tupel mit Freigabe-Signal und Fehler-Flag
        - freigabe: True wenn beide Kanäle HIGH (sichere Freigabe)
        - fehler: True wenn nur EIN Kanal HIGH (Kanalfehler erkannt)
    """
    freigabe = gate_and(kanal_a, kanal_b)  # Beide müssen HIGH sein
    fehler = gate_xor(kanal_a, kanal_b)     # Nur einer HIGH = Fehler
    return (freigabe, fehler)

def foerderband_steuerung(not_aus, start, bewegungsmelder, endschalter):
    """
    Förderbandsteuerung mit Sicherheitslogik.
    
    Motor läuft wenn:
    - Not-Aus NICHT gedrückt UND
    - Start gedrückt UND
    - KEIN Hindernis (Bewegungsmelder frei) UND
    - Endschalter NICHT erreicht
    
    Returns:
        motor_an: True wenn Motor laufen soll
    """
    # Sicherheitsbedingungen
    not_aus_ok = gate_not(not_aus)  # Not-Aus NICHT gedrückt
    weg_frei = gate_not(bewegungsmelder)  # Kein Hindernis
    nicht_am_ende = gate_not(endschalter)  # Endposition nicht erreicht
    
    # Alle Bedingungen müssen erfüllt sein
    motor_an = gate_and(gate_and(gate_and(not_aus_ok, start), weg_frei), nicht_am_ende)
    return motor_an

def ampelsteuerung(sensor_auto, taster_fussgaenger, timer_abgelaufen):
    """
    Ampelkreuzung-Logik für Fußgänger-Anforderung.
    
    Fußgänger-Grün nur wenn:
    - Taster gedrückt UND
    - Kein Auto wartet UND
    - Mindestwartezeit (Timer) abgelaufen
    """
    kein_auto = gate_not(sensor_auto)
    fussgaenger_gruen = gate_and(gate_and(taster_fussgaenger, kein_auto), timer_abgelaufen)
    return fussgaenger_gruen

# ==================================
# 3. Binär-Addierer (für SPS-Zähler)
# ==================================

def half_adder(a, b):
    """
    Halbaddierer: Addiert zwei Bits ohne Carry-Eingang.
    
    Returns:
        (summe, carry): Tupel mit Summen-Bit und Übertrag
    """
    summe = gate_xor(a, b)
    carry = gate_and(a, b)
    return (summe, carry)

def full_adder(a, b, cin):
    """
    Volladdierer: Addiert zwei Bits mit Carry-Eingang.
    
    Returns:
        (summe, cout): Tupel mit Summen-Bit und Carry-Ausgang
    """
    # Erste Stufe: Halbaddierer für A und B
    sum1, carry1 = half_adder(a, b)
    
    # Zweite Stufe: Halbaddierer für sum1 und cin
    summe, carry2 = half_adder(sum1, cin)
    
    # Carry-Ausgang: OR-Verknüpfung beider Carries
    cout = gate_or(carry1, carry2)
    
    return (summe, cout)

# ==================================
# 4. Wahrheitstabellen-Generator
# ==================================

def print_truth_table_2input(func, name, input1_name="A", input2_name="B", output_name="Q"):
    """Druckt Wahrheitstabelle für Funktion mit 2 Eingängen."""
    print(f"\nWahrheitstabelle - {name}:")
    print(f"| {input1_name} | {input2_name} | {output_name} |")
    print("|---|---|---|")
    
    for a in [0, 1]:
        for b in [0, 1]:
            result = func(bool(a), bool(b))
            print(f"| {a} | {b} | {1 if result else 0} |")

def print_truth_table_sicherheit():
    """Druckt Wahrheitstabelle für 2-Kanal-Sicherheitsschaltung."""
    print("\nWahrheitstabelle - 2-Kanal-Sicherheitsschaltung:")
    print("| A | B | Freigabe | Fehler |")
    print("|---|---|----------|--------|")
    
    for a in [0, 1]:
        for b in [0, 1]:
            freigabe, fehler = sicherheitsschaltung_2kanalig(bool(a), bool(b))
            print(f"| {a} | {b} |    {1 if freigabe else 0}     |   {1 if fehler else 0}    |")
    
    print("\nLogik:")
    print("  Freigabe = A AND B")
    print("  Fehler = A XOR B  (nur EIN Kanal aktiv = Fehler)")

# ==================================
# 5. Hauptprogramm - Interaktives SPS-Testpanel
# ==================================

def eingabe_boolean(prompt):
    """Liest Boolean-Eingabe (0/1)."""
    while True:
        wert = input(f"{prompt} (0=LOW/1=HIGH): ").strip()
        if wert in ["0", "1"]:
            return bool(int(wert))
        print("⚠️ Ungültige Eingabe! Bitte 0 oder 1 eingeben.")

def main():
    while True:
        print("\n" + "=" * 70)
        print("=== SPS-LOGIK-SIMULATOR (IEC 61131-3) ===")
        print("=" * 70)
        print("\n1. Grundgatter testen")
        print("2. Sicherheitsschaltung (2-Kanal) testen")
        print("3. Förderbandsteuerung testen")
        print("4. Ampelsteuerung testen")
        print("5. Volladdierer testen (SPS-Zähler)")
        print("6. Wahrheitstabelle anzeigen")
        print("7. Beenden")
        
        wahl = input("\nWähle eine Option: ").strip()
        
        if wahl == "1":
            # Grundgatter testen
            print("\n--- Grundgatter-Test ---")
            a = eingabe_boolean("Eingang A")
            b = eingabe_boolean("Eingang B")
            
            print(f"\nErgebnisse:")
            print(f"  AND:  {1 if gate_and(a, b) else 0}")
            print(f"  OR:   {1 if gate_or(a, b) else 0}")
            print(f"  NOT A: {1 if gate_not(a) else 0}")
            print(f"  XOR:  {1 if gate_xor(a, b) else 0}")
            print(f"  NAND: {1 if gate_nand(a, b) else 0}")
            print(f"  NOR:  {1 if gate_nor(a, b) else 0}")
        
        elif wahl == "2":
            # Sicherheitsschaltung testen
            print("\n--- Sicherheitsschaltung (2-Kanal-System, ISO 13849) ---")
            kanal_a = eingabe_boolean("Kanal A")
            kanal_b = eingabe_boolean("Kanal B")
            
            freigabe, fehler = sicherheitsschaltung_2kanalig(kanal_a, kanal_b)
            
            print(f"\nErgebnisse:")
            print(f"  Freigabe (Q):       {1 if freigabe else 0} {'✅ (Maschine FREIGEGEBEN)' if freigabe else '❌ (Maschine GESPERRT)'}")
            print(f"  Fehler (F):         {1 if fehler else 0} {'⚠️ (KANALFEHLER! Sensor/Verkabelung prüfen!)' if fehler else '✅ (Kein Kanalfehler)'}")
            
            if kanal_a and kanal_b:
                print("\nErklärung: Beide Sicherheitskanäle HIGH → redundante Bestätigung → Betrieb sicher")
            elif fehler:
                print("\nErklärung: Nur EIN Kanal HIGH → Sensor defekt oder Verkabelungsfehler!")
            else:
                print("\nErklärung: Beide Kanäle LOW → Maschine aus (Normal-Zustand)")
        
        elif wahl == "3":
            # Förderbandsteuerung
            print("\n--- Förderbandsteuerung ---")
            not_aus = eingabe_boolean("Not-Aus gedrückt? (0=Nein/1=Ja)")
            start = eingabe_boolean("Start-Taster gedrückt?")
            bewegungsmelder = eingabe_boolean("Bewegungsmelder (Hindernis)? (0=Frei/1=Blockiert)")
            endschalter = eingabe_boolean("Endschalter erreicht?")
            
            motor_an = foerderband_steuerung(not_aus, start, bewegungsmelder, endschalter)
            
            print(f"\nErgebnis:")
            print(f"  Motor-Ausgang (Q): {1 if motor_an else 0} {'✅' if motor_an else '🛑'}")
            print(f"➡️ Förderband {'läuft' if motor_an else 'gestoppt'}")
            
            if not_aus:
                print("   Grund: NOT-AUS gedrückt!")
            elif bewegungsmelder:
                print("   Grund: Hindernis erkannt (Bewegungsmelder)!")
            elif endschalter:
                print("   Grund: Endposition erreicht!")
            elif not start:
                print("   Grund: Start-Taster nicht gedrückt")
        
        elif wahl == "4":
            # Ampelsteuerung
            print("\n--- Ampelsteuerung ---")
            sensor_auto = eingabe_boolean("Sensor Auto (wartet)?")
            taster = eingabe_boolean("Taster Fußgänger gedrückt?")
            timer = eingabe_boolean("Timer abgelaufen (Mindestwartezeit)?")
            
            fussgaenger_gruen = ampelsteuerung(sensor_auto, taster, timer)
            
            print(f"\nErgebnis:")
            print(f"  Fußgänger-Grün: {1 if fussgaenger_gruen else 0} {'🟢' if fussgaenger_gruen else '🔴'}")
            
            if fussgaenger_gruen:
                print("➡️ Fußgänger dürfen gehen")
            else:
                if sensor_auto:
                    print("➡️ Fußgänger müssen warten (Auto hat Vorfahrt)")
                elif not timer:
                    print("➡️ Fußgänger müssen warten (Mindestwartezeit noch nicht abgelaufen)")
                else:
                    print("➡️ Fußgänger-Ampel bleibt rot (Taster nicht gedrückt)")
        
        elif wahl == "5":
            # Volladdierer
            print("\n--- Volladdierer Test (für SPS-Zähler) ---")
            a = eingabe_boolean("Eingabe A")
            b = eingabe_boolean("Eingabe B")
            cin = eingabe_boolean("Carry-In (Cin)")
            
            summe, cout = full_adder(a, b, cin)
            
            print(f"\nErgebnisse:")
            print(f"  Summe (S):     {1 if summe else 0}")
            print(f"  Carry-Out (Cout): {1 if cout else 0}")
            
            # Dezimale Berechnung
            dezimal = int(a) + int(b) + int(cin)
            print(f"\nErklärung: {int(a)} + {int(b)} + {int(cin)} = {dezimal} (dezimal) = {cout}{summe} (binär)")
        
        elif wahl == "6":
            # Wahrheitstabellen
            print("\n--- Wahrheitstabelle ---")
            print("Wähle Schaltung:")
            print("1. XOR")
            print("2. 2-Kanal-Sicherheit")
            print("3. Halbaddierer")
            
            sub_wahl = input("\nWähle: ").strip()
            
            if sub_wahl == "1":
                print_truth_table_2input(gate_xor, "XOR", "A", "B", "Q")
            elif sub_wahl == "2":
                print_truth_table_sicherheit()
            elif sub_wahl == "3":
                print("\nWahrheitstabelle - Halbaddierer:")
                print("| A | B | S | C |")
                print("|---|---|---|---|")
                for a in [0, 1]:
                    for b in [0, 1]:
                        s, c = half_adder(bool(a), bool(b))
                        print(f"| {a} | {b} | {1 if s else 0} | {1 if c else 0} |")
        
        elif wahl == "7":
            print("\nSPS-Simulator beendet.")
            break
        else:
            print("⚠️ Ungültige Auswahl!")

# Programm starten
if __name__ == "__main__":
    main()
```

**Erklärung der Implementierung**:

**1. Grundgatter (IEC 61131-3 Basiselemente)**:
- **AND/OR/NOT**: Direkte Python-Operatoren (`and`, `or`, `not`)
- **XOR**: Nutzt Ungleichheit (`a != b`) - für Booleans äquivalent zu XOR
- **NAND/NOR**: Universelle Gatter (jede Logik kann damit gebaut werden)

**2. Sicherheitsschaltung (2-Kanal)**:
```python
freigabe = gate_and(kanal_a, kanal_b)  # Beide Kanäle müssen HIGH sein
fehler = gate_xor(kanal_a, kanal_b)    # Nur EIN Kanal HIGH = Fehler erkannt
```

**Warum XOR für Fehlererkennung?**
- Beide Kanäle LOW (0,0): XOR = 0 → kein Fehler (Maschine aus)
- Beide Kanäle HIGH (1,1): XOR = 0 → kein Fehler (Maschine freigegeben)
- Ein Kanal HIGH (1,0 oder 0,1): XOR = 1 → **FEHLER** (Sensor defekt!)

**3. Förderbandsteuerung**:
Motor läuft NUR wenn ALLE Bedingungen erfüllt:
```python
motor_an = NOT(not_aus) AND start AND NOT(hindernis) AND NOT(endschalter)
```

**4. Volladdierer (Kaskadierbar für Z Zähler)**:
- Zwei Halbaddierer + OR für Carry
- Wird in SPS-Zählern für Werkstück-Erfassung genutzt

**Praxisbezug**:
- **Siemens TIA Portal**: Ladder Diagram (LD) nutzt identische Gatter
- **Beckhoff TwinCAT**: Strukturierter Text (ST) ähnelt diesem Python-Code
- **ISO 13849**: Performance Level PLd/PLe erfordern 2-Kanal-Sicherheit
- **IEC 61131-3**: Internationale Norm für SPS-Programmierung (5 Sprachen)

**Häufige Fehler**:
- **Fehler**: `and` statt `gate_and()` in komplexen Verkettungen vergessen
- **Fehler**: XOR falsch implementieren als `(a or b) and not (a and b)` statt einfach `a != b`
- **Fehler**: Bei Sicherheitsschaltung: OR statt AND → **hochgefährlich**!
- **Fehler**: Carry-Logik im Volladdierer: AND statt OR für Carry-Ausgang

---

**🎓 Hinweis für Dozenten**: Diese Aufgabe ist bewusst komplex und zeigt die praktische Relevanz Boolescher Algebra in der Automatisierungstechnik. Die 2-Kanal-Sicherheitslogik ist ISO 13849-konform und wird in allen modernen Industrieanlagen eingesetzt.

def gate_nand(a, b):
    """NAND-Gatter: Negiertes AND."""
    return not (a and b)

def gate_nor(a, b):
    """NOR-Gatter: Negiertes OR."""
    return not (a or b)


# ===========================
# 2. Komplexe Schaltungen
# ===========================

def half_adder(a, b):
    """
    Halbaddierer: Addiert zwei Bits.
    
    Returns:
        tuple: (Summe, Carry)
    """
    summe = gate_xor(a, b)      # S = A XOR B
    carry = gate_and(a, b)      # C = A AND B
    return (summe, carry)

def full_adder(a, b, cin):
    """
    Volladdierer: Addiert drei Bits (A, B, Carry-In).
    
    Returns:
        tuple: (Summe, Carry-Out)
    """
    # Erster Halbaddierer: A + B
    s1, c1 = half_adder(a, b)
    
    # Zweiter Halbaddierer: (A + B) + Cin
    summe, c2 = half_adder(s1, cin)
    
    # Carry-Out: OR der beiden Überträge
    cout = gate_or(c1, c2)
    
    return (summe, cout)

def multiplexer_2to1(i0, i1, select):
    """
    2:1 Multiplexer: Wählt einen von zwei Eingängen aus.
    
    Args:
        i0: Eingang 0
        i1: Eingang 1
        select: Auswahl (False=i0, True=i1)
    
    Returns:
        Ausgewählter Eingang
    """
    # Y = (NOT S AND I0) OR (S AND I1)
    term1 = gate_and(gate_not(select), i0)
    term2 = gate_and(select, i1)
    return gate_or(term1, term2)


# ===========================
# 3. Wahrheitstabellen-Generator
# ===========================

def print_truth_table_xor():
    """Druckt Wahrheitstabelle für XOR."""
    print("\nWahrheitstabelle - XOR:")
    print("| A | B | Y |")
    print("|---|---|---|")
    
    for a in [False, True]:
        for b in [False, True]:
            y = gate_xor(a, b)
            print(f"| {int(a)} | {int(b)} | {int(y)} |")

def print_truth_table_half_adder():
    """Druckt Wahrheitstabelle für Halbaddierer."""
    print("\nWahrheitstabelle - Halbaddierer:")
    print("| A | B | S | C |")
    print("|---|---|---|---|")
    
    for a in [False, True]:
        for b in [False, True]:
            s, c = half_adder(a, b)
            print(f"| {int(a)} | {int(b)} | {int(s)} | {int(c)} |")

def print_truth_table_full_adder():
    """Druckt Wahrheitstabelle für Volladdierer."""
    print("\nWahrheitstabelle - Volladdierer:")
    print("| A | B | Cin | S | Cout |")
    print("|---|---|-----|---|------|")
    
    for a in [False, True]:
        for b in [False, True]:
            for cin in [False, True]:
                s, cout = full_adder(a, b, cin)
                print(f"| {int(a)} | {int(b)} | {int(cin)}   | {int(s)} | {int(cout)}    |")


# ===========================
# 4. Hauptprogramm
# ===========================

def bool_von_eingabe(prompt):
    """Hilfsfunktion: Liest 0/1 ein und gibt Boolean zurück."""
    while True:
        eingabe = input(prompt)
        if eingabe in ["0", "1"]:
            return eingabe == "1"
        print("Ungültige Eingabe! Bitte 0 oder 1 eingeben.")

def gatter_testen():
    """Interaktives Testen einzelner Gatter."""
    print("\n--- Gatter Test ---")
    print("Wähle Gatter:")
    print("1. AND")
    print("2. OR")
    print("3. NOT")
    print("4. XOR")
    print("5. NAND")
    print("6. NOR")
    
    wahl = input("Wähle: ")
    
    if wahl == "3":  # NOT benötigt nur einen Eingang
        a = bool_von_eingabe("Eingabe A (0/1): ")
        result = gate_not(a)
        print(f"\nNOT {int(a)} = {int(result)}")
    else:
        a = bool_von_eingabe("Eingabe A (0/1): ")
        b = bool_von_eingabe("Eingabe B (0/1): ")
        
        if wahl == "1":
            result = gate_and(a, b)
            operator = "AND"
        elif wahl == "2":
            result = gate_or(a, b)
            operator = "OR"
        elif wahl == "4":
            result = gate_xor(a, b)
            operator = "XOR"
        elif wahl == "5":
            result = gate_nand(a, b)
            operator = "NAND"
        elif wahl == "6":
            result = gate_nor(a, b)
            operator = "NOR"
        else:
            print("Ungültige Wahl!")
            return
        
        print(f"\n{int(a)} {operator} {int(b)} = {int(result)}")

def hauptmenue():
    """Hauptmenü des Simulators."""
    while True:
        print("\n" + "=" * 40)
        print("=== Digitaler Schaltungssimulator ===")
        print("=" * 40)
        print("\n1. Gatter testen")
        print("2. Halbaddierer testen")
        print("3. Volladdierer testen")
        print("4. Multiplexer testen")
        print("5. Wahrheitstabelle anzeigen")
        print("6. Beenden")
        
        wahl = input("\nWähle eine Option: ")
        
        if wahl == "1":
            gatter_testen()
        
        elif wahl == "2":
            print("\n--- Halbaddierer Test ---")
            a = bool_von_eingabe("Eingabe A (0/1): ")
            b = bool_von_eingabe("Eingabe B (0/1): ")
            s, c = half_adder(a, b)
            print(f"\nErgebnisse:")
            print(f"  Summe (S):     {int(s)}")
            print(f"  Übertrag (C):  {int(c)}")
            print(f"\nErklärung: {int(a)} + {int(b)} = {int(c)}{int(s)} (binär) = {int(a) + int(b)} (dezimal)")
        
        elif wahl == "3":
            print("\n--- Volladdierer Test ---")
            a = bool_von_eingabe("Eingabe A (0/1): ")
            b = bool_von_eingabe("Eingabe B (0/1): ")
            cin = bool_von_eingabe("Eingabe Cin (0/1): ")
            s, cout = full_adder(a, b, cin)
            print(f"\nErgebnisse:")
            print(f"  Summe (S):      {int(s)}")
            print(f"  Übertrag (Cout): {int(cout)}")
            summe_dez = int(a) + int(b) + int(cin)
            print(f"\nErklärung: {int(a)} + {int(b)} + {int(cin)} = {int(cout)}{int(s)} (binär) = {summe_dez} (dezimal)")
        
        elif wahl == "4":
            print("\n--- Multiplexer 2:1 Test ---")
            i0 = bool_von_eingabe("Eingang I0 (0/1): ")
            i1 = bool_von_eingabe("Eingang I1 (0/1): ")
            sel = bool_von_eingabe("Select (0=I0, 1=I1): ")
            y = multiplexer_2to1(i0, i1, sel)
            print(f"\nErgebnis: {int(y)}")
            print(f"Gewählter Eingang: I{'1' if sel else '0'} = {int(i1 if sel else i0)}")
        
        elif wahl == "5":
            print("\n--- Wahrheitstabelle ---")
            print("Wähle Schaltung:")
            print("1. XOR")
            print("2. Halbaddierer")
            print("3. Volladdierer")
            
            sub_wahl = input("Wähle: ")
            
            if sub_wahl == "1":
                print_truth_table_xor()
            elif sub_wahl == "2":
                print_truth_table_half_adder()
            elif sub_wahl == "3":
                print_truth_table_full_adder()
            else:
                print("Ungültige Wahl!")
        
        elif wahl == "6":
            print("\nProgramm beendet.")
            break
        
        else:
            print("Ungültige Wahl!")


# ===========================
# Bonus: 4-Bit-Addierer
# ===========================

def add_4bit(a_bits, b_bits):
    """
    Addiert zwei 4-Bit-Zahlen mit kaskadierten Volladdierern.
    
    Args:
        a_bits: Liste von 4 Booleans [MSB, ..., LSB] für erste Zahl
        b_bits: Liste von 4 Booleans [MSB, ..., LSB] für zweite Zahl
    
    Returns:
        Liste von 5 Booleans [Cout, MSB, ..., LSB] (Ergebnis mit Übertrag)
    """
    # Eingaben umdrehen (von LSB zu MSB verarbeiten)
    a_bits = list(reversed(a_bits))
    b_bits = list(reversed(b_bits))
    
    summe_bits = []
    carry = False  # Kein Eingangsübertrag für erste Stelle
    
    # Vier Volladdierer kaskadieren
    for i in range(4):
        s, carry = full_adder(a_bits[i], b_bits[i], carry)
        summe_bits.append(s)
    
    # Finaler Übertrag
    summe_bits.append(carry)
    
    # Zurück zu MSB-first Format
    return list(reversed(summe_bits))

def teste_4bit_addierer():
    """Test-Funktion für 4-Bit-Addierer."""
    print("\n=== 4-Bit-Addierer Test ===")
    
    # Beispiel: 1011 + 0110 = 10001 (11 + 6 = 17)
    a = [True, False, True, True]   # 1011 = 11
    b = [False, True, True, False]  # 0110 = 6
    
    result = add_4bit(a, b)
    
    # Konvertierung zu Strings für Ausgabe
    a_str = "".join(["1" if bit else "0" for bit in a])
    b_str = "".join(["1" if bit else "0" for bit in b])
    result_str = "".join(["1" if bit else "0" for bit in result])
    
    # Dezimalwerte berechnen
    a_dez = int(a_str, 2)
    b_dez = int(b_str, 2)
    result_dez = int(result_str, 2)
    
    print(f"  {a_str} (binär) = {a_dez} (dezimal)")
    print(f"+ {b_str} (binär) = {b_dez} (dezimal)")
    print("-" * 30)
    print(f"= {result_str} (binär) = {result_dez} (dezimal)")
    print(f"\nVerifikation: {a_dez} + {b_dez} = {result_dez} ✓")


# ===========================
# Programm starten
# ===========================

if __name__ == "__main__":
    # Hauptmenü starten
    hauptmenue()
    
    # Optional: 4-Bit-Addierer demonstrieren
    print("\n" + "=" * 40)
    teste_4bit_addierer()
```

**Erklärung**:

**Architektur-Überblick**:

Das Programm ist in vier logische Module unterteilt:

1. **Grundgatter**: Atomare Bausteine (AND, OR, NOT, XOR, NAND, NOR)
2. **Komplexe Schaltungen**: Zusammengesetzte Schaltungen aus Grundgattern
3. **Wahrheitstabellen-Generator**: Visualisierung der Schaltungslogik
4. **Hauptprogramm**: Interaktives Menü für Benutzereingaben

**Schritt-für-Schritt Erklärung**:

**1. Grundgatter-Funktionen**:

```python
def gate_xor(a, b):
    return a != b  # XOR entspricht Ungleichheit bei Booleans
```

- XOR ist in Python nicht als logischer Operator vorhanden
- Für Booleans gilt: `a XOR b = a != b` (wahr, wenn unterschiedlich)
- Für Integer-Bitoperationen würde man `a ^ b` verwenden

**2. Halbaddierer-Konstruktion**:

```python
def half_adder(a, b):
    summe = gate_xor(a, b)      # S = A XOR B
    carry = gate_and(a, b)      # C = A AND B
    return (summe, carry)
```

- Direkte Umsetzung der Theorie
- Rückgabe als Tupel erlaubt `s, c = half_adder(1, 1)` (Tuple Unpacking)

**3. Volladdierer aus zwei Halbaddierern**:

```python
def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)       # Erster Halbaddierer
    summe, c2 = half_adder(s1, cin) # Zweiter Halbaddierer
    cout = gate_or(c1, c2)          # Überträge zusammenführen
    return (summe, cout)
```

- Elegant: Wiederverwendung von `half_adder()`
- `c1` und `c2` sind die beiden möglichen Übertragsquellen
- OR verknüpft sie: Übertrag, wenn mindestens einer auftritt

**4. Multiplexer**:

```python
def multiplexer_2to1(i0, i1, select):
    term1 = gate_and(gate_not(select), i0)  # (NOT S) AND I0
    term2 = gate_and(select, i1)            # S AND I1
    return gate_or(term1, term2)            # Zusammenführen
```

- Umsetzung der Formel: $Y = (\neg S \land I0) \lor (S \land I1)$
- Wenn `select=False`: `term1` ist aktiv, `term2` ist 0
- Wenn `select=True`: `term1` ist 0, `term2` ist aktiv

**5. Wahrheitstabellen generieren**:

```python
for a in [False, True]:
    for b in [False, True]:
        y = gate_xor(a, b)
        print(f"| {int(a)} | {int(b)} | {int(y)} |")
```

- Verschachtelte Schleifen generieren alle Kombinationen
- `int(bool)` konvertiert `True`→1, `False`→0 für Ausgabe

**6. 4-Bit-Addierer (Bonus)**:

```python
def add_4bit(a_bits, b_bits):
    a_bits = list(reversed(a_bits))  # LSB zuerst
    summe_bits = []
    carry = False
    
    for i in range(4):
        s, carry = full_adder(a_bits[i], b_bits[i], carry)
        summe_bits.append(s)
    
    summe_bits.append(carry)  # Finaler Übertrag
    return list(reversed(summe_bits))  # Zurück zu MSB-first
```

- **Wichtig**: Von niederwertigster Stelle (LSB) zu höchstwertigster (MSB)
- Jeder `carry` wird zum `cin` der nächsten Iteration
- Finaler `carry` wird als fünftes Bit angehängt (Überlauf)

**Design-Entscheidungen**:

1. **Warum Funktionen für jedes Gatter?**
   - **Lesbarkeit**: `gate_and(a, b)` ist klarer als `a and b` im Kontext von Schaltungen
   - **Erweiterbarkeit**: Könnte später um Simulation von Verzögerungen, Stromverbrauch etc. erweitert werden
   - **Konsistenz**: Einheitliche API für alle Gatter

2. **Warum Tupel als Rückgabewert?**
   - Natürliche Darstellung von Mehrfach-Ausgängen
   - Ermöglicht Tuple Unpacking: `s, c = half_adder(a, b)`
   - Alternativ: Dictionaries `{"sum": s, "carry": c}` (verbosER, aber selbstdokumentierend)

3. **Warum separate Wahrheitstabellen-Funktionen?**
   - Einfacher zu verstehen als generische Funktion
   - Jede Funktion kann Layout an Anzahl der Ein-/Ausgänge anpassen
   - Könnte später mit `itertools.product()` verallgemeinert werden

**Alternative Lösungsansätze**:

**Ansatz 1: Bitweise Operatoren statt logischer Operatoren**:
```python
def gate_and(a, b):
    return (a & b) == 1  # Bitweises AND für Integer
```
✅ Vorteile: Näher an Hardware-Realität  
❌ Nachteile: Nur für 0/1-Integer, nicht für Booleans

**Ansatz 2: Klassen-Hierarchie** (objektorientiert):
```python
class Gate:
    def evaluate(self, *inputs):
        raise NotImplementedError

class ANDGate(Gate):
    def evaluate(self, a, b):
        return a and b
```
✅ Vorteile: Sehr erweiterbar, testbar, simulierbar  
❌ Nachteile: Overkill für diese Aufgabe, benötigt OOP

**Komplexitätsanalyse**:

- **Halbaddierer**: O(1) – konstante Anzahl von Operationen
- **Volladdierer**: O(1) – drei Halbaddierer-Aufrufe (konstant)
- **4-Bit-Addierer**: O(n) – n = Anzahl der Bits (hier 4)
- **Wahrheitstabelle** (n Eingänge): O(2^n) – alle Kombinationen durchgehen

**Häufige Fehler**:
- **Fehler**: XOR als `a or b and not (a and b)` implementieren
  - **Kompliziert**: `(a or b) and not (a and b)`
  - **Einfacher**: `a != b` für Booleans
- **Fehler**: Bit-Reihenfolge bei 4-Bit-Addierer vertauschen
  - Muss von LSB zu MSB gerechnet werden (Überträge propagieren nach links)
- **Fehler**: Finalen Übertrag vergessen
  - Bei `1111 + 1111 = 11110` benötigt man 5 Bits für das Ergebnis
- **Fehler**: `int(bool)` nicht verwenden für Ausgabe
  - `print(True)` → "True" (String)
  - `print(int(True))` → "1" (wie in Wahrheitstabellen üblich)

---
