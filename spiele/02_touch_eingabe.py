# === TOUCH EINGABE ===
# Lerne wie man Touch-Eingaben verarbeitet

WIDTH = 400
HEIGHT = 600

# Hier speichern wir wo getippt wurde
finger_x = 200
finger_y = 300
anzahl_tipps = 0

def draw():
    screen.fill("darkblue")

    # Zeichne einen Kreis wo der Finger ist
    screen.draw.filled_circle((finger_x, finger_y), 40, "red")

    # Zeige Anleitung
    screen.draw.text("Tippe irgendwo!", (100, 50), color="white", fontsize=30)

    # Zeige die Position
    screen.draw.text(f"X: {finger_x}", (20, 520), color="yellow", fontsize=25)
    screen.draw.text(f"Y: {finger_y}", (20, 550), color="yellow", fontsize=25)
    screen.draw.text(f"Tipps: {anzahl_tipps}", (250, 535), color="green", fontsize=25)

def on_mouse_down(pos):
    # pos ist eine Liste mit [x, y] Position
    global finger_x, finger_y, anzahl_tipps
    finger_x = pos[0]  # x-Position
    finger_y = pos[1]  # y-Position
    anzahl_tipps = anzahl_tipps + 1