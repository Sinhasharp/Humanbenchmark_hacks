import pyautogui
import time

time.sleep(10)

# Define the RGB color to click on
target_color = (149, 195, 232)

# Define the interval between checks (in seconds)
check_interval = 0.01  # Decreased check interval for faster execution

# Flag to track if a click has been attempted in the current iteration
clicked_this_loop = False

while (True):
    try:
        # Get the screenshot of the defined area
        screenshot = pyautogui.screenshot(region=(432, 299, 1415 - 432, 869 - 299))

        # Find the location of the target pixel within the screenshot
        width, height = screenshot.size
        for x in range(width):
            for y in range(height):
                if screenshot.getpixel((x, y)) == target_color and not clicked_this_loop:
                    # Calculate the absolute coordinates based on the screenshot region
                    absolute_x = x + 432
                    absolute_y = y + 299

                    # Click on the pixel
                    pyautogui.click(absolute_x, absolute_y)
                    print(f"Clicked on pixel at ({absolute_x}, {absolute_y}) with RGB value {target_color}")
                    clicked_this_loop = True  # Mark click attempted
                    break

        # Reset click flag for next iteration
        clicked_this_loop = False

        # Wait for the defined interval before next check
        time.sleep(check_interval)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break