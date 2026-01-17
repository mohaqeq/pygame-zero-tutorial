# Pygame Zero auf Pydroid - Teil 1: Deine ersten Spiele!

Hallo! In diesem Tutorial lernst du, wie du coole Spiele auf deinem Android-Handy programmieren kannst. Wir benutzen dafuer **Pygame Zero** - das ist super einfach!

**Was du am Ende kannst:**
- Formen auf den Bildschirm malen
- Auf Touch-Eingaben reagieren
- 5 komplette Spiele programmieren!

---

## Kapitel 1: Installation und Einrichtung

### Ziel dieses Kapitels
Du installierst alles was du brauchst, um Spiele zu programmieren.

### Was du brauchst
1. Ein Android-Handy oder Tablet
2. Die App **Pydroid 3** (aus dem Play Store)
3. Das Plugin **Pydroid repository plugin** (auch aus dem Play Store)

### Schritt-fuer-Schritt Anleitung

**Schritt 1: Pydroid 3 installieren**
1. Oeffne den Google Play Store auf deinem Handy
2. Suche nach "Pydroid 3"
3. Tippe auf "Installieren"
4. Warte bis die Installation fertig ist

**Schritt 2: Das Plugin installieren**
1. Suche im Play Store nach "Pydroid repository plugin"
2. Installiere es (das hilft dir spaeter Pakete zu installieren)

**Schritt 3: Pygame Zero installieren**
1. Oeffne Pydroid 3
2. Tippe auf die drei Striche oben links (Menu)
3. Waehle "Pip" aus dem Menu
4. Gib in das Textfeld ein: `pgzero`
5. Tippe auf "Install"
6. Warte bis "Successfully installed" erscheint

**Geschafft!** Du bist bereit zum Programmieren!

---

## Kapitel 2: Wie ein Pygame Zero Spiel funktioniert

### Ziel dieses Kapitels
Du verstehst die Grundstruktur eines jeden Spiels.

### Das musst du wissen

Jedes Spiel das du machst hat drei wichtige Teile:

```
+---------------------------------------------------+
|  1. EINSTELLUNGEN (ganz oben)                     |
|     -> Wie gross ist das Spielfenster?            |
|     -> Welche Variablen brauchen wir?             |
+---------------------------------------------------+
|  2. DRAW FUNKTION                                 |
|     -> Was soll auf dem Bildschirm sein?          |
|     -> Wird staendig aufgerufen zum Zeichnen      |
+---------------------------------------------------+
|  3. UPDATE FUNKTION                               |
|     -> Was soll sich veraendern?                  |
|     -> Wird 60x pro Sekunde aufgerufen!           |
+---------------------------------------------------+
```

### Das einfachste Spiel

```python
import pygame
import pgzrun

# TEIL 1: EINSTELLUNGEN
# Hier sagen wir wie gross das Fenster sein soll
WIDTH = 400   # Breite in Pixeln (links nach rechts)
HEIGHT = 600  # Hoehe in Pixeln (oben nach unten)

# TEIL 2: DRAW FUNKTION
# Diese Funktion malt alles auf den Bildschirm
def draw():
    screen.fill("black")  # Hintergrund schwarz machen

# TEIL 3: UPDATE FUNKTION
# Diese Funktion wird immer wieder aufgerufen
def update():
    pass  # "pass" bedeutet: mach nichts

# Diese Zeile startet das Spiel!
pgzrun.go()
```

### So startest du dein Spiel

**Schritt 1:** Oeffne Pydroid 3

**Schritt 2:** Tippe auf das Ordner-Symbol und erstelle eine neue Datei

**Schritt 3:** Schreibe deinen Code

**Schritt 4:** Speichere die Datei mit der Endung `.py` (z.B. `meinspiel.py`)

**Schritt 5:** Tippe auf den Play-Knopf

---

## Kapitel 3: Formen zeichnen lernen

### Ziel dieses Kapitels
Du lernst verschiedene Formen auf den Bildschirm zu malen.

### Warum ist das wichtig?
Bevor wir Spiele machen, muessen wir wissen wie man Dinge zeichnet. In unseren ersten Spielen benutzen wir einfache Formen wie Rechtecke und Kreise als Spielfiguren.

### Das Koordinatensystem verstehen

Der Bildschirm ist wie ein Gitter aus Punkten. Jeder Punkt hat eine Position:
- **x** = wie weit nach rechts (0 ist ganz links)
- **y** = wie weit nach unten (0 ist ganz oben!)

