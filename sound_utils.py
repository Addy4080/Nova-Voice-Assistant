import pygame
import time
import os
import asyncio
import edge_tts
import pygame

def speak(text):
    print("Nova says:", text)

    async def _speak():
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-GB-RyanNeural"
        )
        await communicate.save("temp/Nova.mp3")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(_speak())
    loop.close()

    pygame.mixer.init()
    pygame.mixer.music.load("temp/Nova.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove("temp/Nova.mp3")

def play_beep():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/play.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.quit()

def play_stop_beep():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/stop.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.quit()

