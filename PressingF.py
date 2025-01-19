import ctypes
import time

# Windows API constants
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

def click_mouse():
    # Simulate mouse left button down
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # Simulate mouse left button up
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

try:
    print("Press Ctrl+C to stop the script.")
    while True:
        click_mouse()  # Simulate a left mouse click
        time.sleep(1)  # Wait 1 second between clicks
except KeyboardInterrupt:
    print("Script stopped.")