```
    x = 0       x = 200      x = 400
     |           |            |
     +---------------------------+  <- y = 0
     |                           |
     |     * (100, 150)          |  <- y = 150
     |                           |
     |           * (200, 300)    |  <- y = 300
     |                           |
     |                           |
     +---------------------------+  <- y = 600
```

**Wichtig:** y = 0 ist OBEN, nicht unten! Das ist am Anfang verwirrend, aber du gewoehnst dich daran.

### Schritt 1: Ein Rechteck zeichnen

**Ziel:** Ein rotes Rechteck auf den Bildschirm malen.

**So geht's:**
```python
# Rechteck zeichnen
# screen.draw.filled_rect(Rect(x, y, breite, hoehe), farbe)
screen.draw.filled_rect(Rect(100, 200, 50, 50), "red")
```

**Erklaerung:**
- `Rect(100, 200, 50, 50)` erstellt ein Rechteck
  - `100` = x-Position (100 Pixel von links)
  - `200` = y-Position (200 Pixel von oben)
  - `50` = Breite
  - `50` = Hoehe
- `"red"` = die Farbe

### Schritt 2: Einen Kreis zeichnen

**Ziel:** Einen gelben Kreis auf den Bildschirm malen.

**So geht's:**
```python
# Kreis zeichnen
# screen.draw.filled_circle((x, y), radius, farbe)
screen.draw.filled_circle((200, 300), 30, "yellow")
```

**Erklaerung:**
- `(200, 300)` = die Mitte des Kreises (x=200, y=300)
- `30` = der Radius (wie gross der Kreis ist)
- `"yellow"` = die Farbe

### Schritt 3: Text schreiben

**Ziel:** Text auf den Bildschirm schreiben.

**So geht's:**
```python
# Text schreiben
# screen.draw.text("dein text", (x, y), color="farbe", fontsize=groesse)
screen.draw.text("Hallo!", (150, 100), color="white", fontsize=40)
```

### Komplettes Beispiel: Alles zusammen

**Ziel:** Verschiedene Formen und Text auf einem blauen Hintergrund zeigen.

```python
import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

def draw():
    # Schritt 1: Hintergrund blau machen
    screen.fill("darkblue")

    # Schritt 2: Ein rotes Rechteck zeichnen
    screen.draw.filled_rect(Rect(WIDTH // 4, HEIGHT // 3, 50, 50), "red")

    # Schritt 3: Ein gruenes Rechteck zeichnen
    screen.draw.filled_rect(Rect(WIDTH // 2, HEIGHT // 3, 80, 40), "green")

    # Schritt 4: Einen gelben Kreis zeichnen
    screen.draw.filled_circle((WIDTH // 2, HEIGHT // 2 + 50), 40, "yellow")

    # Schritt 5: Einen orangen Kreis zeichnen
    screen.draw.filled_circle((WIDTH // 4, HEIGHT - 150), 25, "orange")

    # Schritt 6: Eine Linie zeichnen
    screen.draw.line((50, HEIGHT - 100), (WIDTH - 50, HEIGHT - 100), "white")

    # Schritt 7: Text schreiben
    screen.draw.text("Hallo!", (WIDTH // 2 - 50, 80), color="white", fontsize=50)

# Diese Zeile startet das Spiel!
pgzrun.go()
```

### Uebung fuer dich

Versuche folgendes zu aendern:
1. Mach den Hintergrund gruen (`"green"`)
2. Mach das Rechteck groesser (aendere 50, 50 zu 100, 100)
3. Fuege deinen Namen als Text hinzu

### Farben die du benutzen kannst

| Englisch | Deutsch |
|----------|---------|
| `"red"` | Rot |
| `"blue"` | Blau |
| `"green"` | Gruen |
| `"yellow"` | Gelb |
| `"white"` | Weiss |
| `"black"` | Schwarz |
| `"orange"` | Orange |
| `"purple"` | Lila |
| `"pink"` | Rosa |
| `"cyan"` | Tuerkis |
| `"gray"` | Grau |
| `"darkblue"` | Dunkelblau |
| `"darkgreen"` | Dunkelgruen |
| `"skyblue"` | Himmelblau |

---

## Kapitel 4: Touch-Eingabe verstehen

### Ziel dieses Kapitels
Du lernst wie dein Spiel reagiert wenn jemand auf den Bildschirm tippt.

### Warum ist das wichtig?
Bei Handyspielen steuerst du alles durch Tippen. Du musst wissen, wo der Finger den Bildschirm beruehrt hat.

### Die spezielle Funktion: on_mouse_down

