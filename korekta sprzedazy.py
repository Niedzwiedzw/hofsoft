#! python3


#korekta sprzedaży

import pyautogui, time, sys
print("1. Przejdź do menu głównego Hofsoft\n2. Wróć do tego programu\n3. Zeskanuj kod i wciśnij [ENTER]")


kod=input()
a=0.5
kod.strip(" ♪ ")
kod.strip(' ')
kod2="$$$"+kod+"%%%"
pyautogui.click(800,800)
pyautogui.typewrite("31", 0.25)
time.sleep(2)
pyautogui.typewrite(kod2, 0.025)
time.sleep(2)

"""pyautogui.keyDown('shiftleft')

pyautogui.press('f10')

pyautogui.keyUp('shiftleft')

pyautogui.keyUp('f10')

"""

pyautogui.hotkey('shiftleft', 'f10')
pyautogui.hotkey('shiftleft', 'f10')
time.sleep(1)
pyautogui.hotkey('shiftleft', 'f10')
pyautogui.hotkey('shiftleft', 'f10')



time.sleep(1)
pyautogui.typewrite('01012015')
time.sleep(0.5)
pyautogui.keyDown('enter')
time.sleep(0.1)
pyautogui.keyUp('enter')
time.sleep(0.1)
pyautogui.keyDown('enter')
time.sleep(0.1)
pyautogui.keyUp('enter')
time.sleep(0.1)
pyautogui.keyDown('altleft')
time.sleep(0.1)
pyautogui.keyDown('tab')
time.sleep(0.1)
pyautogui.keyUp('altleft')
time.sleep(0.1)
pyautogui.keyUp('tab')
time.sleep(0.1)
print("wprowadz numer dokumentu")
numerd=input()
print("podaj typ dokumentu")
typ=input()

#powrot do menu
pyautogui.click(800,800)
time.sleep(1)

pyautogui.press('esc')
time.sleep(0.3)
pyautogui.press('esc')
time.sleep(0.3)
pyautogui.press('esc')
time.sleep(0.3)
pyautogui.press('esc')
time.sleep(0.3)
pyautogui.typewrite('841', 0.25)
time.sleep(0.3)
pyautogui.press('insert')
pyautogui.press('insert')
pyautogui.press('insert')
time.sleep(0.3)
pyautogui.press('insert')
time.sleep(0.3)

pyautogui.typewrite(typ, 0.25)
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.typewrite(numerd, 0.25)
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('enter')
time.sleep(0.3)
pyautogui.press('enter')
    



