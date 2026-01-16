# Pygame Zero auf Pydroid - Teil 1: Deine ersten Spiele! 🎮

Hallo! In diesem Tutorial lernst du, wie du coole Spiele auf deinem Android-Handy programmieren kannst. Wir benutzen dafür **Pygame Zero** - das ist super einfach!

---

## Was du brauchst

1. Ein Android-Handy oder Tablet
2. Die App **Pydroid 3** (aus dem Play Store)
3. Das Plugin **Pydroid repository plugin** (auch aus dem Play Store)

---

## Installation

### Schritt 1: Pydroid 3 installieren
Lade "Pydroid 3" aus dem Google Play Store herunter.

### Schritt 2: Pygame Zero installieren
1. Öffne Pydroid 3
2. Tippe auf die drei Striche oben links (☰)
3. Wähle "Pip"
4. Gib ein: `pgzero`
5. Tippe auf "Install"

Fertig! Jetzt kann es losgehen!

---

## Wie Pygame Zero funktioniert

Jedes Spiel braucht diese wichtigen Teile:

```python
# Das Fenster (wie groß dein Spiel ist)
WIDTH = 400   # Breite
HEIGHT = 600  # Höhe

# Diese Funktion zeichnet alles auf den Bildschirm
def draw():
    screen.fill("black")  # Hintergrund schwarz machen

# Diese Funktion wird immer wieder aufgerufen (60 mal pro Sekunde!)
def update():
    pass  # Hier kommt die Spiellogik rein
```

**Wichtig:** Speichere deine Datei IMMER mit der Endung `.py` (zum Beispiel `meinspiel.py`)

Um das Spiel zu starten, tippe auf den "Play" Knopf ▶️

---

## Grundlagen: Formen zeichnen

Bevor wir Spiele machen, lernen wir wie man Sachen auf den Bildschirm malt:

```python
WIDTH = 400
HEIGHT = 600

def draw():
    # Hintergrund blau machen
    screen.fill("darkblue")

    # Ein Rechteck (Rect) zeichnen
    # Rect(x, y, breite, höhe)
    screen.draw.filled_rect(Rect(100, 200, 50, 50), "red")

    # Einen Kreis zeichnen
    # circle((x, y), radius, farbe)
    screen.draw.filled_circle((200, 300), 30, "yellow")

    # Text schreiben
    screen.draw.text("Hallo!", (150, 100), color="white", fontsize=40)
```

### Farben die du benutzen kannst:
- `"red"` = Rot
- `"blue"` = Blau
- `"green"` = Grün
- `"yellow"` = Gelb
- `"white"` = Weiß
- `"black"` = Schwarz
- `"orange"` = Orange
- `"purple"` = Lila
- `"pink"` = Rosa

---

## Touch-Eingabe verstehen

Auf dem Handy tippst du mit dem Finger. So erkennt das Spiel wo du tippst:

```python
WIDTH = 400
HEIGHT = 600

# Hier speichern wir wo getippt wurde
finger_x = 200
finger_y = 300

def draw():
    screen.fill("darkblue")
    # Zeichne einen Kreis wo der Finger ist
    screen.draw.filled_circle((finger_x, finger_y), 30, "red")

def on_mouse_down(pos):
    # pos ist eine Liste mit [x, y] Position
    global finger_x, finger_y
    finger_x = pos[0]  # x-Position
    finger_y = pos[1]  # y-Position
```

**Erklärung:**
- `on_mouse_down(pos)` wird aufgerufen wenn du auf den Bildschirm tippst
- `pos[0]` ist die x-Position (links/rechts)
- `pos[1]` ist die y-Position (oben/unten)
- `global` sagt Python, dass wir die Variable von außen ändern wollen

---

# Spiel 1: Fang den Ball! ⚽

Unser erstes Spiel! Ein Ball fällt runter und du musst ihn fangen.

