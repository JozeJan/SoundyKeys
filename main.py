import keyboard
import pygame
from playsound import playsound
keyboardpressnum = 1
while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(event.name) # to check key name
        pygame.mixer.init()
        pygame.mixer.music.load(f"Audio/{keyboardpressnum}.wav")
        pygame.mixer.music.play()
        keyboardpressnum += 1
        if keyboardpressnum > 15:
            keyboardpressnum = 1