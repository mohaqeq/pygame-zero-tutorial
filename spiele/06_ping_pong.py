# === PING PONG ===
# Klassisches Ping Pong! Du spielst gegen den Computer.
# Tippe oder ziehe um deinen Schlaeger zu bewegen.

import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Der Ball
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_groesse = 15
ball_speed_x = 5
ball_speed_y = 5

# Spieler Schlaeger (unten)
spieler_x = WIDTH // 2 - 50
spieler_y = HEIGHT - 50
schlaeger_breite = 100
schlaeger_hoehe = 15

# Computer Schlaeger (oben)
computer_x = WIDTH // 2 - 50
computer_y = 30
computer_speed = 4

# Punkte
spieler_punkte = 0
computer_punkte = 0

def draw():
    screen.fill("black")

    # Mittellinie
    screen.draw.line((0, HEIGHT // 2), (WIDTH, HEIGHT // 2), "gray")

    # Ball zeichnen
    screen.draw.filled_rect(
        Rect(ball_x, ball_y, ball_groesse, ball_groesse),
        "white"
    )

    # Spieler Schlaeger (gruen)
    screen.draw.filled_rect(
        Rect(spieler_x, spieler_y, schlaeger_breite, schlaeger_hoehe),
        "green"
    )

    # Computer Schlaeger (rot)
    screen.draw.filled_rect(
        Rect(computer_x, computer_y, schlaeger_breite, schlaeger_hoehe),
        "red"
    )

    # Punkte anzeigen
    screen.draw.text(f"Computer: {computer_punkte}", (10, HEIGHT // 2 - 40),
                     color="red", fontsize=25)
    screen.draw.text(f"Du: {spieler_punkte}", (10, HEIGHT // 2 + 10),
                     color="green", fontsize=25)

def update():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    global computer_x, spieler_punkte, computer_punkte

    # Ball bewegen
    ball_x = ball_x + ball_speed_x
    ball_y = ball_y + ball_speed_y

    # Ball prallt von Seiten ab
    if ball_x <= 0 or ball_x + ball_groesse >= WIDTH:
        ball_speed_x = -ball_speed_x

    # Ball trifft Spieler Schlaeger
    if ball_y + ball_groesse >= spieler_y:
        if ball_x + ball_groesse >= spieler_x and ball_x <= spieler_x + schlaeger_breite:
            ball_speed_y = -abs(ball_speed_y)  # Nach oben

    # Ball trifft Computer Schlaeger
    if ball_y <= computer_y + schlaeger_hoehe:
        if ball_x + ball_groesse >= computer_x and ball_x <= computer_x + schlaeger_breite:
            ball_speed_y = abs(ball_speed_y)  # Nach unten

    # Punkt fuer Spieler (Ball oben raus)
    if ball_y < 0:
        spieler_punkte = spieler_punkte + 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Punkt fuer Computer (Ball unten raus)
    if ball_y > HEIGHT:
        computer_punkte = computer_punkte + 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Computer KI - folgt dem Ball
    ball_mitte = ball_x + ball_groesse // 2
    computer_mitte = computer_x + schlaeger_breite // 2

    if ball_mitte < computer_mitte - 10:
        computer_x = computer_x - computer_speed
    elif ball_mitte > computer_mitte + 10:
        computer_x = computer_x + computer_speed

def on_mouse_down(pos):
    global spieler_x
    # Spieler Schlaeger folgt dem Finger
    spieler_x = pos[0] - schlaeger_breite // 2

    # Nicht aus dem Bildschirm gehen
    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - schlaeger_breite:
        spieler_x = WIDTH - schlaeger_breite

# Diese Funktion wird aufgerufen wenn der Finger sich bewegt
def on_mouse_move(pos):
    global spieler_x
    spieler_x = pos[0] - schlaeger_breite // 2

    if spieler_x < 0:
        spieler_x = 0
    if spieler_x > WIDTH - schlaeger_breite:
        spieler_x = WIDTH - schlaeger_breite

# Diese Zeile startet das Spiel!
pgzrun.go()
