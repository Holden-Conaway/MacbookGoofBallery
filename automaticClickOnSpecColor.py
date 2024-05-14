import pyautogui
from pynput.mouse import Controller, Button
import time

# Initialize the mouse controller
mouse = Controller()

# Define the target color (R, G, B)
target_color = (255, 0, 0)  # Example: Red color

# Define the tolerance for color matching
tolerance = 20

# Function to find the position of the target color on the screen
def find_color_position(target_color, tolerance):
    screen = pyautogui.screenshot()
    width, height = screen.size

    for x in range(width):
        for y in range(height):
            pixel_color = screen.getpixel((x, y))
            if (abs(pixel_color[0] - target_color[0]) <= tolerance and
                abs(pixel_color[1] - target_color[1]) <= tolerance and
                abs(pixel_color[2] - target_color[2]) <= tolerance):
                return (x, y)
    return None

# Main loop to search and click the color
while True:
    position = find_color_position(target_color, tolerance)
    if position:
        print(f"Found color at {position}")
        mouse.position = position
        mouse.click(Button.left, 1)
        time.sleep(1)  # Pause for 1 second after clicking
    else:
        print("Color not found")
    time.sleep(1)  # Pause for 1 second before next search
