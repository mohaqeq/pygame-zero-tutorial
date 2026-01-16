# === VERBESSERTES PING PONG ===
# Ping Pong mit Bildern und Partikel-Effekten!
#
# WICHTIG: Du brauchst diese Bilder im Ordner "images/":
# - schlaeger_gruen.png (dein Schläger)
# - schlaeger_rot.png (Computer-Schläger)
# - ball.png (der Ball)
#
# Und diese Sounds im Ordner "sounds/":
# - treffer.wav (wenn Ball Schläger trifft)
# - punkt.wav (wenn jemand punktet)

WIDTH = 400
HEIGHT = 600

# Ball
ball = Actor("ball")
ball.x = 200
ball.y = 300
ball_speed_x = 5
ball_speed_y = 5

# Spieler Schläger
spieler = Actor("schlaeger_gruen")
spieler.midbottom = (200, HEIGHT - 20)

# Computer Schläger
computer = Actor("schlaeger_rot")
computer.midtop = (200, 20)
computer_speed = 4

# Punkte
spieler_punkte = 0
computer_punkte = 0

# Partikel für Effekte
partikel = []

def draw():
    screen.fill("black")

    # Spielfeld
    screen.draw.line((0, HEIGHT/2), (WIDTH, HEIGHT/2), "gray")
    screen.draw.rect(Rect(5, 5, WIDTH-10, HEIGHT-10), "white")

    # Partikel zeichnen
    for p in partikel:
        screen.draw.filled_circle((int(p["x"]), int(p["y"])), int(p["size"]), p["farbe"])

    # Schläger und Ball
    computer.draw()
    spieler.draw()
    ball.draw()

    # Punkte
    screen.draw.text(f"{computer_punkte}", (WIDTH/2 - 50, HEIGHT/2 - 60),
                     color="red", fontsize=50)
    screen.draw.text(f"{spieler_punkte}", (WIDTH/2 - 50, HEIGHT/2 + 20),
                     color="green", fontsize=50)

def erstelle_partikel(x, y, farbe):
    import random
    for i in range(10):
        p = {
            "x": x,
            "y": y,
            "speed_x": random.uniform(-5, 5),
            "speed_y": random.uniform(-5, 5),
            "size": random.randint(3, 8),
            "farbe": farbe,
            "leben": 30
        }
        partikel.append(p)

def update():
    global ball_speed_x, ball_speed_y, spieler_punkte, computer_punkte

    # Ball bewegen
    ball.x = ball.x + ball_speed_x
    ball.y = ball.y + ball_speed_y

    # Partikel bewegen
    for p in partikel[:]:
        p["x"] = p["x"] + p["speed_x"]
        p["y"] = p["y"] + p["speed_y"]
        p["leben"] = p["leben"] - 1
        p["size"] = p["size"] * 0.95
        if p["leben"] <= 0:
            partikel.remove(p)

    # Ball prallt von Seiten ab
    if ball.x <= 20 or ball.x >= WIDTH - 20:
        ball_speed_x = -ball_speed_x
        erstelle_partikel(ball.x, ball.y, "white")

    # Ball trifft Spieler
    if ball.colliderect(spieler):
        ball_speed_y = -abs(ball_speed_y)
        erstelle_partikel(ball.x, ball.y, "green")
        # sounds.treffer.play()

    # Ball trifft Computer
    if ball.colliderect(computer):
        ball_speed_y = abs(ball_speed_y)
        erstelle_partikel(ball.x, ball.y, "red")
        # sounds.treffer.play()

    # Punkt für Spieler
    if ball.y < 0:
        spieler_punkte = spieler_punkte + 1
        ball.x = 200
        ball.y = 300
        # sounds.punkt.play()

    # Punkt für Computer
    if ball.y > HEIGHT:
        computer_punkte = computer_punkte + 1
        ball.x = 200
        ball.y = 300
        # sounds.punkt.play()

    # Computer KI
    if ball.x < computer.x - 10:
        computer.x = computer.x - computer_speed
    elif ball.x > computer.x + 10:
        computer.x = computer.x + computer_speed

def on_mouse_down(pos):
    spieler.x = pos[0]

def on_mouse_move(pos):
    spieler.x = pos[0]