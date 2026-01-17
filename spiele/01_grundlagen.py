# === GRUNDLAGEN - FORMEN ZEICHNEN ===
# Lerne wie man Formen auf den Bildschirm malt

import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

def draw():
    # Hintergrund blau machen
    screen.fill("darkblue")

    # Ein Rechteck (Rect) zeichnen
    # Rect(x, y, breite, hoehe)
    screen.draw.filled_rect(Rect(WIDTH // 4, HEIGHT // 3, 50, 50), "red")

    # Noch ein Rechteck
    screen.draw.filled_rect(Rect(WIDTH // 2, HEIGHT // 3, 80, 40), "green")

    # Einen Kreis zeichnen
    # circle((x, y), radius, farbe)
    screen.draw.filled_circle((WIDTH // 2, HEIGHT // 2 + 50), 40, "yellow")

    # Noch ein Kreis
    screen.draw.filled_circle((WIDTH // 4, HEIGHT - 150), 25, "orange")

    # Eine Linie zeichnen
    screen.draw.line((50, HEIGHT - 100), (WIDTH - 50, HEIGHT - 100), "white")

    # Text schreiben
    screen.draw.text("Hallo!", (WIDTH // 2 - 50, 80), color="white", fontsize=50)
    screen.draw.text("Das sind Formen!", (WIDTH // 4, HEIGHT - 50), color="pink", fontsize=25)

# Diese Zeile startet das Spiel!
pgzrun.go()