```python
# === FANG DEN BALL ===
import random

WIDTH = 400
HEIGHT = 600

# Der Ball
ball_x = 200
ball_y = 0
ball_speed = 5

# Der Fänger (du steuerst ihn)
faenger_x = 175
faenger_y = 550
faenger_breite = 80
faenger_hoehe = 20

# Punkte
punkte = 0

def draw():
    screen.fill("darkblue")

    # Ball zeichnen (ein Kreis)
    screen.draw.filled_circle((ball_x, ball_y), 20, "yellow")

    # Fänger zeichnen (ein Rechteck)
    screen.draw.filled_rect(
        Rect(faenger_x, faenger_y, faenger_breite, faenger_hoehe),
        "green"
    )

    # Punkte anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=30)

def update():
    global ball_x, ball_y, ball_speed, punkte

    # Ball fällt nach unten
    ball_y = ball_y + ball_speed

    # Prüfen ob Ball gefangen wurde
    if ball_y >= faenger_y:
        if ball_x >= faenger_x and ball_x <= faenger_x + faenger_breite:
            # Getroffen! Punkt!
            punkte = punkte + 1
            ball_y = 0
            ball_x = random.randint(30, 370)
            # Spiel wird schneller
            ball_speed = ball_speed + 0.5

    # Ball ist unten raus? Neuer Ball!
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(30, 370)
        punkte = 0  # Punkte zurücksetzen
        ball_speed = 5

def on_mouse_down(pos):
    global faenger_x
    # Fänger bewegt sich dahin wo du tippst
    faenger_x = pos[0] - faenger_breite / 2
```

---

# Spiel 2: Springende Box 📦

Eine Box springt über Hindernisse. Tippe um zu springen!

```python
# === SPRINGENDE BOX ===
import random

WIDTH = 400
HEIGHT = 600

# Die Box (der Spieler)
box_x = 80
box_y = 450
box_breite = 40
box_hoehe = 40
box_speed_y = 0  # Geschwindigkeit nach oben/unten
schwerkraft = 0.8
boden_y = 500

# Hindernis
hindernis_x = 400
hindernis_breite = 40
hindernis_hoehe = 60

# Spielstand
punkte = 0
spiel_laeuft = True
geschwindigkeit = 6

def draw():
    screen.fill("skyblue")

    # Boden zeichnen
    screen.draw.filled_rect(Rect(0, boden_y, WIDTH, 100), "green")

    # Box zeichnen
    screen.draw.filled_rect(
        Rect(box_x, box_y, box_breite, box_hoehe),
        "red"
    )

    # Hindernis zeichnen
    screen.draw.filled_rect(
        Rect(hindernis_x, boden_y - hindernis_hoehe, hindernis_breite, hindernis_hoehe),
        "darkgreen"
    )

    # Punkte anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="black", fontsize=30)

    # Anleitung
    screen.draw.text("Tippe zum Springen!", (100, 50), color="gray", fontsize=20)

    # Game Over Nachricht
    if not spiel_laeuft:
        screen.draw.text("GAME OVER!", (100, 250), color="red", fontsize=50)
        screen.draw.text("Tippe zum Neustarten", (80, 320), color="black", fontsize=25)

def update():
    global box_y, box_speed_y, hindernis_x, punkte, spiel_laeuft, geschwindigkeit

    if not spiel_laeuft:
        return  # Nichts machen wenn Spiel vorbei

    # Schwerkraft - Box fällt nach unten
    box_speed_y = box_speed_y + schwerkraft
    box_y = box_y + box_speed_y

    # Box darf nicht durch den Boden fallen
    if box_y + box_hoehe > boden_y:
        box_y = boden_y - box_hoehe
        box_speed_y = 0

    # Hindernis bewegt sich nach links
    hindernis_x = hindernis_x - geschwindigkeit

    # Neues Hindernis wenn altes weg ist
    if hindernis_x < -hindernis_breite:
        hindernis_x = WIDTH + random.randint(0, 200)
        punkte = punkte + 1
        # Spiel wird schneller
        if geschwindigkeit < 15:
            geschwindigkeit = geschwindigkeit + 0.3

    # Kollision prüfen (hat Box das Hindernis berührt?)
    hindernis_y = boden_y - hindernis_hoehe

    # Prüfen ob sich Box und Hindernis überlappen
    if box_x + box_breite > hindernis_x and box_x < hindernis_x + hindernis_breite:
        if box_y + box_hoehe > hindernis_y:
            spiel_laeuft = False

def on_mouse_down(pos):
    global box_speed_y, spiel_laeuft, punkte, hindernis_x, geschwindigkeit

    if spiel_laeuft:
        # Nur springen wenn Box auf dem Boden ist
        if box_y + box_hoehe >= boden_y - 5:
            box_speed_y = -15  # Nach oben springen!
    else:
        # Spiel neu starten
        spiel_laeuft = True
        punkte = 0
        hindernis_x = 400
        geschwindigkeit = 6
```

