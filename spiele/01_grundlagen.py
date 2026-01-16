# === GRUNDLAGEN - FORMEN ZEICHNEN ===
# Lerne wie man Formen auf den Bildschirm malt

import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

def draw():
    # Hintergrund blau machen
    screen.fill("darkblue")

    # Ein Rechteck (Rect) zeichnen
    # Rect(x, y, breite, höhe)
    screen.draw.filled_rect(Rect(100, 200, 50, 50), "red")

    # Noch ein Rechteck
    screen.draw.filled_rect(Rect(200, 200, 80, 40), "green")

    # Einen Kreis zeichnen
    # circle((x, y), radius, farbe)
    screen.draw.filled_circle((200, 350), 40, "yellow")

    # Noch ein Kreis
    screen.draw.filled_circle((100, 450), 25, "orange")

    # Eine Linie zeichnen
    screen.draw.line((50, 500), (350, 500), "white")

    # Text schreiben
    screen.draw.text("Hallo!", (150, 80), color="white", fontsize=50)
    screen.draw.text("Das sind Formen!", (100, 550), color="pink", fontsize=25)

# Diese Zeile startet das Spiel!
pgzrun.go()
