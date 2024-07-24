import random

import keyboard
import pygame
keyboardpressnum = 1
pygame.mixer.init()
am_channel = pygame.mixer.Channel(1)
am_am_ams = [pygame.mixer.Sound(f"Audio/{i}.wav") for i in range(1, 20)]
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        am_channel.play(am_am_ams[random.randint(0, 18)])
