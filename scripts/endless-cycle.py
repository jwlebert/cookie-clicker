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
testing = False

def on_press(key):
    global active

    if key == keyboard.Key.esc:
        print("Escape: exiting script.")
        os._exit(0)

    try:
        if key.char == 'q':
            active = not active
            print(f"Toggle: switching to {active}")
        elif key.char == 'l':
            px, py = pyautogui.position()
            print(f"Position: ({px}, {py})")
        elif key.char == 't':
            if not testing:
                test()
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

LOCATIONS = {
    "buy_all": (1340, 180),
    "legacy": (1125, 100),
    "reincarnate": (710, 145),
    "cursor": (1225, 335),
    "next_building": (1225, 895),
}

def move_and_click(pos, shift=False):
    px, py = pos
    pyautogui.moveTo(px, py, duration=0.1)
    
    if shift: pyautogui.keyDown('shift')
    pyautogui.click()
    if shift: pyautogui.keyUp('shift')

listener = keyboard.Listener(on_press=on_press)
listener.start()

TOTAL_STEPS = 8
def step(s):
    if not (in_cookie_clicker() and (active or testing)): return False

    if s == 0 or s == 1:
        move_and_click(LOCATIONS['buy_all'])
        pyautogui.moveTo(*LOCATIONS['legacy'], 0.05) # move off of upgrade to collapse the upgrades
        move_and_click(LOCATIONS['cursor'], shift=True)
    elif s == 2 or s == 3:
        pyautogui.scroll(-10)
        move_and_click(LOCATIONS['next_building'], shift=True)
        # first time 'next_building' is "fractal engine", second time it's "You"
    elif s == 4:
        pyautogui.scroll(25)
    elif s == 5:
        move_and_click(LOCATIONS['buy_all'])
        time.sleep(1.0)
        pyautogui.click()
    elif s == 6:
        move_and_click(LOCATIONS['legacy'])
        pyautogui.press('enter')
        time.sleep(4)
    elif s == 7:
        move_and_click(LOCATIONS['reincarnate'])
        pyautogui.press('enter')
        time.sleep(1)
        
    return True

def test(num_cycles=5):
    global testing
    testing = True
    print(f"\n{'='*45}\n Starting {num_cycles}-Cycle Test\n{'='*45}")

    timings = []
    for i in range(1, num_cycles + 1):
        print(f"[Test] Cycle {i}/{num_cycles} starting...")
        start_time = time.time()

        for s in range(TOTAL_STEPS):
            while not in_cookie_clicker():
                time.sleep(0.5)
            step(s)
            time.sleep(1)

        duration = time.time() - start_time
        timings.append(duration)
        print(f"[Test] Cycle {i}/{num_cycles} completed in {duration:.2f}s")

    total = sum(timings)
    avg = total / len(timings)
    print(f"\n{'='*45}")
    print(f" Test Summary ({num_cycles} Cycles):")
    print(f"   Total:    {total:.2f}s")
    print(f"   Average:  {avg:.2f}s / cycle")
    print(f"   Fastest:  {min(timings):.2f}s | Slowest: {max(timings):.2f}s")
    print(f"   Timings:  {[f'{t:.2f}s' for t in timings]}")
    print(f"{'='*45}\n")

    testing = False

def start():
    print("Endless Cycle bot initialized.")
    print("Controls:")
    print("  [q]   Toggle loop on/off")
    print("  [t]   Run 5-cycle performance test")
    print("  [l]   Print current mouse position")
    print("  [Esc] Exit script\n")

    cur_step = 0
    while True:
        if testing:
            time.sleep(0.5)
            continue

        if active and step(cur_step):
            cur_step = (cur_step + 1) % TOTAL_STEPS

        time.sleep(1 if active else 0.2)

if __name__ == '__main__':
    start()