import keyboard
import pygame
import random
import os
keyboardpressnum = 1
pygame.mixer.init()
am_channel = pygame.mixer.Channel(1)
menu = "am"

login = pygame.mixer.Sound(f"login.ogg")
am_channel.play(login)

while menu == "am":
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        am_am_ams = pygame.mixer.Sound(f"Am/{keyboardpressnum}.wav")
        print(event.name)
        am_channel.play(am_am_ams)
        keyboardpressnum += 1
        if keyboardpressnum > 15: #How many times to am am am
            keyboardpressnum = 1
        if keyboard.is_pressed('right shift'):  # if key 'q' is pressed
            map = pygame.mixer.Sound(f"map.ogg")
            am_channel.play(map)
            print('Swiching to Štefan')
            menu = "štefan"

while menu == "štefan":
    event = keyboard.read_event()
    if keyboard.is_pressed('a'):
        a = pygame.mixer.Sound(f"Stiven/Ajde grem.mp3")
        am_channel.play(a)
    if keyboard.is_pressed('č'):
        a1 = pygame.mixer.Sound("Stiven/Čakal ne bom.mp3")
        a2 = pygame.mixer.Sound("Stiven/Če boš še kej tazga izjavu2.mp3")
        gamble = [a1, a2]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('d'):
        a1 = pygame.mixer.Sound("Stiven/Dan dober.mp3")
        a2 = pygame.mixer.Sound("Stiven/Dohtar.mp3")
        a3 = pygame.mixer.Sound("Stiven/Dohtar Ueski!.mp3")
        gamble = [a1, a2, a3]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('h'):
        a1 = pygame.mixer.Sound("Stiven/HAHAHA.mp3")
        a2 = pygame.mixer.Sound("Stiven/Hvala.mp3")
        gamble = [a1, a2]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('j'):
        a1 = pygame.mixer.Sound("Stiven/Ja.mp3")
        a2 = pygame.mixer.Sound("Stiven/Jaz sem stiven.mp3")
        gamble = [a1, a2]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('k'):
        a1 = pygame.mixer.Sound("Stiven/Kaj se dogaja.mp3")
        a2 = pygame.mixer.Sound("Stiven/Kako smo.mp3")
        a3 = pygame.mixer.Sound("Stiven/Katero.mp3")
        a4 = pygame.mixer.Sound("Stiven/ker majčo!.mp3")
        gamble = [a1, a2, a3, a4]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('m'):
        a1 = pygame.mixer.Sound("Stiven/Mardžo Špinel.mp3")
        a2 = pygame.mixer.Sound("Stiven/Matija.mp3")
        a3 = pygame.mixer.Sound("Stiven/Mikrofon je poseksala črna lukna.mp3")
        a4 = pygame.mixer.Sound("Stiven/Moški.mp3")
        gamble = [a1, a2, a3, a4]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('n'):
        a1 = pygame.mixer.Sound("Stiven/Nazaj.mp3")
        a2 = pygame.mixer.Sound("Stiven/Ne.mp3")
        a3 = pygame.mixer.Sound("Stiven/Nehaj seksat.mp3")
        a4 = pygame.mixer.Sound("Stiven/Nevem.mp3")
        gamble = [a1, a2, a3, a4]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('o'):
        a1 = pygame.mixer.Sound("Stiven/odzaditi ti ga ovad.mp3")
        a2 = pygame.mixer.Sound("Stiven/O glej baba.mp3")
        a3 = pygame.mixer.Sound("Stiven/Oskar.mp3")
        gamble = [a1, a2, a3]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('p'):
        a1 = pygame.mixer.Sound("Stiven/papat.mp3")
        a2 = pygame.mixer.Sound("Stiven/poseksi črno lukno.mp3")
        a3 = pygame.mixer.Sound("Stiven/Posesal v črno lukno.mp3")
        a4 = pygame.mixer.Sound("Stiven/Prenehaj seksanje.mp3")
        gamble = [a1, a2, a3, a4]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('š'):
        a1 = pygame.mixer.Sound("Stiven/šalim.mp3")
        gamble = [a1]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('s'):
        a1 = pygame.mixer.Sound("Stiven/Sem.mp3")
        a2 = pygame.mixer.Sound("Stiven/Skrivna Formula je tako skrita.mp3")
        a3 = pygame.mixer.Sound("Stiven/Skrivna prepričuje okaz.mp3")
        a4 = pygame.mixer.Sound("Stiven/smrdljiv.mp3")
        a5 = pygame.mixer.Sound("Stiven/Super.mp3")
        gamble = [a1, a2, a3, a4]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('t'):
        a1 = pygame.mixer.Sound("Stiven/Tiho imam nekaj besed.mp3")
        a2 = pygame.mixer.Sound("Stiven/To je skrivna formula.mp3")
        a3 = pygame.mixer.Sound("Stiven/To pa ne povem.mp3")
        gamble = [a1, a2, a3]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('u'):
        a1 = pygame.mixer.Sound("Stiven/Useki eno muziko.mp3")
        gamble = [a1]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('ž'):
        a1 = pygame.mixer.Sound("Stiven/Žanko.mp3")
        a2 = pygame.mixer.Sound("Stiven/Žanko zaštanci.mp3")
        a3 = pygame.mixer.Sound("Stiven/Žiga.mp3")
        gamble = [a1, a2, a3]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('z'):
        a1 = pygame.mixer.Sound("Stiven/Zelo dobra muzika.mp3")
        gamble = [a1]
        am_channel.play(random.choice(gamble))
    if keyboard.is_pressed('right shift'):  # if key 'q' is pressed
        map = pygame.mixer.Sound(f"map.ogg")
        am_channel.play(map)
        print('Swiching to Štefan')
        menu = "kunfu"
while menu == "kunfu":
    if keyboard.is_pressed('¸'):
        kunfu = pygame.mixer.Sound("youtube_bmfudW7rbG0_audio.wav")
        am_channel.play(kunfu)
    if keyboard.is_pressed('right shift'):
        print('Swiching to Am')
        map = pygame.mixer.Sound(f"map.ogg")
        am_channel.play(map)
        menu = "am"
        break
