# Pygame Zero auf Pydroid - Teil 2: Bilder und Sound! 🎨🔊

Super! Du hast Teil 1 geschafft und kannst jetzt einfache Spiele machen. In diesem Teil lernst du, wie du deine Spiele mit **Bildern** und **Sounds** noch cooler machst!

---

## Ordnerstruktur vorbereiten

Pygame Zero braucht spezielle Ordner für Bilder und Sounds. So erstellst du sie:

### Schritt 1: Ordner erstellen
1. Öffne den Datei-Manager auf deinem Handy
2. Gehe zu dem Ordner wo dein Spiel gespeichert ist
3. Erstelle zwei neue Ordner:
   - `images` (für Bilder)
   - `sounds` (für Sounds)

**Wichtig:** Die Ordner müssen genau so heißen! Kleingeschrieben!

```
Dein_Spielordner/
├── meinspiel.py
├── images/
│   ├── spieler.png
│   └── feind.png
└── sounds/
    ├── sprung.wav
    └── punkt.wav
```

---

## Bilder verwenden

### Bilder finden oder erstellen

Du kannst:
1. **Kostenlose Bilder herunterladen** von:
   - [OpenGameArt.org](https://opengameart.org)
   - [Kenney.nl](https://kenney.nl/assets) (super für Anfänger!)

2. **Selbst malen** mit Apps wie:
   - Pixel Studio (kostenlos im Play Store)
   - Dotpict

**Tipp:** Bilder sollten `.png` Format haben und nicht zu groß sein (32x32 bis 128x128 Pixel sind gut)

### Bilder benennen

- Nur **Kleinbuchstaben** verwenden!
- Keine Leerzeichen (benutze `_` statt Leerzeichen)
- Beispiele: `spieler.png`, `vogel_blau.png`, `hindernis.png`

---

## Actors - Spielfiguren mit Bildern

In Pygame Zero heißen Spielfiguren mit Bildern **"Actors"** (Schauspieler).

### Grundlagen

```python
# === ACTOR GRUNDLAGEN ===

WIDTH = 400
HEIGHT = 600

# Actor erstellen - das Bild muss in /images/ sein!
# Ohne .png Endung schreiben!
spieler = Actor("spieler")

# Position setzen
spieler.x = 200
spieler.y = 300

def draw():
    screen.fill("skyblue")
    spieler.draw()  # Actor zeichnen

def update():
    # Actor bewegen
    spieler.x = spieler.x + 2

    # Wenn er rechts raus ist, links wieder rein
    if spieler.x > WIDTH + 50:
        spieler.x = -50

def on_mouse_down(pos):
    # Position ändern wenn getippt wird
    spieler.x = pos[0]
    spieler.y = pos[1]
```

**Erklärung:**
- `Actor("spieler")` lädt das Bild `images/spieler.png`
- `spieler.draw()` zeichnet den Actor auf den Bildschirm
- `spieler.x` und `spieler.y` sind die Position

### Nützliche Actor-Eigenschaften

```python
# Position
spieler.x = 100          # Horizontale Position
spieler.y = 200          # Vertikale Position
spieler.pos = (100, 200) # Beide zusammen

# Bild wechseln
spieler.image = "spieler_springt"  # Lädt images/spieler_springt.png

# Größe herausfinden
breite = spieler.width
hoehe = spieler.height

# Drehen
spieler.angle = 45  # 45 Grad drehen

# Spiegeln/Skalieren
spieler.scale = 2  # Doppelt so groß
```

### Kollisionen prüfen

```python
# Prüfen ob zwei Actors sich berühren
if spieler.colliderect(feind):
    print("Getroffen!")

# Prüfen ob Actor einen Punkt berührt
if spieler.collidepoint(pos):
    print("Angeklickt!")
```

---

## Sounds verwenden

### Sound-Dateien vorbereiten

- Sounds müssen `.wav` oder `.ogg` Format haben
- In den `sounds/` Ordner legen
- Kleinbuchstaben und keine Leerzeichen!

### Kostenlose Sounds finden

- [Freesound.org](https://freesound.org)
- [OpenGameArt.org](https://opengameart.org)

### Sounds abspielen

```python
# Sound abspielen (muss in sounds/ Ordner sein)
sounds.sprung.play()      # Spielt sounds/sprung.wav
sounds.punkt.play()       # Spielt sounds/punkt.wav
sounds.game_over.play()   # Spielt sounds/game_over.wav
```

---

# Spiel 1: Flappy Bird mit Bildern 🐦

Jetzt machen wir Flappy Bird mit echten Bildern!

### Benötigte Bilder
Erstelle oder lade diese Bilder herunter und speichere sie in `images/`:
- `vogel.png` - Ein Vogel (ca. 40x30 Pixel)
- `roehre_oben.png` - Röhre die nach unten zeigt
- `roehre_unten.png` - Röhre die nach oben zeigt

**Oder:** Benutze einfache Quadrate als Platzhalter!

```python
# === FLAPPY BIRD MIT BILDERN ===
import random

WIDTH = 400
HEIGHT = 600

# Vogel Actor
vogel = Actor("vogel")  # Lädt images/vogel.png
vogel.x = 100
vogel.y = 300

# Bewegung
vogel_speed = 0
schwerkraft = 0.5
sprung_kraft = -10

# Röhren (wir benutzen Actors)
roehre_oben = Actor("roehre_oben")
roehre_unten = Actor("roehre_unten")

# Röhren Position
roehre_x = 400
luecke_y = 250
luecke_hoehe = 180
roehre_speed = 4

# Spielstand
punkte = 0
spiel_laeuft = True

def setze_roehren():
    # Röhren an die richtige Position setzen
    roehre_oben.midbottom = (roehre_x, luecke_y)
    roehre_unten.midtop = (roehre_x, luecke_y + luecke_hoehe)

setze_roehren()

def draw():
    screen.fill("skyblue")

    # Wolken zeichnen (nur Deko)
    screen.draw.filled_circle((100, 80), 30, "white")
    screen.draw.filled_circle((130, 80), 40, "white")
    screen.draw.filled_circle((160, 80), 30, "white")

    screen.draw.filled_circle((300, 120), 25, "white")
    screen.draw.filled_circle((330, 120), 35, "white")

    # Röhren zeichnen
    roehre_oben.draw()
    roehre_unten.draw()

    # Vogel zeichnen
    vogel.draw()

    # Punkte
    screen.draw.text(f"{punkte}", (WIDTH/2 - 20, 30), color="white", fontsize=60)

    if not spiel_laeuft:
        screen.draw.text("GAME OVER", (80, 250), color="red", fontsize=50)
        screen.draw.text("Tippe zum Neustarten", (70, 320), color="white", fontsize=25)

def update():
    global vogel_speed, roehre_x, luecke_y, punkte, spiel_laeuft

    if not spiel_laeuft:
        return

    # Schwerkraft
    vogel_speed = vogel_speed + schwerkraft
    vogel.y = vogel.y + vogel_speed

    # Vogel dreht sich basierend auf Geschwindigkeit
    if vogel_speed < 0:
        vogel.angle = 20  # Nach oben zeigen
    else:
        vogel.angle = -20  # Nach unten zeigen

    # Röhren bewegen
    roehre_x = roehre_x - roehre_speed
    setze_roehren()

    # Neue Röhren
    if roehre_x < -50:
        roehre_x = WIDTH + 50
        luecke_y = random.randint(100, HEIGHT - luecke_hoehe - 100)
        punkte = punkte + 1
        # Sound abspielen (wenn du einen hast)
        # sounds.punkt.play()

    # Kollision mit Röhren
    if vogel.colliderect(roehre_oben) or vogel.colliderect(roehre_unten):
        spiel_laeuft = False
        # sounds.game_over.play()

    # Kollision mit Rand
    if vogel.y < 0 or vogel.y > HEIGHT:
        spiel_laeuft = False

def on_mouse_down(pos):
    global vogel_speed, spiel_laeuft, roehre_x, punkte

    if spiel_laeuft:
        vogel_speed = sprung_kraft
        # sounds.sprung.play()
    else:
        # Neustart
        spiel_laeuft = True
        vogel.y = 300
        vogel_speed = 0
        roehre_x = 400
        punkte = 0
```

---

# Spiel 2: Sammle die Münzen 💰

Ein Spiel wo du Münzen sammeln musst!

### Benötigte Bilder
- `spieler.png` - Deine Spielfigur (ca. 40x40 Pixel)
- `muenze.png` - Eine Münze (ca. 30x30 Pixel)
- `feind.png` - Ein Hindernis/Feind (ca. 40x40 Pixel)

```python
# === MÜNZEN SAMMELN ===
import random

WIDTH = 400
HEIGHT = 600

# Spieler
spieler = Actor("spieler")
spieler.x = 200
spieler.y = 500

# Münzen Liste
muenzen = []
for i in range(5):
    muenze = Actor("muenze")
    muenze.x = random.randint(30, WIDTH - 30)
    muenze.y = random.randint(50, 400)
    muenzen.append(muenze)

# Feinde Liste
feinde = []
for i in range(3):
    feind = Actor("feind")
    feind.x = random.randint(30, WIDTH - 30)
    feind.y = random.randint(100, 300)
    feind.speed_x = random.choice([-3, 3])  # Links oder rechts
    feinde.append(feind)

# Spielstand
punkte = 0
leben = 3
unverwundbar = 0  # Timer für Unverwundbarkeit

def draw():
    screen.fill("darkgreen")

    # Gras-Muster
    for x in range(0, WIDTH, 20):
        for y in range(0, HEIGHT, 20):
            if (x + y) % 40 == 0:
                screen.draw.filled_rect(Rect(x, y, 20, 20), "green")

    # Münzen zeichnen
    for muenze in muenzen:
        muenze.draw()

    # Feinde zeichnen
    for feind in feinde:
        feind.draw()

    # Spieler zeichnen (blinkt wenn unverwundbar)
    if unverwundbar <= 0 or unverwundbar % 10 < 5:
        spieler.draw()

    # Info anzeigen
    screen.draw.text(f"Münzen: {punkte}", (10, 10), color="yellow", fontsize=30)
    screen.draw.text(f"Leben: {leben}", (10, 50), color="red", fontsize=30)

    if leben <= 0:
        screen.draw.text("GAME OVER", (100, 280), color="red", fontsize=45)

    if len(muenzen) == 0:
        screen.draw.text("GEWONNEN!", (110, 280), color="yellow", fontsize=50)

def update():
    global punkte, leben, unverwundbar

    if leben <= 0 or len(muenzen) == 0:
        return

    # Unverwundbarkeits-Timer
    if unverwundbar > 0:
        unverwundbar = unverwundbar - 1

    # Feinde bewegen
    for feind in feinde:
        feind.x = feind.x + feind.speed_x

        # Am Rand umdrehen
        if feind.x < 30 or feind.x > WIDTH - 30:
            feind.speed_x = -feind.speed_x

    # Münzen sammeln
    for muenze in muenzen[:]:
        if spieler.colliderect(muenze):
            muenzen.remove(muenze)
            punkte = punkte + 1
            # sounds.muenze.play()

            # Neue Münze erstellen
            neue_muenze = Actor("muenze")
            neue_muenze.x = random.randint(30, WIDTH - 30)
            neue_muenze.y = random.randint(50, 400)
            muenzen.append(neue_muenze)

    # Feind-Kollision
    if unverwundbar <= 0:
        for feind in feinde:
            if spieler.colliderect(feind):
                leben = leben - 1
                unverwundbar = 120  # 2 Sekunden unverwundbar
                # sounds.autsch.play()

def on_mouse_down(pos):
    global spieler

    if leben > 0 and len(muenzen) > 0:
        spieler.x = pos[0]
        spieler.y = pos[1]

        # Nicht aus dem Bildschirm
        if spieler.x < 20:
            spieler.x = 20
        if spieler.x > WIDTH - 20:
            spieler.x = WIDTH - 20
        if spieler.y < 20:
            spieler.y = 20
        if spieler.y > HEIGHT - 20:
            spieler.y = HEIGHT - 20
```

---

# Spiel 3: Space Shooter 🚀

Schieße auf Aliens!

### Benötigte Bilder
- `rakete.png` - Dein Raumschiff
- `alien.png` - Die Aliens
- `schuss.png` - Ein kleiner Laserstrahl

```python
# === SPACE SHOOTER ===
import random

WIDTH = 400
HEIGHT = 600

# Raumschiff
rakete = Actor("rakete")
rakete.x = 200
rakete.midbottom = (200, HEIGHT - 20)

# Schüsse
schuesse = []

# Aliens
aliens = []
alien_timer = 0

# Spielstand
punkte = 0
leben = 3

def erstelle_alien():
    alien = Actor("alien")
    alien.x = random.randint(50, WIDTH - 50)
    alien.y = -30
    alien.speed = random.uniform(2, 5)  # Zufällige Geschwindigkeit
    aliens.append(alien)

def draw():
    # Weltraum-Hintergrund
    screen.fill("black")

    # Sterne
    import random
    random.seed(42)  # Immer gleiche Sterne
    for i in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        screen.draw.filled_circle((x, y), 1, "white")

    # Schüsse zeichnen
    for schuss in schuesse:
        schuss.draw()

    # Aliens zeichnen
    for alien in aliens:
        alien.draw()

    # Rakete zeichnen
    rakete.draw()

    # Info
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=30)
    screen.draw.text(f"Leben: {leben}", (10, 50), color="red", fontsize=30)

    # Schieß-Button
    screen.draw.filled_rect(Rect(WIDTH/2 - 50, HEIGHT - 80, 100, 50), "red")
    screen.draw.text("FEUER!", (WIDTH/2 - 35, HEIGHT - 70), color="white", fontsize=25)

    if leben <= 0:
        screen.draw.text("GAME OVER", (100, 280), color="red", fontsize=45)

def update():
    global alien_timer, punkte, leben

    if leben <= 0:
        return

    # Neue Aliens erstellen
    alien_timer = alien_timer + 1
    if alien_timer > 60:  # Alle 60 Frames
        erstelle_alien()
        alien_timer = 0

    # Schüsse bewegen
    for schuss in schuesse[:]:
        schuss.y = schuss.y - 10

        # Schuss aus dem Bildschirm?
        if schuss.y < -20:
            schuesse.remove(schuss)

    # Aliens bewegen
    for alien in aliens[:]:
        alien.y = alien.y + alien.speed

        # Alien unten angekommen?
        if alien.y > HEIGHT + 30:
            aliens.remove(alien)
            leben = leben - 1
            # sounds.autsch.play()

    # Treffer prüfen
    for schuss in schuesse[:]:
        for alien in aliens[:]:
            if schuss.colliderect(alien):
                if schuss in schuesse:
                    schuesse.remove(schuss)
                aliens.remove(alien)
                punkte = punkte + 10
                # sounds.explosion.play()
                break

def on_mouse_down(pos):
    global rakete

    if leben <= 0:
        return

    # Rakete bewegen (linke Hälfte des Bildschirms)
    if pos[1] < HEIGHT - 100:
        rakete.x = pos[0]

    # Schieß-Button gedrückt?
    feuer_button = Rect(WIDTH/2 - 50, HEIGHT - 80, 100, 50)
    if feuer_button.collidepoint(pos):
        schuss = Actor("schuss")
        schuss.midbottom = rakete.midtop
        schuesse.append(schuss)
        # sounds.schuss.play()

def on_mouse_move(pos):
    if leben > 0 and pos[1] < HEIGHT - 100:
        rakete.x = pos[0]
```

---

# Spiel 4: Verbessertes Ping Pong 🏓

Ping Pong mit Bildern und Sounds!

### Benötigte Bilder
- `schlaeger_gruen.png` - Dein Schläger
- `schlaeger_rot.png` - Computer-Schläger
- `ball.png` - Der Ball

### Benötigte Sounds
- `treffer.wav` - Wenn Ball Schläger trifft
- `punkt.wav` - Wenn jemand punktet

```python
# === VERBESSERTES PING PONG ===

WIDTH = 400
HEIGHT = 600

# Ball
ball = Actor("ball")
ball.x = 200
ball.y = 300
ball_speed_x = 5
ball_speed_y = 5

# Spieler Schläger
spieler = Actor("schlaeger_gruen")
spieler.midbottom = (200, HEIGHT - 20)

# Computer Schläger
computer = Actor("schlaeger_rot")
computer.midtop = (200, 20)
computer_speed = 4

# Punkte
spieler_punkte = 0
computer_punkte = 0

# Partikel für Effekte
partikel = []

def draw():
    screen.fill("black")

    # Spielfeld
    screen.draw.line((0, HEIGHT/2), (WIDTH, HEIGHT/2), "gray")
    screen.draw.rect(Rect(5, 5, WIDTH-10, HEIGHT-10), "white")

    # Partikel zeichnen
    for p in partikel:
        screen.draw.filled_circle((int(p["x"]), int(p["y"])), int(p["size"]), p["farbe"])

    # Schläger und Ball
    computer.draw()
    spieler.draw()
    ball.draw()

    # Punkte
    screen.draw.text(f"{computer_punkte}", (WIDTH/2 - 50, HEIGHT/2 - 60),
                     color="red", fontsize=50)
    screen.draw.text(f"{spieler_punkte}", (WIDTH/2 - 50, HEIGHT/2 + 20),
                     color="green", fontsize=50)

def erstelle_partikel(x, y, farbe):
    import random
    for i in range(10):
        p = {
            "x": x,
            "y": y,
            "speed_x": random.uniform(-5, 5),
            "speed_y": random.uniform(-5, 5),
            "size": random.randint(3, 8),
            "farbe": farbe,
            "leben": 30
        }
        partikel.append(p)

def update():
    global ball_speed_x, ball_speed_y, spieler_punkte, computer_punkte

    # Ball bewegen
    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y

    # Partikel bewegen
    for p in partikel[:]:
        p["x"] = p["x"] + p["speed_x"]
        p["y"] = p["y"] + p["speed_y"]
        p["leben"] = p["leben"] - 1
        p["size"] = p["size"] * 0.95
        if p["leben"] <= 0:
            partikel.remove(p)

    # Ball prallt von Seiten ab
    if ball.x <= 20 or ball.x >= WIDTH - 20:
        ball_speed_x = -ball_speed_x
        erstelle_partikel(ball.x, ball.y, "white")

    # Ball trifft Spieler
    if ball.colliderect(spieler):
        ball_speed_y = -abs(ball_speed_y)
        erstelle_partikel(ball.x, ball.y, "green")
        # sounds.treffer.play()

    # Ball trifft Computer
    if ball.colliderect(computer):
        ball_speed_y = abs(ball_speed_y)
        erstelle_partikel(ball.x, ball.y, "red")
        # sounds.treffer.play()

    # Punkt für Spieler
    if ball.y < 0:
        spieler_punkte = spieler_punkte + 1
        ball.x = 200
        ball.y = 300
        # sounds.punkt.play()

    # Punkt für Computer
    if ball.y > HEIGHT:
        computer_punkte = computer_punkte + 1
        ball.x = 200
        ball.y = 300
        # sounds.punkt.play()

    # Computer KI
    if ball.x < computer.x - 10:
        computer.x = computer.x - computer_speed
    elif ball.x > computer.x + 10:
        computer.x = computer.x + computer_speed

def on_mouse_down(pos):
    spieler.x = pos[0]

def on_mouse_move(pos):
    spieler.x = pos[0]
```

---

# Animationen erstellen 🎬

Du kannst Bilder wechseln um Animationen zu machen!

### Benötigte Bilder
Erstelle mehrere Bilder mit Nummern:
- `laufen1.png`
- `laufen2.png`
- `laufen3.png`
- `laufen4.png`

```python
# === ANIMATION BEISPIEL ===

WIDTH = 400
HEIGHT = 600

# Spieler mit Animation
spieler = Actor("laufen1")
spieler.pos = (200, 300)

# Animation Variablen
animation_frame = 0
animation_timer = 0
animation_bilder = ["laufen1", "laufen2", "laufen3", "laufen4"]

def draw():
    screen.fill("lightblue")
    spieler.draw()
    screen.draw.text("Tippe zum Bewegen!", (100, 50), color="black", fontsize=25)

def update():
    global animation_timer, animation_frame

    # Animation abspielen
    animation_timer = animation_timer + 1

    if animation_timer >= 10:  # Alle 10 Frames wechseln
        animation_timer = 0
        animation_frame = animation_frame + 1

        if animation_frame >= len(animation_bilder):
            animation_frame = 0

        # Bild wechseln
        spieler.image = animation_bilder[animation_frame]

def on_mouse_down(pos):
    spieler.x = pos[0]
    spieler.y = pos[1]
```

---

## Eigene Bilder erstellen (ohne App!)

Du kannst auch Bilder direkt im Code erstellen und speichern. Hier ist ein Hilfsprogramm:

```python
# === BILD-ERSTELLER ===
# Dieses Programm erstellt einfache Bilder für deine Spiele

WIDTH = 400
HEIGHT = 500

# Die Pixel-Daten für einen Vogel (8x8)
# 0 = durchsichtig, 1 = gelb, 2 = orange, 3 = schwarz, 4 = weiß
vogel_daten = [
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 3, 1, 1, 0, 0],
    [2, 2, 1, 1, 1, 1, 1, 0],
    [2, 2, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 4, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

farben = {
    0: None,  # Durchsichtig
    1: "yellow",
    2: "orange",
    3: "black",
    4: "white",
}

def draw():
    screen.fill("gray")

    screen.draw.text("Vogel-Vorschau (vergrößert):", (20, 20), color="white")

    # Vogel groß zeichnen
    pixel_groesse = 20
    start_x = 100
    start_y = 80

    for y, reihe in enumerate(vogel_daten):
        for x, pixel in enumerate(reihe):
            if farben[pixel] is not None:
                screen.draw.filled_rect(
                    Rect(start_x + x * pixel_groesse,
                         start_y + y * pixel_groesse,
                         pixel_groesse, pixel_groesse),
                    farben[pixel]
                )

    screen.draw.text("So erstellst du deine eigenen Bilder:", (20, 280), color="white")
    screen.draw.text("1. Benutze eine App wie 'Pixel Studio'", (20, 320), color="lightgray")
    screen.draw.text("2. Male ein kleines Bild (32x32)", (20, 350), color="lightgray")
    screen.draw.text("3. Speichere es als PNG in /images/", (20, 380), color="lightgray")
```

---

## Sound-Tipps

### Sounds in Pydroid

1. **Sounds herunterladen:**
   - Suche nach "free game sounds wav"
   - Oder nimm eigene Sounds mit dem Handy auf

2. **Sound konvertieren:**
   - Sounds müssen `.wav` oder `.ogg` sein
   - Benutze eine Konverter-App wenn nötig

3. **Sound im Code:**
```python
# Sound abspielen
sounds.mein_sound.play()

# Sound mit Lautstärke (0.0 bis 1.0)
sounds.mein_sound.play()
# Leider geht Lautstärke nicht direkt in pgzero,
# aber du kannst leisere Sounds erstellen
```

---

## Tipps für bessere Spiele

### 1. Hintergrund-Bilder
```python
hintergrund = Actor("hintergrund")
hintergrund.pos = (WIDTH/2, HEIGHT/2)

def draw():
    hintergrund.draw()  # Zuerst Hintergrund
    spieler.draw()      # Dann Spieler
```

### 2. Mehrere Level
```python
level = 1
level_hintergruende = ["level1", "level2", "level3"]

def draw():
    bg = Actor(level_hintergruende[level - 1])
    bg.draw()
```

### 3. Punkte speichern
```python
# Highscore speichern
def speichere_highscore(punkte):
    with open("highscore.txt", "w") as datei:
        datei.write(str(punkte))

# Highscore laden
def lade_highscore():
    try:
        with open("highscore.txt", "r") as datei:
            return int(datei.read())
    except:
        return 0
```

---

## Deine Aufgaben

1. **Füge Bilder hinzu** zu den Spielen aus Teil 1
2. **Erstelle eigene Pixel-Art** mit einer App
3. **Füge Sounds hinzu** wenn Punkte gesammelt werden
4. **Mache Animationen** für deinen Spieler
5. **Erstelle einen Hintergrund** für dein Spiel

---

## Checkliste für ein fertiges Spiel

- [ ] Spieler kann sich bewegen
- [ ] Es gibt ein Ziel (Punkte sammeln, überleben, etc.)
- [ ] Es gibt Hindernisse oder Feinde
- [ ] Punkte werden angezeigt
- [ ] Game Over wenn man verliert
- [ ] Möglichkeit zum Neustarten
- [ ] (Bonus) Bilder für alle Elemente
- [ ] (Bonus) Sounds für Aktionen
- [ ] (Bonus) Highscore speichern

---

**Super gemacht!** 🎉

Jetzt kannst du richtig coole Spiele machen. Zeig deinen Freunden was du programmiert hast!

**Tipp:** Teile deine Spiele! Du kannst die `.py` Datei und den `images/` Ordner zu deinen Freunden schicken, und sie können dein Spiel auf ihrem Handy spielen!