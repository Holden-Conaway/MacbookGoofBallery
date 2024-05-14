import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from pynput.mouse import Controller, Button
import time

# Initialize the mouse controller
mouse = Controller()

# Get the game window (change the window title to match your game)
window_title = "Game Window Title"
game_window = gw.getWindowsWithTitle(window_title)[0]

# Function to capture the game window
def capture_game_window():
    # Get window coordinates
    left, top, right, bottom = game_window.left, game_window.top, game_window.right, game_window.bottom
    width, height = right - left, bottom - top
    
    # Capture the screen within the window bounds
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    
    # Convert screenshot to a format OpenCV can work with
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    return frame, (left, top)

# Function to find specific color (or object) within the screenshot
def find_color_position(frame, target_color, tolerance):
    mask = cv2.inRange(frame, 
                       np.array([c - tolerance for c in target_color]), 
                       np.array([c + tolerance for c in target_color]))
    coords = cv2.findNonZero(mask)
    if coords is not None:
        x, y = coords[0][0]
        return x, y
    return None

# Define the target color (BGR format) and tolerance
target_color = (0, 0, 255)  # Example: Red color in BGR
tolerance = 20

# Main loop to capture, search, and click
while True:
    frame, offset = capture_game_window()
    position = find_color_position(frame, target_color, tolerance)
    if position:
        x, y = position
        click_position = (offset[0] + x, offset[1] + y)
        print(f"Found color at {click_position}")
        mouse.position = click_position
        mouse.click(Button.left, 1)
        time.sleep(1)  # Pause for 1 second after clicking
    else:
        print("Color not found")
    time.sleep(1)  # Pause for 1 second before next search
