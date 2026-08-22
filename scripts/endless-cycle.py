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
    
def get_active_app():
    """Asks macOS which application is currently active."""
    script = 'tell application "System Events" to get name of first application process whose frontmost is true'
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return ""

def in_cookie_clicker():
    return get_active_app() == "Cookie Clicker"

listener = keyboard.Listener(on_press=on_press)
listener.start()

TOTAL_STEPS = 2
def step(s):
    if not (in_cookie_clicker() and active): return False

    if s == 0:
        print("todo")   
    elif s == 1:
        print("todo 2")

    return True

cur_step = 0
while True:
    if step(cur_step):
        cur_step = (cur_step + 1) % TOTAL_STEPS
    time.sleep(1)