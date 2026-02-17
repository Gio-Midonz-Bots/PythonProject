import pyautogui as positionMouse
import pyautogui as timeslep

timeslep.sleep(1)
positionMouse.moveTo(612,1051)
timeslep.sleep(1)
positionMouse.click()
timeslep.sleep(1)
positionMouse.moveTo(711,154)
timeslep.sleep(1)
positionMouse.click()
timeslep.sleep(1)
positionMouse.typewrite('calc')
timeslep.sleep(1)
positionMouse.moveTo(740,337)
timeslep.sleep(1)
positionMouse.click()
print(positionMouse.position())
