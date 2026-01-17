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