---

# Spiel 3: Flappy Box 🐦

Wie Flappy Bird, aber mit einer Box! Tippe um nach oben zu fliegen.

```python
# === FLAPPY BOX ===
import random

WIDTH = 400
HEIGHT = 600

# Die Box (der Spieler)
box_x = 100
box_y = 300
box_groesse = 30
box_speed_y = 0
schwerkraft = 0.5
sprung_kraft = -10

# Röhren (Hindernisse)
roehre_x = 400
luecke_y = 250  # Wo ist die Lücke
luecke_hoehe = 180  # Wie groß ist die Lücke
roehre_breite = 60
roehre_speed = 4

# Spielstand
punkte = 0
spiel_laeuft = True

def draw():
    screen.fill("skyblue")

    # Obere Röhre zeichnen
    screen.draw.filled_rect(
        Rect(roehre_x, 0, roehre_breite, luecke_y),
        "green"
    )

    # Untere Röhre zeichnen
    untere_roehre_y = luecke_y + luecke_hoehe
    screen.draw.filled_rect(
        Rect(roehre_x, untere_roehre_y, roehre_breite, HEIGHT - untere_roehre_y),
        "green"
    )

    # Box zeichnen
    screen.draw.filled_rect(
        Rect(box_x, box_y, box_groesse, box_groesse),
        "yellow"
    )

    # Punkte anzeigen
    screen.draw.text(f"{punkte}", (WIDTH/2 - 20, 50), color="white", fontsize=60)

    # Game Over
    if not spiel_laeuft:
        screen.draw.text("GAME OVER", (80, 250), color="red", fontsize=50)
        screen.draw.text("Tippe zum Neustarten", (70, 320), color="black", fontsize=25)

def update():
    global box_y, box_speed_y, roehre_x, luecke_y, punkte, spiel_laeuft

    if not spiel_laeuft:
        return

    # Schwerkraft - Box fällt nach unten
    box_speed_y = box_speed_y + schwerkraft
    box_y = box_y + box_speed_y

    # Röhre bewegt sich nach links
    roehre_x = roehre_x - roehre_speed

    # Neue Röhre wenn alte weg ist
    if roehre_x < -roehre_breite:
        roehre_x = WIDTH
        luecke_y = random.randint(80, HEIGHT - luecke_hoehe - 80)
        punkte = punkte + 1

    # Kollision mit Röhren prüfen
    if box_x + box_groesse > roehre_x and box_x < roehre_x + roehre_breite:
        # In der Röhren-Zone
        if box_y < luecke_y or box_y + box_groesse > luecke_y + luecke_hoehe:
            # Getroffen!
            spiel_laeuft = False

    # Kollision mit Boden oder Decke
    if box_y < 0 or box_y + box_groesse > HEIGHT:
        spiel_laeuft = False

def on_mouse_down(pos):
    global box_speed_y, spiel_laeuft, box_y, roehre_x, punkte

    if spiel_laeuft:
        # Nach oben fliegen!
        box_speed_y = sprung_kraft
    else:
        # Spiel neu starten
        spiel_laeuft = True
        box_y = 300
        box_speed_y = 0
        roehre_x = 400
        punkte = 0
```

