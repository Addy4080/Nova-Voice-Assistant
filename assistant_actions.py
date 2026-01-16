import pyautogui
import time
import webbrowser
import os

def send_whatsapp_message(contact, message):
    # Open WhatsApp desktop app
    os.system("start whatsapp:")
    time.sleep(8)  # wait for app to open

    # Open search (Ctrl + F works in WhatsApp Desktop)
    pyautogui.hotkey("ctrl", "f")
    time.sleep(1)

    # Type contact name
    pyautogui.write(contact, interval=0.1)
    time.sleep(2)
    pyautogui.press("enter")

    time.sleep(1)

    # Type message and send
    pyautogui.write(message, interval=0.05)
    pyautogui.press("enter")

WORK_MODE_ACTIONS = {
    "chrome": True,
    "vscode": True,
    "youtube": True,
    "chatgpt": True,
}

MOVIE_MODE = {
    "movie": True,
}

def start_work_mode():
    if WORK_MODE_ACTIONS.get("chrome"):
        os.system('start chrome --profile-directory="Profile 1"')
        time.sleep(2)

    if WORK_MODE_ACTIONS.get("vscode"):
        os.system("code")
        time.sleep(2)

    if WORK_MODE_ACTIONS.get("youtube"):
        webbrowser.open("https://www.youtube.com")

    if WORK_MODE_ACTIONS.get("chatgpt"):
        webbrowser.open("https://chatgpt.com")


def start_movie_mode():
    if MOVIE_MODE.get("movie"):
        os.system('start chrome --profile-directory="Default"')

        webbrowser.open("https://www.hotstar.com/in/home")
