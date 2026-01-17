# === SPACE SHOOTER ===
# Schiesse auf Aliens!
#
# WICHTIG: Du brauchst diese Bilder im Ordner "images/":
# - rakete.png (dein Raumschiff)
# - alien.png (die Aliens)
# - schuss.png (der Laserstrahl)

import pygame
import pgzrun
from pgzero.builtins import Actor
from pygame import Rect
import random

WIDTH = 400
HEIGHT = 600

# Raumschiff
rakete = Actor("rakete")
rakete.x = WIDTH // 2
rakete.midbottom = (WIDTH // 2, HEIGHT - 20)

# Schuesse
schuesse = []

# Aliens
aliens = []
alien_timer = 0

# Spielstand
punkte = 0
leben = 3

def erstelle_alien():
    alien = Actor("alien")
    alien.x = random.randint(50, WIDTH - 50)
    alien.y = -30
    alien.speed = random.uniform(2, 5)  # Zufaellige Geschwindigkeit
    aliens.append(alien)

def draw():
    # Weltraum-Hintergrund
    screen.fill("black")

    # Sterne
    random.seed(42)  # Immer gleiche Sterne
    for i in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        screen.draw.filled_circle((x, y), 1, "white")

    # Schuesse zeichnen
    for schuss in schuesse:
        schuss.draw()

    # Aliens zeichnen
    for alien in aliens:
        alien.draw()

    # Rakete zeichnen
    rakete.draw()

    # Info
    screen.draw.text(f"Punkte: {punkte}", (10, 10), color="white", fontsize=30)
    screen.draw.text(f"Leben: {leben}", (10, 50), color="red", fontsize=30)

    # Schiess-Button
    screen.draw.filled_rect(Rect(WIDTH // 2 - 50, HEIGHT - 80, 100, 50), "red")
    screen.draw.text("FEUER!", (WIDTH // 2 - 35, HEIGHT - 70), color="white", fontsize=25)

    if leben <= 0:
        screen.draw.text("GAME OVER", (WIDTH // 4, HEIGHT // 2 - 20), color="red", fontsize=45)

def update():
    global alien_timer, punkte, leben

    if leben <= 0:
        return

    # Neue Aliens erstellen
    alien_timer = alien_timer + 1
    if alien_timer > 60:  # Alle 60 Frames
        erstelle_alien()
        alien_timer = 0

    # Schuesse bewegen
    for schuss in schuesse[:]:
        schuss.y = schuss.y - 10

        # Schuss aus dem Bildschirm?
        if schuss.y < -20:
            schuesse.remove(schuss)

    # Aliens bewegen
    for alien in aliens[:]:
        alien.y = alien.y + alien.speed

        # Alien unten angekommen?
        if alien.y > HEIGHT + 30:
            aliens.remove(alien)
            leben = leben - 1
            sounds.autsch.play()

    # Treffer pruefen
    for schuss in schuesse[:]:
        for alien in aliens[:]:
            if schuss.colliderect(alien):
                if schuss in schuesse:
                    schuesse.remove(schuss)
                aliens.remove(alien)
                punkte = punkte + 10
                sounds.explosion.play()
                break

def on_mouse_down(pos):
    global rakete

    if leben <= 0:
        return

    # Rakete bewegen (obere Haelfte des Bildschirms)
    if pos[1] < HEIGHT - 100:
        rakete.x = pos[0]

    # Schiess-Button gedrueckt?
    feuer_button = Rect(WIDTH // 2 - 50, HEIGHT - 80, 100, 50)
    if feuer_button.collidepoint(pos):
        schuss = Actor("schuss")
        schuss.midbottom = rakete.midtop
        schuesse.append(schuss)
        sounds.schuss.play()

def on_mouse_move(pos):
    if leben > 0 and pos[1] < HEIGHT - 100:
        rakete.x = pos[0]

# Diese Zeile startet das Spiel!
pgzrun.go()