---

# Spiel 4: Ping Pong 🏓

Klassisches Ping Pong! Du spielst gegen den Computer.

```python
# === PING PONG ===

WIDTH = 400
HEIGHT = 600

# Der Ball
ball_x = 200
ball_y = 300
ball_groesse = 15
ball_speed_x = 5
ball_speed_y = 5

# Spieler Schläger (unten)
spieler_x = 150
spieler_y = 550
schlaeger_breite = 100
schlaeger_hoehe = 15

# Computer Schläger (oben)
computer_x = 150
computer_y = 30
computer_speed = 4

# Punkte
spieler_punkte = 0
computer_punkte = 0

def draw():
    screen.fill("black")

    # Mittellinie
    screen.draw.line((0, HEIGHT/2), (WIDTH, HEIGHT/2), "gray")

    # Ball zeichnen
    screen.draw.filled_rect(
        Rect(ball_x, ball_y, ball_groesse, ball_groesse),
        "white"
    )

    # Spieler Schläger (grün)
    screen.draw.filled_rect(
        Rect(spieler_x, spieler_y, schlaeger_breite, schlaeger_hoehe),
        "green"
    )

    # Computer Schläger (rot)
    screen.draw.filled_rect(
        Rect(computer_x, computer_y, schlaeger_breite, schlaeger_hoehe),
        "red"
    )

    # Punkte anzeigen
    screen.draw.text(f"Computer: {computer_punkte}", (10, HEIGHT/2 - 40),
                     color="red", fontsize=25)
    screen.draw.text(f"Du: {spieler_punkte}", (10, HEIGHT/2 + 10),
                     color="green", fontsize=25)

def update():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    global computer_x, spieler_punkte, computer_punkte

    # Ball bewegen
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # Ball prallt von Seiten ab
    if ball_x <= 0 or ball_x + ball_groesse >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Ball trifft Spieler Schläger
    if ball_y + ball_groesse >= spieler_y:
        if ball_x + ball_groesse >= spieler_x and ball_x <= spieler_x + schlaeger_breite:
            ball_speed_y = -abs(ball_speed_y)  # Nach oben

    # Ball trifft Computer Schläger
    if ball_y <= computer_y + schlaeger_hoehe:
        if ball_x + ball_groesse >= computer_x and ball_x <= computer_x + schlaeger_breite:
            ball_speed_y = abs(ball_speed_y)  # Nach unten

    # Punkt für Spieler (Ball oben raus)
    if ball_y < 0:
        spieler_punkte = spieler_punkte + 1
        ball_x = 200
        ball_y = 300

    # Punkt für Computer (Ball unten raus)
    if ball_y > HEIGHT:
        computer_punkte = computer_punkte + 1
        ball_x = 200
        ball_y = 300

    # Computer KI - folgt dem Ball
    ball_mitte = ball_x + ball_groesse / 2
    computer_mitte = computer_x + schlaeger_breite / 2

    if ball_mitte < computer_mitte - 10:
        computer_x = computer_x - computer_speed
    elif ball_mitte > computer_mitte + 10:
        computer_x = computer_x + computer_speed

def on_mouse_down(pos):
    global spieler_x
    # Spieler Schläger folgt dem Finger
    spieler_x = pos[0] - schlaeger_breite / 2

    # Nicht aus dem Bildschirm gehen
    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - schlaeger_breite:
        spieler_x = WIDTH - schlaeger_breite

# Diese Funktion wird aufgerufen wenn der Finger sich bewegt
def on_mouse_move(pos):
    global spieler_x
    spieler_x = pos[0] - schlaeger_breite / 2

    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - schlaeger_breite:
        spieler_x = WIDTH - schlaeger_breite
```

---

# Spiel 5: Breakout (Steine zerstören) 🧱

Zerstöre alle Steine mit dem Ball!

