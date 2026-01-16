# === FLAPPY BOX ===
# Wie Flappy Bird, aber mit einer Box! Tippe um nach oben zu fliegen.

import pgzrun
from pygame import Rect
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

# Diese Zeile startet das Spiel!
pgzrun.go()
