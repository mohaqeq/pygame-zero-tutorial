# Pygame Zero auf Pydroid - Teil 2: Bilder und Sound!

Super! Du hast Teil 1 geschafft und kannst jetzt einfache Spiele mit Formen machen. In diesem Teil lernst du, wie du deine Spiele mit **echten Bildern** und **Sounds** noch cooler machst!

**Was du am Ende kannst:**
- Bilder statt Formen in deinen Spielen benutzen
- Sounds abspielen wenn etwas passiert
- Animationen erstellen
- Deine Spiele professioneller aussehen lassen

**Was du vorher koennen musst:**
- Teil 1 durchgearbeitet haben
- Ein funktionierendes Spiel (z.B. Flappy Box) haben

---

## Kapitel 1: Vorbereitung - Ordner erstellen

### Ziel dieses Kapitels
Du erstellst die Ordnerstruktur die Pygame Zero braucht um Bilder und Sounds zu finden.

### So muss dein Projekt aussehen

```
MeinSpiel/              <- Dein Hauptordner
|-- meinspiel.py        <- Dein Python-Code
|-- images/             <- Ordner fuer BILDER
|   |-- spieler.png
|   |-- feind.png
|-- sounds/             <- Ordner fuer SOUNDS
    |-- sprung.wav
    |-- punkt.wav
```

### Schritt-fuer-Schritt: Ordner erstellen

**Schritt 1:** Oeffne den Datei-Manager auf deinem Handy

**Schritt 2:** Finde den Ordner wo dein Spiel gespeichert ist
- Meistens unter: Interner Speicher -> pydroid3

**Schritt 3:** Erstelle einen neuen Ordner namens `images`
- WICHTIG: Kleingeschrieben!
- Keine Grossbuchstaben!

**Schritt 4:** Erstelle einen neuen Ordner namens `sounds`
- Wieder: Kleingeschrieben!

**Fertig!** Jetzt kannst du Bilder und Sounds hinzufuegen.

### Wichtige Regeln fuer Dateinamen

| Richtig | Falsch |
|---------|--------|
| `spieler.png` | `Spieler.png` (Grossbuchstabe!) |
| `mein_vogel.png` | `mein vogel.png` (Leerzeichen!) |
| `feind1.png` | `feind 1.png` (Leerzeichen!) |
| `ball.png` | `ball.PNG` (Grossbuchstaben!) |

**Merke dir:**
- Nur **Kleinbuchstaben**
- Keine **Leerzeichen** (benutze `_` stattdessen)
- Keine **Sonderzeichen** wie ae, oe, ue

---

## Kapitel 2: Bilder finden oder erstellen

### Ziel dieses Kapitels
Du findest oder erstellst Bilder fuer deine Spiele.

### Woher bekomme ich Bilder?

**Option 1: Kostenlose Bilder herunterladen**

Diese Webseiten haben kostenlose Spielgrafiken:

1. **Kenney.nl** (am besten fuer Anfaenger!)
   - Viele einfache, schoene Bilder
   - Alles kostenlos
   - Suche nach "Kenney game assets"

2. **OpenGameArt.org**
   - Sehr viele Bilder
   - Verschiedene Stile
   - Achte auf die Lizenz!

**Option 2: Selbst malen**

Es gibt Apps um Pixel-Bilder zu malen:

1. **Pixel Studio** (kostenlos im Play Store)
   - Einfach zu benutzen
   - Perfekt fuer kleine Spielfiguren

2. **Dotpict** (kostenlos)
   - Sehr einfach
   - Gut fuer Anfaenger

### Welche Groesse sollten Bilder haben?

| Was | Empfohlene Groesse |
|-----|-------------------|
| Spielfigur | 32x32 oder 64x64 Pixel |
| Feind | 32x32 oder 64x64 Pixel |
| Muenze/Item | 16x16 oder 32x32 Pixel |
| Hintergrund | 400x600 Pixel (ganzer Bildschirm) |

**Tipp:** Kleinere Bilder sind besser! Grosse Bilder machen das Spiel langsam.

---

## Kapitel 3: Actors - Spielfiguren mit Bildern

### Ziel dieses Kapitels
Du lernst wie man Bilder als Spielfiguren benutzt.

### Was ist ein Actor?

In Pygame Zero heissen Spielfiguren mit Bildern **"Actors"** (englisch fuer "Schauspieler"). Ein Actor ist wie ein Rechteck, aber mit einem Bild drauf!

