# /// script
# dependencies = [
#     "pyautogui",
#     "pynput",
#     "Pillow",
#     "opencv-python",
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
        if key.char == 'l':
            px, py = pyautogui.position()
            print(px, py)
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

def get_asset(filename):
    """Builds an absolute path to a file in the ../assets directory."""
    # 1. Find the exact folder this python script is living in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Go up one level (..), into 'assets', and append the filename
    asset_path = os.path.join(script_dir, '..', 'assets', filename)
    
    # 3. Clean up the path (resolves the '..' into a proper absolute path)
    return os.path.abspath(asset_path)

def find_and_click(image_name, click_delay=0.5, double_move=False, shift=False):
    try:
        # confidence=0.8 allows for slight color/rendering differences
        # This is almost mandatory on macOS
        location = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)

        if double_move and location is not None:
            mac_x = location.x / 2
            mac_y = location.y / 2
            
            pyautogui.moveTo(mac_x, mac_y, duration=0.0)

            location = pyautogui.locateCenterOnScreen(image_name, confidence=0.8)
            
        if location is not None:
            # IMPORTANT MAC NOTE: 
            # Retina displays double the screen resolution. 
            # You usually have to divide the found coordinates by 2 to click the right spot.
            mac_x = location.x / 2
            mac_y = location.y / 2
            
            pyautogui.moveTo(mac_x, mac_y, duration=0.1)

            if shift: pyautogui.keyDown('shift')
            pyautogui.click()
            if shift: pyautogui.keyUp('shift')
            
            print(f"Successfully clicked {image_name}")
            time.sleep(click_delay)
            return True
        else:
            print(f"Could not see {image_name} on screen.")
            return False
            
    except Exception as e:
        print(f"Error finding {image_name}: {e}")
        return False

LOCATIONS = {
    "buy_all": (1340, 180),
    "legacy": (1125, 100),
    "reincarnate": (710, 145),
    "cursor": (1225, 335),
}

def move_and_click(pos, shift=False):
    px, py = pos
    pyautogui.moveTo(px, py, duration=0.1)
    
    if shift: pyautogui.keyDown('shift')
    pyautogui.click()
    if shift: pyautogui.keyUp('shift')

listener = keyboard.Listener(on_press=on_press)
listener.start()

TOTAL_STEPS = 10
def step(s):
    if not (in_cookie_clicker() and active): return False

    if s == 0 or s == 1:
        move_and_click(LOCATIONS['buy_all'])
        pyautogui.moveTo(*LOCATIONS['legacy'], 0.05) # move off of upgrade to collapse the upgrades
        move_and_click(LOCATIONS['cursor'], shift=True)
    elif s == 2:
        pyautogui.scroll(-10)
    elif s == 3: 
        find_and_click(get_asset("prism.png"), 0.2, shift=True)
        find_and_click(get_asset("fractal.png"), 0.2, shift=True)
    elif s == 4:
        pyautogui.scroll(-10)
    elif s == 5: 
        find_and_click(get_asset("you.png"), 0.2, shift=True)
    elif s == 6:
        pyautogui.scroll(25)
    elif s == 7:
        move_and_click(LOCATIONS['buy_all'])
        time.sleep(1.0)
        pyautogui.click()
    elif s == 8:
        move_and_click(LOCATIONS['legacy'])
        pyautogui.press('enter')
        time.sleep(4)
    elif s == 9:
        move_and_click(LOCATIONS['reincarnate'])
        pyautogui.press('enter')
        time.sleep(1)
        
    return True

def start():
    cur_step = 0
    while True:
        if step(cur_step):
            cur_step = (cur_step + 1) % TOTAL_STEPS
        time.sleep(1)

if __name__ == '__main__':
    start()