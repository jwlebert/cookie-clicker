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
test_requested = False

def on_press(key):
    global active, test_requested

    if key == keyboard.Key.esc:
        print("Escape: exiting script.")
        os._exit(0)

    try:
        if key.char == 'q':
            print(f"Toggle: switching to {not active}")
            active = not active
        elif key.char == 'l':
            px, py = pyautogui.position()
            print(f"Mouse position: ({px}, {py})")
        elif key.char == 't':
            if not test_requested:
                print("\n[Benchmark] Test hotkey pressed! Starting 5-ascension performance test...")
                test_requested = True
            else:
                print("\n[Benchmark] Test cancelled.")
                test_requested = False
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
    if not (in_cookie_clicker() and (active or test_requested)): return False

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

def run_benchmark(num_ascensions=5):
    global test_requested
    print(f"\n{'='*50}")
    print(f" Starting Performance Benchmark ({num_ascensions} Ascensions)")
    print(f"{'='*50}")

    durations = []
    for i in range(1, num_ascensions + 1):
        if not test_requested:
            print("[Benchmark] Aborted early.")
            break

        print(f"\n[Ascension {i}/{num_ascensions}] Starting cycle...")
        cycle_start = time.time()

        cur_step = 0
        while cur_step < TOTAL_STEPS:
            if not test_requested:
                break
            if not in_cookie_clicker():
                time.sleep(0.5)
                continue
            if step(cur_step):
                cur_step += 1
            time.sleep(1)

        if not test_requested:
            break

        cycle_duration = time.time() - cycle_start
        durations.append(cycle_duration)
        print(f"[Ascension {i}/{num_ascensions}] Completed in {cycle_duration:.2f}s")

    if durations:
        total_time = sum(durations)
        avg_time = total_time / len(durations)
        print(f"\n{'='*50}")
        print(f" Benchmark Results ({len(durations)}/{num_ascensions} Ascensions Completed):")
        print(f"   Total Time:           {total_time:.2f}s")
        print(f"   Average / Ascension:  {avg_time:.2f}s")
        print(f"   Fastest Ascension:    {min(durations):.2f}s")
        print(f"   Slowest Ascension:    {max(durations):.2f}s")
        print(f"   Individual Timings:   {[f'{d:.2f}s' for d in durations]}")
        print(f"{'='*50}\n")

    test_requested = False

def start():
    global test_requested
    print("Endless Cycle bot initialized.")
    print("Controls:")
    print("  [q]   Toggle continuous loop on/off")
    print("  [t]   Run 5-ascension benchmark test")
    print("  [l]   Print current mouse position")
    print("  [Esc] Exit script\n")

    cur_step = 0
    while True:
        if test_requested:
            run_benchmark(5)
            cur_step = 0
        elif active:
            if step(cur_step):
                cur_step = (cur_step + 1) % TOTAL_STEPS
            time.sleep(1)
        else:
            time.sleep(0.2)

if __name__ == '__main__':
    start()