### Vergleich: Rechteck vs. Actor

**Vorher (mit Rechteck):**
```python
spieler_x = 100
spieler_y = 300

def draw():
    screen.draw.filled_rect(Rect(spieler_x, spieler_y, 40, 40), "red")
```

**Nachher (mit Actor):**
```python
spieler = Actor("spieler")  # Laedt images/spieler.png
spieler.x = 100
spieler.y = 300

def draw():
    spieler.draw()
```

**Was ist besser am Actor?**
- Zeigt ein echtes Bild
- Einfacher zu bewegen
- Hat eingebaute Kollisionserkennung

### Schritt-fuer-Schritt: Deinen ersten Actor erstellen

**Ziel:** Ein Bild auf dem Bildschirm anzeigen.

**Vorbereitung:** Du brauchst ein Bild namens `spieler.png` im `images/` Ordner.

**Schritt 1:** Actor erstellen
```python
# Der Name in Klammern ist der Dateiname OHNE .png
spieler = Actor("spieler")
```

**Schritt 2:** Position setzen
```python
spieler.x = WIDTH // 2  # Horizontal (links/rechts)
spieler.y = HEIGHT // 2  # Vertikal (oben/unten)
```

**Schritt 3:** Actor zeichnen
```python
def draw():
    screen.fill("skyblue")
    spieler.draw()  # Das ist alles!
```

### Komplettes Beispiel

```python
# === MEIN ERSTER ACTOR ===

import pygame
import pgzrun
from pgzero.builtins import Actor

WIDTH = 400
HEIGHT = 600

# Actor erstellen
# WICHTIG: "spieler" bedeutet -> images/spieler.png muss existieren!
spieler = Actor("spieler")
spieler.x = WIDTH // 2
spieler.y = HEIGHT // 2

def draw():
    screen.fill("skyblue")
    spieler.draw()

def update():
    # Actor nach rechts bewegen
    spieler.x = spieler.x + 2

    # Wenn rechts raus, links wieder rein
    if spieler.x > WIDTH + 50:
        spieler.x = -50

def on_mouse_down(pos):
    # Actor springt zu Fingerposition
    spieler.x = pos[0]
    spieler.y = pos[1]

# Diese Zeile startet das Spiel!
pgzrun.go()
```

### Was du mit Actors machen kannst

| Was | Wie | Beispiel |
|-----|-----|----------|
| Position aendern | `.x` und `.y` | `spieler.x = 100` |
| Bild wechseln | `.image` | `spieler.image = "spieler_springt"` |
| Drehen | `.angle` | `spieler.angle = 45` |
| Groesse aendern | `.scale` | `spieler.scale = 2` |
| Breite abfragen | `.width` | `print(spieler.width)` |
| Hoehe abfragen | `.height` | `print(spieler.height)` |

---

## Kapitel 4: Kollisionen mit Actors

### Ziel dieses Kapitels
Du lernst wie man prueft ob sich zwei Actors beruehren.

### Warum ist das einfacher als vorher?

**Vorher (Teil 1) - Kompliziert:**
```python
# Manuell pruefen ob sich Rechtecke ueberlappen
if spieler_x + spieler_breite > feind_x and spieler_x < feind_x + feind_breite:
    if spieler_y + spieler_hoehe > feind_y and spieler_y < feind_y + feind_hoehe:
        print("Getroffen!")
```

**Mit Actors - Einfach:**
```python
# Ein Befehl!
if spieler.colliderect(feind):
    print("Getroffen!")
```

### Die wichtigsten Kollisions-Befehle

**1. colliderect() - Beruehrt einen anderen Actor?**
```python
if spieler.colliderect(feind):
    print("Spieler beruehrt Feind!")
```

**2. collidepoint() - Wurde angeklickt/getippt?**
```python
def on_mouse_down(pos):
    if spieler.collidepoint(pos):
        print("Spieler wurde angetippt!")
```

### Beispiel: Muenzen sammeln

**Ziel:** Wenn der Spieler eine Muenze beruehrt, verschwindet sie.

