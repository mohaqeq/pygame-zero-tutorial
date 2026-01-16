# === ANIMATION BEISPIEL ===
# Lerne wie man Animationen erstellt!
#
# WICHTIG: Du brauchst diese Bilder im Ordner "images/":
# - laufen1.png
# - laufen2.png
# - laufen3.png
# - laufen4.png
#
# Alle Bilder sollten gleich groß sein (z.B. 40x40 Pixel)

import pgzrun
from pgzero.builtins import Actor
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Spieler mit Animation
spieler = Actor("laufen1")
spieler.pos = (200, 300)

# Animation Variablen
animation_frame = 0
animation_timer = 0
animation_bilder = ["laufen1", "laufen2", "laufen3", "laufen4"]

# Bewegung
ist_am_laufen = False
ziel_x = 200
ziel_y = 300

def draw():
    screen.fill("lightblue")

    # Boden
    screen.draw.filled_rect(Rect(0, 450, WIDTH, 150), "green")

    # Spieler
    spieler.draw()

    # Anleitung
    screen.draw.text("Tippe irgendwo zum Laufen!", (70, 30), color="black", fontsize=25)

    # Position anzeigen
    screen.draw.text(f"Frame: {animation_frame + 1}", (10, 550), color="white", fontsize=20)

def update():
    global animation_timer, animation_frame, ist_am_laufen

    # Zur Zielposition bewegen
    if ist_am_laufen:
        # Richtung berechnen
        diff_x = ziel_x - spieler.x
        diff_y = ziel_y - spieler.y

        # Geschwindigkeit
        speed = 4

        # Bewegen
        if abs(diff_x) > speed:
            if diff_x > 0:
                spieler.x = spieler.x + speed
            else:
                spieler.x = spieler.x - speed
        else:
            spieler.x = ziel_x

        if abs(diff_y) > speed:
            if diff_y > 0:
                spieler.y = spieler.y + speed
            else:
                spieler.y = spieler.y - speed
        else:
            spieler.y = ziel_y

        # Angekommen?
        if spieler.x == ziel_x and spieler.y == ziel_y:
            ist_am_laufen = False
            animation_frame = 0
            spieler.image = animation_bilder[0]

    # Animation nur abspielen wenn am Laufen
    if ist_am_laufen:
        animation_timer = animation_timer + 1

        if animation_timer >= 8:  # Alle 8 Frames wechseln
            animation_timer = 0
            animation_frame = animation_frame + 1

            if animation_frame >= len(animation_bilder):
                animation_frame = 0

            # Bild wechseln
            spieler.image = animation_bilder[animation_frame]

def on_mouse_down(pos):
    global ziel_x, ziel_y, ist_am_laufen

    # Neues Ziel setzen
    ziel_x = pos[0]
    ziel_y = pos[1]
    ist_am_laufen = True

# Diese Zeile startet das Spiel!
pgzrun.go()
