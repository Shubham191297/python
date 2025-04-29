import pyttsx3 as pts
import time

fleetList = ["Gunju","Lalu","Thappa","Jeetu","Mali"]
t2sEngine = pts.init()

t2sEngine.setProperty('rate', 180)

for sre in fleetList:
    t2sEngine.say(f"Shoutout to {sre}. Great work!!")
    t2sEngine.runAndWait()
    time.sleep(1)
    
t2sEngine.say("Thank you guys for joining us today. Have a great day!")
t2sEngine.runAndWait()