```python
import pygame
import pgzrun
from pgzero.builtins import Actor

WIDTH = 400
HEIGHT = 600

spieler = Actor("spieler")
spieler.pos = (WIDTH // 2, HEIGHT - 100)

muenze = Actor("muenze")
muenze.pos = (WIDTH // 2, HEIGHT // 3)

punkte = 0
muenze_da = True

def draw():
    screen.fill("darkgreen")
    spieler.draw()
    if muenze_da:
        muenze.draw()
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=30)

def update():
    global punkte, muenze_da

    # Pruefen ob Spieler Muenze beruehrt
    if muenze_da and spieler.colliderect(muenze):
        punkte = punkte + 1
        muenze_da = False
        # Hier koennte man auch: sounds.muenze.play()

def on_mouse_down(pos):
    spieler.x = pos[0]
    spieler.y = pos[1]

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

## Kapitel 5: Sounds hinzufuegen

### Ziel dieses Kapitels
Du lernst wie man Sounds in dein Spiel einbaut.

### Sound-Dateien vorbereiten

**Welche Formate funktionieren?**
- `.wav` (am besten!)
- `.ogg` (auch gut)

**MP3 funktioniert NICHT immer!** Konvertiere MP3 zu WAV.

### Woher bekomme ich Sounds?

1. **Freesound.org** - Viele kostenlose Sounds
2. **OpenGameArt.org** - Auch Sounds fuer Spiele
3. **Selber aufnehmen** - Mit dem Handy!

### Schritt-fuer-Schritt: Einen Sound hinzufuegen

**Ziel:** Einen "Sprung" Sound abspielen.

**Schritt 1:** Sound-Datei finden
- Suche nach "jump sound effect free wav"
- Lade eine .wav Datei herunter

**Schritt 2:** Datei umbenennen
- Nenne sie `sprung.wav` (kleingeschrieben!)

**Schritt 3:** In sounds/ Ordner verschieben
- Die Datei muss in `sounds/sprung.wav` sein

**Schritt 4:** Im Code abspielen
```python
def on_mouse_down(pos):
    sounds.sprung.play()  # Das ist alles!
```

### Wichtig: Wie Sounds benannt werden

Der Dateiname wird zum Befehl:

| Dateiname | Befehl im Code |
|-----------|---------------|
| `sounds/sprung.wav` | `sounds.sprung.play()` |
| `sounds/punkt.wav` | `sounds.punkt.play()` |
| `sounds/game_over.wav` | `sounds.game_over.play()` |
| `sounds/muenze_sammel.wav` | `sounds.muenze_sammel.play()` |

**Achte auf:**
- Kleinbuchstaben
- Unterstriche statt Leerzeichen
- Keine Bindestriche (-)

### Beispiel: Spiel mit Sounds

```python
import pygame
import pgzrun
from pgzero.builtins import Actor

WIDTH = 400
HEIGHT = 600