Wenn jemand auf den Bildschirm tippt, ruft Pygame Zero automatisch eine Funktion auf:

```python
def on_mouse_down(pos):
    # pos enthaelt die Position wo getippt wurde
    # pos[0] = x-Position
    # pos[1] = y-Position
```

### Das Problem mit Variablen

Wenn du eine Variable in einer Funktion aendern willst, musst du Python sagen, dass du die Variable von "aussen" meinst. Das machst du mit dem Wort `global`.

**Ohne global (funktioniert NICHT richtig):**
```python
punkte = 0

def on_mouse_down(pos):
    punkte = punkte + 1  # FEHLER! Python denkt das ist eine neue Variable
```

**Mit global (funktioniert!):**
```python
punkte = 0

def on_mouse_down(pos):
    global punkte  # Sag Python: ich meine die Variable von oben!
    punkte = punkte + 1  # Jetzt geht es!
```

### Schritt-fuer-Schritt: Ein Kreis folgt dem Finger

**Ziel:** Ein Kreis erscheint dort wo du auf den Bildschirm tippst.

**Schritt 1:** Die Grundstruktur erstellen
```python
WIDTH = 400
HEIGHT = 600

# Startposition fuer den Kreis
kreis_x = WIDTH // 2
kreis_y = HEIGHT // 2
```

**Schritt 2:** Den Kreis zeichnen
```python
def draw():
    screen.fill("darkblue")
    screen.draw.filled_circle((kreis_x, kreis_y), 40, "red")
```

**Schritt 3:** Auf Tippen reagieren
```python
def on_mouse_down(pos):
    global kreis_x, kreis_y  # WICHTIG: global nicht vergessen!
    kreis_x = pos[0]  # x-Position vom Finger
    kreis_y = pos[1]  # y-Position vom Finger
```

**Das komplette Programm:**
```python
import pygame
import pgzrun

WIDTH = 400
HEIGHT = 600

# Hier speichern wir die Position des Kreises
kreis_x = WIDTH // 2
kreis_y = HEIGHT // 2
anzahl_tipps = 0

def draw():
    screen.fill("darkblue")

    # Kreis an der aktuellen Position zeichnen
    screen.draw.filled_circle((kreis_x, kreis_y), 40, "red")

    # Anleitung zeigen
    screen.draw.text("Tippe irgendwo!", (WIDTH // 4, 50), color="white", fontsize=30)

    # Position anzeigen
    screen.draw.text(f"X: {kreis_x}", (20, HEIGHT - 80), color="yellow", fontsize=25)
    screen.draw.text(f"Y: {kreis_y}", (20, HEIGHT - 50), color="yellow", fontsize=25)
    screen.draw.text(f"Tipps: {anzahl_tipps}", (WIDTH - 150, HEIGHT - 65), color="green", fontsize=25)

def on_mouse_down(pos):
    global kreis_x, kreis_y, anzahl_tipps
    kreis_x = pos[0]
    kreis_y = pos[1]
    anzahl_tipps = anzahl_tipps + 1

# Diese Zeile startet das Spiel!
pgzrun.go()
```

### Was du gelernt hast

1. `on_mouse_down(pos)` wird aufgerufen wenn du tippst
2. `pos[0]` ist die x-Position (links/rechts)
3. `pos[1]` ist die y-Position (oben/unten)
4. `global` brauchst du um Variablen in Funktionen zu aendern

---

## Kapitel 5: Bewegung mit der Update-Funktion

### Ziel dieses Kapitels
Du lernst wie sich Dinge von alleine bewegen.

### Warum ist das wichtig?
In Spielen bewegen sich Baelle, Feinde und andere Objekte automatisch. Das passiert alles in der `update()` Funktion.

### Wie funktioniert update()?

Die `update()` Funktion wird 60 mal pro Sekunde aufgerufen! Wenn du dort die Position eines Objekts ein kleines bisschen aenderst, sieht es aus als wuerde es sich bewegen.

```
Sekunde 1:    *
Sekunde 2:      *
Sekunde 3:        *
Sekunde 4:          *
              -> Der Ball bewegt sich nach rechts!
```

### Schritt-fuer-Schritt: Ein Ball der sich bewegt

**Ziel:** Ein Ball bewegt sich von links nach rechts ueber den Bildschirm.

**Schritt 1:** Variablen fuer Position und Geschwindigkeit
```python
WIDTH = 400
HEIGHT = 600

ball_x = 50  # Startposition links
ball_y = HEIGHT // 2  # Mitte des Bildschirms
geschwindigkeit = 3  # Wie viele Pixel pro Frame
```

