import keyboard
import pygame
keyboardpressnum = 1
pygame.mixer.init()
am_channel = pygame.mixer.Channel(1)
menu = "am"
event = keyboard.read_event()
while menu == "am":
    if event.event_type == keyboard.KEY_DOWN:
        am_am_ams = pygame.mixer.Sound(f"Audio/{keyboardpressnum}.wav")
        print(event.name)
        am_channel.play(am_am_ams)
        keyboardpressnum += 1
        if keyboardpressnum > 15: #How many times to am am am
            keyboardpressnum = 1
        if keyboard.is_pressed('f2'):  # if key 'q' is pressed
            print('You Pressed A Key!')
            menu = "štefan"
while menu == "štefan":








