# === SPIEL MIT BUTTONS ===
# Lerne wie man Bildschirm-Buttons erstellt
# Tippe auf die Buttons um die Box zu bewegen

WIDTH = 400
HEIGHT = 600

# Spieler Position
spieler_x = 180
spieler_y = 250

# Button Positionen
button_links = Rect(20, 480, 80, 60)
button_rechts = Rect(120, 480, 80, 60)
button_hoch = Rect(220, 480, 80, 60)
button_runter = Rect(300, 480, 80, 60)

# Geschwindigkeit
speed = 15

def draw():
    screen.fill("darkblue")

    # Spielbereich markieren
    screen.draw.rect(Rect(10, 10, WIDTH - 20, 450), "white")

    # Spieler zeichnen
    screen.draw.filled_rect(Rect(spieler_x, spieler_y, 40, 40), "red")

    # Buttons zeichnen
    screen.draw.filled_rect(button_links, "gray")
    screen.draw.filled_rect(button_rechts, "gray")
    screen.draw.filled_rect(button_hoch, "gray")
    screen.draw.filled_rect(button_runter, "gray")

    # Button Rahmen
    screen.draw.rect(button_links, "white")
    screen.draw.rect(button_rechts, "white")
    screen.draw.rect(button_hoch, "white")
    screen.draw.rect(button_runter, "white")

    # Button Beschriftungen
    screen.draw.text("←", (45, 495), color="white", fontsize=35)
    screen.draw.text("→", (145, 495), color="white", fontsize=35)
    screen.draw.text("↑", (248, 495), color="white", fontsize=35)
    screen.draw.text("↓", (328, 495), color="white", fontsize=35)

    # Anleitung
    screen.draw.text("Tippe die Buttons!", (100, 560), color="yellow", fontsize=25)

def on_mouse_down(pos):
    global spieler_x, spieler_y

    # Welcher Button wurde gedrückt?
    if button_links.collidepoint(pos):
        spieler_x = spieler_x - speed

    if button_rechts.collidepoint(pos):
        spieler_x = spieler_x + speed

    if button_hoch.collidepoint(pos):
        spieler_y = spieler_y - speed

    if button_runter.collidepoint(pos):
        spieler_y = spieler_y + speed

    # Nicht aus dem Spielbereich gehen
    if spieler_x < 15:
        spieler_x = 15
    if spieler_x > WIDTH - 55:
        spieler_x = WIDTH - 55
    if spieler_y < 15:
        spieler_y = 15
    if spieler_y > 410:
        spieler_y = 410