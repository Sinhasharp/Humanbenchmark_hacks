import pyautogui

print('Press Ctrl-C to quit.')
try:
  while True:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(positionStr, end='')  # Print without newline
    print('\b' * len(positionStr), end='', flush=True)  # Clear previous line
except KeyboardInterrupt:
  print('\n')
