from pynput.mouse import Listener

# Function to be called when a mouse click event occurs
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# Set up the listener
with Listener(on_click=on_click) as listener:
    print("Listening for mouse clicks. Press Ctrl+C to stop.")
    listener.join()