**Schritt 2:** Den Ball zeichnen
```python
def draw():
    screen.fill("darkblue")
    screen.draw.filled_circle((ball_x, ball_y), 20, "yellow")
```

**Schritt 3:** Den Ball bewegen
```python
def update():
    global ball_x

    # Ball nach rechts bewegen
    ball_x = ball_x + geschwindigkeit

    # Wenn Ball rechts raus ist, links wieder rein
    if ball_x > WIDTH + 20:
        ball_x = -20
```

**Das komplette Programm:**
```python
import pygame
import pgzrun

WIDTH = 400
HEIGHT = 600

ball_x = 50
ball_y = HEIGHT // 2
geschwindigkeit = 3

def draw():
    screen.fill("darkblue")
    screen.draw.filled_circle((ball_x, ball_y), 20, "yellow")
    screen.draw.text("Der Ball bewegt sich!", (WIDTH // 5, 50), color="white", fontsize=25)

def update():
    global ball_x
    ball_x = ball_x + geschwindigkeit

    if ball_x > WIDTH + 20:
        ball_x = -20

# Diese Zeile startet das Spiel!
pgzrun.go()
```

### Schwerkraft simulieren

In vielen Spielen fallen Dinge nach unten. Das nennt man Schwerkraft.

**Wie funktioniert Schwerkraft im Code?**
```python
geschwindigkeit_y = 0  # Am Anfang steht der Ball still
schwerkraft = 0.5      # Die Schwerkraft

def update():
    global ball_y, geschwindigkeit_y

    # Schwerkraft macht den Ball schneller (nach unten)
    geschwindigkeit_y = geschwindigkeit_y + schwerkraft

    # Ball faellt nach unten
    ball_y = ball_y + geschwindigkeit_y
```

---

# SPIEL 1: Fang den Ball!

### Ziel des Spiels
Ein Ball faellt von oben nach unten. Du musst ihn mit einem Faenger auffangen. Jedes Mal wenn du den Ball faengst, bekommst du einen Punkt!

### Was wir programmieren muessen

```
+-------------------------------------------+
|  1. Einen Ball der nach unten faellt      |
|  2. Einen Faenger den du steuern kannst   |
|  3. Punkte zaehlen                        |
|  4. Pruefen ob Ball gefangen wurde        |
|  5. Spiel schwerer machen                 |
+-------------------------------------------+
```

### Das komplette Spiel

```python
# === FANG DEN BALL ===
# Fange den Ball mit deinem Faenger!
# Tippe um den Faenger zu bewegen.

import pygame
import pgzrun
from pygame import Rect
import random

WIDTH = 400
HEIGHT = 600

# Der Ball
ball_x = WIDTH // 2
ball_y = 0
ball_speed = 5

# Der Faenger (du steuerst ihn)
faenger_breite = 80
faenger_hoehe = 20
faenger_x = WIDTH // 2 - faenger_breite // 2
faenger_y = HEIGHT - 50

# Punkte
punkte = 0

def draw():
    screen.fill("darkblue")

    # Ball zeichnen (ein Kreis)
    screen.draw.filled_circle((ball_x, ball_y), 20, "yellow")

    # Faenger zeichnen (ein Rechteck)
    screen.draw.filled_rect(
        Rect(faenger_x, faenger_y, faenger_breite, faenger_hoehe),
        "green"
    )

    # Punkte anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=30)

    # Anleitung
    screen.draw.text("Tippe um den Faenger zu bewegen!", (20, 50), color="gray", fontsize=18)

def update():
    global ball_x, ball_y, ball_speed, punkte

    # Ball faellt nach unten
    ball_y = ball_y + ball_speed

    # Pruefen ob Ball gefangen wurde
    if ball_y >= faenger_y:
        if ball_x >= faenger_x and ball_x <= faenger_x + faenger_breite:
            # Getroffen! Punkt!
            punkte = punkte + 1
            ball_y = 0
            ball_x = random.randint(30, WIDTH - 30)
            # Spiel wird schneller
            ball_speed = ball_speed + 0.5

    # Ball ist unten raus? Neuer Ball!
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(30, WIDTH - 30)
        punkte = 0  # Punkte zuruecksetzen
        ball_speed = 5

def on_mouse_down(pos):
    global faenger_x
    # Faenger bewegt sich dahin wo du tippst
    faenger_x = pos[0] - faenger_breite // 2

    # Nicht aus dem Bildschirm
    if faenger_x < 0:
        faenger_x = 0
    if faenger_x > WIDTH - faenger_breite:
        faenger_x = WIDTH - faenger_breite

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

# SPIEL 2: Springende Box

### Ziel des Spiels
Eine Box laeuft auf dem Boden. Hindernisse kommen von rechts. Du musst ueber sie springen! Wie das Dino-Spiel in Chrome.

### Das komplette Spiel

```python
# === SPRINGENDE BOX ===
# Eine Box springt ueber Hindernisse. Tippe um zu springen!

