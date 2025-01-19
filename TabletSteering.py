import pyautogui
import vgamepad
import time

# Initialize vgamepad
gamepad = vgamepad.VX360Gamepad()

# Screen and steering parameters
screen_width = pyautogui.size()[0]
neutral_zone = 10  # Dead zone to prevent jitter near center

def scale_to_analog(x, center_x, width):
    """
    Scale the x-coordinate to a range of -1 (left) to 1 (right).
    Includes a dead zone for no steering.
    """
    offset = x - center_x
    max_offset = width // 2  # Maximum distance from the center

    # Apply dead zone logic
    if abs(offset) < neutral_zone:
        return 0.0  # No steering

    # Scale the offset to the range -1 to 1
    scaled_value = offset / max_offset
    return max(-1.0, min(1.0, scaled_value))  # Clamp values to -1 and 1

def process_input():
    # Get the current pen (mouse) position
    x, _ = pyautogui.position()
    center_x = screen_width // 2

    # Convert position to analog joystick value
    analog_value = scale_to_analog(x, center_x, screen_width)

    # Update the virtual joystick
    gamepad.left_joystick_float(x_value_float=analog_value, y_value_float=0.0)
    gamepad.update()

try:
    print("Running analog steering script. Move your pen to steer.")
    while True:
        process_input()
        time.sleep(0.01)  # Small delay for smoother updates
except KeyboardInterrupt:
    print("\nScript terminated. Resetting joystick...")
    gamepad.reset()
    gamepad.update()

