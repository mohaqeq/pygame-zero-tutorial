# === SPRINGENDE BOX ===
# Eine Box springt über Hindernisse. Tippe um zu springen!

import pgzrun
from pygame import Rect
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

# Diese Zeile startet das Spiel!
pgzrun.go()
