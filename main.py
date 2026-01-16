import speech_recognition as sr
import webbrowser
import asyncio
import edge_tts
import os
import pygame
import time
from musicLibrary import getSongLink
from newsLibrary import get_news_titles
from assistant_actions import send_whatsapp_message, start_work_mode, start_movie_mode

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

def takeCommand():
    with sr.Microphone() as source:
        audio = r.listen(source)
        return r.recognize_google(audio)


def processCommand(c):
    print("COMMAND RECEIVED:", c)

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com/")
    elif "open ground" in c.lower():
        speak("Opening ground")
        webbrowser.open("https://www.G.round.com/")
    elif c.lower().startswith("play"):
        song, link = getSongLink(c)
        speak(f"Playing {song}")
        webbrowser.open(link)
        return
    elif "news" in c.lower():
        titles = get_news_titles()[:3]  # only top 3
        for title in titles:
            speak(title)
        return
    elif "send whatsapp message" in c.lower():
        speak("Whom should I message?")
        contact = takeCommand()

        speak("What should I say?")
        message = takeCommand()

        speak(f"Sending message to {contact}")
        send_whatsapp_message(contact, message)
        speak("Message sent")
        return
    elif "start work mode" in c.lower() or "work mode" in c.lower():
        speak("Starting your work mode")
        start_work_mode()
        speak("Work mode activated")
    elif "start movie mode" in c.lower() or "movie mode" in c.lower():
        speak("Starting your movie mode")
        start_movie_mode()
        speak("movie mode activated")

    else:
        speak("Sorry, I didn't understand that command")


if __name__ == "__main__":
    speak("Initializing Nova....")
    
    r = sr.Recognizer()
    
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=4, phrase_time_limit=20)

            word = r.recognize_google(audio)

            if "nova" in word.lower():
                speak("Yes Sir")

                with sr.Microphone() as source:
                    print("Nova Active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except Exception as e:
            print("Error;", e)
