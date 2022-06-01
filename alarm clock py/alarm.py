from datetime import datetime
from playsound import playsound

alarmH = int(input("Set the hour : "))
alarmM = int(input("Set the minute: "))
ampm = input("am or pm : ")

if ampm == "pm":
    alarmH+=12

    while True:
        if alarmH == datetime.now().hour and alarmM == datetime.now().minute:
            print("playing sound")
            playsound("coffee.mp3")
            
            break