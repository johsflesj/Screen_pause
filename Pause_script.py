#20-20-20 eye rule
# The program notify the user to take a brake after watching the screen for 20 minutes.

import time, ctypes

x = 0

while x < 1:
    time.sleep(1200) #20 min = 1200 sec
    ctypes.windll.user32.MessageBoxW(0, "You have watched the screen for 20 minutes!\n" "Look at something 20 feet away for 20 seconds!", "Take a break, look away!")
    