```python
# === BREAKOUT ===

WIDTH = 400
HEIGHT = 600

# Ball
ball_x = 200
ball_y = 400
ball_groesse = 12
ball_speed_x = 4
ball_speed_y = -4

# Schläger
schlaeger_x = 150
schlaeger_y = 550
schlaeger_breite = 80
schlaeger_hoehe = 12

# Steine - eine Liste mit allen Steinen
steine = []
stein_breite = 45
stein_hoehe = 20
stein_abstand = 5

# Punkte und Leben
punkte = 0
leben = 3

def erstelle_steine():
    # Diese Funktion erstellt alle Steine
    global steine
    steine = []
    farben = ["red", "orange", "yellow", "green", "blue"]

    for reihe in range(5):
        for spalte in range(8):
            x = spalte * (stein_breite + stein_abstand) + 10
            y = reihe * (stein_hoehe + stein_abstand) + 60
            farbe = farben[reihe]
            steine.append({"x": x, "y": y, "farbe": farbe})

# Am Anfang Steine erstellen
erstelle_steine()

def draw():
    screen.fill("black")

    # Alle Steine zeichnen
    for stein in steine:
        screen.draw.filled_rect(
            Rect(stein["x"], stein["y"], stein_breite, stein_hoehe),
            stein["farbe"]
        )

    # Ball zeichnen
    screen.draw.filled_circle((ball_x, ball_y), ball_groesse, "white")

    # Schläger zeichnen
    screen.draw.filled_rect(
        Rect(schlaeger_x, schlaeger_y, schlaeger_breite, schlaeger_hoehe),
        "cyan"
    )

    # Punkte und Leben anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=25)
    screen.draw.text(f"Leben: {leben}", (300, 10), color="white", fontsize=25)

    # Gewonnen?
    if len(steine) == 0:
        screen.draw.text("DU HAST GEWONNEN!", (50, 300), color="green", fontsize=35)

    # Verloren?
    if leben <= 0:
        screen.draw.text("GAME OVER", (100, 300), color="red", fontsize=45)

def update():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, punkte, leben

    if leben <= 0 or len(steine) == 0:
        return

    # Ball bewegen
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # Ball prallt von Wänden ab
    if ball_x - ball_groesse <= 0 or ball_x + ball_groesse >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Ball prallt von Decke ab
    if ball_y - ball_groesse <= 0:
        ball_speed_y = -ball_speed_y

    # Ball fällt runter - Leben verlieren
    if ball_y > HEIGHT:
        leben = leben - 1
        ball_x = 200
        ball_y = 400
        ball_speed_y = -4

    # Ball trifft Schläger
    if ball_y + ball_groesse >= schlaeger_y:
        if ball_x >= schlaeger_x and ball_x <= schlaeger_x + schlaeger_breite:
            ball_speed_y = -abs(ball_speed_y)

    # Ball trifft Steine
    for stein in steine[:]:  # [:] macht eine Kopie der Liste
        if (ball_x + ball_groesse > stein["x"] and
            ball_x - ball_groesse < stein["x"] + stein_breite and
            ball_y + ball_groesse > stein["y"] and
            ball_y - ball_groesse < stein["y"] + stein_hoehe):
            # Stein getroffen!
            steine.remove(stein)
            ball_speed_y = -ball_speed_y
            punkte = punkte + 10
            break

def on_mouse_down(pos):
    global schlaeger_x
    schlaeger_x = pos[0] - schlaeger_breite / 2

    if schlaeger_x < 0:
        schlaeger_x = 0
    if schlaeger_x > WIDTH - schlaeger_breite:
        schlaeger_x = WIDTH - schlaeger_breite

def on_mouse_move(pos):
    global schlaeger_x
    schlaeger_x = pos[0] - schlaeger_breite / 2

    if schlaeger_x < 0:
        schlaeger_x = 0
    if schlaeger_x > WIDTH - schlaeger_breite:
        schlaeger_x = WIDTH - schlaeger_breite
```

