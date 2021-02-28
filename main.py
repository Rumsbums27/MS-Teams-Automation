import pyautogui
import datetime
import random
import os

class Teams():
    def meeting(self, hours=int(), minutes=int(), latency=int(3)):
        time_latency = list()
        minutes -= latency

        for ltnc in range(latency * 2):
            time_latency.append(minutes + ltnc)

        accestime = random.choice(time_latency)
        time = datetime.time(hour=hours,minute=accestime)
        time = time.strftime("%H.%M")

        print(time)

        while True:
            now = datetime.datetime.now().strftime("%H.%M")
            if time == now:
                picture = pyautogui.locateCenterOnScreen(f'images/teams.PNG')
                pyautogui.moveTo(picture,duration=2)
                pyautogui.click(clicks=2,interval=0.1)
                break

if __name__ == '__main__':
    teams = Teams()
    hour = pyautogui.prompt(title='Hour',text='Please type the hour: ',default=0)
    minute = pyautogui.prompt(title='Minute', text='Please type the minute: ', default=0)
    latency = pyautogui.prompt(title='Latency', text='Please type the latency: ', default=3)
    teams.meeting(int(hour), int(minute), int(latency))