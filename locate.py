#getintegra
import pyautogui, time, pyperclip, re

def getIntegra():
    integraIcon=pyautogui.locateOnScreen('integra.png')
    time.sleep(1)
    #print("Ikona integry: " + str(integraIcon))
    pyautogui.click(integraIcon[0], integraIcon[1])
    


def getHofsoft():
    hofsoftIcon=pyautogui.locateOnScreen('hofsoft.png')
    time.sleep(1)
    pyautogui.click(hofsoftIcon[0], hofsoftIcon[1])
    #print("Ikona hofsoftu: " + str(hofsoftIcon) + "\nOkno hofsoftu: " + str(hofsoftWindow))



def posIntegra():
    integraWindow=pyautogui.locateOnScreen('integrawin.png')
    return integraWindow
    
def posHofsoft():
    hofsoftWindow=pyautogui.locateOnScreen('hofsoftwin.png')
    return hofsoftWindow




#mapuj hofsoft
def mapujHofsoft():
    hofsoftTopLeft=pyautogui.locateOnScreen('hofsoftwin.png')
    hofsoftWorkspaceTopLeft=(hofsoftTopLeft[0], hofsoftTopLeft[1]+37)
    #hofsoftWorkspaceBottomRight=(pyautogui.locateOnScreen('hosfsoftbottomright.png')[0] + pyautogui.locateOnScreen('hosfsoftbottomright.png')[2], pyautogui.locateOnScreen('hosfsoftbottomright.png')[1] + pyautogui.locateOnScreen('hosfsoftbottomright.png')[3])
    hofsoftWorkspaceBottomRight=((hofsoftWorkspaceTopLeft[0]+1114),(hofsoftWorkspaceTopLeft[1]+854))
    return (hofsoftWorkspaceTopLeft,hofsoftWorkspaceBottomRight)

def zrzutHofsoft():

    mapa=mapujHofsoft()
    pyautogui.moveTo(mapa[0][0], mapa[0][1])
    time.sleep(0.5)
    pyautogui.mouseDown()
    pyautogui.dragTo(mapa[1][0], mapa[1][1], duration=0.2)
    time.sleep(0.5)
    pyautogui.mouseUp()
    return pyperclip.paste()

"""mapa=mapujHofsoft()
pyautogui.click(mapa[0][0], mapa[0][1])
pyautogui.dragTo(mapa[1][0], mapa[1][1], duration=0.5)
"""



            

getHofsoft()
print(zrzutHofsoft())

    

