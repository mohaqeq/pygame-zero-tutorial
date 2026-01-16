# === MÜNZEN SAMMELN ===
# Sammle Münzen und weiche Feinden aus!
#
# WICHTIG: Du brauchst diese Bilder im Ordner "images/":
# - spieler.png (ca. 40x40 Pixel)
# - muenze.png (ca. 30x30 Pixel)
# - feind.png (ca. 40x40 Pixel)

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