spieler = Actor("spieler")
spieler.pos = (WIDTH // 4, HEIGHT - 100)

punkte = 0
spiel_vorbei = False

def draw():
    screen.fill("skyblue")
    spieler.draw()
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="black", fontsize=30)

    if spiel_vorbei:
        screen.draw.text("GAME OVER", (WIDTH // 4, HEIGHT // 2 - 20), color="red", fontsize=50)

def on_mouse_down(pos):
    global punkte, spiel_vorbei

    if not spiel_vorbei:
        # Sprung-Sound abspielen
        sounds.sprung.play()
        spieler.x = pos[0]

        # Punkt sammeln (Beispiel)
        punkte = punkte + 1
        sounds.punkt.play()

    if punkte >= 10:
        spiel_vorbei = True
        sounds.game_over.play()

# Diese Zeile startet das Spiel!
pgzrun.go()
```

### Wenn Sounds nicht funktionieren

**Problem:** `AttributeError: 'module' object has no attribute 'sprung'`

**Loesung:**
1. Pruefe ob die Datei im `sounds/` Ordner ist
2. Pruefe ob der Name kleingeschrieben ist
3. Pruefe ob es `.wav` oder `.ogg` ist (nicht `.mp3`)

---

## Kapitel 6: Flappy Bird mit Bildern und Sound

### Ziel dieses Kapitels
Du baust das Flappy Box Spiel zu einem echten Flappy Bird um!

### Was du brauchst

**Bilder (in `images/` Ordner):**
- `vogel.png` - Dein Vogel (ca. 40x30 Pixel)
- `roehre_oben.png` - Roehre von oben
- `roehre_unten.png` - Roehre von unten

**Sounds (in `sounds/` Ordner):**
- `flap.wav` - Fluegelschlag beim Tippen
- `punkt.wav` - Wenn du durch eine Roehre kommst
- `game_over.wav` - Wenn du stirbst

### Das komplette Spiel

```python
# === FLAPPY BIRD MIT BILDERN UND SOUND ===
# Benoetigte Bilder: vogel.png, roehre_oben.png, roehre_unten.png
# Benoetigte Sounds: flap.wav, punkt.wav, game_over.wav

import pygame
import pgzrun
from pgzero.builtins import Actor
import random

WIDTH = 400
HEIGHT = 600

# === DER VOGEL ===
vogel = Actor("vogel")
vogel.x = WIDTH // 4
vogel.y = HEIGHT // 2

vogel_speed = 0
schwerkraft = 0.5
sprung_kraft = -10

# === DIE ROEHREN ===
roehre_oben = Actor("roehre_oben")
roehre_unten = Actor("roehre_unten")

roehre_x = WIDTH
luecke_y = HEIGHT // 2 - 50
luecke_hoehe = 180
roehre_speed = 4

# === SPIELSTAND ===
punkte = 0
spiel_laeuft = True

def setze_roehren_position():
    roehre_oben.midbottom = (roehre_x, luecke_y)
    roehre_unten.midtop = (roehre_x, luecke_y + luecke_hoehe)

# Am Anfang positionieren
setze_roehren_position()

def draw():
    # Himmel
    screen.fill("skyblue")

    # Wolken (Dekoration)
    screen.draw.filled_circle((WIDTH // 4, 80), 30, "white")
    screen.draw.filled_circle((WIDTH // 4 + 30, 80), 40, "white")
    screen.draw.filled_circle((WIDTH // 4 + 60, 80), 30, "white")

    # Roehren
    roehre_oben.draw()
    roehre_unten.draw()

    # Vogel
    vogel.draw()

    # Punkte
    screen.draw.text(f"{punkte}", (WIDTH // 2 - 20, 30), color="white", fontsize=60)

    # Game Over
    if not spiel_laeuft:
        screen.draw.text("GAME OVER", (WIDTH // 5, HEIGHT // 2 - 50), color="red", fontsize=50)
        screen.draw.text("Tippe zum Neustarten", (WIDTH // 6, HEIGHT // 2 + 20), color="white", fontsize=25)

def update():
    global vogel_speed, roehre_x, luecke_y, punkte, spiel_laeuft

    if not spiel_laeuft:
        return

    # Schwerkraft
    vogel_speed = vogel_speed + schwerkraft
    vogel.y = vogel.y + vogel_speed

    # Vogel dreht sich
    if vogel_speed < 0:
        vogel.angle = 15
    else:
        vogel.angle = -15

    # Roehren bewegen
    roehre_x = roehre_x - roehre_speed
    setze_roehren_position()

    # Neue Roehren
    if roehre_x < -50:
        roehre_x = WIDTH + 50
        luecke_y = random.randint(100, HEIGHT - luecke_hoehe - 100)
        punkte = punkte + 1
        sounds.punkt.play()

    # Kollision mit Roehren
    if vogel.colliderect(roehre_oben) or vogel.colliderect(roehre_unten):
        spiel_laeuft = False
        sounds.game_over.play()

    # Kollision mit Rand
    if vogel.y < 0 or vogel.y > HEIGHT:
        spiel_laeuft = False
        sounds.game_over.play()

def on_mouse_down(pos):
    global vogel_speed, spiel_laeuft, roehre_x, punkte

    if spiel_laeuft:
        vogel_speed = sprung_kraft
        sounds.flap.play()
    else:
        # Neustart
        spiel_laeuft = True
        vogel.y = HEIGHT // 2
        vogel_speed = 0
        roehre_x = WIDTH
        punkte = 0

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

## Kapitel 7: Muenzen sammeln Spiel

### Ziel dieses Kapitels
Du baust ein Spiel wo du Muenzen sammelst und Feinden ausweichst.

### Was du brauchst

**Bilder:**
- `spieler.png` - Deine Spielfigur
- `muenze.png` - Eine Muenze
- `feind.png` - Ein Feind/Monster

**Sounds:**
- `muenze.wav` - Wenn Muenze gesammelt
- `autsch.wav` - Wenn Feind beruehrt

### Das komplette Spiel

```python
# === MUENZEN SAMMELN ===
# Sammle Muenzen und weiche Feinden aus!

import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect
import random

WIDTH = 400
HEIGHT = 600

# Spieler
spieler = Actor("spieler")
spieler.x = WIDTH // 2
spieler.y = HEIGHT - 100

# Muenzen erstellen
muenzen = []
for i in range(5):
    muenze = Actor("muenze")
    muenze.x = random.randint(30, WIDTH - 30)
    muenze.y = random.randint(50, HEIGHT * 2 // 3)
    muenzen.append(muenze)

# Feinde erstellen
feinde = []
for i in range(3):
    feind = Actor("feind")
    feind.x = random.randint(30, WIDTH - 30)
    feind.y = random.randint(100, HEIGHT // 2)
    feind.speed_x = random.choice([-3, 3])
    feinde.append(feind)

# Spielstand
punkte = 0
leben = 3
unverwundbar = 0

def draw():
    screen.fill("darkgreen")

    # Gras-Muster
    for x in range(0, WIDTH, 20):
        for y in range(0, HEIGHT, 20):
            if (x + y) % 40 == 0:
                screen.draw.filled_rect(Rect(x, y, 20, 20), "green")

    # Muenzen
    for muenze in muenzen:
        muenze.draw()

    # Feinde
    for feind in feinde:
        feind.draw()

    # Spieler (blinkt wenn unverwundbar)
    if unverwundbar <= 0 or unverwundbar % 10 < 5:
        spieler.draw()

    # Info
    screen.draw.text(f"Muenzen: {punkte}", (10, 10), color="yellow", fontsize=30)
    screen.draw.text(f"Leben: {leben}", (10, 50), color="red", fontsize=30)

    if leben <= 0:
        screen.draw.text("GAME OVER", (WIDTH // 4, HEIGHT // 2 - 20), color="red", fontsize=45)

def update():
    global punkte, leben, unverwundbar

    if leben <= 0:
        return

    # Unverwundbar-Timer
    if unverwundbar > 0:
        unverwundbar = unverwundbar - 1

    # Feinde bewegen
    for feind in feinde:
        feind.x = feind.x + feind.speed_x
        if feind.x < 30 or feind.x > WIDTH - 30:
            feind.speed_x = -feind.speed_x

    # Muenzen sammeln
    for muenze in muenzen[:]:
        if spieler.colliderect(muenze):
            muenzen.remove(muenze)
            punkte = punkte + 1
            sounds.muenze.play()

            neue_muenze = Actor("muenze")
            neue_muenze.x = random.randint(30, WIDTH - 30)
            neue_muenze.y = random.randint(50, HEIGHT * 2 // 3)
            muenzen.append(neue_muenze)

    # Feind-Kollision
    if unverwundbar <= 0:
        for feind in feinde:
            if spieler.colliderect(feind):
                leben = leben - 1
                unverwundbar = 120
                sounds.autsch.play()

def on_mouse_down(pos):
    if leben > 0:
        spieler.x = pos[0]
        spieler.y = pos[1]

        # Grenzen
        if spieler.x < 20: spieler.x = 20
        if spieler.x > WIDTH - 20: spieler.x = WIDTH - 20
        if spieler.y < 20: spieler.y = 20
        if spieler.y > HEIGHT - 20: spieler.y = HEIGHT - 20

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

## Kapitel 8: Animationen

### Ziel dieses Kapitels
Du lernst wie man Bilder wechselt um Animationen zu erstellen.

### Was ist eine Animation?

Eine Animation ist, wenn Bilder schnell hintereinander gezeigt werden:

```
Bild 1:  Person  (Bein vorne)
Bild 2:  Person  (Bein hinten)
Bild 3:  Person  (Bein vorne)
... und so weiter

-> Sieht aus wie Laufen!
```

### Bilder fuer Animation vorbereiten

Du brauchst mehrere Bilder mit Nummern:
- `images/laufen1.png`
- `images/laufen2.png`
- `images/laufen3.png`
- `images/laufen4.png`

### Komplettes Animationsbeispiel

```python
# === ANIMATION BEISPIEL ===
# Lerne wie man Animationen erstellt!

import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Spieler
spieler = Actor("laufen1")
spieler.pos = (WIDTH // 2, HEIGHT // 2)

# Animation
animation_bilder = ["laufen1", "laufen2", "laufen3", "laufen4"]
animation_frame = 0
animation_timer = 0

# Bewegung
ziel_x = WIDTH // 2
ziel_y = HEIGHT // 2
ist_am_laufen = False

def draw():
    screen.fill("lightblue")
    screen.draw.filled_rect(Rect(0, HEIGHT * 3 // 4, WIDTH, HEIGHT // 4), "green")
    spieler.draw()
    screen.draw.text("Tippe irgendwo!", (WIDTH // 6, 30), color="black", fontsize=25)

def update():
    global animation_timer, animation_frame, ist_am_laufen

    if ist_am_laufen:
        # Zum Ziel bewegen
        speed = 4
        diff_x = ziel_x - spieler.x
        diff_y = ziel_y - spieler.y

        if abs(diff_x) > speed:
            spieler.x = spieler.x + (speed if diff_x > 0 else -speed)
        else:
            spieler.x = ziel_x

        if abs(diff_y) > speed:
            spieler.y = spieler.y + (speed if diff_y > 0 else -speed)
        else:
            spieler.y = ziel_y

        # Angekommen?
        if spieler.x == ziel_x and spieler.y == ziel_y:
            ist_am_laufen = False
            spieler.image = animation_bilder[0]

        # Animation
        animation_timer = animation_timer + 1
        if animation_timer >= 8:
            animation_timer = 0
            animation_frame = (animation_frame + 1) % len(animation_bilder)
            spieler.image = animation_bilder[animation_frame]

def on_mouse_down(pos):
    global ziel_x, ziel_y, ist_am_laufen
    ziel_x = pos[0]
    ziel_y = pos[1]
    ist_am_laufen = True

# Diese Zeile startet das Spiel!
pgzrun.go()
```

---

## Zusammenfassung

### Was du gelernt hast

| Thema | Was du jetzt kannst |
|-------|-------------------|
| Ordner | `images/` und `sounds/` Ordner erstellen |
| Actors | Bilder als Spielfiguren benutzen |
| Kollision | `colliderect()` fuer einfache Kollisionspruefung |
| Sounds | `sounds.name.play()` fuer Sound-Effekte |
| Animation | Bilder wechseln fuer Bewegungseffekte |
| Listen | Mehrere Actors verwalten |

### Checkliste fuer ein fertiges Spiel

- [ ] Spieler kann sich bewegen
- [ ] Es gibt ein Ziel (Punkte, ueberleben, etc.)
- [ ] Es gibt Hindernisse oder Feinde
- [ ] Punkte werden angezeigt
- [ ] Game Over wenn man verliert
- [ ] Moeglichkeit zum Neustarten
- [ ] **Bilder fuer alle Elemente**
- [ ] **Sounds fuer Aktionen**
- [ ] **(Bonus) Animationen**

---

## Problemloesungen

### Wichtig fuer Pydroid!

In Pydroid 3 musst du IMMER diese Zeilen in deinem Code haben:

**Am Anfang der Datei:**
```python
import pygame
import pgzrun
from pgzero.builtins import Actor  # Wenn du Actor benutzt!
from pygame import Rect  # Wenn du Rect benutzt!
```

**Am Ende der Datei:**
```python
pgzrun.go()
```

### "NameError: name 'Rect' is not defined"
**Loesung:** Fuege `from pygame import Rect` am Anfang deiner Datei hinzu.

### "Actor not found" Fehler
```
Actor 'spieler' not found
```
**Loesung:**
1. Existiert `images/spieler.png`?
2. Ist der Name kleingeschrieben?
3. Ist die Endung `.png` (nicht `.PNG`)?

### Sound spielt nicht
```
AttributeError: 'module' object has no attribute 'sprung'
```
**Loesung:**
1. Existiert `sounds/sprung.wav`?
2. Ist es `.wav` oder `.ogg` (nicht `.mp3`)?
3. Ist der Name kleingeschrieben?

### Das Spiel startet nicht
**Loesung:**
1. Hast du `import pygame` am Anfang?
2. Hast du `import pgzrun` am Anfang?
3. Hast du `pgzrun.go()` am Ende?

### Bild ist zu gross/klein
**Loesung:**
```python
spieler.scale = 0.5  # Halb so gross
spieler.scale = 2    # Doppelt so gross
```

---

**Super gemacht!**

Du kannst jetzt richtig professionelle Spiele machen mit Bildern, Sounds und Animationen. Zeig deinen Freunden was du programmiert hast!

**Tipp:** Du kannst deine Spiele teilen! Schicke die `.py` Datei und die `images/` und `sounds/` Ordner zu deinen Freunden. Sie koennen dann dein Spiel auf ihrem Handy spielen!
