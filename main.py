import keyboard
import pygame
import random
keyboardpressnum = 1
pygame.mixer.init()
am_channel = pygame.mixer.Channel(1)
menu = "am"


while menu == "am":
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        am_am_ams = pygame.mixer.Sound(f"Am/{keyboardpressnum}.wav")
        print(event.name)
        am_channel.play(am_am_ams)
        keyboardpressnum += 1
        if keyboardpressnum > 15: #How many times to am am am
            keyboardpressnum = 1
        if keyboard.is_pressed('f2'):  # if key 'q' is pressed
            print('Swiching to Štefan')
            menu = "štefan"
while menu == "štefan":
    event = keyboard.read_event()
    if keyboard.is_pressed('a'):
        a = pygame.mixer.Sound(f"Stiven/Ajde grem.mp3")
        am_channel.play(a)
    if keyboard.is_pressed('č'):
        gamble = ["č1", "č2"]
        print(random.choice(gamble))
        gambleval = (random.choice(gamble))
        č1 = pygame.mixer.Sound("Stiven/Čakal ne bom.mp3")
        č2 = pygame.mixer.Sound("Stiven/Če boš še kej tazga izjavu2.mp3")
        am_channel.play(gambleval)

# ačaača



    # if keyboard.is_pressed('a'):
    #     a = pygame.mixer.Sound(f"Stiven/Ajde grem.mp3")
    #     am_channel.play(a)






