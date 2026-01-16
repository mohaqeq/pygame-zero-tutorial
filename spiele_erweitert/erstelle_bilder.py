# === BILDER ERSTELLEN ===
# Führe dieses Skript aus um einfache Platzhalter-Bilder zu erstellen
# Du brauchst dafür PIL/Pillow: pip install Pillow

from PIL import Image, ImageDraw

def erstelle_bild(dateiname, breite, hoehe, farbe, form="rect", text=None):
    """Erstellt ein einfaches Bild"""
    # Transparenter Hintergrund
    bild = Image.new('RGBA', (breite, hoehe), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)

    if form == "rect":
        zeichner.rectangle([2, 2, breite-3, hoehe-3], fill=farbe, outline="black")
    elif form == "circle":
        zeichner.ellipse([2, 2, breite-3, hoehe-3], fill=farbe, outline="black")
    elif form == "triangle":
        # Dreieck nach oben
        punkte = [(breite//2, 2), (2, hoehe-3), (breite-3, hoehe-3)]
        zeichner.polygon(punkte, fill=farbe, outline="black")

    bild.save(f"images/{dateiname}.png")
    print(f"Erstellt: images/{dateiname}.png")

def erstelle_roehre(dateiname, breite, hoehe, farbe, oben=True):
    """Erstellt eine Röhre für Flappy Bird"""
    bild = Image.new('RGBA', (breite, hoehe), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)

    # Hauptkörper
    zeichner.rectangle([5, 0, breite-6, hoehe], fill=farbe, outline="darkgreen")

    # Kappe (oben oder unten)
    if oben:
        # Kappe unten
        zeichner.rectangle([0, hoehe-25, breite-1, hoehe-1], fill=farbe, outline="darkgreen")
    else:
        # Kappe oben
        zeichner.rectangle([0, 0, breite-1, 25], fill=farbe, outline="darkgreen")

    bild.save(f"images/{dateiname}.png")
    print(f"Erstellt: images/{dateiname}.png")

def erstelle_alle_bilder():
    """Erstellt alle benötigten Bilder"""
    import os
    os.makedirs("images", exist_ok=True)

    print("Erstelle Bilder...")
    print()

    # === FLAPPY BIRD ===
    print("--- Flappy Bird ---")
    # Vogel (gelb, oval)
    bild = Image.new('RGBA', (40, 30), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.ellipse([2, 2, 37, 27], fill="yellow", outline="orange")
    # Auge
    zeichner.ellipse([25, 8, 32, 15], fill="white", outline="black")
    zeichner.ellipse([28, 10, 31, 13], fill="black")
    # Schnabel
    zeichner.polygon([(35, 15), (40, 18), (35, 21)], fill="orange")
    bild.save("images/vogel.png")
    print("Erstellt: images/vogel.png")

    # Röhren
    erstelle_roehre("roehre_oben", 60, 300, "green", oben=True)
    erstelle_roehre("roehre_unten", 60, 300, "green", oben=False)

    # === MÜNZEN SAMMELN ===
    print()
    print("--- Münzen Sammeln ---")
    # Spieler (blaues Quadrat mit Gesicht)
    bild = Image.new('RGBA', (40, 40), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.rectangle([2, 2, 37, 37], fill="dodgerblue", outline="blue")
    # Augen
    zeichner.ellipse([10, 12, 16, 18], fill="white")
    zeichner.ellipse([24, 12, 30, 18], fill="white")
    # Mund
    zeichner.arc([12, 20, 28, 32], 0, 180, fill="white", width=2)
    bild.save("images/spieler.png")
    print("Erstellt: images/spieler.png")

    # Münze (gelber Kreis)
    bild = Image.new('RGBA', (30, 30), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.ellipse([2, 2, 27, 27], fill="gold", outline="orange")
    zeichner.ellipse([8, 8, 21, 21], fill="yellow")
    bild.save("images/muenze.png")
    print("Erstellt: images/muenze.png")

    # Feind (rotes Monster)
    bild = Image.new('RGBA', (40, 40), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.rectangle([2, 10, 37, 37], fill="red", outline="darkred")
    # Zacken oben
    zeichner.polygon([(5, 10), (10, 2), (15, 10)], fill="red", outline="darkred")
    zeichner.polygon([(17, 10), (22, 2), (27, 10)], fill="red", outline="darkred")
    zeichner.polygon([(29, 10), (34, 2), (37, 10)], fill="red", outline="darkred")
    # Augen
    zeichner.ellipse([8, 15, 16, 23], fill="white")
    zeichner.ellipse([24, 15, 32, 23], fill="white")
    zeichner.ellipse([10, 17, 14, 21], fill="black")
    zeichner.ellipse([26, 17, 30, 21], fill="black")
    bild.save("images/feind.png")
    print("Erstellt: images/feind.png")

    # === SPACE SHOOTER ===
    print()
    print("--- Space Shooter ---")
    # Rakete (grün, dreieckig)
    bild = Image.new('RGBA', (40, 50), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    # Körper
    zeichner.polygon([(20, 2), (5, 45), (35, 45)], fill="limegreen", outline="green")
    # Fenster
    zeichner.ellipse([14, 15, 26, 27], fill="cyan", outline="blue")
    # Flamme
    zeichner.polygon([(12, 45), (20, 55), (28, 45)], fill="orange")
    bild.save("images/rakete.png")
    print("Erstellt: images/rakete.png")

    # Alien (lila)
    bild = Image.new('RGBA', (40, 35), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    # Kopf
    zeichner.ellipse([5, 5, 35, 30], fill="purple", outline="darkviolet")
    # Augen
    zeichner.ellipse([10, 12, 18, 22], fill="lime")
    zeichner.ellipse([22, 12, 30, 22], fill="lime")
    # Antennen
    zeichner.line([(12, 5), (8, 0)], fill="purple", width=2)
    zeichner.line([(28, 5), (32, 0)], fill="purple", width=2)
    bild.save("images/alien.png")
    print("Erstellt: images/alien.png")

    # Schuss (gelber Strahl)
    bild = Image.new('RGBA', (8, 20), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.rectangle([2, 0, 5, 19], fill="yellow", outline="orange")
    bild.save("images/schuss.png")
    print("Erstellt: images/schuss.png")

    # === PING PONG ERWEITERT ===
    print()
    print("--- Ping Pong ---")
    # Ball
    bild = Image.new('RGBA', (20, 20), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.ellipse([1, 1, 18, 18], fill="white", outline="gray")
    bild.save("images/ball.png")
    print("Erstellt: images/ball.png")

    # Schläger grün
    bild = Image.new('RGBA', (100, 20), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.rectangle([2, 2, 97, 17], fill="limegreen", outline="green")
    bild.save("images/schlaeger_gruen.png")
    print("Erstellt: images/schlaeger_gruen.png")

    # Schläger rot
    bild = Image.new('RGBA', (100, 20), (0, 0, 0, 0))
    zeichner = ImageDraw.Draw(bild)
    zeichner.rectangle([2, 2, 97, 17], fill="red", outline="darkred")
    bild.save("images/schlaeger_rot.png")
    print("Erstellt: images/schlaeger_rot.png")

    # === ANIMATION ===
    print()
    print("--- Animation ---")
    # Laufende Figur (4 Frames)
    for i in range(1, 5):
        bild = Image.new('RGBA', (40, 50), (0, 0, 0, 0))
        zeichner = ImageDraw.Draw(bild)

        # Kopf
        zeichner.ellipse([12, 2, 28, 18], fill="peachpuff", outline="tan")

        # Körper
        zeichner.rectangle([14, 18, 26, 35], fill="blue", outline="darkblue")

        # Beine (unterschiedlich je nach Frame)
        if i == 1:
            zeichner.line([(16, 35), (10, 48)], fill="blue", width=4)
            zeichner.line([(24, 35), (30, 48)], fill="blue", width=4)
        elif i == 2:
            zeichner.line([(16, 35), (14, 48)], fill="blue", width=4)
            zeichner.line([(24, 35), (26, 48)], fill="blue", width=4)
        elif i == 3:
            zeichner.line([(16, 35), (22, 48)], fill="blue", width=4)
            zeichner.line([(24, 35), (18, 48)], fill="blue", width=4)
        else:
            zeichner.line([(16, 35), (14, 48)], fill="blue", width=4)
            zeichner.line([(24, 35), (26, 48)], fill="blue", width=4)

        # Augen
        zeichner.ellipse([15, 7, 18, 10], fill="black")
        zeichner.ellipse([22, 7, 25, 10], fill="black")

        bild.save(f"images/laufen{i}.png")
        print(f"Erstellt: images/laufen{i}.png")

    print()
    print("=" * 40)
    print("Alle Bilder wurden erstellt!")
    print("=" * 40)

if __name__ == "__main__":
    erstelle_alle_bilder()
