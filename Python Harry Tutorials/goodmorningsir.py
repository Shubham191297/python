import time

currentTime = time.strftime("%H:%M:%S")
currentHour = int(time.strftime("%H"))
currentMinute=int(time.strftime("%M"))
currentSecond=int(time.strftime("%S"))

if(currentHour>=0 and currentHour<12):
    print("Good morning sir!")
elif(currentHour>=12 and currentHour<16):
    print("Good afternoon sir!")
elif(currentHour>=16 and currentHour<8):
    print("Good evening sir!")
else:
    print("Good night sir!")