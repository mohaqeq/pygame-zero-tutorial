# === FANG DEN BALL ===
# Ein Ball fällt runter und du musst ihn fangen!
# Tippe um den Fänger zu bewegen.

import random

WIDTH = 400
HEIGHT = 600

# Der Ball
ball_x = 200
ball_y = 0
ball_speed = 5

# Der Fänger (du steuerst ihn)
faenger_x = 175
faenger_y = 550
faenger_breite = 80
faenger_hoehe = 20

# Punkte
punkte = 0

def draw():
    screen.fill("darkblue")

    # Ball zeichnen (ein Kreis)
    screen.draw.filled_circle((ball_x, ball_y), 20, "yellow")

    # Fänger zeichnen (ein Rechteck)
    screen.draw.filled_rect(
        Rect(faenger_x, faenger_y, faenger_breite, faenger_hoehe),
        "green"
    )

    # Punkte anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=30)

    # Anleitung
    screen.draw.text("Tippe um den Fänger zu bewegen!", (40, 50), color="gray", fontsize=18)

def update():
    global ball_x, ball_y, ball_speed, punkte

    # Ball fällt nach unten
    ball_y = ball_y + ball_speed

    # Prüfen ob Ball gefangen wurde
    if ball_y >= faenger_y:
        if ball_x >= faenger_x and ball_x <= faenger_x + faenger_breite:
            # Getroffen! Punkt!
            punkte = punkte + 1
            ball_y = 0
            ball_x = random.randint(30, 370)
            # Spiel wird schneller
            ball_speed = ball_speed + 0.5

    # Ball ist unten raus? Neuer Ball!
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(30, 370)
        punkte = 0  # Punkte zurücksetzen
        ball_speed = 5

def on_mouse_down(pos):
    global faenger_x
    # Fänger bewegt sich dahin wo du tippst
    faenger_x = pos[0] - faenger_breite / 2