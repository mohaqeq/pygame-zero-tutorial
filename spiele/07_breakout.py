# === BREAKOUT ===
# Zerstöre alle Steine mit dem Ball!
# Tippe oder ziehe um den Schläger zu bewegen.

WIDTH = 400
HEIGHT = 600

# Ball
ball_x = 200
ball_y = 400
ball_groesse = 12
ball_speed_x = 4
ball_speed_y = -4

# Schläger
schlaeger_x = 150
schlaeger_y = 550
schlaeger_breite = 80
schlaeger_hoehe = 12

# Steine - eine Liste mit allen Steinen
steine = []
stein_breite = 45
stein_hoehe = 20
stein_abstand = 5

# Punkte und Leben
punkte = 0
leben = 3

def erstelle_steine():
    # Diese Funktion erstellt alle Steine
    global steine
    steine = []
    farben = ["red", "orange", "yellow", "green", "blue"]

    for reihe in range(5):
        for spalte in range(8):
            x = spalte * (stein_breite + stein_abstand) + 10
            y = reihe * (stein_hoehe + stein_abstand) + 60
            farbe = farben[reihe]
            steine.append({"x": x, "y": y, "farbe": farbe})

# Am Anfang Steine erstellen
erstelle_steine()

def draw():
    screen.fill("black")

    # Alle Steine zeichnen
    for stein in steine:
        screen.draw.filled_rect(
            Rect(stein["x"], stein["y"], stein_breite, stein_hoehe),
            stein["farbe"]
        )

    # Ball zeichnen
    screen.draw.filled_circle((ball_x, ball_y), ball_groesse, "white")

    # Schläger zeichnen
    screen.draw.filled_rect(
        Rect(schlaeger_x, schlaeger_y, schlaeger_breite, schlaeger_hoehe),
        "cyan"
    )

    # Punkte und Leben anzeigen
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=25)
    screen.draw.text(f"Leben: {leben}", (300, 10), color="white", fontsize=25)

    # Gewonnen?
    if len(steine) == 0:
        screen.draw.text("DU HAST GEWONNEN!", (50, 300), color="green", fontsize=35)

    # Verloren?
    if leben <= 0:
        screen.draw.text("GAME OVER", (100, 300), color="red", fontsize=45)

def update():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, punkte, leben

    if leben <= 0 or len(steine) == 0:
        return

    # Ball bewegen
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # Ball prallt von Wänden ab
    if ball_x - ball_groesse <= 0 or ball_x + ball_groesse >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Ball prallt von Decke ab
    if ball_y - ball_groesse <= 0:
        ball_speed_y = -ball_speed_y

    # Ball fällt runter - Leben verlieren
    if ball_y > HEIGHT:
        leben = leben - 1
        ball_x = 200
        ball_y = 400
        ball_speed_y = -4

    # Ball trifft Schläger
    if ball_y + ball_groesse >= schlaeger_y:
        if ball_x >= schlaeger_x and ball_x <= schlaeger_x + schlaeger_breite:
            ball_speed_y = -abs(ball_speed_y)

    # Ball trifft Steine
    for stein in steine[:]:  # [:] macht eine Kopie der Liste
        if (ball_x + ball_groesse > stein["x"] and
            ball_x - ball_groesse < stein["x"] + stein_breite and
            ball_y + ball_groesse > stein["y"] and
            ball_y - ball_groesse < stein["y"] + stein_hoehe):
            # Stein getroffen!
            steine.remove(stein)
            ball_speed_y = -ball_speed_y
            punkte = punkte + 10
            break

def on_mouse_down(pos):
    global schlaeger_x
    schlaeger_x = pos[0] - schlaeger_breite / 2

    if schlaeger_x < 0:
        schlaeger_x = 0
    if schlaeger_x > WIDTH - schlaeger_breite:
        schlaeger_x = WIDTH - schlaeger_breite

def on_mouse_move(pos):
    global schlaeger_x
    schlaeger_x = pos[0] - schlaeger_breite / 2

    if schlaeger_x < 0:
        schlaeger_x = 0
    if schlaeger_x > WIDTH - schlaeger_breite:
        schlaeger_x = WIDTH - schlaeger_breite