import pyautogui

# Define initial color (RGB)
initial_color = (206, 38, 54)

# Define target color (RGB)
target_color = (75, 219, 106)
clk = 0

# Get initial color at position (optional - for verification)
# initial_color = pyautogui.screenshot(region=(1490, 301, 1, 1)).getpixel((0, 0))
# print('Initial color captured:', initial_color)  # Uncomment for verification

print('Running checks 5 times. Press Ctrl-C to quit.')

while (clk != 5):  # Loop 5 times
  # Capture a single pixel screenshot at the position
  current_color = pyautogui.screenshot(region=(1490, 301, 1, 1)).getpixel((0, 0))

  # Check if color changed to target
  if current_color != initial_color and current_color == target_color:
    print('Color changed to target, clicking!')
    pyautogui.click(1490, 301)  # Click at the position
    clk = clk + 1

print('\nAll checks done. Script completed.')
