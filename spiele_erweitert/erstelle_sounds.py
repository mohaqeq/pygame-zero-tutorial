# === SOUNDS ERSTELLEN ===
# Führe dieses Skript aus um einfache Platzhalter-Sounds zu erstellen

import numpy as np
import wave
import struct
import os

def erstelle_sound(dateiname, frequenz, dauer, lautstaerke=0.5, fade_out=True):
    """Erstellt einen einfachen Ton als WAV-Datei"""
    sample_rate = 44100
    samples = int(sample_rate * dauer)

    # Sinuswelle generieren
    t = np.linspace(0, dauer, samples, False)
    ton = np.sin(2 * np.pi * frequenz * t) * lautstaerke

    # Fade out für natürlicheren Klang
    if fade_out:
        fade = np.linspace(1, 0, samples)
        ton = ton * fade

    # Auf 16-bit skalieren
    audio = (ton * 32767).astype(np.int16)

    # WAV-Datei schreiben
    with wave.open(f"sounds/{dateiname}.wav", 'w') as wav:
        wav.setnchannels(1)  # Mono
        wav.setsampwidth(2)  # 16-bit
        wav.setframerate(sample_rate)
        wav.writeframes(audio.tobytes())

    print(f"Erstellt: sounds/{dateiname}.wav")

def erstelle_aufsteigend(dateiname, start_freq, end_freq, dauer):
    """Erstellt einen aufsteigenden Ton"""
    sample_rate = 44100
    samples = int(sample_rate * dauer)

    t = np.linspace(0, dauer, samples, False)
    # Frequenz steigt linear
    freq = np.linspace(start_freq, end_freq, samples)
    phase = np.cumsum(2 * np.pi * freq / sample_rate)
    ton = np.sin(phase) * 0.5

    # Fade out
    fade = np.linspace(1, 0, samples)
    ton = ton * fade

    audio = (ton * 32767).astype(np.int16)

    with wave.open(f"sounds/{dateiname}.wav", 'w') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(audio.tobytes())

    print(f"Erstellt: sounds/{dateiname}.wav")

def erstelle_absteigend(dateiname, start_freq, end_freq, dauer):
    """Erstellt einen absteigenden Ton"""
    sample_rate = 44100
    samples = int(sample_rate * dauer)

    t = np.linspace(0, dauer, samples, False)
    freq = np.linspace(start_freq, end_freq, samples)
    phase = np.cumsum(2 * np.pi * freq / sample_rate)
    ton = np.sin(phase) * 0.5

    fade = np.linspace(1, 0, samples)
    ton = ton * fade

    audio = (ton * 32767).astype(np.int16)

    with wave.open(f"sounds/{dateiname}.wav", 'w') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        wav.writeframes(audio.tobytes())

    print(f"Erstellt: sounds/{dateiname}.wav")

def erstelle_alle_sounds():
    """Erstellt alle benötigten Sounds"""
    os.makedirs("sounds", exist_ok=True)

    print("Erstelle Sounds...")
    print()

    # === FLAPPY BIRD ===
    print("--- Flappy Bird ---")
    erstelle_aufsteigend("flap", 300, 600, 0.1)  # Flügelschlag
    erstelle_aufsteigend("punkt", 500, 1000, 0.15)  # Punkt gesammelt
    erstelle_absteigend("game_over", 400, 100, 0.5)  # Game Over

    # === MÜNZEN SAMMELN ===
    print()
    print("--- Münzen Sammeln ---")
    erstelle_aufsteigend("muenze", 800, 1200, 0.1)  # Münze gesammelt
    erstelle_absteigend("autsch", 300, 100, 0.2)  # Schaden

    # === SPACE SHOOTER ===
    print()
    print("--- Space Shooter ---")
    erstelle_sound("schuss", 1000, 0.1, 0.3)  # Laser
    erstelle_absteigend("explosion", 200, 50, 0.3)  # Explosion

    # === PING PONG ===
    print()
    print("--- Ping Pong ---")
    erstelle_sound("treffer", 600, 0.05, 0.4)  # Ball trifft Schläger

    # === ALLGEMEIN ===
    print()
    print("--- Allgemein ---")
    erstelle_aufsteigend("sprung", 200, 500, 0.15)  # Sprung-Sound

    print()
    print("=" * 40)
    print("Alle Sounds wurden erstellt!")
    print("=" * 40)

if __name__ == "__main__":
    erstelle_alle_sounds()
