# === SPIEL MIT BUTTONS ===
# Lerne wie man Bildschirm-Buttons erstellt
# Tippe auf die Buttons um die Box zu bewegen

import pygame
import pgzrun
from pygame import Rect

WIDTH = 400
HEIGHT = 600

# Spieler Position
spieler_x = WIDTH // 2 - 20
spieler_y = HEIGHT // 2 - 70

# Button Bereich (unten)
button_bereich_y = HEIGHT - 120
button_breite = 80
button_hoehe = 60
button_abstand = 10

# Button Positionen - gleichmaessig verteilt
button_links = Rect(button_abstand, button_bereich_y, button_breite, button_hoehe)
button_rechts = Rect(button_abstand + button_breite + button_abstand, button_bereich_y, button_breite, button_hoehe)
button_hoch = Rect(WIDTH - 2 * button_breite - 2 * button_abstand, button_bereich_y, button_breite, button_hoehe)
button_runter = Rect(WIDTH - button_breite - button_abstand, button_bereich_y, button_breite, button_hoehe)

# Geschwindigkeit
speed = 15

# Spielbereich
spielbereich_rand = 10
spielbereich_hoehe = HEIGHT - 150

def draw():
    screen.fill("darkblue")

    # Spielbereich markieren
    screen.draw.rect(Rect(spielbereich_rand, spielbereich_rand, WIDTH - 2 * spielbereich_rand, spielbereich_hoehe), "white")

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

    # Button Beschriftungen - zentriert in jedem Button
    screen.draw.text("<", (button_links.x + button_breite // 2 - 8, button_links.y + button_hoehe // 2 - 15), color="white", fontsize=35)
    screen.draw.text(">", (button_rechts.x + button_breite // 2 - 8, button_rechts.y + button_hoehe // 2 - 15), color="white", fontsize=35)
    screen.draw.text("^", (button_hoch.x + button_breite // 2 - 8, button_hoch.y + button_hoehe // 2 - 15), color="white", fontsize=35)
    screen.draw.text("v", (button_runter.x + button_breite // 2 - 8, button_runter.y + button_hoehe // 2 - 15), color="white", fontsize=35)

    # Anleitung
    screen.draw.text("Tippe die Buttons!", (WIDTH // 4, HEIGHT - 40), color="yellow", fontsize=25)

def on_mouse_down(pos):
    global spieler_x, spieler_y

    # Welcher Button wurde gedrueckt?
    if button_links.collidepoint(pos):
        spieler_x = spieler_x - speed

    if button_rechts.collidepoint(pos):
        spieler_x = spieler_x + speed

    if button_hoch.collidepoint(pos):
        spieler_y = spieler_y - speed

    if button_runter.collidepoint(pos):
        spieler_y = spieler_y + speed

    # Nicht aus dem Spielbereich gehen
    if spieler_x < spielbereich_rand + 5:
        spieler_x = spielbereich_rand + 5
    if spieler_x > WIDTH - spielbereich_rand - 45:
        spieler_x = WIDTH - spielbereich_rand - 45
    if spieler_y < spielbereich_rand + 5:
        spieler_y = spielbereich_rand + 5
    if spieler_y > spielbereich_hoehe - 35:
        spieler_y = spielbereich_hoehe - 35

# Diese Zeile startet das Spiel!
pgzrun.go()
