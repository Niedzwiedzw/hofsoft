import pyautogui, random


print('podaj liczbe')
c=int(input())
for i in range(0,c):
    a=random.randint(300,400)
    b=random.randint(300,400)


    pyautogui.click(a,b)
    i=1+1
