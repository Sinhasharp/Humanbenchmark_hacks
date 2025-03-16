import threading
import time
import pyautogui
import math

time.sleep(10)
# Define center coordinates and radius
center_x, center_y = 960, 560
radius = 300

# Pre-calculate positions in a list
positions = []
for i in range(360):
    angle = math.radians(i)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    positions.append((x, y))


def move_cursor():
    # Move cursor to starting position (slightly above center) 3 seconds later
    time.sleep(3)
    pyautogui.moveTo(center_x, center_y - radius)


# Thread to move cursor 3 seconds before execution
cursor_thread = threading.Timer(3, move_cursor)
cursor_thread.start()

# Your main program logic here (e.g., send positions after delay)

# Wait for cursor thread to finish (optional)
# cursor_thread.join()