import pygame
import pgzrun
from pygame import Rect
import random

WIDTH = 400
HEIGHT = 600

# Die Box (der Spieler)
box_breite = 40
box_hoehe = 40
box_x = WIDTH // 5
boden_y = HEIGHT - 100
box_y = boden_y - box_hoehe
box_speed_y = 0  # Geschwindigkeit nach oben/unten
schwerkraft = 0.8

# Hindernis
hindernis_x = WIDTH
hindernis_breite = 40
hindernis_hoehe = 60

# Spielstand
punkte = 0
spiel_laeuft = True
geschwindigkeit = 6

def draw():
    screen.fill("skyblue")

    # Boden zeichnen
    screen.draw.filled_rect(Rect(0, boden_y, WIDTH, HEIGHT - boden_y), "green")

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
    screen.draw.text("Tippe zum Springen!", (WIDTH // 4, 50), color="gray", fontsize=20)

    # Game Over Nachricht
    if not spiel_laeuft:
        screen.draw.text("GAME OVER!", (WIDTH // 4, HEIGHT // 2 - 50), color="red", fontsize=50)
        screen.draw.text("Tippe zum Neustarten", (WIDTH // 5, HEIGHT // 2 + 20), color="black", fontsize=25)

def update():
    global box_y, box_speed_y, hindernis_x, punkte, spiel_laeuft, geschwindigkeit

    if not spiel_laeuft:
        return  # Nichts machen wenn Spiel vorbei

    # Schwerkraft - Box faellt nach unten
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
        hindernis_x = WIDTH + random.randint(0, WIDTH // 2)
        punkte = punkte + 1
        # Spiel wird schneller
        if geschwindigkeit < 15:
            geschwindigkeit = geschwindigkeit + 0.3

    # Kollision pruefen (hat Box das Hindernis beruehrt?)
    hindernis_y = boden_y - hindernis_hoehe

    # Pruefen ob sich Box und Hindernis ueberlappen
    if box_x + box_breite > hindernis_x and box_x < hindernis_x + hindernis_breite:
        if box_y + box_hoehe > hindernis_y:
            spiel_laeuft = False

def on_mouse_down(pos):
    global box_speed_y, spiel_laeuft, punkte, hindernis_x, geschwindigkeit, box_y

    if spiel_laeuft:
        # Nur springen wenn Box auf dem Boden ist
        if box_y + box_hoehe >= boden_y - 5:
            box_speed_y = -15  # Nach oben springen!
    else:
        # Spiel neu starten
        spiel_laeuft = True
        punkte = 0
        hindernis_x = WIDTH
        geschwindigkeit = 6
        box_y = boden_y - box_hoehe
        box_speed_y = 0

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

# SPIEL 3: Flappy Box

### Ziel des Spiels
Eine Box fliegt durch Roehren. Tippe um nach oben zu fliegen. Beruehre keine Roehre!

### Das komplette Spiel

```python
# === FLAPPY BOX ===
# Wie Flappy Bird, aber mit einer Box! Tippe um nach oben zu fliegen.

import pygame
import pgzrun
from pygame import Rect
import random

WIDTH = 400
HEIGHT = 600

# Die Box (der Spieler)
box_x = WIDTH // 4
box_y = HEIGHT // 2
box_groesse = 30
box_speed_y = 0
schwerkraft = 0.5
sprung_kraft = -10

# Roehren (Hindernisse)
roehre_x = WIDTH
luecke_y = HEIGHT // 2 - 90  # Wo ist die Luecke
luecke_hoehe = 180  # Wie gross ist die Luecke
roehre_breite = 60
roehre_speed = 4

# Spielstand
punkte = 0
spiel_laeuft = True

def draw():
    screen.fill("skyblue")

    # Obere Roehre zeichnen
    screen.draw.filled_rect(
        Rect(roehre_x, 0, roehre_breite, luecke_y),
        "green"
    )

    # Untere Roehre zeichnen
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
    screen.draw.text(f"{punkte}", (WIDTH // 2 - 20, 50), color="white", fontsize=60)

    # Game Over
    if not spiel_laeuft:
        screen.draw.text("GAME OVER", (WIDTH // 5, HEIGHT // 2 - 50), color="red", fontsize=50)
        screen.draw.text("Tippe zum Neustarten", (WIDTH // 6, HEIGHT // 2 + 20), color="black", fontsize=25)

def update():
    global box_y, box_speed_y, roehre_x, luecke_y, punkte, spiel_laeuft

    if not spiel_laeuft:
        return

    # Schwerkraft - Box faellt nach unten
    box_speed_y = box_speed_y + schwerkraft
    box_y = box_y + box_speed_y

    # Roehre bewegt sich nach links
    roehre_x = roehre_x - roehre_speed

    # Neue Roehre wenn alte weg ist
    if roehre_x < -roehre_breite:
        roehre_x = WIDTH
        luecke_y = random.randint(80, HEIGHT - luecke_hoehe - 80)
        punkte = punkte + 1

    # Kollision mit Roehren pruefen
    if box_x + box_groesse > roehre_x and box_x < roehre_x + roehre_breite:
        # In der Roehren-Zone
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
        box_y = HEIGHT // 2
        box_speed_y = 0
        roehre_x = WIDTH
        punkte = 0

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

# SPIEL 4: Ping Pong

### Ziel des Spiels
Ein Ball springt hin und her. Du spielst gegen den Computer. Triff den Ball mit deinem Schlaeger!

### Das komplette Spiel

```python
# === PING PONG ===
# Klassisches Ping Pong! Du spielst gegen den Computer.
# Tippe oder ziehe um deinen Schlaeger zu bewegen.

import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Der Ball
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_groesse = 15
ball_speed_x = 5
ball_speed_y = 5

# Spieler Schlaeger (unten)
spieler_x = WIDTH // 2 - 50
spieler_y = HEIGHT - 50
schlaeger_breite = 100
schlaeger_hoehe = 15

# Computer Schlaeger (oben)
computer_x = WIDTH // 2 - 50
computer_y = 30
computer_speed = 4

# Punkte
spieler_punkte = 0
computer_punkte = 0

def draw():
    screen.fill("black")

    # Mittellinie
    screen.draw.line((0, HEIGHT // 2), (WIDTH, HEIGHT // 2), "gray")

    # Ball zeichnen
    screen.draw.filled_rect(
        Rect(ball_x, ball_y, ball_groesse, ball_groesse),
        "white"
    )

    # Spieler Schlaeger (gruen)
    screen.draw.filled_rect(
        Rect(spieler_x, spieler_y, schlaeger_breite, schlaeger_hoehe),
        "green"
    )

    # Computer Schlaeger (rot)
    screen.draw.filled_rect(
        Rect(computer_x, computer_y, schlaeger_breite, schlaeger_hoehe),
        "red"
    )

    # Punkte anzeigen
    screen.draw.text(f"Computer: {computer_punkte}", (10, HEIGHT // 2 - 40),
                     color="red", fontsize=25)
    screen.draw.text(f"Du: {spieler_punkte}", (10, HEIGHT // 2 + 10),
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

    # Ball trifft Spieler Schlaeger
    if ball_y + ball_groesse >= spieler_y:
        if ball_x + ball_groesse >= spieler_x and ball_x <= spieler_x + schlaeger_breite:
            ball_speed_y = -abs(ball_speed_y)  # Nach oben

    # Ball trifft Computer Schlaeger
    if ball_y <= computer_y + schlaeger_hoehe:
        if ball_x + ball_groesse >= computer_x and ball_x <= computer_x + schlaeger_breite:
            ball_speed_y = abs(ball_speed_y)  # Nach unten

    # Punkt fuer Spieler (Ball oben raus)
    if ball_y < 0:
        spieler_punkte = spieler_punkte + 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Punkt fuer Computer (Ball unten raus)
    if ball_y > HEIGHT:
        computer_punkte = computer_punkte + 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Computer KI - folgt dem Ball
    ball_mitte = ball_x + ball_groesse // 2
    computer_mitte = computer_x + schlaeger_breite // 2

    if ball_mitte < computer_mitte - 10:
        computer_x = computer_x - computer_speed
    elif ball_mitte > computer_mitte + 10:
        computer_x = computer_x + computer_speed

def on_mouse_down(pos):
    global spieler_x
    # Spieler Schlaeger folgt dem Finger
    spieler_x = pos[0] - schlaeger_breite // 2

    # Nicht aus dem Bildschirm gehen
    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - schlaeger_breite:
        spieler_x = WIDTH - schlaeger_breite

# Diese Funktion wird aufgerufen wenn der Finger sich bewegt
def on_mouse_move(pos):
    global spieler_x
    spieler_x = pos[0] - schlaeger_breite // 2

    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - schlaeger_breite:
        spieler_x = WIDTH - schlaeger_breite

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

# SPIEL 5: Breakout

### Ziel des Spiels
Zerstoere alle Steine mit dem Ball! Lass den Ball nicht fallen.

### Das komplette Spiel

```python
# === BREAKOUT ===
# Zerstoere alle Steine mit dem Ball!
# Tippe oder ziehe um den Schlaeger zu bewegen.

import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Ball
ball_x = WIDTH // 2
ball_y = HEIGHT * 2 // 3
ball_groesse = 12
ball_speed_x = 4
ball_speed_y = -4

# Schlaeger
schlaeger_x = WIDTH // 2 - 40
schlaeger_y = HEIGHT - 50
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

    # Schlaeger zeichnen
    screen.draw.filled_rect(
        Rect(schlaeger_x, schlaeger_y, schlaeger_breite, schlaeger_hoehe),
        "cyan"
    )

    # Punkte und Leben anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=25)
    screen.draw.text(f"Leben: {leben}", (WIDTH - 100, 10), color="white", fontsize=25)

    # Gewonnen?
    if len(steine) == 0:
        screen.draw.text("DU HAST GEWONNEN!", (WIDTH // 8, HEIGHT // 2), color="green", fontsize=35)

    # Verloren?
    if leben <= 0:
        screen.draw.text("GAME OVER", (WIDTH // 4, HEIGHT // 2), color="red", fontsize=45)

def update():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, punkte, leben

    if leben <= 0 or len(steine) == 0:
        return

    # Ball bewegen
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # Ball prallt von Waenden ab
    if ball_x - ball_groesse <= 0 or ball_x + ball_groesse >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Ball prallt von Decke ab
    if ball_y - ball_groesse <= 0:
        ball_speed_y = -ball_speed_y

    # Ball faellt runter - Leben verlieren
    if ball_y > HEIGHT:
        leben = leben - 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT * 2 // 3
        ball_speed_y = -4

    # Ball trifft Schlaeger
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
    schlaeger_x = pos[0] - schlaeger_breite // 2

    if schlaeger_x < 0:
        schlaeger_x = 0
    if schlaeger_x > WIDTH - schlaeger_breite:
        schlaeger_x = WIDTH - schlaeger_breite

def on_mouse_move(pos):
    global schlaeger_x
    schlaeger_x = pos[0] - schlaeger_breite // 2

    if schlaeger_x < 0:
        schlaeger_x = 0
    if schlaeger_x > WIDTH - schlaeger_breite:
        schlaeger_x = WIDTH - schlaeger_breite

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

# Bonus: Bildschirm-Buttons erstellen

### Ziel dieses Kapitels
Du lernst Buttons auf den Bildschirm zu zeichnen die du antippen kannst.

### Beispiel mit Buttons

```python
# === SPIEL MIT BUTTONS ===
# Lerne wie man Bildschirm-Buttons erstellt
# Tippe auf die Buttons um die Box zu bewegen

import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Spieler Position
spieler_x = WIDTH // 2 - 20
spieler_y = HEIGHT // 2 - 70

# Button Bereich (unten)
button_bereich_y = HEIGHT - 120
button_breite = 80
button_hoehe = 60
button_abstand = 10

# Button Positionen - gleichmaessig verteilt
button_links = Rect(button_abstand, button_bereich_y, button_breite, button_hoehe)
button_rechts = Rect(button_abstand + button_breite + button_abstand, button_bereich_y, button_breite, button_hoehe)
button_hoch = Rect(WIDTH - 2 * button_breite - 2 * button_abstand, button_bereich_y, button_breite, button_hoehe)
button_runter = Rect(WIDTH - button_breite - button_abstand, button_bereich_y, button_breite, button_hoehe)

# Geschwindigkeit
speed = 15

# Spielbereich
spielbereich_rand = 10
spielbereich_hoehe = HEIGHT - 150

def draw():
    screen.fill("darkblue")

    # Spielbereich markieren
    screen.draw.rect(Rect(spielbereich_rand, spielbereich_rand, WIDTH - 2 * spielbereich_rand, spielbereich_hoehe), "white")

    # Spieler zeichnen
    screen.draw.filled_rect(Rect(spieler_x, spieler_y, 40, 40), "red")

    # Buttons zeichnen
    screen.draw.filled_rect(button_links, "gray")
    screen.draw.filled_rect(button_rechts, "gray")
    screen.draw.filled_rect(button_hoch, "gray")
    screen.draw.filled_rect(button_runter, "gray")

    # Button Rahmen
    screen.draw.rect(button_links, "white")
    screen.draw.rect(button_rechts, "white")
    screen.draw.rect(button_hoch, "white")
    screen.draw.rect(button_runter, "white")

    # Button Beschriftungen - zentriert in jedem Button
    screen.draw.text("<", (button_links.x + button_breite // 2 - 8, button_links.y + button_hoehe // 2 - 15), color="white", fontsize=35)
    screen.draw.text(">", (button_rechts.x + button_breite // 2 - 8, button_rechts.y + button_hoehe // 2 - 15), color="white", fontsize=35)
    screen.draw.text("^", (button_hoch.x + button_breite // 2 - 8, button_hoch.y + button_hoehe // 2 - 15), color="white", fontsize=35)
    screen.draw.text("v", (button_runter.x + button_breite // 2 - 8, button_runter.y + button_hoehe // 2 - 15), color="white", fontsize=35)

    # Anleitung
    screen.draw.text("Tippe die Buttons!", (WIDTH // 4, HEIGHT - 40), color="yellow", fontsize=25)

def on_mouse_down(pos):
    global spieler_x, spieler_y

    # Welcher Button wurde gedrueckt?
    if button_links.collidepoint(pos):
        spieler_x = spieler_x - speed

    if button_rechts.collidepoint(pos):
        spieler_x = spieler_x + speed

    if button_hoch.collidepoint(pos):
        spieler_y = spieler_y - speed

    if button_runter.collidepoint(pos):
        spieler_y = spieler_y + speed

    # Nicht aus dem Spielbereich gehen
    if spieler_x < spielbereich_rand + 5:
        spieler_x = spielbereich_rand + 5
    if spieler_x > WIDTH - spielbereich_rand - 45:
        spieler_x = WIDTH - spielbereich_rand - 45
    if spieler_y < spielbereich_rand + 5:
        spieler_y = spielbereich_rand + 5
    if spieler_y > spielbereich_hoehe - 35:
        spieler_y = spielbereich_hoehe - 35

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

# Zusammenfassung: Was du gelernt hast

## Die wichtigsten Funktionen

| Funktion | Wann wird sie aufgerufen? |
|----------|--------------------------|
| `draw()` | Um den Bildschirm zu zeichnen |
| `update()` | 60 mal pro Sekunde (fuer Bewegung) |
| `on_mouse_down(pos)` | Wenn du auf den Bildschirm tippst |
| `on_mouse_move(pos)` | Wenn du den Finger ueber den Bildschirm ziehst |

## Wichtige Konzepte

1. **Koordinaten:** x = links/rechts, y = oben/unten (y=0 ist OBEN!)
2. **global:** Brauchst du um Variablen in Funktionen zu aendern
3. **Kollision:** Pruefen ob sich zwei Rechtecke ueberlappen
4. **Schwerkraft:** Geschwindigkeit wird immer groesser -> Objekt faellt schneller
5. **Listen:** Speichern viele Objekte zusammen (z.B. alle Steine)

---

## Haeufige Fehler und Loesungen

| Fehler | Loesung |
|--------|--------|
| `NameError: name 'Rect' is not defined` | Fuege `from pygame import Rect` am Anfang hinzu |
| `NameError: name 'punkte' is not defined` | Hast du `global punkte` vergessen? |
| Nichts passiert beim Tippen | Pruefe ob `on_mouse_down(pos)` richtig geschrieben ist |
| Das Spiel startet nicht | Hast du `import pygame`, `import pgzrun` und `pgzrun.go()` am Ende? |

### Wichtig fuer Pydroid!

In Pydroid 3 musst du IMMER diese Zeilen in deinem Code haben:

**Am Anfang der Datei:**
```python
import pygame
import pgzrun
from pgzero.builtins import Actor  # Wenn du Actor benutzt (Teil 2)!
from pygame import Rect  # Wenn du Rect benutzt!
```

**Am Ende der Datei:**
```python
pgzrun.go()
```

Ohne diese Zeilen bekommst du Fehler!

---

## Naechste Schritte

1. **Probiere die Spiele aus** und aendere die Werte (Geschwindigkeit, Groessen, Farben)
2. **Kombiniere Ideen** aus verschiedenen Spielen
3. **Lies Teil 2** um zu lernen wie man Bilder und Sounds hinzufuegt!

**Viel Spass beim Programmieren!**
