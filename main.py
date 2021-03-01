import pyautogui
import datetime
import random
import os
import time


class Teams():
    def meeting(self):
        for filename in os.listdir('./images'):
            if filename.startswith('meeting_'):
                print(filename)
                date = filename.split('_')[1]
                date = date.split('-')
                time_latency = list()

                hours = int(date[0])
                minutes = int(date[1])
                latency = date[2]
                latency = int(latency.split('.')[0])

                minutes -= latency

                for ltnc in range(latency * 2):
                    time_latency.append(minutes + ltnc)

                accesstime = random.choice(time_latency)
                start_time = datetime.time(hour=hours, minute=accesstime)
                start_time = start_time.strftime("%H.%M")

                print(start_time)

                while True:
                    now = datetime.datetime.now().strftime("%H.%M")

                    if start_time == now:
                        start_teams = pyautogui.locateCenterOnScreen('images/settings/teams.PNG')
                        pyautogui.moveTo(start_teams, duration=1)
                        pyautogui.click(clicks=2, interval=0.1)

                        time.sleep(4)

                        maximise = pyautogui.locateCenterOnScreen('images/settings/maximise.PNG')

                        if maximise is not None:
                            pyautogui.moveTo(maximise, duration=1)
                            pyautogui.click()

                            time.sleep(3)

                        calendar = pyautogui.locateCenterOnScreen('images/settings/calendar.PNG')

                        if calendar is not None:
                            pyautogui.moveTo(calendar, duration=1)
                            pyautogui.click()

                            time.sleep(3)

                        file = pyautogui.locateCenterOnScreen(f'images/{filename}')
                        if file is not None:
                            pyautogui.moveTo(file, duration=1)
                            pyautogui.click()

                            time.sleep(3)

                        access = pyautogui.locateCenterOnScreen('images/settings/access.PNG')
                        pyautogui.moveTo(access, duration=1)
                        pyautogui.click()

                        time.sleep(3)

                        cam = pyautogui.locateCenterOnScreen('images/settings/cam.PNG')
                        mic = pyautogui.locateCenterOnScreen('images/settings/mic.PNG')
                        if cam:
                            pyautogui.moveTo(cam, duration=1)
                            pyautogui.click()

                            time.sleep(3)

                        if mic:
                            pyautogui.moveTo(mic, duration=1)
                            pyautogui.click()

                            time.sleep(3)

                        now_access = pyautogui.locateCenterOnScreen('images/settings/now_access.PNG')
                        pyautogui.moveTo(now_access, duration=1)
                        pyautogui.click()
                        break


if __name__ == '__main__':
    teams = Teams()
    teams.meeting()
