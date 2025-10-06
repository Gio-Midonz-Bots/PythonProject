import pyautogui as timeslep
import pyautogui as positionMouse
import os
timeslep.sleep(1)
os.system('start chrome')
timeslep.sleep(1)


positionMouse.moveTo(662,334)
timeslep.sleep(1)
positionMouse.click()
timeslep.sleep(1)
positionMouse.moveTo(706,578)
timeslep.sleep(1)
positionMouse.click()
timeslep.sleep(1)
positionMouse.moveTo(470,77)
timeslep.sleep(1)
positionMouse.click()
timeslep.sleep(1)
positionMouse.typewrite('google')
timeslep.sleep(4)
positionMouse.moveTo(517,123)
timeslep.sleep(1)
positionMouse.click()
timeslep.sleep(6)
positionMouse.moveTo(661,450)
timeslep.sleep(1)
positionMouse.click()
positionMouse.typewrite('dolar de hoje')
timeslep.sleep(1)
positionMouse.press("enter")
print(positionMouse.position())


