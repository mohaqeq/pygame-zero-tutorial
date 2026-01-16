# === FLAPPY BIRD MIT BILDERN ===
# Flappy Bird mit echten Bildern!
#
# WICHTIG: Du brauchst diese Bilder im Ordner "images/":
# - vogel.png (ca. 40x30 Pixel)
# - roehre_oben.png (Röhre nach unten)
# - roehre_unten.png (Röhre nach oben)
#
# Falls du keine Bilder hast, benutze das einfache Flappy Box Spiel!

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