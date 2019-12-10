#!/usr/bin/env python
"""
Aufgabe 5: Schere/Stein/Papier
"""

# time und random importieren
import time
import random

# Einleitung
print("*******************")
time.sleep(1.0)
print("SCHERE-STEIN-PAPIER")
time.sleep(1.0)
print("*******************")
time.sleep(1.0)
print("Diesmal geht es gegen den Computer!")
time.sleep(1.0)

# Definition zweier Variablen um Spielstand einzutragen
PLAY_SCORE = 0
COMP_SCORE = 0
# Array für zufällige Auswahl des Computers
GAME = ["Schere", "Stein", "Papier"]
# Festlegung einer while-Schleife die unendlich ist
while True:
    # Eingabeabfrage für Spieler und Computer
    PLAY = input("Wähle zwischen Schere, Stein und Papier: ")
    COMP = random.choice(GAME)
   # Sieger ermitteln
    try:
        if PLAY in GAME and COMP in GAME:
            if PLAY == COMP:
                print("Computer wählte ebenfalls " + COMP + "!")
                print("Unentschieden!")
            else:
                if PLAY == "Schere":
                    print("Computer wählte " + COMP + "!")
                    if COMP == "Stein":
                        print("Computer gewinnt!")
                        # Zählen des Spielstands (Computer)
                        COMP_SCORE += 1
                    else:
                        print("Spieler gewinnt!")
                        #Zählen des Spielstands (Spieler)
                        PLAY_SCORE += 1
                if PLAY == "Stein":
                    print("Computer wählte " + COMP + "!")
                    if COMP == "Papier":
                        print("Computer gewinnt!")
                        COMP_SCORE += 1
                    else:
                        print("Spieler gewinnt!")
                        PLAY_SCORE += 1
                if PLAY == "Papier":
                    print("Computer wählte " + COMP + "!")
                    if COMP == "Schere":
                        print("Computer gewinnt!")
                        COMP_SCORE += 1
                    else:
                        print("Spieler gewinnt!")
                        PLAY_SCORE += + 1
        else:
            # Aufrufen der Exception
            raise TypeError
    # Definiton der Excpetion TypError zum Abfangen von falschen Eingabe
    except TypeError:
        print("Falsche Eingabe, versuchen Sie es erneut!")
    # Festlegen ob Spiel weiter geht oder abgebrochen wird
    if PLAY_SCORE >= 3:
        # Mechanismus innerhalb der while-Schleife um diese zu beenden
        break
    elif COMP_SCORE >= 3:
        break

# Ausgabe des Endstands und des Gewinners
print("")
print("*******************")
time.sleep(1.0)
print("DANKE FÜRS SPIELEN!")
time.sleep(1.0)
print("*******************")
time.sleep(1.0)
print("")
print("ENDSTAND:")
print("---------")
time.sleep(1.6)
print("Computer:" + str(COMP_SCORE))
time.sleep(1.6)
print("Spieler:" + str(PLAY_SCORE))
time.sleep(1.6)

if COMP_SCORE > PLAY_SCORE:
    print("Diesmal hat der Computer gewonnen.")
else:
    print("Gratulation, sie haben gewonnen!")
