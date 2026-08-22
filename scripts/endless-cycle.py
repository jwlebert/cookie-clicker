# /// script
# dependencies = [
#     "pyautogui",
#     "pynput",
# ]
# ///

from pynput import keyboard
import pyautogui
import subprocess
import time
import os

pyautogui.FAILSAFE = True

active = False
def on_press(key):
    global active

    if key == keyboard.Key.esc:
        print("Escape: exiting script.")
        os._exit(0)

    try:
        if key.char == 'q':
            print(f"Toggle: switching to {not active}")
            active = not active
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()