---

# Bonus: Bildschirm-Buttons erstellen 🔘

Manchmal brauchst du Buttons auf dem Bildschirm. So machst du das:

```python
# === SPIEL MIT BUTTONS ===

WIDTH = 400
HEIGHT = 600

# Spieler Position
spieler_x = 180
spieler_y = 300

# Button Positionen
button_links = Rect(20, 500, 80, 60)
button_rechts = Rect(120, 500, 80, 60)
button_hoch = Rect(220, 500, 80, 60)
button_runter = Rect(320, 500, 80, 60)

# Geschwindigkeit
speed = 8

def draw():
    screen.fill("darkblue")

    # Spieler zeichnen
    screen.draw.filled_rect(Rect(spieler_x, spieler_y, 40, 40), "red")

    # Buttons zeichnen
    screen.draw.filled_rect(button_links, "gray")
    screen.draw.filled_rect(button_rechts, "gray")
    screen.draw.filled_rect(button_hoch, "gray")
    screen.draw.filled_rect(button_runter, "gray")

    # Button Beschriftungen
    screen.draw.text("←", (45, 515), color="white", fontsize=35)
    screen.draw.text("→", (145, 515), color="white", fontsize=35)
    screen.draw.text("↑", (248, 515), color="white", fontsize=35)
    screen.draw.text("↓", (348, 515), color="white", fontsize=35)

def on_mouse_down(pos):
    global spieler_x, spieler_y

    # Welcher Button wurde gedrückt?
    if button_links.collidepoint(pos):
        spieler_x = spieler_x - speed

    if button_rechts.collidepoint(pos):
        spieler_x = spieler_x + speed

    if button_hoch.collidepoint(pos):
        spieler_y = spieler_y - speed

    if button_runter.collidepoint(pos):
        spieler_y = spieler_y + speed

    # Nicht aus dem Bildschirm gehen
    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - 40:
        spieler_x = WIDTH - 40
    if spieler_y < 0:
        spieler_y = 0
    if spieler_y > 450:
        spieler_y = 450
```

**Erklärung:**
- `Rect(x, y, breite, höhe)` erstellt ein Rechteck
- `collidepoint(pos)` prüft ob ein Punkt im Rechteck ist
- So wissen wir welchen Button du gedrückt hast!

---

## Wichtige Tipps

### 1. Variablen ändern mit `global`
Wenn du eine Variable in einer Funktion ändern willst, musst du `global` benutzen:
```python
punkte = 0

def update():
    global punkte  # Das brauchst du!
    punkte = punkte + 1
```

### 2. Zufallszahlen
```python
import random

# Zufällige Zahl zwischen 1 und 10
zahl = random.randint(1, 10)
```

### 3. Listen
```python
# Eine Liste erstellen
meine_liste = [1, 2, 3]

# Etwas hinzufügen
meine_liste.append(4)

# Etwas entfernen
meine_liste.remove(2)

# Wie viele Elemente?
anzahl = len(meine_liste)
```

---

## Deine Aufgaben

Jetzt bist du dran! Versuche diese Dinge:

1. **Ändere die Farben** in den Spielen
2. **Mach die Spiele schneller oder langsamer** (ändere die speed Variablen)
3. **Füge mehr Hindernisse hinzu**
4. **Kombiniere Ideen** aus verschiedenen Spielen

---

## Häufige Fehler

❌ **Fehler:** `NameError: name 'punkte' is not defined`
✅ **Lösung:** Hast du `global punkte` in der Funktion vergessen?

❌ **Fehler:** Nichts passiert wenn ich tippe
✅ **Lösung:** Prüfe ob du `on_mouse_down(pos)` richtig geschrieben hast

❌ **Fehler:** Das Spiel startet nicht
✅ **Lösung:** Hast du die Datei mit `.py` gespeichert?

---

**Viel Spaß beim Programmieren!** 🎮

Im nächsten Teil lernst du, wie du Bilder und Sounds hinzufügen kannst!