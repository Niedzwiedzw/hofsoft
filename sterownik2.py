#! python3

import pyperclip, pyautogui



kod=input()

kod.strip(" ♪ ")
kod.strip(' ')
kod2="$$$"+kod+"%%%"

pyperclip.copy(kod)
pyautogui.click(800,800)
pyautogui.typewrite(kod2, 0.025)

