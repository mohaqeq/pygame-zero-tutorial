# === FANG DEN BALL ===
# Ein Ball faellt runter und du musst ihn fangen!
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
