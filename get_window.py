import pyautogui

# Continuously monitor and print mouse position
while True:
    x, y = pyautogui.position()
    print(f"Mouse position: x={x}, y={y}")