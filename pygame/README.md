# Rocket Avoid – Pygame

**High School Computing Science** · Python · Pygame · Sep 2022 – Jan 2023

A 2D arcade game: fly a jet and dodge incoming missiles.

## Features
- Arrow keys move the jet, which stays within the screen
- Missiles and clouds spawn at random heights and speeds
- Collision detection triggers an explosion animation and sound
- Background music, and sound effects for moving up and down
- Press `SPACE` to play again or `ESC` to exit after a crash

## Built with
Object-oriented design using Pygame sprites: `Player`, `Enemy`, `Cloud`, `Explosion`, and a `Game` class that runs the main loop at 30 FPS.

## Run it
Requires Python 3 and Pygame. Run it from inside this folder so the image and audio paths resolve:
```
pip install pygame
python rocket_avoid.py
```
